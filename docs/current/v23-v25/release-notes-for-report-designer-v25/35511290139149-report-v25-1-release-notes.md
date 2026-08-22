---
title: "Report v25.1 Release Notes"
id: 35511290139149
section: "Release Notes for Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/35511290139149-Report-v25-1-Release-Notes
updated_at: 2026-03-03T14:17:19Z
source_host: docs-report.zendesk.com
---
# 
Report v25.1 Release Notes

This topic describes feature enhancements, resolved issues, and known issues of the Report v25.1 release, from March 31, 2025.

For more product information, including new purchases and upgrades, contact US Sales or UK Sales.
    

- v25.1 Service Pack 5 Resolved Issues

- v25.1 Service Pack 4 Resolved Issues

- v25.1 Service Pack 3 Resolved Issues

- v25.1 Service Pack 2 Resolved Issues

- v25.1 Service Pack 1 Resolved Issues

- v25.1 Feature Enhancements

- v25.1 Resolved Issues

### Prerequisites

Version 25.1 includes changes to True Type Font (TTF) handling. If you are upgrading from version 23.4 or later, ensure all TTF files used in your existing reports are located in the %ReportHome%/fonts folder before rendering or delivering results. Without this one-time setup, you may experience unexpected font mismatching issues. Once the fonts are properly located, reports will render normally.

### Log4j and Log4Net Vulnerabilities Update

In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: Statement on Log4j and Log4Net Vulnerabilities.
    

## 
v25.1 Service Pack 5 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| Upgrade to 25.1 issue | 05336886 & 05316682 | Following the upgrade to version 25.1, the Escape Formula functionality for CSV files and reports now works as expected. |
| Parser tool issue | None | The parser tool successfully parses all header values and parameter names, and handles special characters as expected. |
| Error When Adding Imported SQL Columns with Subquery Filters | 05330097 | Now, columns from Imported SQL can be successfully added to the Business View (BV) even when a query filter with a subquery is already applied. |
| PowerSchool RTL Preference Not Reflected in Studio | None | Studio now correctly displays RTL layout when jrs.server_profile_direction_display_rtl is set to true in the URL. |
| Exported Excel File Excludes Subreport Index and Links | 05324777 | When both 'On New Sheet' and 'Suppress Subreport Index' are enabled, the exported Excel file now correctly displays the subreport index and associated hyperlinks. |
| Conditional Link Dynamic Field Issue | 05330988 | Editing conditional links no longer results in the loss of dynamic field information under specific conditions. |
| MongoDB URI in log file showed user and pwd. | 05319475 | Logi mask username and password of mongo db connection URI in log. |
| UDS Subreport Data Retrieval Issue | 05302308 | Customer reports now handle data retrieval from subreport UDS more efficiently |
| New Link issue on Bar graph type | 05308820 | Chart link conditions are now reliably preserved during editing, even in complex scenarios. |
| Cascading report filter performance issue | 05317842 | Cache data is now successfully saved when editing cascading parameters. |
| Page number issue | 05317471 | Subreport page numbers now display correctly when the main report’s onNewPage property is set to true. |
| Tile panel sorting issue | 05317471 | Tile panels can now be sorted correctly when the main report’s onNewPage property is set to true. |
| Syntax Errors in OnTheFlyFormula During Catalog Edits | 05310165 | The formula FX_GBMAX_BMS_LOC (OnTheFlyFormula) now retains correct syntax when editing the catalog’s data resource name. |

