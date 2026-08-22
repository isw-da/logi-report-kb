---
title: "Logi Report v18 Release Notes"
id: 4405664606871
section: "Release Notes for Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664606871-Logi-Report-v18-Release-Notes
updated_at: 2022-03-01T06:34:59Z
---

# Logi Report v18 Release Notes

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661783703-Logi-Report-v18-1-Enhancements)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661782679-Logi-Report-v18-Enhancements)

# Logi Reportv18 Release Notes

This topic describes feature enhancements, resolved issues, and known issues of the Logi Report v18 release, from April 30, 2021.

For more product information, including new purchases and upgrades, contact [US Sales](mailto:salesteam@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me. "US Sales email address.") or [UK Sales](mailto:emea_sales@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product.%20Please%20contact%20me. "Email address for UK sales team.").

* [Feature Enhancements](#Feature)
* [Resolved Issues](#Resolved)
* [Known Issues](#Known)

### Log4j and Log4Net Vulnerabilities Update

In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: [Statement on Log4j and Log4Net Vulnerabilities](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751).

## Feature Enhancements

| Title | Description |
| --- | --- |
| [Business View](https://devnet.logianalytics.com/hc/en-us/articles/4405661782679-Logi-Report-v18-Enhancements#BVSecurity) | Server administrators can now define business view security in a catalog and customize business views for reports. See the following topics in the *Logi Report Server Guide*:  * Defining Business View Security in a Catalog * Customizing Business Views for Reports |
| [Change Server Resource Owner](https://devnet.logianalytics.com/hc/en-us/articles/4405661782679-Logi-Report-v18-Enhancements#ChangeResourceOwner) | Server administrators can now change the owner of a resource. See Resource Owner in the *Logi Report Server Guide*. |
| Chart Static Data Labels | You can now specify the rotation angle of the text in the static data labels of a chart, regardless of their position on the data markers. |
| [Column Resources for Parameters](https://devnet.logianalytics.com/hc/en-us/articles/4405661782679-Logi-Report-v18-Enhancements#EnhancedParameter) | You can now use columns in queries or imported APEs as the Bind Column and Display Column of parameters. See: [Creating Parameters in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/4405664612887-Creating-Parameters-in-a-Catalog#Predefine). |
| [Constrained Runtime Data](https://devnet.logianalytics.com/hc/en-us/articles/4405661782679-Logi-Report-v18-Enhancements#ConstrainedData) | You can now use the Constrained Data property to specify the data sources that users can apply at runtime, if they need to add more data components into the reports developed in Designer. See:  * [Page Report Properties](https://devnet.logianalytics.com/hc/en-us/articles/4405664668695-Page-Report-Properties) * [Web Report Properties](https://devnet.logianalytics.com/hc/en-us/articles/4405661909143-Web-Report-Properties) |
| [Customizable Chart Value Names in Hint](https://devnet.logianalytics.com/hc/en-us/articles/4405661782679-Logi-Report-v18-Enhancements#ChartValueName) | You can now customize the names of the fields on the value axis of a chart, which you want to display in the data marker hint of the chart to provide users meaningful information. See: [Customize Chart Value Names Dialog Box](https://devnet.logianalytics.com/hc/en-us/articles/4405661488279-Customize-Chart-Value-Names-Dialog-Box). |
| [Customizable Sheet Name in Excel Output](https://devnet.logianalytics.com/hc/en-us/articles/4405661782679-Logi-Report-v18-Enhancements#EnhancedExcel) | You can now use the Sheet Name property to specify the sheet name for a web report or business view-based page report tab, in the Excel output. See:  * [Page Report Tab Properties](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties) * [Web Report Properties](https://devnet.logianalytics.com/hc/en-us/articles/4405661909143-Web-Report-Properties) |
| Customize Toolbar in Page Report Studio Basic View | You can now easily display the TOC Browser, show or hide toolbar items, and adjust their order, in the Basic View of Page Report Studio. See the following topics in the *Logi Report Server Guide*:  * Customize the toolbar items in the Basic View * TOC Browser |
| [Dynamic MongoDB Connection and Imported APE](https://devnet.logianalytics.com/hc/en-us/articles/4405661782679-Logi-Report-v18-Enhancements#DynamicMongoDB) | You can now reference parameters, constant level formulas, and the special field "User Name" when specifying the information to connect to a MongoDB database, and use a parameter or constant level formula to specify the database and collection from which to get data for an imported APE. See:  * [Working with MongoDB Connections in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/4405664420375-Working-with-MongoDB-Connections-in-a-Catalog#Set) * [MongoDB Connection Properties](https://devnet.logianalytics.com/hc/en-us/articles/4405661818391-MongoDB-Connection-Properties) * [Using Imported APEs](https://devnet.logianalytics.com/hc/en-us/articles/4405664418583-Using-Imported-APEs#Import) * [Imported APE Properties](https://devnet.logianalytics.com/hc/en-us/articles/4405664616343-Imported-APE-Properties) |
| [Enhanced Custom Aggregation](https://devnet.logianalytics.com/hc/en-us/articles/4405661782679-Logi-Report-v18-Enhancements#EnhancedCustomAgg) | You can now create custom aggregations for group level calculations referenced by specific members of the groups, including the maximum and minimum members. |
| [Enhanced Format for Empty Cells in Excel Output](https://devnet.logianalytics.com/hc/en-us/articles/4405661782679-Logi-Report-v18-Enhancements#EnhancedExcel) | You can now use the Full Fill and Border property to specify whether to apply format to the empty cells in the Excel output of your reports. See:  * [Page Report Tab Properties](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties) * [Web Report Properties](https://devnet.logianalytics.com/hc/en-us/articles/4405661909143-Web-Report-Properties) |
| Formula Control for Alignment Properties in Page Report | You can now use a formula to control the Horizontal Alignment and Vertical Alignment properties of data fields and labels in page reports. |
| [Formula Control for Page Properties](https://devnet.logianalytics.com/hc/en-us/articles/4405661782679-Logi-Report-v18-Enhancements#DynamicPagination) | You can now use constant level formulas to control the page properties of your reports. See:  * [Page Setup Dialog Box](https://devnet.logianalytics.com/hc/en-us/articles/4405664543511-Page-Setup-Dialog-Box) * [Page Panel Properties](https://devnet.logianalytics.com/hc/en-us/articles/4405661878807-Page-Panel-Properties) |
| [Horizontal Table in Business View-Based Page Report](https://devnet.logianalytics.com/hc/en-us/articles/4405661782679-Logi-Report-v18-Enhancements#HorizontalTable) | You can now create horizontal tables in page reports that use business views as the data source. See:  * [Inserting Tables in a Report](https://devnet.logianalytics.com/hc/en-us/articles/4405661401239-Inserting-Tables-in-a-Report) * [Create Table Dialog Box](https://devnet.logianalytics.com/hc/en-us/articles/4405664441879-Create-Table-Dialog-Box) * [Table Wizard Dialog Box](https://devnet.logianalytics.com/hc/en-us/articles/4405661737495-Table-Wizard-Dialog-Box) |
| Keep Scrollable Chart Status in PDF | You can now keep the current data status of scrollable charts in the PDF output. See Keep Scrollable Chart Status in the *Logi Report Server Guide*. |
| Link Org to URL | You can now link Org and Heat Map charts to URL. |
| MongoDB API | Logi Report now supports the new MongoDB client driver API mongodb-driver-sync. |
| [MongoDB Connection on Server](https://devnet.logianalytics.com/hc/en-us/articles/4405661782679-Logi-Report-v18-Enhancements#MongoDBConnectionServer) | You can now configure the MongoDB connection in Logi Report Server or when running reports via URL, and create dynamic MongoDB connections. See the following topics in the *Logi Report Server Guide*:  * Content of datasource.xml * Creating Dynamic Connections * Opening Web Reports in Web Report Studio via JSON * URL Properties for Viewing Reports |
| Open Server Public Reports Folder | You can now open the Public Reports folder quickly on the Server Console when the folder is big, and if many users and groups have complicated permissions on the folder. |
| Page Report Tab Status | You can now specify the report tabs in specific page reports to open by default when users run the page reports in Page Report Studio. See:  * [Customizing the Status of Report Tabs in Page Reports](https://devnet.logianalytics.com/hc/en-us/articles/4405664693399-Managing-Page-Reports#Status) * [Customize Page Report Tab Status Dialog Box](https://devnet.logianalytics.com/hc/en-us/articles/4405661492503-Customize-Page-Report-Tab-Status-Dialog-Box) |
| [Page Report Tab as Subreport](https://devnet.logianalytics.com/hc/en-us/articles/4405661782679-Logi-Report-v18-Enhancements#AsSubreport) | You can now use the Work as Subreport property to define the usage of a page report tab as subreport only, so that the report tab no longer displays in the Go To drop-down list in Page Report Studio. See: [Page Report Tab Properties](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties). |
| Report Body Layout Performance | Logi Report now just fetches necessary layout data when the report body contains only parameters, constant level formulas, or detail DBFields, to improve performance. |
| Sign in LDAP User | You can now specify multiple organization units in an LDAP server to the Distinguished Name property, so that all users in the organization units can sign in to Logi Report Server. See Distinguished Name in the *Logi Report Server Guide*. |
| [Sort and Search Parameter Resources](https://devnet.logianalytics.com/hc/en-us/articles/4405661782679-Logi-Report-v18-Enhancements#EnhancedParameter) | You can now sort and search the DBFields when you specify the Bind Column and Display Column for a parameter. See:  * [New Parameter Dialog Box](https://devnet.logianalytics.com/hc/en-us/articles/4405661658135-New-Parameter-Dialog-Box) * [Edit Parameter Dialog Box](https://devnet.logianalytics.com/hc/en-us/articles/4405664463511-Edit-Parameter-Dialog-Box) |
| [Sort Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/4405661782679-Logi-Report-v18-Enhancements#EnhancedParameter) | You can now sort the values of a parameter that is bound with a single column. See: [Creating Parameters in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/4405664612887-Creating-Parameters-in-a-Catalog#Sort). |
| [Table Columns in Report Output](https://devnet.logianalytics.com/hc/en-us/articles/4405661782679-Logi-Report-v18-Enhancements#TableColumn) | You can now specify whether to include or exclude specific table columns in your report output. See: [Table Column Properties](https://devnet.logianalytics.com/hc/en-us/articles/4405661898263-Table-Column-Properties). |
| Text and CSV Outputs of Report | You can now use the Remove Extra Characters on First Line property to specify whether to remove the quotation marks and commas from the first line of a report's Text and CSV outputs. See:  * [Page Report Tab Properties](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties) * [Web Report Properties](https://devnet.logianalytics.com/hc/en-us/articles/4405661909143-Web-Report-Properties) |
| User Session Timeout | Your user session now expires when you do not perform any operations in Page Report Studio within the amount of time you set for the server.session.timeout property. |
| View Table Header Label Description | You can now see the description of the related data field when you hover over a label in the table header in Web Report Studio and JDashboard. See Show Description When Hovering Over Table Header Labels in the *Logi Report Server Guide*. |
| Web Report Page Template | You can now select a default page template in the Web Report Studio profile in advance, for web reports that you create using quick start. See Setting the Default Page Template for Quick-start Web Reports in the *Logi Report Server Guide*. |

## Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| Banded Object with Cross Page Setting | 76866 | Logi Report Engine now displays banded panels correctly in the report, when the banded object contains more than one group and you set the Cross Page property of all the group header panels to "false". |
| Change Server Context Path | 76036 | You can now change the context path of a standalone Logi Report Server. |
| Columned Excel Output | 75628 | You can now export reports to Excel using Column Format, with the Columned property set to "true". |
| Content Display in Page Report Studio | 75522 | Page Report Studio now fully displays report content. |
| Convert NLS Property File in Server | 75934 | Logi Report Server now also converts the NLS property file when automatically converting the report type of a page report you deployed from Logi Report Designer from .cls.xml to .cls. |
| CSS Style Files to Publish | 76512 | Logi Report Designer now lists the CSS style files that you can publish to Server correctly in the Publish Additional Resources dialog box. |
| Date Format in Dashboards | 76718 | JDashboard now displays date values in sliders according to the format you defined for the field in the catalog. |
| Display Enter Parameter Values Dialog Box | 76852 | JDashboard now displays the Enter Parameter Values dialog box when you open a dashboard that uses parameters, if you select the Show Enter Parameter Values Dialog option in the JDashboard profile, and if you have saved a parameter value that is out of range. |
| DistinctCount in Chart in Dashboard | 77654 | JDashboard now calculates the DistinctCount function in the chart value correctly, when the field you add in the filter control is different from the group-by field of the chart. |
| DistinctSum in Excel | 75558 | The DistinctSum aggregate function in a report now calculates properly when you export the report to Excel. |
| Keep Catalog File in Real Path | 75391 | Logi Report Server now does not delete the catalog file from the real path when you run a page report result file (.rsd) in the server resource tree via URL. |
| Logi Report Result in Excel on Server | 75900 | You can now export a Logi Report Result (.rst) containing no data to Excel with Report Format or Column Format without getting an error message. |
| No Blank Parentheses in On-screen Filter Value | 76427 | Page Report Studio now no longer displays filter values of blank parenthesis "()" in the on-screen filter if there is no value to display. |
| No Null Value for Array Type Field | 76548 | Logi Report now displays the proper report by not passing the null value to an Array type field in a condition, when you upgrade from v12. |
| Open JHyperlink in Email in Browser | 77025 | The UDO JHyperlink in reports now works properly in email messages when you view the email using a browser. |
| Open Link in Email Body | 77025 | Links in reports now work properly when you publish using "Email Result in HTML E-mail Format." |
| Open Page Report on iPad | 75718 | Logi Report Server now hides the menu and toolbar when you open a page report in Safari on the iPad with iOS 14. |
| Open PDF from Remote Tomcat | 75654 | You can now open scheduled PDF outputs on the Logi Report Server Console remotely from within the Tomcat UI. |
| Parameter in Query Filter | 76685 | Logi Report Designer can now parse parameters that you reference in the filter conditions of a query correctly, when you wrap the parameter names in double quotation marks. |
| Pass Plus to Linked Report | 76420 | Web Report Studio now passes the plus character "+" to the parameter of the linked report successfully when you link to the report via URL. |
| Publish Resources to Organization Folders | 77021 | You can now publish resources from Logi Report Designer to the organization folders on a Logi Report Server that is integrated with a Tomcat application server. |
| QR Code in Print Result | 75592 | When you print a report containing a QR Code in Logi Report Designer, the QR Code now displays completely in the print result. |
| Rename Folder During Publishing | 76623 | Logi Report Designer now applies the Rename operation to the folder in the server resource tree correctly, when you specify the target folder to publish your resources. |
| Run Report with Linked Catalog | 76065 | You can now run a report that links to a catalog in another folder and that uses parameters on Logi Report Server within Tomcat without errors. |
| Server Cluster with TCP | 77208 | You can now set up a Logi Report Server Cluster when using TCP in jgroups.xml. |
| Suppress Crosstab Field | 75661 | Web Report Studio and JDashboard now displays the proper result when you enable the Suppress property of crosstab fields. |
| Subreport in Excel Output | 76782 | The banded object which contains a subreport now displays correctly in the Excel output, when you export the primary report to Excel using Column Format after setting the Columned property to "true". |
| Vertical Alignment for JRotator | 75760 | When you set the Vertical Alignment property of a JRotator to "bottom", Logi Report Engine now aligns the text correctly. |
| Web API for Publishing Resources | 76811 | You can now use the "/nodes POST" method in the Web API to publish resources to Logi Report Server. |
| Word Wrap in Excel Output | 75643 | When you export values for a multivalued parameter to Excel, Logi Report Engine correctly word wraps the values. |

## Known Issues

**Report data cut off in PDF due to PDF page size limitation**

When you export a report to PDF, you will find that in the PDF output, some data of the report are cut off if the report contains a large amount of data but its page mode was specified to be continuous page mode or its page size was set to be larger than 200 inches. This is due to a PDF limitation where the data displayed can be no larger than 200 inches in a single PDF page.

**Unsupported go-to action when using dynamic formulas on chart**

You will get exceptions when you perform the go-to action on a chart which uses a dynamic formula as its shown value and the formula contains group information. This is a limitation in the current version. It will be resolved in a future release.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661783703-Logi-Report-v18-1-Enhancements)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661782679-Logi-Report-v18-Enhancements)
