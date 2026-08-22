---
title: "Logi Report v18.1 Release Notes"
id: 4405683905815
section: "Release Notes for Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683905815-Logi-Report-v18-1-Release-Notes
updated_at: 2022-01-27T08:00:07Z
---

# Logi Report v18.1 Release Notes

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4411830858775-Logi-Report-v18-2-Enhancements)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690623895-Logi-Report-v18-1-Enhancements)

# Logi Report v18.1 Release Notes

This topic describes feature enhancements, resolved issues, and known issues of the Logi Report v18.1 releases.

For more product information, including new purchases and upgrades, contact [US Sales](mailto:salesteam@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me. "US Sales email address.") or [UK Sales](mailto:emea_sales@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product.%20Please%20contact%20me. "Email address for UK sales team.").

* [v18.1 Service Pack 3 Resolved Issues](#SP3)
* [v18.1 Service Pack 2 Resolved Issues](#SP2)
* [v18.1 Service Pack 1 Resolved Issues](#SP1)
* [v18.1 Feature Enhancements](#Feature)
* [v18.1 Resolved Issues](#Resolved)
* [Known Issues](#Known)

## v18.1 Service Pack 3 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| Enhanced Performance of Rendering Page Reports | 80963 | Server can now run page reports with parameters in Page Report Studio faster through performance enhancements relating to checking business view resources availability, when you are not the built-in system admin user. |
| Logi Report Server Upgrade in Tomcat | 85313 | Logi Report Server no longer acts like the Logi Report Server version in the WAR is higher than that in the reporthome (causing it to back up the workspace), when you have upgraded Logi Report Server from V13.1 update 2 successfully in Tomcat, and both Logi Report Servers in the WAR and reporthome are the new version. |
| Switch Between Page Report Tabs | 80812 | You can now switch between report tabs in Page Report Studio. |

## v18.1 Service Pack 2 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| Change of Top Layer Cascading Parameter Values | 80301 | Server now submits the proper parameter values to the page report, when you change all values of the top-layer parameter of cascading parameters to specific values in a parameter form control. |
| Create Parameter with API | 80545 | You can now use the API method *boolean set(JetObject obj, ParameterInfo info)* to successfully define the value list for a type-in parameter. |
| Designer Connects with Server | 79955 | You can now connect Designer with Server via SSL, regardless of the certificate Server is using. |

## v18.1 Service Pack 1 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| Crosstab Formula | 79981 | You can now successfully run a crosstab containing crosstab formulas that apply the *isNull()* function. |

## v18.1 Feature Enhancements

| Title | Description |
| --- | --- |
| [Blank Spaces in Field Values in Text](https://devnet.logianalytics.com/hc/en-us/articles/4405690623895-Logi-Report-v18-1-Enhancements#TrimBlankSpaces) | You can now remove or keep blank spaces at the beginning and end of field values in your text output. See [Trim Blank Spaces](https://devnet.logianalytics.com/hc/en-us/articles/4405683737751-Advanced-Run-Dialog-Box-Properties#TrimBlankSpaces). |
| [Customizable Object Reading Order in Accessible PDF](https://devnet.logianalytics.com/hc/en-us/articles/4405690623895-Logi-Report-v18-1-Enhancements#ObjectSequence) | You can now change the order of the report objects in the accessible PDF of your report. See Adjusting the Reading Order of Report Objects in Accessible PDF in the *Logi Report Designer Guide*. |
| Easy Removal of Paragraphs | Designer now displays nodes for the paragraphs you create in the report body of page report tabs in the report structure tree of the Report Inspector, enabling you to remove them easily by just deleting the nodes. See Paragraph Properties in the *Logi Report Designer Guide*. |
| Enhanced Accessible PDF | You can now export tables and crosstabs to a tagged PDF to make finding contents in the PDF easier. |
| [Enhanced Default Report Style](https://devnet.logianalytics.com/hc/en-us/articles/4405690623895-Logi-Report-v18-1-Enhancements#DefaultSequential) | Logi Report now has a new report style called DefaultSequential. This is also the default report style, providing you with an enhanced and modern look for your new reports. |
| Enhanced UX for Controlling Page Properties Using Formula | Designer now guides you to bind data first when you want to use a formula to control some page properties for a page report tab, if you have not bound data to its report body. See Bind Data Dialog Box in the *Logi Report Designer Guide*. |
| [Improved Report UI/UX](https://devnet.logianalytics.com/hc/en-us/articles/4405690623895-Logi-Report-v18-1-Enhancements#ImprovedReportUI) | Logi Report has modernized the style of embedded components like Table, Chart, Crosstab, Banded Object, and Web Control, enhancing their look and feel. |
| [Merged Cell in Excel Output](https://devnet.logianalytics.com/hc/en-us/articles/4405690623895-Logi-Report-v18-1-Enhancements#MergedCell) | You can now use the Merged Cell property of a table cell to specify whether the cell is also a merged cell in the Excel output of a report, when the cell displays with its sequential cells as a merged cell in the report result. See Table Cell Properties in the *Logi Report Designer Guide*. |
| Support for OpenJDK 14 | Logi Report now supports OpenJDK 14, in addition to OpenJDK 8, 11, 12, and 13. |
| Termination of Flash Support | Logi Report no longer supports Flash as a report component. |
| [Web Report Files in XML](https://devnet.logianalytics.com/hc/en-us/articles/4405690623895-Logi-Report-v18-1-Enhancements#XMLWebReport) | You can now save web report files in XML in both Designer and Web Report Studio, and download web reports from Server to Designer as XML resources. See:   * [Saving a Web Report](https://devnet.logianalytics.com/hc/en-us/articles/4405684044439-Saving-a-Web-Report) * [Save As Dialog Box Properties](https://devnet.logianalytics.com/hc/en-us/articles/4405690607895-Save-As-Dialog-Box-Properties) |

## v18.1 Resolved Issues

| Title | Case # | Description |
| --- | --- | --- |
| Blank Page Report | 79270 | Page reports no longer show blank in the Designer View Mode and Page Report Studio with NullPointerException when you upgrade from v16.1. |
| Blank Report Result on Remote Server | 79415 | Reports no longer show blank when running on a remote standalone Logi Report Server, which runs as a Windows service, if you access the server using HTTPS. |
| Change JDashboard Theme | 78635 | Dashboards now display successfully after you change the theme. |
| Conditional Formatting on DBFields in Nested Banded Object | 78000 | Logi Report can now apply the conditional formatting you specify on DBFields in a banded object that is inside another banded object. |
| Conditionally Formatted Background Color | 77519 | Conditionally formatted background color now displays properly when you publish using "E-mail Result in HTML E-mail Format." |
| Crosstab/Chart Wizard | 78538 | Crosstab Wizard and Chart Wizard now work properly when you clear the Style checkbox in the Page Report Studio profile. |
| DBArray Values | 67719 | Logi Report now returns correct DBArray values for constant level formulas. |
| Default Value for Category Label Text | 78406 | Designer now does not assign a default value for the Label Text option, when you clear the Auto checkbox in the Axis tab of the Format Category (X) Axis dialog box. |
| Display Parameter Values | 78583 | Web Report Studio now displays the proper parameter values for parameter form controls in link reports that you open from other reports. |
| Display Save As Dialog Box | 78224 | Server now displays the Save As dialog box without error from a page report in the JavaScript API demo when you are a user in an organization and set the "jrd\_userinfo" property. |
| Empty Parameter Values | 77136 | Server now displays empty values properly in a parameter value list. |
| Enhanced Web Report Running Experience | 78871 | Server now responds quickly with an error message, if resource mapping names in formulas are invalid to available data sources, when you run web reports created in Web Report Studio. |
| Font Size of Hyperlink with Dynamic Fields | 77667 | Designer now displays the other text of the email or URL hyperlink in normal size in the Hyperlink box of the Insert Link and Edit Link dialog boxes, when you use dynamic fields in the hyperlink. |
| Formula Syntax Check | 78870 | Designer now displays a syntax error message when you save a formula that contains the "@" symbol before the function, for example, *@ToText*. |
| FTP/SFTP Information Removal | 79625 | Server no longer removes FTP/SFTP information after you change cascading parameter values when updating scheduled task properties. |
| Memory Leak | 78453 | Server now closes related virtual datasets after you close page reports, to help avoid memory leaks. |
| Multiple Parameter Values Selection | 78232 | Server now displays the proper button for you to select multiple parameter values. |
| Page Report Studio Performance | 78218 | Page Report Studio now responds quickly when you perform actions on tables. |
| Panel Height in Horizontal Banded Object | 77873 | Designer now keeps the height of the existing panels when you insert a new banded header panel (BH) into a horizontal banded object. |
| Parameter Value Delimiter | 78332 | The parameter property "Value Delimiter" now works properly in Page Report Studio. |
| Printable PDF Page Report Output | 79604 | You can now create printable PDF page report output with multiple pages without error. |
| Publish Subreports | 78665 | Server now publishes all the subreports when you publish the primary report to another server. |
| Resource Conversion | 78004 | Server now converts resources of earlier versions without displaying the NullPointerException error message. |
| Run Dashboards | 79085 | Dashboards now run successfully without displaying the NotSerializableException error message in the RMI integration environment. |
| Run Web Reports in Web Report Studio | 78806 | Web reports containing empty values now run successfully in Web Report Studio without displaying the NullPointerException error message. |
| Select All Parameter Values Using Shift | 78609 | You can now select all parameter values from a search, using Shift in Page Report Studio. |
| Sort Summary Table Group Column | 78871 | Web Report Studio now sorts group columns in summary tables properly without displaying the ArrayIndexOutOfBoundsException error message, when the group fields are VARCHAR date type with invalid precision. |
| Timestamp Parameter Values with 12 Hour Format | 78964 | Logi Report no longer changes a PM value to AM after you submit Timestamp parameter values using the 12-hour format in the web report Enter Parameter Values window. |
| Time Zone on Server | 77670 | Time zone settings now work properly when reports run upon scheduled tasks on Server. |

## Known Issues

**Report data gets cut off in PDF result due to PDF page size limitation**

When you export a report to PDF, you will find that in the PDF output, some data of the report are cut off if the report contains a large amount of data but its page mode was specified to be continuous page mode or its page size was set to be larger than 200 inches. This is due to a PDF limitation where the data displayed can be no larger than 200 inches in a single PDF page.

**Unsupported go-to action temporarily when using dynamic formulas on chart**

You will get exceptions when you perform the go-to action on a chart which uses a dynamic formula as its shown value and the formula contains group information. This is a limitation in the current version. It will be resolved in a future release.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4411830858775-Logi-Report-v18-2-Enhancements)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690623895-Logi-Report-v18-1-Enhancements)
