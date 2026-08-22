---
title: "Scheduling Reports via URL"
id: 1500009778901
section: "Working on Logi Report Server via URL Logi Report Server v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009778901-Scheduling-Reports-via-URL
updated_at: 2021-07-24T00:47:26Z
---

# Scheduling Reports via URL

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750362-Running-Reports-via-URL)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750322-Creating-Reports-via-URL)

# Scheduling Reports via URL

You can use the **submitSchedPage.jsp** to schedule reports via URL in a web browser, and should call the method **jrs.submit\_schedule** in the URL. This topic describes how you can schedule report results to different locations.

The following is a description of this method.

* **Description:** Submits a scheduled task to Logi Report Server. If the report has no parameters, then it directly run the URL. If the report has parameters and no parameter specified in the URL or the parameters provided in the URL fail to include all necessary parameters, the server then returns the parameter dialog box for specifying parameter values.
* **HTTP Method:** GET/POST.
* **Response:** Returns the ID of the schedule task, or a message if the task fails.

A schedule contains two kinds of properties. The first is about time information and the second is about task information. For more information, see [Appendix 1: URL Properties for Running, Scheduling, and Viewing Reports via URL](https://devnet.logianalytics.com/hc/en-us/articles/1500009743382-Appendix-1-URL-Properties-for-Running-Scheduling-and-Viewing-Reports-via-URL).

The following are some specific examples on how to schedule a report via URL. We use the report ABC.cls with the catalog /SampleReports/SampleReports.cat in these examples.

**Publishing to the versioning system immediately**

To publish the report to the versioning system in PDF format immediately, the URL used for this task could be as follows:  
  
`http://localhost:8888/jinfonet/submitSchedPage.jsp?jrs.cmd=jrs.submit_schedule&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.task_class=jet.server.schedule.jrtasks.PublishRptTask&jrs.launch_type=0&jrs.param$P_StartDate=2016-01-01&jrs.param$p_EndDate=2017-12-31&jrs.uid=admin&jrs.to_version_pdf=true&jrs.to_version=true&jrs.report=%2fSampleReports%2fABC.cls`

If you want to publish the report to other formats, you can refer to the examples above, but you will need to modify the property *jrs.to\_version\_pdf=true* to suit the particular format that the report will be published to. For example, if you want to publish the report to Excel, you will need to change the property to *jrs.to\_version\_excel=true*.

**Publishing to the versioning system periodically**

To publish the report to the versioning system periodically, the URL used for this task could be as follows:

`http://localhost:8888/jinfonet/submitSchedPage.jsp?jrs.cmd=jrs.submit_schedule&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.hour2=5&jrs.task_class=jet.server.schedule.jrtasks.PublishRptTask&jrs.to_version=true&jrs.to_version_html=true&jrs.is_between=true&jrs.is_weekday=false&jrs.launch_type=8&jrs.min2=0&jrs.is_pm=false&jrs.hour=9&jrs.is_pm2=true&jrs.param$P_StartDate=2016-01-01&jrs.param$p_EndDate=2017-12-31&jrs.uid=admin&jrs.hours=1&jrs.is_hourly=true&jrs.at_min=0&jrs.days_id=0&jrs.day=1&jrs.timezone=CTT&jrs.min=0&jrs.expire_days=30&jrs.report=%2fSampleReports%2fABC.cls&jrs.rpt_language=en&jrs.report_sheet$Report=true&jrs.schedule_name=periodicalTask`

**Publishing to the versioning system at a specific time**

To publish the report to the versioning system at 12:00:00 CST, December 1, 2018, the URL used for this task could be as follows:

`http://localhost:8888/jinfonet/submitSchedPage.jsp?jrs.cmd=jrs.submit_schedule&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.task_class=jet.server.schedule.jrtasks.PublishRptTask&jrs.to_version=true&jrs.to_version_rst=true&jrs.launch_type=1&jrs.param$P_StartDate=2016-01-01&jrs.param$p_EndDate=2017-12-31&jrs.uid=admin&jrs.exe_day=1&jrs.exe_month=12&jrs.exe_hour=12&jrs.exe_min=00&jrs.exe_year=2018&jrs.expire_days=30&jrs.report=%2fSampleReports%2fABC.cls&jrs.report_sheet$Report=true&jrs.schedule_name=atTimeTask`

**Publishing to the versioning system immediately and notifying others of success or failure**

To publish the report to the versioning system immediately, and notify the user support1, support2, and support3 of success or failure, the URL used for this task could be as follows:

`http://localhost:8888/jinfonet/submitSchedPage.jsp?jrs.cmd=jrs.submit_schedule&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.task_class=jet.server.schedule.jrtasks.PublishRptTask&jrs.launch_type=0&jrs.param$P_StartDate=2016-01-01&jrs.param$p_EndDate=2017-12-31&jrs.uid=admin&jrs.expire_days=30&jrs.report=%2fSampleReports%2fABC.cls&jrs.to_version=true&jrs.to_version_rst=true&jrs.success_notify=true&jrs.fail_notify=true&jrs.notification_emails=To%3A+person1@company.com%0D%0ACc%3A+person2@company.com%0D%0ABcc%3A+person3@company.com%0D%0A`

**Publishing to the file system immediately**

To publish the report to the file system immediately, the URL used for this task could be as follows:

* **To RST**  
  `http://localhost:8888/jinfonet/submitSchedPage.jsp?jrs.cmd=jrs.submit_schedule&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.task_class=jet.server.schedule.jrtasks.PublishRptTask&jrs.launch_type=0&jrs.param$P_StartDate=2016-01-01&jrs.param$p_EndDate=2017-12-31&jrs.uid=admin&jrs.to_disk_rst_path_type=1&jrs.rst_dir=C:\&jrs.to_disk=true&jrs.to_rst=true&jrs.rst=ABC.rst&jrs.report=%2fSampleReports%2fABC.cls&`
* **To PDF**  
  `http://localhost:8888/jinfonet/submitSchedPage.jsp?jrs.cmd=jrs.submit_schedule&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.task_class=jet.server.schedule.jrtasks.PublishRptTask&jrs.launch_type=0&jrs.param$P_StartDate=2016-01-01&jrs.param$p_EndDate=2017-12-31&jrs.uid=admin&jrs.to_disk_pdf_path_type=1&jrs.pdf_dir=C:\&jrs.to_disk=true&jrs.to_pdf=true&jrs.pdf=ABC.pdf&jrs.report=%2fSampleReports%2fABC.cls&`

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)If you want to publish a report to a disk path, for example, jrs.rst\_dir=C:\, you can do the same as the example described above. If you want to publish a report to a resource tree, for example, jrs.rst\_dir=%2fSampleReports, you can omit this property *&jrs.to\_disk\_pdf\_path\_type=1* in the above example and replace jrs.pdf\_dir=C:\ with jrs.rst\_dir=%2fSampleReports. Here **SampleReports** is the resource path.

