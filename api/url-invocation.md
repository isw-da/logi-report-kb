# URL invocation

Everything the Server Console does, you can ask for by building a URL. This is the route
for any caller that can make an HTTP request and does not want to be a Java program:
.NET, static HTML, a shell script, a scheduler.

Primary source: [Working on Logi Report Server via URL (v19)](../docs/logi-report-v17-v19/working-on-logi-report-server-via-url-logi-report-server-v19/5741464810263-working-on-logi-report-server-via-url-logi-report-server-v19.md).
Era: `logi-report-v17-v19`.

## Ground rules

- GET and POST both work for almost every command. POST has no attribute length limit;
  GET does.
- Every example uses the default context path of a standalone install. If the context path
  has been changed, substitute it.
- Resource paths follow the resource tree, not the disk: Public Reports starts with `/`,
  and My Reports starts with `/USERFOLDERPATH/<username>/`.
- Paths in a URL are usually URL-encoded, so `/SampleReports/X.cls` appears as
  `%2fSampleReports%2fX.cls`.

## Running reports: three JSPs

| JSP | Behaviour with parameters |
| --- | --- |
| `tryView.jsp` | The normal entry. Missing or incomplete parameters produce the parameter dialog box. |
| `runReport.jsp` | Same as tryView when the report has no parameters. Otherwise runs with the values you supply, defaults for the rest, and no dialog. |
| `run.jsp` | Studio entry points. Runs with supplied values or defaults. |

```
http://localhost:8888/jinfonet/tryView.jsp?jrs.report=%2fSampleReports%2fEmployee Information List.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=2
```

`run.jsp` has a different path per surface:

- page reports and page report result files: `webos/app/pagestudio/run.jsp`
- web reports in Web Report Studio: `webreport/studio/entry/run.jsp`
- dashboards: `dashboard/app/entry/run.jsp`
- Visual Analysis: `webos/app/designer/run.jsp`
- creating a web report, wizard: `webos/app/webstudio/run.jsp?jrd_wizard=1&`
- creating a web report, quick start: `webos/app/webstudio/run.jsp`

The `jrserver` servlet can also run reports, but it redirects to the appropriate JSP, so the
docs tell you to call the JSP directly.

Source: [Running Reports via URL (v19)](../docs/logi-report-v17-v19/working-on-logi-report-server-via-url-logi-report-server-v19/5741456438167-running-reports-via-url.md).

## The properties you will use constantly

| Property | Meaning |
| --- | --- |
| `jrs.catalog` | Catalog with full path |
| `jrs.report` | Report with full path |
| `jrs.path` | A path, or a resource name with full path |
| `jrs.result_type` | 1 HTML, 2 PDF, 3 Text, 4 Excel, 5 PostScript, 6 RTF, 7 XML, 8 Studio (Page Report Studio for page reports, Web Report Studio for web reports) |
| `jrs.param$NAME` | One parameter value. Multi-valued needs `_isMultiple_jrs.param$NAME=true` first. `%07` means all values. |
| `jrs.param_values` | All parameter values as one escaped `NAME=VALUE,NAME=VALUE` string |
| `jrs.param_page` | `false` suppresses the parameter dialog for the whole run |
| `jrs.rpt_language`, `jrs.rpt_country` | NLS language for the output |
| `jrs.db_user`, `jrs.db_pswd`, `jrs.jdbc_url`, `jrs.jdbc_driver` | Override the catalog's database connection |
| `jrs.wp`, `jrs.named_wp` | Ad hoc or named WHERE portion |
| `jrs.security_file_name` | Replace the catalog's security definitions with a security file |
| `jrs.language` | UI language of the Console or Page Report Studio, lower case, matching the folder name under `<server_install_root>\resources\server\languages` |
| `jrs.report_timeout`, `jrs.timeout_send_email` | Task duration and whether to email on overrun |
| `jrs.auto_refresh_data`, `jrs.auto_refresh_data_time` | Auto-refresh a page report in Page Report Studio, seconds; requires `run.jsp` |
| `jrs.report_sheet$TAB` | Run one report tab, using its report name and not its display name |