## 
v25.1 Service Pack 4 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| jrs.profile not applied | None | The issue with specifying a profile using jrs.profile in the JavaScript API is now resolved, and it works as expected. |
| Profile parameter not applied | None | The issue is specifying a profile using jrs.profile in the new report.jsp now works as expected. |
| API failure on multi-value parameters | 05312938 | /report/parameterInformation now supports multi-value parameters. |
| Catalog Rename Fails | 05310165 | In Designer, the catalog is successfully saved after updating the data source name. |
| Formatting issue | 05300521 | In Designer, the catalog is successfully saved after updating the data source name. |
| Temporary file retrieval issue | 05282631 | You can always download the temporary result file using the /sendfile/result link, whether or not it was created on a shared memory node. |
| Public Report Folder Missing | 05256803 | Resource system data now remains consistent even if an update event occurs before the initialization process completes. |
| Group pagination issue | 05292114 | The report now correctly displays each group on a separate page in version 23.4, as it did in version 15.5. |
| Cluster file sync issue | 05291722 | The server can successfully return the required result file without error, even if the file's status is not synchronized across the cluster. |
| Show All Labels Issue | 05298850 | The chart property "Show All Labels" is now correctly saved and read when exporting the report in XML format. |
| Upgrade to 25.1.1 issue | 05287204 | After upgrading to 25.1.1, you can now specify a default BV when selecting a BV to create a web report. |
| Labels border display issue | 05297691 | Labels with border-radius now correctly display rounded corners when placed inside table cells. |
| Word wrap issue | 05295567 | The word wrap property now remains effective when applied to the record number field. |
| Out of memory issue | 05302308 | The type-in parameter no longer retains multiple value lists across repeated subreport iterations. |

## 
v25.1 Service Pack 3 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| SSO token sessionVariable dynamic connection issue | 05297598 | Reports now behave as expected when running report in Schedule Run mode or Advanced Run mode by using "jrd_datasource" parameter to indicate dynamic connection. |
| Empty Date Prompts Cause Incorrect Filtering | 05261396 | The report now correctly shows all records for Open Date and Due Date, displaying both null and non-null values even when SQL filters are applied to these fields. |
| Formula Compilation on WildFly issue | 05244239 | When the Logi server is deployed on WildFly, formula references to user-defined functions can now be successfully compiled. |
| LogiReport server memory spike | 05268779 | The LogiReport server memory spike issue has been fixed. Memory usage is now stable after tuning and optimization. |
| Potential On-Screen Filter Bug | 05273677 | Filter control titles in Web Studio now display correctly when a Dynamic Display Name is configured. |
| Multiple Cross-tab flickering issue | 05261646 | The report with three crosstabs now runs smoothly without screen flickering. |
| Last Page Header Issue with Formula Control | 05268071 | The column header controlled by a formula now displays correctly on the last page with no data. |
| Sorting Issue on Page Report | 05270490 | The behavior of radio button selection in the sort dialog of the page report is now corrected. |
| Border Display Issue in Excel output | 05264167 | The current version now accurately reads the "Full Fill and Border" property values saved in earlier report versions. |
| Inconsistent date in web reports | 05258474 | The report footer now accurately shows the date selected by the user, with no offset. |
| Date Format Issue on VARCHAR Field | 05260507 | Designer now correctly handles String (Numeric) values without converting them to Date type in JSON connections. |
| Blurry Designer Page When Inserting Images | 05225599 | Designer now renders clearly across resolutions when images are added to reports. |
| Restart Delay After Crash | n/a | The server can now restart quickly after a crash, without waiting 2 minutes, if the customer sets the timeout using the -Djreport.restart.timeout option. |

## 
v25.1 Service Pack 2 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| Stacked Charts issue | None | After setting the graph's URL link, the stacked bar and branch charts work correctly on the server. |
| Encrypted Reports issue | 05158939 | When the Logi Report Server is deployed on a web server, customers can now correctly access static resource files with capitalized extensions (e.g., .PDF) via the browser. |
| Mix query Run Issue | 05234008 | Fixed the issue where complex mix queries caused reports to run indefinitely. |
| Catalog mapping issue | None | The stored report-catalog relation will be used if no catalog is specified when running a report via URL, JS API, Web PI, or Java API. |
| Chart shadow issue | 05239739 | In the web studio, the shadow drawing of the chart is now displayed correctly. |
| Label shadow issue | 05239739 | In the web studio, the label shadow is now displayed correctly. |
| Display of tags issue | 05224610 | Page Studio displays the  tag position correctly. |
| Issue with Report-CONTROL-TOWER-ORDER.cls | 05234008 | The report now runs successfully with Report-CONTROL-TOWER-ORDER.cls. |
| Image display issue | 05225599 | Reports now show inserted images clearly in designer view, regardless of resolution. |

