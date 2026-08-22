---
title: "Example 5: Publishing a Report to Fax"
id: 1500009674721
section: "Running and Scheduling Reports Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009674721-Example-5-Publishing-a-Report-to-Fax
updated_at: 2021-07-24T20:53:43Z
---

# Example 5: Publishing a Report to Fax

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009649942-Example-4-Publishing-a-Report-to-Printer)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009674741-Example-6-Publishing-a-Report-to-an-FTP-Site)

# Example 5: Publishing a Report to Fax

Before you can fax the report results, the [fax settings](https://devnet.logianalytics.com/hc/en-us/articles/1500009644522-Configuring-Export-Settings#Fax)  must have been predefined by the administrator.

In this example, you will learn how to set up a task to publish the report result to fax.

1. On the Logi JReport Console > Resources page, select the report row, right-click in the row and select **Schedule** from the shortcut menu to display the Schedule dialog.
2. In the General tab, specify the general report settings.
3. In the Parameter tab, specify the parameter values as required if the report has parameters.
4. In the Publish tab, select the **To Fax** sub tab, check the **Publish to Fax** option and then fill in [every field](https://devnet.logianalytics.com/hc/en-us/articles/1500009646762-Schedule#Fax) and set the settings according to your requirements.
5. In the Conditions tab, select the **Time** sub tab, define the time zone from the Time Zone drop-down list, then from the Time Type drop-down list, choose **Run this task immediately**.
6. If you want to notify someone of when the task is finished by sending an e-mail, go to the Notification tab and set the settings.
7. If you want to specify a timeout for the task, specify the settings in the Duration tab as required.
8. Select **Finish** to have the task performed.

Then, select **My Tasks**  on the system toolbar. When the task is being performed, you can see a record of it in the Running table and on completion it will be put into the Completed table.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009649942-Example-4-Publishing-a-Report-to-Printer)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009674741-Example-6-Publishing-a-Report-to-an-FTP-Site)