**Publishing to e-mail immediately**

To publish the report to e-mail immediately, the URL used for this task could be as follows:

`http://localhost:8888/jinfonet/submitSchedPage.jsp?jrs.cmd=jrs.submit_schedule&jrs.catalog=/SampleReports/SampleReports.cat&jrs.report=/SampleReports/ABC.cls&jrs.task_class=jet.server.schedule.jrtasks.PublishRptTask&jrs.to_mail=true&jrs.jrmail0=jrs.mailto%3dperson@company.com%26jrs.mailsubject%3dreport&jrs.launch_type=0&jrs.param$P_StartDate=2016-01-01&jrs.param$p_EndDate=2017-12-31&jrs.uid=admin&jrs.rpt_language=en`

**Publishing to printer immediately**

To publish the report to a printer immediately, the URL used for this task could be as follows:

`http://localhost:8888/jinfonet/submitSchedPage.jsp?jrs.cmd=jrs.submit_schedule&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.task_class=jet.server.schedule.jrtasks.PublishRptTask&jrs.launch_type=0&jrs.to_printer=true&jrs.report=%2fSampleReports%2fABC.cls&jrs.param$P_StartDate=2016-01-01&jrs.param$p_EndDate=2017-12-31&jrs.rpt_language=en`

**Publishing to fax immediately**

To publish the report to a fax immediately, the URL used for this task could be as follows:

`http://localhost:8888/jinfonet/submitSchedPage.jsp?jrs.cmd=jrs.submit_schedule&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.report=%2fSampleReports%2fABC.cls&jrs.task_class=jet.server.schedule.jrtasks.PublishRptTask&jrs.launch_type=0&jrs.param$P_StartDate2016-01-01&jrs.param$p_EndDate=2017-12-31&jrs.uid=admin&jrs.to_fax=true&jrs.to_fax_is_include_cover=false&jrs.to_fax_to_fax_number=888888`

**Publishing to FTP immediately**

To publish the report to an FTP site immediately, the URL used for this task could be as follows:

`http://localhost:8888/jinfonet/submitSchedPage.jsp?jrs.cmd=jrs.submit_schedule&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.report=%2fSampleReports%2fABC.cls&jrs.task_class=jet.server.schedule.jrtasks.PublishRptTask&jrs.launch_type=0&jrs.param$P_StartDate=2016-01-01&jrs.param$p_EndDate=2017-12-31&jrs.uid=admin&jrs.to_FTP=true&jrs.ftp0=jrs.ftpHost%3d192.168.0.0%26jrs.ftpPort%3d21%26jrs.ftpUn%3dftpuser%26jrs.ftpPsd%3d1234%26jrs.ftpLoc%3d%2ftest%26jrs.ftpPdf%3dtrue`

**Publishing a bursting report to disk and to PDF**

The following URL publishes the bursting report Sales Statistics by Region Report.cls to disk and to PDF:

`http://localhost:8888/jinfonet/submitSchedPage.jsp?jrs.auth_uid=admin&jrs.auth_pwd=admin&jrs.cmd=jrs.submit_schedule&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.report=%2fSampleReports%2fSales Statistics by Region Report.cls&jrs.task_class=jet.server.schedule.jrtasks.PublishRptTask&jrs.launch_type=0&jrs.bursting_schema$BurstingSchema=true&jrs.is_bursting_task=true&jrs.to_disk=true&jrs.to_pdf=true&jrs.disk_pdf_encrypt=true&jrs.password_pdf=true&jrs.pdf_permis_pasw=1234&jrs.confirm_new_password=1234&jrs.pdf_printallow=2`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750362-Running-Reports-via-URL)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750322-Creating-Reports-via-URL)