## 
v25.1 Service Pack 1 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| Data Loading and Flickering Issue | 05217295 | Now, when editing a web report in Logi Analytics, the data loads successfully, and the screen stays stable. |
| Formatting issues in CSS | None | The chart axis and legend now correctly use the number/date format settings from the CSS file. |
| Connection pool issue | None | The idle time is always 0, so the connection is not terminated based on the expirer_url default setting. This will lead to reaching the maximum limit of 50 connections, resulting in an error due to the lack of available connections. |
| Scrollbar issue | 05231548 | The filter expression dialog now displays the X-scrollbar. |
| Issue with the edit option | 05228028 | When opening a dialog, it will check if the location is within the screen's range. If not, it will use the default location to open. |
| Display issue with library components | 05220213 | Now, when the library component is displayed on the dashboard, the 'displayNull' property of the aggregation field shows correct values. |
| Access issue | 05163282 | Permission check performance improves when the customer specifies that no principal has access to a particular resource node. |
| Realpath Reports issue | 05181037 | In Page Studio, you can now open a report with the real path in a cluster environment. |
| Dynamic connection null pointer exception | 05162034 | Server startup will fail if an exception occurs, preventing a non-functional server instance. |
| Sample images issue | None | Now, if the customer uses a custom style file, the name of the preview image corresponding to the style displayed in the wizard will include the file name. |
| Job Scheduling issue | 05208369 | Now, a scheduled task does not run twice in the cluster, even if one node is down and another node is restarting. |
| 2200 error page | 05144581 | Now, closing and reopening Catalog Studio in the same user session using the browser's close button does not display the 2200 error page. |
| Symbol missing in Query Filter | 05208387 | In the Query Editor filter panel, now single quotes in filter values are not lost when reopening the catalog. |
| Resizing tabular cells issue | 05199468 | In the web studio inspector panel, you can now resize the table cells' width and height. |
| XML save issue | 05161933 | Now, saving the report in XML format correctly saves the chart scrolling area's height. |
| Border issue | 05157416 | Now, even when the browser zoom is 33%, the border of the crosstab cell is also displayed correctly. |

## 
Feature Enhancements

