---
title: "Scheduling Reports"
id: 1500009749542
section: "Scheduling Reports"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009749542-Scheduling-Reports
updated_at: 2021-07-24T00:47:39Z
---

# Scheduling Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009778381-Running-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009778421-Scheduling-Tasks-to-Run-Reports)

# Scheduling Reports

Logi Report Server provides a schedule system with which you can schedule tasks to run reports automatically at one or more designated dates and times, publish the report results to different destinations in various formats such as PDF, HTML, and Excel, and customize notification messages to notify others of whether the tasks are executed successfully. This topic describes the server scheduling system, user task, and quick schedule.

You can submit a scheduled task from web page, [via URL](https://devnet.logianalytics.com/hc/en-us/articles/1500009778901-Scheduling-Reports-via-URL), or by [calling the Server API methods](https://devnet.logianalytics.com/hc/en-us/articles/1500009743302-Scheduling-a-Report-Task). Server records the scheduled tasks according to their different executing status (for more information, see [Managing Report-Running Tasks](https://devnet.logianalytics.com/hc/en-us/articles/1500009777301-Managing-Report-Running-Tasks)).

In order to provide the means to run tasks defined outside of Logi Report on Server, and to only use Server's Schedule function, Logi Report provides a task named User Task, using which developer users can implement a customized task with the schedule properties. For more information, see [Scheduling a Customized Task Using User Task](https://devnet.logianalytics.com/hc/en-us/articles/1500009743282-Scheduling-a-Customized-Task-Using-User-Task).

Developer users can also specify a Java class to monitor the task event when setting up a schedule task. For more information, see [Applying TaskListener](https://devnet.logianalytics.com/hc/en-us/articles/1500009771141-Applying-TaskListener).

In addition, [Web Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/1500009778761-General-Operations-in-Web-Report#Schedule) and [Page Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/1500009749002-General-Operations-in-Page-Report#Schedule) provide the Quick Schedule feature to enable end users to submit simple schedule tasks from the studio UI.

Select the following links to view the topics:

* [Scheduling Tasks to Run Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009778421-Scheduling-Tasks-to-Run-Reports)
* [Scheduling Bursting Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009778401-Scheduling-Bursting-Reports)
* [Applying Dynamic Names for Published Result Files](https://devnet.logianalytics.com/hc/en-us/articles/1500009749622-Applying-Dynamic-Names-for-Published-Result-Files)
* [Viewing Scheduled Report Results](https://devnet.logianalytics.com/hc/en-us/articles/1500009749642-Viewing-Scheduled-Report-Results)
* [Importing and Exporting Scheduled Tasks](https://devnet.logianalytics.com/hc/en-us/articles/1500009749602-Importing-and-Exporting-Scheduled-Tasks)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)

* When you schedule to publish a report to the Page Report Result format, if the report links to another report, Server no longer supports the link in the page report result. If you schedule to publish the report to several formats including the Page Report Result format, the link is not available in the other format outputs either.
* When you schedule to publish a report to the HTML format, you can localize the names of page navigation links in the report, such as First, Previous, Next, and Last. For more information, see [Localizing the Page Navigation Links in HTML Report Outputs](https://devnet.logianalytics.com/hc/en-us/articles/1500009777481-NLS-at-Report-Level#Link).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009778381-Running-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009778421-Scheduling-Tasks-to-Run-Reports)
