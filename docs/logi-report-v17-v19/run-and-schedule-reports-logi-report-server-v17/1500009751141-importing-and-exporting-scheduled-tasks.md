---
title: "Importing and Exporting Scheduled Tasks"
id: 1500009751141
section: "Run and Schedule Reports Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009751141-Importing-and-Exporting-Scheduled-Tasks
updated_at: 2021-07-25T07:18:40Z
---

# Importing and Exporting Scheduled Tasks

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009751161-Viewing-Scheduled-Report-Results)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009724202-Specifying-Parameter-Values)

# Importing and Exporting Schedule Tasks

In Logi Report Server, you can export the report schedule tasks to a script file on your own disk, or import a script file from disk to generate a report schedule task.

**To export a scheduled task to a script file:**

1. In the Logi Report Server console, select **My Tasks** on the system toolbar.

   ![My Tasks Page](https://devnet.logianalytics.com/hc/article_attachments/4404942480535/wkrpt_sch_import_expt.gif)
2. In the Scheduled tab, select the task your want to export.
3. Do one of the following:
   * Put the mouse pointer over the task row and select the **Export to Script** button ![Export to Script button](https://devnet.logianalytics.com/hc/article_attachments/4404936767255/btn_srv_expt.gif) on the floating toolbar.
   * Right-click in the task row and select **Export to Script** from the shortcut menu.
   * Select **Tools** > **Export to Script** on the task bar of the My Tasks page.
4. In the Edit Script box, you can edit the schedule properties. For details about the properties, see [Appendix 1: URL Properties for Running, Scheduling, and Viewing Reports via URL](https://devnet.logianalytics.com/hc/en-us/articles/1500009744581-Appendix-1-URL-Properties-for-Running-Scheduling-and-Viewing-Reports-via-URL).

   ![Edit Script dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942480919/wkrpt_sch_import_edtscrpt.gif)
5. Select **OK** to start exporting. The script file will be saved as schedule.script in the specified download folder of your web browser.

You can also export multiple schedule tasks to a single scrip file. To do this, select the tasks, then select **Tools** > **Export to Script** on the task bar of the My Tasks page. In the Edit Script box, edit the schedule properties if you want and select **OK**.

**To import a script file from disk to generate a schedule task:**

1. In the Scheduled tab of the My Tasks page, select **New Schedule** on the task bar.
2. In the [New Schedule](https://devnet.logianalytics.com/hc/en-us/articles/1500009747641-New-Schedule) dialog box, select the option **Import Script to Create Schedule**.

   ![Import Script to Create Schedule](https://devnet.logianalytics.com/hc/article_attachments/4404936767511/wkrpt_sch_import_impt.gif)
3. Select the **Browse** button to select the script file from the local disk, then select **OK** to import the specified script file.
4. In the Edit Script box, you can modify the schedule properties.
5. Select **OK** to generate a scheduled task.

**Note:** If you just updated from an older version of Logi Report Server, there may be some old scripts saved in your server. In order to use these old scripts, you can select the **Import old script from server** link in the New Schedule dialog box to select an old script to import it to generate a schedule task. To use this link, you must log onto Logi Report Server as an administrator role.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009751161-Viewing-Scheduled-Report-Results)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009724202-Specifying-Parameter-Values)
