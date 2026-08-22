---
title: "Logi Report v17.1 Release Notes"
id: 1500009776761
section: "Release Notes for Logi Report Server v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009776761-Logi-Report-v17-1-Release-Notes
updated_at: 2021-12-07T03:35:54Z
---

# Logi Report v17.1 Release Notes

[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009748362-Logi-Report-v17-1-Enhancements)

# Logi Report v17.1 Release Notes

This topic describes feature enhancements, resolved issues, and known issues of the Logi Report v17.1 releases.

![](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg) Logi Analytics has made a change in the way we name releases. Logi Report 17.1 Service Pack 2 (17.1 SP2) is the next immediate release after Logi Report 17.1 Update 1. We will no longer use the word "Update" for Logi Report, and will name subsequent releases of this type using the phrase "Service Pack."

## v17.1 Service Pack 3 Resolved Issue

| Title | Case # | Change Description |
| --- | --- | --- |
| Fast Rendering of Page Reports | 79036 | After you upgrade from v16.1, the page report containing a table now quickly displays a blank table (as expected) when no data returns to the table, if the Suppress When No Records property of the table detail row is "true". |

## v17.1 Service Pack 2 Resolved Issue

| Title | Case # | Change Description |
| --- | --- | --- |
| Timestamp Parameter Values with 12 Hour Format | 78964 | Logi Report no longer changes a PM value to AM after you submit Timestamp parameter values using the 12-hour format in the web report Enter Parameter Values window. |

## v17.1 Update 1 Feature Enhancement

| Title | Description |
| --- | --- |
| Third-Party Package Upgrade | Logi Report upgrades the support for some third-party packages to newer versions. |

## v17.1 Update 1 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| Access Folder | 75345 | After you remove a web report that has a shared copy in a public folder, you can now access the folder on Logi Report Server, and publish resources to the Public Reports folder from Logi Report Designer. |
| HTML Font Size | 74643 | The values of a field now display in the font size you specify, if you set the Convert HTML Tag property of the field to "true" and do not define the font size in the HTML tag. |
| JDashboard - Chart | 75460 | JDashboard now displays the Date type category labels in bar charts in the proper order when you enable the Reverse Category feature. |
| JDashboard - Chart | 75373 | JDashboard now displays pie charts created in v16.1 Update 1 correctly, when a pie slice takes up more than 60% of the pie, and you set the Explode Amount property to "2". |
| Page-Level Formula | 74812 | Logi Report now returns the correct value to the X property of an object, when you use a page-level formula to control the property. |
| Page Report Result | 75391 | You can now run page report results that use .rsd as the file suffix, via URL by using the two properties jrs.resource\_path and jrs.file. |
| Parameter | 74543 | Designer now retrieves values for a parameter automatically, based on the value you specify for another parameter, if the two parameters are related. |
| Parameter | 75040 | You now see the correct parameter value in a page report in Logi Report Designer and Page Report Studio, when you select the value after searching or sorting the value list in descending order, in the Enter Parameter Values dialog box. |
| Report | 74501 | You can now successfully run a report on Logi Report Server and reenter the table wizard in Logi Report Designer, even if an expression used for controlling a property has syntax errors. |
| Report | 75263 | You can now run reports successfully in Page Report Studio when you use an unknown field in the isnull() method in a formula. |
| Report - Page Number | 74650 | After you insert a banded object into another banded object's group header, and set a data container link between the two banded objects, you can now reset the Page Number field for each group. |
| Report - Save To | 74718 | You can now save a report created using an Imported SQL query to a directory without Designer displaying the Merge dialog box, if the catalog in the directory matches the catalog in the report. |
| Report Studio | 74913 | You can now see report content at top left in the View Mode of Web Report Studio and in the Basic View of Page Report Studio. |
| Time Zone | 75480 | Logi Report Server now uses the VM time zone in a PDF report, when you run the report via URL containing date-type parameters. |
| User-Defined Formula Function | 74602 | Logi Report now parses user-defined formula functions in the correct order, according to the level set in the functions. |
| Web Report Studio - Chart | 74788 | Web Report Studio now shows nodes for all lines in a chart when you set Show Node to "true". |
| Web Report Studio - Chart | 74879 | You now see complete labels in the chart legend in Web Report Studio when you set Placement to "customized" while using True Type Font with Chrome Version 86. |
| Web Report Studio - Report | 74794 | You can now run a web report successfully in Web Report Studio when a chart in a banded object inherits data from the banded object, and the chart uses a dynamic formula as the category or series field. |

