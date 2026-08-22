---
title: "Report v23.2 Release Notes"
id: 44254209297677
section: "Report Designer v23 (Archive)"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/44254209297677-Report-v23-2-Release-Notes
updated_at: 2026-03-16T01:09:19Z
source_host: docs-report.zendesk.com
---
# 
Report v23.2 Release Notes

This topic describes feature enhancements, resolved issues, and known issues of Report v23.2. Subsequent updates are listed chronologically, most recent first.

For more product information, including new purchases and upgrades, contact US Sales or UK Sales.
    

- v23.2 Service Pack 3 Resolved Issues

- v23.2 Service Pack 2 Resolved Issues

- v23.2 Service Pack 1 Resolved Issues

- v23.2 Feature Enhancements

- v23.2 Resolved Issues

- Known Issues

### Log4j and Log4Net Vulnerabilities Update

In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: Statement on Log4j and Log4Net Vulnerabilities.
    

## 
v23.2 Service Pack 3 Resolved Issues (7/31/2023)

| Title | Case # | Change Description |
| --- | --- | --- |
| Convert Subreports | 03287152 | Server now converts subreports together with primary reports when you use Administration > Other > Converting, and if the subreports need to be converted. |
| Display Data Field as SVG Image | 03065702 | Report now properly displays a data field as image, when you use the SVG decode type for the image data. |
| Formula Applying the join() Function | 03283007 | A formula that applies the join() built-in function can now return correct value. |
| Run Scheduled Bursting Tasks to FTP | 03209298 | Server can now run scheduled bursting tasks to FTP without displaying a ClassCastException error message. |
| Save Parameter Values as Default on Server | 03287763 | Server now applies parameter values you save as the default on the Server Console, when other parameters are specified in session variables. |

## 
v23.2 Service Pack 2 Resolved Issues (6/30/2023)

| Title | Case # | Change Description |
| --- | --- | --- |
| Apply New Web Report Studio Profile | 02853515 | Web Report Studio now displays the Save Bookmark and Bookmark Setting icons on the toolbar as defined for new users, when you apply a new Web Report Studio profile as the default profile. |
| Crosstab with Formula Controlled Column/Row Header | None | Report now properly displays a crosstab, when you use a constant level formula to control the Text property of the crosstab's column/row header label and set the label's Word Wrap property to "true". |
| Dispatch Opened Dashboards in Cluster | 02848791 02821371 | Server no longer displays the "The report session has expired" error message when opened dashboards are dispatched to another node in your cluster to run. |
| Dispatch Sub Bursting Tasks in Cluster | 02981615 | Server can now dispatch subtasks of bursting reports to another node in a cluster. |
| Display Horizontal Tables with Invisible Columns | None | Page Report Studio now displays your horizontal table and page numbers as expected, when the table contains invisible columns. |
| Display Scheduled Tasks | 02854949 | Server now displays the scheduled task list as expected after you upgrade from v14 and restore your realm database. |
| Field Value Containing  Tag | 02866521 | Report now properly displays the value of a field, when the value contains  tags and you set the field's Convert HTML Tag property to "true". |
| Filterable and Sortable Label in BV-Based Page Report | None | You can now use the four properties: Bind Column, Filter Options, Filterable, and Sortable, on labels in business view-based page reports, to enable filtering and sorting based on DBFields bound with the labels at runtime. |
| Inline Style in Field Value | 02851576 | Report now correctly applies the background-color and text-align inline style properties in the value of a field, when you set the field's Convert HTML Tag property to "true". |
| Font Size of Field Value | 02851576 | Report now applies correct font size to the value of a field, when the value contains both  and  tags and you set the field's Convert HTML Tag property to "true". |
| Formula Error When Open Report | None | When you open a report that has expression controlled properties, Designer now no longer displays a formula syntax error message if you reference dynamic formulas in the expressions. |
| Merge Catalogs in Catalog Doctor | 02857646 | When you merge catalogs using the Catalog Doctor, Designer now no longer checks reports in the catalogs to avoid displaying an inappropriate message. |
| No Page Break for Crosstab in Excel Output | 02486131 | Report now properly removes the page breaks in a crosstab in Excel output, when you set the No Page Break for Report Format or No Page Break for Data Format property of the report containing the crosstab to "true" and export the report to Excel in the corresponding format. |
| Parameter Controls in Web Report Studio | 02794349 | After you set the Invisible property of parameter controls to true, and then change true to a formula, Web Report Studio now displays or hides the parameter controls as expected. |
| Print Multiple Report Tabs to PDF | 03053716 | Page Report Studio can now print multiple report tabs to PDF without displaying a "page not existing" error message. |
| Same PDF Outputs on Linux and Windows | 02859131 | Server now displays the same PDF report outputs on Linux as on Windows, when the Convert HTML Tag property of data fields is "true", and if you set the same font and resolution for both operating systems. |
| Set CSS Style Using Session Variables | None | After you set the jrs.has_style=true and jrs.style_group=CSSFileName session variables, Server now applies the CSS to reports and report wizards in Web/Page Report Studio, to replace the style in your server profile. |
| Test Dynamic Connections | 02857549 | Server no longer displays a "driver not found" error message when you test dynamic connections, even if the database driver is not in Server's classpath. |
| Text Between  Tags | 02851576 | When the value of a field contains several  tags and there is text between two  tags, Report now correctly displays the text if you set the field's Convert HTML Tag property to "true". |
| Use Time Zone | None | When the -Dreport.date.withTimezone option is false, Report now does not set time zone offset for date type fields, and uses the JVM time zone instead of the Engine environment time zone for date string values of parameters. |
| Web Report Rendering | 02833612 | Web Report Studio now displays report data as expected without endless delays, when a chart X axis uses a number or date type field. |

