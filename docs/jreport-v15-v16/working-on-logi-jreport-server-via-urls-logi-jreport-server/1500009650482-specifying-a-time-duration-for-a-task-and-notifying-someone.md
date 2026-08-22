---
title: "Specifying a Time Duration for a Task and Notifying Someone by E-mail"
id: 1500009650482
section: "Working on Logi JReport Server via URLs Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009650482-Specifying-a-Time-Duration-for-a-Task-and-Notifying-Someone-by-E-mail
updated_at: 2021-07-24T20:53:32Z
---

# Specifying a Time Duration for a Task and Notifying Someone by E-mail

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650502-Specifying-the-Report-Studio-Mode)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675461-Switching-the-Report-Database-Connection)

# Specifying a Time Duration for a Task and Notifying Someone by E-Mail

Take the following examples to specify a time duration for a report run task, and ask Logi JReport Server to notify someone of the task status via e-mail if the task has not yet finished running when the task duration is up:

* Use tryView.jsp to run a report without a parameter:

  `http://localhost:8888/jinfonet/tryView.jsp?&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.report=%2fSampleReports%2fEmployee Information.cls&jrs.timeout_send_email=true&jrs.report_timeout=5&jrs.mailto=person@company.com&jrs.mailsubject=TaskForTimeoutSendEmail&jrs.result_type=1&jrs.mailcomments=IFTHEREPORTISFINISHEDTHERESULTWILLBESENT&jrs.mailfrom=person@company.com`
* Use runReport.jsp to run a report with parameters:

  `http://localhost:8888/jinfonet/runReport.jsp?jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.report=%2fSampleReports%2fCustomerAnalysis.cls&jrs.param$P_StartDate=2006-1-1&jrs.param$p_EndDate=2007-12-31&jrs.timeout_send_email=true&jrs.report_timeout=1&jrs.mailto=person@company.com&jrs.mailsubject=AboutTaskForTimeout&jrs.result_type=1`

You can also set a message in the e-mail by setting the property *jrs.timeout\_sendmail\_message*.

For example, you want to display message as follows:

Running <report name> takes more than <Timeout> seconds.  
 The subject is <mail subject> and has been sent to <mailto> from <mailfrom>  
 It is a file whose type is <type>.

Then you can set the property in URL as follows:

jrs.timeout\_sendmail\_message=Running {6} takes more than {0} seconds.<p>The subject is {2} and has been sent to {1} from {5}.<p>It is a file whose type is {3}.

**Where**

{0} - The report timeout  
 {1} - mail to  
 {2} - mail subject  
 {3} - result type  
 {4} - mail comment  
 {5} - mail from  
 {6} - Catalog name/report  
<p> - an Enter key

**Example**

`http://localhost:8888/jinfonet/tryView.jsp?jrs.report=%2fSampleReports%2fCustomerAnalysis.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.timeout_send_email=true&jrs.report_timeout=1&jrs.mailto=person@company.com&jrs.mailsubject=AboutTaskForTimeoutSendEmail&jrs.result_type=1&jrs.mailcomments=CustomerAnalysis&jrs.mailfrom=person@company.com&jrs.timeout_sendmail_message=.This {6} is a large report whose runtime is over {0} seconds.<p>The report is sent to {1} from {5}.<p>The subject of the mail is {2}.<p>Its type is {3}.`

**Note:** You should type the single quote sign " ' " twice if you use it in the message.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650502-Specifying-the-Report-Studio-Mode)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675461-Switching-the-Report-Database-Connection)
