---
title: "Report v24.1 Release Notes"
id: 28898308752269
section: "Release Notes for Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28898308752269-Report-v24-1-Release-Notes
updated_at: 2025-04-29T17:12:13Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Report v24.1 Release Notes

This topic describes feature enhancements, resolved issues, and known issues of Report v24.1. Subsequent updates are listed chronologically, most recent first.

For more product information, including new purchases and upgrades, contact US Sales or UK Sales.

- v24.1 Service Pack 6 Resolved Issues

- v24.1 Service Pack 5 Resolved Issues

- v24.1 Service Pack 4 Resolved Issues

- v24.1 Service Pack 3 Resolved Issues

- v24.1 Service Pack 2 Resolved Issues

- v24.1 Service Pack 1 Resolved Issues

- v24.1 Feature Enhancements

- v24.1 Resolved Issues

- Known Issues

### Log4j and Log4Net Vulnerabilities Update

In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: Statement on Log4j and Log4Net Vulnerabilities.

## 
v24.1 Service Pack 6 Resolved Issues (9/06/2024)

| Title | Case # | Change Description |
| --- | --- | --- |
| Time zone error | 04822269 | Logi Report now correctly applies the configured time zone setting for both fetch time and print time. |
| Server temp folder not clearing | 04848110 | The application now correctly applies the server setting to delete temp files after 24 hours. |
| Export to PDF error | 04840763 | When exporting a report to PDF using API, the task no longer fails when using a non-admin account and the report runs successfully. |
| Updating the Properties panel | 04851028 | When adding or editing parameters in the catalog, any modified properties are now applied successfully. |
| Inaccurate 200 (OK) code returned | 04851016 | When updating a report name via API, the Logi Web API now verifies if the report name already exists and returns the appropriate error code if it does. |
| Web report preview error | 04845625 | You can now successfully preview a web report. |
| Incorrect HTML formatting of the margin | 04847510 | The HTML formatting of the margin has been fixed. |
| The reports did not display for the user in a public folder | 04780308 | The reports in a public folder are properly displayed. |
| Logi Report Designer installation failed after selecting JDK | 04770097 | The Select JDK issues have been fixed. During Designer installation, the wizard no longer shows the error after selecting JDK. |
| Exception in error logs after deleting the profile | None | Now the Server can startup completely with a empty server DB and there are existing profiles but no profile with "New Profile1". |
| Checkboxes working improperly | 04822849 | The working of checkboxes has been fixed so that you can check and uncheck items as expected. |
| Not possible to translate the Title property of the TOC (table of contents) using NLS | 04839811 | Logi Report now supports the translation of the Title property of the ToC object for NLS. |
| The column header field in a Crosstab does not display the background correctly in PDF format if the field is converted from an HTML tag. | 04827048 | The Report PDF can now accurately display the background of the Crosstab header field. |
| The alignment and spacing of content that starts with a bullet point was inconsistent. | 04832636 | The inconsistency with alignment of bullet points is resolved, and the PDF output renders as expected. |
| Users encountered a ClassCastException error in the Crosstab when selecting the Go to Detail option. | 04832631 | This issue is resolved, and users can now navigate to the Go to Detail option successfully. |
| The catalog credentials were visible even when the user did not have administrator privileges. | 04833902 | The user password for the JDBC connection on the Connections tab of the catalog's version properties page is now hidden. |
| The delete button was visible even when Delete permission was not granted. | 04833151 | This issue is resolved, and the delete button now only appears for users who have the appropriate delete permission. |
| Improved line-breaks in formula outputs | 04826729 | When concatenating text formulas, now you can insert line breaks between output lines for accurate multi-line display. |
| Fixed Support for HTML 
 Tag | 04825511 | When converting HTML, support for the 
 tag has been fully implemented. This ensures proper rendering of line breaks. |
| Label cut off with X-axis title and top position | 04814099 | When chart legend's position is top, X-axis's title no longer gets cut off. |
| Parameter Retrieval Issue in Report Folder Resolved | 04821012 | When accessing reports in a specific folder on the server, the issue with parameters not retrieving values from the backend is now resolved. |
| Connection Pool Error Message Resolved | 04821012 | The error message about selecting a connection no longer appears when managing connections in the Connection Pool. |