## 
v23.2 Service Pack 1 Resolved Issues (5/31/2023)

| Title | Case # | Change Description |
| --- | --- | --- |
| Account Lockout | 02803805 | Server no longer locks your account in an integrated environment after you provide a wrong password on the welcome page once and refresh the welcome page several times. |
| Alias Table in Query | 02582772 | After upgrading from v10 to v19.0, Designer now properly updates the mapping names of columns contained in query filters when the queries refer to alias tables. |
| Connect to Server Through HTTPS | 02800028 | You now can connect from Designer to Server through HTTPS without getting an error message, if your Designer applies JDK 17 or later. |
| Display  in Parameter Value List | 02831895 | Server now displays  in the value list of a parameter in the Enter Parameter Values dialog box as expected, after you search the value list. |
| Export Pie/Donut Chart with Null KPI Value to PDF | 02834164 | Designer now correctly exports to PDF reports containing a pie/donut chart with a null KPI value. |
| Export to PDF | 02579180 | You can now export reports to PDF in Web Report Studio without experiencing long delays, when a bind column parameter has a large number of values. |
| Formula Controlled Font Size | 02796713 | When you use a formula returning a fixed value to control the Font Size property of a field that has an absolute position, Designer now properly applies this value if you set the field's Convert HTML Tag property to "true". |
| Hide Toolbox and Resource View | None | Page Report Studio now does not display Toolbox and Resource View in the Interactive View when you turn them off in the Page Report Studio profile. |
| On-Screen Filters | 02580166 | Web Report Studio no longer excludes usable values of on-screen filters. |
| Parameter Bound with Imported SQL Column | None | Report now properly retrieves values for a parameter that is bound with an imported SQL column, when the imported SQL statement references another parameter. |
| Run Page Reports in Integrated Environment | 02800755 | Page Report Studio now displays report data as expected in an integrated environment, even if it cannot load an associated image. |
| Run Page Reports in RMI Integrated Environment | 02793483 | You can now run page reports in an RMI-integrated environment by setting the request attribute with the "req-params" key, even if this key already exists in Report. |
| Run Report | None | You can now successfully run a report applying a business view that mashes up a table from a JSON connection and a query from a JDBC connection, when the JDBC-based query contains computed columns. |

## 
v23.2 Feature Enhancements (4/28/2023)