Excel output has its own set: `jrs.excel_format` (0 xlsx, 1 xls), `jrs.excel_format_types`
(0 auto, 1 report format, 2 column format, 3 data format, xls only), `jrs.excel_extension`,
`jrs.has_shapes`, `jrs.is_wordwrap`, `jrs.print_header`, `jrs.print_footer`.

Full table: [URL Properties for Running, Scheduling and Viewing Reports via URL (v19)](../docs/logi-report-v17-v19/working-on-logi-report-server-via-url-logi-report-server-v19/5741464843927-url-properties-for-running-scheduling-and-viewing-reports-vi.md).

## Scheduling by URL

Post to `submitSchedPage.jsp` with `jrs.cmd=jrs.submit_schedule`. It returns the schedule
task ID, or a message on failure. A schedule carries two groups of properties, time
information and task information. `jrs.task_class` names the task implementation, in every
documented example `jet.server.schedule.jrtasks.PublishRptTask`. `jrs.launch_type` picks
when: 0 immediately, 1 at a specific time, 8 periodically in the examples given.

Publish to the versioning system as PDF, immediately:

```
http://localhost:8888/jinfonet/submitSchedPage.jsp?jrs.cmd=jrs.submit_schedule
  &jrs.catalog=%2fSampleReports%2fSampleReports.cat
  &jrs.report=%2fSampleReports%2fABC.cls
  &jrs.task_class=jet.server.schedule.jrtasks.PublishRptTask
  &jrs.launch_type=0
  &jrs.uid=admin
  &jrs.to_version=true&jrs.to_version_pdf=true
  &jrs.param$P_StartDate=2016-01-01&jrs.param$p_EndDate=2017-12-31
```

Change format by changing the flag: `jrs.to_version_excel=true`, `jrs.to_version_html=true`,
`jrs.to_version_rst=true`.

Destinations, each with its own flag and supporting properties:

- versioning system: `jrs.to_version` plus `jrs.expire_days`
- disk: `jrs.to_disk` with `jrs.to_pdf` and `jrs.pdf`, `jrs.pdf_dir`, plus
  `jrs.to_disk_pdf_path_type=1` for a real disk path. Omit the path-type property and use
  `jrs.rst_dir=%2fSampleReports` to write into the resource tree instead.
- email: `jrs.to_mail` with an encoded `jrs.jrmail0` bundle carrying `jrs.mailto`,
  `jrs.mailsubject` and format flags
- printer: `jrs.to_printer`
- fax: `jrs.to_fax` with `jrs.to_fax_to_fax_number`
- FTP: `jrs.to_FTP` with an encoded `jrs.ftp0` bundle carrying host, port, user, password
  and location
- bursting: `jrs.is_bursting_task=true` with `jrs.bursting_schema$NAME=true`

Notification: `jrs.success_notify`, `jrs.fail_notify` and `jrs.notification_emails`, whose
value is an encoded `To:`, `Cc:`, `Bcc:` block.

Time properties in the periodic example include `jrs.is_hourly`, `jrs.hours`, `jrs.hour`,
`jrs.min`, `jrs.hour2`, `jrs.min2`, `jrs.is_pm`, `jrs.is_pm2`, `jrs.is_between`,
`jrs.is_weekday`, `jrs.day`, `jrs.days_id`, `jrs.at_min` and `jrs.timezone`. The at-a-time
example uses `jrs.exe_year`, `jrs.exe_month`, `jrs.exe_day`, `jrs.exe_hour` and
`jrs.exe_min`.

Source: [Scheduling Reports via URL (v19)](../docs/logi-report-v17-v19/working-on-logi-report-server-via-url-logi-report-server-v19/5741456465047-scheduling-reports-via-url.md).

## Authentication in a URL

Two mechanisms, both proprietary and both insecure outside a firewall:

- `jrs.authorization=<base64 of userID:password>`, for example `YWRtaW46YWRtaW4%3D` for
  admin/admin. The docs say plainly that it looks encrypted and is not.
- `jrs.auth_uid=USER_ID&jrs.auth_pwd=PASSWORD`.

One trap: JRServlet performs no authentication check when a request has no `jrs.cmd` in the
query at the servlet's root path, and in that case accepts neither mechanism.

