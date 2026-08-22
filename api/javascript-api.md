# JavaScript API (jreportapi.js)

The JavaScript API embeds page reports, web reports and dashboards inside your own web
application and lets you drive them from the page, without going through Page Report
Studio, Web Report Studio or JDashboard as the surrounding UI.

Primary source: [Using JavaScript API to Embed Server Console and Reports in Your Applications (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741394606103-using-javascript-api-to-embed-server-console-and-reports-in.md).
Era: `logi-report-v17-v19`. The Server Console side of that same article is covered
separately in [rest-web-api.md](rest-web-api.md).

## What you can drive

Open, close, export, print, specify parameter values, refresh data, save, save as, and
navigate pages in page reports. Web controls defined in the report, such as filter controls
and custom controls, keep working inside the embed, and following a link shows a link path
above the body that you can use to go back.

## Loading it

The whole API is one file, `jreportapi.js`, created by the server at
`<install_root>\public_html\webos\jsvm\lib`. Two ways in:

```html
<!-- copied into your own app -->
<script id="j$vm" type="text/javascript" src="C:\API\jreportapi.js"></script>

<!-- served from a running server at 192.0.0.1:8888 -->
<script id="j$vm" type="text/javascript" src="http://192.0.0.1:8888/webos/jsvm/lib/jreportapi.js"></script>
```

The `id="j$vm"` attribute is part of the documented snippet in both eras, so keep it.

## Demos on a running server

`<install_root>\public_html\webos\app\demo` holds `jreportapi-demo-rpt.html` for a page or
web report and `jreportapi-demo-dsb.html` for dashboards, each with its own
`demo-rpt.js` or `demo-dsb.js` showing the calls. Open them at
`http://localhost:8888/webos/app/demo/jreportapi-demo-rpt.html` and pick an
**Open xxx** item from the left menu. The dashboard demo opens two dashboards and lets you
switch between them by name.

## Worked example: open a page report with parameters

```javascript
thi$.openPageReport = function(entryId){
  var params1 = {
    "p_Cascading-Country": "USA",
    "p_Cascading-City": ["New York","Los Angeles","Chicago"],
    "p_Year": "\x07"
  };
  var app = Factory.runReport(server, prptRes, catRes, params1, entryId);
};
```

`"\x07"` means apply every value of that parameter. A multi-valued parameter takes a
JavaScript array.

## Reading and changing parameters after the report is open

- `getParameterInfo(callback)` returns an array of parameter name and default value pairs
  for the current report or dashboard.
- `changeParameters(parameterInfo)` sets values and reruns. Each element is
  `{pname, pvalue, ownerID}`, where `pvalue` is an array (one element for most types,
  several for a multi-valued parameter) and `ownerID` is the report or library component
  ID. `ownerID` is optional for reports and mandatory for dashboards.

For more, the article points at `Dashboard.js` and `ReportSet.js` in
`<install_root>\public_html\webos\jsvm\src\com\jinfonet\api`.

## The server object

Normal sign-in carries credentials:

```javascript
var server = {
  url: "http://localhost:8888/jinfonet/tryView.jsp",
  user: "admin",
  pass: "admin",
  jrd_prefer: {
    pagereport: {
      feature_UserInfoBar: false, feature_ToolBar: false, feature_Toolbox: false,
      feature_DSOTree: false, feature_TOCTree: false, feature_PopupMenu: false,
      feature_ADHOC: false
    },
    webreport: { viewMode: { hasToolbar: false, hasSideArea: false } }
  },
  jrd_studio_mode: "view",
  "jrs.param_page": true
};
```

Under single sign-on, drop `user` and `pass` and name the authorised user instead:

```javascript
var server = {
  url: "http://localhost:8888/jinfonet/tryView.jsp",
  authorized_user: "admin",
  ...
};
```

The `jrd_prefer` block is how you strip the surrounding chrome, which is usually the point
of embedding. Server-side SSO still has to be configured; see [security-api.md](security-api.md).

## Era note

The JavaScript API exists in the v15 Logi JReport documentation too, with the same
integration model (one file, load locally or from the server) and the same action list,
minus save as. Two v15-era differences worth naming:

- The v15 article's action list has no **Save As** and no **Specify Parameter Values** as a
  separate item, though it does have a parameter section.
- The v15 article renders the file name as `Logi JReportapi.js` throughout, including
  inside code samples and URLs. That reads as an artefact of the search-and-replace that
  rebranded JReport to Logi JReport, not as a real file name. The v19 article calls it
  `jreportapi.js`. I cannot confirm from the corpus which name the v15 file actually had on
  disk, so check the install rather than trusting either article.

Source: [Embedding Logi JReport With JavaScript APIs (v15)](../docs/jreport-v15-v16/working-with-apis-logi-jreport-server-v15/1500009667961-embedding-logi-jreport-server-guide-v15-with-javascript-apis.md).

## What this API is not

It does not administer the server. Listing resources, managing users, scheduling and
console operations go through the [RESTful Web API](rest-web-api.md) or
[URL invocation](url-invocation.md).
