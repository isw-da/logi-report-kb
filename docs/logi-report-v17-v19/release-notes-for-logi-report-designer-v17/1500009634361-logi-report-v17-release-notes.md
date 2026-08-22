---
title: "Logi Report v17 Release Notes"
id: 1500009634361
section: "Release Notes for Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009634361-Logi-Report-v17-Release-Notes
updated_at: 2022-03-01T06:36:23Z
---

# Logi Report v17 Release Notes

[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009634381-Logi-Report-v17-Enhancements)

# Logi Report v17 Release Notes

This topic describes feature enhancements, resolved issues, and known issues of Logi Report v17. Subsequent updates are listed chronologically, most recent first.

* [v17 Update 1 Feature Enhancements](#h_01FR2FS0ZRRTEBYWZ1C89EH6Q3)
* [v17 Update 1 Resolved Issues](#h_01FR2FS6AMP484WVSZP4VH4BC8)
* [v17 Feature Enhancements](#h_01FR2FSPQB2P4R51774WPKYSM7)
* [v17 Resolved Issues](#h_01FR2FSWX3TAG8JRGBJD89YB5S)
* [Known Issues](#h_01FR2FT2D2KVDMX9GZ4V1CN50J)

### Log4j and Log4Net Vulnerabilities Update

In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: *[Statement on Log4j and Log4Net Vulnerabilities](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751)*.

## v17 Update 1 Feature Enhancements

| Title | Description |
| --- | --- |
| Server URL - Responsive View | You can now turn off Responsive View in the view mode of JDashboard or Web Report Studio on computers when running dashboards or web reports via URL, by setting the property jrd\_responsive to "false". |

## v17 Update 1 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| Heat Map - Send Sync | 71045 | You can now select the Send Sync option after right-clicking a heat map in JDashboard to send sync messages from Heat Map in your dashboards. |
| Server - Batch Refresh Dynamic Resources | 71089 | The Server administrators can now use the Batch Refresh Dynamic Resources feature to update the dynamic resources saved in reports correctly. |
| Server - Cluster | 71514 | You can now always run reports successfully in a Logi Report Server Cluster when you set server.enableMultipleLogin=false for the cluster. |
| Server - Dynamic Display Names | 71527 | You are now able to select business view elements in a catalog to define their dynamic display names, after you remove a business view from the catalog, and if you have already defined dynamic display names for several elements in the business view. |
| Server RMI | 71801 | Logi Report Server RMI environment can now initialize successfully, and RemoteReportServerToolkit.getRemoteWrappedRptServer() now returns the proper value after you call jet.server.tools.DBMaintain to backup or restore DB and then start Logi Report server in the same VM. |
| Web Report - Filter Crosstab | 71587 | You can now apply filters to a crosstab in a web report multiple times, without causing an out of memory error. |
| Web Report Studio - Crosstab | 72089 | You can now always see the labels of the aggregation fields without them disappearing, in a crosstab in Web Report Studio when you scroll the data horizontally, and if the crosstab contains over 30 columns. |
| Web Report Studio - Parameter | 71468 | You can now see the correct display column value in the Parameters panel in Web Report Studio, after you sort the values in the drop-down list of a parameter, select a value, and then select Apply, when the parameter binds with a column and uses another column as the display column, and when the values are more than 500. |

## v17 Feature Enhancements

| Title | Description |
| --- | --- |
| API - ReportCallback | You can now implement the callback interface jet.bean.ReportCallback to audit the Export, Print, and Save actions performed on reports. For more information, select [Auditing on Exporting, Printing, and Saving of Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009605102-Auditing-on-Exporting-Printing-and-Saving-of-Reports). |
| Business View - Element Name | You can now have database table names removed automatically from the display names of business view elements. |
| Business View - Filtering Resources | You can now choose the view elements in a business view and use them as the resources for filtering report data. For more information, select the following links:   * [Creating Business Views in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009613102-Creating-Business-Views-in-a-Catalog) * [Business View Editor Dialog](https://devnet.logianalytics.com/hc/en-us/articles/1500009607342-Business-View-Editor-Dialog) * [Select Filter Resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009633541-Select-Filter-Resources-Dialog) |
| Business View - Hierarchy | You can now create a hierarchy directly from the different time levels of a timestamp field when adding the field into a business view. For more information, select the following links:   * [Creating Business Views in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009613102-Creating-Business-Views-in-a-Catalog) * [Select Time Interval Dialog](https://devnet.logianalytics.com/hc/en-us/articles/1500009610402-Select-Time-Interval-Dialog) |
| Business View Editor - Sort | You can now select multiple elements to move them up and down at a time and sort view elements in either ascending or descending order conveniently, in the Business View Editor. For more information, select [Creating Business Views in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009613102-Creating-Business-Views-in-a-Catalog). |
| Business View Resource Tree | You now have the option to collapse the nodes in the business view resource tree by default, so you do not see data fields within the resource list. |
| Catalog - Imported SQLs | You can now keep your customized mapping names of the columns after you update imported SQLs. |
| Catalog - Merge | You can now keep the connection property values in the target catalog using the Skip button while merging catalogs. |
| CSS - Chart Line and Node Objects | You can now save the properties specified on the lines and nodes of a line chart respectively into CSS files by selecting either the Line or Node object on the chart and accessing Save Style on its shortcut menu. |
| Designer - Bar Chart | You can now customize the bar gap in bar charts even when the Fixed Bar Width property is true. For more information, select the following links:   * [Formatting the Bars in a Bar/Bench Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009628561-Formatting-the-Bars-in-a-Bar-Bench-Chart) * [Format Bar Dialog](https://devnet.logianalytics.com/hc/en-us/articles/1500009608342-Format-Bar-Dialog) |
| Designer UI Scale | You can now customize the scale ratio based on your device requirements to make the graphics and text on the Logi Report Designer UI shown in the size you expect. |
| Export - Excel - Height/Width Auto Fit | Logi Report now disables Height/Width Auto Fit in the page setting for exporting a newly created report to Excel by default, to improve the performance of the exporting process especially for a huge report. For more information, select [Page Setup Dialog](https://devnet.logianalytics.com/hc/en-us/articles/1500009609582-Page-Setup-Dialog). |
| Export - PDF - 508 Compliance | You can now set numbered headings on labels and fields for 508 Compliance support in PDF report result. For more information, select [DBField Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009635341-DBField-Properties). |
| Export - PDF - Default Zoom | When exporting a report to a PDF file, you can now specify the default zoom to apply when the PDF file is opened in Adobe Acrobat Reader. For more information, select the following links:   * [Exporting to PDF](https://devnet.logianalytics.com/hc/en-us/articles/1500009611002-Exporting-to-PDF) * [Export to PDF Dialog](https://devnet.logianalytics.com/hc/en-us/articles/1500009631101-Export-to-PDF-Dialog) * [PDF Option](https://devnet.logianalytics.com/hc/en-us/articles/1500009609522-PDF-Option-Dialog) |
| Filter - Empty String | You can now filter data records that are empty string through dataset filter, component filter, and query filter specified at runtime, and apply conditional link and format to them. For more information, select [DBFields](https://devnet.logianalytics.com/hc/en-us/articles/1500009629081-DBFields). |
| JavaScript API - Dynamic Security | Logi Report improves the JavaScript API to fully support defining dynamic security on business view elements. |
| JDBC Database - Quote Names | You can now keep the uppercase or lowercase characters in the names of the resources in a JDBC database while using the resources in Logi Report Designer, by setting the new property Quote Names added on the JDBC Connection object in a catalog |
| License Control | Logi Report now supports machine specific license control to restrict installing Logi Report products to permitted computers only. |
| Log - DailyRollingFile Appender | You can now specify the maximum rolling file number for the DailyRollingFile appender when configuring log via LogConfig.properties that is stored in the `<install_root>\bin` directory. |
| MongoDB Data Source - Distinct Count | Logi Report can now push down the calculation of the Distinct Count function of an aggregation to MongoDB for speeding up performance when there are a large number of records, as long as it is the only aggregation in a data component and is positioned at the lowest group level. |
| Name Length | Logi Report Server now allows administrators to name organizations, users, groups, and roles within 255 characters. |
| Pie Chart - Static Data Label | You can now use the option Show Truncated Label to show static data labels that are hidden on pie or donut charts after you upgrade Logi Report from a version earlier than v15 to v17. For more information, select [Format Pie Dialog](https://devnet.logianalytics.com/hc/en-us/articles/1500009608522-Format-Pie-Dialog). |
| Query Filter | You can now reference functions that are predefined in the database with qualifiers when editing query filter conditions. |
| Report Database - InterSystems IRIS | You can now set up catalog data source connections to get data from InterSystems IRIS databases using the InterSystems IRIS Connection Plugin Logi Report Designer provides. |
| REST Web Service Data Source - Proxy | You can now set proxy parameters in a configuration file for connecting to a REST Web Service as the data source via a proxy. For more information, select [JSON Connections](https://devnet.logianalytics.com/hc/en-us/articles/1500009606902-JSON-Connections). |
| Server - Dynamic Resources | Logi Report Server administrators can now recompile the dynamic resources in reports for them to work normally when there are changes in the business views used by the reports. |
| Server - Login User Name | The server administrators can now set the server profile option Case-Sensitive Login User Name to enable or disable Logi Report Server from checking the case format of the login user names. |
| Server - Running Report | You can now decide whether to run a report only once or multiple times to avoid repeated running of the report when Logi Report Server detects the submit of running the report more than once within a very short time. |
| Server - Result Version Download | You can now download the output files of a report result version to the local disk for easy viewing. |
| Server Database - Connection Properties | You can now specify any special connection properties for any purposes for connecting to a database server, for instance, the socket timeout for the Oracle database connection. |
| Server Database - InterSystems IRIS | You can now use an InterSystems IRIS database as the Logi Report Server system database. |
| Server Database - Realm DB Archive | You can now archive the data that is generated after a specified date time in the realm database of Logi Report Server. |
| Server Database - Sybase JDBC Driver | The Logi Report Server system database now supports the latest Sybase JDBC drivers such as sajdbc4.jar and jconn4.jar. |
| Stored Procedures - Sort and Search | You can now sort and search stored procedures when adding stored procedures to a catalog via the Add Stored Procedures dialog. |
| Subreport | You can now insert a subreport in a page report that is created using a business view, using Logi Report Designer. |
| Third-Party Package Upgrade | Logi Report upgrades the support for some third-party packages to newer versions. |

## v17 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| Banded Object - Subreport |  | You are now able to see the uncut subreport when a detail panel in a banded object contains a field and a subreport, where the field crosses pages with its first row placed at the beginning of the second page, and the Y location of the subreport is higher than or equal to the height of the field's first row. |
| Catalog - Parameter | 70081 | You can now open a catalog of an earlier version even though there are invalid parameters when the parameters bind with columns whose tables have been deleted. |
| Catalog - Where Condition Group | 37443 & 38331 | You can now view a catalog of an earlier version that had a SQL Where condition group in the query statement. |
| Catalog API - Query Resources | 69124 | You can now use the Catalog API instead of the Query Editor UI to update query resources in a business view. For more information, select [Using Catalog API to Manage Catalogs](https://devnet.logianalytics.com/hc/en-us/articles/1500009628161-Using-Catalog-API-to-Manage-Catalogs). |
| Chart - Sort | 38516 | You can now see the correct sort order when you sort the category of a stacked bar chart by summary, and enable Top N of the category. |
| Chart Legend Label Properties | 67553 | Chart legend now display properly with enhanced label height calculation when the legend label properties Show Values or Show Percent is true and Word Wrap is also true. |
| Cross-Origin Frame | 69212 | You can now access a cross-origin frame when Logi Report Server is embedded within an iframe at the third or deeper level. |
| Designer - Custom Sort | 69046 | You now see the correct sort order after you download a summary table created using Web Report Studio to Logi Report Designer and change the custom sort from sorting by a group column to by a summary column. |
| Designer - Report | 69127 | You can now open an earlier version report in Logi Report Designer even when a dynamic formula in the report fails to be recompiled. |
| Designer - Stored Procedure | 37428 | You are now able to see the stored procedures of a previous version in Logi Report Designer and see the reports using data from them. |
| Dynamic Formula | 68875 | You can now reference a user-defined formula imported using UI in a dynamic formula and save the dynamic formula as a group object successfully. |
| JDashboard - Filter Control | 69956 | When running dashboards that contain filter controls in Internet Explorer, you can now select the Calendar icon Calendar icon to specify date and time values for Date/Time fields in the Edit Filter Control dialog. |
| JDashboard - Parameter | 69111 | You can now see the correct order in the parameter value list after sharing the same name parameters used by different library components in a dashboard and merging their values. |
| JDashboard Profile | 68864 | The option Show Enter Parameter Values Dialog in the JDashboard profile now works properly. |
| JDashboard - Slider Filter Control | 69956 | You can now use the Slider filter control which is bound with Date/Time fields with special functions to filter the table components in a dashboard. |
| JREngine.jar |  | Logi Report Server and Designer now have JEncoding.properties added in JREngine.jar in the directory `<install_root>\lib`. |
| Linked Catalog | 70840 | When you run a report that uses linked catalog which holds several versions on Logi Report Server, the Server can always apply the correct catalog version for the report now. |
| Oracle SP UDP - Report |  | You can now see reports using data from Oracle SP. |
| Page Report Studio - Filter dialog | 68971 | You can now see the correct field names with NLS support after reopening the Filter dialog in Page Report Studio when working on a report created using Logi Report Designer. |
| Parameter - Customized SQL | 68398 | The customized SQL statement of a parameter that is bound with a single column can now get the correct URL of the dynamic connection. |
| Parameter - Value Word Wrap | 70793 | The Word Wrap property now works correctly on values of multi-valued parameters that apply different Bind Column and Display Column. |
| PDF - HTML Tag Conversion | 67726 | Logi Report now parses the two HTML tag elements <span></span> and <a></a> in report data fields successfully when exporting the reports in the PDF format. |
| Server Administration - Resource Conversion | 69127 | Logi Report now converts reports of an earlier version in a folder that does not contain a catalog successfully to adapt to the current version, using the catalogs the reports are linked to. |
| Server - Change Password | 69784 | An organization admin can now successfully change his password for logging in Log Report Server, using either the server console or the RESTful Web API. |
| Server - Completed Tasks | 37424 | The My Tasks > Completed page in the Logi Report Server console can now quickly display 3000 completed tasks to a user who is not an administrator. |
| Server - CORS | 68582 | You can now create new users using Logi Report web API in a remote Logi Report Server from a different origin, without being blocked by Cross-Origin Resource Sharing (CORS) policy. |
| Server - JavaScript API | 68719 | jreportapi.js now does not intercept and cancel touch and mouse events outside the iframe when Logi Report Server is embedded in the customer's application within an iframe. |
| Server - Parameter | 69156 | You can now get correct date and time values when editing expressions with the currentdate() function to specify Date/Time parameter values. |
| Server - Quick Schedule | 69021 | You can now see the correct time for the next run when you use the quick schedule to run reports periodically. |
| Server - Quick Schedule | 83952 | You can now perform quick schedule on a report only when you have the schedule permission on it. |
| Server - Report | 69126 | A report in a folder that does not have a catalog now runs successfully with the correct version of the linked catalog, upon clicking the Run, Edit or Advanced Run button on its floating toolbar in the Logi Report Server console. |
| Server - Report | 67648 | Reports now run successfully as scheduled in Logi Report Server even when the parameter value file does not contain all the required parameters. |
| Server - Security | 86082 | An organization administrator can now add members to groups and roles in the organization without errors. |
| Server - TTF | 68583 | Multiple True Type Fonts specified on objects in a report now all take effect when the report runs in Logi Report Server. |
| Server Database - InterSystems Caché | 69367 | You can now see dashboards in the resource list and Logi Report Server can now start successfully without recreating system tables after you upgrade Logi Report Server from an earlier version that used InterSystems Caché as the system database. |
| Web Report Studio - Default Report Style | 70136 | You can now apply your own style as the default style when creating new reports using Web Report Wizard in Web Report Studio. |
| Web Report Studio - Heat Map | 69897 | You are now able to see the correct color in a heat map in Web Report Studio when using a formula to define the conditional fill color. |
| Web Report Studio - KPI Conditional formatting | 69103 | Conditional formatting specified on labels or fields in a KPI now takes effect right after the report opens in Web Report Studio, without having to refresh the report. |
| Web Report Studio - Label Properties | 68936 | You can now see label text in the correct position in the lab el when the Vertical Alignment property value is Center in the Web Report Studio. |
| Web Report Studio - Label Properties | 68936 & 68576 | You can now see a label in the proper position in Web Report Studio when it has a thick border or has the X property customized. |
| Web Report Studio - Library Component | 68878 | After opening a report in Web Report Studio, an organization user can now save a data component in the report as a library component successfully without errors. |
| Web Report Studio - Sort | 70734 | The Sort function now works properly on data fields of the nvarchar(max) type in Web Report Studio. |
| WebSphere - DHTMLContext |  | DHTMLContext.init in jet.webreport.client.DHTMLContext.java can now initiate normally in WebSphere, which no longer causes incorrect JSP URLs. |

## Known Issues

**Report data cut off in PDF due to PDF page size limitation**

When you export a report to PDF format, you will find that in the PDF result some data of the report are cut off if the report contains a large amount of data but its page mode was specified to be continuous page mode or its page size was set to be larger than 200 inches. This is due to a PDF limitation where the data displayed can be no larger than 200 inches in a single PDF page.

**Unsupported go-to action when using dynamic formulas on chart**

You will get exceptions when you perform the go-to action on a chart which uses a dynamic formula as its shown value and the formula contains group information. This is a limitation in the current version. It will be resolved in a future release.

[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009634381-Logi-Report-v17-Enhancements)