## 
v24.1 Service Pack 5 Resolved Issues (7/31/2024)

| Title | Case # | Change Description |
| --- | --- | --- |
| ToC links did not work properly in MS Edge browser when the Report was in the PDF format | 04739200 | When the Report is in the PDF format and you view it using MS Edge browser, links in the ToC work properly and lead to correct destinations. |
| Logi Report installers could not be launched by double clicking on macOS | 04812900 | Due to known issues in InstallAnywhere v2023, macOS installers of Logi Report products can only be launched manually from the Terminal instead of by clicking on them. InstallAnywhere upgrade to 2024 version fixes this issue. |
| Filter control issue: The second selection filter condition replaced the first selection filter | 04806059 | The second filter condition no longer replaces the first selection filter. The aria-label attribute has been added to the link field so that now the text is discernible. |
| Accessibility issue in Page Studio: Non-discernible link text | 04782227 | The second filter condition no longer replaces the first selection filter. The aria-label attribute has been added to the link field so that now the text is discernible. |
| Accessibility issue in Page Studio: No keyboard access for scrollable content | 04782227 | There is keyboard access now for a scrollable content. |
| Accessibility issue in Page Studio: Missing labels for form elements | 04782227 | Missing labels have been added to form elements. |
| Accessibility issue in Page Studio: Zooming and scaling disabled | 04782227 | Zooming and scaling now works properly. |
| Accessibility issue in Page Studio: Missing  attribute in  element | 04782227 | The missing lang attribute has been added to the  element. |
| Accessibility issue in Page Studio: Invisible label for form elements | 04782227 | The label for form elements has been fixed, so that now it is visible. |
| Accessibility issue in Page Studio: Select elements did not have accessible names | 04782227 | Select elements have accessible names. |
| Accessibility issue in Page Studio: Images did not have alternate text | 04782227 | The alternate text has been added to images. |
| Accessibility issue in Page Studio: Scrollable region did not have keyboard access | 04796652 | Scrollable region is now accessible to keyboard. |
| Accessibility issue in Page Studio: Documents did not have the  element | 04796652 | The  element has been added to documents. |
| Accessibility issue in Page Studio: Images did not have alternate text | 04796652 | The alternate text has been added to images. |
| Runtime engine issue | 04786781 | When using the Schedule Execution Timeout option, even though a planned task takes longer than expected, the engine does not stop. |
| Issue with the Save option | 04784277 | You can now set the Time Before Moving to Background option on one node in the cluster, and it will apply to all nodes. |
| Image display issue | None | Now it can support the width and height attributes in  tag |
| NullPointer Exception error | None | Modifying column properties in the properties panel of an imported SQL query no longer causes a null pointer exception. |
| Save catalog issue | None | We add Always Save Catalog as New Version option in Common tab of page studio/web studio profile, which is used to control adding new version or not to existing catalog under target folder when Set Catalog Copy to Target Folder is chose on save as dialog of page studio or web studio. |
| Issue of generating duplicate links by Excel | 04786205 | When exporting a report to Excel, the Excel format now does not create duplicate links for the same sheet. |
| Non-Admin Access Error | None | In Catalog Studio, the formula editor can be opened when a non-admin user tries to create a formula in it. |
| Crosstab formula issue | 04784062 | Bold property is now applied when calculating the formula expression used in crosstab. |
| Issue with edit table | 04783386 | You can now modify the display sequence of the columns in a table using the Table Wizard option when edit a table. |
| Display of incomplete node tree | 04779070 | You can now successfully publish reports to another server that includes Set-Cookie and set-cookie headers in its response. |
| Query modification error | 04782345 | You can now add a new computed column in the query filter after a parameter is added. |
| Extra space issue in Detail panel | 04639877 | Web view now supports display of table with the enable navigation property set to false in a Detail Panel. |
| Table data visibility issue | 04587337 | In the reports now, there is no missing data in the table grid, and no sections of the table are cropped off-screen between pages |

## 
v24.1 Service Pack 4 Resolved Issues (6/28/2024)

