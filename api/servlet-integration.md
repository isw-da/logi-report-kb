# Servlet integration

How Logi Report Server sits inside a Java web application: what the shipped servlets and
JSP pages are, how your code reaches the server from inside a servlet container, and how to
package the server into a WAR or EAR.

Primary sources: [Technical Architecture (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741408039575-technical-architecture.md)
and [Java API for a Servlet (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741408671639-java-api-for-a-servlet.md).
Era: `logi-report-v17-v19`.

## Three layers

- JSP files that generate the interactive web pages of the Server Console, under
  `<install_root>\public_html\jinfonet`, `\dhtmljsp`, `\admin` and `\javascript`.
- Compiled servlets that perform running, scheduling and viewing, driven by query
  parameters.
- The Java API, `JREngine.jar` and the rest of `<install_root>\lib`, which the JSPs and
  servlets themselves call.

The shipped JSP pages are production-ready and have visible source, so they double as
worked examples of the Java API. Adding reporting to an existing application can be as
little as linking to them. Because the servlets are called by URL, the calling application
can be .NET, static HTML, anything.

## Getting the server handle inside a servlet

```java
System.getProperties().put("reporthome", "C:\\LogiReport\\Server");
HttpUtil.initEnv(System.getProperties());
HttpRptServer httpRptServer = HttpUtil.getHttpRptServer();
if (httpRptServer == null) {
    return; // handle the failure
}
```

All programs in one JVM share a single server instance; a request either starts it or
connects to the running one. `HttpRptServer` knows the HTTP request, the HTTP response and
the servlet session, and the servlet session is where Logi Report state is kept between
requests.

The parameterless `getHttpRptServer()` only works when your code and the server share a
JVM. The v19 article flags this as not the portable form and points at an overload for code
that must work in every configuration. For a different JVM or machine, see [rmi.md](rmi.md).

## Helper methods for servlet work

```java
String cat = request.getParameter(APIConst.TAG_CATALOG);
String rptName = request.getParameter(APIConst.TAG_REPORT);

Properties ht = HttpUtil.getParameters(request);   // URL params into a Properties
String user = HttpUtil.getUser(request);           // empty string if no Logi Report user
String rescPath = HttpUtil.decodeEsc(request.getParameter(APIConst.TAG_PATH)); // %HexHex

HttpRptServer httpRptServer = HttpUtil.getHttpRptServer();
String rst = httpRptServer.runReport(user, cat, rptName, ht);
```

`getParameters()` flattens a multi-valued parameter from a vector of strings into a single
delimiter-separated string.

Every JSP page and servlet in the product checks that the requester is an authenticated
Logi Report user before running. See [security-api.md](security-api.md) for `checkLogin()`
and single sign-on.

## The servlet classes

From the `web.xml` sample in the integration guide:

| Servlet name | Class |
| --- | --- |
| `jrserver` | `jet.server.servlets.JRServlet` |
| `sendfile` | `jet.server.servlets.SendFileServlet` |
| `dhtml` | `jet.web.dhtml.DHTMLlet` |

Plus the context listener `jet.server.servlets.JRServerContextListener`.

Source: [Four Ways of Integrating Logi Report Server (v19)](../docs/logi-report-v17-v19/logi-report-server-integration-logi-report-server-v19/5741453049495-four-ways-of-integrating-logi-report-server.md).

## Four packaging routes

1. Build a Logi Report Server WAR (for example `jreport.war`, containing `WEB-INF/web.xml`,
   `lib/`, `admin/`, `jinfonet/` and `dhtmljsp/`).
2. Build a Logi Report Server EAR.
3. Build your own WAR and embed a self-contained server inside it.
4. Build your own EAR and embed a self-contained server inside it.

See also [Building a WAR/EAR File to Include a Self-contained Logi Report Server (v19)](../docs/logi-report-v17-v19/logi-report-server-integration-logi-report-server-v19/5741473837719-building-a-war-ear-file-to-include-a-self-contained-logi-rep.md)
and [Integrating Remote Logi Report Server (v19)](../docs/logi-report-v17-v19/logi-report-server-integration-logi-report-server-v19/5741473756311-integrating-remote-logi-report-server.md).

## reporthome in a Java EE container

Setting `reporthome` and other server properties inside an application server is its own
problem, covered by
[Setting Server Reporthome and Properties in a Java EE Environment (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741400319639-setting-server-reporthome-and-properties-in-a-java-ee-enviro.md)
and [Specifying Reporthome for Logi Report Server in a Java EE Environment (v19)](../docs/logi-report-v17-v19/logi-report-server-integration-logi-report-server-v19/5741467928983-specifying-reporthome-for-logi-report-server-in-a-java-ee-en.md).

## Application servers with named instructions

The v19 integration set has a page per target: Tomcat, WebLogic 14.1.1, IBM WebSphere
9.0.5.6, JBoss EAP, WildFly, Jetty, Resin, GlassFish Open Source Edition 5.0, and Sun Java
System Application Server. Start from
[Deploying Logi Report Server to a Java Application Server (v19)](../docs/logi-report-v17-v19/logi-report-server-integration-logi-report-server-v19/5741431629463-deploying-logi-report-server-to-a-java-application-server.md).
An unversioned copy of the same set, with slightly different version numbers, is at
[Deploying Logi Report Server to a Java Application Server (unversioned)](../docs/unversioned/deploying-logi-report-server-to-a-java-application-server/1500009748402-deploying-logi-report-server-to-a-java-application-server.md).

## Do not confuse this with Server Monitor integration

[Integrating with a Servlet-Enabled Web Server (unversioned)](../docs/unversioned/integrating-with-a-servlet-enabled-web-server/1500009711721-integrating-with-a-servlet-enabled-web-server.md)
is about deploying **Logi Report Server Monitor**, not the server, and it still uses the
Logi JReport name and much older container versions (Tomcat 8.0.15, WebLogic 12c,
WebSphere 8.5.3.3). Its advice is that Monitor belongs on a separate system from the server.

## Era note

The three-layer architecture (JSP pages, servlets, Java API) and the `HttpUtil` entry points
are the same in the v15 Logi JReport documentation; see
[Java API for a Servlet (v15)](../docs/jreport-v15-v16/working-with-apis-logi-jreport-server-v15/1500009644182-java-api-for-a-servlet.md).
The container versions in the deployment pages are the part that moves between eras, along
with the javax to jakarta servlet API change described in [server-api.md](server-api.md).
