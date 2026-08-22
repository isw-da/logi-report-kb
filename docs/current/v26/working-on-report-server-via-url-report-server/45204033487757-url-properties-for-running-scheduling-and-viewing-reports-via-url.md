---
title: "URL Properties for Running, Scheduling, and Viewing Reports via URL"
id: 45204033487757
section: "Working on Report Server via URL Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45204033487757-URL-Properties-for-Running-Scheduling-and-Viewing-Reports-via-URL
updated_at: 2026-04-30T14:11:05Z
source_host: logi-report-v26.insightsoftware.com
---
# 
URL Properties for Running, Scheduling, and Viewing Reports via URL

This topic describes the basic URL properties you should consider when running, scheduling, and viewing reports, and adding and deleting users/roles/groups. 

You need to specify the properties for each report format when you run or schedule reports via URL. For more information, see the Report Javadoc.

This topic contains the following sections:

- General URL Properties for Running and Scheduling Reports

- URL Properties for Scheduling Reports

- URL Properties for Viewing Reports

- URL Properties for Adding and Deleting Users/Roles/Groups

## 
General URL Properties for Running and Scheduling Reports

| Property | Description |
| --- | --- |
| jrs.path | Specify a path or a resource name with full path. Example: /SampleReports, or /SampleReports/Payroll Report.cls |
| jrs.catalog | Specify the catalog name with full path. The customer does not need to specify the catalog in the URL, if the report and report version are associated with a report-catalog relation, which can be retrieved via the web API endpoint GET /node/rptcatrelation. Example: /SampleReports/SampleReports.cat, or %2fSampleReports%2fSampleReports.cat |
| jrs.report | Specify the report name with full path. Example: /SampleReports/Employee Information List.cls, or %2fSampleReports%2fEmployee Information List.cls |
| When specifying the full path of a resource in the preceding three properties: If the resource is in the Public Reports folder in the server resource tree, you should start the path with "/". For example, for the /Public Report/SampleReports folder, provide the path as "/SampleReports". If the resource is in the My Reports folder in the server resource tree, you should start the path with "/USERFOLDERPATH/username/" (change username to the real username with which you sign in to Report Server). For example, suppose your username is Jim and you want to access the /My Reports/Shipments folder, provide the path in the URL as "/USERFOLDERPATH/Jim/Shipments". |  |
| jrs.combined_reports | A JSON format string to specify combined report list when run/schedule a web report, the combined report must be web report. Example: [{"name":"/SampleReports/Shipment Status Report.wls","ver":1},{"name":"/SampleReports/Sales by Account Manager Report.wls","ver":1}], or %5B%7B%22name%22%3A%22%2FSampleReports%2FShipment%20Status%20Report.wls%22%2C%22ver%22%3A1%7D%2C%7B%22name%22%3A%22%2FSampleReports%2FSales%20by%20Account%20Manager%20Report.wls%22%2C%22ver%22%3A1%7D%5D |
| jrs.result_type | Specify the format in which you want to run a report. Possible values: 1 - To HTML 2 - To PDF 3 - To TEXT 4 - To Excel 5 - To PostScript 6 - To Rich Text Format 7 - To XML 8 - To Page Report Studio (for page reports) 8 - To Web Report Studio (for web reports) |
| jrs.param$PARAMETER_NAME | Specify the parameter values for running a report. Use jrs.param$PARAMETER_NAME=VALUE to set parameter values of a report, where PARAMETER_NAME is a parameter name and VALUE is a URL-encoded value of the parameter. For example, jrs.param$TERMSDAYS=30&jrs.param$PTODAY=May 21, 1998. When specifying values for a multi-valued parameter, you need to add _isMultiple_jrs.param$PARAMETER_NAME=true before the parameter values, to declare that the parameter supports multiple values. For example: &_isMultiple_jrs.param$PM=true&jrs.param$PM=3&jrs.param$PM=16. To apply all the values of a parameter, use jrs.param$PARAMETER_NAME=%07. See the example: http://localhost:8888/jinfonet/tryView.jsp?jrs.report=%2fSampleReports%2fShipment+Status+Report.wls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=8&jrs.param%24P_StartDate=2015-12-30&jrs.param%24p_EndDate=2017-1-1&jrs.param%24P_ShipperTerritory-Shipper+Territory=%07&jrs.param%24P_ShipperTerritory-Shipper+Name=%07&jrs.param_page=false |
| jrs.param_values | Specify the parameter values for running a report. This is the escaped string of the parameter values of the report.Format: PARAMETER_NAME=VALUE,PARAMETER_NAME=VALUE,... Examples: jrs.param_values=PTODAY%3dMay%2021%5c%2c%201998%2cTERMSDAYS%3d30 (original: PTODAY=May 21\, 1998,TERMSDAYS=30) jrs.param_values=STARTDATE%3d1998-05-10%2cENDDATE%3d1998-07-10 (original: STARTDATE=1998-05-10,ENDDATE=1998-07-10) |
| jrs.param_page | Specify whether to show the parameter dialog box for specifying parameter values that you did not provide by jrs.param$ in the URL. Such parameter dialog boxes include the one Server displays during report running and those brought by actions that lead to the change of parameters after the report renders in Page Report Studio, for example, the actions such as inserting a formula with a new parameter and running a master/detail report. However, this property does not affect the dialog box displayed via Menu > Report > Change Parameters, because the dialog box is to display all the parameters of the report. The default value of the property is true. When you provide the value of a middle level cascading parameter (including old style cascading parameter) in the URL, the parameter dialog box only shows the lower-level parameters. When you set the property value to false, Server will not display the parameter dialog box during the whole report running. Server uses the parameter values you provided and the default values of the other parameters to run the report. |
| jrs.rpt_language | Specify the language in which you want to generate the report. The value should be consistent with the language and country code part of the language property file name. For example, if the language property file name is ReportName_de_DE.properties, you should set this property as jrs.rpt_language=de_DE. You can also use jrs.rpt_language=de&jrs.rpt_country=DE to achieve the same goal. If you only want to use jrs.rpt_language=de, you will have to rename the language property file to ReportName_de.properties. Examples: http://localhost:8888/jinfonet/tryView.jsp?jrs.report=%2fSampleReports%2fEmployee Information List.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=2&jrs.enable_nls=true&jrs.rpt_language=de_DE http://localhost:8888/webos/app/pagestudio/run.jsp?jrs.catalog=/SampleReports/SampleReports.cat&jrs.report=/SampleReports/Employee Information List.cls&jrs.enable_nls=true&jrs.rpt_language=de&jrs.rpt_country=DE If you change Employee Information List_de_DE.properties to Employee Information List_aaa.properties in Employee Information List.cls's real path folder, for example C:\LogiReport\Server\history\1\JReport_System_User457188937, then you can use the following URL to run NLS report: http://localhost:8888/webos/app/pagestudio/run.jsp?jrs.catalog=/SampleReports/SampleReports.cat&jrs.report=/SampleReports/Employee Information List.cls&jrs.enable_nls=true&jrs.rpt_language=aaa |
| jrs.rpt_encoding | Specify the encoding in which you want to generate the output. |
| jrs.has_style | Specify whether to enable the style group that you have set for the report. |
| jrs.style_group | Specify the style group which could be StyleName or StyleName.css. StyleName is a CSS Style Sheet whose name is StyleName in the Report resources system. It might come from a .css file on drive or be created from the CSS editor. StyleName.css is a *.css file on drive which may not follow the CSS style rule and therefore not work. You should use jrs.style_group=StyleName in case StyleName.css fails, though both can work most of the time. |
| jrs.db_user | Specify the new database user ID if you do not want to use the default DB user ID in the catalog. |
| jrs.db_pswd | Specify the new database password if you do not want to use the default DB password in the catalog. |
| jrs.jdbc_url | Specify the new JDBC URL in the catalog to run a report. |
| jrs.jdbc_driver | Specify the new JDBC driver in the catalog to run a report. |
| jrs.wp | Specify the WHERE portion. For example, a report has the field Customer Region, and you want to restrict the field to CA in the URL. You can then set a new WHERE portion like "...jrs.result_type=1&jrs.wp=Customers.Region='CA'...". |
| jrs.named_wp | Specify the named WHERE portion that exists in the catalog. |
| jrs.jdbc_connection_object | Specify a java.sql.Connection object to run a report dynamically. You can use this parameter in the three methods of jet.server.api.RptServer: runReport(), runReportNotWaitResult(), and submitScheduledTask(). Example: Running a report with your JDBC connection object using the Report Server API. //Create the java.sql.Connection object. java.sql.Connection myCon = java.sql.DriverManager.getConnection(dbUrl); //Set the parameter "jrs.jdbc_connection_object" to run a report. propParams.put("jrs.jdbc_connection_object", myCon); //Run the report using this java.sql.Connection object instead of //the default DB settings in the catalog. rptServer.runReport(userID, catalog, report set, propParams); |
| jrs.security_file_name | Specify a security file. The security definitions in the security file will replace that in the specified catalog. |
| jrs.applet_type | Specify the Java runtime environment to run applets. Possible values: 2 - Java Plug-In 1.2 for Windows 3 - Java Plug-In 1.3 for Windows |
| jrs.web_browser | Specify the web browser for which the HTML output adapts. Possible values: 0 - IE or Chrome 1 - Firefox |
| jrs.timeout_send_email | Specify whether to notify someone of the task status via email if the task has not finished running when the task duration is up. Possible values: true/false. The task duration uses the time specified by jrs.report_timeout in the URL. If there is not jrs.report_timeout, Server uses the time specified by the web.timeouts.report_wait property in the server.properties file in \bin. |
| jrs.report_timeout | Specify a time duration in seconds for a scheduled report running task. |
| jrs.mailto | Specify the address you want to send the email to. |
| jrs.mailsubject | Specify the subject of the email. |
| jrs.mailcomments | Specify the comments to the email contents. |
| jrs.mailfrom | Specify the email address of the sender. |
| jrs.timeout_sendmail_message | Specify the contents of the email. |
| CustomOffset | Add the property CustomOffset=true in the URL if you want the date and time values in your report to use the time zone that you have set on the values in the XML data source, instead of using the time zone of your server runtime environment. In the case you do not add the property in the URL, which means that CustomOffset=false, if you do not provide a specific time zone in the URL or session, the server runtime time zone is the time zone setting you defined on the Server Console > My Profile. The calculation of grouping and filtering on data of the Date/Time/DateTime type is always based on the runtime time zone, as the unified standard, regardless of the value-level time zone that you set in the XML data source. When CustomOffset=true, the values of parameters of the Date/Time/DateTime type always use the runtime time zone, regardless of the value-level time zone that you set in the XML data source. |
| FunctionApplyOffset | By default, Server applies the time zone you set in server preferences to Date/Time/DateTime field values in built-in functions. If you want to retain the time zone of the field values in built-in functions, run reports via URL and add "CustomOffset=true&FunctionApplyOffset=true" in the URL. |
| Excel format properties |  |
| jrs.result_type=4 | It means to export to Excel. Example: http://localhost:8888/jinfonet/tryView.jsp?jrs.cmd=jrs.try_vw&jrs.report=%2fSampleReports%2fPayroll%20Report.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=4&jrs.excel_format=0&jrs.excel_format_types=1 |
| jrs.excel_extension | Specify whether to use custom file extension. |
| jrs.excel_format | Specify the Excel version. Possible values: 0 - The Excel output file uses the .xlsx format. 1 - The Excel output file uses the .xls format. |
| jrs.excel_format_types | Specify the format of the Excel output. Possible values: 0 - It means Auto Format, and Server defines the format according to the objects in the report. Server uses Column Format when the report contains crosstabs or tables, or else Report Format. 1 - It means Report Format and uses the format as you designed in the template, for the report in Excel. Use this format if you just want to view the report in Excel. 2 - It means Column Format and calculates all components' row/column values in the report using the Columned property value of the report when exporting. Use this format if you want to actively use the report in Excel such as filtering and sorting. 3 - It means Data Format and only generates the report data without any format. This value is only available when jrs.excel_format=1. |
| jrs.has_shapes | Specify whether to include the drawing objects in the Excel output, such as lines, ovals, and boxes. |
| jrs.print_header | Specify the page header text for the printed file. |
| jrs.print_footer | Specify the page footer text for the printed file. |
| jrs.is_wordwrap | Specify the word-wrap settings. Possible values: 0 - It means All Keep Existing and keeps all the settings of each object's Word Wrap property originally specified in the report. 1 - It means All Disabled and disables the Word Wrap property for all objects. That is, the Word Wrap property is false for all objects. 2 - It means All Enabled and enables the Word Wrap property for all objects. That is, the Word Wrap property is true for all objects. |
| jrs.print_gridlines | Specify whether to include gridlines when printing the Excel output. |
| jrs.to_excel_runLinkedReport | Specify whether to generate the linked reports (excluding the detail reports) in the output when the report is linked with other reports. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data. |
| Text format properties |  |
| jrs.delimiter | Specify a delimiter other than comma, for example, jrs.delimiter=%23(#) jrs.delimiter=~ jrs.delimiter=/ |
| jrs.is_text_delimiter=jrs.is_csv | To use the CSV format, set these properties: jrs.result_type=3&jrs.is_text_delimiter=jrs.is_csv&jrs.is_norm_txt=false. |
| jrs.is_quotemark=true | Specify whether to use quote marks in the text output. Possible values: true/false. |
| jrs.udchar_width | Specify an integer value for each unit of the horizontal density between columns. The resulting density is a direct ratio of the value you specify. That is, the greater the value, the smaller the width between columns. By default, Report defines the density. |
| jrs.udchar_height | Specify an integer value for each unit of the vertical density between columns. The resulting density is a direct ratio of the value you specify. That is, the greater the value, the smaller the height between columns. By default, Report defines the density. |
| jrs.txt_compress | Specify whether to generate the output in Text in a compressed size. Possible values: true/false. If true, there will be no clearance between the columns. |
| jrs.hasHeadFoot | Set this property to true if you want the Text file to contain all headers and footers in the report, including Report Header/Footer, Page Header/Footer, and Group Header/Footer. Otherwise, set it to false, and the Text file will only contain the data in the Detail panel. |
| jrs.txt_windows | Set this property to true if you want to use Windows end-of-line characters to indicate the start of a new line. Report will use two characters  and  at the end of the line. Or, set it to false if you want to use UNIX End-of-line characters to indicate the start of a new line. Report will only use the UNIX End-of-line character . |
| jrs.result_file_name | Set the output file name, for instance, jrs.result_file_name=test.txt. |
| jrs.to_text_runLinkedReport | Specify whether to generate the linked reports (excluding the detail reports) in the output when the report is linked with other reports. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data. |

## 
URL Properties for Scheduling Reports

| Property | Description |
| --- | --- |
| General properties |  |
| jrs.task_class | Specify the class name of the task. Possible values: jet.server.schedule.jrtasks.UpdateRptTask jet.server.schedule.jrtasks.PublishToDiskTask jet.server.schedule.jrtasks.SendJRMailTask jet.server.schedule.jrtasks.SendMailTask jet.server.schedule.jrtasks.PrintRptTask |
| jrs.has_task_listener | Specify whether to implement TaskListener. |
| jrs.task_listener_class | Specify a Java class name which implements the TaskListener (jrs.task_listener_class). |
| jrs.task_id | Specify the task ID of a scheduled task. This property is unnecessary if you are submitting a new schedule. |
| jrs.mail_to_referuser | Specify whether to send email to each user who can view a report with cached report bursting. |
| jrs.is_bursting_task | Indicate that you are scheduling a bursting report task. |
| jrs.bursting_schema$Schema_Name | Specify the names of the schemes you want to schedule. |
| Publishing to the versioning system properties |  |
| jrs.to_version | Specify whether to publish the output to the versioning system. |
| jrs.to_version_rst | Specify whether to publish a page report to a Logi Report result file (RST file) or publish a web report to a static web report result file (WST file). You can further specify the result properties. For more information, see the Report Javadoc. |
| jrs.to_version_rsd | Specify whether to publish the output to a page report result file (RSD file). You can further specify the result properties. For more information, see the Report Javadoc. |
| jrs.to_version_html | Specify whether to publish the output to the versioning system in HTML. You can further specify the HTML properties. For more information, see the Report Javadoc. |
| jrs.to_version_pdf | Specify whether to publish the output to the versioning system in PDF. You can further specify the PDF properties. For more information, see the Report Javadoc. |
| jrs.to_version_excel | Specify whether to publish the output to the versioning system in Excel. You can further specify the Excel properties. For more information, see the Report Javadoc. |
| jrs.to_version_txt | Specify whether to publish the output to the versioning system in Text. You can further specify the Text properties. For more information, see the Report Javadoc. |
| jrs.to_version_rtf | Specify whether to publish the output to the versioning system in RTF. You can further specify the RTF properties. For more information, see the Report Javadoc. |
| jrs.to_version_xml | Specify whether to publish the output to the versioning system in XML. You can further specify the XML properties. For more information, see the Report Javadoc. |
| jrs.to_version_ps | Specify whether to publish the output to the versioning system in PostScript. You can further specify the PostScript properties. For more information, see the Report Javadoc. |
| jrs.archive_location | Specify the location where you want to save the report. Possible values: 0 - Save the report to the built-in version folder. Not supported for organization users when the report is from the Public Reports folder. 1 - Save the report to the My Reports folder. You can then use jrs.archive_my_destination to specify a report version name with the path in the My Reports folder. 2 - Save the report to the Public Reports folder. You can then use jrs.archive_public_destination to specify a report version name with the path in the Public Reports folder. Not supported for organization users. |
| jrs.enable_archive_policy | Specify whether to apply an archive policy to the saved report. |
| jrs.archive_new_version | Specify how to archive the new version. Possible values: true - Use multiple versions for the report. You can then use jrs.maxversion to specify the maximum number of versions in the version table of the report. 0 means unlimited number. false - Replace the old version with the new version. |
| jrs.need_expire | Specify whether you want the saved report to expire. |
| jrs.auto_delete_method | Specify when you want the saved report to expire and to delete it. If the time you specify exceeds one hundred years, Server will keep the report forever. Possible values: 0 - Server automatically deletes the report after a specified number of days. You can then use jrs.expire_days to specify the number of days, for example: jrs.need_expire=true&jrs.auto_delete_method=0&jrs.expire_days=60. 1 - Server automatically deletes the report after a specified date. You can then use jrs.auto_delete_year, jrs.auto_delete_month, and jrs.auto_delete_date to specify the year, month, and date, for example: jrs.need_expire=true&jrs.auto_delete_method=1&jrs.auto_delete_year=2017&jrs.auto_delete_month=5&jrs.auto_delete_date=16. |
| jrs.expire_days | Specify the number of days Server keeps a report version until it expires. The default value is 30. |
| Publishing to the file system properties |  |
| jrs.to_disk | Specify whether you want to publish the report to disk. |
| jrs.to_rst | Specify whether to publish a page report to a Logi Report result file (RST file) or publish a web report to a static web report result file (WST file). You can further specify the result properties. For more information, see the Report Javadoc. |
| jrs.to_rsd | Specify whether to publish the output to page report result file (RSD file). You can further specify the result properties. For more information, see the Report Javadoc. |
| jrs.to_html | Specify whether to publish the output to the file system in HTML. You can further specify the HTML properties. For more information, see the Report Javadoc. |
| jrs.to_pdf | Specify whether to publish the output to the file system in PDF. You can further specify the PDF properties. For more information, see the Report Javadoc. |
| jrs.to_excel | Specify whether to publish the output to the file system in Excel. You can further specify the Excel properties. For more information, see the Report Javadoc. |
| jrs.to_text | Specify whether to publish the output to the file system in Text. You can further specify the Text properties. For more information, see the Report Javadoc. |
| jrs.to_rtf | Specify whether to publish the output to the file system in RTF. You can further specify the RTF properties. For more information, see the Report Javadoc. |
| jrs.to_xml | Specify whether to publish the output to the file system in XML. You can further specify the XML properties. For more information, see the Report Javadoc. |
| jrs.to_ps | Specify whether to publish the output to the file system in PostScript. You can further specify the PostScript properties. For more information, see the Report Javadoc. |
| jrs.to_disk_xxx_path_type | Specify where to publish the output in the xxx format: to the server resource tree or to the server disk path. Possible values: 0 - Publish to the Report Server resource tree. 1 - Publish to a drive path. |
| jrs.xxx_dir | Specify the path for the xxx format output. |
| jrs.xxx | Specify the file name for the xxx format output. |
| Publishing to email properties |  |
| jrs.jrmail + NUMBER | Contain specifications (Report email properties) of one email task for a report. |
| jrs.csmail + NUMBER | Contain specifications (Report email properties) of one email task for sending an email with or without an attachment. You can use this property via URL or via invoking the Server API. |
| jrs.mailto | Specify the email address you want to send the email to. |
| jrs.mailcc | Specify the email address you want to send a copy of the email to. |
| jrs.mailbcc | Specify the email address you want to secretly send a copy of the email to. |
| jrs.mailsubject | Specify the subject of the email. |
| jrs.mailcomments | Specify the comments of the email. |
| jrs.mailformat | Specify the email format. Possible values: 0 - E-mail Result in HTML E-mail Format 1 - E-mail Result in Plain Text E-mail Format 2 - Attachment in HTML Format 3 - Attachment in PDF Format 4 - Attachment in Logi Report Result Format (for page reports) 4 - Attachment in Web Report Result Format (for web reports) 6 - Attachment in PostScript Format 7 - Attachment in Excel Format 8 - Attachment in RTF Format 9 - Attachment in XML Format 11 - Attachment in Text Format When sending the report as an attachment file, you need to specify a file name using jrs.mailattach + NUMBER. You can further specify format properties for the attachment file. For more information, see the Report Javadoc. |
| jrs.mailcompress | Specify whether to enable Java archive compress. |
| jrs.mailattach + NUMBER | Specify the attached file for the email. You can attach multiple files to one email. Possible values: The attached file name. |
| jrs.mailencoding | Specify the encoding of the email. Possible values: such as UTF-8, UTF-16, and ISO8859-1. You can use jrs.mailencoding to specify the email encoding in the URL. When sending emails by RMI API, sometimes, Server might return wrong characters in the email. To avoid such problems, specify the same correct value of -Djreport.url.encoding on both the server and RMI client side. For example, your web application calls Report Server (standalone) via the RMI function from WebSphere, and you want to use UTF-8 (rather than UTF8) as the email encoding, do as follows: Specify -Djreport.url.encoding=UTF-8 for both JVM running Report Server and WebSphere. Specify jrs.mailencoding=UTF-8. |
| E-mail Result in HTML E-mail Format |  |
| jrs.to_mail_htmlmail | Specify whether to send the report in the HTML format in the email body. If true, the report will overwrite the comments that you specify for the email. |
| jrs.to_mail_htmlmail_runLinkedReport | Specify whether to generate the linked reports (excluding the detail reports) in the output when the report is linked with other reports. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data. If you are only interested in the primary report, do not set this property. |
| E-mail Result in Plain Text E-mail Format |  |
| jrs.to_mail_textmail | Specify whether to send the report in the plain text format in the email body, with no other information such as color and images.jrs.to_mail_textmail and jrs.to_mail_htmlmail cannot work concurrently. |
| jrs.plaintext_mail_char_width | Specify an integer value for each unit of the horizontal density between the columns. The resulting density is a direct ratio of the value you specify. That is, the greater the value, the smaller the width between the columns. By default, Report defines the density. |
| jrs.plaintext_mail_char_height | Specify an integer value for each unit of the vertical density between the columns. The resulting density is a direct ratio of the value you specify. That is, the greater the value, the smaller the height between the columns. By default, Report defines the density. |
| jrs.plaintext_mail_txt_compress | Specify whether to generate the report to Text in a compressed size. There will be no clearance between the columns. |
| jrs.plaintext_mail_hasheadfoot | Specify whether you want the Text output to contain all headers and footers in the report, including Report Header/Footer, Page Header/Footer, and Group Header/Footer. Otherwise, the Text output will only contain the data in the Detail panel. |
| jrs.plaintext_mail_txt_windows=true | Specify to use Windows end-of-line characters to indicate the start of a new line. Report will use two characters  and  at the end of the line. |
| jrs.plaintext_mail_txt_windows=false | Specify to use UNIX End-of-line characters to indicate the start of a new line. Report will only use the UNIX character  at the end of the line. |
| jrs.to_mail_textmail_runLinkedReport | Specify whether to generate the linked reports (excluding the detail reports) in the output when the report is linked with other reports. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data. If you are only interested in the primary report, do not set this property. |
| Attachment in Logi Report Result Format or Web Report Result Format |  |
| jrs.to_mail_rst | Specify whether to send the report in a Logi Report Result file or Web Report Result file as the email attachment. Do not set this property when the schedule task contains both page reports and web reports. |
| jrs.mail_rst_file | Specify the name of the Logi Report result file. |
| jrs.mail_zip_result | Specify whether to compress the report to reduce the disk size and I/O; however, it uses more CPU resources. |
| jrs.mail_rst_precision | Specify the precision level with which you want to publish the report: Low or High. Changing the default value may cause abnormalities in report layout. |
| jrs.to_mail_rst_runLinkedReport | Specify whether to generate the linked reports (excluding the detail reports) in the output when the report is linked with other reports. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data. If you are only interested in the primary report, do not set this property. |
| Attachment in HTML Format |  |
| jrs.to_mail_html | Specify whether to send the report in an HTML file as the email attachment. |
| jrs.mail_html_file | Specify the name of the HTML file. |
| jrs.mail_no_margin_html | Specify whether to remove the margins you originally set while designing the report. |
| jrs.mail_is_multi_files | Specify whether to generate the report to multiple HTML files. Server designates a serial number for each HTML page. For example, if you name a 3-page report as "sales", Server will create three files called sales_1.html, sales_2.html, and sales_3.html. |
| jrs.mail_embedded_css | Specify whether to embed the cascading style sheet (CSS) in the HTML files; otherwise, Server generates the .css file individually. |
| jrs.mail_has_hyperlink_pref | Specify whether to display hyperlinks for navigating previous and next pages on the navigation bar of the HTML output. |
| jrs.mail_has_page_number | Specify whether to display the current page number and the total page number on the navigation bar of the HTML output. |
| jrs.mail_drilldown | Specify whether to enable the Drilldown feature in the HTML output so that you can inspect certain items for further detailed data. |
| jrs.mail_use_section508_output | Specify whether to add the accessibility attributes you defined for the report elements via the Designer Report Inspector to the HTML output, which is Section 508 compliant including HTML data table, accessible attributes, and relative font feature . For more information, see Making HTML and PDF Report Results and Server Console Accessible. |
| jrs.mail_use_html_table | Specify whether to output the table and crosstab components to table objects in the HTML output. |
| jrs.mail_relative_font_size=false | Specify to generate the report using the fixed font size that you cannot adjust according to the font size settings in the web browser. |
| jrs.mail_relative_font_size=true | Specify to generate the report using a relative font size that you can adjust according to the font size settings in the web browser. |
| jrs.mail_format_chart | Specify the image type with which you want to display charts: GIF, JPEG, PNG, or Auto-select (Server will automatically detect the image format: GIF if the image colors are less than 256 colors or else JPEG). |
| jrs.mail_html_resolution | Resolution of the report to zoom in/out, in DPI. Server obtains the default value from the operation system, which is the resolution of your monitor, for example, 72 DPI on UNIX or 96 on Windows. You can set a higher/lower value to zoom in/out. |
| jrs.mail_web_browser | Specify IE or Firefox as the web browser for which the HTML output adapts. |
| jrs.mail_text_overflow | Specify whether to make the text overflow is visible or hidden. |
| jrs.to_mail_html_runLinkedReport | Specify whether to generate the linked reports (excluding the detail reports) in the output when the report is linked with other reports. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data. If you are only interested in the primary report, do not set this property. |
| Attachment in PDF Format |  |
| jrs.to_mail_pdf | Specify whether to send the report in a PDF file as the email attachment. |
| jrs.mail_pdf_file | Specify the name of the PDF file. |
| jrs.mail_no_margin_pdf | Specify whether to remove the margins you originally set while designing the report. |
| jrs.compress_chk_pdf_mail | Specify the percentage to compress the images in the report. |
| jrs.mail_print_mode_pdf=true | Specify to take the whole report as a graphic to transform the report by the method of simulated printer. |
| jrs.mail_print_mode_pdf=false | Specify to take the whole report as a dataset to transform the report by sequence. |
| jrs.mail_toc_pdf | Specify whether to generate a Table of Contents in the PDF output. Not supported for web reports. |
| jrs.mail_drilldown_pdf | Specify whether to enable the Drilldown feature in the HTML output so that you can inspect certain items for further detailed data. |
| jrs.mail_pdf_encrypt | Specify whether to encrypt the PDF output. |
| jrs.mail_pdf_sign | Specify whether to add the digital sign to the PDF output. |
| jrs.to_mail_pdf_runLinkedReport | Specify whether to generate the linked reports (excluding the detail reports) in the output when the report is linked with other reports. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data. If you are only interested in the primary report, do not set this property. |
| jrs.mail_accessible_pdf | Specify whether to generate the report as an accessible PDF file. For more information, select Making HTML and PDF Report Outputs and Server Console Accessible. |
| mail_pdf_zoom | Specify the percentage by which you want to zoom the report contents in the PDF output. A valid percentage is greater than 0 and no larger than 6400%. |
| Attachment in Excel Format |  |
| jrs.to_mail_excel | Specify whether to send the report in an Excel file as the email attachment. |
| jrs.mail_excel_file | Specify the name of the Excel file. |
| jrs.mail_excel_format | Specify the Excel version: Excel 97-2003 Workbook (*.xls) Specify to run the file in the .xls format. Excel Workbook (*.xlsx) Specify to run the file in the .xlsx format. |
| jrs.mail_excel_format_types | Specify the format of the Excel output. Auto Format Specify to define the format according to the objects in the report. Server uses Column Format when the report contains crosstabs or tables, or else Report Format. Report Format Specify to use the format as you designed in the template, for the report in Excel. Use this format if you just want to view the report in Excel. Column Format Specify to calculate all components' row/column values in the report using the Columned property value of the report when exporting. Use this format if you want to actively use the report in Excel such as filtering and sorting. Data Format Specify to only generate the report data without any format. Data Format is only available for the Excel version of Excel 97-2003 Workbook (*.xls). |
| jrs.mail_has_shapes | Specify whether to include the drawing objects in the Excel output, such as lines, ovals, and boxes. |
| jrs.mail_print_header | Specify the page header text for the printed file. |
| jrs.mail_print_footer | Specify the page footer text for the printed file. |
| jrs.mail_excel_wordwrap | Specify the word-wrap settings: All Keep Existing Specify to keep all the settings of each object's Word Wrap property originally specified in the report. All Disabled Specify to disable the Word Wrap property for all objects. That is, the Word Wrap property is false for all objects. All Enabled Specify to enable the Word Wrap property for all objects. That is, the Word Wrap property is true for all objects. |
| jrs.mail_print_gridlines | Specify whether to include gridlines when printing the Excel output. |
| jrs.to_mail_excel_runLinkedReport | Specify whether to generate the linked reports (excluding the detail reports) in the output when the report is linked with other reports. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data. If you are only interested in the primary report, do not set this property. |
| Attachment in Text Format |  |
| jrs.to_mail_txt | Specify whether to send the report in a Text file as the email attachment. |
| jrs.mail_text_file | Specify the name of the Text file. |
| jrs.mail_is_normal_text | Specify whether to generate the report to a standard text file, using a delimiter to separate fields. |
| jrs.mail_char_width | Specify an integer value for each unit of the horizontal density between the columns. The resulting density is a direct ratio of the value you specify. That is, the greater the value, the smaller the width between the columns. |
| jrs.mail_char_height | Specify an integer value for each unit of the vertical density between the columns. The resulting density is a direct ratio of the value you specify. That is, the greater the value, the smaller the height between the columns. |
| jrs.mail_text_is_delimiter | Specify the delimiter to separate fields. CSV Format Specify to use a comma to separate fields. Tab Delimited Specify to use a Tab delimiter to separate fields. Custom Delimiter Specify to separate fields by a user defined delimiter. Then, specify your own delimiter using jrs.mail_delimiter. |
| jrs.mail_delimiter | Specify your own delimiter. |
| jrs.mail_is_quotemark | Specify whether to use quote marks in the Text output. |
| jrs.mail_repeat | Specify whether you want a cell that has no value in the Text output to use the value of the previous cell in the same column. |
| jrs.mail_is_text_TrimBlankSpaces | Specify whether you want to remove the blank spaces at the beginning and end of field values, instead of keeping them. |
| jrs.mail_txt_compress | Specify whether to generate the report to Text in a compressed size. There will be no clearance between the columns. |
| jrs.mail_hasheadfoot | Specify whether you want the Text output to contain all headers and footers in the report, including Report Header/Footer, Page Header/Footer, and Group Header/Footer. Otherwise, the Text output will only contain the data in the Detail panel. |
| jrs.mail_txt_windows=true | Specify to use Windows end-of-line characters to indicate the start of a new line. Report will use two characters  and  at the end of the line. |
| jrs.mail_txt_windows=fase | Specify to use UNIX End-of-line characters to indicate the start of a new line. Report will only use the UNIX character  at the end of the line. |
| jrs.to_mail_txt_runLinkedReport | Specify whether to generate the linked reports (excluding the detail reports) in the output when the report is linked with other reports. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data. If you are only interested in the primary report, do not set this property. |
| jrs.mail_text_file_suffix | Specify the suffix of the attached Text file, which can be .txt or .dat. |
| Attachment in RTF Format |  |
| jrs.to_mail_rtf | Specify whether to send the report in an RTF file as the email attachment. |
| jrs.mail_rtf_file | Specify the name of the RTF file. |
| jrs.mail_best_editing_rtf | Specify whether to apply flow layout to the RTF output. |
| jrs.mail_no_margin_rtf | Specify whether to remove the margins you originally set while designing the report. |
| jrs.to_mail_rtf_runLinkedReport | Specify whether to generate the linked reports (excluding the detail reports) in the output when the report is linked with other reports. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data. If you are only interested in the primary report, do not set this property. |
| Attachment in XML Format |  |
| jrs.to_mail_xml | Specify whether to send the report in an XML file as the email attachment. |
| jrs.mail_xml_file | Specify the name of the XML file. |
| jrs.mail_is_only_data | Specify whether you want to only contain the database column information in the generated XML file and to only contain the structure information of the report in the generated XML schema file. |
| jrs.mail_xsdfile | Specify the path of an existing XML schema file (.xsd). Server generates the XML file based on it. Otherwise, Server generates a new XML schema file to the folder where the XML file is. The new XML schema file and the XML file will have the same name but with different extensions. |
| jrs.to_mail_xml_runLinkedReport | Specify whether to generate the linked reports (excluding the detail reports) in the output when the report is linked with other reports. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data. If you are only interested in the primary report, do not set this property. |
| Attachment in PostScript Format |  |
| jrs.to_mail_ps | Specify whether to send the report in a PostScript file as the email attachment. |
| jrs.mail_ps_file | Specify the name of the PostScript file. |
| jrs.mail_no_margin_ps | Specify whether to remove the margins you originally set while designing the report. |
| jrs.to_mail_ps_runLinkedReport | Specify whether to generate the linked reports (excluding the detail reports) in the output when the report is linked with other reports. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data. If you are only interested in the primary report, do not set this property. |
| Publishing to a printer properties |  |
| jrs.if_print | Specify whether to print the output. |
| jrs.printer | Specify the printer with which you want to print the output. |
| jrs.print_copies | Specify the number of copies you want to print the output. |
| jrs.print_mediatray | Specify the custom tray you want to put the printing paper. |
| jrs.has_margins | Specify whether you want the printed output to have margins. |
| When jrs.has_margins=true, you must set the following properties: |  |
| jrs.margins_left | Specify the length of the left margin in the printed output. |
| jrs.margins_right | Specify the length of the right margin in the printed output. |
| jrs.margins_top | Specify the length of the top margin in the printed output. |
| jrs.margins_bottom | Specify the length of the bottom margin in the printed output. |
| jrs.margins_unit | Specify the margin unit. Possible values: jrs.margins_unit_mm - Use mm as the margin unit. jrs.margins_unit_inch - Use inch as the margin unit. |
| Publishing to fax properties |  |
| jrs.to_fax | Specify whether to publish the output to fax. |
| jrs.to_fax_quality | Specify the fax quality. Possible values: jrs.to_fax_quality_best - Best fax quality. jrs.to_fax_quality_fast - Fast fax quality. jrs.to_fax_quality_normal - Normal fax quality. |
| jrs.to_fax_is_inclue_cover | Specify whether to send a cover sheet with the fax. |
| jrs.to_fax_date | Specify the date on which you want to send the fax. |
| jrs.to_fax_to | Specify the fax recipient. |
| jrs.to_fax_to_fax_num | Specify the fax number of the recipient. |
| jrs.to_fax_from | Specify the fax sender. |
| jrs.to_fax_from_company_name | Specify the sender's company. |
| jrs.to_fax_from_phone | Specify the sender's phone number. |
| jrs.to_fax_subject | Specify the subject of the fax. |
| jrs.to_fax_comments | Specify the comments of the fax. |
| jrs.to_fax_urgent | Specify whether the fax is urgent. |
| jrs.to_fax_for_review | Specify whether the fax is for review. |
| jrs.to_fax_please_comment | Specify whether you want the recipient to comment on the contents of the fax. |
| jrs.to_fax_please_reply | Specify whether you want a reply for the fax. |
| Publishing to FTP properties |  |
| jrs.to_FTP | Specify whether to publish the output to FTP. |
| jrs.ftp | Specify an FTP site by holding the FTP setting properties. To configure multiple FTP sites, use jrs.ftp0 to specify the first site and jrs.ftp1 to specify the second, and so on. Separate multiple sites by &. Example: jrs.ftp0=jrs.ftpHost%3D192.0.0.1%26jrs.ftpPort%3D21...&jrs.ftp1=jrs.ftpHost%3D192.0.0.2%26jrs.ftpPort%3D22... (%3D represents "=" and %26 represents "&".) |
| jrs.ftpLbl | Specify the label of the FTP server. |
| jrs.ftpHost | Specify the host of the FTP server. |
| jrs.ftpPort | Specify the port of the FTP server. |
| jrs.ftpUn | Specify the username for signing in to the FTP server. |
| jrs.ftpPsd | Specify the password for signing in to the FTP server. |
| jrs.ftpAcct | Specify the account for signing in to the FTP server. |
| jrs.ftpLoc | Specify the remote directory on the FTP server to which you want to publish the files. |
| jrs.ftpHdlCls | Specify the FTP client-end handler class for communicating with the FTP server. Possible values: FTPHandler class name or null which is the default value. |
| jrs.ftpProt | Specify the protocol for communicating with the FTP server. Possible values: 0 - FTP 1 - SFTP 2 - SCP 3 - FTPS |
| jrs.ftpsConType | Specify the connection type of FTPS. Possible values: 0 - EXPLICIT 1 - IMPLICIT |
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
| jrs.ftp_param_validation | Specify the command of checking the validation of FTP connection properties. Possible values: TAG_FTP_CONNECTION_FAILED - Server cannot create the connection because the host name/IP or port is not valid. Possible value: 100 (the only value) TAG_FTP_CONNECTION_IS_OK - The connection is valid. Possible value: 200 (the only value) TAG_FTP_NO_PERMISSION - Server can build the connection, but the username or password is not valid. Possible value: 300 (the only value) TAG_FTP_INVALID_FOLDER - Server can build the connection but cannot find the folder where the output files reside. Possible value: 400 (the only value) |
| jrs.ftpIsDht | Specify whether to export TOC in the HTML output. |
| You can use the following properties to specify the formats in which you want to send the output to the FTP site. For each output file you can further specify its format properties. |  |
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
| Notification properties |  |
| jrs.notification_emails | Specify the email notification list for successful/failed scheduled tasks. |
| jrs.success_notify | Specify to send email notification for successful reports. |
| jrs.fail_notify | Specify to send email notification for failed reports. |
| Time condition properties |  |
| jrs.timezone | Specify the time zone. Possible values: time zone ID strings of Java. The default is current locale. |
| jrs.launch_type | Specify to run a report immediately, at a specific time, or periodically. Possible values: 0 - Immediately 1 - At a specified date and time 8 - Periodically |
| Properties for a specific date and time (jrs.launch_type=1) |  |
| jrs.exe_date | Specify a date. |
| jrs.exe_year | Specify the year. Four digits. |
| jrs.exe_month | Specify the month. Possible values: 0 to 11. 0 is January, 1 is February, ..., and 11 is December. |
| jrs.exe_day | Specify a day number. |
| jrs.exe_hour | Specify an hour number (when jrs.is_hourly is false). |
| jrs.exe_min | Specify a minute number (when jrs.is_hourly is false). |
| jrs.exe_sec | Specify a second number (when jrs.is_hourly is false). |
| Properties for periodical time (jrs.launch_type=8) |  |
| jrs.is_after | Specify whether to run the report after the specified date and time. If the value is true, use the properties for a specific time to define the start time of the whole periodical time. |
| jrs.is_before | Specify whether to run the report before the specified date and time. If the value is true, specify the specified time using the jrs.cease_* properties. |
| jrs.cease_year | Specify the year. Four digits. |
| jrs.cease_month | Specify the month. Possible values: 0 to 11. 0 is January, 1 is February, ..., and 11 is December. |
| jrs.cease_day | Specify a day number. |
| jrs.cease_hour | Specify an hour number (when jrs.is_hourly is false). |
| jrs.cease_min | Specify a minute number (when jrs.is_hourly is false). |
| jrs.cease_sec | Specify a second number (when jrs.is_hourly is false). |
| jrs.days_id | Specify whether you want to run the report daily, weekly, or monthly. Possible values: 0 - Daily 1 - Weekly 2 - Monthly |
| Properties for daily (jrs.days_id=0) |  |
| jrs.is_weekday | Specify whether to run the report on each weekday (Monday to Friday). |
| jrs.day | Specify to run the report per a specified number of days (when jrs.is_weekday is false). For example, if you set the value to 1, the report will run once every day. If you set it to 2, the report will run once every 2 days. Possible values: 1 to 999 days |
| Properties for weekly (jrs.days_id=1) |  |
| jrs.week | Specify to run the report per a specified number of weeks. Possible values: 1 to 99 weeks |
| jrs.weekdays | Specify to run the report on the specified days of the week. Possible values: A digit string. {0, 1, 2, 3, 4, 5, 6}. 0 is Sunday, 1 is Monday, ..., and 6 is Saturday. Example: jrs.weekdays=05 means running on Sunday and Friday. |
| Properties for monthly (jrs.days_id=2) |  |
| jrs.is_day | Specify whether to run the report on the xth day of the month. |
| jrs.day | Specify to run the report on the xth day of the month (when jrs.is_day is true). Possible values: 1 to 31 |
| jrs.week | Specify to run the report on the xth week of the month (when jrs.is_day is false). Possible values: 0 - The first week 1 - The second week 2 - The third week 3 - The fourth week 4 - The last week |
| jrs.weekday | Specify to run the report on the specified day of the week (jrs.is_day is false). Possible values: 1 to 7. 1 is Sunday, 2 is Monday, ..., and 7 is Saturday. |
| jrs.month | Specify to run the report per a specified number of months. Possible values: 1 to 6 months. |
| Properties for a specific time |  |
| jrs.hour | Specify to run the report at a specific hour of the day. |
| jrs.min | Specify to run the report at a specific minute of the hour. |
| jrs.is_pm | Specify whether the time is PM or AM of the day. |
| Properties for hourly |  |
| jrs.is_hourly | Specify whether to run the report hourly. |
| jrs.hours | Specify to run the report per a specified number of hours. Possible values: 1 to 99 hours |
| jrs.at_min | Specify to run the report at a specific minute of the hour. |
| jrs.is_between | Specify whether to run the report between a period. When the value is true, use Properties for when jrs.is_between=true to define a the period. |
| Properties for minutely |  |
| jrs.is_minutely | Specify whether to run the report minutely. The property jrs.is_hourly has the higher priority. If you set both jrs.is_hourly and jrs.is_minutely to true, the report will run hourly. |
| jrs.minutes | Specify to run the report per a specified number of minutes. |
| jrs.is_between | Specify whether to run the report between a period. When the value is true, use Properties for when jrs.is_between=true to define a time duration. |
| Properties for when jrs.is_between=true |  |
| jrs.hour | Specify the start hour of a period. |
| jrs.min | Specify the start minute of a period. |
| jrs.is_pm | Specify whether the start time is PM or AM. |
| jrs.hour2 | Specify the end hour of a period. |
| jrs.min2 | Specify the end minute of a period. |
| jrs.is_pm2 | Specify whether the end time is PM or AM. |

## 
URL Properties for Viewing Reports

| Property | Description |
| --- | --- |
| jrd_filters | Specify the values of on-screen filters. |
| jrs.datasources | Specify the data source. It is a JSON string, with the format: jrs.datasources= { jrs.datasources:[ { "jrs.data_source_name":"xxx", "jrs.connections":[ { "jrs.connection_name":"xxx", "jrs._ds_driver":"xxx", "jrs._ds_url":"xxx", "jrs.ds_user":"xxx", "jrs.ds_pswd":"xxx", "jrs.databases":[ // The database list in the MongoDB connection, which is an array. { "jrs.dbs_catalog-database-name":"xxx", // The database name you defined in the catalog for MongoDB. "jrs.dbs_database-name":"xx", // The new database name you want to use at runtime to replace the original database name you defined in MongoDB APE. "jrs.dbs_collections":[ // The collection list in a MongoDB database, which is an array. { "jrs.dbs_catalog-collection-name":"xxx", // The collection name you defined in the catalog for MongoDB. "jrs.dbs_collection-name":"xxx" // The new collection name you want to use at runtime to replace the original collection name you defined in MongoDB APE. } ] } ] } ] } ] } URL Example: http://localhost:8888/jinfonet/tryView.jsp?…&jrs.datasources={jrs.datasources:[{"jrs.data_source_name":"xxx","jrs.connections":[{"jrs.connection_name":"xxx","jrs._ds_driver":"xxx","jrs._ds_url":"xxx","jrs.ds_user":"xxx","jrs.ds_pswd":"xxx","jrs.databases":[{"jrs.dbs_catalog-database-name":"xxx","jrs.dbs_database-name":"xx","jrs.dbs_collections":[{"jrs.dbs_catalog-collection-name":"xxx","jrs.dbs_collection-name":"xxx"}]}]}]}]}… |
| jrs.file | Specify the file name of the report. |
| jrs.hist_file | Specify the file name of the report with its real path in the \history folder, for example, 1%2fadmin567625353%2f2109098280.pdf. |
| jrs.resource_path | Specify the path of the resource in the server resource tree, for example, /SampleReports. |
| jrs.result | Specify the name of the report with its path in the server resource tree, for example, /SampleReports/Payroll Report. |
| jrs.rst_version | Specify the version number of the report. |
| jrs.ver_suff | Specify the suffix of the report file. Possible values: .rst - The suffix of Logi Report Result (for page report) or Web Report Result (for web report). .html - The suffix of the HTML file. .pdf - The suffix of the PDF file. .txt - The suffix of the Text file. .xls - The suffix of the Excel file. .ps - The suffix of the PostScript file. .rtf - The suffix of the RTF file. .xml - The suffix of the XML file. |
| jrs.version_number | Specify the version number of the resource, for example, 1. |
| type | Specify the type of the report. Possible values: rstfile - Get the result versions of a specific report. rstdoc - Get the versions of a specific result. |
| jrs.bookmark | Specify the name of a bookmark that you saved for the web report to run the bookmark. |
| jrs.is_pls_result=true | Apply cached report bursting to view the report. |
| jrs.profile | Specify the name of a Web Report Studio profile, Page Report Studio profile, or JDashboard profile that server administrators created. For more information, see Configuring Server Profile. |

## 
URL Properties for Adding and Deleting Users/Roles/Groups

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
| passwordLife | Specify the validity period of the user password. Possible values: neverExpire Set passwordLife=neverExpire if you don't want the user password to expire. expire Set passwordLife=expire, and then specify the number of days during which the password is valid, by setting the expireTime property. |
| expireTime | Specify the number of days during which the user password is valid. |
| enableBlank | Specify the length of the user password. Possible values: blank Set enableBlank=blank if the password can be blank. minValue Set enableBlank=minValue, and then specify the minimum number of characters in the password, by setting the minLength property. |
| minLength | Specify the minimum number of characters in the user password. Possible values: 1 to 20 |
| jrs.privilege_publish_report | Specify whether to grant the user/role/group the ability to publish resources to Report Server. |
| jrs.privilege_access_advanced_properties | Specify whether to grant the user/role/group the ability to view advanced version properties information, such as catalog connections and report related resources. |
| roleName | Specify the name of the role. |
| parentRoles | Specify the parent role for the role. Possible values: An existing role name or "NoneParent" if the role does not have a parent role. |
| groupName | Specify the name of the group. |
| parentGroups | Specify the parent group for the group. Possible values: An existing group name or "NoneParent" if the group does not have a parent group. |