| Title | Case # | Change Description |
| --- | --- | --- |
| Preventing multiple button clicks | 04769112 | The Show Details button in reports remains disabled until the grid data finishes loading, preventing multiple clicks that could result in an error. Similarly, the Submit button remains disabled after submitting values in the parameter form control. |
| Donut chart label placement | 04771441 | The label for each slice in a donut chart now displays correctly. |
| Word-wrapping | None | The word-wrap function now works correctly when applied to server reports. |
| Vertical alignment in tables | None | The text alignment within each row is now correct in the reports. |
| Charts in XLS reports | 04766277 | When exporting a report to Excel, the X-axis values in charts now display correctly instead of showing the legend. |
| PARAMETERS column length | 04774070 | When generating a report, the application no longer encounters an error related to the maximum character length set for the PARAMETERS column in Logi Server. |
| The Escape Formula for CSV value is not saved and the server displays the default value after restart | 04769063 | The server saves the value of the Escape Formula for CSV option in Administration > Configuration > Export >Text so that the value is properly displayed after restart. |
| Bullet points misalignment | None | The bullet points align properly in the report when you use the  or  HTML tags to wrap the content in the -  tag. |
| Missing bullet points | None | The bullet point symbols display properly in the PDF file when you use the  HTML tags. |
| Text cut-off at line breaks | None | The bullet points align properly in the report when you use the  or  HTML tags to wrap the content in the -  tag. |
| Error after deleting CrossTable report | 04725232 | The application no longer shows the 80FF001 NullPointerError when the CrossTable bind data is the same as with the report body and you select the delete option from the CrossTable wizard. |
| Error when loading a report | 04766303 | You can now successfully load the report which has wrong image resource in Logi Report Server. |
| Display issue to delayed word wrapping | 04734643 | You can now set the highPrecision property to true to ensure words are wrapped correctly and avoid extra spaces in a report. |
| Error loading checklist message while trying to run a report in Logi Report Designer | 04758586 | The improved logic in the code now automatically compiles formulas even when there are no appropriate FML classes. |
| Running a shared report results in a NullPointerException error | 04757022 | You can now run a shared web report and the source web report that contains parameters without the NullPointerException. |
| Error while editing a Dynamic field | 04723275 | You can now modify the value of a dynamic field in Logi Server without running into an error. |
| Reducing Delay | 04737461 | For reports containing a chart, the loading spinner will remain displayed until the chart is fully drawn before disappearing. |
| User information leakage | 04786824 | The customer can now hide user information by enabling the INFO level for DHTML.log. |
| Security bug issue | 04782211 | When the input type changes, the password will be fixed to clear text. |
| Catalog studio issue | None | In the catalog, new queries, procedures, and UDS can now be created and edited. |
| Display issue | 04784800 | In reports, the content copied from excel is now displayed correctly. |

## 
v24.1 Service Pack 3 Resolved Issues (5/31/2024)

| Title | Case # | Change Description |
| --- | --- | --- |
| Create Stored Procedures in Catalog Studio | 04703508 | You can now create stored procedures in Catalog Studio without getting an IllegalArgumentException error message. |
| Display of Text in HTML Tags | 04739011 | When the content of a field contains HTML tag elements and you enable the Convert HTML Tag property of the field, Report now properly: Displays the text in a heading tag that is in between a -  tag. Adds left padding to -  items in a  list. Applies font size to text in heading tags. |
| Drag Fields from Resource View | 04707428 | You can now drag and drop fields from the Resource View panel to your report as expected in Page Report Studio in Firefox. |
| Edit Parameter | 04747455 | You can now select the OK button in the Edit Parameter dialog box to apply parameter changes, when you set the log level to "trace" for Designer. |
| Edit Precision Property of Columns in JSON Connection | 04689403 | After you change the Mapped SQL Type property of a schema in a JSON connection, you can now refresh the table transformed from the schema to edit the Precision property of columns in the table. |
| Enhanced Error Message | 04711099 | Report Studio now includes the deeper causes when displaying a report validation check on data container error message. |
| Export Report with Non-Existent Images to PDF | 04739011 | You can now successfully export your report to PDF without Designer displaying an error message, when the report references images that Designer cannot load from the corresponding catalog folder. |
| Hide Scrollbar When No Need | 04670089 | Web Report Studio no longer displays a scrollbar in a report when the data can be completely displayed vertically. |
| Panel Height in Banded Report | 04676564 | Report now properly displays your banded report when you set the height of the banded detail panel larger than that of the report page panel. |
| Parse of Special HTML Characters | 04734643 | When you upgrade from v23.4, Report now properly parses the special HTML characters in the content of your field, when you set the Convert HTML Tag property of the field to "true". |
| Performance Enhancements in Publishing Resources to Server | 04692042 | Server now enhances the report loading performance and looks for font files only once, when you call addResourcesToFolder() to publish catalogs and reports to Server during Server startup. |
| Run Reports with TOC Multiple Times | 04697005 | Server now works as expected without memory leak when you run reports with TOC multiple times. |
| Scroll to Next Parameter Values Page | 04532325 | You can now scroll down to the next page of parameter values in the Enter Parameter Values dialog box when you create web reports on Server. |
| Specify Linked Catalog for Organization Reports | 04712651 | You can now specify a linked catalog for the Organization Reports folder, even if there is a catalog in the folder. |
| Set Permissions When Publishing | 04699551 | Server now remembers the permissions you set when publishing from local directory. |
| TTF Display After JDK Upgrade | 04679442 | After upgrading JDK to v17, when you find the TTF you apply in a report slightly shifts upwards in the report output, you can now add the -Dlogireport.applyLeading4Ascent option in Report's startup file to improve the display, for example, -Dlogireport.applyLeading4Ascent="*Calibri-Bold;*Calibri". |
| View Report Outputs Generated by Archive | 04713354 | You can now view your report outputs from the Result Versions page if you generate the outputs by using the Advanced Run > Archive tab or the "archive" element in the on-demand API POST/myTasks/OnDemand. |

