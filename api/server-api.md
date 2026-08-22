# Server API (jet.* Java classes)

The Server API is a set of Java interfaces that run reports, explore report resources and
provide access control for Logi Report Server. You use it to write servlets, JSPs and
plain Java applications.

Primary source: [Using Server API to Work with Logi Report Server (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741407944855-using-server-api-to-work-with-logi-report-server.md)
and [Tour of the Java API (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741408065175-tour-of-the-java-api.md).
Era: `logi-report-v17-v19`. The v15 equivalents are
[Logi JReport Server API](../docs/jreport-v15-v16/working-with-apis-logi-jreport-server-v15/1500009668121-logi-jreport-server-guide-v15-server-api.md)
and [Tour of the Java API (v15)](../docs/jreport-v15-v16/working-with-apis-logi-jreport-server-v15/1500009668401-tour-of-the-java-api.md).

## Every program starts the same way

Two methods on `jet.server.api.http.HttpUtil` must be called before anything else:

- `HttpUtil.initEnv()` starts the singleton server on this machine, or does nothing if
  one is already running.
- `HttpUtil.getHttpRptServer()` connects and returns a handle for later calls.

```java
System.getProperties().put("reporthome", "C:\\LogiReport\\Server");
HttpUtil.initEnv(System.getProperties());
RptServer server = HttpUtil.getHttpRptServer();
```

Inside a servlet container the handle is an `HttpRptServer`, which also knows the HTTP
request, the HTTP response and the servlet session. The servlet session is where the
engine holds Logi Report state between requests.

Source: [Java API for an Application (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741394666391-java-api-for-an-application.md),
[Java API for a Servlet (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741408671639-java-api-for-a-servlet.md).

## Resource paths

Paths passed to the API follow the server resource tree, not the file system:

- Public Reports starts with `/`, so `/Public Reports/SampleReports` is written `/SampleReports`.
- My Reports starts with `/USERFOLDERPATH/<username>/`, so Jim's Shipments folder is
  `/USERFOLDERPATH/Jim/Shipments`.

Source: [Using the Server API (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741394799255-using-the-server-api.md).

## The functional areas, with the classes the docs name

Taken from the v19 tour. Each entry names the class or interface and the methods the
prose calls out. Anything not listed here is not documented in this corpus.

| Area | Class or interface | Methods named |
| --- | --- | --- |
| Initialise and connect | `jet.server.api.http.HttpUtil` | `initEnv`, `getHttpRptServer`, `checkLogin`, `getParameters`, `getUser`, `decodeEsc` |
| Run and export | `jet.server.api.RptServer` | `runReport`, `exportResult` |
| Schedule | `jet.server.api.RptServer` | `submitScheduledTask` |
| Triggers | `jet.server.api.TriggerManager` | `subScheduledTask`, `fire` |
| Resource management | `jet.server.api.ResourceManager` | `createFolder`, `addResource`, `addResourcesToFolder`, `removeNode`, `removeVersion`, `getReportsInPath`, `getResultsInPath`, `checkBasePermission` |
| Authorisation | `jet.server.api.Authenticator` | `isValidUser`, `isPermissionOK`, `isValidAdminUser` |
| Security administration | `jet.server.api.admin.SecurityAdminService` | `addRole`, `addGroup`, `addUser` |
| Event framework | `jet.server.api.TaskListener` | `beforeRun`, `afterRun`, `validateParameter` |
| Engine, no server | `jet.server.api.engine.ReportEngine` | `ReportEngineFactory.getInstance`, `setReportHome`, `runReport`, `exportToPDF` |
| NLS | `jet.util.NLSBundleInfo` | `NLSBundleInfo` |
| Remote file service | `jet.server.api.RemoteReportServerToolkit` | `getRemoteFileService`, `copyFromRemote` |
| RMI | `jet.server.api.rmi.RemoteReportServerToolkit` | `getRemoteRptServer`, `runTask`, `getResourceManager`, `getRemoteFileService` |
| Cluster dispatch | `jet.server.api.rmi.RemoteDispatcher` | `RemoteDispatcher` |
| Load balancing | `jet.server.api.cluster.LoadBalancer` | `selectMember` |

Packages named without a method list: `jet.server.api.admin.cfg` (server configuration),
`jet.server.api.monitor` (Server Monitor), `jet.server.api.profiling` (JMX profiling),
`jet.server.api.crd` (cached report data).

`RptServer` is documented as a Java interface but is not meant to be reimplemented. Treat
it as a class.

Source: [Tour of the Java API (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741408065175-tour-of-the-java-api.md).

## Worked example: schedule a report to disk as PDF

```java
RptServer server = HttpUtil.getHttpRptServer();

Properties props = new Properties();
props.put(APIConst.TAG_TASK_CLASS, APIConst.TASK_TO_RPT);
props.put(APIConst.TAG_LAUNCH_TYPE, String.valueOf(APIConst.IMMEDIATELY));
props.put(APIConst.TAG_CATALOG, "/SampleReports/SampleReports.cat");
props.put(APIConst.TAG_REPORT, "Employee Information List.cls");
props.put(APIConst.TAG_TO_DISK, "true");
props.put(APIConst.TAG_TO_PDF, "true");
props.put(APIConst.TAG_PDF, "Employee Information List.cls.pdf");
props.put(APIConst.TAG_PDF_DIR, "/SampleReports");
props.put(APIConst.TAG_REPORT_LANGUAGE, "en_US");

String taskID = server.submitScheduledTask("admin", props);
CompletedTaskTable completeTable = server.getCompletedTaskTable();
server.shutdown();
```

Every schedule property is a constant on `jet.cs.util.APIConst`. The runnable version is
`APIDemoPublishRpt.java` in `<install_root>\help\samples\APIServer`.

Source: [Scheduling a Report Task (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741386712599-scheduling-a-report-task.md).

## Worked example: schedule on a trigger you fire yourself

```java
RptServer svr = RemoteReportServerToolkit.getRemoteWrappedRptServer("127.0.0.1", "1129");
TriggerManager trigMan = svr.getTriggerManager();
String exTriggerName = "exTriggerDemo";
if (!trigMan.contains(exTriggerName)) {
    trigMan.createTrigger(exTriggerName, "an external trigger demo");
}

Properties props = new Properties();
props.put(APIConst.TAG_TASK_CLASS, APIConst.TASK_TO_RPT);
props.put(APIConst.TAG_LAUNCH_TYPE, String.valueOf(APIConst.IMMEDIATELY));
props.put(APIConst.TAG_TRIGGERS_LOGIC, "ONLY");
props.put(APIConst.TAG_TRIGGERS_ARRAY, "exTriggerDemo");
props.put(APIConst.TAG_CATALOG, "/SampleReports/SampleReports.cat");
props.put(APIConst.TAG_REPORT, "/SampleReports/Payroll Report.cls");
props.put(APIConst.TAG_TO_VERSION, "true");
props.put(APIConst.TAG_TO_VERSION_PDF, "true");

String taskID = svr.submitScheduledTask("admin", props);
trigMan.fire(exTriggerName, new Properties());
```

Same source. The runnable version is `DemoTrigger.java`.

## Worked example: advanced run, then export

Run to PDF straight to a disk path:

```java
Properties props = new Properties();
props.put(APIConst.TAG_RESULT_TYPE, String.valueOf(APIConst.PDF));
props.put(APIConst.TAG_RESULT_LOCATION_TYPE,
          String.valueOf(APIConst.TAG_LOCATION_TO_SERVER_DISK_REAL_PATH));
props.put(APIConst.TAG_RESULT_LOCATION, "C:\\");
tempResult = rptServer.runReport(user, catalog, rptName, props);
```

Run to an RST result, then export that result to HTML:

```java
props.put(APIConst.TAG_RESULT_TYPE, String.valueOf(APIConst.RST));
props.put(APIConst.TAG_RESULT_LOCATION_TYPE, "0");
props.put(APIConst.TAG_RESULT_LOCATION, "/");
String tempResult = server.runReport("admin", catalog, rptName, props);

props.put(APIConst.TAG_HTML, "Crosstab");
props.put(APIConst.TAG_HTML_DIR, "/");
props.put(APIConst.TAG_HTML_DIR_TYPE,
          String.valueOf(APIConst.TAG_LOCATION_TO_SERVER_RESOURCE_PATH));
ExportedFileList fileList = server.exportResult("admin", tempResult, props);
```

`TAG_LOCATION_TO_SERVER_RESOURCE_PATH` is 0 and `TAG_LOCATION_TO_SERVER_DISK_REAL_PATH`
is 1. The default for `TAG_RESULT_LOCATION_TYPE` is 1.

Source: [Advanced Running Reports Using the On-Demand API (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741400530711-advanced-running-reports-using-the-on-demand-api.md).
The v15 article on the same subject is [Specifying Paths for the Result Files When Using On-Demand API](../docs/jreport-v15-v16/working-with-apis-logi-jreport-server-v15/1500009668721-specifying-paths-for-the-result-files-when-using-on-demand-a.md).

## Running a report with your own JDBC connection

Put a `java.sql.Connection` object under the key `jrs.jdbc_connection_object`. The
property is accepted by three `jet.server.api.RptServer` methods: `runReport()`,
`runReportNotWaitResult()` and `submitScheduledTask()`.

Source: [URL Properties for Running, Scheduling and Viewing Reports via URL (v19)](../docs/logi-report-v17-v19/working-on-logi-report-server-via-url-logi-report-server-v19/5741464843927-url-properties-for-running-scheduling-and-viewing-reports-vi.md).

## Engine API: reporting without a server

`jet.server.api.engine.ReportEngine` runs reports directly inside your application with no
server instance. The docs are explicit about the trade: you give up Page Report Studio,
security and scheduling. Sample: `APIServer\APIDemoReportEngine.java`. See also
[Creating and Getting Instances of Report Engine and Logi Report Server (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741400342295-creating-and-getting-instances-of-report-engine-and-logi-rep.md).

## Installing and classpath

The Server API installs with the server. Classes live in `JRESServlets.jar`. Local calls
need `JRESServlets.jar` and `JREngine.jar` plus the servlet, logging, hsqldb, sac,
commons-logging, quartz and DBMS driver jars. Remote RMI calls need `JRSRMI.jar` instead
of the local pair. Designer ships a server too, at `<designer_install_root>\server\lib`.

Era difference worth knowing: v15 lists `javax.servlet-api-3.1.0.jar`, `hsqldb-2.3.4.jar`,
`log4j-*-2.7.jar`, `quartz-all-2.2.3.jar` and `commons-codec-1.2.jar`. v19 lists
`jakarta.servlet-4.0.4.jar`, `hsqldb-2.6.1.jar`, `log4j-*-2.17.2.jar` and
`quartz-2.3.2.jar`, and drops commons-codec. The javax to jakarta move is the one that
will break a v15-era build against a v19 server.

Sources: [Installing the Server API (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741363396375-installing-the-server-api.md),
[Installing the Server API (v15, Logi JReport)](../docs/jreport-v15-v16/working-with-apis-logi-jreport-server-v15/1500009643642-installing-the-server-api.md),
and the unversioned [Installing the Server API](../docs/unversioned/server-api/1500009686182-installing-the-server-api.md).

## Related task articles in the v19 set

[Applying TaskListener](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741395089175-applying-tasklistener.md),
[Scheduling a Customized Task Using User Task](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741400624023-scheduling-a-customized-task-using-user-task.md),
[Working with Resource Versions](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741386771735-working-with-resource-versions.md),
[Publishing Resources from One Server to Another](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741400553623-publishing-resources-from-one-server-to-another.md),
[Dynamic Connection API](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741408239895-dynamic-connection-api.md),
[Using the NLS API](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741408431895-using-the-nls-api.md),
[API Demos](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741407991063-api-demos.md).

## Dynamic Connection API in one paragraph

`jet.server.api.admin.AdminService.getDynamicConnectionManager()` returns a
`DynamicConnectionManager` with `addDynamicConnection()`, `updateDynamicConnection()` and
`removeDynamicConnection()`. At run time the server asks a `DynamicConnectionProvider` for
connections for every data source used, then the engine merges those properties over the
catalog's own. To source connections from your own system, implement
`jet.server.api.dynamiccon.DynamicConnectionProvider` and register it with the
`server.custom.DynamicConnectionProvider` property in `<install_root>\bin\server.properties`.
