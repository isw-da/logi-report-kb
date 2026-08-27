# Logi Report programmable surface — index

Source: this repo's own corpus, 13,235 articles. 411 articles sit in a
`working-with-apis-*` section, 79 in a `*-via-url-*` section and 154 in a
`*-integration-*` section, spread across four eras. Per-surface detail with worked
examples: [`api/`](api/). Task-based routing: [`api/README.md`](api/README.md).

Logi Report is organised by class and method rather than by HTTP verb, so this index
is keyed on package, class and entry point. Every claim below carries the doc path it
came from, relative to this repo root. Where the corpus does not answer something the
entry says so rather than guessing.

**No Javadoc is mirrored here.** The complete class reference ships on the install at
`<install_root>\help\api`
(`docs/current/v26/working-with-apis-report-server/45203869669005-tour-of-the-java-api.md`).
Class and method names in this file are only those the prose names.

## A REST API exists, and an early version of this index said it did not

`docs/current/v26/working-with-apis-report-server/45203895093901-using-javascript-api-to-embed-server-console-and-reports-in-your-applications.md`,
line 36: "Report provides modularized RESTful Web APIs for the Server Console so that
you can call these APIs to set up a similar server console as the Report Server Console
in your applications on any platforms such as JavaScript, Java, .NET, and C++ ... Report
develops Web API definition using openAPI as the specification."

Three things make this easy to miss, and all three have caught someone before:

- No document is titled "REST API" or "RESTful Web Service". The surface is documented
  inside an article whose title says JavaScript.
- The openAPI definition is not published on the web. It ships on disk at
  `<install_root>\help\webapi\logireportserver.yaml`, and the rendered docs are served
  by a running server at
  `http://localhost:8888/servlet/sendfile/help/webapi/webapi-docs/index.html`
  (same file, line 38). A probe of `/jinfonet/api` or `/jinfonet/rest` returns 404
  because neither is the path.
- Most REST and SOAP articles in the corpus really are about Logi Report *consuming* a
  REST or SOAP data source, which makes a keyword sweep look conclusive when it is not.

Nine files document it:
`docs/jreport-v15-v16/working-on-logi-jreport-server-via-urls-logi-jreport-server/1500009686122-embedding-logi-jreport-with-javascript-apis.md`,
one in v23-v25, one in v26, four in v17-v19 (two of them release notes) and one in
`docs/unversioned/`. Detail: [`api/rest-web-api.md`](api/rest-web-api.md).

## At a glance

| Family | Primary entry point | Separate licence key? | v26 | v23-v25 | v17-v19 | v15-v16 |
|---|---|---|---|---|---|---|
| Design API | `Designer`, `MultipliedDesigner` | **Yes** | 12 | 26 | 49 | 21 |
| Catalog API | `jet.api.MultipliedCatalogAPI` | **Yes** (Design API key) | 9 | 19 | 35 | 15 |
| Server API (Java) | `jet.server.api.RptServer` | No | 29 | 36 | 79 | 38 |
| Java API for servlets | `jet.server.api.http.HttpUtil` | No | 7 | 7 | 18 | 8 |
| JavaScript viewer API | `jreportapi.js`, global `J$VM` | No | 5 | 17 | 29 | 7 |
| RESTful Web API | `logireportserver.yaml` | No | 1 | 1 | 5 | 1 |
| URL invocation | `jrs.cmd` query parameter | No | 9 | 10 | 26 | 25 |
| Servlet integration | `jet.server.servlets.JRServlet` | No | 18 | 19 | 41 | 24 |

Counts are files per era whose body mentions the family name (for URL invocation and
servlet integration, files in the matching section directory). They measure coverage,
not surface size.

