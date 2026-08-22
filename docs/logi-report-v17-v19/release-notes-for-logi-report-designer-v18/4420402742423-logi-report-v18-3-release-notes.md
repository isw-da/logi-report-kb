---
title: "Logi Report v18.3 Release Notes"
id: 4420402742423
section: "Release Notes for Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4420402742423-Logi-Report-v18-3-Release-Notes
updated_at: 2022-04-29T03:11:50Z
---

# Logi Report v18.3 Release Notes

[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4420402743319-Logi-Report-v18-3-Enhancements)

# Logi Reportv18.3 Release Notes

This topic describes feature enhancements, resolved issues, and known issues of Logi Report v18.3. Subsequent updates are listed chronologically, most recent first.

For more product information, including new purchases and upgrades, contact [US Sales](mailto:salesteam@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me. "US Sales email address.") or [UK Sales](mailto:emea_sales@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product.%20Please%20contact%20me. "Email address for UK sales team.").

* [v18.3 Service Pack 3 Resolved Issues](#h_01FZER79QBB7YQT3MC811AP56T)
* [v18.3 Service Pack 2 Resolved Issues](#h_01FZER79QBB7YQT3MC811AP56T)
* [v18.3 Service Pack 1 Resolved Issues](#h_01FWZ6DTK6VQNJQMB6HSS68G3F)
* [v18.3 Feature Enhancements](#Feature)
* [v18.3 Resolved Issues](#Resolved)
* [Known Issues](#Known)

### Log4j and Log4Net Vulnerabilities Update

In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: [Statement on Log4j and Log4Net Vulnerabilities](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751).

## v18.3 Service Pack 3 Resolved Issues (4/29/2022)

| Title | Case # | Change Description |
| --- | --- | --- |
| Distinct On Field for DistinctSum Summary in XML Catalog | 01972302 | Designer now saves the Distinct On field you specify for a summary that applies the DistinctSum aggregate function, when you save the catalog in XML. |
| Go to Detail on Charts | 01991475 | Web Report Studio now applies values from filter controls to display data the way you want, when you select Go to Detail on a chart. |

## v18.3 Service Pack 2 Resolved Issues (3/30/2022)

| Title | Case # | Change Description |
| --- | --- | --- |
| Formula Using "select-case" Statement | 88043 | Logi Report now returns correct values when formulas reference a DBField in a "select-case" statement. |
| Summary Value in Excel Output | 88183 | When the value of a summary field shows at the bottom of a report page and you export the report to Excel using Report Format, the value now displays in the correct position in the Excel output if the cell containing it is converted to a formula cell by Excel. |
| View To E-mail Settings in Scheduled Tasks | 88110 | You can now view To E-mail settings in scheduled tasks, when your user name contains special characters. |

## v18.3 Service Pack 1 Resolved Issues (2/28/2022)

| Title | Case # | Change Description |
| --- | --- | --- |
| Cascading Parameters in Linked Report | 87772 | Page Report Studio can now pass the correct values to the lower-level cascading parameters in the linked report, when you change the higher-level cascading parameter values in the master report. |
| Convert Reports Using rptconv.bat | 87320 | Logi Report no longer displays a command line error stating "unknown error" when you use the batch tool rptconv.bat to convert reports created by an earlier release to the current. |
| Create Banded Report in Designer | 87271 | Designer now generates the banded report correctly instead of becoming nonresponsive, when you specify a report title in the Select Component for Page Report dialog box and select Create a Banded Report in the Style screen of the Banded Wizard dialog box. |
| Export Reports | 87657 | After upgrading from v16 Update 2 to v18.3, when your reports contain images and JRotator objects and you use formulas to control the image's Image Name property and JRotator's Display Image property, you can now export the reports successfully. |
| Formula Controlled Images | 87611 | After upgrading from v16 Update 2 to v18.3, Logi Report properly displays the images and JRotator objects when you use formulas to control the image's Image Name property and JRotator's Display Image property. |
| Percentage Values | 87647 | Logi Report now displays percentage values correctly when you set the Display Rounding Mode property of a catalog data source to "Half Up" or "Half Down" and upgrade from v16 Update 2 to v18.3. |
| Repeat of Split Tabular Cell | 86994 | If you set the "Repeat Content" property of a tabular cell in a report to "true", and the cell is split and expands to the next page, Server no longer repeats the split tabular cell to avoid errors whenever running the scheduled report. |
| Repeated Banded Group Header | 87646 | When a banded object contains parallel group headers under the same group panel and you set the Keep Group Together property of the group panel to "true", the first group header repeats properly when you set its Repeat property to "true" and other group header's Suppress to "true". |
| Time Zone in Parameter Values | 87383 | Page Report Studio now displays date type parameter values in the correct time zone when you change the parameter values, when the parameter is a high-level cascading parameter. |

## v18.3 Feature Enhancements (1/28/2022)

| Title | Description |
| --- | --- |
| Cached Report Bursting on TOC Entries | When users run a report containing a Table of Contents, Logi Report displays TOC entries for the groups they are authorized to view, according to the cached report bursting security policy the report applies. |
| [Customizable Subreport Index in Excel Output](https://devnet.logianalytics.com/hc/en-us/articles/4420402743319-Logi-Report-v18-3-Enhancements#SubreportIndexFormat) | You can now customize the text format of the subreport links in Excel output when you export the subreport in separate sheet, to make these links more easily recognizable inside the primary report. See [Subreport Properties](https://devnet.logianalytics.com/hc/en-us/articles/4405661891479-Subreport-Properties). |
| [Dynamic Page Panel Visibility](https://devnet.logianalytics.com/hc/en-us/articles/4420402743319-Logi-Report-v18-3-Enhancements#PagePanelVisibility) | Designer now provides the Invisible property for page panels in query-based page reports, and you can use formulas to dynamically display or hide the content inside page panels according to different user scenarios with continued page numbers in the reports. |
| Dynamic Sheet Name in Excel Output | You can now use a formula to control the Sheet Name property of a report, to dynamically specify the sheet name in the report’s Excel output. |
| Enhanced Resource Publish via REST API | You can now use REST API to publish resources from the Server computer to Server and from one Server to another, besides from the local drive to Server, as you do on the Server Console. |
| Formula Control for TOC Properties in Web Reports | You can now use formulas to control the TOC Anchor and Anchor Display Name properties of objects in web reports, to dynamically define entries in the Table of Contents of the reports. |
| Log4j Upgrade | Logi Report replaces older Log4j implementations with Log4j v2.17.1 to mitigate the security vulnerabilities. |
| More Secure Single-Way Algorithm SHA-384 | Server administrators can now use a more secure single-way algorithm (SHA-384) to encrypt passwords for users in specific realms. |
| [New Formula Functions for Space Calculation](https://devnet.logianalytics.com/hc/en-us/articles/4420402743319-Logi-Report-v18-3-Enhancements#SpaceFunctions) | You can now use four new formula functions: *currentUsedHeight()*, *currentUsedWidth()*, *totalAvailableHeight()*, and *totalAvailableWidth()*, for calculating report space dynamically at runtime. See [Appendix 1: Formula Functions](https://devnet.logianalytics.com/hc/en-us/articles/4405664357143-Appendix-1-Formula-Functions#currentUsedHeight). |
| [New Special Field for Displaying TOC Page Numbers](https://devnet.logianalytics.com/hc/en-us/articles/4420402743319-Logi-Report-v18-3-Enhancements#TOC) | You can now use the special field TOC Page Number in the page header/footer of a TOC page, to display page numbers for the Table of Contents differently than your report pages. |
| Parameter Reference in Dynamic Formulas | Logi Report enhances dynamic formulas by enabling report designers to create local parameters directly via the Formula Editor dialog box to reference in the formulas in Designer, and enabling end users to reference local and global parameters in the formulas in both Web Report Studio and Page Report Studio. |
| Support for Oracle JDK 17 and OpenJDK 17 | Logi Report now supports Oracle JDK 17 and OpenJDK 17, in addition to Oracle JDK 8, 9, 11, and 12, and OpenJDK 8, 11, 12, 13, 14, 15, and 16. |
| [Table of Contents in Report](https://devnet.logianalytics.com/hc/en-us/articles/4420402743319-Logi-Report-v18-3-Enhancements#TOC) | You can now add a Table of Contents in a page report or web report and customize format of the TOC entries, to enable easy navigation of the report contents when previewing the report in Designer and in the report outputs. See:  * [Adding Table of Contents in a Report](https://devnet.logianalytics.com/hc/en-us/articles/4405661931671-Editing-Reports#TOC) * [TOC Container Properties](https://devnet.logianalytics.com/hc/en-us/articles/4420402744215-TOC-Container-Properties) |
| Third-Party Package Upgrade | Logi Report upgrades the support for some third-party packages to newer versions. |
| Tool for Converting Strings in CQR Files | You can now use the batch tool cqrtrans.bat/cqrtrans.sh to convert String values in your cached query result (CQR) files to specified characters, to secure your data when you need to send the files to others. See [Using the Designer Launch Files](https://devnet.logianalytics.com/hc/en-us/articles/4405661770647-Using-the-Designer-Launch-Files#cqrtrans.bat). |

## v18.3 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| All Values for Parameter | 85687 | You can now select "All Values" in the Enter Values dialog, when running a page report with parameters on FireFox 91.0 (64 bit). |
| Auto Fit of Crosstab Fields in XML Page Reports | 85954 | Designer now correctly saves the Auto Fit property setting for fields in page report crosstabs, when you save the reports in XML. |
| Banded Footer Position | 86021 | The footer of a banded object now displays at the bottom of the report page, when you set its To Bottom property to "true" and the Height Auto Fit property of the corresponding page panel is "false". |
| Blank String as Parameter Value | 85975 | Page Report Studio now displays correct report data when the last value of a multi-valued parameter is blank string. |
| Chart Legend Color Pattern | 86675 | Web Report Studio now displays the correct chart legend color pattern in a bar-line combo chart. |
| Correctly Quoted Names for Queries | 85882 | Designer now correctly quotes field names and their qualified names in the FROM clause of a query's SQL statement, when the query applies outer joins. |
| Crosstab Column/Row Header Background Color | 86281 | Logi Report now applies the correct background color to the column/row header in a crosstab, when you use a crosstab formula that returns values based on the higher group of the current column/row group to specify the color. |
| Designer Dialog Box Display | 87028 | Designer now displays the Connect to Logi Report Server and Publish to Logi Report Server dialog boxes correctly, when you increase the font size of your system. |
| Designer UI Resolution on macOS | 87164 | Designer now scales the UI correctly for macOS users, per the ratio you specify in the Options dialog box. |
| Filtering Components in Page Header/Footer | 86163 | You can now apply the web action Filter to components in the page header and page footer. |
| Group Field Time Zone | 87080 | Web Report Studio now displays group fields with the proper time zone in banded objects. |
| Groups in Nested Formulas | 79885 | Logi Report now parses groups in a formula correctly, when the formula is at the end of a formula reference chain that contains more than two levels. |
| Mail From Address Update via URL | 80727 | If you have cleared the "Server Requires Authentication" checkbox when you configure your email server, you can now use jrs.mailfrom in the URL to change the Mail From address while sending PDF reports as email attachments. |
| NLS Number Format | 86667 | Web Report Studio can now apply the German (Switzerland) number format you define in NLS to bench chart data labels. |
| No IndexedDB Error | 86625 | Logi Report no longer displays the IndexedDB error message when you run reports via URL in a cross-domain iframe on a Chrome Incognito window. |
| Number Zero in Charts in Excel Output | 86990 | The number zero in charts now display correctly in the Excel output, when you set the Auto Scale in Number option to "true" in the corresponding format dialog box. |
| Number Zero in Charts in Excel Output | 86990 | The number zero now no longer displays in charts in the Excel output, when you select Suppress Label When 0 in the corresponding format dialog box. |
| Page Control in Page Layout | 86093 | Page Report Studio now displays page controls when the current report tab uses Page Layout. |
| PDF Output with Blank Parameter Value | 80562 | After upgrading from V16.1 update 1, Server now displays proper data in the PDF output when you use runReport.jsp to run a report with a blank parameter value, and if the parameter's Treat Blank as Null property is "true". |
| Preview Server in Designer | 85915 | Logi Report edits the default value of the property httpserver.ssl.enable to "false" for the Preview Server in Designer, to avoid it unnecessarily retrieving the keystore information when you preview reports in Page Report Result in Designer. |
| Quick Schedule with CSV Format | 86547 | Server now saves outputs with the file suffix .csv, when you quick schedule reports to Text, after you enable "CSV Format" for Text in the Server Profile > Customize Server Preference > Export Formats page. |
| Resource Servlet Context Path in Tomcat | 85781 | Logi Report Server now outputs the correct resource servlet context path when you access the Filter dialog in Page Report Studio, when integrated with Tomcat. |
| Running of Parameter-Based Reports | 85915 | Server now runs parameter-based reports correctly, when the parameter's Bind Column and Display Column are different data types. |
| Scheduled Tasks in a Cluster | 79035 | Logi Report no longer misses scheduled tasks in a cluster that uses SQL Server 2017 while concurrently running scheduled tasks. |
| Sort Icon for Summary Column in Summary Table | 86352 | Web Report Studio now displays sort icons (shaped like triangles), for summary/common column labels in summary tables, when you add summaries in the table header/footer panels. |
| Table Column Headers in Web Reports | 86352 | Designer adds the display name of an aggregation object as the column header, when you drag the aggregation to an empty common column in a web report table. |
| Table Filtering | 86446 | You can now filter tables in Web Report Studio without getting a NullPointerException error message, when the tables inherit data from parents. |
| Table Formatting with Page Break | 85582 | Tables in Page Report Studio now retain their formatting when you insert a page break after them. |
| Updated JavaScript Array Prototype Properties | 85902 | Logi Report now updates extended properties in the JavaScript Array prototype and makes them non-iterable. |
| User Removal via Web API | 85846 | Server now removes associated user sessions after you remove users via the Web API. |
| View Element Position | 86152 | Designer now retains the position of a view element in the resource tree of a business view, when you change the element type between Detail and Group and save the business view. |

## Known Issues

**Report data cut off in PDF due to PDF page size limitation**

When you export a report to PDF, you will find that in the PDF output, some data of the report are cut off if the report contains a large amount of data but its page mode was specified to be continuous page mode or its page size was set to be larger than 200 inches. This is due to a PDF limitation where the data displayed can be no larger than 200 inches in a single PDF page.

**Unsupported go-to action when using dynamic formulas on chart**

You will get exceptions when you perform the go-to action on a chart which uses a dynamic formula as its shown value and the formula contains group information. This is a limitation in the current version. It will be resolved in a future release.

[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4420402743319-Logi-Report-v18-3-Enhancements)
