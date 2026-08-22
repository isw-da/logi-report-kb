---
title: " Report v25.3 Release Notes"
id: 41686905950349
section: "Release Notes for Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/41686905950349--Report-v25-3-Release-Notes
updated_at: 2026-03-03T14:33:26Z
source_host: docs-report.zendesk.com
---
# 
Reportwe v25.3 Release Notes

This topic describes feature enhancements, resolved issues, and known issues of the Report v25.3 release, from September 30, 2025. Subsequent updates are listed chronologically, most recent first.

For more product information, including new purchases and upgrades, contact US Sales or UK Sales.
    

- v25.3 Service Pack 5 Resolved Issues

- v25.3 Service Pack 4 Resolved Issues

- v25.3 Service Pack 3 Resolved Issues

- v25.3 Service Pack 2 Resolved Issues

- v25.3 Service Pack 1 Resolved Issues

- v25.3 Feature Enhancements

- v25.3 Resolved Issues

### Prerequisites

Version 25.1 includes changes to True Type Font (TTF) handling. If you are upgrading from version 23.4 or later, ensure all TTF files used in your existing reports are located in the %ReportHome%/fonts folder before rendering or delivering results. Without this one-time setup, you may experience unexpected font mismatching issues. Once the fonts are properly located, reports will render normally. 

### Log4j and Log4Net Vulnerabilities Update

In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, see Statement on Log4j and Log4Net Vulnerabilities.

## 
v25.3 Service Pack 5 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| SE Snapshot Report issue | 05488590 | SE snapshot reports now generate successfully without errors. |
| Application Performance Issue | 05487958 | Enhanced concurrency handling to further improve the stability of opening page report studio/web report studio when accessed simultaneously by multiple threads. |
| Report Refresh Button and Loading Icon issue | 05487817 | Refresh button and loading icon now display correctly in reports. |
| Parameter Form Submit Button Unclickable | 05482176 | Submit button in dashboard parameter forms now functions correctly. |
| Japanese Characters in Scheduled File Names issue | 05462279 | Scheduled file names now support Japanese characters successfully. |
| Report Scheduling Slowness issue | 05447307 | Improved compilation reliability for formulas referencing UDFs across all environments. |
| Upgrade Cleanup Issue | None | Upgrade process now successfully removes old version JAR files. |
| Crosstab Order By Field Access issue | 05472817 | Property "Order By" now lists used BusinessView-Resources in Library Component Crosstab. |
| Crosstab Data Population Issue | 05459650 | Crosstabs now populate data correctly when fields are removed from Rows. |

## 
v25.3 Service Pack 4 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| AM/PM display in en_CA Locale | 05462326 | When using JDK 17 or later, date parameters with pattern 'a' display as "a.m." / "p.m." in the en_CA locale. |
| Cell background color misalignment | 05461757 | Crosstab cell background colors now display properly in generated PDF files. |
| Report schedule unsupport Japanese text | 05462279 | Web Report and Page Report schedules now support Japanese characters in email subject lines, file attachments, and body comments. |
| Header/Footer auto-expansion issue | 05456648 | Page header/footer panels no longer automatically expand when large images are inserted. |
| Incorrect date parameter values | 05338273 | Date parameter values now return correctly in JSON format. |
| HTTP/2 issues | None | Compression is now enabled by default, allowing users to access the server through HTTP/2 enabled proxies or gateways. |

## 
v25.3 Service Pack 3 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| Date Format issue | 05444221 | Date formats now display correctly in Excel exports. |
| Unable to Use Existing Data Set on KPI | 05440859 | Users can now select data when using existing datasets on KPI in the web studio. |
| CSS Error in Cloud Deployment | 05433441 | Compression is now disabled by default; re-enable via \bin\servlet.properties. |
| Web Report Conversion issue | 05437028 | Added support for converting web reports in XMLConverterSample.java. |
| Filter - Overlapping Fields | 05431123 | Filter dialog fields no longer overlap when field text is too long. |
| Incomplete Data Display in Web Reports | 05400066 | Minor sort now works correctly on summary tables in scheduled web report exports. |
| Dashboard Logs issue | 05403044 | Dashboard logs are now clearer and easier to collect. |
| Page Break Issue in French | 05373413 | Page breaks and subreports now work correctly in French language reports. |
| Trigger data issue | 05410819 | Users can now attach trigger data when firing a trigger through the PUT /trigger/fire web API endpoint. |
| Grouping issue in Web Report and Page Report | 05359919 | Grouping now works consistently across Web Reports and Page Reports. |
| Merged Cell Display Issue | 05359919 | Text in merged cells no longer truncates when word wrap is enabled. |
| Dark Mode Dashboards and Reports settings | 05382788 | Dashboards now support default dark mode display with the ability to save configuration settings. |