**Every family is present in v15-v16.** Nothing in the list above appeared after the
JReport era. What changed is packaging, dependencies and platform, covered under
[v16 to v26, what actually moved](#v16-to-v26-what-actually-moved).

---

## 1. Design API

Builds and edits report templates in Java: tables, crosstabs, charts, banded objects,
subreports, library components. An SE reaches for it when a customer wants reports
generated from a specification rather than drawn by hand, typically per-tenant or
per-client variants of one layout.

### Entry points

`docs/current/v26/working-with-apis-report-designer/45190386986125-making-preparations-before-using-the-design-api.md`:

```java
DesignerUserInfo userInfo = new DesignerUserInfo(Uid, key);
Designer desg = new Designer(catalogPath, catalogName, userInfo);              // page report
MultipliedDesigner md = new MultipliedDesigner(path, catName, Designer.CAT, userInfo); // web report
```

The corpus never writes a fully qualified package for `Designer` or
`MultipliedDesigner`. It places the Catalog API in `jet.api` and leaves these bare.
Read the Javadoc on the install before writing an import.

Every object in a report is addressed by an opaque `HANDLE` string. Navigation is
`getHandles()`, `getHandles(String handle)`, `getHandles(String handle, int type)`,
`getHandles(String handle, int type, int depth)` and `getParent(String handle)` (same
doc). `type` is a class-type constant defined on the API class.

`docs/current/v26/working-with-apis-report-designer/45190378444557-designing-reports-with-the-design-api.md`
names about 100 methods. The mutators, listed in full:
`createReportSet`, `createWebReportSet`, `createLC`, `saveLC`, `addReport`,
`addDataset`, `insert`, `insertTable`, `insertCrossTab`, `insertChart`, `insertLabel`,
`insertImage`, `insertSpecialField`, `open`, `close`, `closeReportSet`, `delete`,
`setDataset`, `setDataDriver`, `setControlFields`, `setControlledByExpression`,
`setControlledByDynamicFormula`, `setSecurityPolicyName`, `setMaxRecords`,
`setMaxPageNumber`, `setRecordsPerPage`, `setLog`, `exit`. Dynamic report objects add
`addDynamicFormula`, `addDynamicAggregation`, `compileDynamicFormulas` and their
`get*Handles` / `get*Info` counterparts. The accessors are not listed here; read the
doc.

### Prerequisites and licensing

This is where an SE gets stuck, and the reason is commercial rather than technical.

**The Design API needs a licence key that a normal Designer or Server licence does not
include.** From
`docs/current/v26/working-with-apis-report-designer/45190405021325-design-api-packages-and-license.md`:
"Design API and Server Design API use an independent license from other Report
products. You need to contact your Logi Analytics sales to obtain this special license
key". The key applies to the program, not to the installation.

There are two packages with two incompatible keys, and which one you need is decided by
your classpath:

| Package | Classes from | Key required | Difference |
|---|---|---|---|
| Design API | `<designer_install_root>\lib` (`report.jar`, `JREngine.jar`) | Designer License Key | single threaded |
| Server Design API | `<server_install_root>\lib` (`JRESServlets.jar`, `JREngine.jar`) | Server Designer License Key | multithreaded; catalog, query, report and parameter edit methods take an extra `UID` argument |

A key for one is rejected by the other. Independent packages exist for machines with
neither product installed (`designAPI.jar`, `serverDesignAPI.jar`), and each workstation
then needs its own licence
(`docs/current/v26/working-with-apis-report-designer/45190404977933-installing-the-design-api.md`).

Runtime requirements from that same file:

- `JREngine.jar` must come **before** `report.jar` on the classpath. The doc says so
  twice and it is the most common silent failure.
- Full v26 Designer-side classpath: `JREngine.jar`, `report.jar`, `sac-1.3.jar`,
  `log4j-api-2.17.2.jar`, `log4j-core-2.17.2.jar`, `log4j-slf4j-impl-2.17.2.jar`,
  `slf4j-api-1.7.36.jar`.
- JDBC driver jars for the customer's database, added by you.
- `-Dreporthome` set to the product root.
- `setUserInfo(String uid, String key)` called before any other Design API method.

### Samples

`<install_root>\help\samples\APIDesign`, eight programs
(`docs/current/v26/working-with-apis-report-designer/45190378498061-running-the-design-api-samples.md`):
`CreateLCSample.java` (library component with table, crosstab and chart),
`CreateWebReportSample.java` (web report, the same three in a tabular),
`TestDesignInvoice.java` (banded object), `TestDesignEditInvoice.java` (modify an
existing page report template), `TestDesignGraph.java` (chart),
`TestDesignSubreport.java`, `TestInsertCrossTabIntoReport.java`,
`TestInsertCrossTabIntoBanded.java`.

Each takes catalog path and catalog name, optionally a log path. The doc gives the exact
`javac` and `java` lines against `C:\LogiReport\Designer` and
`JinfonetGourmetJava.cat`, which is the fastest thing to run in front of a customer.
`TellMeConnection.java` in `\help\samples\APICatalog` is the smaller first test: it
prints a catalog's connection details
(`docs/current/v26/working-with-apis-report-designer/45190394932365-getting-started-using-the-design-api.md`).

### Version coverage

v26 splits the family across 8 articles. v16 consolidates the identical material into a
single 507-line article,
`docs/jreport-v15-v16/working-with-apis-logi-jreport-designer-v16/1500010028422-design-api.md`,
with the same section list (packages and license, installing, preparations, getting
started, using, samples), the same two-package split, the same `DesignerUserInfo`
constructor and the same independent-licence rule. `MultipliedDesigner`,
`designAPI.jar`, `serverDesignAPI.jar` and `CreateWebReportSample` all appear in the
v15-v16 tree. The differences are jar versions, listed below.

---

## 2. Catalog API

Creates and edits `.cat` catalogs in code: connections, imported SQL, queries, joins,
QBE conditions, stored procedures, user data sources, formulas, summaries, parameters
and business views. An SE reaches for it when a customer provisions catalogs per tenant,
or wants a catalog generated from a schema rather than clicked together in Catalog
Studio.

### Entry points

Two classes, and picking the wrong one fails on catalogs of the wrong age
(`docs/current/v26/working-with-apis-report-designer/45190404647565-using-catalog-api-to-manipulate-catalogs.md`):

- `jet.api.CatalogAPI` — catalogs created **before v13.5**
- `jet.api.MultipliedCatalogAPI` — catalogs created **since v13.5**, which is anything a
  live customer has

You do not construct either directly. You go through the Design API
(`docs/current/v26/working-with-apis-report-designer/45190394380813-making-preparations-before-using-the-catalog-api.md`):

```java
DesignerUserInfo userInfo = new DesignerUserInfo(Uid, key);
Designer desg = new Designer(catalogPath, catalogName, userInfo);
CatalogAPI catalog = desg.getCatalogAPI();
```

The catalog path must be an existing directory; to create a new catalog it must not
already hold a `.cat` file.

`docs/current/v26/working-with-apis-report-designer/45190378038797-manipulating-catalogs-with-the-catalog-api.md`
gives signatures for roughly 55 methods. Grouped, with the list capped at what the doc
actually names:

- Connections: `insert(boolean bUseJDBCODBCBridge, String name, String desc, String url, String driver)`
  and its `ConnectionInfo` overload; `insertJSONConnection(...)` with
  `JSONSchemaURIInfo` and `JSONInstanceURIInfo`.
- Tables and procedures: `insert(String catalogName, String schemaPattern, String tableName, int type)`,
  `getTables`, `getProcedureNames`, `getMappingnames`.
- Queries: `insert(String qryName, QueryFieldInfo, QueryJoinInfo, QueryQBEInfo, QueryAndInfo)`,
  `getQueries`, `getSQLString`, `getImportedSQLString`, `getColumns`, `getJoins`,
  `getQBEInfo`, `getAndConditions`, `deleteQueryField`, `deleteQueryJoin`,
  `deleteQueryTable`, `deleteQBE`, `getNewQueryName`.
- Derived objects: `insert(String formulaName, String desc, String expression)`,
  `insert(String summaryName, String desc, int functionType, String fieldName, String groupByFld)`,
  `insert(String parameterName, String desc, String prompt, String type, String defaultValue)`,
  `insert(String wherePortionName, String desc, WherePortionInfo)`.
- User data sources: `insert(String strDSName, String strClassName, String strParameter, UDSColumnInfo)`.
- Business views: `insertBusinessViewCategory`, `insertBusinessViewGroup`,
  `insertBusinessViewAggregation` (with an `isRawExpression` overload),
  `insertBusinessViewDetail`, `compileBVFormulas`.
- Lifecycle: `save()`, `saveAs(String path, String name)`, `delete(String handle)`,
  `refreshReference()`.

Most methods come in a pair, one with a leading `dataSourceName` and one without, for
multi-data-source and single-data-source catalogs respectively.

### Prerequisites and licensing

Installed with Designer; no separate install step
(`docs/current/v26/working-with-apis-report-designer/45190377989133-installing-the-catalog-api.md`).
The classes live in `report.jar`.

**It runs on the Design API licence key**, not a Catalog-specific one: "In your Java
program, you must set the licensed user and Design API license key.
`DesignerUserInfo userInfo=new DesignerUserInfo("UID","Design API Key");`". Same file.
So a customer who has not bought the Design API licence cannot use the Catalog API
either, which is worth saying before scoping any provisioning work.

Same classpath ordering rule (`JREngine.jar` before `report.jar`) and the same
`-Dreporthome`. To use Server's libraries instead, put
`<server_install_root>\lib\JRESServlets.jar` on the path in place of `report.jar` and
switch to the Server Design API key.

### Samples

`<install_root>\help\samples\APICatalog`
(`docs/current/v26/working-with-apis-report-designer/45190386787213-running-the-catalog-api-samples.md`):
`TestCatalogAPI.java` creates a catalog, `TestCatalogBV.java` creates business views in
one. The doc gives the full `javac` and `java` lines and warns that the output directory
(`C:\LogiReport\Designer\Demo\MyReports`) must exist and be empty first.

### Version coverage

Present in all four eras. v16's copy is
`docs/jreport-v15-v16/working-with-apis-logi-jreport-designer-v16/1500010028402-catalog-api.md`,
388 lines, one article. The v13.5 catalog-structure split that produced
`MultipliedCatalogAPI` predates v15, so a v16 customer already faces the same choice of
class.

---

## 3. Server API (Java)

Drives a running Report Server from Java: running and exporting reports, scheduling,
publishing resources, versions, security, clustering, monitoring. An SE reaches for it
when reporting has to be triggered by the customer's own application rather than by a
person in the Server Console.

`docs/current/v26/working-with-apis-report-server/45203869669005-tour-of-the-java-api.md`
is the map. It categorises the API into 19 functional areas and states plainly that the
classes "provide thousands of methods", so treat the names below as the doorways the
prose opens, not as the surface.

### Entry points

Every program starts the same way (same doc):

```java
HttpUtil.initEnv();          // start or attach to the singleton server on this machine
HttpUtil.getHttpRptServer(); // handle used by every later call
```

Classes the tour names, with their area:

| Area | Class or interface |
|---|---|
| Init, connect, servlet utilities | `jet.server.api.http.HttpUtil` |
| Web session and sign-in | `jet.server.api.http.HttpUserSessionManager` |
| Single sign-on hook | `jet.server.api.http.HttpExternalAuthorized` |
| Authentication | `jet.server.api.custom.security.AuthenticationProvider` (`isValidUser()`), `jet.server.api.Authenticator` |
| Authorisation | `jet.server.api.custom.security.AuthorizationProvider` (`isBasePermissionOk()`) |
| Security administration | `jet.server.api.admin.SecurityAdminService` |
| Task events | `jet.server.api.TaskListener` |
| Engine, no server needed | `jet.server.api.engine.ReportEngine` |
| NLS | `jet.util.NLSBundleInfo` |
| Resources | `jet.server.api.ResourceManager` |
| Triggers | `jet.server.api.TriggerManager` |
| Run and schedule | `jet.server.api.RptServer` (`submitScheduledTask()`) |
| Cluster load balancing | `jet.server.api.cluster.LoadBalancer` |
| Remote dispatch | `jet.server.api.rmi.RemoteDispatcher` |
| Remote server | `jet.server.api.RemoteReportServerToolkit`, `jet.server.api.rmi.RemoteReportServerToolkit` |
| Configuration | `jet.server.api.admin.cfg.*` |
| Monitor | `jet.server.api.monitor.*` |
| Profiling | `jet.server.api.profiling.*` |
| Cached report data | `jet.server.api.crd.*` |

Smaller named surfaces, each with its own v26 article in
`docs/current/v26/working-with-apis-report-server/`:

- **Information Bus API** (`45203870365581-information-bus-api.md`): `InformationBus`,
  `InformationBusManager`, `InformationContainer`, `InfoLifeCycleType`. Three container
  scopes (global, organisation, user) and three lifetimes (`LONG_TIME`,
  `SPECIFIED_TIME`, `ONCE_TIME`). This is how you pass a tenant discriminator from your
  application into a report run.
- **Dynamic Security API** (`45203849636365-dynamic-security-api.md`):
  `getDynamicSecurities`, `addDynamicSecurity`, `deleteDynamicSecurity`,
  `getCatalogPath`, `getSecurityFileName`, `getSecurityFile`, `setSecurityFile`,
  `setDefault`, constant `APIConst.TAG_SECURITY_FILE_NAME`.
- **Dynamic Connection API** (`45203855273997-dynamic-connection-api.md`).
- **On-Demand API** (`45203870740237-advanced-running-reports-using-the-on-demand-api.md`).
- **NLS API** (`45203896215053-using-the-nls-api.md`).
- **Dashboard Listener API** (`45203862257549-applying-the-implementations-of-the-dashboard-listener-api.md`).
- **RMI** (`45203855986829-using-rmi-in-report-server.md`): remote calls authenticate
  against `<install_root>\bin\rmi.auth`, generated at install. Pass it with
  `-Djrs.rmi.auth_file=` or `-Djrs.rmi.auth_string=`; the server checks
  `auth_string`, then `auth_file`, then `<install_root>\bin`. Every node in a cluster
  must hold the same file.

`docs/current/v26/working-with-apis-report-server/45203849318285-using-the-server-api.md`
adds the resource-path rule that trips people up: Public Reports paths start with `/`,
My Reports paths start with `/USERFOLDERPATH/<username>/`.

### Prerequisites and licensing

No separate licence. The Server API installs with Server, classes in `JRESServlets.jar`
(`docs/current/v26/working-with-apis-report-server/45203861851533-installing-the-server-api.md`).

Two classpaths, and choosing wrongly is a runtime failure rather than a compile failure:

- **Same JVM as the server**: `JRESServlets.jar`, `JREngine.jar`,
  `jakarta.servlet-api-4.0.4.jar`, `hsqldb-2.6.1.jar`, `log4j-core-2.17.2.jar`,
  `log4j-api-2.17.2.jar`, `sac-1.3.jar`, `commons-logging-1.2.jar`, `quartz-2.3.2.jar`,
  and the four Derby jars from `<install_root>\derby\lib`.
- **Different JVM or machine (RMI)**: `JRSRMI.jar` in place of the first two, rest as
  above, no Derby.

Swap the Derby jars for the customer's JDBC driver if their system database is not
Derby. Export targets need their own jars, added by you: `jakarta.mail-1.6.7.jar` for
email, `commons-net-3.8.0.jar` for FTP, `poi-5.2.2.jar` for Excel, `JRWebDesign.jar` for
Page Report Result.

Designer ships a Server for preview, so the same libraries exist at
`<designer_install_root>\server\lib`.

### Samples

`<install_root>\help\samples`
(`docs/current/v26/working-with-apis-report-server/45203879324557-api-demos.md`), with a
folder per topic: `APIServer`, `APICluster` (`DemoLoadBalancer.java`,
`DemoRemoteDispatcher.java`), `APISecurity` (`DemoAuthenticationProvider.java`,
`DemoAuthorizationProvider.java`, `CustomizedSendFileAuthorizor.java`, plus
`AddPrincipal` with `AddUser`, `AddGroup`, `AddRole` and their `*Cover` variants, plus
`LoginLogout` with JSP files that exercise both `checkLogin()` overloads),
`APIParameter` (`DemoParameterGenerator.java`), `APIConvertData`
(`ResultSetConvertorImpl.java`), `APITaskListener`, and the `APIDemo*` set:
`APIDemoRunReport`, `APIDemoRunAndExportReport`, `APIDemoRunReportWithTimeout`,
`APIDemoPublishRpt`, `APIDemoDeployRpt`, `APIDemoDynamicExportTask`,
`APIDemoSendEMail`, `APIDemoReportEngine`. RMI demos have their own article,
`45203869492749-rmi-demos.md`.

### Version coverage

The fullest treatment in the corpus is v19
(`docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/`, 79 files
mentioning the family). v15 covers the same ground in
`docs/jreport-v15-v16/working-with-apis-logi-jreport-server-v15/`, 41 articles including
its own `tour-of-the-java-api`, `information-bus-api`, `dynamic-security-api`,
`dynamic-connection-api`, `using-nls-api`, `rmi-demos` and
`adding-tasklistener-when-scheduling-reports`. The class names match. The jars do not.

---

## 4. Java API for servlets, and servlet integration

Putting Report Server inside a Java web application rather than beside it. An SE reaches
for this when the customer will not accept a second URL and a second sign-in, which is
most embedded deals.

### Entry points

`docs/current/v26/working-with-apis-report-server/45203863153933-java-api-for-a-servlet.md`
covers sending an HTTP request for service, connecting from the same JVM and from a
different one, three authentication styles (JSP-style, URL query parameter, application
authentication), authorisation, starting a user session, and running a report by Java
call or servlet URL.

The connect sequence, from
[`api/servlet-integration.md`](api/servlet-integration.md) citing the v19 article:

```java
System.getProperties().put("reporthome", "C:\\LogiReport\\Server");
HttpUtil.initEnv(System.getProperties());
HttpRptServer httpRptServer = HttpUtil.getHttpRptServer();
```

The parameterless `getHttpRptServer()` only works when your code shares a JVM with the
server. Helpers: `HttpUtil.getParameters(request)`, `HttpUtil.getUser(request)`,
`HttpUtil.decodeEsc(...)`, and the `APIConst.TAG_*` parameter-name constants.

Servlets and listeners declared in `web.xml`, from
`docs/current/v26/report-server-integration-report-server/45203989538701-four-ways-of-integrating-report-server.md`:

| Servlet name | Class |
|---|---|
| `jrserver` | `jet.server.servlets.JRServlet` |
| `sendfile` | `jet.server.servlets.SendFileServlet` |
| `dhtml` | `jet.web.dhtml.DHTMLlet` |
| `help` | `jet.web.dhtml.JHelplet` |
| `WebOSServlet` | `com.jinfonet.web.client.WebOSServlet` |
| `JRWSServlet` | `jet.server.ws.xfire.servlets.JRWebServiceServlet` |

Plus `jet.server.servlets.JRServerContextListener` and
`jet.server.servlets.CharacterEncodingFilter`.

The four integration routes named in that article: build a Report Server WAR, build a
Report Server EAR, embed a self-contained server in your own WAR, embed one in your own
EAR.

### Prerequisites

Same libraries as the Server API. `reporthome` must be set, and doing that inside a Java
EE container has its own article,
`docs/current/v26/report-server-integration-report-server/45203989455629-specifying-reporthome-for-report-server-in-a-java-ee-environment.md`.

v26 ships a page per container in
`docs/current/v26/report-server-integration-report-server/`: Tomcat, WebLogic 14.1.1,
IBM WebSphere 9.0.5.6, JBoss EAP, WildFly, Jetty, Resin, GlassFish Open Source Edition
5.0, and Sun Java System Application Server Platform Edition 9.1. Two more cover
integrating a **remote** server by WAR into WebSphere 9.0.0.7 and WebLogic 14.1.1.

### Samples

The shipped JSP pages under `<install_root>\public_html\jinfonet`, `\dhtmljsp`, `\admin`
and `\javascript` are production code with visible source, which the v19 technical
architecture article presents as the worked examples for this layer. The
`APISecurity\LoginLogout` JSP set (entry point `loginIndex.jsp`) is the one that
demonstrates authentication behaviour end to end.

### Version coverage

The three-layer model (JSP pages, compiled servlets, Java API) and the `HttpUtil` entry
points are identical in v15
(`docs/jreport-v15-v16/working-with-apis-logi-jreport-server-v15/1500009644182-java-api-for-a-servlet.md`).
The container list and the servlet API package are what moved.

---

## 5. JavaScript viewer API

Embeds page reports, web reports and dashboards in a host page and drives them from
JavaScript, without the surrounding Page Report Studio, Web Report Studio or JDashboard
chrome. An SE reaches for it in any embedded-analytics conversation where the customer
wants their own header, their own navigation and no visible Logi UI.

### Entry points

One file, `jreportapi.js`, produced by the server at
`<install_root>\public_html\webos\jsvm\lib` and served at
`/webos/jsvm/lib/jreportapi.js`. Load it with `id="j$vm"` on the script tag, which is
part of the documented snippet in every era.

**The runtime global is `J$VM`, upper case.** The lower-case `j$vm` is only the tag's
id, and because browsers expose element ids as globals, `typeof j$vm` returns
`"object"` whether or not the API ever initialised. Verified against
`logianalytics/logireport-server:latest` (26.2 SP1) on 22 August 2026; full detail and
the correct load guard in [`api/javascript-api.md`](api/javascript-api.md).

Calls the corpus names: `Factory.runReport(server, prptRes, catRes, params, entryId)`,
`getParameterInfo(callback)`, `changeParameters(parameterInfo)`. Actions available on an
embedded report: open, close, export, print, specify parameter values, refresh data,
save, save as, page navigation. The `server` object carries `url`, `user`, `pass` or
`authorized_user` under SSO, and a `jrd_prefer` block that switches off toolbars, the
user info bar, the toolbox, the DSO tree, the TOC tree, the popup menu and ad hoc mode.

Source article, v26:
`docs/current/v26/working-with-apis-report-server/45203895093901-using-javascript-api-to-embed-server-console-and-reports-in-your-applications.md`.

### Prerequisites

No separate licence key. An unlicensed or expired server still serves the static file
with a 200 and then redirects every runtime request to `/expired.jsp`, so the symptom of
an expired licence is an API that loads and never boots. Check the licence before
debugging the page.

Cross-origin embedding needs `-Djreport.server.csrf.whitelist=<calling host>` on the
server, the same property the Web API authentication walkthrough uses.

### Samples

`<install_root>\public_html\webos\app\demo`: `jreportapi-demo-rpt.html` with
`demo-rpt.js` for page and web reports, `jreportapi-demo-dsb.html` with `demo-dsb.js`
for dashboards. Reachable on a running server at
`http://localhost:8888/webos/app/demo/jreportapi-demo-rpt.html`. Deeper source at
`<install_root>\public_html\webos\jsvm\src\com\jinfonet\api` (`Dashboard.js`,
`ReportSet.js`).

### Version coverage

Present in v15 as
`docs/jreport-v15-v16/working-with-apis-logi-jreport-server-v15/1500009667961-embedding-logi-jreport-server-guide-v15-with-javascript-apis.md`,
with the same one-file integration model and the same action list minus Save As. That
v15 article renders the filename as `Logi JReportapi.js` throughout, including inside
code samples, which reads as rebrand search-and-replace damage. The corpus does not say
what the file was actually called on a v15 disk; check the install rather than trusting
either article.

---

## 6. RESTful Web API (Server Console)

HTTP API covering what the Server Console does, defined by an openAPI file that ships on
the install. An SE reaches for it when the customer wants to administer Logi Report from
their own portal, or to automate provisioning from something that is not Java.

### Entry points

- Definition: `<install_root>\help\webapi\logireportserver.yaml`
- Mirrored here: `api/logireportserver.yaml` (Swagger 2.0, 124 paths, 225 operations)
- Operation-level index: `api/ENDPOINTS.md`, generated from that file, grouped by tag
- Pre-generated JavaScript client:
  `<install_root>\help\webapi\client-js\javascript-client-generated.zip`
- Client docs: `<install_root>\help\webapi\client-js\js-docs\index.html`
- Sample: `<install_root>\help\webapi\client-js\sample\index.html`, code in `src\index.js`
- Rendered API docs on a running server:
  `http://localhost:8888/servlet/sendfile/help/webapi/webapi-docs/index.html`

Only the JavaScript client is pre-generated. Java, .NET and C++ clients you generate
yourself from the yaml.

Capabilities the corpus lists: sign in and out and session management; resource listing,
folder creation, publishing, properties, permissions and NLS; business views with their
categories, groups, aggregations and details, including business view security; users,
groups, roles and organisations with resource allocations; scheduling and bursting to
versioning, disk, email, printer, fax and FTP across the full export format set; server
preferences and Studio profiles; LDAP settings, user and group import, sync schedule and
role maps (new at 19.2); triggers (new at 19.2); dynamic connections, dynamic security
and dynamic display names.

**The corpus gives no path, verb or payload.** For that, read the yaml on a real
install. Do not invent endpoints.

### Prerequisites

Cross-origin calls need `-Djreport.server.csrf.whitelist=<calling host>` in
`JRServer.bat`. SSO uses `-Djrs.httpExternalAuthorized=<your class>`, which is the same
hook the Java security API uses; the walkthrough compiles
`help\webapi\sample\WebAPIExternalAuthorized.java` against `<install_root>\lib\*` and
adds it to `SSO.jar`
(`docs/current/v26/working-with-apis-report-server/45203895093901-using-javascript-api-to-embed-server-console-and-reports-in-your-applications.md`,
lines 317 onward).

### Samples

`<install_root>\help\webapi\sample\WebAPIDemo.html`, which walks six sign-in scenarios
(credentials in the URL, in a header, and by SSO).

### Version coverage

Documented in v16
(`docs/jreport-v15-v16/working-on-logi-jreport-server-via-urls-logi-jreport-server/1500009686122-embedding-logi-jreport-with-javascript-apis.md`)
under the name `jreportserver.yaml`. The file was renamed to `logireportserver.yaml` at
v17.1. **v15 alone appears to lack it**, on the evidence of a single v15 article, which
is thin evidence; check a v15 install before telling a v15 customer either way.

---

## 7. URL invocation

Running, scheduling, creating and administering by building a URL, from any language
that can make an HTTP request. The v19 server guide frames this as one of three ways in
and notes it is not technically an API while serving the same purpose; an SE reaches for
it when the customer's stack is .NET, PHP or a static page and nobody wants to write
Java.

`docs/current/v26/working-on-report-server-via-url-report-server/` holds 9 articles:
running, scheduling and creating reports via URL; authentication properties in URL;
working with the server via URL; working with dashboards via URL; accessing Visual
Analysis via URL; and the property reference,
`45204033487757-url-properties-for-running-scheduling-and-viewing-reports-via-url.md`.

The command is the `jrs.cmd` query parameter. The v26 set names **38 distinct `jrs.cmd`
values** and **362 distinct `jrs.*` properties**, which is the closest thing Logi Report
has to an endpoint index. Examples of the command values: `jrs.get_subnodes`,
`jrs.delete_resource`, `jrs.del_schedule`, `jrs.enable_schedule`,
`jrs.disable_schedule`, `jrs.del_completed`, `jrs.del_all_completed`,
`jrs.del_rpt_ver`, `jrs.del_rst_ver`, `jrs.del_rstdoc_ver`, `jrs.change_password`. Both
GET and POST work for almost all commands; POST has no attribute-length limit, GET does.

Samples: `<install_root>\help\samples\URLSamples\TestURL.html`. Detail:
[`api/url-invocation.md`](api/url-invocation.md).

Coverage is even across eras (25 articles in v15-v16, 26 in v17-v19, 9 to 10 in the
current trees). The current trees are thinner in article count, not in property count.

---

## v16 to v26, what actually moved

For a JReport v16 renewal the honest headline is that **no API family was added and none
was removed**. Design, Catalog, Server, Java servlet, JavaScript viewer, RESTful Web
API, Information Bus, Dynamic Security, Dynamic Connection, NLS, On-Demand, Trigger
Manager, Dashboard Listener and URL invocation are all documented in the v15-v16 tree.
Code written against v16 is describing the same classes.

What did move, all of it verifiable in the corpus:

| Thing | v15-v16 | v26 | Why it matters |
|---|---|---|---|
| Servlet API | `javax.servlet-api-3.1.0.jar` | `jakarta.servlet-4.0.4.jar` | `javax` to `jakarta` is a source-breaking rename. Any customer servlet or JSP calling the server needs its imports changed. This is the single biggest code change in the upgrade. |
| Mail | `mail-1.4.7.jar` | `jakarta.mail-1.6.7.jar` | Same rename, hits email delivery integrations |
| Log4j | `log4j-*-2.7` (v15), `2.9.1` (v16) | `log4j-*-2.17.2` plus `slf4j-api-1.7.36` and `log4j-slf4j-impl` | v16's 2.9.1 is inside the Log4Shell range. Worth raising as a security argument, not just a version bump |
| Excel export | `poi-3.15.jar` | `poi-5.2.2.jar` | |
| FTP | `commons-net-3.5.jar` | `commons-net-3.8.0.jar` | |
| Scheduler | `quartz-all-2.2.3.jar` | `quartz-2.3.2.jar` | Artefact name changed as well as version |
| HSQLDB | `hsqldb-2.3.4.jar` (v15), `2.4.0` (v16) | `hsqldb-2.6.1.jar` | |
| Web API definition | `jreportserver.yaml` | `logireportserver.yaml` | Renamed at v17.1; a v16 integration pointing at the old filename breaks |
| JDK | recommended Oracle 8, 9, 11, 12 / OpenJDK 8, 11, 12, 13; minimum 8 | recommended Oracle or OpenJDK 11, 17, 21, 25; minimum 8 | Minimum is still 8, so a JDK 8 estate is not blocked. Sources: `docs/jreport-v15-v16/introduction-to-logi-jreport-server-v16/1500009691062-system-requirements.md`, `docs/current/v26/introduction-to-report-server/45203976092813-report-server-system-requirements.md` |
| Composer import | absent | `Composer Trusted Access Credentials`, 2 v26 files | New at v26.2. Composer sources translate into Business Views. Nothing in v15 to v25 mentions Composer |
| Doc structure | one long article per API family | 8 to 38 articles per family | Same content, different navigation. A v16 customer's bookmarks will not resolve |

The upgrade procedure itself is
`docs/current/v26/introduction-to-report-server/45203988660237-upgrading-report-server.md`.
It documents "Upgrading from v13 and later to v26" as one supported path, in-place into
the same directory with a new licence key, and states that the two migration tools in
`<install_root>\bin` are only needed below v6.0. A v16 customer is inside the
no-migration-tool range. Report resources are converted to comply with the new server
version; back up the system database first.

---

## What the corpus does not answer

- **No Javadoc, no method signatures beyond the prose.** For the Server API in
  particular, the tour says "thousands of methods" and names about 25 classes. Public
  Javadoc exists for v19 through v24 at `reportkbase.logianalytics.com` and not for v25
  or v26.
- **No REST path, verb or payload list.** The capability list above is what the corpus
  gives. The yaml on the install is the only reference.
- **No fully qualified package for `Designer` or `MultipliedDesigner`.** The Catalog API
  is placed in `jet.api`; the Design API entry classes are named bare in every era.
- **No licence prices, no key issuing process.** The Design API licence is stated to be
  separate and obtained from sales. What it costs, whether a v16 customer's existing key
  carries forward, and whether Server Design API is bundled in any edition are not in
  the corpus.
- **No support lifecycle or end-of-life dates.** Nothing states when v16 leaves support.
  The only lifecycle signal is that patches were still being cut against v15.6 in August
  2026.
- **No performance or sizing data for any API.** No throughput figures, no concurrency
  limits, no guidance on how many Design API instances a JVM will hold.
- **No worked v16-to-v26 code migration.** The `javax` to `jakarta` change is inferable
  from two jar lists in two eras, and is stated nowhere as a migration instruction.
