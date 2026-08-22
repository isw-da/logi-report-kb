---
title: "Managing Triggers"
id: 1500009648982
section: "Managing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009648982-Managing-Triggers
updated_at: 2021-07-24T20:54:01Z
---

# Managing Triggers

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673461-Recovering-and-Synchronizing-In-memory-Cubes)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673841-National-Language-Support)

# Managing Triggers

Triggers work together with time conditions for activating scheduled tasks. Users bind triggers when creating schedule tasks, and then the administrator determines whether the condition is ready and fires the triggers to start running all of the scheduled tasks waiting on the triggers at any time.

Administrators manage triggers on the Logi JReport Administration > Trigger page (to access the page, select **Triggers** on the system toolbar of the Logi JReport Administration page).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920486679/mng_trgr.gif)

Administrators can manage the triggers in the table as follows:

* **Creating a trigger**
  1. Select **New Trigger** on the task bar of the Triggers page.
  2. In the displayed dialog, input a unique name and a description for the trigger. Select **Conflict Check** to check whether the name has been used.
  3. Select **OK**.
  4. A message box is prompted telling whether the trigger is created successfully. Select **OK** to close the message.

  The new trigger is now added to the trigger table and is enabled by default. The trigger table contains the following columns:

  | Column | Description |
  | --- | --- |
  | Name | Displays the names of the triggers. |
  | Is Enabled | Shows whether the triggers are enabled or not. |
  | Referenced | Shows the times when the triggers are referenced. |
  | Last Fired | Shows the time when the triggers are lasted fired. |
  | Description | Displays the descriptions of the triggers. |

  You can select triggers in the trigger table by selecting the checkboxes ahead of them. To select all the triggers, check the checkbox on the column header.
* **Firing triggers**When a trigger is enabled, it can be fired to enable scheduled tasks that are bound with the trigger. To file a trigger, select it in the trigger table by checking the checkbox ahead of it, and then select **Fire** on the task bar. The firing time will be recorded in the Last Fired column. Multiple triggers can be fired at a time.
* **Disabling triggers**  
   To disable the enabled triggers, select them in the trigger table and then select **Disable**.
* **Enabling triggers**To enable the disabled triggers, select them in the trigger table and then select **Enable**.
* **Deleting triggers**  
   Triggers that have not been referred to by any scheduled tasks can be deleted. To delete a trigger, select it in the trigger table and then select **Delete**. Multiple triggers can be deleted at a time.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673461-Recovering-and-Synchronizing-In-memory-Cubes)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673841-National-Language-Support)