## 
v25.3 Service Pack 2 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| Report Processing Delays | 05402416 | Enhanced the server-side task dispatch mechanism to boost report processing speed and overall throughput. |
| Incorrect Page Breaks in subreports | 05409070 | The ‘On New Page’ property now works consistently on group header panel in main report and subreport. |
| Invalid Query Generation with Grouped Filters | 05403277 | Logi Report now handles grouped filters with complex conditions and record-level formulas without generating invalid SQL. |
| Incomplete Data Display in Web Reports | 05400659 | Web Reports now display the full dataset in the viewer, matching exports for accurate results. |
| Null Pointer Exception on Data Mode Switching | 05384882 | Reports using local parameters now switch seamlessly between partial and full data modes without NullPointerExceptions. |
| Column Alignment Issues in Excel Export | 05403175 | Now it is possible to control the maximum width of Excel columns when exporting Excel. |
| Accessible PDF Tag Order Issues | 05399209 | Accessible PDF settings now work correctly when submitting scheduled tasks via URL, including proper tag order configuration. |
| Table of Contents Not Rendering in Browser | 05403633 | Report browser now shows the Table of Contents properly, consistent with designer and export views. |
| Password Change Default Setting issue | 05401910 | Users can change password in Tomcat-integrated environments once after login if password change is required. |
| Save As API Functionality | 05401204 | Reports can now be saved in XML (.wls.xml) format via Save As API with proper parameter and path handling. |
| Sorting Option Missing in Table Wizard | 05400066 | Sort options are now available in the table wizard after table creation, enabling users to configure sorting anytime. |
| Accessible PDF Settings Not Saving | 05399209 | Logi Report Console (v23.4 SP1) now retains Accessible PDF settings after saving, ensuring consistent configuration. |
| Parameter Retrieval Failure in Database Queries | 05376730 | Report-catalog relationship will always be applied when users run report via server UI even the report has been set the default linked catalog. |
| Slow Report Execution Due to Missing Fonts | None | Report engine now handles missing TTF font files efficiently, eliminating performance bottlenecks during execution. |

## 
v25.3 Service Pack 1 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| Crosstab Field Sorting issue | 05392485 | The Format Crosstab panel in the Template Editor will now display the sort status of crosstab rows and columns in its menu. |
| Timezone issue for Datetime Parameters | 05338273 | The timezone issue affecting datetime-type parameters when running the report has now been resolved. |
| Startup issue | None | Reports created in an English environment now run successfully in a Turkish environment without triggering any errors. |
| Parameter related issues | 05389034 | NLS properties included in the payload of the POST /report/parameterInfos Web API endpoint will now be applied successfully. |
| Incorrect parameter format issue | 05389034 | Catalog studio now displays correct parameter format. |
| Dialog control issue | None | You can now configure dialog behavior using available options when inserting time or date-time resources into BV. |
| Sorting issue | 05388891 | Resource Tree sort type updated to 'No Sort – Normal' to align with query order. |
| Web Report Sorting issue | 05354281 | Sorting is now successful when creating a Web Report, without triggering an Index Out of Bound error. |
| Multi-Tab Reports issue | 05349050 | Web Page Report with multiple tabs now runs successfully without triggering a NullPointerException related to session access. |
| Resource page loading issue | 05345810 | Resource page now loads more quickly with improved performance. |
| Error on the operating system | 05335850 | The server now starts up successfully in a Turkish locale environment. |
| Cluster Rejoin Issue | 05374207 | Both the servers now successfully rejoin the JR24 cluster after restart following a configuration change. |
| JSON Query Filtering Issue | 05371850 | Filtering on a parameter value in a single-table query now works successfully without excluding all data from the Web Report. |
| Valid Emails rejected on schedule page | 05373408 | Email address validation has been improved to successfully accept valid addresses on the Schedule to E-mail page. |
| Filter condition issue | 05355575 | Web Report and Page Report now successfully support multiple filter conditions. |
| Image lacks sharpness | 05369317 | When generating PDF files, image quality for fields with display type set to image is now enhanced. |
| Report filter issue | 05367206 | Report webpage now successfully remains active after responding to popup alerts. |
| Short overflow issue | 05367216 | The MariaDB JDBC driver now successfully handles type constant values exceeding the short range in the getTypeInfo() method without triggering errors. |
| Parameter dialog pop-up issue | 05319475 | Logi Report now successfully retrieves parameters in MongoDB APE, with the parameter dialog appearing as expected during insertion. |

## 
Feature Enhancements

| Title | Description |
| --- | --- |
| Light Theme Added | Added a new 'Light' theme option for the server UI, providing users with an alternative display mode. |
| Server UI Theme Options | Users can now switch between 'Light' and 'Classic' themes in the server UI, allowing customization of the interface appearance based on individual preferences. |

## 
Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| isDirty Flag issue | None | A new function has been added to the JS API to determine whether the current web report is in view mode or edit mode. |
| Error when printing Excel report | 05350171 | When exporting a report result to Excel, filtered tables now display the correct dataset. |
| Issue with Stopping Scheduled Tasks | 05355344 | Scheduled tasks now terminate as expected when exceeding their configured duration, even if the server encounters errors during duration checks. |
| Multi-Select Prompts display issue | 05346956 | When multiple values are specified for the parameter, executing the report consecutively without reopening the parameter input dialog now yields accurate results. |
| Incorrect display of column borders in crosstab format | 05351108 | The inspector tree nodes will be hidden if crosstab column row did not show in the report. |
| Task has been cancelled error | 05337064 | Added support for -D parameters to enhance report control, including preventing execution on DSException and managing maximum page counts. |
| Database Connection Test Failed | 05354178 | When the password remains unchanged under Configuration > Server DB, the system automatically uses the password stored in dbconfig.xml during the connection test. |
| Padding Not Applied in Word Wrap | 05342613 | The field now correctly aligns wrapped text to the right. |
| Arcadis gen upgrade issue | 05353441 | The exporting PDF with TOC component issue has been fixed, and the system is now functioning as expected. |
| Failed to Open Logi Report File | 05343540 | Improved handling of Logi report definition files to ensure they open reliably. |
| Cannot select a user/role/group in Catalog Editor | 05347851 | For Catalog Studio access control, a scrollbar now appears when the users/groups/roles list is long, allowing all items to be easily selected. |
| Blank Cover Page issue | 05292114 | Now the first page is no longer blank in the report (v23.4). |
| Realpath Reports issue | 05181037 | Resolved NullPointerException when opening reports deployed with real path in cluster environment. |
