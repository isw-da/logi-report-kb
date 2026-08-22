---
title: "Report v24.3 Release Notes"
id: 35498446567693
section: "Release Notes for Report Server v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/35498446567693-Report-v24-3-Release-Notes
updated_at: 2025-04-29T17:12:14Z
source_host: docs-report.zendesk.com
---
Next Topic

# 
Report v24.3 Release Notes

This topic describes feature enhancements, resolved issues, and known issues of the Report v24.3 release, from September 30, 2024.

For more product information, including new purchases and upgrades, contact US Sales or UK Sales.

- v24.3 Service Pack 5 Resolved Issues

- v24.3 Service Pack 4 Resolved Issues

- v24.3 Service Pack 3 Resolved Issues

- v24.3 Service Pack 2 Resolved Issues

- v24.3 Service Pack 1 Resolved Issues

- Feature Enhancements

- Resolved Issues

- Known Issues

### Log4j and Log4Net Vulnerabilities Update

In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, see Statement on Log4j and Log4Net Vulnerabilities.

## 
v24.3 Service Pack 5 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| Browser Compatibility Issue with Reports | None | Fixed the issue where scrollbars did not appear for crosstabs and banners in Firefox. |
| Scroller issues | 05076773 | The label date of the format on category X and the date of the scroll bar are now consistent. |
| Crosstab Component Border Issue | 05067934 | When generating PDF files, the crosstab borders are displayed correctly. |
| No parameter, no report | 05062155 | when run report in Server side in case of define the parameter value is required, NO message pop-up and report can be run when there is no parameter value input. |
| Issue of error message "CODE:1005" | None | Catalog Studio now displays the correct runtime code, and the error messages are accurate in the new update. |
| HTML -  Tag Display Issue | 05032684 | The HTML -  tag marker now displays correctly in both Page Studio and Web Studio when 'Ignore HTML Tag' is set to false. |
| Version inconsistency in Quick Schedule submissions | None | The catalog and report versions in quick schedule now match the versions in Page/Web Studio. |
| Sorting not applied | 05034409 | Implemented sorting functionality in the /myTasks/scheduled/list/page API and in the /myTasks/completed/page API. |
| Issue with QR code image | 05021550 | Enhanced the QR code image quality during PDF generation. |

## 
v24.3 Service Pack 4 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| Error message Issue | None | The 'report session is expired' error message no longer appears when opening Catalog Studio already active in another session. |
| Qualifier Update issu | 05021481 | In the Designer, you can now update the qualifier while editing the connection. |
| PageSize API issue | 05034406 | The API of myTasks/com now returns the specified number of records. |
| Border Issue at 67% Zoom | 05029231 | CTField's border not displaying in crosstab, when zooming browserv24.3 Service Pack 3 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| Custom Profile Setup IssueSo | 05003631 | The software correctly saves user permissions when you create a new user from a default administrator account. |
| Incorrect Software Behavior after Users Chose the Cancel Option | None | When users wanted to exit the newly created page report, the software prompted them to either Save or Cancel. The Cancel option closed the report instead of returning to the report. Currently, when users choose the Cancel option, the software allows them to return to the report instead of closing it. |
| Incorrect Software Behavior after Users Chose the Cancel Option | None | When users wanted to exit the report, the software prompted them to either Save or Cancel. Currently, when users choose the save option， the software allows them to save and click ok, then it will popup banner with ‘Save successfully’ and then click ok, it would close the report window instead of exiting report window directly. |
| Error When Applying Changes to the Edited Imported SQL | None | When users edited an existing imported SQL and wanted to apply the dynamic connection, the software displayed an error with default connection. Currently, the users can successfully apply dynamic connection. |
| Dynamic Connection Bug in Auto-Joins | None | Fixed the dynamic connection bug in versions 24.1.6 and 24.3.2, which caused incorrect auto-joins in file query editor. |
| Duplicate Values for Cascading Parameters | 04978653 | Fixed an issue where duplicate values appeared in the filter list when "cache=true" for cascading parameters. |
| Save Error for New Page Reports | None | When creating a new page report and clicking "Yes" on the save prompt, the report now saves correctly instead of showing "Error Code: A0FF0001. |
| Added Fields to Query Filter Expressions Dialog | 04969858 | The Query Filter Expressions dialog will show the views/synonyms fields. |
| Dynamic connection issue | 04976373 | Fixed DBMaintain restore bug where data in DYNAMIC_CONNECTIONS_MAPPING_3 was lost after backup and restore. |
| Lost Web Actions Post | 04973718 | The Web Action List will now include the previously missing web actions. |
| KPI label cutoff issue | 04968599 | The KPI value feature now ensures the entire value in the donut's center appears in the chosen font. |
| Banded object issue | 04969395 | When a page report includes multiple banded objects, the last page also renders even when the first object fills the first page completely. |
| Trouble with chart | 04964065 | The link report works even when the x-axis label is not set to auto. |
| Web API issue | 04959326 | The GET or tree web API endpoint now works correctly without causing the 'cannot read node' error. |

