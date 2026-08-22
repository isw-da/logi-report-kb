---
title: "Scheduling Reports"
id: 1500009692482
section: "Running and Scheduling Reports Logi JReport Server v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009692482-Scheduling-Reports
updated_at: 2021-11-03T06:56:36Z
---

# Scheduling Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009692462-Running-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009692502-Scheduling-Tasks-to-Publish-Reports)

# Scheduling Reports

Logi JReport Server provides a schedule system with which you can schedule tasks for reports to run at a specified time or periodically and customize notification messages to notify others of whether or not the tasks are executed successfully. You can submit a scheduled task from web page, [via URL](https://devnet.logianalytics.com/hc/en-us/articles/1500009693022-Scheduling-Reports) or by [calling the Server API methods](https://devnet.logianalytics.com/hc/en-us/articles/1500009686402-Scheduling-a-Report-Task). Logi JReport Server records the scheduled tasks according to their different executing status (for details, refer to [Managing Tasks](https://devnet.logianalytics.com/hc/en-us/articles/1500009691382-Managing-Tasks)).

In order to provide the means to run tasks defined outside of Logi JReport on Logi JReport Server, and to just use Logi JReport Server's Schedule function, Logi JReport provides a task named User Task, using which developer users can implement a customized task with the schedule properties. For details, see [Scheduling a Customized Task Using User Task](https://devnet.logianalytics.com/hc/en-us/articles/1500009712181-Scheduling-a-Customized-Task-Using-User-Task).

Developer users can also specify a Java class to monitor the task event when setting up a schedule task. For details, see [Applying TaskListener](https://devnet.logianalytics.com/hc/en-us/articles/1500009712081-Applying-TaskListener).

In addition, [Web Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/1500009719161-General-Operations-in-a-Report#Schedule) and [Page Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/1500009718181-General-Operations-in-a-Report#Schedule) provide the Quick Schedule feature to allow end users to submit simple schedule tasks from the studio UI.

The following topics provide detailed information on scheduling reports:

* [Scheduling Tasks to Publish Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009692502-Scheduling-Tasks-to-Publish-Reports)
* [Scheduling a Task Containing a Bursting Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009718701-Scheduling-a-Task-Containing-a-Bursting-Report)
* [Applying Dynamic Names for Published Result Files](https://devnet.logianalytics.com/hc/en-us/articles/1500009718721-Applying-Dynamic-Names-for-Published-Result-Files)
* [Viewing Scheduled Report Results](https://devnet.logianalytics.com/hc/en-us/articles/1500009718741-Viewing-Scheduled-Report-Results)
* [Importing and Exporting Scheduled Tasks](https://devnet.logianalytics.com/hc/en-us/articles/1500009692522-Importing-and-Exporting-Scheduled-Tasks)

**Notes:**

* When you schedule to publish a report to Page Report Result format, if the report is linked to another report, in the Page Report Result file, the link will no longer be supported, and if you schedule to publish the report to several formats and Page Report Result format is included at the same time, the link will not be available in the other format outputs either.
* When you schedule to publish a report to HTML format, the names of page navigation links in the report, such as First, Previous, Next, and Last, can be localized according to your requirements. For details, refer to [Localizing the Page Navigation Links in HTML Report Outputs](https://devnet.logianalytics.com/hc/en-us/articles/1500009718081-NLS-at-Report-Level#Link).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009692462-Running-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009692502-Scheduling-Tasks-to-Publish-Reports)
