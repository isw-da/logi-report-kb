---
title: "Managing Triggers"
id: 1500009777321
section: "Managing Logi Report Server v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009777321-Managing-Triggers
updated_at: 2021-07-24T00:47:56Z
---

# Managing Triggers

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009777121-Managing-In-Memory-Cubes)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009777441-National-Language-Support)

# Managing Triggers

Triggers work together with time conditions for activating scheduled tasks. This topic describes how you can manage triggers in the Server Console as an administrator.

You can bind triggers when creating scheduled tasks, and then the administrator determines whether the condition is ready and fires the triggers to start running the scheduled tasks waiting on the triggers at any time.

Administrators manage triggers in the Triggers page of the Server Console. To access the page, point to **Administration** on the system toolbar, and then select **Other** > **Triggers** from the drop-down menu.

![Trigger page](https://devnet.logianalytics.com/hc/article_attachments/4404885409047/mng_trgr.gif)

You can manage the triggers as follows:

* **Creating a trigger**
  1. Select **New Trigger** on the task bar. Server displays the [New Trigger](https://devnet.logianalytics.com/hc/en-us/articles/1500009774281-New-Trigger-Dialog-Box-Properties) dialog box.

     ![New Trigger dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885409303/nwtrigr.gif)
  2. In the **Trigger Name** text box, type a unique name for the trigger. Select **Conflict Check** to check whether the name has been used.
  3. In the **Description** text box, type a brief description to introduce the trigger.
  4. Select **OK** to create the trigger.

  Server adds the new trigger in the trigger table and enables it by default. The trigger table contains the following columns:

  | Column | Description |
  | --- | --- |
  | Name | The names of the triggers. |
  | Is Enabled | Show whether the triggers are enabled. |
  | Referenced | The times when the triggers are referenced. |
  | Last Fired | The time when you fired the triggers last time. |
  | Description | The descriptions of the triggers. |

  You can select triggers in the trigger table by selecting the check boxes ahead of them. To select all the triggers, select the check box on the column header.
* **Firing triggers**When a trigger is enabled, you can fire it to enable scheduled tasks that are bound with the trigger. To fire a trigger, select it in the trigger table by selecting the check box ahead of it, and then select **Fire** on the task bar. Server records the firing time in the **Last Fired** column. You can fire multiple triggers at a time.
* **Disabling triggers**  
   To disable the enabled triggers, select them in the trigger table and then select **Disable**.
* **Enabling triggers**To enable the disabled triggers, select them in the trigger table and then select **Enable**.
* **Deleting triggers**  
   You can delete triggers that no scheduled tasks have referenced. To delete a trigger, select it in the trigger table and then select **Delete**. You can delete multiple triggers at a time.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009777121-Managing-In-Memory-Cubes)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009777441-National-Language-Support)