## 
v24.1 Service Pack 2 Resolved Issues (4/30/2024)

| Title | Case # | Change Description |
| --- | --- | --- |
| Apply Schemas to Tables | 04692092 | Catalog Studio now applies schemas to tables, views, and stored procedures as you define. |
| Available Schemas in Catalog Studio | 04692092 | In Catalog Studio > Edit JDBC Connection Resource Editor, the available Schemas now only show the included schemas you set in the Edit JDBC Connection Info Editor. |
| Conditional Link on Crosstab Aggregation Field | 04693689 | Designer now correctly saves the conditional link that you create on a crosstab aggregation field. |
| Conditional Link on Null Values | 04693689 | Web Report Studio no longer blocks the UI or displays exceptions when you select Null values with a conditional link. |
| Data of Banded Object in Report Outputs After Upgrade | 04485806 | After upgrading from v15.6 to v24.1 SP2, Report now completely displays data of all fields in the detail panel of your banded object in the report outputs, when you have added many fields in the detail panel and a new page is generated for laying out the panel. |
| Display All Tables in Web Report Studio | 04659591 | Web Report Studio now displays all the tables in the detail panel of the banded object. |
| Display Complete Customize Profile Page | 04672666 | Server now displays the complete content of the My Profile > Customize Profile page, when you select Enable Customize Properties, even if some properties in the profile are missing in the properties file. |
| Display Date/DateTime Parameter Values | 04676741 | Server now displays date/datetime type parameter values with the user defined format of the correct locale in the Enter Parameter Values dialog box after you select the values from the calendar, when the locales of the Server machine and browser are not the same. |
| Display Sequence Numbers in Tables | 04652527 | Web Report Studio now displays the sequence numbers starting from 1 as expected in tables. |
| Display X button on Background Tasks Page | 04640282 | Server now displays the X button in the proper position when you hover over a row on the Background Tasks page, and you can click the button as expected. |
| Enhance Object Loading Performance | 04503023 | Server does not summarize the memory size of objects when loading them in the cached mode to improve performance, if no maximum memory capacity is specified. |
| Enhance Subreport Loading Performance | 04503023 | Server now enhances the performance of loading subreports. |
| Enhanced Export Performance | 04503023 | You can now get better performance when exporting reports in Report, when you enable the Convert HTML Tag property for labels/fields in the reports and the content of the labels/fields does not contain HTML tags. |
| Go to Respective Page from Start Page | None | Server now displays the respective page as expected, when you select My Folder, Public Folder, My Profile, or Schedule on the Server Start Page embedded in a cross-domain iframe. |
| Idle for Long when Setting Permissions | 04674274 | You can now save your permission setting normally when you select OK even after you update permissions and let the permission page idle for a long time. |
| Line Chart Display | 04658349 | Web Report Studio and Designer View now display lines properly in a line chart that uses a continuous axis, when there are multiple charts with large amounts of data in your report. You now have the ability to close the chart animation. |
| Run Reports to Excel with tryview.jsp | 04659786 | Server now applies the default Report Format as you defined in Designer, when you run reports to Excel via URL with tryview.jsp. |
| Start Server with FedRAMP | 04658586 | Report Server can now start normally after you update your system to meet the requirements of FedRAMP, by not calling the RNG algorithm "SHA1PRNG" during AES encryption/decryption. |
| Superscript in PDF Output | 04661687 | Report now correctly displays the text that applies Superscript formatting in your PDF output. |
| Synchronize Excel Properties on Server | 04659786 | Server now synchronizes the Excel properties on the Tool > Preferences > Export Formats tab with the My Profile > Customize Server Preferences > Export Formats tab. |
| Vertical Scroll on Mobile | 04639865 | Web Report Studio now displays your report data fully when you scroll vertically on a mobile. |

