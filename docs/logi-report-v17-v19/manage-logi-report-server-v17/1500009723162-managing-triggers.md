---
title: "Managing Triggers"
id: 1500009723162
section: "Manage Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009723162-Managing-Triggers
updated_at: 2021-07-25T07:18:57Z
---

# Managing Triggers

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750021-Managing-In-memory-Cubes)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750281-National-Language-Support)

# Managing Triggers

Triggers work together with time conditions for activating scheduled tasks. Users bind triggers when creating schedule tasks, and then the administrator determines whether the condition is ready and fires the triggers to start running all of the scheduled tasks waiting on the triggers at any time.

Administrators manage triggers in the Triggers page of the Logi Report Server console (to access the page, point to **Administration** on the system toolbar, and then select **Other** > **Triggers** from the drop-down menu).

![Trigger page](https://devnet.logianalytics.com/hc/article_attachments/4404936796823/mng_trgr.gif)

Administrators can manage the triggers as follows:

* **Creating a trigger**
  1. Select **New Trigger** on the task bar. Report Server displays the [New Trigger](https://devnet.logianalytics.com/hc/en-us/articles/1500009720722-New-Trigger) dialog box.

     ![New Trigger dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942501271/nwtrigr.gif)
  2. In the Trigger Name text box, type a unique name for the trigger. Select **Conflict Check** to check whether the name has been used.
  3. In the Description text box, type a brief description to introduce the trigge
  4. Select **OK**to create the trigger.

  The new trigger is now added in the trigger table and is enabled by default. The trigger table contains the following columns:

  | Column | Description |
  | --- | --- |
  | Name | Displays the names of the triggers. |
  | Is Enabled | Shows whether the triggers are enabled or not. |
  | Referenced | Shows the times when the triggers are referenced. |
  | Last Fired | Shows the time when the triggers are lasted fired. |
  | Description | Displays the descriptions of the triggers. |

  You can select triggers in the trigger table by selecting the check boxes ahead of them. To select all the triggers, select the check box on the column header.
* **Firing triggers**When a trigger is enabled, it can be fired to enable scheduled tasks that are bound with the trigger. To file a trigger, select it in the trigger table by selecting the check box ahead of it, and then select **Fire** on the task bar. The firing time will be recorded in the Last Fired column. Multiple triggers can be fired at a time.
* **Disabling triggers**  
   To disable the enabled triggers, select them in the trigger table and then select **Disable**.
* **Enabling triggers**To enable the disabled triggers, select them in the trigger table and then select **Enable**.
* **Deleting triggers**  
   Triggers that have not been referred to by any scheduled tasks can be deleted. To delete a trigger, select it in the trigger table and then select **Delete**. Multiple triggers can be deleted at a time.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750021-Managing-In-memory-Cubes)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750281-National-Language-Support)