| Title | Description |
| --- | --- |
| Callback SQL Queries for JDBC Connection | When creating or editing a JDBC connection in Designer, you can now add callback SQL queries, that Designer executes right after you set up the connection in the Callback SQLs tab of the Get JDBC Connection Information dialog box. Callback SQL queries enable you to configure the session context before running the queries to fetch data for reports. |
| Catalog Studio on Server | You can now create and edit catalogs via the Catalog Studio on Server without having to use the Catalog Manager in Designer. You can set up connections and create queries, business views, stored procedures, imported SQL statements, parameters, and formulas in data sources. By default, Report turns off this feature. You should contact our Sales Engineer to use it. |
| Customizable Start Position of Scrollable Chart | When creating a scrollable chart in both Designer and Web Report Studio, you can now use the Start Position option in the Scrollable Chart dialog box to specify the default start position of the scroll bar for the chart as on the left or right, or on the top or bottom for a bench chart. |
| Enhanced Report Style and Demo Reports | Report now has a new report style called Mellow that provides you with an enhanced and modern look for your reports. Report also updates the built-in demo reports to improve the appearance and usability of your reports. |
| Environment Variables for Docker | Server now provides environment variables that you can configure when you run containers from its Docker image. |
| Search Performance Enhancement | Page Report Studio now enhances search performance in filter controls when there are a large number of records. |
| Specify New Properties to Improve Report Appearance | You can now use more properties to customize borders of the Chart, Crosstab, Table, Data Field, Special Field, Label, and Filter Control objects in your reports to enhance the report look and feel. You can also specify these properties in the CSS styles you apply to the reports. |
| Stop Running Reports | You can now stop running reports on the Server Console > My Tasks page or by the Server web API, when you run them in Web/Page Report Studio using Run, Advanced Run, or the Server API. You can also cancel database running queries. Besides, Server also stops reports and database queries from running after the session or report timeout. |
| Third-Party Package Upgrade | Report upgrades the support for the following third-party packages to newer versions: batik-all, to version 1.16 commons-net, to version 3.9.0 hsqldb, to version 2.7.1 jsoup, to version 1.15.3 log4j, to version 2.20 mongodb-driver-sync, to version 4.7 |
| Update Chart Properties in Template Editor | You can now update chart properties using the Inspector panel in the page report template editor. |
| Upgrade Earlier Version Resources | Server now enhances the upgrade of your earlier version resources including report templates, catalogs, and formulas to adapt to the current version, for better report running performance, when you publish resources to Server, convert them using the Server Console or rptconv.bat/rptconv.sh, or upgrade Server by installing. |

