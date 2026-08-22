---
title: "Managing Triggers"
id: 45203990668813
section: "Managing Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203990668813-Managing-Triggers
updated_at: 2026-04-30T14:10:32Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Managing Triggers 

Triggers work together with time conditions for activating scheduled tasks. This topic describes how you can manage triggers on the Server Console as an administrator.

You can bind triggers when creating scheduled tasks, and then the administrator determines whether the condition is ready and fires the triggers to start running the scheduled tasks waiting on the triggers at any time.

Administrators manage triggers on the Triggers page of the Server Console. To access the page, navigate to Administration > Other > Triggers on the system toolbar.

You can manage the triggers:

- 
Creating a trigger
- Select New Trigger on the task bar. Server displays the New Trigger dialog box.
                        

- In the Trigger Name text box, type a unique name for the trigger. Select Conflict Check to check whether the name has been used.

- In the Description text box, type a brief description to introduce the trigger.

- Select OK to create the trigger.

Server adds the new trigger in the trigger table and enables it by default. The trigger table contains the following columns:

| Column | Description |
| --- | --- |
| Name | The names of the triggers. |
| Is Enabled | Show whether the triggers are enabled. |
| Referenced | The times when the triggers are referenced. |
| Last Fired | The time when you fired the triggers last time. |
| Description | The descriptions of the triggers. |

 You can select triggers in the trigger table by selecting the checkboxes ahead of them. To select all the triggers, select the checkbox on the column header.

- 
Firing triggers
When a trigger is enabled, you can fire it to enable scheduled tasks that are bound with the trigger. To fire a trigger, select it in the trigger table by selecting the checkbox ahead of it, and then select Fire on the task bar. Server records the firing time in the Last Fired column. You can fire multiple triggers  at a time.

- 
Disabling triggers
  To disable the enabled triggers, select them in the trigger table and then select Disable.

- 
Enabling triggers
To enable the disabled triggers, select them in the trigger table and then select Enable.

- 
Deleting triggers
  You can delete triggers that no scheduled tasks have referenced. To delete a trigger, select it in the trigger table and then select Delete. You can delete multiple triggers at a time.