## 
v24.1 Service Pack 1 Resolved Issues (3/29/2024)

| Title | Case # | Change Description |
| --- | --- | --- |
| Change Cascading Parameter Values | 04630233 | Server no longer resets the higher-level parameter values when you change cascading parameter values. |
| Display of HTML Tag Content After Upgrade | 04634462 | After upgrading from v23.4 to v24.1 SP1, Report now correctly displays the content of objects that have the Convert HTML Tag property set to "true" in the detail panel of a banded object, when there are page breaks in the detail panel. |
| Display Repeated Content Once for Multiple Rows | 04568655 | Web Report Studio now only displays repeated content once in a table cell for multiple data rows, when the table cell's Joining Merge property is set to "true". |
| Display Web Reports on Mobile Devices | 04639865 | Web Report Studio now displays the report body and horizontal/vertical scrollbars as expected on mobile devices. |
| Open Banded Report | 04628518 | Designer now opens your report properly rather than displaying an error message, when you open a banded report where you have mistakenly pasted a group header panel (GH) into another GH in the banded object. |
| Paste Image into TOC | 04635125 | Designer now displays a warning message when you paste an image into the TOC page header panel, where images are not allowed. |
| Synchronize Schedule Time on Clustered Servers | 04572248 | After you schedule to run a report periodically, delete the report, and then restart your cluster, Server now displays the same next run time of the schedule on the two nodes. |

## 
v24.1 Feature Enhancements (2/29/2024)

| Title | Description |
| --- | --- |
| Catalog Studio Enhancements | More useful functionalities have been added to Catalog Studio. You can now add user defined data sources, define data security based on data source table records, and save non-XML format catalogs in Catalog Studio. Server adds a new permission "Catalog Access Control" for granting end users access to the Catalog Studio Access Control Editor. Organization admin can now access the editor within the scope of Organization Reports and Organization Components. You can batch setting permissions in the editor. Edit Children and Delete Children permissions are added to parent nodes in Object Security. Server enhances the download and publish algorithms for Data Security for administrators and end users. Server incorporates a catalog session locking mechanism to prevent resource conflicts. User Session Timeout now also takes effect in Catalog Studio. |
| Convert HTML Tags in Crosstab | You can now set the Convert HTML Tag property for fields and labels in a query-based crosstab. |
| Customizable PDF Attachment Annotation | You can now customize annotations of the attachments in your PDF/A compliant document. You can display the annotations in image that draws from file path, URL, DBField, or formula, or in text. These customizable options enable you to enhance the visual representation of attached files and text within your PDF/A compliant document. See Adding PDF Attachment to a Report. |
| Dynamic Table Column Width | You can now specify the width of a table column using the Width property in the Report Inspector and apply a constant level formula as the property value to dynamically change the width. |
| Enhanced HTML Tag Conversion in Table | Report can now convert HTML tags in the content of fields/labels that are in static or relative position in a table, in addition to absolute fields/labels in the table. |
| More HTML Tags Support | Report now supports most common HTML tags when rendering reports in Page Report Studio, Designer view mode, and PDF/Excel/HTML/RTF outputs. They include , , , nested  and , and SVG and Base64 format images. |
| Set Default Parameter Values via Web API | You can now set default parameter values for reports using the Web API. |
| Support Multiple Selection in Page Report Template Editor | You can now: Access Template Editor without the need to enable it. Select multiple fields in the resource panel and multiple report objects in the template area and in Inspector. Drag multiple fields into tables, banded objects, crosstabs, report body, and report header/footer panels. Batch align, move, and resize multiple report objects. Specify the report-level background image. |
| Unique Schedule Names | Server now supports unique schedule names at the system level to avoid schedule duplication on a Report Server. Administrators can enable this feature by selecting the Unique Schedule Names option in the Server Console > Administration > Configuration > Advanced tab or setting the server.enable.unique_schedule_names property to "true" in the server.properties file. |

