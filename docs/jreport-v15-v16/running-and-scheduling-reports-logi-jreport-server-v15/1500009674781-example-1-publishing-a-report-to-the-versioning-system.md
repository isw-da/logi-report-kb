---
title: "Example 1: Publishing a Report to the Versioning System"
id: 1500009674781
section: "Running and Scheduling Reports Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009674781-Example-1-Publishing-a-Report-to-the-Versioning-System
updated_at: 2021-07-24T20:53:42Z
---

# Example 1: Publishing a Report to the Versioning System

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009649902-Scheduling-Tasks-to-Publish-Reports)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009649922-Example-2-Publishing-a-Report-to-Disk-)

# Example 1: Publishing a Report to the Versioning System

In this example, a task is set up and will be performed immediately. The generated result is asked to be kept for 30 days.

1. On the Logi JReport Console > Resources page, select the report row, right-click in the row and select **Schedule** from the shortcut menu to display the Schedule dialog.
2. In the General tab, specify the general report settings.
3. In the Parameter tab, specify the parameter values as required if the report has parameters.
4. In the Publish tab,
   1. Select the **To Version** sub tab, then check **Publish to Versioning System**.

      ![](https://devnet.logianalytics.com/hc/article_attachments/4404926663063/sch_pub_vrsn.gif)
   2. Select the required formats and set the format settings.
   3. Check the **Built-in Version Folder** option in Archive Location to save the report result version in the built-in version folder.
   4. Set **0** for the Maximum Number of Versions.
   5. Check the  **Result Auto-delete** option and define the result to expire in 30 days.
5. In the Conditions tab, select the **Time** sub tab, define the time zone from the Time Zone drop-down list, then from the Time Type drop-down list, choose **Run this task immediately**.
6. If you want to notify someone of when the task is finished by sending an e-mail, go to the Notification tab and then set the settings.
7. Select **Finish** to have the task performed.

Then, select **My Tasks** on the system toolbar. While the task is being performed, you can see a record of it in the Running table. On completion it will be put into the Completed table.

**Notes:**

* When scheduling to publish a page report to the versioning system, the Page Report Result and Logi JReport Result formats are based on the report level, that is the report with all selected report tabs will be output to a single file no matter Export to One File in the General tab is checked or not.
* There is another way to publish the report result to version. If the property server.version.from.temp is set to true in the server.properties file in  `<install_root>\bin`, or the option Enable "Publish to Versioning System" for Background Tasks View on the Logi JReport Administration > Configuration > Advanced page is selected, you will get the link Publish to Version System on the system toolbar of the Logi JReport Console page.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009649902-Scheduling-Tasks-to-Publish-Reports)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009649922-Example-2-Publishing-a-Report-to-Disk-)