## 
v24.3 Service Pack 2 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| PDF issue when upgraded to v24.3.1 | 04959096 | When the customer sets all borders to none and configures the table radius, the report no longer triggers a null pointer exception during PDF export. |
| Efficient Resource Management in Reports | 04927441 | Optimizing the code enhanced resource release efficiency during report execution. |
| Automatic Font Change on 'Enter' Key | 04886896 | The font family in the text box now does not automatically change after pressing the 'Enter' key. |
| Enhancement of rest API session control | None | When a web API call is made, the customer can specify whether or not to log out the user session by setting a new request header called "forceSessionTerminate" after the server has finished processing the request. |
| Issue with table in footer | 04914282 | The table in the banded group footer now appears in all groupings. |
| Issue with Locating the Formula with Errors | 04922944 | To enable the users to easily find the formula that has errors, the software shows the shorter display name instead of the formula mapping name. |
| Attempt to Share Report Within the Root Folder Causes Errors | 04922856 | Then users can create a shared web report to Public Reports or Organization Reports folder using web API endpoint POST/nodes/shared. |
| Resource Cannot be Found Error when Uploading the File to Designer Preview | 04923780 | The users can successfully preview the file using Designer Preview even if the main report has multiple reports linked and one of them has failed. |
| PDF Support for Uncommon Chinese Characters | 04922363 | PDFs now correctly display uncommon Chinese characters. |
| Viewing Reports with the Enable Waiting Page Setting Checked | 04872956 | The Enable Waiting Page setting no longer slows down the process of running reports. |
| Caching Resources for Faster Operations | 04847803 | Logi Report now accurately caches resources at server startup, resolving issues with slow save as report and load node list processes. |

## 
v24.3 Service Pack 1 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| Fixed field and paragraph issue during PDF export | 04886896 | When exporting to PDF, the field and paragraph text were not aligned on the same baseline, causing formatting inconsistencies. This issue has been resolved, and both elements now appear correctly aligned. |
| Overlapping text in BandedObject fields issue | 04897275 | When using a banded object, instances of overlapping text within a single database field were occurring. This issue has been fixed, eliminating any overlapping. |
| Navigation issue in page reports | 04911806 | When using a page report created from the server, users were unable to navigate between tabs. This issue has been resolved, and tab navigation now works correctly |
| Aggregate formula issue in table group footer | 04909111 | The aggregate formula was not functioning correctly in the table group footer. This issue has been resolved, allowing the aggregate formula to calculate correctly. |
| Logi Report server can do quick schedule for the reports in organization folder | 04904156 | The "Cannot do Quick Schedule in Web Studio" issue for reports in the organization folder has been resolved. |
| Issue with database connection in session | None | The connection to the database works properly when you attempt to create and configure the web report. |
| Overlapping text within a single field | None | Solved the issue of string overlap when using  or  tags. |
| Silent installation bug | None | Fixed the silent installation issue. |
| Error when trying to export the report to PDF | 04898548 | Solved the issue where the web report with major sort in template could not be exported to Excel. Currently, the export to Excel works properly. |
| Justify alignment applied to a formula inserted spaces in the last line of a paragraph | 04886896 | Fixed the issue where the Justify alignment of a formula inserted spaces in a paragraph last line. Currently, Logi Designer correctly prints the paragraph text and field values in viewer. |
| Issue with updating linked catalogs post-renaming | None | Following a catalog rename, the linked catalog in the return data of the GET or nodes web API endpoint is now updated correctly. |
| Deletion issue with interactive reports table | 04871522 | This release fixes the issue where the interactive reports table could not be deleted because of an incorrect SQL statement in MySQL 5.6+. |
| Accessibility issue with blocked threads | 04878163 | Getting locked out of a resource due to a GET connection error will no longer block subsequent update processes for the same resource. |
| Issue with new login requests being blocked | 04862515 | New login requests will no longer be blocked by an expired user session that cannot exit the related engine. |
| Save as Default does not keep parameter settings | 04869133 | The saved default parameter values will take effect the next time this report is run, even if some parameters have the Get Value from API option enabled. |
| Lock issues in the customer cluster environment | 04862515 | The threads are no longer locked in the customer cluster environment and the server is now accessible. |
| Fails to display summary values in chart with UNION Query | 04872325 | The formula in the UNION Query now calculates correctly. |
| Dynamic parameter loses value after refresh | 04850700 | For cascading parameters that allow typing, the values can now be refreshed after entry. |

## 
Feature Enhancements

