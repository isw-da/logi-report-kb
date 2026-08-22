---
title: "Logi Report v18.2 Release Notes"
id: 4411822430231
section: "Release Notes for Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4411822430231-Logi-Report-v18-2-Release-Notes
updated_at: 2022-01-27T08:00:09Z
---

# Logi Report v18.2 Release Notes

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4420461816983-Logi-Report-v18-3-Enhancements)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4411830858775-Logi-Report-v18-2-Enhancements)

# Logi Report v18.2 Release Notes

This topic describes feature enhancements, resolved issues, and known issues of the Logi Report v18.2 releases.

* [v18.2 Service Pack 3 Feature Enhancements](#SP3Feature)
* [v18.2 Service Pack 3 Resolved Issues](#SP3Resolved)
* [v18.2 Service Pack 2 Feature Enhancements](#SP2Feature)
* [v18.2 Service Pack 2 Resolved Issues](#SP2Resolved)
* [v18.2 Service Pack 1 Resolved Issues](#SP1Resolved)
* [v18.2 Feature Enhancements](#Feature)
* [v18.2 Resolved Issues](#Resolved)
* [Known Issues](#Known)

## v18.2 Service Pack 3 Feature Enhancements

| Title | Description |
| --- | --- |
| Log4j Upgrade | Logi Report now replaces Log4j v2.17.0 with v2.17.1 to mitigate security vulnerabilities. |

## v18.2 Service Pack 3 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| DateTime Format Parameter from Stored Procedure | 85769 | Parameters from stored procedures can now apply the DateTime format "MM-dd-yyyy hh:mm:ss a" that you define in the connection. |

## v18.2 Service Pack 2 Feature Enhancements

| Title | Description |
| --- | --- |
| Log4j Upgrade | Logi Report replaces older Log4j implementations with Log4j v2.17.0 to mitigate the security vulnerabilities. |
| Server Sign On | Server administrators can now control the maximum number of times that users can attempt to consecutively sign on to Server before Server locks the account, and the amount of time the lock lasts, by setting the properties "Max Login Attempts Before Lockout" and "Account Lock Duration". See [Configuring Advanced Server Settings](https://devnet.logianalytics.com/hc/en-us/articles/4405683579799-Configuring-Advanced-Server-Settings). |

## v18.2 Service Pack 2 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| Access to Linked Report with Parameter | 85907 | You can now open linked reports with a parameter in Page Report Studio. |
| Enhanced Performance of Page Report Studio | 80963 | Page Report Studio now runs faster through business view resources visibility and accessibility enhancements. |
| Page Report with Formula | 86208 | You can now successfully run a report in Page Report Studio without displaying the NullPointerException error message, when the report uses IsNull functions in formulas. |
| Resource Reference Update for Dynamic Formulas | 86440 | Designer now correctly updates the dynamic formulas after you rename a catalog data source, if you have configured the reference table to monitor reference relationships of all resource types. |
| Table with Special Field as Group | 86541 | Web Report Studio now displays the top group values in a table inside a banded object, when the lower group in the table is a special field. |
| UDO Reports | 86390 | You can now run reports that contain User-Defined Objects (UDOs) successfully after upgrading to v18.2. |

## v18.2 Service Pack 1 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| None |  | No public facing changes in this update. |

## v18.2 Feature Enhancements

| Title | Description |
| --- | --- |
| [Built-in Formula Functions to Convert Locale-Sensitive Data](https://devnet.logianalytics.com/hc/en-us/articles/4411830858775-Logi-Report-v18-2-Enhancements#LocaleFunction) | You can now call a set of functions in your formulas to convert Currency, Number, Date, DateTime, and Time data to strings based on specified locales. See Appendix 1: Formula Functions in the *Logi Report Designer Guide*. |
| [Enhanced Autofit](https://devnet.logianalytics.com/hc/en-us/articles/4411830858775-Logi-Report-v18-2-Enhancements#ReduceWidth) | You can now use the Reduce Width When Autofit property to get an improved autofit display by reducing the width of an object, when the associated content is not as wide as the object. See:   * [Setting Web Report Object Properties Using the Inspector Panel](https://devnet.logianalytics.com/hc/en-us/articles/4411830859799-Setting-Web-Report-Object-Properties-Using-the-Inspector-Panel) * [Manipulating Data Components in Web Report](https://devnet.logianalytics.com/hc/en-us/articles/4405684043031-Manipulating-Data-Components-in-Web-Report) * [Manipulating Data Components in Page Report](https://devnet.logianalytics.com/hc/en-us/articles/4405683959319-Manipulating-Data-Components-in-Page-Report) |
| [Enhanced Designer UI](https://devnet.logianalytics.com/hc/en-us/articles/4411830858775-Logi-Report-v18-2-Enhancements#DesignerTheme) | Designer now applies a new color theme to the Start Page and main frame top banner, providing you with an enhanced and modern look. |
| Enhanced UX for JSON Connection | Designer improves the UX for specifying RESTful options when you set up a JSON connection via URI based on the "http://" or "https://" protocol. |
| Improved Map Style | Logi Report has modernized the style of the Geographic Map component, enhancing its look and feel. |
| [Locale Sensitive Data Formatting](https://devnet.logianalytics.com/hc/en-us/articles/4411830858775-Logi-Report-v18-2-Enhancements#FormatLocale) | You can now use the Format Locale property to display the appropriate values of data fields and special fields for a country or region. See:  * [Setting Web Report Object Properties Using the Inspector Panel](https://devnet.logianalytics.com/hc/en-us/articles/4411830859799-Setting-Web-Report-Object-Properties-Using-the-Inspector-Panel) * [Data Field Properties](https://devnet.logianalytics.com/hc/en-us/articles/4405683621271-Data-Field-Properties) * [Parameter Field Properties](https://devnet.logianalytics.com/hc/en-us/articles/4405690520215-Parameter-Field-Properties) * [Special Field Properties](https://devnet.logianalytics.com/hc/en-us/articles/4405683683991-Special-Field-Properties) |
| [Page Break in Excel Output](https://devnet.logianalytics.com/hc/en-us/articles/4411830858775-Logi-Report-v18-2-Enhancements#PageBreak) | You can now use the new properties No Page Break for Data Format and No Page Break for Report Format to remove the page breaks on each individual sheet in Excel output, when you export a report to Excel using Data Format and Report Format, in addition to Column Format. See the following links in the *Logi Report Designer Guide*:  * Page Report Tab Properties * Web Report Properties |
| Sorted Summary Table Columns in Exported Output | Sorted summary table columns using major sort now display in the schedule and exported outputs as they do in Web Report Studio. |
| [Support for Office 365 Email Server](https://devnet.logianalytics.com/hc/en-us/articles/4411830858775-Logi-Report-v18-2-Enhancements#Office365) | You can now use an Office 365 email server for scheduling to email and emailing system notifications for task notifications in Logi Report. |
| Support for OpenJDK 15 and 16 | Logi Report now supports OpenJDK 15 and 16, in addition to OpenJDK 8, 11, 12, 13, and 14. |
| Update of Integrated Server Property Values | You can now change the property values in server.properties in an integrated Logi Report after you upgrade to v18.2, by creating the install.server.properties file and adding properties in it. See [Upgrading Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/4405690621207-Upgrading-Logi-Report-Server#ChangeServerProperties). |

## v18.2 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| Access to Public Folders as Admin User | 80537 | You can now access any public folder when you are the admin user, without getting the Access Denied error message. |
| Access to Server Scheduled Page | 85222 | Server no longer displays the "'insertDataInIETable' is undefined" error message when you are accessing the Server Console > My Tasks > Scheduled page on IE 10. |
| Addition of Same NLS Keys | 79923 | Server now no longer clears the global NLS table content when you add the NLS keys "Country" and "Country " (Country with an added space at the end), if you are using MySQL as the system database. |
| All Values in Filter Control with NLS | 85030 | Server can now apply NLS to the "All" values in the filter controls successfully after you insert filter controls in web reports. |
| Business View Filter on Fields of Same Name | 80024 | Logi Report now fetches values for a business view filter correctly when you use fields with the same display name but in different categories in the filter. |
| Chart Conditional Color Fill in Excel Output | 79959 | Logi Report now applies the conditional color fill on a chart as you specified when you export or run the chart in Excel. |
| Chart Data After Upgrade | 79824 | Logi Report can now display data for the chart that you created using v14 or earlier which uses a record level pass two formula as the category or series field after you upgrade to a recent release. |
| Conditional Fill in Chart | 85252 | Web Report Studio can now work properly without displaying the Error in Adaptor error message, when you change the parameter value in a parameter control in a bar chart to a value which results in a null value of the chart value field, after you have set conditional color fill based on the chart value field. |
| Correct Date Conversion | 79898 | You can now use the *ToDate()* formula function to convert a string that is in the MM/dd/yyyy format to a correct date. |
| Crosstab Formula in Property | 79818 | You can now use crosstab formulas to control the Width property of the aggregate fields in a query-based crosstab. |
| Designer Connects with Server | 79755 | You can now connect Designer with Server via SSL, regardless of the certificate Server is using. |
| Duplicated Scheduled Tasks | 79035 | Server now no longer duplicates scheduled tasks and sends duplicated reports in the cluster environment. |
| Facility Printing in Syslog | 85098 | Server can now save changes through the UI and in the LogConfig.properties file, when you select Syslog and set Facility Printing to "True" on the Server Console > Administration > Configuration > Log page. |
| Field Display and Format in Email | 80552 | Server now displays fields with proper format, and displays complete fields when their position is static, in the HTML output as email content. |
| Folder Access When Publishing Resources | 80752 | Server now grants you correct access to folders based on your permissions, when you publish resources from Designer. |
| Font Size in PDF Output on Linux | 80207 | Logi Report now displays the same font size in the PDF output of your report using either Linux or Windows systems when you set the Convert HTML Tag property for objects in the report to "true". |
| Initial Parameters Values when Linking Reports | 79869 | Web Report Studio now displays the initial parameter values as expected, when you change the parameter values in a web report, select a link to open another web report, change the parameter values in this report, and then select a link to open the first report. |
| Non-bursting Result for Schedule | 80190 | You can now successfully schedule a bursting report to generate the Non-bursting Result, when the report contains a value longer than 255 characters. |
| NullPointerException | 85418 | Server no longer displays the NullPointerException error message in error.log when you call HttpUtil.initEnv(System.getProperties()), after you install Server silently with the "Live Disabled" license. |
| Open Linked Report in Page Report Studio | 79119 | Page Report Studio now displays the linked report properly with the report data, when both the primary report and the linked report use a multi-valued parameter whose value is "All". |
| Page Report Running with Customized Parameter | 80849 | Page Report Studio can now run page reports successfully (no longer displaying the A0FF0001 error message) when your customized parameter has the same name as a Logi Report parameter, and has a different value type. |
| PDF Output with Converted HTML Tag | 80207 | Logi Report can now generate correct PDF output for your report when the report contains a lot pages and you set the Convert HTML Tag property for objects in the report to "true". |
| Pie Chart with Conditional Color | 79889 | JDashboard now displays pie charts with the proper conditional color in library components. |
| Publish to FTP in CSV Format | 79984 | Server now properly generates output in .csv format instead of .txt format, when you schedule a report to publish to FTP in Text with CSV Format. |
| Quick Export to Excel with Data Format | 80100 | Page Report Studio now exports page reports to Excel with Data Format quickly. |
| Recipient Parameter in Bursting Report Schedule | 79988 | Server now displays the recipient parameter when you schedule a bursting report that uses a JSON file as the data source, and if the JSON file contains both the report data table and recipient table, and you use a parameter to refer the JSON file name. |
| Report Running After Upgrade | 79412 | You can now run reports successfully after upgrading from v14 Update 2 to v18, when your catalog contains a large number of formulas. |
| Schedule to Email | 80312 | Server can now successfully submit the scheduled task when you schedule a page report with "Export to One File" to email. |
| Schedule to Email | 80977 | Server can now work properly (without displaying the MailException error message), when you schedule a page report with multiple report tabs with "Export to One File" to email, when you set STARTTLS in the email server and select Server Requires a Secure Connection (STARTTLS) on the Logi Report Server Console > Administration > Configuration > E-mail Server page. |
| Sign in to Server from Designer | 80628 | You can now connect from Designer to Server without getting an error, when the encrypted string of your user name and password contains the "+" character. |
| Smaller Line Space for Fields | 80317 | Server now reduces line space in a field value in Page Report Studio and in the PDF output, to match what was happening in v16 Update 2. |
| UDF in XML Catalog | 79826 | Designer can now save the user-defined formula functions (UDF) in a catalog and display them in the Catalog Manager resource tree, when you save the catalog as a .cat.xml file. |
| Value List with Business View Security | 85163 | Web Report Studio no longer displays the denied values of fields (as you defined in the Business View Security), in the value lists in the Query Filter dialog. |
| Web Report with Parameter | 79716 | Web reports now run successfully on Server without displaying the invalid parameter value error message, when the parameter property Enable the "All Values" Option is "true". |

## Known Issues

**Report data gets cut off in PDF result due to PDF page size limitation**

When you export a report to PDF, you will find that in the PDF output, some data of the report are cut off if the report contains a large amount of data but its page mode was specified to be continuous page mode or its page size was set to be larger than 200 inches. This is due to a PDF limitation where the data displayed can be no larger than 200 inches in a single PDF page.

**Unsupported go-to action temporarily when using dynamic formulas on chart**

You will get exceptions when you perform the go-to action on a chart which uses a dynamic formula as its shown value and the formula contains group information. This is a limitation in the current version. It will be resolved in a future release.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4420461816983-Logi-Report-v18-3-Enhancements)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4411830858775-Logi-Report-v18-2-Enhancements)
