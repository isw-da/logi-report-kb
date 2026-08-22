# RESTful Web API (Server Console)

Logi Report Server exposes modularised RESTful Web APIs covering the Server Console, so you
can build a console of your own on any platform. The definition is an openAPI file, so a
client can be generated for JavaScript, Java, .NET or C++.

Primary source: [Using JavaScript API to Embed Server Console and Reports in Your Applications (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741394606103-using-javascript-api-to-embed-server-console-and-reports-in.md),
first section. Era: `logi-report-v17-v19`.

## Where the definition and the clients live

- openAPI definition: `<install_root>\help\webapi\logireportserver.yaml`
- generated JavaScript client: `<install_root>\help\webapi\client-js\javascript-client-generated.zip`,
  which unpacks to a `javascript-client` folder with the code in `src` and docs in `docs`
- JavaScript API documentation: `<install_root>\help\webapi\client-js\js-docs\index.html`
- sample: `<install_root>\help\webapi\client-js\sample`, entry `index.html`, code in
  `src\index.js`
- Web API documentation on a running local server:
  `http://localhost:8888/servlet/sendfile/help/webapi/webapi-docs/index.html`

Only the JavaScript client is pre-generated. Java, .NET and C++ clients you generate
yourself from the yaml.

## What the API covers

- **Sign in and out**: sign in, sign out, read session information such as username and
  session ID, set session timeout.
- **Resources**: list folders, reports, library components, dashboards and versions; create
  folders and publish into them; get and set properties; set and delete permissions; get,
  set and delete catalog-level, report-level and global NLS; fetch the whole resource tree
  with properties in one call, with parameter information.
- **Business views**: list business views in a catalog with their categories, group objects,
  aggregation objects and detail objects; get, set and delete permissions on business views
  and group objects; manage which business views a report may use; get, set and delete
  business view security in a catalog.
- **Security**: add, remove, get and edit users, groups and roles and their members; create,
  read, update and delete organisations; read and update organisation resource allocations.
- **Scheduling and advanced run**: schedule report running and bursting tasks to the
  versioning system, disk, email, printer, fax and FTP, in Page Report Result, Web Report
  Result, HTML, PDF, Excel, Text, RTF, XML and PostScript; view, enable, disable, copy, get,
  run, import, export and delete tasks.
- **Preferences**: get and set server preferences; get, add, edit and delete Page Report
  Studio, Web Report Studio and JDashboard profiles.
- **LDAP** (marked new for 19.2): read and change LDAP settings, import users and groups,
  read and set the synchronisation schedule, read, add and change role maps.
- **Triggers** (marked new for 19.2): get, create, enable, disable and fire triggers.
- **Dynamic catalog settings**: get, set, create and delete dynamic connections, dynamic
  security and dynamic display names for business view elements.

The corpus lists capabilities, not endpoints. There is no path, verb or payload reference
here; read the yaml.

## Authenticating a Web API call

The article walks one setup end to end, covering username and password in the URL, in a
header, and by SSO:

1. Install the server on machine B (`b.test.com`) at `D:\LogiReport\Server`.
2. Compile `D:\LogiReport\Server\help\webapi\sample\WebAPIExternalAuthorized.java` against
   `D:\LogiReport\Server\lib\*`.
3. Add the compiled class to `SSO.jar`.
4. Put `SSO.jar` on the path in `D:\LogiReport\Server\bin\JRServer.bat`.
5. Add `-Djrs.httpExternalAuthorized=WebAPIExternalAuthorized` and
   `-Djreport.server.csrf.whitelist=a.test.com` to `JRServer.bat`.
6. Start the server.
7. On machine A (`a.test.com`), serve `WebAPIDemo.html` (from the server's
   `help\webapi\sample`) through IIS.
8. Open `http://a.test.com/webapidemo.html` and work through its six sign-in scenarios.

The CSRF whitelist property is the piece that makes a cross-origin call from A to B work.
`jrs.httpExternalAuthorized` is the same SSO hook the Java API uses, so see
[security-api.md](security-api.md).

## Era note

This surface is absent from the v15 Logi JReport documentation. The
[v15 JavaScript article](../docs/jreport-v15-v16/working-with-apis-logi-jreport-server-v15/1500009667961-embedding-logi-jreport-server-guide-v15-with-javascript-apis.md)
covers embedding only, with no Server Console REST section, no openAPI definition and no
generated clients. Within the v17 to v19 era it is present from
[v17.1](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v17-1/1500009770701-embedding-logi-report-server-console-and-reports-in-your-app.md)
onward, with LDAP and trigger coverage flagged as new at 19.2. If a customer is on v15 or
v16, do not promise them this API.
