---
title: "Scheduling Reports"
id: 1500009674681
section: "Running and Scheduling Reports Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009674681-Scheduling-Reports
updated_at: 2021-07-24T20:53:45Z
---

# Scheduling Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009674661-Running-Reports)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009649902-Scheduling-Tasks-to-Publish-Reports)

# Scheduling Reports

Logi JReport Server provides a scheduling system with which you can schedule tasks for reports to run the reports at a specified time or periodically and customize notification messages to notify others of whether or not the tasks are executed successfully. You can submit a scheduled task from web page, [via URL](https://devnet.logianalytics.com/hc/en-us/articles/1500009650522-Scheduling-Reports) or by [calling the Server API methods](https://devnet.logianalytics.com/hc/en-us/articles/1500009644142-Scheduling-a-Report-Task). Logi JReport Server records the scheduled tasks according to their different executing status (for details, refer to [Managing Tasks](https://devnet.logianalytics.com/hc/en-us/articles/1500009673681-Managing-Tasks)).

In order to provide the means to run tasks defined outside of Logi JReport on Logi JReport Server, and to just use Logi JReport Server's schedule function, Logi JReport provides a task named User Task, using which developer users can implement a customized task with the schedule properties. For details, see [Scheduling a Customized Task Using User Task](https://devnet.logianalytics.com/hc/en-us/articles/1500009644122-Scheduling-a-Customized-Task-Using-User-Task).

Developer users can also specify a Java class to monitor the task event when setting up a schedule task. For details, see [Adding TaskListener When Scheduling Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009668701-Adding-TaskListener-When-Scheduling-Reports).

This section focuses on the following:

* [Scheduling Tasks to Publish Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009649902-Scheduling-Tasks-to-Publish-Reports)
* [Scheduling a Task Containing a Bursting Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009674701-Scheduling-a-Task-Containing-a-Bursting-Report)
* [Applying Dynamic Names for Published Result Files](https://devnet.logianalytics.com/hc/en-us/articles/1500009674821-Applying-Dynamic-Names-for-Published-Result-Files)
* [Viewing Scheduled Report Results](https://devnet.logianalytics.com/hc/en-us/articles/1500009674841-Viewing-Scheduled-Report-Results)
* [Importing and Exporting Scheduled Tasks](https://devnet.logianalytics.com/hc/en-us/articles/1500009674801-Importing-and-Exporting-Scheduled-Tasks)

**Notes:**

* When you schedule to publish a report to Page Report Result format, if the report is linked to another report, in the Page Report Result file, the link will no longer be supported, and if you schedule to publish the report to several formats and Page Report Result format is included at the same time, the link will not be available in the other format outputs either.
* When you schedule to publish a report to HTML format, the names of page navigation links in the report, such as First, Previous, Next, and Last, can be localized according to your requirements. For details, refer to [Localizing the Page Navigation Links in HTML Report Outputs](https://devnet.logianalytics.com/hc/en-us/articles/1500009649202-Localizing-Page-Navigation-Links-in-HTML-Report-Outputs).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009674661-Running-Reports)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009649902-Scheduling-Tasks-to-Publish-Reports)
