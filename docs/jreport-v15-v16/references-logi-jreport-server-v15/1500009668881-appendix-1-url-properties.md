---
title: "Appendix 1: URL Properties"
id: 1500009668881
section: "References Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009668881-Appendix-1-URL-Properties
updated_at: 2021-07-24T20:55:24Z
---

# Appendix 1: URL Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644222-Appendices)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009668861-Appendix-2-Properties-in-server-properties)

# Appendix 1: URL Properties

This appendix presents the basic properties concerned with working on Logi JReport Server using URL. When you run and schedule reports via URL, you also need to specify the properties for each report format. For details about those format properties, refer to the [Logi JReport Javadoc](http://www.jinfonet.com/kbase/jreport15/api/jet/cs/util/APIConst.html).

Below is a list of the sections covered in this topic:

* [General Properties for Running and Scheduling Reports](#General)
* [Properties for Scheduling Reports](#Schedule)
* [Properties for Viewing Report Results](#Result)
* [Properties for Adding and Deleting Users/Roles](#User)

## General Properties for Running and Scheduling Reports

| Property | Description |
| --- | --- |
| jrs.path | Specifies a path or a resource name with full path.  Example: /SampleReports, or /SampleReports/InvoiceReport.cls |
| jrs.catalog | Specifies the catalog name with full path. Example: /SampleReports/SampleReports.cat, or %2fSampleReports%2fSampleReports.cat |
| jrs.report | Specifies the report name with full path. Example: /SampleReports/Employee Information.cls, or %2fSampleReports%2fEmployee Information.cls |
| jrs.result\_type | Specifies which format to run a report to.  Possible values: {0, 8}  * 0 - To Applet * 1 - To HTML * 2 - To PDF * 3 - To TEXT * 4 - To Excel * 5 - To PostScript * 6 - To Rich Text Format * 7 - To XML * 8 - To Page Report Studio (for page reports) * 8 - To Web Report Studio (for web reports) |
| jrs.param$+PARAMETER\_NAME | Specifies parameter values for running the report. Use *jrs.param$NAME=VALUE* to set parameter values of the report, where, NAME is the parameter name and VALUE is the URL-encoded parameter value. For example: jrs.param$TERMSDAYS=30&jrs.param$PTODAY=May 21, 1998.  When specifying values for a multi-value parameter, you need to add *\_isMultiple\_jrs.param$NAME=true* before the parameter values to declear that the parameter supports multiple values. For example: &\_isMultiple\_jrs.param$PM=true&jrs.param$PM=3&jrs.param$PM=16. |
| jrs.param\_values | Specifies parameter values for running the report. This is the escaped string of the parameter values of the report. Format: PARAMETER\_NAME=VALUE,PARAMETER\_NAME=VALUE,...  Examples:  * jrs.param\_values=PTODAY%3dMay%2021%5c%2c%201998%2cTERMSDAYS%3d30 (original: PTODAY=May 21\, 1998,TERMSDAYS=30) * jrs.param\_values=STARTDATE%3d1998-05-10%2cENDDATE%3d1998-07-10 (original: STARTDATE=1998-05-10,ENDDATE=1998-07-10) |
| jrs.param\_page | Specifies whether to show the parameter dialog for specifying parameter values that are not provided by jrs.param$ in the URL. Such parameter dialogs include the one displayed during report running and those brought by actions that lead to the change of parameters after the report is rendered in Page Report Studio, for example, the actions such as inserting a formula with a new parameter, running a master/detail report, and so on. However, the dialog displayed via Menu > Report > Change Parameters is not affected by this property, because the dialog is to display all the parameters of the report. When it is true and the value of a middle level cascading parameter (including old style cascading parameter) is provided, the parameter dialog only shows the lower level parameters. When it is false, no involved parameter dialog will pop up during the whole report running. The given parameter values and the default values of the other parameters will be used to run the report. The default value of the property is true. |
| jrs.rpt\_language | Specifies the language in which to generate the report. The value you set for this command should be consistent with the language and country code part of the language property file name. For example, if the language property file is named ReportName\_de\_DE.properties, you should set this command as jrs.rpt\_language=de\_DE. You can also use jrs.rpt\_language=de&jrs.rpt\_country=DE to achieve the same goal. If you only want to use jrs.rpt\_language=de, then you will have to rename the language property file to ReportName\_de.properties. Examples:  * `http://localhost:8888/jinfonet/tryView.jsp?jrs.report=%2fSampleReports%2fEmployee Information.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=2&jrs.enable_nls=true&jrs.rpt_language=de_DE` * `http://localhost:8888/webos/app/pagestudio/run.jsp?jrs.catalog=/SampleReports/SampleReports.cat&jrs.report=/SampleReports/Employee Information.cls&jrs.enable_nls=true&jrs.rpt_language=de&jrs.rpt_country=DE` * If you change Employee Information\_de\_DE.properties to Employee Information\_aaa.properties in Employee Information.cls's real path folder, for example `C:\Logi JReport\Server\history\1\Logi JReport_System_User457188937`, then you can use the following URL to run NLS report: `http://localhost:8888/webos/app/pagestudio/run.jsp?jrs.catalog=/SampleReports/SampleReports.cat&jrs.report=/SampleReports/Employee Information.cls&jrs.enable_nls=true&jrs.rpt_language=aaa` |
| jrs.rpt\_encoding | Specifies the encoding in which to generate the report. |
| jrs.has\_style | Specifies whether or not to enable the style group that has been set for the report. |
| jrs.style\_group | Specifies the style group which could be StyleName<CSS> or StyleName.css. StyleName<CSS> is CSS Style Sheet whose name is StyleName in the Logi JReport resources system. It may come from a .css file on disk or be created from the CSS editor. StyleName.css is a \*.css file on disk which may not follow the CSS style rule and therefore not work. It is recommended to use jrs.style\_group=StyleName<CSS> in case StyleName.css fails though both can work most of the time. |
| jrs.db\_user | Specifies the new database user ID if you do not want to use the default DB user ID stored in the catalog. |
| jrs.db\_pswd | Specifies the new database password if you do not want to use the default DB password in the catalog. |
| jrs.jdbc\_url | Specifies the new JDBC URL in the catalog to run a report. |
| jrs.jdbc\_driver | Specifies the new JDBC driver in the catalog to run a report. |
| jrs.wp | Specifies the WHERE portion. For example, a report has a DBField Customer Region, and you want to restrict the field Customer Region to CA in the URL. You can then set a new WHERE portion such as, `"...jrs.result_type=1&jrs.wp=Customers.Region='CA'...".` |
| jrs.named\_wp | Specifies the named WHERE portion that exists in the catalog. |
| jrs.jdbc\_connection\_object | Specifies to dynamically use the user's java.sql.Connection object to run a report. This parameter can be used in methods runReport(...), runReportNotWaitResult(...) and submitScheduledTask(...) of jet.server.api.RptServer. Example: Running a report with user's JDBC connection object by using Logi JReport Server API.    |  | | --- | | ``` //create the java.sql.Connection object. java.sql.Connection myCon = java.sql.DriverManager.getConnection(dbUrl); //set the parameter "jrs.jdbc_connection_object" to run a report. propParams.put("jrs.jdbc_connection_object", myCon); //run the report using this java.sql.Connection object instead of  //the default DB settings in the catalog. rptServer.runReport(userID, catalog, report set, propParams); ``` | |
| jrs.security\_file\_name | Specifies to apply a [security file](https://devnet.logianalytics.com/hc/en-us/articles/1500009674921-Dynamic-Security). When a security file is given, the security definitions in the specified catalog will be replaced by that defined in the security file. |
| jrs.applet\_type | Specifies the Java runtime environment to run applets. Possible values:   * 2 - Java Plug-In 1.2 for Windows * 3 - Java Plug-In 1.3 for Windows |
| jrs.web\_browser | Specifies the web browser for which the HTML result adapts. Possible values:   * 0 - IE or Chrome * 1 - Firefox |
| jrs.timeout\_send\_email | Specifies whether to notify someone of the task status via e-mail if the task has not yet finished running when the task duration is up. Possible values: true/false. The task duration uses the time specified by jrs.report\_timeout in the URL. If there is not jrs.report\_timeout, the time specified by web.timeouts.report\_wait in the server.properties file in `<install_root>\bin` will be used. |
| jrs.report\_timeout | Specifies a time duration in seconds for a scheduled report running task. |
| jrs.mailto | Specifies the address you want to send the e-mail to. |
| jrs.mailsubject | Specifies the subject of the e-mail. |
| jrs.mailcomments | Specifies the comments to the e-mail contents. |
| jrs.mailfrom | Specifies the e-mail address of the sender. |
| jrs.timeout\_sendmail\_message | Specifies the contents of the e-mail. |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Properties for Scheduling Reports

| Property | Description |
| --- | --- |
| General properties | | | |
| jrs.task\_class | Specifies the class name of the task.  Possible values:  * jet.server.schedule.jrtasks.UpdateRptTask * jet.server.schedule.jrtasks.PublishToDiskTask * jet.server.schedule.jrtasks.SendJRMailTask * jet.server.schedule.jrtasks.SendMailTask * jet.server.schedule.jrtasks.PrintRptTask |
| jrs.has\_task\_listener | Specifies whether or not to implement TaskListener. |
| jrs.task\_listener\_class | Specifies the user's Java class name which implements the TaskListener (jrs.task\_listener\_class). |
| jrs.task\_id | Specifies the task ID of a scheduled task. This property is unnecessary if a new schedule is submitted. |
| jrs.mail\_to\_referuser | Specifies whether or not to send mails to each user who is authorized to view a report with cached report bursting. |
| jrs.is\_bursting\_task | Indicates it is to schedule a bursting report task. |
| jrs.bursting\_schema$Schema\_Name | Specifies the names of the schemes to schedule. |
| Publishing to the versioning system properties | | | |
| jrs.to\_version | Specifies whether to publish the report result to the versioning system. |
| jrs.to\_version\_rst | Specifies whether to publish page report to a Logi JReport result file or publish web report to a static web report result file (WST file). You can further specify the result properties. See the Logi JReport Javadoc for details about these properties. |
| jrs.to\_version\_rsd | Specifies whether to publish the report to page report result. You can further specify the result properties. See the Logi JReport Javadoc for details about these properties. |
| jrs.to\_version\_html | Specifies whether to publish the report result to the versioning system in HTML format. You can further specify the format properties. See the Logi JReport Javadoc for details about these properties. |
| jrs.to\_version\_pdf | Specifies whether to publish the report result to the versioning system in PDF format. You can further specify the format properties. See the Logi JReport Javadoc for details about these properties. |
| jrs.to\_version\_excel | Specifies whether to publish the report result to the versioning system in Excel format. You can further specify the format properties. See the Logi JReport Javadoc for details about these properties. |
| jrs.to\_version\_txt | Specifies whether to publish the report result to the versioning system in Text format. You can further specify the format properties. See the Logi JReport Javadoc for details about these properties. |
| jrs.to\_version\_rtf | Specifies whether to publish the report result to the versioning system in RTF format. You can further specify the format properties. See the Logi JReport Javadoc for details about these properties. |
| jrs.to\_version\_xml | Specifies whether to publish the report result to the versioning system in XML format. You can further specify the format properties. See the Logi JReport Javadoc for details about these properties. |
| jrs.to\_version\_ps | Specifies whether to publish the report result to the versioning system in PostScript format. You can further specify the format properties. See the Logi JReport Javadoc for details about these properties. |
| jrs.archive\_location | Specifies the location for the saved report result version. Possible values:   * 0 - Specifies to save the report result version to the built-in version folder. Not supported for [organization users](https://devnet.logianalytics.com/hc/en-us/articles/1500009675081-Multi-tenancy-Supported-via-Organizations) when the report is from the Public Reports folder. * 1 - Specifies to save the report result version to the My Reports folder. You can then use jrs.archive\_my\_destination to specify a version name with the path in the My Reports folder. * 2 - Specifies to save the report result version to the Public Reports folder. You can then use jrs.archive\_public\_destination to specify a version name with the path in the Public Reports folder. Not supported for organization users. |
| jrs.enable\_archive\_policy | Specifies whether to apply an archive policy to the report result version. |
| jrs.archive\_new\_version | Specifies how to archive the new version. Possible values:   * true - Specifies to use multiple versions for the report result. You can then use jrs.maxversion to specify the maximum number of versions that will be listed in the version table of the report result. 0 means that the version number is unlimited. * false - Specifies to replace the old version when a new version is generated. |
| jrs.need\_expire | Specifies whether the report result will be expired. |
| jrs.auto\_delete\_method | Specifies when the report result will be expired and deleted. Set the result to be automatically deleted within one hundred years. If the time you specify exceeds one hundred years, Logi JReport Server will keep the report result forever. Possible values:   * 0 - The report result will be automatically deleted after a specified number of days. You can then use jrs.expire\_days to specify the number of days, for example: `jrs.need_expire=true&jrs.auto_delete_method=0&jrs.expire_days=60`. * 1 -The report result will be automatically deleted after a specified date. You can then use jrs.auto\_delete\_year, jrs.auto\_delete\_month, and jrs.auto\_delete\_date to specify the year, month and date, for example: `jrs.need_expire=true&jrs.auto_delete_method=1&jrs.auto_delete_year=2017&jrs.auto_delete_month=5&jrs.auto_delete_date=16`. |
| jrs.expire\_days | Specifies the number of days a result version will be kept until it expires. The default value is 30. |
| Publishing to the file system properties | | | |
| jrs.to\_disk | Specifies whether or not the report is scheduled for publishing to disk. |
| jrs.to\_rst | Specifies whether to publish page report to a Logi JReport result file or publish web report to a static web report result file (WST file). You can further specify the result properties. See the Logi JReport Javadoc for details about these properties. |
| jrs.to\_rsd | Specifies whether to publish the report to page report result. You can further specify the result properties. See the Logi JReport Javadoc for details about these properties. |
| jrs.to\_html | Specifies whether to publish the report result to the file system in HTML format. You can further specify the format properties. See the Logi JReport Javadoc for details about these properties. |
| jrs.to\_pdf | Specifies whether to publish the report result to the file system in PDF format. You can further specify the format properties. See the Logi JReport Javadoc for details about these properties. |
| jrs.to\_excel | Specifies whether to publish the report result to the file system in Excel format. You can further specify the format properties. See the Logi JReport Javadoc for details about these properties. |
| jrs.to\_text | Specifies whether to publish the report result to the file system in Text format. You can further specify the format properties. See the Logi JReport Javadoc for details about these properties. |
| jrs.to\_rtf | Specifies whether to publish the report result to the file system in RTF format. You can further specify the format properties. See the Logi JReport Javadoc for details about these properties. |
| jrs.to\_xml | Specifies whether to publish the report result to the file system in XML format. You can further specify the format properties. See the Logi JReport Javadoc for details about these properties. |
| jrs.to\_ps | Specifies whether to publish the report result to the file system in PostScript format. You can further specify the format properties. See the Logi JReport Javadoc for details about these properties. |
| jrs.to\_disk\_xxx\_path\_type | Specifies where to publish the report result in xxx format: to the server resource tree or to the server disk path.  Possible values: {0, 1}  * 0 - Publishes to the Logi JReport Server resource tree. * 1 - Publishes to a real disk path. |
| jrs.xxx\_dir | Specifies the path for the published xxx format file. |
| jrs.xxx | Specifies the file name for the published xxx format file. |
| Publishing to e-mail properties | | | |
| jrs.jrmail + NUMBER | Contains specifications (Logi JReport mail properties) of one send-mail task for a report. |
| jrs.csmail + NUMBER | Contains specifications (Logi JReport mail properties) of one send-mail task for sending an e-mail with or without an attachment. This property is used via URL or via invoking Server API. |
| jrs.mailto | Specifies the mail address. |
| jrs.mailcc | Specifies the mail address to be carbon copied to. |
| jrs.mailbcc | Specifies the mail address to be blind carbon copied to. |
| jrs.mailsubject | Specifies the subject of the e-mail. |
| jrs.mailcomments | Specifies the comment of the e-mail. |
| jrs.mailformat | Specifies the mail format. Possible values: {0, 1, 2, 3, 4, 6, 7, 8, 9, 11}  * 0 - E-mail Result in HTML E-mail Format * 1 - E-mail Result in Plain Text E-mail Format * 2 - Attachment in HTML Format * 3 - Attachment in PDF Format * 4 - Attachment in Logi JReport Result Format (for page reports) * 4 - Attachment in Web Report Result Format (for web reports) * 6 - Attachment in PostScript Format * 7 - Attachment in Excel Format * 8 - Attachment in RTF Format * 9 - Attachment in XML Format * 11 - Attachment in Text Format   When sending the report result as an attachment file, you need to specify a file name using jrs.mailattach + NUMBER. You can further specify format properties for the attachment file. See the Logi JReport Javadoc for details about these properties. |
| jrs.mailcompress | Specifies whether to enable Java archive compress. |
| jrs.mailattach + NUMBER | Specifies the attached file for this mail. You can attach multiple files with one mail. Possible values: The attached file name. |
| jrs.mailencoding | Specifies the encoding of the mails.  Possible values: UTF-8, UTF-16, ISO8859-1 and so on. **Note:** jrs.mailencoding is used to specify the mail encoding in the URL. When sending mails by RMI API, sometimes, wrong characters may be returned in the mail. In order to avoid such problems, specify the same correct value of -DLogi JReport.url.encoding on both the server and RMI client side. For example, your web application calls Logi JReport Server (standalone) via the RMI function from WebSphere, and UTF-8 (use UTF-8 rather than UTF8) will be used as the mail encoding, do as follows:  * Specify -DLogi JReport.url.encoding=UTF-8 for both JVM running Logi JReport Server and WebSphere. * Specify jrs.mailencoding=UTF-8. |
| Publishing to a printer properties | | | |
| jrs.if\_print | Specifies whether or not to print the report result. |
| jrs.printer | Specifies the printer with which to print the report result. |
| jrs.print\_copies | Specifies the number of copies to print the report result. |
| jrs.print\_mediatray | Specifies the custom tray to put the printing paper. |
| jrs.has\_margins | Specifies whether or not to have margins in the printed report result. |
| When jrs.has\_margins=true, you must set the following properties: | |
| jrs.margins\_left | Specifies the length of the left margin to print the report result. |
| jrs.margins\_right | Specifies the length of the right margin to print the report result. |
| jrs.margins\_top | Specifies the length of the top margin to print the report result. |
| jrs.margins\_bottom | Specifies the length of the bottom margin to print the report result. |
| jrs.margins\_unit | Specifies the unit to print the report result. Possible values:  * **jrs.margins\_unit\_mm**  Specifies mm as the margin unit. * **jrs.margins\_unit\_inch**  Specifies inch as the margin unit. |
| Publishing to fax properties | | | |
| jrs.to\_fax | Specifies whether or not to publish the report result to fax. |
| jrs.to\_fax\_quality | Specifies the fax quality. Possible values:  * **jrs.to\_fax\_quality\_best**  Indicates the best fax quality. * **jrs.to\_fax\_quality\_fast**  Indicates the fast fax quality. * **jrs.to\_fax\_quality\_normal**  Indicates the normal fax quality. |
| jrs.to\_fax\_is\_inclue\_cover | Specifies whether to send a cover sheet with the fax. |
| jrs.to\_fax\_date | Specifies the date on which the fax is to be sent. |
| jrs.to\_fax\_to | Specifies the fax recipient. |
| jrs.to\_fax\_to\_fax\_num | Specifies the fax number of the recipient. |
| jrs.to\_fax\_from | Specifies the fax sender. |
| jrs.to\_fax\_from\_company\_name | Specifies the sender's company. |
| jrs.to\_fax\_from\_phone | Specifies the sender's phone number. |
| jrs.to\_fax\_subject | Specifies the subject of the fax. |
| jrs.to\_fax\_comments | Specifies the comments of the fax. |
| jrs.to\_fax\_urgent | Specifies whether or not the fax is urgent. |
| jrs.to\_fax\_for\_review | Specifies whether or not the fax is for review. |
| jrs.to\_fax\_please\_comment | Specifies whether or not the recipient is required to comment on the content of the fax. |
| jrs.to\_fax\_please\_reply | Specifies whether or not a reply is required for the fax. |
| Publishing to FTP properties | | | |
| jrs.to\_FTP | Specifies whether or not to publish the report result to FTP. |
| jrs.ftp | Specifies an FTP site by holding the FTP setting properties. To configure multiple FTP sites, use jrs.ftp0 to specify the first site and jrs.ftp1 to specify the second, and so on. Multiple sites are separated by &. Examples:  `jrs.ftp=Property1%3DValue1%26Property2%3DValue2...`, here %3D represents "=" and %26 represents "&".  `jrs.ftp0=jrs.ftpHost%3D192.0.0.1%26jrs.ftpPort%3D21%26jrs.ftpUn%3Dtest%26jrs.ftpPsd%3Dtest%26jrs.ftpAcct%3Dtest...&jrs.ftp1=jrs.ftpHost%3D192.0.0.2%26jrs.ftpPort%3D22...` |
| jrs.ftpLbl | Specifies the label of the FTP server. |
| jrs.ftpHost | Specifies the host of the FTP server. |
| jrs.ftpPort | Specifies the port of the FTP server. |
| jrs.ftpUn | Specifies the user name for logging in the FTP server. |
| jrs.ftpPsd | Specifies the password for logging in the FTP server. |
| jrs.ftpAcct | Specifies the account for logging in the FTP server. |
| jrs.ftpLoc | Specifies the remote directory on the FTP server to which the files will be published. |
| jrs.ftpHdlCls | Specifies the FTP client-end handler class for communicating with the FTP server.  Possible values: FTPHandler class name or null which is the default value. |
| jrs.ftpProt | Specifies the protocol for communicating with the FTP server.  Possible values: {0, 1, 2, 3}  * 0 - FTP * 1 - SFTP * 2 - SCP * 3 - FTPS |
| jrs.ftpsConType | Specifies the connection type of FTPS.   Possible values: {0, 1}  * 0 - EXPLICIT * 1 - IMPLICIT |
| jrs.ftpsEnNoSec | Specifies whether to enable falling back to the no-security FTP connection if the explicit FTPS connection is not available. |
| jrs.ftpsKSType | Specifies the keystore type of FTPS. |
| jrs.ftpsKSFile | Specifies the keystore file of FTPS. |
| jrs.ftpsKSPsd | Specifies the keystore password of FTPS. |
| jrs.ftpsKMAlg | Specifies the keymanager algorithm of FTPS. |
| jrs.ftpsSecProt | Specifies the security protocol of FTPS. |
| jrs.ftpsTMAlg | Specifies the trustmanager algorithm of FTPS. |
| jrs.ftpsTransMode | Specifies the transfer mode of FTPS. |
| jrs.ftpsTSType | Specifies the truststore type of FTPS. |
| jrs.ftpsTSFile | Specifies the truststore file name of FTPS. |
| jrs.ftpsTSPsd | Specifies the truststore password of FTPS. |
| jrs.sftpC2SCmpA | Specifies the C2S compression algorithms of SFTP/SCP. |
| jrs.sftpC2SCphA | Specifies the C2S cipher algorithms of SFTP/SCP. |
| jrs.sftpC2SLang | Specifies the C2S language of SFTP/SCP. |
| jrs.sftpC2SMA | Specifies the C2S MAC algorithms of SFTP/SCP. |
| jrs.sftpHKAlgs | Specifies the host key algorithms of SFTP/SCP. |
| jrs.sftpKexAlgs | Specifies the kex algorithms of SFTP/SCP. |
| jrs.sftpKH | Specifies the knownhosts file of SFTP/SCP. |
| jrs.sftpS2CCmpA | Specifies the s2c compression algorithms of SFTP/SCP. |
| jrs.sftpS2CCphA | Specifies the S2C cipher algorithms of SFTP/SCP. |
| jrs.sftpS2CLang | Specifies the S2C language of SFTP/SCP. |
| jrs.sftpS2CMA | Specifies the S2C MAC algorithms of SFTP/SCP. |
| jrs.sftpSHKC | Specifies whether to check the strict host key.  Possible values: {yes, no} |
| jrs.ftp\_param\_validation | Specifies the command of checking the validation of FTP connection options.  Possible values:  * **TAG\_FTP\_CONNECTION\_FAILED**  The connection cannot be created because the host name/IP or port is not valid.  Possible values: {100} (the only value) * **TAG\_FTP\_CONNECTION\_IS\_OK**  The connection is valid.  Possible values: {200} (the only value) * **TAG\_FTP\_NO\_PERMISSION**  The connection can be built but the user name or password is not valid.  Possible values: {300} (the only value) * **TAG\_FTP\_INVALID\_FOLDER**  The connection can be built but the directory where the report result files reside cannot be found.   Possible values: {400} (the only value) |
| jrs.ftpIsDht | Specifies whether to export TOC in the HTML result. |
| The following properties are used to specify in which formats to send the report result file to the FTP site. For each result file you can further specify the format properties. See the Logi JReport Javadoc for details about these properties. | |
| jrs.ftpRst | Specifies whether to send report result in a Logi JReport Result file (for page report) or in web report result (for web report) to the FTP site. |
| jrs.ftpRstFn | Specifies the file name of the Logi JReport Result file (for page report) or of the web report result (for web report). |
| jrs.ftpHtml | Specifies whether to send the report result in an HTML file to the FTP site. |
| jrs.ftpHtmlFn | Specifies the file name of the HTML file. |
| jrs.ftpPdf | Specifies whether to send the report result in a PDF file to the FTP site. |
| jrs.ftpPdfFn | Specifies the file name of the PDF file. |
| jrs.ftpExl | Specifies whether to send the report result in an Excel file to the FTP site. |
| jrs.ftpExlFn | Specifies the file name of the Excel file. |
| jrs.ftpTxt | Specifies whether to send the report result in a Text file to the FTP site. |
| jrs.ftpTxtFn | Specifies the file name of the Text file. |
| jrs.ftpRtf | Specifies whether to send the report result in a RTF file to the FTP site. |
| jrs.ftpRtfFn | Specifies the file name of the RTF file. |
| jrs.ftpXml | Specifies whether to send the report result in an XML file to the FTP site. |
| jrs.ftpXmlFn | Specifies the file name of the XML file. |
| jrs.ftpPs | Specifies whether to send the report result in a PostScript file to the FTP site. |
| jrs.ftpPsFn | Specifies the file name of the PostScript file. |
| Notification properties | | | |
| jrs.notification\_emails | Specifies the e-mail notification list for successful/failed scheduled tasks. |
| jrs.success\_notify | Specifies to send e-mail notification for successful reports. |
| jrs.fail\_notify | Specifies to send e-mail notification for failed reports. |
| Time condition properties | | | |
| jrs.timezone | Specifies the timezone. Possible values: timezone ID strings of java default is current locale. |
| jrs.launch\_type | Specifies to run a report immediately, at a specific time or periodically.  Possible values: {0, 1, 8}  * 0 - Immediately * [1 - At a specified date and time](#DateTime) * [8 - Periodically](#Periodical) |
| **Properties for a specific date and time (jrs.launch\_type=1)** | |
| jrs.exe\_date | Specifies a date. |
| jrs.exe\_year | Specifies a year of 4 numbers. |
| jrs.exe\_month | Specifies a month, for example, May. Possible values: 0 to 11. 0 is January, 1 is February, ..., and 11 is December. |
| jrs.exe\_day | Specifies a day number.  Possible values: 1 to 31 |
| jrs.exe\_hour | Specifies an hour number (when jrs.is\_hourly is false). Possible values: 0 to 23 |
| jrs.exe\_min | Specifies a minute number (when jrs.is\_hourly is false). Possible values: 0 to 59 |
| jrs.exe\_sec | Specifies a second number (when jrs.is\_hourly is false). Possible values: 0 to 59 |
| **Properties for periodical time (jrs.launch\_type=8)** | |
| jrs.is\_after | Specifies whether to run after the specified date and time, also the start time of the whole periodical time. If the value is true, use [properties for a specific time](#Time) to define the specific time. |
| jrs.is\_before | Specifies whether to run before the specified date and time. If the value is true, the specified time is represented by the jrs.cease\_\* properties. |
| jrs.cease\_year | Specifies a year of 4 numbers. |
| jrs.cease\_month | Specifies a month.  Possible values: 0 to 11. 0 is January, 1 is February, ..., and 11 is December. |
| jrs.cease\_day | Specifies a day number.  Possible values: 1 to 31 |
| jrs.cease\_hour | Specifies an hour number (when jrs.is\_hourly is false). Possible values: 0 to 23 |
| jrs.cease\_min | Specifies a minute number (when jrs.is\_hourly is false). Possible values: 0 to 59 |
| jrs.cease\_sec | Specifies a second number (when jrs.is\_hourly is false). Possible values: 0 to 59 |
| jrs.days\_id | Specifies whether the schedule will run daily, weekly or monthly.  Possible values: {0, 1, 2}  * [0 - Daily](#Daily) * [1 - Weekly](#Weekly) * [2 - Monthly](#Monthly) |
| **Properties for daily (jrs.days\_id=0)** | |
| jrs.is\_weekday | Specifies whether to run a report on each weekday (Monday to Friday). |
| jrs.day | Specifies that the report will run once every how many days specified here (when jrs.is\_weekday is false). For example, if the value is set to 1, the report will run once everyday. If the value is set to 2, the report will run once every 2 days. Possible values: 1 to 999 days |
| **Properties for weekly (jrs.days\_id=1)** | |
| jrs.week | Specifies that the report will run once every how many weeks specified here. Possible values: 1 to 99 weeks |
| jrs.weekdays | Specifies on which days to run in a week. Possible values: A digit string. {0, 1, 2, 3, 4, 5, 6}. 0 is Sunday, 1 is Monday, ..., and 6 is Saturday. Example: jrs.weekdays=05 means running on Sunday and Friday. |
| **Properties for monthly (jrs.days\_id=2)** | |
| jrs.is\_day | Specifies whether to run on the xth day in a month. |
| jrs.day | Specifies to run on the xth day in a month (when jrs.is\_day is true). Possible values: 1 to 31 |
| jrs.week | Specifies to run on the xth week in a month (when jrs.is\_day is false).  Possible values: {0, 1, 2, 3, 4}  * 0 - The first week * 1 - The second week * 2 - The third week * 3 - The fourth week * 4 - The last week |
| jrs.weekday | Specifies to run on which day in the week (jrs.is\_day is false).  Possible values: {1, 2, 3, 4, 5, 6, 7}. 1 is Sunday, 2 is Monday, ..., and 7 is Saturday. |
| jrs.month | Specifies that the report will run once every how many months specified here. Possible values: 1 to 6 months. |
| **Properties for a specific time** | |
| jrs.hour | Specifies to run at which hour in a day.  Possible values: 1 to 12 |
| jrs.min | Specifies to run at which minute in an hour.  Possible values: 0 to 59 |
| jrs.is\_pm | Specifies whether the time is PM or AM in a day. |
| **Properties for hourly** | |
| jrs.is\_hourly | Specifies whether to run the schedule every hour. |
| jrs.hours | Specifies that the report will run once every how many hours specified here. Possible values: 1 to 99 hours |
| jrs.at\_min | Specifies to run at which minute in an hour. Possible values: 0 to 59 |
| jrs.is\_between | Specifies whether to run between the start time and the finish time. When the value is true, see [Properties for when jrs.is\_between=true](#jrsisbetween) to define a time duration. |
| **Properties for minutely** | |
| jrs.is\_minutely | Specifies whether to run the schedule every minute.  **Note:** The property jrs.is\_hourly has the higher priority. That is, if you set both jrs.is\_hourly and jrs.is\_minutely to true, the schedule will run the task based on hour. |
| jrs.minutes | Specifies that the report will run once every how many minutes specified here. |
| jrs.is\_between | Specifies whether to run between the start time and the finish time. When the value is true, see [Properties for when jrs.is\_between=true](#jrsisbetween) to define a time duration. |
| **Properties for when jrs.is\_between=true** | |
| jrs.hour | Specifies the start hour of a period of time.  Possible values: 1 to 12 |
| jrs.min | Specifies the start minute of a period of time.  Possible values: 0 to 59 |
| jrs.is\_pm | Specifies whether the start time is PM or AM. |
| jrs.hour2 | Specifies the finish hour of a period of time.  Possible values: 1 to 12 |
| jrs.min2 | Specifies the finish minute of a period of time.  Possible values: 0 to 59 |
| jrs.is\_pm2 | Specifies whether the finish time is PM or AM. |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Properties for Viewing Report Results

| Property | Description |
| --- | --- |
| jrs.file | Specifies the file name of the result. |
| jrs.hist\_file | Specifies the file name of the result with its real path in the `<install_root>\history` folder, for example, 1%2fadmin567625353%2f2109098280.pdf. |
| jrs.resource\_path | Specifies the path of the resource in the server resource tree, for example, /SampleReports. |
| jrs.result | Specifies the name of the result with its path in the server resource tree, for example, /SampleReports/InvoiceReport. |
| jrs.rst\_version | Specifies the version number of the result. |
| jrs.ver\_suff | Specifies the suffix of the result file. Possible values:   * .rst - The suffix of Logi JReport result (for page report) or web report result (for web report). * .html - The suffix of the HTML result file. * .pdf - The suffix of the PDF result file. * .txt - The suffix of the Text result file. * .xls - The suffix of the Excel result file. * .ps - The suffix of the PostScript result file. * .rtf - The suffix of the RTF result file. * .xml - The suffix of the XML result file. |
| jrs.version\_number | Specifies the version number of the resource, for example, 1. |
| type | Specifies the type of the result. Possible values:   * rstfile - Gets the result versions attached to a specific report. * rstdoc - Gets the versions of a specific result. |
| jrs.is\_pls\_result=true | Applies [cached report bursting](https://devnet.logianalytics.com/hc/en-us/articles/1500009674901-Cached-Report-Bursting) to view the result. |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Properties for Adding and Deleting Users/Roles

| Property | Description |
| --- | --- |
| currentEditRealm | Specifies the security realm in which the user/role is. |
| user | Specifies the name of the user. |
| fullName | Specifies the full name of the user. |
| email | Specifies the e-mail address of the user. |
| password | Specifies the password of the user. |
| confirmPassword | Confirms the password. |
| accountDisabled=ON | Disables the user account for the time being. |
| passwordLife | Specifies the validity period of the password.  Possible values:  * **neverExpire**  When *passwordLife=neverExpire*, the password will not expire. * **expire**  When *passwordLife=expire*, you can specify   a period of time during which the password is valid, by setting the expireTime property. |
| expireTime | Specifies a period of time in days during which the password is valid. |
| enableBlank | Specifies the length of the password.  Possible values:  * **blank**  When *enableBlank=blank*, the password can be blank. * **minValue**  When *enableBlank=minValue*, you can specify the minimum number of characters that can be used in the password, by setting the minLength property. |
| minLength | Specifies the minimum number of characters that can be used in the password.  Possible values: 1 to 20 |
| roleName | Specifies the name of the role. |
| parentRoles | Specifies the parent role for the role.  Possible values: An existing role name or "NoneParent" which means that the role does not have a parent role. |
| description | Specifies the description for the role. |
| jrs.privilege\_publish\_report | Specifies whether to grant the user/role the ability to publish resources to Logi JReport Server. |
| jrs.privilege\_access\_advanced\_properties | Specifies whether to grant the user/role the ability to view advanced version properties information, such as catalog connections and report related resources. |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644222-Appendices)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009668861-Appendix-2-Properties-in-server-properties)
