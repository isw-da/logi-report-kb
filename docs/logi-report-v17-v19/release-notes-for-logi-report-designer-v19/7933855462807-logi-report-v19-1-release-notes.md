---
title: "Logi Report v19.1 Release Notes"
id: 7933855462807
section: "Release Notes for Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/7933855462807-Logi-Report-v19-1-Release-Notes
updated_at: 2022-11-02T03:53:09Z
---

# Logi Report v19.1 Release Notes

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/9898540229783-Logi-Report-v19-2-Enhancements)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/7933825213847-Logi-Report-v19-1-Enhancements)

# Logi Report v19.1 Release Notes

This topic describes feature enhancements, resolved issues, and known issues of Logi Report v19.1. Subsequent updates are listed chronologically, most recent first.

For more product information, including new purchases and upgrades, contact [US Sales](mailto:salesteam@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me. "US Sales email address.") or [UK Sales](mailto:emea_sales@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product.%20Please%20contact%20me. "Email address for UK sales team.").

* [v19.1 Service Pack 3 Resolved Issues](#SP3)
* [v19.1 Service Pack 2 Resolved Issues](#SP2)
* [v19.1 Service Pack 1 Resolved Issues](#SP1)
* [v19.1 Feature Enhancements](#Feature)
* [v19.1 Resolved Issues](#Resolved)
* [Known Issues](#Known)

### Log4j and Log4Net Vulnerabilities Update

In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: [Statement on Log4j and Log4Net Vulnerabilities](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751).

## v19.1 Service Pack 3 Resolved Issues (10/31/2022)

| Title | Case # | Change Description |
| --- | --- | --- |
| Formulas After Upgrade | 02183104 | Report Customers upgrading from v14 to v19 can now return correct formula values when the formula references two functions as *func1() || func2()*. |
| Memory Leaks from SortGrpNodeEngine | 02190949 | Memory leaks are no longer created by SortGrpNodeEngine in Server. |
| Scroll down Page Report to Next Page | 02243081 | Page Report Studio now displays the next page when you scroll down to the bottom, no matter whether the page report has a horizontal scrollbar. |

## v19.1 Service Pack 2 Resolved Issues (9/30/2022)

| Title | Case # | Change Description |
| --- | --- | --- |
| Computed Columns with Parameters | 02181958 | After upgrading from v16 to v18.3, Designer now displays the Enter Parameter dialog box, when you preview reports that apply a query containing computed columns using parameters. |
| Convert CQR Files Containing Null Values | 02142250 | You can now properly convert String values in your cached query result (CQR) files using cqrtrans.bat/cqrtrans.sh, when the files contain null values. |
| Convert .xml Reports and Catalogs | 02152903 | You can now run rptconv.bat/rptconv.sh in Designer v19.1.2 to convert reports and catalogs saved in .xml format in an earlier release. |
| Crosstab Performance | 02123012 | Server now reduces memory footprint by reusing column description instances, and creating formulas related to crosstabs only when needed. |
| Display Reports with Crosstabs | 02170883 | You can now run reports with crosstabs in Web Report Studio, and if the business view's name is the same as the name of a field in the business view without getting a JavaScript error - TypeError. |
| Group Order of Tables in .xml Reports | 02153851 | You can now reopen a table report saved in .xml format to edit the order of the groups you have added to the table in the Table Wizard. |
| Open Linked Report Containing Parameters | 02091063 | You can now open a linked report that contains parameters that apply values passed from the primary report, when the parameters are also referenced by other parameters. |
| Preview and Export Reports with Conditional Links | 02161417 | You can now preview reports containing conditional links in Designer and export the reports, after upgrading from v18.3 SP1 to v19.1 SP1. |
| Preview Expression Controlled Reports | 02140344 | You can now preview reports created using v16.1 Update 1 that use expressions referencing formulas applying global variables to control object properties in the reports, after upgrading to v19.1. |
| Preview Reports Containing Dynamic Formulas | 02157786 | You can now preview reports containing dynamic formulas that reference local parameters without Designer displaying formula syntax errors after upgrading from v18.2 to v19.1. |
| Suppress Crosstab Column/Row Totals | 02123012 | Server no longer calculates aggregation fields in the same column/row if no other objects reference the aggregation fields in the report, to improve crosstab performance, when you suppress column/row subtotals or grand totals. |

## v19.1 Service Pack 1 Resolved Issues (8/31/2022)

| Title | Case # | Change Description |
| --- | --- | --- |
| @INNER as Parameter Value | 02122439 | Page Report Studio now replaces @INNER with the proper field value at runtime when you use a formula to control the Hyperlink property on a chart and set @INNER as a parameter value. |
| Display Zero Values in Chart Legend | 02071089 | You can now display zero values in the chart legend by setting the Show All Labels property of chart legend to "true". |
| Group Headers in Nested Banded Objects | 02095530 | Logi Report now displays the entire group header in a banded object on the next page if it cannot completely show on current page, when the banded object is in the group header panel of another banded object and you set the Cross Page property of the parent group header panel to "true". |
| Pass Parameter Values with "%" to Linked Reports | 02120521 | Server can now pass proper parameter values to linked reports when the parameter values contain the "%" character. |

## v19.1 Feature Enhancements (7/29/2022)

| Title | Description |
| --- | --- |
| Advanced Fill Color List for Charts | Web Report Studio now applies the advanced fill color list that you defined for charts in Designer. |
| [Bookmark Web Reports](https://devnet.logianalytics.com/hc/en-us/articles/7933825213847-Logi-Report-v19-1-Enhancements#Bookmark) | You can now bookmark web reports and manage bookmarks at the report level in Web Report Studio. See [Bookmarking a Web Report](https://devnet.logianalytics.com/hc/en-us/articles/7985371637143-Bookmarking-a-Web-Report) in the *Logi Report Server Guide*. |
| [Crosstab Formulas](https://devnet.logianalytics.com/hc/en-us/articles/7933825213847-Logi-Report-v19-1-Enhancements#CrosstabFormula) | You can now use crosstab formulas in web reports and business view-based page reports in Designer, in addition to query-based page reports, and create and edit crosstab formulas in Web/Page Report Studio at runtime as well. See the following links in the *Logi Report Server Guide*:  * [Using Dynamic Resources and Local Parameters in Web Report](https://devnet.logianalytics.com/hc/en-us/articles/5741476426263-Using-Dynamic-Resources-and-Local-Parameters-in-Web-Report-) * [Using Dynamic Resources in Page Report](https://devnet.logianalytics.com/hc/en-us/articles/5741438849559-Using-Dynamic-Resources-in-Page-Report) |
| [Customizable Length of Chart Category Names](https://devnet.logianalytics.com/hc/en-us/articles/7933825213847-Logi-Report-v19-1-Enhancements#CategoryLength) | If you choose to limit the number of characters you want to display in your category names, you can now specify the maximum number of characters using the Maximum Length property on the Chart Paper object. See [Chart Paper Properties](https://devnet.logianalytics.com/hc/en-us/articles/5735546052119-Chart-Paper-Properties#MaximumLength). |
| [Customizable TOC Style](https://devnet.logianalytics.com/hc/en-us/articles/7933825213847-Logi-Report-v19-1-Enhancements#TOC) | You can now apply different formatting to the title and entries of each level in the table of contents of your reports. See:  * [Adding a Table of Contents in a Report](https://devnet.logianalytics.com/hc/en-us/articles/5735569955863-Adding-a-Table-of-Contents-in-a-Report) * [Format TOC Title & Levels Dialog Box](https://devnet.logianalytics.com/hc/en-us/articles/7933801563543-Format-TOC-Title-Levels-Dialog-Box) |
| [Dynamic Bursting File Names](https://devnet.logianalytics.com/hc/en-us/articles/7933825213847-Logi-Report-v19-1-Enhancements#DynamicFileName) | You can now define dynamic bursting file names to include field values when scheduling report bursting tasks, by using "recipMapping\_<colName>" in file names. See the following links in the *Logi Report Server Guide*:  * [Scheduling Bursting Reports](https://devnet.logianalytics.com/hc/en-us/articles/5741463244055-Scheduling-Bursting-Reports) * [Applying Dynamic Names for Published Report Files](https://devnet.logianalytics.com/hc/en-us/articles/5741483587607-Applying-Dynamic-Names-for-Published-Report-Files) |
| [Dynamic Link from Current Chart Category/Series](https://devnet.logianalytics.com/hc/en-us/articles/7933825213847-Logi-Report-v19-1-Enhancements#CurrentCategory) | When creating links on data markers in charts in both Designer and Web Report Studio, you can now use Current Category/Series in the link conditions, URLs, or email addresses, to enable users to generate dynamic links from different chart categories/series. See [Adding Links in a Report](https://devnet.logianalytics.com/hc/en-us/articles/5735569846807-Adding-Links-in-a-Report). |
| Formula Controllable Excel Properties | You can now use formulas when exporting a report to Excel, to dynamically specify the maximum number of rows in every worksheet (Rows per Sheet), the sheet name for the report (Sheet Name), and whether to remove page breaks (No Page Break for Column/Data/Report Format) in the Excel output. |
| [Organization Management via JavaScript API](https://devnet.logianalytics.com/hc/en-us/articles/7933825213847-Logi-Report-v19-1-Enhancements#OrganizationAPI) | You can now get, create, update, and delete organizations, as well as get and update the resource allocation of organizations, using the JavaScript REST API. |
| [Profile Customization](https://devnet.logianalytics.com/hc/en-us/articles/7933825213847-Logi-Report-v19-1-Enhancements#CustomizeProfile) | You can now customize all common and specific properties for Web Report Studio, Page Report Studio, and JDashboard together in the server profile at the task level more conveniently, using either the Server Console or API. See the following links in the *Logi Report Server Guide*:  * [Configuring Server Profile](https://devnet.logianalytics.com/hc/en-us/articles/5741409420567-Configuring-Server-Profile) * [Customize Profile Dialog Box Properties](https://devnet.logianalytics.com/hc/en-us/articles/7985371543191-Customize-Profile-Dialog-Box-Properties) |
| [Shared Datasets in Web/Page Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/7933825213847-Logi-Report-v19-1-Enhancements#ShareDataset) | In Web/Page Report Studio, Data components in one report can now share and inherit datasets and dataset filters for better performance, and you can manage datasets as you do in Designer. See the following links in the *Logi Report Server Guide*:  * [Managing Datasets in Web Report](https://devnet.logianalytics.com/hc/en-us/articles/7985339998487-Managing-Datasets-in-Web-Report) * [Managing Datasets in Page Report](https://devnet.logianalytics.com/hc/en-us/articles/7985371620375-Managing-Datasets-in-Page-Report) |
| Synchronized Title in Filter Control and Special Field Expression | Logi Report now applies the text you specify as the title of a Text List filter control in the filter expression of the related On-screen Filter special field. See [Filter Control Properties](https://devnet.logianalytics.com/hc/en-us/articles/5735533183511-Filter-Control-Properties). |
| Third-Party Package Upgrade | Logi Report upgrades the support for some third-party packages to newer versions. |
| Title Height of Text List Filter Control | You can now use the Title Height property of a Text List filter control to ensure that larger fonts in titles are visible. See [Filter Control Properties](https://devnet.logianalytics.com/hc/en-us/articles/5735533183511-Filter-Control-Properties). |

## v19.1 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| Access to Shared Reports in Organizations | 02077468 | You can now run shared reports in the Organization Reports folder when signed in as an Administrator. |
| Bind Data to Report Body | None | Designer now selects the dataset you have bound to the report body of a web report or business view-based page report, when you reopen the Bind Data dialog box. |
| Change Range Slider Value | 2077392 | Server no longer displays a NullPointerException error message when you change the values in range sliders in dashboards. |
| CSS Code Enhancement | None | Server now enhances and standardizes CSS code that may not render properly. |
| Date and Time Display in Excel | 02020904 | Server now displays the correct date and time values in the Excel output when the date is October 25th. |
| Date Selection in Parameter Form Control | 01869524 | Web Report Studio now applies the correct date to parameters when you clear the values of the parameters and change the values of other date parameters in a parameter form control. |
| Decimal Values in Chart Legend | 02091067 | After upgrading from v16 Update 2 to v18.3, Designer now correctly displays the fractional part of the decimal values in the chart legend. |
| Drag Field from Existing Dataset to Web Report | None | Designer no longer creates a new, duplicate dataset in a web report, when you drag a field that is in the dataset applied by a data component of the report, from the Data panel to the report body or page header/footer panel. |
| Extra Border Lines in Crosstabs | 02089842 | Server no longer adds extra lines to the right and bottom borders of crosstabs after you set the background color. |
| Faster Crosstab Display with Suppressed Aggregations | None | Web/Page Report Studio displays crosstabs faster when you suppress aggregations and no other aggregations reference the suppressed aggregations. |
| Faster Linked Report Display | 2069380 | When you select a linked report, Server displays the report faster. |
| JDK Selection in Server installer | 02076767 | Server installer can now display your local JDKs successfully when you use the two system environment variables "\_JAVA\_OPTIONS" and "JAVA\_TOOL\_OPTIONS". |
| Minimize the Catalog Manager Window in Designer | 02089894 | After upgrading from v15.5 to v19, you can now minimize the Catalog Manager window to the smallest size in Designer, when you select Always on Top for the window. |
| New Dynamic Connection with Duplicate Key | 01998146 | Server no longer displays a duplicate key error message when you add new dynamic connections to existing ones after upgrading from v17.1 Update 1. |
| No Delimiter For Text Export | 02005828 | Server now uses double quotation marks as the delimiter without displaying an exception, when you export reports to text, select Save to File System, and then select Custom Delimiter, but define no delimiter. |
| JRotator with Formula-Controlled Properties | 02028886 | You can now reopen the page report containing a JRotator user-defined object (UDO), when you use a formula to control any property of the JRotator. |
| Open Link from Designer Preview | 02076062 | After upgrading to v19, when you preview a report and open a link that contains special characters such as "+" and "=" from the report, Designer now opens the link properly in your browser. |
| Pass Parameter Values to Subreports from Charts | 02087390 | Web Report Studio now passes the proper parameter values to subreports when you select category names in bar/bench charts after using the scroll bar. |
| PDF Output with Multiple Pages | 02079102 | Server now displays the PDF output of your linked page report on multiple pages as expected instead of one page, when you clear Auto Fit for paper height in the Page Setup dialog box. |
| Preview and Run Reports with DateTime Parameters | 02038387 | You can now preview and run reports containing DateTime parameters in both Designer and Server, without Logi Report displaying an error message. |
| Preview Reports Containing Expressions in Designer | 02064671 | Designer now displays a report quickly without compiling formulas of the same name repeatedly, when you use expressions to control values of many object properties in the report. |
| Publish Later Version Resources | 02006433 | Designer now properly displays an error message when you attempt to publish resources to Server that you saved using a later version of Designer. |
| Publish Reports from Designer to Server | 02015704 | You can now successfully publish reports from Designer to Server, when the catalog in the target folder on the server resource tree does not have a version. |
| Reduce Server WAR/EAR Size | 02014384 | Server now enables you to remove the Feature Guide from your Logi Report Server WAR/EAR, reducing the size of the file by over 150 MB. |
| Report Pages Overlap in Nested Banded Report | 02069315 | After you upgrade from v16 Update 2 to v18.3 SP 1, Logi Report now properly displays content in the report pages without overlapping, when the report contains a banded object and you nest more than two layers of child components in the banded object. |
| Scrollable Bench Chart | 02087390 | Logi Report now displays the correct categories on a scrollable bench chart, according to the value range you select from the scroll bar. |
| Sort Crosstab Column/Row | None | You can now set the Order By property for the column/row fields of crosstabs in business view-based page reports, to sort the column/row headers of the crosstabs by another field. |
| Specify Parameter Values on Server Console | 02086946 | Server Console now retains your type-in parameter value updates, when you type to change an existing value, or when you select a value from the value drop-down list. |
| SQL Error after Upgrade | 2075714 | After you add dynamic connections and upgrade from v18.3, Server no longer stops with an SQL exception when using SQL Server as the system database. |
| Table Display in Dashboards | 01994968 | Server now properly displays tables in dashboards in the RMI environment. |
| Use Expression for Group Object | 02011766 | You can now select Settings in the New/Edit View Element dialog box, to write an expression to retrieve values for a group object. |
| Wrap Text | 02089500 | Logi Report now applies the same font size to display and wrap text, so the text can display without cut-off after being wrapped. |

## Known Issues

**Report data cut off in PDF due to PDF page size limitation**

When you export a report to PDF, you will find that in the PDF output, some data of the report are cut off if the report contains a large amount of data but its page mode was specified to be continuous page mode or its page size was set to be larger than 200 inches. This is due to a PDF limitation where the data displayed can be no larger than 200 inches in a single PDF page.

**Unsupported go-to action when using dynamic formulas on chart**

You get exceptions when you perform the go-to action on a chart that uses a dynamic formula as its shown value and the formula contains group information. This is a limitation in the current version.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/9898540229783-Logi-Report-v19-2-Enhancements)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/7933825213847-Logi-Report-v19-1-Enhancements)
