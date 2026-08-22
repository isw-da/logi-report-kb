---
title: "Importing and Exporting Scheduled Tasks"
id: 5741483570071
section: "Running and Scheduling Reports Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741483570071-Importing-and-Exporting-Scheduled-Tasks
updated_at: 2022-10-31T17:18:21Z
---

# Importing and Exporting Scheduled Tasks

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741469840663-Viewing-Scheduled-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741454720023-Specifying-Parameter-Values)

# Importing and Exporting Scheduled Tasks

On Logi Report Server, you can export a report task that you scheduled to a script file on disk, or import a script file from disk to generate a scheduled report task.

This topic contains the following sections:

* [Exporting a Scheduled Task to a Script File](#Export)
* [Importing a Script File From Disk to Generate a Scheduled Task](#Import)

## Exporting a Scheduled Task to a Script File

1. On the Server Console, select **My Tasks** on the system toolbar.

   ![My Tasks Page](https://devnet.logianalytics.com/hc/article_attachments/9905658645783/wkrpt_sch_import_expt.gif)
2. In the Scheduled tab, select the task you want to export.
3. Do one of the following:
   * Put the mouse pointer over the task row and select the **Export to Script** button ![Export to Script button](https://devnet.logianalytics.com/hc/article_attachments/9905658679191/btn_srv_expt.gif) on the floating toolbar.
   * Right-click in the task row and select **Export to Script** from the shortcut menu.
   * Select **Tools** > **Export to Script** on the task bar of the My Tasks page.
4. In the Edit Script box, you can edit the schedule properties. For more information, see [URL Properties for Running, Scheduling, and Viewing Reports via URL](https://devnet.logianalytics.com/hc/en-us/articles/5741464843927-URL-Properties-for-Running-Scheduling-and-Viewing-Reports-via-URL).

   ![Edit Script dialog](https://devnet.logianalytics.com/hc/article_attachments/9905637302807/wkrpt_sch_import_edtscrpt.gif)
5. Select **OK** to start exporting. The script file will be saved as schedule.script in the specified download folder of your web browser.

You can also export multiple schedule tasks to a single scrip file. To do this, select the tasks, then select **Tools** > **Export to Script** on the task bar of the My Tasks page. In the Edit Script box, edit the schedule properties if you want and select **OK**.

## Importing a Script File From Disk to Generate a Scheduled Task

1. In the Scheduled tab of the My Tasks page, select **New Schedule** on the task bar.
2. In the [New Schedule](https://devnet.logianalytics.com/hc/en-us/articles/5741406176919-New-Schedule-Dialog-Box-Properties) dialog box, select the option **Import Script to Create Schedule**.

   ![Import Script to Create Schedule](https://devnet.logianalytics.com/hc/article_attachments/9905658744087/wkrpt_sch_import_impt.gif)
3. Select the **Browse** button to select the script file from the local disk, then select **OK** to import the specified script file.
4. In the Edit Script box, you can modify the schedule properties.
5. Select **OK** to generate a scheduled task.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)If you just updated from an older version of Logi Report Server, there may be some old scripts saved in your server. In order to use these old scripts, you can select the **Import old script from server** link in the New Schedule dialog box to select an old script to import it to generate a schedule task. To use this link, you must sign in to Logi Report Server as an administrator.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741469840663-Viewing-Scheduled-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741454720023-Specifying-Parameter-Values)
