---
title: "Example 4: Publishing a Report to Printer"
id: 1500009649942
section: "Running and Scheduling Reports Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009649942-Example-4-Publishing-a-Report-to-Printer
updated_at: 2021-07-24T20:53:43Z
---

# Example 4: Publishing a Report to Printer

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009674761-Example-3-Publishing-a-Report-to-E-mail)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009674721-Example-5-Publishing-a-Report-to-Fax)

# Example 4: Publishing a Report to Printer

In this example, you will learn how to set up a task to publish the report result to a printer.

1. On the Logi JReport Console > Resources page, select the report row, right-click in the row and select **Schedule** from the shortcut menu to display the Schedule dialog.
2. In the General tab, specify the general report settings.
3. In the Parameter tab, specify the parameter values as required if the report has parameters.
4. In the Publish tab,
   1. Select the  **To Printer** sub tab and then check **Publish to Printer**.
   2. Select a JDK print method for the report result in the Select Print Method field.
   3. Type a name with the path of the printer in the Printer field.
   4. Specify other [options](https://devnet.logianalytics.com/hc/en-us/articles/1500009646762-Schedule#Printer) according to your requirements.
5. In the Conditions tab, select the **Time** sub tab, define the time zone from the Time Zone drop-down list, then from the Time Type drop-down list of the Time tab, choose **Run this task immediately**.
6. If you want to notify someone of when the task is finished by sending an e-mail, go to the Notification tab and set the settings.
7. If you want to specify a timeout for the task, specify the settings in the Duration tab as required.
8. Select **Finish** to have the task performed.

Then, select **My Tasks** on the system toolbar. When the task is being performed, you can see a record of it in the Running table and on completion it will be put into the Completed table.

**Note:** When there is no printer connected with Logi JReport Server, and you schedule to publish a report to a printer, the server may crash or throw an exception.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009674761-Example-3-Publishing-a-Report-to-E-mail)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009674721-Example-5-Publishing-a-Report-to-Fax)
