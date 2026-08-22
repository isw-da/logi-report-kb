# RMI and the Remote Server API

Logi Report Server uses Java RMI for everything distributed: clustering, the event system,
the Remote API and the monitoring system. If your code runs in a different JVM or on a
different machine from the server, this is the transport.

Primary sources: [Using RMI in Logi Report Server (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741415368343-using-rmi-in-logi-report-server.md)
and [Java API for an Application (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741394666391-java-api-for-an-application.md).
Era: `logi-report-v17-v19`.

## Local and remote differ only at the first call

The Server API starts a server inside your own JVM. The Remote Server API connects to one
already running, locally in another JVM or on another machine. After the first call the
rest of the API is identical, which is what makes it practical to write code that tries
remote first and falls back to local.

Local:

```java
System.getProperties().put("reporthome", "C:\\LogiReport\\Server");
HttpUtil.initEnv(System.getProperties());
RptServer server = HttpUtil.getHttpRptServer();
```

Remote:

```java
System.getProperties().put("reporthome", "C:\\LogiReport\\Server");
System.getProperties().put("jrs.rmi.auth_file", "C:\\LogiReport\\Server\\bin\\rmi.auth");
String host = "localhost";
String port = "1129";
RptServer server = RemoteReportServerToolkit.getRemoteWrappedRptServer(host, port);
```

Port 1129 is the default in the corpus's own example. `reporthome` is needed remotely for
logging and to locate `rmi.auth`.

Note: the v19 source for the remote snippet contains an editing artefact (a stray
`:diffupdate` token mid-assignment). The method call is
`RemoteReportServerToolkit.getRemoteWrappedRptServer(host, port)`; the snippet above is the
corrected form.

## Universal remote object management

Objects are not bound to the RMI registry directly. Getting a remote object, on a local or
remote server or from a third-party application through the Remote API, means requesting it
from the remote object management system, and authentication happens before the request is
processed. The stated reason for the design is that registry-bound remote objects are both
a security risk and unmanageable.

## The authentication file

`<install_root>\bin\rmi.auth` is generated during server installation. Move it somewhere
safe afterwards if you want to protect it.

Where it must match:

- **Server**: read from `<server_install_root>\bin`.
- **Cluster**: every clustered server must hold the same file. Adding a server with a
  different one means backing that one up and copying a clustered server's file into
  `<server_install_root>\bin`.
- **Server Monitor**: copy the file into `<monitor_install_root>\bin`, from which Monitor
  builds an `authInfo` object.
- **Remote API**: specify it when launching your application.

```
java -cp ... -Djrs.rmi.auth_file=%authFileName% mainClass
java -cp ... -Djrs.rmi.auth_string=my_auth_info mainClass
```

Lookup order is `-Djrs.rmi.auth_string`, then `-Djrs.rmi.auth_file`, then
`<monitor_install_root>\bin`; the first hit is used. The content can be any bytes, as long
as local and remote match, so an arbitrary agreed string works. You can also generate a
file with `RMIAuthFileCreator.bat` in `<server_install_root>\bin`, or write one by hand.

## Remote classes and methods the corpus names

| Purpose | Class | Methods |
| --- | --- | --- |
| Remote server access | `jet.server.api.rmi.RemoteReportServerToolkit` | `getRemoteRptServer()`, `runTask()`, `getResourceManager()`, `getRemoteFileService()` |
| Fetch output back to the client | `jet.server.api.RemoteReportServerToolkit` | `getRemoteFileService()`, `copyFromRemote()` |
| Cluster dispatch | `jet.server.api.rmi.RemoteDispatcher` | `RemoteDispatcher()` |

The remote file service exists for the case where a report runs on a remote server and the
exported PDF or Excel file has to be opened on the client machine. Reports can be run
asynchronously using the timeout option.

Source: [Tour of the Java API (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741408065175-tour-of-the-java-api.md).

## Running the demos

Samples are in `<install_root>\help\samples\APIRemoteServer`:

- `RemoteAPIDemoFileService.java`, using a remote server
- `RemoteAPIDemoPublishRpt.java`, scheduling to version, disk or email
- `RemoteAPIDemoRunAndExportReport.java`, running and exporting to other formats
- `RemoteAPIDemoRunReportWithTimeout.java`, marking a run as a large report by setting a
  timeout and returning large-report information

Three things must be true first:

1. `server.rmiserver.enable` set to `true` in `<install_root>\bin\server.properties`.
2. `-Djrs.rmi.auth_file="%authFileName%"` on the command line.
3. Classpath containing `JRESServlets.jar`, `JREngine.jar`, the servlet jar, log4j and
   `sac-1.3.jar`.

Source: [RMI Demos (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741363379863-rmi-demos.md).

## Classpath for remote calls

Calling the Server API by RMI from another JVM uses `JRSRMI.jar` rather than the local
`JRESServlets.jar` plus `JREngine.jar` pair. Note the v19 RMI Demos article and the v19
Installing the Server API article disagree on this point, the demos article listing the
local jars. Prefer the installing article for the remote case, and see
[server-api.md](server-api.md) for the full lists.

## SSO does not apply over RMI

Access to a dedicated back end server goes over RMI, which uses neither `checkLogin()` nor
single sign-on for access control. See [security-api.md](security-api.md).

## Era note

The v15 article, [Using RMI in Logi JReport Server](../docs/jreport-v15-v16/working-with-apis-logi-jreport-server-v15/1500009668761-using-rmi-in-logi-jreport-server-guide-v15-server.md),
covers the same authentication file mechanism under the old product name. The jar list
differs by era in the same way as the rest of the Server API (javax.servlet in v15,
jakarta.servlet in v19).
