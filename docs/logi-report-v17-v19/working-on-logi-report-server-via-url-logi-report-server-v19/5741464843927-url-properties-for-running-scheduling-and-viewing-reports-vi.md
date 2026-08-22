---
title: "URL Properties for Running, Scheduling, and Viewing Reports via URL"
id: 5741464843927
section: "Working on Logi Report Server via URL Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741464843927-URL-Properties-for-Running-Scheduling-and-Viewing-Reports-via-URL
updated_at: 2022-10-31T17:18:38Z
---

# URL Properties for Running, Scheduling, and Viewing Reports via URL

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741471451159-Accessing-Visual-Analysis-via-URL)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741464180119-Web-Report-Studio-Server-v19)

# URL Properties for Running, Scheduling, and Viewing Reports via URL

This topic describes the basic URL properties you should consider when running, scheduling, and viewing reports, and adding and deleting users/roles/groups.

You need to specify the properties for each report format when you run or schedule reports via URL. For more information, see the Logi Report Javadoc.

This topic contains the following sections:

* [General URL Properties for Running and Scheduling Reports](#General)
* [URL Properties for Scheduling Reports](#Schedule)
* [URL Properties for Viewing Reports](#Result)
* [URL Properties for Adding and Deleting Users/Roles/Groups](#User)

## General URL Properties for Running and Scheduling Reports

| Property | Description |
| --- | --- |
| jrs.path | Specify a path or a resource name with full path. Example: /SampleReports, or /SampleReports/Payroll Report.cls |
| jrs.catalog | Specify the catalog name with full path. Example: /SampleReports/SampleReports.cat, or %2fSampleReports%2fSampleReports.cat |
| jrs.report | Specify the report name with full path. Example: /SampleReports/Employee Information List.cls, or %2fSampleReports%2fEmployee Information List.cls |
| When specifying the full path of a resource in the preceding three properties:  * If the resource is in the Public Reports folder in the server resource tree, you should start the path with "/". For example, for the /Public Report/SampleReports folder, provide the path as "/SampleReports". * If the resource is in the My Reports folder in the server resource tree, you should start the path with "/USERFOLDERPATH/*username*/" (change *username* to the real username with which you sign in to Logi Report Server). For example, suppose your username is Jim and you want to access the /My Reports/Shipments folder, provide the path in the URL as "/USERFOLDERPATH/Jim/Shipments". | |
| jrs.result\_type | Specify the format in which you want to run a report. Possible values:   * **1** - To HTML * **2** - To PDF * **3** - To TEXT * **4** - To Excel * **5** - To PostScript * **6** - To Rich Text Format * **7** - To XML * **8** - To Page Report Studio (for page reports) * **8** - To Web Report Studio (for web reports) |
| jrs.param$PARAMETER\_NAME | Specify the parameter values for running a report. Use **jrs.param$PARAMETER\_NAME=VALUE** to set parameter values of a report, where PARAMETER\_NAME is a parameter name and VALUE is a URL-encoded value of the parameter. For example, `jrs.param$TERMSDAYS=30&jrs.param$PTODAY=May 21, 1998`.  When specifying values for a multi-valued parameter, you need to add `_isMultiple_jrs.param$PARAMETER_NAME=true` before the parameter values, to declare that the parameter supports multiple values. For example: `&_isMultiple_jrs.param$PM=true&jrs.param$PM=3&jrs.param$PM=16`.  To apply all the values of a parameter, use `jrs.param$PARAMETER_NAME=%07`. See the example:  `http://localhost:8888/jinfonet/tryView.jsp?jrs.report=%2fSampleReports%2fShipment+Status+Report.wls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=8&jrs.param%24P_StartDate=2015-12-30&jrs.param%24p_EndDate=2017-1-1&jrs.param%24P_ShipperTerritory-Shipper+Territory=%07&jrs.param%24P_ShipperTerritory-Shipper+Name=%07&jrs.param_page=false` |
| jrs.param\_values | Specify the parameter values for running a report. This is the escaped string of the parameter values of the report. Format: PARAMETER\_NAME=VALUE,PARAMETER\_NAME=VALUE,...  Examples:   * jrs.param\_values=PTODAY%3dMay%2021%5c%2c%201998%2cTERMSDAYS%3d30 (original: PTODAY=May 21\, 1998,TERMSDAYS=30) * jrs.param\_values=STARTDATE%3d1998-05-10%2cENDDATE%3d1998-07-10 (original: STARTDATE=1998-05-10,ENDDATE=1998-07-10) |
| jrs.param\_page | Specify whether to show the parameter dialog box for specifying parameter values that you did not provide by **jrs.param$** in the URL. Such parameter dialog boxes include the one Server displays during report running and those brought by actions that lead to the change of parameters after the report renders in Page Report Studio, for example, the actions such as inserting a formula with a new parameter and running a master/detail report. However, this property does not affect the dialog box displayed via Menu > Report > Change Parameters, because the dialog box is to display all the parameters of the report. The default value of the property is true. When you provide the value of a middle level cascading parameter (including old style cascading parameter) in the URL, the parameter dialog box only shows the lower-level parameters.  When you set the property value to false, Server will not display the parameter dialog box during the whole report running. Server uses the parameter values you provided and the default values of the other parameters to run the report. |
| jrs.rpt\_language | Specify the language in which you want to generate the report. The value should be consistent with the language and country code part of the language property file name. For example, if the language property file name is ReportName\_de\_DE.properties, you should set this property as jrs.rpt\_language=de\_DE. You can also use jrs.rpt\_language=de&jrs.rpt\_country=DE to achieve the same goal. If you only want to use jrs.rpt\_language=de, you will have to rename the language property file to ReportName\_de.properties. Examples:   * `http://localhost:8888/jinfonet/tryView.jsp?jrs.report=%2fSampleReports%2fEmployee Information List.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=2&jrs.enable_nls=true&jrs.rpt_language=de_DE` * `http://localhost:8888/webos/app/pagestudio/run.jsp?jrs.catalog=/SampleReports/SampleReports.cat&jrs.report=/SampleReports/Employee Information List.cls&jrs.enable_nls=true&jrs.rpt_language=de&jrs.rpt_country=DE` * If you change Employee Information List\_de\_DE.properties to Employee Information List\_aaa.properties in Employee Information List.cls's real path folder, for example `C:\LogiReport\Server\history\1\JReport_System_User457188937`, then you can use the following URL to run NLS report: `http://localhost:8888/webos/app/pagestudio/run.jsp?jrs.catalog=/SampleReports/SampleReports.cat&jrs.report=/SampleReports/Employee Information List.cls&jrs.enable_nls=true&jrs.rpt_language=aaa` |
| jrs.rpt\_encoding | Specify the encoding in which you want to generate the output. |
| jrs.has\_style | Specify whether to enable the style group that you have set for the report. |
| jrs.style\_group | Specify the style group which could be StyleName<CSS> or StyleName.css. StyleName<CSS> is a CSS Style Sheet whose name is StyleName in the Logi Report resources system. It might come from a .css file on drive or be created from the CSS editor. StyleName.css is a \*.css file on drive which may not follow the CSS style rule and therefore not work. You should use jrs.style\_group=StyleName<CSS> in case StyleName.css fails, though both can work most of the time. |
| jrs.db\_user | Specify the new database user ID if you do not want to use the default DB user ID in the catalog. |
| jrs.db\_pswd | Specify the new database password if you do not want to use the default DB password in the catalog. |
| jrs.jdbc\_url | Specify the new JDBC URL in the catalog to run a report. |
| jrs.jdbc\_driver | Specify the new JDBC driver in the catalog to run a report. |
| jrs.wp | Specify the WHERE portion. For example, a report has the field Customer Region, and you want to restrict the field to CA in the URL. You can then set a new WHERE portion like `"...jrs.result_type=1&jrs.wp=Customers.Region='CA'...".` |
| jrs.named\_wp | Specify the named WHERE portion that exists in the catalog. |
| jrs.jdbc\_connection\_object | Specify a java.sql.Connection object to run a report dynamically. You can use this parameter in the three methods of jet.server.api.RptServer: *runReport()*, *runReportNotWaitResult()*, and *submitScheduledTask()*.  Example: Running a report with your JDBC connection object using the Logi Report Server API.     ``` //Create the java.sql.Connection object. java.sql.Connection myCon = java.sql.DriverManager.getConnection(dbUrl); //Set the parameter "jrs.jdbc_connection_object" to run a report. propParams.put("jrs.jdbc_connection_object", myCon); //Run the report using this java.sql.Connection object instead of //the default DB settings in the catalog. rptServer.runReport(userID, catalog, report set, propParams); ``` |
| jrs.security\_file\_name | Specify a [security file](https://devnet.logianalytics.com/hc/en-us/articles/5741483705367-Dynamic-Security). The security definitions in the security file will replace that in the specified catalog. |
| jrs.applet\_type | Specify the Java runtime environment to run applets. Possible values:   * **2** - Java Plug-In 1.2 for Windows * **3** - Java Plug-In 1.3 for Windows |
| jrs.web\_browser | Specify the web browser for which the HTML output adapts. Possible values:   * **0** - IE or Chrome * **1** - Firefox |
| jrs.timeout\_send\_email | Specify whether to notify someone of the task status via email if the task has not finished running when the task duration is up. Possible values: true/false. The task duration uses the time specified by **jrs.report\_timeout** in the URL. If there is not jrs.report\_timeout, Server uses the time specified by the **web.timeouts.report\_wait** property in the server.properties file in `<install_root>\bin`. |
| jrs.report\_timeout | Specify a time duration in seconds for a scheduled report running task. |
| jrs.mailto | Specify the address you want to send the email to. |
| jrs.mailsubject | Specify the subject of the email. |
| jrs.mailcomments | Specify the comments to the email contents. |
| jrs.mailfrom | Specify the email address of the sender. |
| jrs.timeout\_sendmail\_message | Specify the contents of the email. |
| CustomOffset | Add the property **CustomOffset=true** in the URL if you want the date and time values in your report to use the time zone that you have set on the values in the XML data source, instead of using the time zone of your server runtime environment.  In the case you do not add the property in the URL, which means that CustomOffset=false, if you do not provide a specific time zone in the URL or session, the server runtime time zone is the time zone setting you defined on the Server Console > My Profile.  Note icon   * The calculation of grouping and filtering on data of the Date/Time/DateTime type is always based on the runtime time zone, as the unified standard, regardless of the value-level time zone that you set in the XML data source. * When CustomOffset=true, the values of parameters of the Date/Time/DateTime type always use the runtime time zone, regardless of the value-level time zone that you set in the XML data source. |
| This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.FunctionApplyOffset | By default, Server applies the time zone you set in server preferences to Date/Time/DateTime field values in built-in functions. If you want to retain the time zone of the field values in built-in functions, run reports via URL and add "[CustomOffset=true](#CustomOffset)&FunctionApplyOffset=true" in the URL. |
| Excel format properties | |
| jrs.result\_type=4 | It means to export to Excel. Example: `http://localhost:8888/jinfonet/tryView.jsp?jrs.cmd=jrs.try_vw&jrs.report=%2fSampleReports%2fPayroll%20Report.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=4&jrs.excel_format=0&jrs.excel_format_types=1` |
| jrs.excel\_extension | Specify whether to use custom file extension. |
| jrs.excel\_format | Specify the Excel version. Possible values:   * **0** - The Excel output file uses the .xlsx format. * **1** - The Excel output file uses the .xls format. |
| jrs.excel\_format\_types | Specify the format of the Excel output. Possible values:   * **0** - It means Auto Format, and Server defines the format according to the objects in the report. Server uses Column Format when the report contains crosstabs or tables, or else Report Format. * **1** - It means Report Format and uses the format as you designed in the template, for the report in Excel. Use this format if you just want to view the report in Excel. * **2** - It means Column Format and calculates all components' row/column values in the report using the Columned property value of the report when exporting. Use this format if you want to actively use the report in Excel such as filtering and sorting. * **3** - It means Data Format and only generates the report data without any format. This value is only available when jrs.excel\_format=1. |
| jrs.has\_shapes | Specify whether to include the drawing objects in the Excel output, such as lines, ovals, and boxes. |
| jrs.print\_header | Specify the page header text for the printed file. |
| jrs.print\_footer | Specify the page footer text for the printed file. |
| jrs.is\_wordwrap | Specify the word-wrap settings. Possible values:  * **0** - It means All Keep Existing and keeps all the settings of each object's Word Wrap property originally specified in the report. * **1** - It means All Disabled and disables the Word Wrap property for all objects. That is, the Word Wrap property is false for all objects. * **2** - It means All Enabled and enables the Word Wrap property for all objects. That is, the Word Wrap property is true for all objects. |
| jrs.print\_gridlines | Specify whether to include gridlines when printing the Excel output. |
| jrs.to\_excel\_runLinkedReport | Specify whether to generate the linked reports (excluding the detail reports) in the output when the report is linked with other reports. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data. |
| Text format properties | |
| jrs.delimiter | Specify a delimiter other than comma, for example,  * jrs.delimiter=%23(#) * jrs.delimiter=~ * jrs.delimiter=/ |
| jrs.is\_text\_delimiter=jrs.is\_csv | To use the CSV format, set these properties: jrs.result\_type=3&jrs.is\_text\_delimiter=jrs.is\_csv&jrs.is\_norm\_txt=false. |
| jrs.is\_quotemark=true | Specify whether to use quote marks in the text output. Possible values: true/false. |
| jrs.udchar\_width | Specify an integer value for each unit of the horizontal density between columns. The resulting density is a direct ratio of the value you specify. That is, the greater the value, the smaller the width between columns. By default, Logi Report defines the density. |
| jrs.udchar\_height | Specify an integer value for each unit of the vertical density between columns. The resulting density is a direct ratio of the value you specify. That is, the greater the value, the smaller the height between columns. By default, Logi Report defines the density. |
| jrs.txt\_compress | Specify whether to generate the output in Text in a compressed size. Possible values: true/false. If true, there will be no clearance between the columns. |
| jrs.hasHeadFoot | Set this property to true if you want the Text file to contain all headers and footers in the report, including Report Header/Footer, Page Header/Footer, and Group Header/Footer. Otherwise, set it to false, and the Text file will only contain the data in the Detail panel. |
| jrs.txt\_windows | Set this property to true if you want to use Windows end-of-line characters to indicate the start of a new line. Logi Report will use two characters <cr> and <lf> at the end of the line. Or, set it to false if you want to use UNIX End-of-line characters to indicate the start of a new line. Logi Report will only use the UNIX End-of-line character <lf>. |
| jrs.result\_file\_name | Set the output file name, for instance, `jrs.result_file_name=test.txt`. |
| jrs.to\_text\_runLinkedReport | Specify whether to generate the linked reports (excluding the detail reports) in the output when the report is linked with other reports. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data. |

## URL Properties for Scheduling Reports

| Property | Description |
| --- | --- |
| General properties | |
| jrs.task\_class | Specify the class name of the task. Possible values:   * jet.server.schedule.jrtasks.UpdateRptTask * jet.server.schedule.jrtasks.PublishToDiskTask * jet.server.schedule.jrtasks.SendJRMailTask * jet.server.schedule.jrtasks.SendMailTask * jet.server.schedule.jrtasks.PrintRptTask |
| jrs.has\_task\_listener | Specify whether to implement TaskListener. |
| jrs.task\_listener\_class | Specify a Java class name which implements the TaskListener (jrs.task\_listener\_class). |
| jrs.task\_id | Specify the task ID of a scheduled task. This property is unnecessary if you are submitting a new schedule. |
| jrs.mail\_to\_referuser | Specify whether to send email to each user who can view a report with cached report bursting. |
| jrs.is\_bursting\_task | Indicate that you are scheduling a bursting report task. |
| jrs.bursting\_schema$Schema\_Name | Specify the names of the schemes you want to schedule. |
| Publishing to the versioning system properties | |
| jrs.to\_version | Specify whether to publish the output to the versioning system. |
| jrs.to\_version\_rst | Specify whether to publish a page report to a Logi Report result file (RST file) or publish a web report to a static web report result file (WST file). You can further specify the result properties. For more information, see the Logi Report Javadoc. |
| jrs.to\_version\_rsd | Specify whether to publish the output to a page report result file (RSD file). You can further specify the result properties. For more information, see the Logi Report Javadoc. |
| jrs.to\_version\_html | Specify whether to publish the output to the versioning system in HTML. You can further specify the HTML properties. For more information, see the Logi Report Javadoc. |
| jrs.to\_version\_pdf | Specify whether to publish the output to the versioning system in PDF. You can further specify the PDF properties. For more information, see the Logi Report Javadoc. |
| jrs.to\_version\_excel | Specify whether to publish the output to the versioning system in Excel. You can further specify the Excel properties. For more information, see the Logi Report Javadoc. |
| jrs.to\_version\_txt | Specify whether to publish the output to the versioning system in Text. You can further specify the Text properties. For more information, see the Logi Report Javadoc. |
| jrs.to\_version\_rtf | Specify whether to publish the output to the versioning system in RTF. You can further specify the RTF properties. For more information, see the Logi Report Javadoc. |
| jrs.to\_version\_xml | Specify whether to publish the output to the versioning system in XML. You can further specify the XML properties. For more information, see the Logi Report Javadoc. |
| jrs.to\_version\_ps | Specify whether to publish the output to the versioning system in PostScript. You can further specify the PostScript properties. For more information, see the Logi Report Javadoc. |
| jrs.archive\_location | Specify the location where you want to save the report. Possible values:   * **0** - Save the report to the built-in version folder. Not supported for [organization users](https://devnet.logianalytics.com/hc/en-us/articles/5741463905047-Multitenancy-Supported-via-Organizations) when the report is from the Public Reports folder. * **1** - Save the report to the My Reports folder. You can then use **jrs.archive\_my\_destination** to specify a report version name with the path in the My Reports folder. * **2** - Save the report to the Public Reports folder. You can then use **jrs.archive\_public\_destination** to specify a report version name with the path in the Public Reports folder. Not supported for organization users. |
| jrs.enable\_archive\_policy | Specify whether to apply an archive policy to the saved report. |
| jrs.archive\_new\_version | Specify how to archive the new version. Possible values:   * **true** - Use multiple versions for the report. You can then use **jrs.maxversion** to specify the maximum number of versions in the version table of the report. 0 means unlimited number. * **false** - Replace the old version with the new version. |
| jrs.need\_expire | Specify whether you want the saved report to expire. |
| jrs.auto\_delete\_method | Specify when you want the saved report to expire and to delete it. If the time you specify exceeds one hundred years, Server will keep the report forever. Possible values:   * **0** - Server automatically deletes the report after a specified number of days. You can then use **jrs.expire\_days** to specify the number of days, for example: `jrs.need_expire=true&jrs.auto_delete_method=0&jrs.expire_days=60`. * **1** - Server automatically deletes the report after a specified date. You can then use jrs.auto\_delete\_year, jrs.auto\_delete\_month, and jrs.auto\_delete\_date to specify the year, month, and date, for example: `jrs.need_expire=true&jrs.auto_delete_method=1&jrs.auto_delete_year=2017&jrs.auto_delete_month=5&jrs.auto_delete_date=16`. |
| jrs.expire\_days | Specify the number of days Server keeps a report version until it expires. The default value is 30. |
| Publishing to the file system properties | |
| jrs.to\_disk | Specify whether you want to publish the report to disk. |
| jrs.to\_rst | Specify whether to publish a page report to a Logi Report result file (RST file) or publish a web report to a static web report result file (WST file). You can further specify the result properties. For more information, see the Logi Report Javadoc. |
| jrs.to\_rsd | Specify whether to publish the output to page report result file (RSD file). You can further specify the result properties. For more information, see the Logi Report Javadoc. |
| jrs.to\_html | Specify whether to publish the output to the file system in HTML. You can further specify the HTML properties. For more information, see the Logi Report Javadoc. |
| jrs.to\_pdf | Specify whether to publish the output to the file system in PDF. You can further specify the PDF properties. For more information, see the Logi Report Javadoc. |
| jrs.to\_excel | Specify whether to publish the output to the file system in Excel. You can further specify the Excel properties. For more information, see the Logi Report Javadoc. |
| jrs.to\_text | Specify whether to publish the output to the file system in Text. You can further specify the Text properties. For more information, see the Logi Report Javadoc. |
| jrs.to\_rtf | Specify whether to publish the output to the file system in RTF. You can further specify the RTF properties. For more information, see the Logi Report Javadoc. |
| jrs.to\_xml | Specify whether to publish the output to the file system in XML. You can further specify the XML properties. For more information, see the Logi Report Javadoc. |
| jrs.to\_ps | Specify whether to publish the output to the file system in PostScript. You can further specify the PostScript properties. For more information, see the Logi Report Javadoc. |
| jrs.to\_disk\_xxx\_path\_type | Specify where to publish the output in the xxx format: to the server resource tree or to the server disk path. Possible values:   * **0** - Publish to the Logi Report Server resource tree. * **1** - Publish to a drive path. |
| jrs.xxx\_dir | Specify the path for the xxx format output. |
| jrs.xxx | Specify the file name for the xxx format output. |
| Publishing to email properties | |
| jrs.jrmail + NUMBER | Contain specifications (Logi Report email properties) of one email task for a report. |
| jrs.csmail + NUMBER | Contain specifications (Logi Report email properties) of one email task for sending an email with or without an attachment. You can use this property via URL or via invoking the Server API. |
| jrs.mailto | Specify the email address you want to send the email to. |
| jrs.mailcc | Specify the email address you want to send a copy of the email to. |
| jrs.mailbcc | Specify the email address you want to secretly send a copy of the email to. |
| jrs.mailsubject | Specify the subject of the email. |
| jrs.mailcomments | Specify the comments of the email. |
| jrs.mailformat | Specify the email format. Possible values:   * **0** - E-mail Result in HTML E-mail Format * **1** - E-mail Result in Plain Text E-mail Format * **2** - Attachment in HTML Format * **3** - Attachment in PDF Format * **4** - Attachment in Logi Report Result Format (for page reports) * **4** - Attachment in Web Report Result Format (for web reports) * **6** - Attachment in PostScript Format * **7** - Attachment in Excel Format * **8** - Attachment in RTF Format * **9** - Attachment in XML Format * **11** - Attachment in Text Format   When sending the report as an attachment file, you need to specify a file name using jrs.mailattach + NUMBER. You can further specify format properties for the attachment file. For more information, see the Logi Report Javadoc. |
| jrs.mailcompress | Specify whether to enable Java archive compress. |
| jrs.mailattach + NUMBER | Specify the attached file for the email. You can attach multiple files to one email. Possible values: The attached file name. |
| jrs.mailencoding | Specify the encoding of the email. Possible values: such as UTF-8, UTF-16, and ISO8859-1.  Note icon You can use **jrs.mailencoding** to specify the email encoding in the URL. When sending emails by RMI API, sometimes, Server might return wrong characters in the email. To avoid such problems, specify the same correct value of **-Djreport.url.encoding** on both the server and RMI client side.  For example, your web application calls Logi Report Server (standalone) via the RMI function from WebSphere, and you want to use UTF-8 (rather than UTF8) as the email encoding, do as follows:   * Specify `-Djreport.url.encoding=UTF-8` for both JVM running Logi Report Server and WebSphere. * Specify `jrs.mailencoding=UTF-8`. |
| E-mail Result in HTML E-mail Format | |
| jrs.to\_mail\_htmlmail | Specify whether to send the report in the HTML format in the email body. If true, the report will overwrite the comments that you specify for the email. |
| jrs.to\_mail\_htmlmail\_runLinkedReport | Specify whether to generate the linked reports (excluding the detail reports) in the output when the report is linked with other reports. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data. If you are only interested in the primary report, do not set this property. |
| E-mail Result in Plain Text E-mail Format | |
| jrs.to\_mail\_textmail | Specify whether to send the report in the plain [text](https://devnet.logianalytics.com/hc/en-us/articles/5741420507799-Advanced-Run-Dialog-Box-Properties#Text) format in the email body, with no other information such as color and images. Note icon**jrs.to\_mail\_textmail** and **jrs.to\_mail\_htmlmail** cannot work concurrently. |
| jrs.plaintext\_mail\_char\_width | Specify an integer value for each unit of the horizontal density between the columns. The resulting density is a direct ratio of the value you specify. That is, the greater the value, the smaller the width between the columns. By default, Logi Report defines the density. |
| jrs.plaintext\_mail\_char\_height | Specify an integer value for each unit of the vertical density between the columns. The resulting density is a direct ratio of the value you specify. That is, the greater the value, the smaller the height between the columns. By default, Logi Report defines the density. |
| jrs.plaintext\_mail\_txt\_compress | Specify whether to generate the report to Text in a compressed size. There will be no clearance between the columns. |
| jrs.plaintext\_mail\_hasheadfoot | Specify whether you want the Text output to contain all headers and footers in the report, including Report Header/Footer, Page Header/Footer, and Group Header/Footer. Otherwise, the Text output will only contain the data in the Detail panel. |
| jrs.plaintext\_mail\_txt\_windows=true | Specify to use Windows end-of-line characters to indicate the start of a new line. Logi Report will use two characters <cr> and <lf> at the end of the line. |
| jrs.plaintext\_mail\_txt\_windows=false | Specify to use UNIX End-of-line characters to indicate the start of a new line. Logi Report will only use the UNIX character <lf> at the end of the line. |
| jrs.to\_mail\_textmail\_runLinkedReport | Specify whether to generate the linked reports (excluding the detail reports) in the output when the report is linked with other reports. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data. If you are only interested in the primary report, do not set this property. |
| Attachment in Logi Report Result Format or **Web Report Result Format** | |
| jrs.to\_mail\_rst | Specify whether to send the report in a [Logi Report Result](https://devnet.logianalytics.com/hc/en-us/articles/5741433620631-Schedule-Dialog-Box-Properties#RST) file or [Web Report Result](https://devnet.logianalytics.com/hc/en-us/articles/5741433620631-Schedule-Dialog-Box-Properties#WST) file as the email attachment. Do not set this property when the schedule task contains both page reports and web reports. |
| jrs.mail\_rst\_file | Specify the name of the Logi Report result file. |
| jrs.mail\_zip\_result | Specify whether to compress the report to reduce the disk size and I/O; however, it uses more CPU resources. |
| jrs.mail\_rst\_precision | Specify the precision level with which you want to publish the report: Low or High. Note icon Changing the default value may cause abnormalities in report layout. |
| jrs.to\_mail\_rst\_runLinkedReport | Specify whether to generate the linked reports (excluding the detail reports) in the output when the report is linked with other reports. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data. If you are only interested in the primary report, do not set this property. |
| Attachment in HTML Format | |
| jrs.to\_mail\_html | Specify whether to send the report in an [HTML](https://devnet.logianalytics.com/hc/en-us/articles/5741420507799-Advanced-Run-Dialog-Box-Properties#HTML) file as the email attachment. |
| jrs.mail\_html\_file | Specify the name of the HTML file. |
| jrs.mail\_no\_margin\_html | Specify whether to remove the margins you originally set while designing the report. |
| jrs.mail\_is\_multi\_files | Specify whether to generate the report to multiple HTML files. Server designates a serial number for each HTML page. For example, if you name a 3-page report as "sales", Server will create three files called sales\_1.html, sales\_2.html, and sales\_3.html. |
| jrs.mail\_embedded\_css | Specify whether to embed the cascading style sheet (CSS) in the HTML files; otherwise, Server generates the .css file individually. |
| jrs.mail\_has\_hyperlink\_pref | Specify whether to display hyperlinks for navigating previous and next pages on the navigation bar of the HTML output. |
| jrs.mail\_has\_page\_number | Specify whether to display the current page number and the total page number on the navigation bar of the HTML output. |
| jrs.mail\_drilldown | Specify whether to enable the Drilldown feature in the HTML output so that you can inspect certain items for further detailed data. |
| jrs.mail\_use\_section508\_output | Specify whether to add the accessibility attributes you defined for the report elements via the Designer Report Inspector to the HTML output, which is Section 508 compliant including HTML data table, accessible attributes, and relative font feature . For more information, see [Making HTML and PDF Report Results and Server Console Accessible](https://devnet.logianalytics.com/hc/en-us/articles/5741473969431-Making-HTML-and-PDF-Report-Outputs-and-Server-Console-Accessible). |
| jrs.mail\_use\_html\_table | Specify whether to output the table and crosstab components to table objects in the HTML output. |
| jrs.mail\_relative\_font\_size=false | Specify to generate the report using the fixed font size that you cannot adjust according to the font size settings in the web browser. |
| jrs.mail\_relative\_font\_size=true | Specify to generate the report using a relative font size that you can adjust according to the font size settings in the web browser. |
| jrs.mail\_format\_chart | Specify the image type with which you want to display charts: GIF, JPEG, PNG, or Auto-select (Server will automatically detect the image format: GIF if the image colors are less than 256 colors or else JPEG). |
| jrs.mail\_html\_resolution | Resolution of the report to zoom in/out, in DPI. Server obtains the default value from the operation system, which is the resolution of your monitor, for example, 72 DPI on UNIX or 96 on Windows. You can set a higher/lower value to zoom in/out. |
| jrs.mail\_web\_browser | Specify IE or Firefox as the web browser for which the HTML output adapts. |
| jrs.mail\_text\_overflow | Specify whether to make the text overflow is visible or hidden. |
| jrs.to\_mail\_html\_runLinkedReport | Specify whether to generate the linked reports (excluding the detail reports) in the output when the report is linked with other reports. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data. If you are only interested in the primary report, do not set this property. |
| Attachment in PDF Format | |
| jrs.to\_mail\_pdf | Specify whether to send the report in a [PDF](https://devnet.logianalytics.com/hc/en-us/articles/5741420507799-Advanced-Run-Dialog-Box-Properties#PDF) file as the email attachment. |
| jrs.mail\_pdf\_file | Specify the name of the PDF file. |
| jrs.mail\_no\_margin\_pdf | Specify whether to remove the margins you originally set while designing the report. |
| jrs.compress\_chk\_pdf\_mail | Specify the percentage to compress the images in the report. |
| jrs.mail\_print\_mode\_pdf=true | Specify to take the whole report as a graphic to transform the report by the method of simulated printer. |
| jrs.mail\_print\_mode\_pdf=false | Specify to take the whole report as a dataset to transform the report by sequence. |
| jrs.mail\_toc\_pdf | Specify whether to generate a Table of Contents in the PDF output. Not supported for web reports. |
| jrs.mail\_drilldown\_pdf | Specify whether to enable the Drilldown feature in the HTML output so that you can inspect certain items for further detailed data. |
| jrs.mail\_pdf\_encrypt | Specify whether to encrypt the PDF output. |
| jrs.mail\_pdf\_sign | Specify whether to add the digital sign to the PDF output. |
| jrs.to\_mail\_pdf\_runLinkedReport | Specify whether to generate the linked reports (excluding the detail reports) in the output when the report is linked with other reports. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data. If you are only interested in the primary report, do not set this property. |
| jrs.mail\_accessible\_pdf | Specify whether to generate the report as an accessible PDF file. For more information, select [Making HTML and PDF Report Outputs and Server Console Accessible](https://devnet.logianalytics.com/hc/en-us/articles/5741473969431-Making-HTML-and-PDF-Report-Outputs-and-Server-Console-Accessible). |
| mail\_pdf\_zoom | Specify the percentage by which you want to zoom the report contents in the PDF output. A valid percentage is greater than 0 and no larger than 6400%. |
| Attachment in Excel Format | |
| jrs.to\_mail\_excel | Specify whether to send the report in an [Excel](https://devnet.logianalytics.com/hc/en-us/articles/5741420507799-Advanced-Run-Dialog-Box-Properties#Excel) file as the email attachment. |
| jrs.mail\_excel\_file | Specify the name of the Excel file. |
| jrs.mail\_excel\_format | Specify the Excel version:   * **Excel 97-2003 Workbook (\*.xls)**  Specify to run the file in the .xls format. * **Excel Workbook (\*.xlsx)**  Specify to run the file in the .xlsx format. |
| jrs.mail\_excel\_format\_types | Specify the format of the Excel output.   * **Auto Format**  Specify to define the format according to the objects in the report. Server uses Column Format when the report contains crosstabs or tables, or else Report Format. * **Report Format** Specify to use the format as you designed in the template, for the report in Excel. Use this format if you just want to view the report in Excel. * **Column Format**  Specify to calculate all components' row/column values in the report using the Columned property value of the report when exporting. Use this format if you want to actively use the report in Excel such as filtering and sorting. * **Data Format**   Specify to only generate the report data without any format. **Data Format** is only available for the Excel version of Excel 97-2003 Workbook (\*.xls). |
| jrs.mail\_has\_shapes | Specify whether to include the drawing objects in the Excel output, such as lines, ovals, and boxes. |
| jrs.mail\_print\_header | Specify the page header text for the printed file. |
| jrs.mail\_print\_footer | Specify the page footer text for the printed file. |
| jrs.mail\_excel\_wordwrap | Specify the word-wrap settings:  * **All Keep Existing** Specify to keep all the settings of each object's Word Wrap property originally specified in the report. * **All Disabled**  Specify to disable the Word Wrap property for all objects. That is, the Word Wrap property is false for all objects. * **All Enabled**  Specify to enable the Word Wrap property for all objects. That is, the Word Wrap property is true for all objects. |
| jrs.mail\_print\_gridlines | Specify whether to include gridlines when printing the Excel output. |
| jrs.to\_mail\_excel\_runLinkedReport | Specify whether to generate the linked reports (excluding the detail reports) in the output when the report is linked with other reports. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data. If you are only interested in the primary report, do not set this property. |
| Attachment in Text Format | |
| jrs.to\_mail\_txt | Specify whether to send the report in a [Text](https://devnet.logianalytics.com/hc/en-us/articles/5741420507799-Advanced-Run-Dialog-Box-Properties#Text) file as the email attachment. |
| jrs.mail\_text\_file | Specify the name of the Text file. |
| jrs.mail\_is\_normal\_text | Specify whether to generate the report to a standard text file, using a delimiter to separate fields. |
| jrs.mail\_char\_width | Specify an integer value for each unit of the horizontal density between the columns. The resulting density is a direct ratio of the value you specify. That is, the greater the value, the smaller the width between the columns. |
| jrs.mail\_char\_height | Specify an integer value for each unit of the vertical density between the columns. The resulting density is a direct ratio of the value you specify. That is, the greater the value, the smaller the height between the columns. |
| jrs.mail\_text\_is\_delimiter | Specify the delimiter to separate fields.   * **CSV Format**   Specify to use a comma to separate fields. * **Tab Delimited**  Specify to use a Tab delimiter to separate fields. * **Custom Delimiter**  Specify to separate fields by a user defined delimiter. Then, specify your own delimiter using jrs.mail\_delimiter. |
| jrs.mail\_delimiter | Specify your own delimiter. |
| jrs.mail\_is\_quotemark | Specify whether to use quote marks in the Text output. |
| jrs.mail\_repeat | Specify whether you want a cell that has no value in the Text output to use the value of the previous cell in the same column. |
| jrs.mail\_is\_text\_TrimBlankSpaces | Specify whether you want to remove the blank spaces at the beginning and end of field values, instead of keeping them. |
| jrs.mail\_txt\_compress | Specify whether to generate the report to Text in a compressed size. There will be no clearance between the columns. |
| jrs.mail\_hasheadfoot | Specify whether you want the Text output to contain all headers and footers in the report, including Report Header/Footer, Page Header/Footer, and Group Header/Footer. Otherwise, the Text output will only contain the data in the Detail panel. |
| jrs.mail\_txt\_windows=true | Specify to use Windows end-of-line characters to indicate the start of a new line. Logi Report will use two characters <cr> and <lf> at the end of the line. |
| jrs.mail\_txt\_windows=fase | Specify to use UNIX End-of-line characters to indicate the start of a new line. Logi Report will only use the UNIX character <lf> at the end of the line. |
| jrs.to\_mail\_txt\_runLinkedReport | Specify whether to generate the linked reports (excluding the detail reports) in the output when the report is linked with other reports. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data. If you are only interested in the primary report, do not set this property. |
| jrs.mail\_text\_file\_suffix | Specify the suffix of the attached Text file, which can be .txt or .dat. |
| Attachment in RTF Format | |
| jrs.to\_mail\_rtf | Specify whether to send the report in an [RTF](https://devnet.logianalytics.com/hc/en-us/articles/5741420507799-Advanced-Run-Dialog-Box-Properties#RTF) file as the email attachment. |
| jrs.mail\_rtf\_file | Specify the name of the RTF file. |
| jrs.mail\_best\_editing\_rtf | Specify whether to apply flow layout to the RTF output. |
| jrs.mail\_no\_margin\_rtf | Specify whether to remove the margins you originally set while designing the report. |
| jrs.to\_mail\_rtf\_runLinkedReport | Specify whether to generate the linked reports (excluding the detail reports) in the output when the report is linked with other reports. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data. If you are only interested in the primary report, do not set this property. |
| Attachment in XML Format | |
| jrs.to\_mail\_xml | Specify whether to send the report in an [XML](https://devnet.logianalytics.com/hc/en-us/articles/5741420507799-Advanced-Run-Dialog-Box-Properties#XML) file as the email attachment. |
| jrs.mail\_xml\_file | Specify the name of the XML file. |
| jrs.mail\_is\_only\_data | Specify whether you want to only contain the database column information in the generated XML file and to only contain the structure information of the report in the generated XML schema file. |
| jrs.mail\_xsdfile | Specify the path of an existing XML schema file (.xsd). Server generates the XML file based on it. Otherwise, Server generates a new XML schema file to the folder where the XML file is. The new XML schema file and the XML file will have the same name but with different extensions. |
| jrs.to\_mail\_xml\_runLinkedReport | Specify whether to generate the linked reports (excluding the detail reports) in the output when the report is linked with other reports. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data. If you are only interested in the primary report, do not set this property. |
| Attachment in PostScript Format | |
| jrs.to\_mail\_ps | Specify whether to send the report in a [PostScript](https://devnet.logianalytics.com/hc/en-us/articles/5741420507799-Advanced-Run-Dialog-Box-Properties#PS) file as the email attachment. |
| jrs.mail\_ps\_file | Specify the name of the PostScript file. |
| jrs.mail\_no\_margin\_ps | Specify whether to remove the margins you originally set while designing the report. |
| jrs.to\_mail\_ps\_runLinkedReport | Specify whether to generate the linked reports (excluding the detail reports) in the output when the report is linked with other reports. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data. If you are only interested in the primary report, do not set this property. |
| Publishing to a printer properties | |
| jrs.if\_print | Specify whether to print the output. |
| jrs.printer | Specify the printer with which you want to print the output. |
| jrs.print\_copies | Specify the number of copies you want to print the output. |
| jrs.print\_mediatray | Specify the custom tray you want to put the printing paper. |
| jrs.has\_margins | Specify whether you want the printed output to have margins. |
| When jrs.has\_margins=true, you must set the following properties: | |
| jrs.margins\_left | Specify the length of the left margin in the printed output. |
| jrs.margins\_right | Specify the length of the right margin in the printed output. |
| jrs.margins\_top | Specify the length of the top margin in the printed output. |
| jrs.margins\_bottom | Specify the length of the bottom margin in the printed output. |
| jrs.margins\_unit | Specify the margin unit.  Possible values:   * **jrs.margins\_unit\_mm** - Use mm as the margin unit. * **jrs.margins\_unit\_inch** - Use inch as the margin unit. |
| Publishing to fax properties | |
| jrs.to\_fax | Specify whether to publish the output to fax. |
| jrs.to\_fax\_quality | Specify the fax quality.  Possible values:   * **jrs.to\_fax\_quality\_best** - Best fax quality. * **jrs.to\_fax\_quality\_fast** - Fast fax quality. * **jrs.to\_fax\_quality\_normal** - Normal fax quality. |
| jrs.to\_fax\_is\_inclue\_cover | Specify whether to send a cover sheet with the fax. |
| jrs.to\_fax\_date | Specify the date on which you want to send the fax. |
| jrs.to\_fax\_to | Specify the fax recipient. |
| jrs.to\_fax\_to\_fax\_num | Specify the fax number of the recipient. |
| jrs.to\_fax\_from | Specify the fax sender. |
| jrs.to\_fax\_from\_company\_name | Specify the sender's company. |
| jrs.to\_fax\_from\_phone | Specify the sender's phone number. |
| jrs.to\_fax\_subject | Specify the subject of the fax. |
| jrs.to\_fax\_comments | Specify the comments of the fax. |
| jrs.to\_fax\_urgent | Specify whether the fax is urgent. |
| jrs.to\_fax\_for\_review | Specify whether the fax is for review. |
| jrs.to\_fax\_please\_comment | Specify whether you want the recipient to comment on the contents of the fax. |
| jrs.to\_fax\_please\_reply | Specify whether you want a reply for the fax. |
| Publishing to FTP properties | |
| jrs.to\_FTP | Specify whether to publish the output to FTP. |
| jrs.ftp | Specify an FTP site by holding the FTP setting properties. To configure multiple FTP sites, use jrs.ftp0 to specify the first site and jrs.ftp1 to specify the second, and so on. Separate multiple sites by &. Example: `jrs.ftp0=jrs.ftpHost%3D192.0.0.1%26jrs.ftpPort%3D21...&jrs.ftp1=jrs.ftpHost%3D192.0.0.2%26jrs.ftpPort%3D22...` (%3D represents "=" and %26 represents "&".) |
| jrs.ftpLbl | Specify the label of the FTP server. |
| jrs.ftpHost | Specify the host of the FTP server. |
| jrs.ftpPort | Specify the port of the FTP server. |
| jrs.ftpUn | Specify the username for signing in to the FTP server. |
| jrs.ftpPsd | Specify the password for signing in to the FTP server. |
| jrs.ftpAcct | Specify the account for signing in to the FTP server. |
| jrs.ftpLoc | Specify the remote directory on the FTP server to which you want to publish the files. |
| jrs.ftpHdlCls | Specify the FTP client-end handler class for communicating with the FTP server. Possible values: FTPHandler class name or null which is the default value. |
| jrs.ftpProt | Specify the protocol for communicating with the FTP server. Possible values:   * **0** - FTP * **1** - SFTP * **2** - SCP * **3** - FTPS |
| jrs.ftpsConType | Specify the connection type of FTPS. Possible values:   * **0** - EXPLICIT * **1** - IMPLICIT |
| jrs.ftpsEnNoSec | Specify whether to enable falling back to the no-security FTP connection if the explicit FTPS connection is not available. |
| jrs.ftpsKSType | Specify the keystore type of FTPS. |
| jrs.ftpsKSFile | Specify the keystore file of FTPS. |
| jrs.ftpsKSPsd | Specify the keystore password of FTPS. |
| jrs.ftpsKMAlg | Specify the keymanager algorithm of FTPS. |
| jrs.ftpsSecProt | Specify the security protocol of FTPS. |
| jrs.ftpsTMAlg | Specify the trustmanager algorithm of FTPS. |
| jrs.ftpsTransMode | Specify the transfer mode of FTPS. |
| jrs.ftpsTSType | Specify the truststore type of FTPS. |
| jrs.ftpsTSFile | Specify the truststore file name of FTPS. |
| jrs.ftpsTSPsd | Specify the truststore password of FTPS. |
| jrs.sftpC2SCmpA | Specify the C2S compression algorithms of SFTP/SCP. |
| jrs.sftpC2SCphA | Specify the C2S cipher algorithms of SFTP/SCP. |
| jrs.sftpC2SLang | Specify the C2S language of SFTP/SCP. |
| jrs.sftpC2SMA | Specify the C2S MAC algorithms of SFTP/SCP. |
| jrs.sftpHKAlgs | Specify the host key algorithms of SFTP/SCP. |
| jrs.sftpKexAlgs | Specify the kex algorithms of SFTP/SCP. |
| jrs.sftpKH | Specify the knownhosts file of SFTP/SCP. |
| jrs.sftpS2CCmpA | Specify the s2c compression algorithms of SFTP/SCP. |
| jrs.sftpS2CCphA | Specify the S2C cipher algorithms of SFTP/SCP. |
| jrs.sftpS2CLang | Specify the S2C language of SFTP/SCP. |
| jrs.sftpS2CMA | Specify the S2C MAC algorithms of SFTP/SCP. |
| jrs.sftpSHKC | Specify whether to check the strict host key. Possible values: {yes, no} |
| jrs.ftp\_param\_validation | Specify the command of checking the validation of FTP connection properties. Possible values:   * **TAG\_FTP\_CONNECTION\_FAILED** - Server cannot create the connection because the host name/IP or port is not valid.  Possible value: 100 (the only value) * **TAG\_FTP\_CONNECTION\_IS\_OK** - The connection is valid.  Possible value: 200 (the only value) * **TAG\_FTP\_NO\_PERMISSION** - Server can build the connection, but the username or password is not valid.  Possible value: 300 (the only value) * **TAG\_FTP\_INVALID\_FOLDER** - Server can build the connection but cannot find the folder where the output files reside.   Possible value: 400 (the only value) |
| jrs.ftpIsDht | Specify whether to export TOC in the HTML output. |
| You can use the following properties to specify the formats in which you want to send the output to the FTP site. For each output file you can further specify its format properties. | |
| jrs.ftpRst | Specify whether to send the output in a Logi Report Result file (for page report) or in a Web Report Result file (for web report) to the FTP site. |
| jrs.ftpRstFn | Specify the file name of the Logi Report Result file (for page report) or of the Web Report Result file (for web report). |
| jrs.ftpHtml | Specify whether to send the output in an HTML file to the FTP site. |
| jrs.ftpHtmlFn | Specify the file name of the HTML file. |
| jrs.ftpPdf | Specify whether to send the output in a PDF file to the FTP site. |
| jrs.ftpPdfFn | Specify the file name of the PDF file. |
| jrs.ftpExl | Specify whether to send the output in an Excel file to the FTP site. |
| jrs.ftpExlFn | Specify the file name of the Excel file. |
| jrs.ftpTxt | Specify whether to send the output in a Text file to the FTP site. |
| jrs.ftpTxtFn | Specify the file name of the Text file. |
| jrs.ftpRtf | Specify whether to send the output in an RTF file to the FTP site. |
| jrs.ftpRtfFn | Specify the file name of the RTF file. |
| jrs.ftpXml | Specify whether to send the output in an XML file to the FTP site. |
| jrs.ftpXmlFn | Specify the file name of the XML file. |
| jrs.ftpPs | Specify whether to send the output in a PostScript file to the FTP site. |
| jrs.ftpPsFn | Specify the file name of the PostScript file. |
| Notification properties | |
| jrs.notification\_emails | Specify the email notification list for successful/failed scheduled tasks. |
| jrs.success\_notify | Specify to send email notification for successful reports. |
| jrs.fail\_notify | Specify to send email notification for failed reports. |
| Time condition properties | |
| jrs.timezone | Specify the time zone. Possible values: time zone ID strings of Java. The default is current locale. |
| jrs.launch\_type | Specify to run a report immediately, at a specific time, or periodically. Possible values:   * **0** - Immediately * [**1** - At a specified date and time](#DateTime) * [**8** - Periodically](#Periodical) |
| **Properties for a specific date and time (jrs.launch\_type=1)** | |
| jrs.exe\_date | Specify a date. |
| jrs.exe\_year | Specify the year. Four digits. |
| jrs.exe\_month | Specify the month. Possible values: 0 to 11. 0 is January, 1 is February, ..., and 11 is December. |
| jrs.exe\_day | Specify a day number. |
| jrs.exe\_hour | Specify an hour number (when jrs.is\_hourly is false). |
| jrs.exe\_min | Specify a minute number (when jrs.is\_hourly is false). |
| jrs.exe\_sec | Specify a second number (when jrs.is\_hourly is false). |
| **Properties for periodical time (jrs.launch\_type=8)** | |
| jrs.is\_after | Specify whether to run the report after the specified date and time. If the value is true, use [the properties for a specific time](#Time) to define the start time of the whole periodical time. |
| jrs.is\_before | Specify whether to run the report before the specified date and time. If the value is true, specify the specified time using the jrs.cease\_\* properties. |
| jrs.cease\_year | Specify the year. Four digits. |
| jrs.cease\_month | Specify the month. Possible values: 0 to 11. 0 is January, 1 is February, ..., and 11 is December. |
| jrs.cease\_day | Specify a day number. |
| jrs.cease\_hour | Specify an hour number (when jrs.is\_hourly is false). |
| jrs.cease\_min | Specify a minute number (when jrs.is\_hourly is false). |
| jrs.cease\_sec | Specify a second number (when jrs.is\_hourly is false). |
| jrs.days\_id | Specify whether you want to run the report daily, weekly, or monthly. Possible values:   * [**0** - Daily](#Daily) * [**1** - Weekly](#Weekly) * [**2** - Monthly](#Monthly) |
| **Properties for daily (jrs.days\_id=0)** | |
| jrs.is\_weekday | Specify whether to run the report on each weekday (Monday to Friday). |
| jrs.day | Specify to run the report per a specified number of days (when jrs.is\_weekday is false). For example, if you set the value to 1, the report will run once every day. If you set it to 2, the report will run once every 2 days. Possible values: 1 to 999 days |
| **Properties for weekly (jrs.days\_id=1)** | |
| jrs.week | Specify to run the report per a specified number of weeks. Possible values: 1 to 99 weeks |
| jrs.weekdays | Specify to run the report on the specified days of the week.  Possible values: A digit string. {0, 1, 2, 3, 4, 5, 6}. 0 is Sunday, 1 is Monday, ..., and 6 is Saturday.  Example: jrs.weekdays=05 means running on Sunday and Friday. |
| **Properties for monthly (jrs.days\_id=2)** | |
| jrs.is\_day | Specify whether to run the report on the xth day of the month. |
| jrs.day | Specify to run the report on the xth day of the month (when jrs.is\_day is true). Possible values: 1 to 31 |
| jrs.week | Specify to run the report on the xth week of the month (when jrs.is\_day is false).  Possible values:   * **0** - The first week * **1** - The second week * **2** - The third week * **3** - The fourth week * **4** - The last week |
| jrs.weekday | Specify to run the report on the specified day of the week (jrs.is\_day is false). Possible values: 1 to 7. 1 is Sunday, 2 is Monday, ..., and 7 is Saturday. |
| jrs.month | Specify to run the report per a specified number of months. Possible values: 1 to 6 months. |
| **Properties for a specific time** | |
| jrs.hour | Specify to run the report at a specific hour of the day. |
| jrs.min | Specify to run the report at a specific minute of the hour. |
| jrs.is\_pm | Specify whether the time is PM or AM of the day. |
| **Properties for hourly** | |
| jrs.is\_hourly | Specify whether to run the report hourly. |
| jrs.hours | Specify to run the report per a specified number of hours.  Possible values: 1 to 99 hours |
| jrs.at\_min | Specify to run the report at a specific minute of the hour. |
| jrs.is\_between | Specify whether to run the report between a period. When the value is true, use [Properties for when jrs.is\_between=true](#jrsisbetween) to define a the period. |
| **Properties for minutely** | |
| jrs.is\_minutely | Specify whether to run the report minutely. Note iconThe property jrs.is\_hourly has the higher priority. If you set both jrs.is\_hourly and jrs.is\_minutely to true, the report will run hourly. |
| jrs.minutes | Specify to run the report per a specified number of minutes. |
| jrs.is\_between | Specify whether to run the report between a period. When the value is true, use [Properties for when jrs.is\_between=true](#jrsisbetween) to define a time duration. |
| **Properties for when jrs.is\_between=true** | |
| jrs.hour | Specify the start hour of a period. |
| jrs.min | Specify the start minute of a period. |
| jrs.is\_pm | Specify whether the start time is PM or AM. |
| jrs.hour2 | Specify the end hour of a period. |
| jrs.min2 | Specify the end minute of a period. |
| jrs.is\_pm2 | Specify whether the end time is PM or AM. |

## URL Properties for Viewing Reports

| Property | Description |
| --- | --- |
| [jrd\_filters](https://devnet.logianalytics.com/hc/en-us/articles/5741456438167-Running-Reports-via-URL#jrd_filters) | Specify the values of on-screen filters. |
| jrs.datasources | Specify the data source. It is a JSON string, with the format:  jrs.datasources= {     jrs.datasources:[     {         "jrs.data\_source\_name":"xxx",          "jrs.connections":[         {             "jrs.connection\_name":"xxx",             "jrs.\_ds\_driver":"xxx",             "jrs.\_ds\_url":"xxx",             "jrs.ds\_user":"xxx",             "jrs.ds\_pswd":"xxx",             "jrs.databases":[             // The database list in the MongoDB connection, which is an array.             {                 "jrs.dbs\_catalog-database-name":"xxx", // The database name you defined in the catalog for MongoDB.                 "jrs.dbs\_database-name":"xx", // The new database name you want to use at runtime to replace the original database name you defined in MongoDB APE.                 "jrs.dbs\_collections":[                 // The collection list in a MongoDB database, which is an array.                 {                     "jrs.dbs\_catalog-collection-name":"xxx", // The collection name you defined in the catalog for MongoDB.                     "jrs.dbs\_collection-name":"xxx" // The new collection name you want to use at runtime to replace the original collection name you defined in MongoDB APE.                 }                 ]             }             ]         }         ]     }     ] }  URL Example:  http://localhost:8888/jinfonet/tryView.jsp?…&jrs.datasources={jrs.datasources:[{"jrs.data\_source\_name":"xxx","jrs.connections":[{"jrs.connection\_name":"xxx","jrs.\_ds\_driver":"xxx","jrs.\_ds\_url":"xxx","jrs.ds\_user":"xxx","jrs.ds\_pswd":"xxx","jrs.databases":[{"jrs.dbs\_catalog-database-name":"xxx","jrs.dbs\_database-name":"xx","jrs.dbs\_collections":[{"jrs.dbs\_catalog-collection-name":"xxx","jrs.dbs\_collection-name":"xxx"}]}]}]}]}… |
| jrs.file | Specify the file name of the report. |
| jrs.hist\_file | Specify the file name of the report with its real path in the `<install_root>\history` folder, for example, 1%2fadmin567625353%2f2109098280.pdf. |
| jrs.resource\_path | Specify the path of the resource in the server resource tree, for example, /SampleReports. |
| jrs.result | Specify the name of the report with its path in the server resource tree, for example, /SampleReports/Payroll Report. |
| jrs.rst\_version | Specify the version number of the report. |
| jrs.ver\_suff | Specify the suffix of the report file. Possible values:   * **.rst** - The suffix of Logi Report Result (for page report) or Web Report Result (for web report). * **.html** - The suffix of the HTML file. * **.pdf** - The suffix of the PDF file. * **.txt** - The suffix of the Text file. * **.xls** - The suffix of the Excel file. * **.ps** - The suffix of the PostScript file. * **.rtf** - The suffix of the RTF file. * **.xml** - The suffix of the XML file. |
| jrs.version\_number | Specify the version number of the resource, for example, 1. |
| type | Specify the type of the report. Possible values:   * **rstfile** - Get the result versions of a specific report. * **rstdoc** - Get the versions of a specific result. |
| jrs.bookmark | Specify the name of a [bookmark](https://devnet.logianalytics.com/hc/en-us/articles/7985371637143-Bookmarking-a-Web-Report) that you saved for the web report to run the bookmark. |
| jrs.is\_pls\_result=true | Apply [cached report bursting](https://devnet.logianalytics.com/hc/en-us/articles/5741469954327-Cached-Report-Bursting) to view the report. |
| jrs.profile | Specify the name of a Web Report Studio profile, Page Report Studio profile, or JDashboard profile that server administrators created. For more information, see [Configuring Server Profile](https://devnet.logianalytics.com/hc/en-us/articles/5741409420567-Configuring-Server-Profile). |

## URL Properties for Adding and Deleting Users/Roles/Groups

| Property | Description |
| --- | --- |
| currentEditRealm | Specify the security realm in which the user/role/group is. |
| user | Specify the name of the user. |
| fullName | Specify the full name of the user. |
| description | Specify the description for the user/role/group. |
| email | Specify the email address of the user. |
| password | Specify the password of the user. |
| confirmPassword | Specify the password of the user again to confirm it. |
| accountDisabled=ON | Disable the user account for the time being. |
| passwordLife | Specify the validity period of the user password. Possible values:   * **neverExpire** Set `passwordLife=neverExpire` if you don't want the user password to expire. * **expire** Set `passwordLife=expire`, and then specify   the number of days during which the password is valid, by setting the **expireTime** property. |
| expireTime | Specify the number of days during which the user password is valid. |
| enableBlank | Specify the length of the user password. Possible values:   * **blank**  Set `enableBlank=blank` if the password can be blank. * **minValue** Set `enableBlank=minValue`, and then specify the minimum number of characters in the password, by setting the **minLength** property. |
| minLength | Specify the minimum number of characters in the user password. Possible values: 1 to 20 |
| jrs.privilege\_publish\_report | Specify whether to grant the user/role/group the ability to publish resources to Logi Report Server. |
| jrs.privilege\_access\_advanced\_properties | Specify whether to grant the user/role/group the ability to view advanced version properties information, such as catalog connections and report related resources. |
| roleName | Specify the name of the role. |
| parentRoles | Specify the parent role for the role. Possible values: An existing role name or "NoneParent" if the role does not have a parent role. |
| groupName | Specify the name of the group. |
| parentGroups | Specify the parent group for the group. Possible values: An existing group name or "NoneParent" if the group does not have a parent group. |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741471451159-Accessing-Visual-Analysis-via-URL)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741464180119-Web-Report-Studio-Server-v19)