Source: [Using the Authentication Properties in URL (v19)](../docs/logi-report-v17-v19/working-on-logi-report-server-via-url-logi-report-server-v19/5741471314711-using-the-authentication-properties-in-url.md).

## Administering the server by URL

Viewing results, adding and deleting principals, resource operations, scheduled task
management, versions, preferences and password changes are all reachable. Two shapes
appear:

**JSP pages**, mostly under `/admin/security/`, for principals. You must be an
administrator and must already have signed in to the Console.

```
http://localhost:8888/admin/security/processNewUser.jsp?currentEditRealm=defaultRealm&user=Dean&...
```

The set is `processNewUser.jsp`, `processRemoveUser.jsp`, `processNewRole.jsp`,
`processRemoveRole.jsp`, `processNewGroup.jsp`, `processRemoveGroup.jsp`.

**Servlet commands** against `/jrserver`, driven by `jrs.cmd`:

```
http://localhost:8888/jrserver?jrs.cmd=jrs.get_cat_rpts_new&jrs.path=/SampleReports
http://localhost:8888/jrserver?jrs.cmd=jrs.get_node_prop&jrs.path=/SampleReports/SampleReports.cat
```

Named commands include `jrs.get_cat_rpts_new` and `jrs.get_subnodes` (resource nodes in a
folder), `jrs.get_node_prop` (node properties), `jrs.delete_resource`, `jrs.view_ver_rst`
and `jrs.view_ver_def` (viewing result versions), and `jrs.submit_schedule`.

Viewing a result depends on its type: page report results (RSD) open in Page Report Studio
through `webos/app/pagestudio/run.jsp`, other formats such as PDF and HTML go through
`jinfonet/viewVersion.jsp`.

Source: [Working with Logi Report Server via URL (v19)](../docs/logi-report-v17-v19/working-on-logi-report-server-via-url-logi-report-server-v19/5741485252503-working-with-server-via-url.md).

## Dashboards and Visual Analysis

JDashboard's entry is `/{context_root}/dashboard/app/entry/run.jsp`. Calling it bare opens a
new blank dashboard. `jrd_lastsession=true` opens the dashboard set as the Console home
page. Specific dashboards go in a JSON `jrd_resext` object holding an `active` index and a
`reslst` array of `{name, ver}`, where `ver` of -1 means latest. Encode it with
`encodeURI`. Web reports opened in Web Report Studio use a similar JSON property,
`jrd_report`.

Sources: [Working with Dashboards via URL (v19)](../docs/logi-report-v17-v19/working-on-logi-report-server-via-url-logi-report-server-v19/5741491211159-working-with-dashboards-via-url.md),
[Accessing Visual Analysis via URL (v19)](../docs/logi-report-v17-v19/working-on-logi-report-server-via-url-logi-report-server-v19/5741471451159-accessing-visual-analysis-via-url.md),
[Creating Reports via URL (v19)](../docs/logi-report-v17-v19/working-on-logi-report-server-via-url-logi-report-server-v19/5741464908183-creating-reports-via-url.md).

## Sample file

`<install_root>\help\samples\URLSamples\TestURL.html` shows how the servlets are called.
Source: [Technical Architecture (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741408039575-technical-architecture.md).

## Era note

The v15 Logi JReport documentation has the same structure and the same `jrs.` property
namespace, split across
[Running Reports](../docs/jreport-v15-v16/working-on-logi-jreport-server-via-urls-logi-jreport-server/1500009650462-running-reports.md),
[Scheduling Reports](../docs/jreport-v15-v16/working-on-logi-jreport-server-via-urls-logi-jreport-server/1500009650522-scheduling-reports.md)
and [Using the Authentication Properties](../docs/jreport-v15-v16/working-on-logi-jreport-server-via-urls-logi-jreport-server/1500009650382-using-the-authentication-properties.md).
The `jrs.` prefix and the `jinfonet` context path survive the rename in both eras, so a
v15-era URL is a reasonable starting point against v19. Properties flagged as new for 19.2
in the v19 set obviously will not work on older builds. An unversioned copy of the same
material sits at
[Working on Logi Report Server via URLs](../docs/unversioned/work-with-server-via-urls/1500009724942-working-on-logi-report-server-via-urls-logi-report-server-v1.md).
