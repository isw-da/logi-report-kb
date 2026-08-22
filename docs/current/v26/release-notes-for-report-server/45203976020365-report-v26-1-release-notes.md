---
title: " Report v26.1 Release Notes"
id: 45203976020365
section: "Release Notes for Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203976020365--Report-v26-1-Release-Notes
updated_at: 2026-06-29T20:17:38Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Report v26.1 Release Notes

This topic describes resolved issues and known issues of the Report v26.1 release, from March 31, 2026.

For more product information, including new purchases and upgrades, contact US Sales or UK Sales.
    

- v26.1 Service Pack 2 Resolved Issues

- v26.1 Service Pack 1 Resolved Issues

- Report v26.1 Release Notes

- v26.1 Resolved Issues

### Prerequisites

Version 26.1 includes changes to True Type Font (TTF) handling. If you are upgrading from version 23.4 or later, ensure all TTF files used in your existing reports are located in the %ReportHome%/fonts folder before rendering or delivering results. Without this one-time setup, you may experience unexpected font mismatching issues. Once the fonts are properly located, reports will render normally. 

### Log4j and Log4Net Vulnerabilities Update

In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, see Statement on Log4j and Log4Net Vulnerabilities.

## 
v26.1 Service Pack 2 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| File Export Settings wizard fails to expand after upgrade | 05560756 | The file export settings wizard in Logi Report now successfully expands after upgrading from v23, allowing users to access additional options and complete the export configuration. |
| Empty row appears in Excel export when Export to Excel is disabled | 05557177 | Logi Report now correctly excludes rows with the Export to Excel attribute set to false when exporting reports, eliminating the empty rows that previously appeared in Excel export output. |
| Error occurs when adding a field into a table in Logi Report Designer | 05548485 | Logi Report Designer now successfully runs reports containing dynamic query fields without throwing a NullPointerException, resolving the DSException error that previously occurred when adding fields into a table. |
| Subreport does not display in Logi Report v26.1 | 05550909 | Subreports that are part of a main report now display correctly in Logi Report Designer v26.1, resolving the issue where subreports were not rendering when the main report was executed. |
| PDF hyperlink appears incorrectly in Logi Report v26.1 | 05549616 | Hyperlinks in reports exported to PDF from Logi Report v26.1 now display correctly, resolving the appearance issue that caused hyperlinks to render incorrectly in the PDF output. |
| Integer overflow error occurs during report initialization | 05548982 | Logi Report now successfully handles integer overflow data types from the result set by applying safe downgrade compatibility handling for out-of-range metadata values, preventing the error that previously interrupted the initialization flow. |
| Server does not log user or group imports from LDAP | 05539246 | Logi Report Server now successfully writes log entries when users or groups are imported from an LDAP server, allowing administrators to track and audit user import activity. |
| Server in cluster fails to upgrade to shared memory node | 05499837 | A server in a cluster now successfully upgrades to a shared memory node even when the resource.share.realm.dir setting points to a path that does not exist, resolving the exception that previously caused the upgrade to fail. |
| Date parameter throws Invalid format or expression error | 05544357 | Logi Report now successfully processes date parameters without throwing an Invalid format or expression error, resolving the missing resource exception that previously caused date parameter validation to fail. |
| Report fields with Convert HTML tag enabled fail to display during page breaks | 05542843 | Report fields with the Convert HTML tag attribute set to true now display correctly across page breaks, resolving the display issue that previously caused field content to be missing when the report spanned multiple pages. |
| Word wrap attribute does not work in crosstab when Convert HTML tag is enabled | 05542599 | The word wrap attribute for fields inside a crosstab now works correctly when the Convert HTML tag property is set to true, resolving the issue where word wrap settings were ignored when HTML conversion was enabled. |
| Crosstab field width displays incorrectly in PDF when Convert HTML tag is enabled | 05542599 | Crosstab fields with the Convert HTML tag attribute set to true now display with the correct field width when generating PDF files, resolving the width rendering issue that previously caused fields to appear incorrectly sized in PDF output. |
| Unable to create formulas on unioned queries in Logi Report | 05540964 | Logi Report now successfully creates and applies formulas on reports that use unioned queries, resolving the exception that previously prevented formula creation when multiple queries were combined using a union. |
| Invalid mapping name error occurs on unioned queries | 05540964 | Logi Report now successfully processes reports with unioned queries that contain mapping names, resolving the InvalidEntityException that previously caused the mapping name to be flagged as invalid with the current query. |
| Images inside HTML table tags do not render correctly | 05542741 | Images inside HTML table tags now display correctly when using the HTML tag rendering feature in Logi Report, resolving the issue where images were not rendered when embedded within table elements in HTML content. |
| Refresh and clear all filter buttons stop working on custom dashboards | 05541145 | The Refresh and Clear All Filter buttons on custom dashboards now work correctly after repeated use, resolving the issue where these controls stopped responding after one or two clicks on newly created custom dashboard reports. |
| Scroll bar missing in Edit Formula window in Logi Report Server | 05542454 | The Edit Formula window in Logi Report Server now displays a scroll bar correctly, allowing users to scroll through and edit formulas that exceed the visible area of the window. |
| Cubes are deleted or stop working after an edit is applied | 05542454 | Cubes in Logi Report now work correctly after being edited, resolving the issue where cubes were being deleted or failing to cache results after an edit was applied. |

