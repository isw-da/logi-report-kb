# Logi Report API map

Logi Report exposes several programmable surfaces. This file says which one exists,
what it is for, and which to reach for given a task. The per-surface files carry the
classes, entry points and worked examples.

Logi Report is a separate product from Logi Composer. They share no documentation
surface, and nothing in this corpus describes Composer. Do not answer a Logi Report
API question with Composer knowledge, or the reverse.

## Eras

Every claim below is drawn from one of three source trees, and the tree is the era label:

| Era directory | Product name in the text | Notes |
| --- | --- | --- |
| `../docs/jreport-v15-v16/` | Logi JReport | v15 and v16 |
| `../docs/logi-report-v17-v19/` | Logi Report | v17, v17.1, v18, v19; the v19 set is the fullest |
| `../docs/unversioned/` | mixed | some articles say Logi Report, some still say Logi JReport; no version in the path, so treat a claim sourced only from here as unversioned |

The v17 rename changed the product name throughout the text. Where an API itself
changed between eras, the per-surface file says so. Where the corpus does not let me
tell, the file says that instead of guessing.

## Which surface for which task

| Task | Surface | File |
| --- | --- | --- |
| Run or export a report from Java code | Server API (`jet.server.api.RptServer`) | [server-api.md](server-api.md) |
| Schedule a report task from Java code | Server API (`submitScheduledTask`, `TriggerManager`) | [server-api.md](server-api.md) |
| Schedule a report without writing Java | URL invocation (`submitSchedPage.jsp`) | [url-invocation.md](url-invocation.md) |
| Run a report with no server running at all | Engine API (`jet.server.api.engine.ReportEngine`) | [server-api.md](server-api.md) |
| Publish, deploy, delete or list server resources | Server API (`jet.server.api.ResourceManager`) | [server-api.md](server-api.md) |
| Build or edit a catalog in code (connections, queries, business views) | Catalog API | [catalog-api.md](catalog-api.md) |
| Build or edit a report template in code (tables, crosstabs, charts) | Design API | [design-api.md](design-api.md) |
| Replace authentication or authorisation with your own system | Security API | [security-api.md](security-api.md) |
| Single sign-on into the server web session | `HttpExternalAuthorized` | [security-api.md](security-api.md) |
| Pass information between server components at global, organisation or user scope | Information Bus API | [information-bus-api.md](information-bus-api.md) |
| Drive a server running in another JVM or on another machine | RMI, Remote Server API | [rmi.md](rmi.md) |
| Embed a report or dashboard in a web page and control it from the browser | JavaScript API (`jreportapi.js`) | [javascript-api.md](javascript-api.md) |
| Drive the Server Console from JavaScript, Java, .NET or C++ over HTTP | RESTful Web API (openAPI definition) | [rest-web-api.md](rest-web-api.md) |
| Run, schedule, view or administer by building a URL from any language | URL invocation | [url-invocation.md](url-invocation.md) |
| Put the server inside your own web application or application server | Servlet integration | [servlet-integration.md](servlet-integration.md) |

## The three ways in, as the docs frame them

The v19 server guide names three ways to use the server from an application: browse to
the JSP pages the product ships, call the compiled servlets by URL, or call the Java API
classes directly. The servlet route is described as not technically an API but serving
the same purpose, and is limited to running, scheduling and viewing reports. The same
three-way framing appears in the v15 tour under the Logi JReport name.

Source: [Using Server API to Work with Logi Report Server (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741407944855-using-server-api-to-work-with-logi-report-server.md),
[Tour of the Java API (v15, Logi JReport)](../docs/jreport-v15-v16/working-with-apis-logi-jreport-server-v15/1500009668401-tour-of-the-java-api.md).

## Where the reference material lives on a real install

The corpus repeatedly points outside itself. None of these paths are in this repo:

- Javadoc for every class and method: `<install_root>\help\api`
- Runnable samples: `<install_root>\help\samples` (subfolders `APIServer`, `APIRemoteServer`, `APISecurity`, `APICluster`, `APICatalog`, `APIParameter`, `APINLS`, `APITaskListener`)
- URL samples: `<install_root>\help\samples\URLSamples\TestURL.html`
- Web API definition: `<install_root>\help\webapi\logireportserver.yaml`
- Generated JavaScript client: `<install_root>\help\webapi\client-js`

Sources: [Tour of the Java API (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741408065175-tour-of-the-java-api.md),
[API Demos (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741407991063-api-demos.md),
[Technical Architecture (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741408039575-technical-architecture.md).

## What the corpus does not contain

- No Javadoc. Class and method names below are only those the prose names. Signatures
  beyond that are not documented here and should not be invented.
- No REST endpoint list. The Web API is described by capability and by the location of
  its openAPI definition file, not by path.
- No Logi Composer material of any kind.