## 
v24.1 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| Automatic Cache JSON/XML Stream | 04503023 | You can now enable the "Automatic Cache JSON/XML stream" option without getting a DSException error message, when your data source is XML. |
| Banded Object Display | 03626137 | Report now generates a new page to display the content in a page header panel of a banded object, when the content cannot be completely show up in one page and there is no other visible panels next to this page header panel. |
| Change Table Columns Order | 04567787 | You can now adjust the order of the first and second columns in a table in Web Report Studio without getting a RuntimeException error message. |
| Chinese Font in CSV Output | 04489359 | Server now displays Chinese font as expected when you export your reports to the Delimited Format (including CSV) of the Text format through scheduled tasks. |
| Display Error Message | 04511390 | Designer now properly displays an error message when something goes wrong in the Report Engine. |
| Display Percentage Values in Pie/Donut | 04622831 | Web Report Studio no longer displays the percentage values twice in Pie/Donut charts, when you resize the window frequently on a mobile device. |
| Export Dashboards to PDF | 04513399 | JDashboard now displays your dashboard within the PDF page as expected when you export it to PDF in an integrated environment. |
| Filter with Data Container Link | 04568655 | Web Report Studio now filters report data as expected when you set up the data container link between a table and its parent banded object. |
| Font Resource Usage Optimization | 03463417 | Server now optimizes font resource usage by reducing competition stress. |
| Hide Components in Banded Objects | 04509753 | Web Report Studio now hides components in banded objects as expected when there is no data, if you use formulas to control the components' visibility. |
| Keep Long-Time Running Reports Alive | None | Server now sends multiple short requests to replace a long request to prevent the browser from killing long-time running reports in Page Report Studio, when there is a proxy server between Report Server and the browser. |
| Link Report | 03635020 | Designer now allows you to link your report to another report that does not contain any dataset. |
| Load Parameter Value List | 04496410 | Report no longer clones irrelevant parameters when loading a parameter value list. |
| Open Web Reports with Mobile Emulator | None | Server no longer displays JavaScript errors when you open web reports using a mobile emulator. |
| Post "/report/parameterInfos" | 04530861 | You can now call REST API with post "/report/parameterInfos" without getting exceptions, when the database is not specified. |
| Publish Reports via REST API | 04515910 | You can now publish reports between two Servers on different computers using the REST API. |
| Run Page Reports in Chrome | 04503535 | You can now run a page report with a crosstab as expected in the Chrome browser. |
| Run Reports with runReport.jsp | 04525622 | You can now run reports by calling runReport.jsp without getting an HTTP 401 error message, even if the request cannot pass CSRF check. |
| Schedule Web Reports | 04512303 | Server no longer displays a NullPointerException error message when you schedule to run a web report after you set multiple values (one value contains a comma) for a multivalued parameter in the default bookmark of the web report. |
| Set Partial Parameters in Session Variable | 04530861 | If you set partial parameters of a report in the session variable, they now take effect when you submit a schedule via the Web API and include the rest parameters in "reportParameters". |
| Visit API Routes | 04525747 | Server no longer displays many NullPointerException error messages when you visit API routes. |

## 
Known Issues

Report data cut off in PDF due to PDF page size limitation

When you export a report to PDF, some data of the report are cut off in the PDF output when the report contains a large amount of data, and you have applied continuous page mode to the report or set the page size to be larger than 200 inches. This is due to a PDF limitation where the data displayed can be no larger than 200 inches in a single PDF page.

Unsupported go-to action when using dynamic formulas on chart

You get exceptions when you perform the go-to action on a chart that uses a dynamic formula on the value axis and the formula contains group information.

Previous Topic  Next Topic
