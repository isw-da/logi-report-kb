---
title: "Logi Report v19 Release Notes"
id: 5735568241431
section: "Release Notes for Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735568241431-Logi-Report-v19-Release-Notes
updated_at: 2022-11-02T03:54:38Z
---

# Logi Report v19 Release Notes

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/7933825213847-Logi-Report-v19-1-Enhancements)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735568250647-Logi-Report-v19-Enhancements)

# Logi Report v19 Release Notes

This topic describes feature enhancements, resolved issues, and known issues of Logi Report v19. Subsequent updates are listed chronologically, most recent first.

For more product information, including new purchases and upgrades, contact [US Sales](mailto:salesteam@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me. "US Sales email address.") or [UK Sales](mailto:emea_sales@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product.%20Please%20contact%20me. "Email address for UK sales team.").

* [v19 Service Pack 3 Resolved Issues](#SP3)
* [v19 Service Pack 2 Resolved Issues](#SP2)
* [v19 Service Pack 1 Resolved Issues](#SP1)
* [v19 Feature Enhancements](#Feature)
* [v19 Resolved Issues](#Resolved)
* [Known Issues](#Known)

### Log4j and Log4Net Vulnerabilities Update

In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: [Statement on Log4j and Log4Net Vulnerabilities](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751).

## v19 Service Pack 3 Resolved Issues (7/27/2022)

| Title | Case # | Change Description |
| --- | --- | --- |
| Access to Shared Reports in Organizations | 02077468 | You can now run shared reports in the Organization Reports folder when signed in as an Administrator. |
| Change Range Slider Value | 02077392 | Server no longer displays a NullPointerException error message when you change the values in range sliders in dashboards. |
| JDK Selection in Server Installer | 02076767 | Server installer can now display your local JDKs successfully when you use the two system environment variables "\_JAVA\_OPTIONS" and "JAVA\_TOOL\_OPTIONS". |
| Open Link from Designer Preview | 02076062 | After upgrading to v19, when you preview a report and open a link that contains special characters such as "+" and "=" from the report, Designer now opens the link properly in your browser. |
| PDF Output with Multiple Pages | 02079102 | Server now displays the PDF output of your linked page report on multiple pages as expected instead of one page, when you clear "Auto Fit" for paper height in the Page Setup dialog box. |
| Scrollable Bench Chart | 02087390 | Logi Report now displays the correct categories on a scrollable bench chart, according to the value range you select from the scroll bar. |

## v19 Service Pack 2 Resolved Issues (6/28/2022)

| Title | Case # | Change Description |
| --- | --- | --- |
| Find Published Earlier Version Reports | 02039158 | Server can now find your published previous version reports and run them successfully after you upgrade. |
| JDashboard Disabled | 02038030 | If your Server license has disabled JDashboard, Server no longer displays the two folders My Components and Public Components when you select My Reports or Public Reports on the Resources page of the Server Console. |
| Merge Catalogs Using Catalog Doctor | 02027369 | You can now merge catalogs properly using the Catalog Doctor in Designer v18.3 and later. |
| PDF Output for Second Report Page | 02022100 | Page Report Studio can now successfully generate a PDF for the second report page, when you insert a table into a repeated group header. |
| Run v15.5 Reports | 02029718 | After you upgrade to v19.1, Server now properly displays your v15.5 reports with parameters when running in Tomcat on Windows, without displaying a NullPointerException error message. |
| Suppressed Banded Group Header | 02042903 | After upgrading from v16 Update 2 to v18.3 SP 1 and later, Logi Report no longer displays the group header panel of a banded object in the report, when you set the panel's Suppress property to "true" and the corresponding group's Keep Group Together property to "true" at the same time. |
| Text in Vertical Center Alignment | 02040188 | After upgrading from v15.5 to a later version, Logi Report now properly aligns the text in a field, when you set the field's Vertical Alignment property to "center" and the height of the text is greater than that of the field. |

## v19 Service Pack 1 Resolved Issues (5/30/2022)

| Title | Case # | Change Description |
| --- | --- | --- |
| Keep Group Together Property | 02002737 | You can now set the Keep Group Together property for banded groups in web reports and business view-based page reports in Designer, so the header of a group always displays together with the group details in the same page. |
| Schedule Properties via Web API | 02007417 | Logi Report now includes the "Next Run Time" and "Is Enabled" properties, when you use the Web API to get scheduled task information. |
| Schedule to Email via REST Web API | 02023044 | Server now saves schedule properties properly and sends out emails successfully, when you use the REST Web API to schedule report tasks to email after upgrading from v17.1. |

## v19 Feature Enhancements (4/29/2022)

| Title | Description |
| --- | --- |
| AES 128-Bit Encryption for Configuration Files | Logi Report now uses AES 128-bit encryption algorithm for configuration files. The files include dbconfig.xml, datasource.xml, LDAPProperties.xml, mailconfig.properties, and restdsproxy.xml. |
| Avoid Chrome Pop-Up Block | Logi Report no longer uses the methods window.alert, window.confirm, and window.prompt, to avoid pop-up blocking in Server and Page/Web Report Studio on the latest Google Chrome versions. |
| [Continuous Page Number in Report Outputs](https://devnet.logianalytics.com/hc/en-us/articles/5735568250647-Logi-Report-v19-Enhancements#TOC) | You can now insert the Export Page Number and Export Total Page Number special fields in a report, and set the report's Continuous Page Number with TOC property to specify whether you want to calculate the report pages continuously for the special fields when the report contains a TOC. See:  * [Working with Special Fields](https://devnet.logianalytics.com/hc/en-us/articles/5735564398999-Working-with-Special-Fields#Export) * [Web Report Properties](https://devnet.logianalytics.com/hc/en-us/articles/5735555208983-Web-Report-Properties#ContinuousPageNumber) * [Page Report Tab Properties](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#ContinuousPageNumber) |
| [Custom File Extension for Report Outputs](https://devnet.logianalytics.com/hc/en-us/articles/5735568250647-Logi-Report-v19-Enhancements#CustomFileExtension) | You can now select Use Custom File Extension on the export UI if you want to use your preferred extension (or to have no extension) for the file name of your report output. See:  * [Exporting Reports to HTML](https://devnet.logianalytics.com/hc/en-us/articles/5735553350295-Exporting-Reports-to-HTML) * [Exporting Reports to PDF](https://devnet.logianalytics.com/hc/en-us/articles/5735531895447-Exporting-Reports-to-PDF) * [Exporting Reports to Excel](https://devnet.logianalytics.com/hc/en-us/articles/5735516034199-Exporting-Reports-to-Excel) * [Exporting Reports to Text](https://devnet.logianalytics.com/hc/en-us/articles/5735525405719-Exporting-Reports-to-Text) * [Exporting Reports to RTF](https://devnet.logianalytics.com/hc/en-us/articles/5735531933591-Exporting-Reports-to-RTF) * [Exporting Reports to XML](https://devnet.logianalytics.com/hc/en-us/articles/5735516111511-Exporting-Reports-to-XML) * [Exporting Reports to PostScript](https://devnet.logianalytics.com/hc/en-us/articles/5735531904791-Exporting-Reports-to-PostScript) * [Exporting Reports to Logi Report Result](https://devnet.logianalytics.com/hc/en-us/articles/5735525374615-Exporting-Reports-to-Logi-Report-Result) |
| [Data Container Link in Web Report](https://devnet.logianalytics.com/hc/en-us/articles/5735568250647-Logi-Report-v19-Enhancements#DataContainerLink) | You can now use data container links in web reports to set up data relations between two data containers in a parent-child relationship. See [Setting Up Data Container Links in a Report](https://devnet.logianalytics.com/hc/en-us/articles/5735586301207-Setting-Up-Data-Container-Links-in-a-Report). |
| Easy Removal of Page Panels | You can now use the Delete Page shortcut menu command to delete a page panel from a page report tab or web report. See [Designing the Report Pages](https://devnet.logianalytics.com/hc/en-us/articles/5735569908631-Designing-the-Report-Pages). |
| Enhanced Installer for macOS | You can now run the installer file to install Logi Report on macOS. |
| [Enhanced TOC](https://devnet.logianalytics.com/hc/en-us/articles/5735568250647-Logi-Report-v19-Enhancements#TOC) | You can now add page panels before the TOC page panel in a report if you want to display additional information before the table of contents when you export or print the report, such as a cover or preface for the report. See:  * [Adding a Table of Contents in a Report](https://devnet.logianalytics.com/hc/en-us/articles/5735569955863-Adding-a-Table-of-Contents-in-a-Report) * [Designing the Report Pages](https://devnet.logianalytics.com/hc/en-us/articles/5735569908631-Designing-the-Report-Pages) |
| [JSON/XML Connection Data Cache](https://devnet.logianalytics.com/hc/en-us/articles/5735568250647-Logi-Report-v19-Enhancements#CachedConnectionData) | Administrators can now cache JSON/XML connection data on Server in advance so that reports created from these connections can reuse the cached data, improving the report rendering performance. See [Configuring Cache](https://devnet.logianalytics.com/hc/en-us/articles/5741415874327-Configuring-Cache) in the *Logi Report Server Guide*. |
| [Paginated JSON Data Fetch](https://devnet.logianalytics.com/hc/en-us/articles/5735568250647-Logi-Report-v19-Enhancements#Paginated) | You can now call the method *\_client.send(Request)* or *\_client.send(Request[], integer)* in a formula to fetch paginated JSON data from a REST Web Service either sequentially or concurrently. See [Working with JSON Connections in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/5735528141079-Working-with-JSON-Connections-in-a-Catalog#Paginated). |
| [PDF Title and Subject](https://devnet.logianalytics.com/hc/en-us/articles/5735568250647-Logi-Report-v19-Enhancements#PDF) | You can now define the Title and Subject properties for the PDF output of your reports. See [Exporting a Report to PDF](https://devnet.logianalytics.com/hc/en-us/articles/5735531895447-Exporting-Reports-to-PDF). |
| [Push Down On-Screen Filters to Database](https://devnet.logianalytics.com/hc/en-us/articles/5735568250647-Logi-Report-v19-Enhancements#PushDown) | Logi Report now attempts to apply all filters to the database when generating report data, when you enable On-Screen Filter Push-Down. See:  * [Web Report Properties](https://devnet.logianalytics.com/hc/en-us/articles/5735555208983-Web-Report-Properties#PushDownFilter) * [Page Report Tab Properties](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#PushDownFilter) |
| [Report Bursting Schedule via REST APIs](https://devnet.logianalytics.com/hc/en-us/articles/5735568250647-Logi-Report-v19-Enhancements#BurstingSchedule) | You can now use REST APIs to schedule report bursting tasks to Version/Disk/E-mail/FTP, and schedule non-bursting results to Version/Disk/E-mail/Printer/Fax/FTP. |
| [Share Business View-Based Datasets in Report](https://devnet.logianalytics.com/hc/en-us/articles/5735568250647-Logi-Report-v19-Enhancements#Dataset) | You can now share datasets that are based on business views between data components in a web or page report, to improve the report performance at runtime. See [Applying Datasets in a Report](https://devnet.logianalytics.com/hc/en-us/articles/5735586128791-Applying-Datasets-in-a-Report). |
| Support for macOS Big Sure and Monterey | You can now run Designer on macOS Big Sure and Monterey, in addition to Sierra. |
| Termination of IE Support | Logi Report no longer supports the Microsoft Internet Explorer browser, due to Microsoft terminating support for IE 11 starting June 15, 2022. See https://docs.microsoft.com/en-us/lifecycle/products/internet-explorer-11. |
| Tile Detail Panel with Same Height | You can now set the Tile with Same Height property to apply the same height to record tiles on the same row, when you specify to tile records in the detail panel of a banded object horizontally. See [Detail Panel Properties](https://devnet.logianalytics.com/hc/en-us/articles/9898557673239-Banded-Detail-Panel-Properties#TileWithSameHeight). |
| [TOC Entries for Child Objects](https://devnet.logianalytics.com/hc/en-us/articles/5735568250647-Logi-Report-v19-Enhancements#TOC) | You can now use the report property Ignore TOC Anchor of Parent to control whether to generate TOC entries for objects that are contained in other objects, when you exclude their parent objects from the TOC of a report. See:  * [Web Report Properties](https://devnet.logianalytics.com/hc/en-us/articles/5735555208983-Web-Report-Properties#IgnoreParentTOCAnchor) * [Page Report Tab Properties](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#IgnoreParentTOCAnchor) |

## v19 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| Bar Chart Data Labels | 88006 | Logi Report now displays data labels on the corresponding bars when they exceed the chart wall boundary. |
| Blank Parameter Value Line | 01990640 | Server no longer displays a blank value line in the Enter Values dialog box when you specify multiple values for a parameter, and if the parameter's Enable the "All Values" Option property is "false". |
| Close Designer from Taskbar | 87814 | You can now close Designer by right-clicking on the icon on your taskbar and selecting "Close window". |
| Content in Cross-Page Banded Panel | 86959 | Logi Report now displays the content in a banded panel correctly when the panel spans more than one page. |
| Cross-Origin Frame Access | 88814 | Server no longer blocks cross-origin frame access when you select "New" in the To E-mail tab while scheduling a report task. |
| Data Label Display on Bench Charts | 01994965 | Web Report Studio and Designer now display static data labels in bench charts properly, when the Auto Arrange property is "true". |
| Designer Dialog Box Display | 87028 | Designer now displays dialog boxes correctly after you increase the font size of your operating system. |
| Designer Installation on macOS | 86942 | Designer no longer displays a file damaged error when you double-click jrpsetup.app to install Designer on macOS. |
| Distinct On Field for DistinctSum Summary in XML Catalog | 01972302 | Designer now saves the Distinct On field you specify for a summary that applies the DistinctSum aggregate function, when you save the catalog in XML. |
| Go to Detail on Charts | 01991475 | Web Report Studio now applies values from filter controls to display data the way you want, when you select Go to Detail on a chart. |
| Include jgroups-4.2.11.Final.jar in Server WAR | 88737 | Logi Report Server now includes jgroups-4.2.11.Final.jar in your WAR file, and you can now migrate your Logi Report Server from v17.1 Update 1 to v19.0 successfully with Cluster enabled in Tomcat. |
| MongoDB Connection via SSL | 87416 | You can now set up MongoDB connections using SSL. |
| PDF Export with View Report Result | 87535 | Server can now open PDF outputs in a web browser when you export reports with the View Report Result option in Web/Page Report Studio. |
| Predefined Filters of Business View | 88523 | Designer no longer removes predefined filters you create in a business view, when you sort the view elements in the Business View Editor dialog box. |
| Publish NLS Properties Files with Catalogs | 87789 | Logi Report now publishes NLS properties files together with catalogs, from Designer to remote Servers. |
| Report Content Overwrite | 88038 | Server now passes proper parameter values to two web reports, when you run the two reports to PDF on-demand at the same time, and now Server provides the proper content in the PDF outputs. |
| Run Bursting Reports with Large Data | 88121 | Server no longer displays an OutOfMemoryError message when you run bursting reports with large amounts of data. |
| Run Page Report | 87530 | Page Report Studio now successfully parses IExpression (that references parameters) without errors, when you run page reports. |
| Run Scheduled Reports with Date Parameter Values | 01993895 | When running scheduled reports to email, Server now applies correct date parameter values (if the parameter is an expression referring to the date before today) and displays reports with proper data. |
| Scheduled Tasks in Cluster | 01859224 | When running scheduled reports in a cluster, Server now reduces the possibility of deadlock and synchronizes memory objects only when needed. |
| Scheduled Tasks Simultaneously | 01859224 | Server now creates report running tasks simultaneously rather than one by one to improve performance, when scheduled tasks are triggered at the same time. |
| Scheduled Tasks with Memory Leaks | 01859224 | Server now releases useless cached PageHelper and ParamDesc objects to avoid memory leaks, when you create scheduled tasks or run scheduled reports. |
| Search Scheduled Tasks | 88631 | Server now displays proper results when you search scheduled tasks using the Server Console. |
| Subreport in Excel Output | 88514 | A subreport in the group header panel of a banded object that is more than one page long now displays properly in Excel output, when you set the report's No Page Break for Column Format, No Page Break for Data Format, or No Page Break for Report Format property to "true" and export the report to Excel in the corresponding format. |
| Text Area Border Thickness | 87790 | Logi Report now applies the border thickness you want for the text areas of your reports. |
| True Type Font in Charts | 85645 | Web Report Studio now displays charts with the True Type Font SourceSansPro-Regular properly, when you set NLS Default Language as "French". |
| Unlimited Number of Completed Schedule Tasks | 86131 | Server now enables you to use unlimited number of completed schedule tasks when you set the server.completed.max\_count property to "0". |
| Web Image Referenced in Function | 01997788 | Logi Report now displays the Web image you reference in the *openBinURL()* function correctly, as long as you can access the image using Web browsers. |

## Known Issues

**Report data cut off in PDF due to PDF page size limitation**

When you export a report to PDF, you will find that in the PDF output, some data of the report are cut off if the report contains a large amount of data but its page mode was specified to be continuous page mode or its page size was set to be larger than 200 inches. This is due to a PDF limitation where the data displayed can be no larger than 200 inches in a single PDF page.

**Unsupported go-to action when using dynamic formulas on chart**

You get exceptions when you perform the go-to action on a chart that uses a dynamic formula as its shown value and the formula contains group information. This is a limitation in the current version.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/7933825213847-Logi-Report-v19-1-Enhancements)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735568250647-Logi-Report-v19-Enhancements)