| Title | Description |
| --- | --- |
| Image type support | The software supports the following image types in both studio and PDF: TIF BITMAPINFOHEADER, BiSize = 124. |
| xml properties enhancement | The Output properties orderly in XML format option has been added to the XML tab in Designer > Options > Export to. With this option, you can control whether to save the report or catalog properties orderly in the XML format. |
| "-D" Parameters support | Users can turn on or off the Resource from Real Path function and set default real paths for public reports with the following -D parameters: jreport.enableDynamicResource – to enable or disable resource from real paths. jreport.publicReportsRealPath - has higher priority than server.publicReportsRealPath in install.server.properties. jreport.publicComponentsRealPath - has higher priority than server.publicComponentsRealPath in install.server.properties. |
| Optimizing Quartz Scheduler | Server can run a scheduled task when Quartz misfires the schedule after enabling the Attempt to Run Misfired Periodical Schedule Once option. |
| Third party libraries updates | Upgraded 3rd party libraries to fix vulnerabilities in 24.3.x/25.1. |
| customized security API implementation | With JDK 14 and above, customers can create custom security API implementations based on thejet.server.api.custom.security.BaseAuthorizationProvider interface. |
| rptconv.bat/rptconv.sh enhancement | Upgraded the rptconv.bat/rptconv.sh tool to support multiple catalogs for specific report enhancements. |
| Rest API session control enhancement | When making a web API call, customers can use the forceSessionTerminate request header to specify if the user session should be logged out after the server completes processing. |
| Optimizing Report Execution | When running reports in the built-in UI, the rpt/cat relationship should be effective. |
| Predefined filters support | You can now add predefined filters in the side menu like in web reports. |
| Switch Units Easily | The server now supports switching between metric and imperial units. |
| Enhanced the local image option | Using Web API, you can now add locally embedded images in the report server. |
| Dynamic Subjects & Patterns support | The server supports dynamic subjects for scheduled emails and introduces new patterns [pathrpt/RPT/rpt] for reports. |
| Easy Web Report Alignment | Aligning fields or labels has become easier, but it still involves numerical adjustments for each element one by one. The ability to align elements based on others or to modify multiple selected elements at once is still lacking. |
| Enhanced UI layout | The support page studio now shows the layout from right to left for the main UI. |
| Enhanced REST API | Customers can now wrap SSO API functions with REST API calls. |
| API-Based Image Authentication | The server now supports authentication to an external host for image fetching. The idea is to use parameters to pass the username and password, with values provided solely by the API, making the authentication seamless for end users. |
| Label-Bar Spacing | You can now customize the spacing between data labels and bars. |
| Support for Jakarta EE deployment | The makewar.sh and makewar.bat utility now accepts a new argument, -Djakartaee=true, which generates WAR or EAR files compatible with Jakarta EE-based application servers, including Tomcat 10/11, WildFly 35/36, and others. |
| Scheduled Jobs Now Load Quickly with Icon Display | A new property server.completed.enable_cache has been introduced in server.properties, with a default value of true, enhancing the performance of loading the first page of the My Tasks > Completed section. |
| Support Added for OPTIONS in JSP Responses | Server support has been enhanced to correctly handle OPTIONS requests for JSPs. Response headers such as Access-Control-Allow-Headers and Access-Control-Allow-Origin can now be configured via responseHeader.properties. |

## 
Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| jsoup Vulnerabilities | None | Upgrading the jsoup jar resolves the issue. |
| SFTP Schedule NullPointerException issue | 05155200 | The web API endpoint GET /myTasks/scheduled/list no longer triggers a NullPointerException even if the "logon type" field is missing in an SFTP publish schedule. |
| Legend label display issue | 05028048 | Displays the legend label value accurately based on the series format. |
| Formula Tag Removal | 05133590 | The new built-in function removes the HTML tag flag in formulas |
| Issue with Server Startup with Group-Level Permissions | 05144581 | The server can now start correctly even if a node has only group-level permissions. |
| Errors appearing when Horizontal Alignment=justify and convert HTML=true | 05133590 | Resolved errors appearing when Horizontal Alignment was set to justify and convert HTML tag was set to true. |
| HTML conversion failed in reports exported to PDF or Excel | 05095489 | The software correctly supports the  and  HTML tags written in the uppercase. |
| Width tag issues | 05133590 | The software supports the table-layout attribute of the  HTML tag. |
| Rendering graphs in Logi Server negatively impacts the quality of chart images | 05133590 | Improved the quality of chart images when exporting to PDF. |
| Field formula in the Text Format > Bold section did not work properly | 05133590 | Resolved the issue where the system did not evaluate the result against the formula used on a field in the Text Format > Bold section. |
| Content incorrectly rendered by the server | 05133590 | The software correctly supports the  HTML tags with the Convert HTML Tag option. |
| Position property status display issue | None | The server's template editor now correctly displays the editing status of the "Position" property for the component within the bandedObject. |
| Quick schedule version mismatch | None | In the quick schedule submitted in Page/Web Studio, the catalog and report versions are the same as those used to open Page/Web Studio. |
| Text overlap issue | 04897275 | Resolve an overlap issue with the bandedObject. |
| Issue with DB connection in session | None | Adhoc report creation now uses the session's connection. |
| Issue with Justify alignment | 04886896 | Applying 'Justify' alignment to a formula no longer inserts large spaces in the last line of a paragraph. |