## 
v23.2 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| Alias Table in Query | 02564364 | After upgrading from v10 to v19.0, Designer now properly updates the mapping names of columns contained in query filters when the queries refer to alias tables. |
| Change DateTime Parameter Value to Date | 02517157 | Server now displays the proper error message instead of a NullPointerException, when you select a DateTime parameter value and then manually change it to a date. |
| Change Parameter Value | 02577202 | You can now change the value of a parameter as you want in a business view based report, when a formula references the parameter. |
| Change Parameter Values in Web Report Studio | None | Web Report Studio can now refresh the report data when you change the value of a parameter in a parameter control, if you use a formula expression to control the Invisible property of an object and the expression references the parameter. |
| Clear Accessible PDF in Server Profile | 02518670 | Server now saves your setting after you clear the Accessible PDF option for the PDF format from the Administration > Server Profile > Customize Server Preferences > Export Formats tab. |
| DBField Content Containing "\n" | 02534104 | After upgrading from v15.5 to v19.0, Report now correctly displays the content of a DBField, when the content contains the "\n" newline character and you set the Position property of the DBField to "true". |
| Display Charts in Web Report Studio | 02527851 | Web Report Studio now displays charts as expected in the latest browser, when you place the charts, web controls, and filter controls in one container. |
| Display Columns of Parameters | None | Web Report Studio now properly displays columns of parameters, without exposing the bind columns while the report loads. |
| Display Dialog Boxes with Special Characters | 02509637 | Page Report Studio now transforms special characters like apostrophes (') in report descriptions before displaying them on dialog boxes, so that the dialog boxes appear as formatted. |
| Display Linked Report From Pie Chart | 02560484 | Web Report Studo can now display the linked report after you select a pie chart, when the pie chart has only one value and the Angle Y property is set to 60. |
| Display Slash in User ID | 02551125 | Server Monitor now displays the slash between the organization name and username as expected in the User ID column, when you run reports via the JavaScript API. |
| Drag Library Components in Dashboards | 02559248 | You can now drag library components in dashboards, even if the templates of the library components have non-normal cases. |
| Export Reports to PDF with Many Pages | 02571242 | Server no longer ends your report session when you export reports with a large number of pages to PDF in Web Report Studio. |
| Export to PDF | None | You can now export reports to PDF in Web Report Studio without getting a NullPointerException error message, when a table column header label contains a long string. |
| Limit Business views of Reports | 02802933 | Web Report Studio now displays the proper business views when you add new components in reports, after you limit the business views of the reports. |
| Merge Catalogs Using API | None | You can now successfully merge catalogs that contain user-defined formula functions (UDF) using an API. |
| No Page Break for Crosstab in Excel Output | 02486131 | Report now properly removes the page breaks in a crosstab in Excel output, when you set the No Page Break for Column Format property of the report containing the crosstab to "true" and export the report to Excel in the column format. |
| NULL Parameter Value in JSON URL | 02517114 | Report now no longer adds a white space to represent the NULL value of an Integer parameter, when you reference the parameter in the URL for connecting to a JSON Web Service. |
| Parameter Control Containing Boolean Parameter | None | Report now correctly displays a checkbox for the parameter control containing a Boolean parameter. |
| Property Controlled by Expression with UDF | 02464063 | You can now successfully open and run reports in both Designer and Server, when you use expressions that reference formulas calling user-defined functions to control properties of the reports. |
| Publish Reports with Same Catalog | 02491372 | Server now publishes a catalog once instead of multiple times, when you publish reports from one server to another and all the reports use the same catalog. |
| Remove "False" Prompt from Logs | 02559690 | Server now removes the "false" prompt from the SystemOut and SystemErr logs when your application server starts. |
| Rename Parameter Referenced in Imported SQL Query | 02582232 | Designer now no longer displays a Java error message when you preview a report, if you renamed the parameter referenced in the imported SQL query the report applies. |
| Rename Resources in Cluster | 02580168 | You can now access reports and catalogs from other clustered servers, after you rename them or their folders on a clustered server in a cluster. |
| Run Multiple Results Simultaneously | 02484474 | Server now processes result requests faster, when you open multiple results at the same time. |
| Run Server as Windows Service | 02519306 | You can now run reports as expected after you publish them from the local directory, when you run Server as a Windows Service. |
| Schedule to Excel with Report Format | 02487577 | You can now schedule to run a Logi Report Result to Excel with Report Format, without getting a NullPointerException error message. |
| Server Security Enhancements | None | We have enhanced the Report Server security. |
| Set Dynamic File Name in URL | 02489015 | You can now use jrs.result_file_name to set a dynamic file name, when you run a report and export it to a result file directly via URL. |
| Sort Icon in Table Headers | 02458361 | Web Report Studio now places the Sort icon on the right of table column headers without covering the label text. |
| Update Cascading Parameter Values | 02558464 | You can now change cascading parameter values in reports on Server as expected, when two groups of cascading parameters share the same top-level cascading parameter. |
| Update Scheduled Tasks | 02507786 | Server now saves your changes when you update scheduled tasks via the web API by removing a format from Publish to Disk. |
| Use saveAs() | 02469319 | You can now use the saveAs() JavaScript API function to prevent the Save As dialog box from appearing. |
| Value Display in Pie Chart | 02576067 | Web Report Studio now displays the value of each pie slice on the slice as expected. |
| Word Wrap on Custom Aggregation | 02489015 | Report now properly wraps the content of a custom aggregation, when you set its Word Wrap property to "true". |

## 
Known Issues

Report data cut off in PDF due to PDF page size limitation

When you export a report to PDF, some data of the report are cut off in the PDF output when the report contains a large amount of data, and you have applied continuous page mode to the report or set the page size to be larger than 200 inches. This is due to a PDF limitation where the data displayed can be no larger than 200 inches in a single PDF page.

Unsupported go-to action when using dynamic formulas on chart

You get exceptions when you perform the go-to action on a chart that uses a dynamic formula on the value axis and the formula contains group information.
