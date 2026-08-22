---
title: "Importing and Exporting Scheduled Tasks"
id: 1500009674801
section: "Running and Scheduling Reports Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009674801-Importing-and-Exporting-Scheduled-Tasks
updated_at: 2021-07-24T20:53:42Z
---

# Importing and Exporting Scheduled Tasks

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009674841-Viewing-Scheduled-Report-Results)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009649882-Specifying-Parameter-Values)

# Importing and Exporting Scheduled Tasks

In Logi JReport Server, you can export a scheduled task to a script file which will then be saved on your own disk as a script file. In addition, you can import a script file from the disk file to generate a scheduled task.

**To export a scheduled task to a script file and save it in the disk:**

1. On the Logi JReport Console page, select **My Tasks**  on the system toolbar.
2. In the Scheduled tab, select the rows that one or more scheduled tasks are in.
3. Select **Tools > Export to Script** on the task bar of the My Tasks page (if only one task is selected, you can also right-click in the task row and select **Export to Script** from the shortcut menu, or put the mouse pointer over the task row and select the **Export to Script** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920423575/btn_srv_expt.gif) on the floating toolbar), then modify the script text in the Edit Script box as required.
4. Select **OK** to export the specified scheduled task to a script file.
5. Specify the directory and name for this script file in the File download dialog.

**To import a script file from your disk:**

1. On the Logi JReport Console page, select **My Tasks**  on the system toolbar, then select the **Scheduled** tab.
2. Select **New Schedule** on the task bar of the My Tasks page.
3. In the New Schedule dialog, check the option **Import Script to Create Schedule**.
4. Select the **Browse** button to select a script file from your disk file, then select **OK** to import the specified script file and modify the script text in the Edit Script box as required.
5. Select **OK** to generate a scheduled task.

**Note:** If you just updated from an older version of Logi JReport Server, there may be some old scripts saved in your server. In order to use these old scripts, you can select the **Import old script from server** link in the Import Script page to select an old script to import it to generate a scheduled task. To use this link, you must logon Logi JReport Server as an administrator role.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009674841-Viewing-Scheduled-Report-Results)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009649882-Specifying-Parameter-Values)