## 
v26.1 Service Pack 1 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| Issue with Always Latest Version option | 05520501 | The 'Always the Latest Version' option for Report Version and Catalog Version in Ad Hoc Report Scheduling now persists correctly after selection, allowing users to configure this option successfully without the setting reverting unexpectedly. |
| NullPointerException issue | 05524914 | Scheduled reports now run successfully. The server now cleans orphan folder records before processing, preventing the NullPointerException that previously caused scheduled publish operations to fail. |
| Banded Object Position issue | 05510941 | Page reports that use banded objects in Logi Report Server can now be edited successfully without encountering an error when returning from the Template Editor to Page Studio. |
| Dashboard PDF Export issue | 05527968 | Dashboards that previously failed to export to PDF from the JDashboard viewer now export successfully, with the PDF generated and displayed correctly. |
| Chart Diagonal Pattern issue | 05527584 | Charts with diagonal texture patterns now export to PDF correctly, with lines rendered without misalignment or distortion when vector graphics are used. |
| JRotator Out of Memory issue | 05523645 | Reports using JRotator with certain fonts now run successfully without triggering out of memory errors. |
| Report Link Error | 05525195 | Web reports in the Organization Reports folder can now successfully add a Report link type and browse for linked reports without encountering an error. |
| Issue with Dashboard Log | 05425058 | Dashboard logs now successfully capture the username, parameter values, and ticket information at the start of each dashboard action and refresh. |
| Parameter Shuttle Control issue | 05524572 | The parameter shuttle control now correctly displays selected values on both panes simultaneously across Page Report, Web Report, and the Server Parameter page, with a new server option allowing multi-valued parameters to remain visible on both sides. |
| Parameter Form Control issue | 05511024 | Blank values in Parameter Form control can now be selected successfully in Web Studio. |
| Thai Characters Overlapping issue | 05520740 | Thai characters using the Sarabun-Regular font now render correctly without overlapping or misalignment when exporting reports to PDF. |
| Catalog Studio ERR_2200 Error Message | 05514040 | Catalog Studio error messages, including ERR_2200, now display the username of the user currently editing the catalog, allowing administrators to quickly identify and resolve locking conflicts. |
| Issue with 'IN' Operator | 05524218 | The 'IN' operator in filter web actions now works correctly for both server-side filtering and multi-parameter value scenarios. |

| Title | Description |
| --- | --- |
| Publish reports from Designer to Server on local Docker container | Logi Report Designer now successfully publishes reports to a Logi Report Server running on a local Docker container by packaging and uploading report files as a zip instead of reading from the local disk path. |

## 
v26.1 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| Report Runs Interactively but Not in Schedule | 05508417 | Reports that previously failed when run as scheduled tasks now execute successfully, resolving a query execution error caused by SELECT DISTINCT and ORDER BY expression conflicts. |
| Designer Upgrade: Group Cast Exception | 05510584 | Reports upgraded from older versions to v25.3 now open successfully without throwing a Group cast exception (JetUResourceEntity). |
| Line Drawing Objects Stretching into BPH Sections in PDF | 05508478 | Line drawing objects in the DT section now stretch correctly to the next DB section below, and no longer extend incorrectly into BPH sections in PDF output. |
| Logi App Server High Memory and CPU Usage | 05478443 | Queries during scheduled bursting reports are now closed successfully after execution, and cached rawQuery pointers at the DC level are now closed correctly, preventing resource accumulation that previously caused OutOfMemory errors and server downtime. |
| Measurement Unit Conversion Issue in Designer | 05502995 | Component property fields (X, Y, Navigation Height, Navigation Width) now retain the values entered by the user and no longer convert them automatically from centimeters to inches. The X value now also retains its correct input after the Height field is changed. |
| Application Performance Issue – Thread Blocked | 05487958 | Web Report Studio and Page Report Studio now open successfully without performance delays, resolving a global lock contention issue that previously blocked up to 104 worker threads. |
| Dashboard Logging Enhancements | 05425058 | Dashboard logs now record the username successfully at the start of each dashboard action, and now capture default parameter values successfully when the parameter dialog is not displayed by the user. |
| Incorrect Scrollbar in Page Studio with Long Instance Names | 05483634 | Page Report Studio now displays the instance name list correctly without showing an incorrect scrollbar when long instance names are included. |
| Datetime Export Issue in Excel | 05497460 | Datetime field values now export successfully to Excel with the correct date, resolving an issue where only the Unix epoch date (1/1/1970) was shown. |
| RTF Export – Repeated Images in Related Images Section | 05490403 | RTF exports now display all images correctly in the related images section, resolving an issue where the same image was repeated instead of showing different images. |
| Running Report Issue – Parameter Value List Not Paginated | 05487755 | The parameter value list now paginates successfully when multi-values are enabled and the Enable All Values option is set to true.a |
| XLS Export – Misalignment When First Banded Has No Records | 04951407 | XLS exports now display banded sections correctly, resolving a misalignment issue that occurred when the first banded wizard contained no data. |
| XLS Export – Blank Rows in Column Format | 04951407 | XLS exports in column format now render correctly without blank rows when word wrap is enabled. |