| Title | Description |
| --- | --- |
| Decide on the report save behavior in profile settings | Before this feature, when you wanted to save the report, the software always displayed the Confirm dialog where you could choose to replace the report or save it as a new version. With this feature, you can configure the software so that it either replaces the report or saves the report as a new version without displaying the Confirm dialog each time. You can configure this behavior by going to Logi Report Properties Panel > Administration > Server Profile > Customize Profile > WebReport Studio and choosing Edit option for a specific profile. In the Common tab, you can disable Always Need Confirm When Saving As option. When the option is disabled, the software displays Default Save Behavior When Report Exists setting with the following options: Replace As version The settings have been added both in the UI, Java API and Web API. |
| Retain descriptions and metadata after saving the report | Before this feature, saving a copy of the report removed descriptions and other metadata. With this feature, the software keeps the data when you save the report copy. To enable this feature, go to the Common tab of a specific report and enable the Copy metadata of original report option. |
| Download catalog or report from server using API | You can now download a catalog or report from server in the POST/nodes/download endpoint using the downloadResourceParam parameter. The “root” value is the root folder of the file, and the “name” value is the name of the file you want to download. |
| Suppression of tabular cell constant level formula | With this feature, you can show or hide tabular cells conditionally so that there’s no wasted space in the report. You can do it by setting the Suppress value to True. Path: Properties > Suppress. |
| Comments in getCompletedTasks API function return value | Before this feature, the return value of the getCompletedTasks funtion didn’t include comments. With this feature, the comments are included in the return value. |
| JDK 21 (LTS) Support | Logi Reports software now supports JDK 21 (LTS). |
| Adding Right-to-left Option to Layout Direction | The Right-to-left option has been added to Layout Direction of preference on UI and Web API. |
| Customizable Data Label Spacing in Report Designer | The report designer enables you to adjust the spacing between data labels and bars. |
| Adjust Data Label Spacing | The web studio allows customization of the spacing between data labels and bars. |
| Tasks Auto Retrigger When Quartz Misfired Certain Scheduler Tasks | insightsoftware has introduced the Attempt to Run Misfired Periodical Schedule Once option to Administration > Configuration > Advanced view. With this option, you can control whether to run a schedule task when Quartz misfired the schedule. |
| Dynamic Name in Subject | Server supports dynamic mail subject when publishing email(s) by schedule, and new patterns [pathrpt/RPT/rpt] are added for report. |
| "-D" Parameters support for real path setup | Customers can enable or disable the "Resource from Real Path" feature and configure default real paths for public reports using the -D parameters: "jreport.enableDynamicResource", "jreport.publicReportsRealPath", and "jreport.publicComponentsRealPath". |
| Creating Security APIs with JDK 14 and Above | The new jet.server.api.custom.security.BaseAuthorizationProvider interface allows customers to develop their own security API implementation based on JDK 14 or higher. |

## 
Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| TextBox issue | 04885271 | The Desig ner view can now accurately display paragraph text with both a background color and justified alignment. |
| Display issue | 04883559 | The 
 tag is now applied correctly following the Logi update |
| Simultaneous report runs cause one cent Issue | 04863795 | You can now run multiple reports simultaneously or sequentially without causing a cent issue. |
| TextBox Misalignment Issues | 04858342 | When using JDK 11+ with the special font ‘Calibri Bold TTF’, the designer view and the PDF now display consistently. |
| Server performance degradation issue | 04864067 | With the recent server performance enhancements, you can now access any folder or run any report faster. |
| Text Truncation and Wrapping issues | 04872789 | When using the ‘Arial Unicode MS’ font and set to bold, the text now wraps correctly and is not truncated on the web page. |
| Date Filters Enhanced for Format Changes | 04866130 | When changing the date format, date filters now work correctly with the applied browser filter on date-type fields. |
| Scrollable Chart Fixed on Mobile Devices. | 04853276 | When interacting with the scrollable chart in the "Add Apps" section on mobile devices, it now functions correctly after the first interaction. |
| Display Values Enhanced in Parameter Selection | 04847805 | You can now see display values instead of bind values in the parameter selection dialog |
| Improved parameter value search on parameter setting page | 04725240 | Server now does not create redundant engine instances when enter parameter setting page with "Open All Reports and Dashboards in New Window" and "Run and Export Report in New Window" are unchecked in preference. |
| Fixed 'Save As' Functionality for Public Reports Folder | 04767563 | When saving reports in V23.4, there was no "Save As" option to the Public Reports folder. This has now been resolved, and you can save it into the Public Reports folder if the user has the required permissions. |
| Duplicate Parameter Issue Resolved for Distinct Settings | 04656407 | The parameter values no longer duplicate when set to distinct, with only unique values listed. |

## 
Known Issues

Report data cut off in PDF due to PDF page size limitation

When you export a report to PDF, some data of the report are cut off in the PDF output when the report contains a large amount of data, and you have applied continuous page mode to the report or set the page size to be larger than 200 inches. This is due to a PDF limitation where the data displayed can be no larger than 200 inches in a single PDF page.

Unsupported go-to action when using dynamic formulas on chart

You get exceptions when you perform the go-to action on a chart that uses a dynamic formula on the value axis and the formula contains group information.

Next Topic