## v17.1 Update 1 Feature Enhancements

| Title | Description |
| --- | --- |
| Data Source Connection - Oracle | You can connect a catalog data source to an Oracle database via Wallet after making the necessary configurations. For more information, see Connecting to Oracle Databases via Wallets. |
| Design API - Filter | You can now use the Design API to manipulate the filters that apply to the datasets and data components in a report. For more information, see Setting, Getting, and Clearing Filters in a Report. |
| Designer - Batch Update Page Properties | You can now update the page properties for all the reports in a specified catalog at a time by running PageSetup.bat/PageSetup.sh that Designer provides in the `<install_root>\bin` directory. For more information, see Updating the Page Properties of Multiple Reports. |
| Line Chart - Fill Area | You can now choose whether or not to fill the areas that are formed by the chart axes and the lines. For more information, see Formatting the Lines in a Line Chart. |
| Link to URL | You can now display multiple runtime values of a dynamic field, instead of only one value, in the URL to which you link an object in a chart, table, banded object, or crosstab. For more information, select the following links:   * [Adding Links in Web Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009778801-Adding-Links-in-Web-Report) * [Select Field Dialog Box Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009776241-Select-Field-Dialog-Box-Properties) |
| Report - Bind Data | You can now bind a data resource to the report body of page report tabs. For more information, see Binding Data to the Report Body. |
| Report - Ignore HTML Tag | You can now set the Ignore HTML Tag property in the Inspector panel in Web Report Studio and for business view-based reports in the Report Inspector in Designer. |
| Server - Active X | Logi Report Server JavaScript now does not use ActiveXObject because Microsoft no longer supports Active X. |
| Server - Cross-Domain Access | You can now successfully access Logi Report Server that is embedded in another domain when you are using the recent Chrome version, without further configuration. |
| Server - Derby Database | You can now make Derby run in Embedded mode as the default server system database, by setting the server.derby.embedded.enableproperty to"true". For more information, see [Appendix 2: Configuring Logi Report Server Using Properties in server.properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009771281-Appendix-2-Configuring-Logi-Report-Server-Using-Properties-in-server-properties). |
| Server - Derby Database | You can now hide the information that the Derby database is provided for testing and evaluation purposes only and should not be used in a production system, from the Logi Report Server command console or the log, by setting the server.derbytip.show property to "false". For more information, see [Appendix 2: Configuring Logi Report Server Using Properties in server.properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009771281-Appendix-2-Configuring-Logi-Report-Server-Using-Properties-in-server-properties). |
| Server - Email Server | You can now use Microsoft Office 365 via the STARTTLS protocol to send report results in emails, by selecting Server Requires a Secure Connection (STARTTLS) when configuring the email server. |
| Server - Export to XML | You can now add a white list of URLs in the startup file of Logi Report Server by using a Java system property -Dlogireport.ssrf.whitelist, so that Server proceeds the schema file URL for exporting a report to XML, only when it matches one of the URL patterns in the white list. For more information, see [Advanced Run Dialog Box Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009773921-Advanced-Run-Dialog-Box-Properties). |
| Server - Silent Install | You can now set up DB\_TYPE=Production to connect to another DB instead of Derby for Profiling DB as well as System DB and Realm DB, when you install Logi Report Server silently using the file ServerInstall\_custom.properties. |
| Server - UDS | You can now pass customized variables to a user data source (UDS) at runtime. For more information, see [Passing Customized Variables to User Data Source at Runtime](https://devnet.logianalytics.com/hc/en-us/articles/1500009743162-Passing-Customized-Variables-to-User-Data-Source-at-Runtime). |
| Third-Party Package Upgrade | Logi Report upgrades the support for jQuery from v3.4.1 to v3.5.1 which resolves some security issues. |
| User Defined Formula Function | Logi Report no longer displays a syntax error when you use the Formula Editor to import a user defined function via the "import" statement multiple times. |
| Web Report Studio and Page Report Studio | You can now see the report content at the center of the report body instead of the top left position in the view mode of Web Report Studio and Page Report Studio. For more information, select the following links:   * [Customizing Web Report Studio Profile](https://devnet.logianalytics.com/hc/en-us/articles/1500009750242-Customizing-Web-Report-Studio-Profile) * [Customizing Page Report Studio Profile](https://devnet.logianalytics.com/hc/en-us/articles/1500009777681-Customizing-Page-Report-Studio-Profile) |

## v17.1 Update 1 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| Crosstab - Word Wrap | 74195 | Logi Report Designer and Page Report Studio now word wrap row header title text in page report crosstabs successfully. |
| Designer Performance | 73324 | You can now run Logi Report Designer more smoothly with greatly improved performance. |
| NLS - Export | 74286 | Logi Report Server now exports page reports successfully when you use French as the server language and when you define button names in the Export dialog box in single quotes. |
| Page Report Studio - Report | 73516 | You can now switch among the report tabs in a page report or export them simultaneously in Page Report Studio successfully, when more than one data component in the report tabs pushes down group-level aggregation calculation to the data source at the same time, while there are record level pass one formulas to be calculated for the data components. |
| Page Report Studio - Report Session Timeout | 73443 | You can now see the proper message when you export a report in Page Report Studio after the report session expired, without 404 error. |
| Page Report Studio - Sort | 73769 | Page Report Studio now displays the updated display name of a group field in the Sort dialog after you change the display name in the business view. |
| Page Report Studio - Switch Mode | 73528 | Page Report Studio now correctly changes the mode name between Interactive View and Basic View, when you switch between them after you turn off Toolbox in the Page Report Studio Profile. |
| Report - Group Footer Background Color | 73726 | The group footer panel in the last page of a report can now apply the background color that you specify while designing the report, no matter the page contains the detail panel or not. |
| Server Web API - PUT | 72579 | You can now use PUT in Web API to update the weekly time condition that you scheduled to Sunday. |
| Table - Export to PDF | 72082 | The right border of a table cell now shows correctly in the PDF export when you set the Auto Expands property of the table to "true" and the Horizontal Alignment property of the field in the cell to "right". |
| Web Report Studio - Chart | 73965 | Web Report Studio now loads report charts successfully. |
| Web Report Studio - Chart Data Label | 73229 | Web Report Studio now rotates data labels in charts successfully. |
| Web Report Studio - Chart Data Label | 73766 | Web Report Studio now displays correct percentage values in chart data labels, with enhanced decimal rounding. |
| Web Report Studio - Edit Mode | 73758 | Web Report Studio now does not display the Edit Mode option for a linked report when you do not have the Edit permission on the primary report. |
| Web Report Studio - Sort Chart | 72284 | Web Report Studio now pushes down aggregation to database when you sort by an aggregation field in charts. |
| Web Report Studio - Table | 73355 | Web Report Studio now displays proper cell width in the table group footer panel after you change the bottom border width of the group footer. |
| Web Report Studio - True Type Font | 74118 | Web Report Studio now downloads the true type font OpenSans-regular from Logi Report Server and displays it in web reports successfully. |

## v17.1 Update 1 Known Issues

**Report data gets cut off in PDF result due to PDF page size limitation**

When you export a report to PDF, you will find that in the PDF output, some data of the report are cut off if the report contains a large amount of data but its page mode was specified to be continuous page mode or its page size was set to be larger than 200 inches. This is due to a PDF limitation where the data displayed can be no larger than 200 inches in a single PDF page.

**Unsupported go-to action temporarily when using dynamic formulas on chart**

You will get exceptions when you perform the go-to action on a chart which uses a dynamic formula as its shown value and the formula contains group information. This is a limitation in the current version. It will be resolved in a future release.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748362-Logi-Report-v17-1-Enhancements)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009748362-Logi-Report-v17-1-Enhancements)
