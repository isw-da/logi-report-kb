---
title: "Scheduling Reports"
id: 1500009751081
section: "Run and Schedule Reports Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009751081-Scheduling-Reports
updated_at: 2021-07-25T07:18:42Z
---

# Scheduling Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009724222-Running-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009724262-Scheduling-Tasks-to-Run-Reports)

# Scheduling Reports

Logi Report Server provides a schedule system with which you can schedule tasks to run reports automatically at one or more designated dates and times, publish the report results to different destinations in various formats such as PDF, HTML, Excel, and so on, and customize notification messages to notify others of whether or not the tasks are executed successfully. You can submit a scheduled task from web page, [via URL](https://devnet.logianalytics.com/hc/en-us/articles/1500009751741-Scheduling-Reports) or by [calling the Server API methods](https://devnet.logianalytics.com/hc/en-us/articles/1500009744501-Scheduling-a-Report-Task). Logi Report Server records the scheduled tasks according to their different executing status (for details, refer to [Managing Tasks](https://devnet.logianalytics.com/hc/en-us/articles/1500009750161-Managing-Tasks)).

In order to provide the means to run tasks defined outside of Logi Report on Logi Report Server, and to just use Logi Report Server's Schedule function, Logi Report provides a task named User Task, using which developer users can implement a customized task with the schedule properties. For details, see [Scheduling a Customized Task Using User Task](https://devnet.logianalytics.com/hc/en-us/articles/1500009744481-Scheduling-a-Customized-Task-Using-User-Task).

Developer users can also specify a Java class to monitor the task event when setting up a schedule task. For details, see [Applying TaskListener](https://devnet.logianalytics.com/hc/en-us/articles/1500009718522-Applying-TaskListener).

In addition, [Web Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/1500009724782-General-Operations-in-a-Report#Schedule) and [Page Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/1500009723422-General-Operations-in-a-Report#Schedule) provide the Quick Schedule feature to allow end users to submit simple schedule tasks from the studio UI.

The following topics provide detailed information on scheduling reports:

* [Scheduling Tasks to Run Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009724262-Scheduling-Tasks-to-Run-Reports)
* [Scheduling Bursting Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009724242-Scheduling-Bursting-Reports)
* [Applying Dynamic Names for Published Result Files](https://devnet.logianalytics.com/hc/en-us/articles/1500009724322-Applying-Dynamic-Names-for-Published-Result-Files)
* [Viewing Scheduled Report Results](https://devnet.logianalytics.com/hc/en-us/articles/1500009751161-Viewing-Scheduled-Report-Results)
* [Importing and Exporting Schedule Tasks](https://devnet.logianalytics.com/hc/en-us/articles/1500009751141-Importing-and-Exporting-Scheduled-Tasks)

**Notes:**

* When you schedule to publish a report to the Page Report Result format, if the report is linked to another report, the link will no longer be supported in page report result. If you schedule to publish the report to several formats and the Page Report Result format is included at the same time, the link will not be available in the other format outputs either.
* When you schedule to publish a report to the HTML format, the names of page navigation links in the report, such as First, Previous, Next, and Last, can be localized according to your requirements. For details, refer to [Localizing the Page Navigation Links in HTML Report Outputs](https://devnet.logianalytics.com/hc/en-us/articles/1500009750321-NLS-at-Report-Level#Link).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009724222-Running-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009724262-Scheduling-Tasks-to-Run-Reports)
