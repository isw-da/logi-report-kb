---
title: "Importing and Exporting Scheduled Tasks"
id: 45204030924813
section: "Running and Scheduling Reports Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45204030924813-Importing-and-Exporting-Scheduled-Tasks
updated_at: 2026-04-30T14:10:48Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Importing and Exporting Scheduled Tasks 

On Report Server, you can export a report task that you scheduled to a script file on disk, or import a script file from disk to generate a scheduled report task.

This topic contains the following sections:

- Exporting a Scheduled Task to a Script File

- Importing a Script File From Disk to Generate a Scheduled Task

## 
Exporting a Scheduled Task to a Script File

- On the Server Console, select My Tasks on the system toolbar.
    

- In the Scheduled tab, select the task you want to export.

- Do one of the following:
- Put the mouse pointer over the task row and select the Export to Script button  on the floating toolbar.

- Right-click in the task row and select Export to Script from the shortcut menu.

- Select Tools > Export to Script on the task bar of the My Tasks page.

- In the Edit Script box, you can edit the schedule properties. For more information, see URL Properties for Running, Scheduling, and Viewing Reports via URL.

- Select OK to start exporting. The script file will be saved as schedule.script in the specified download folder of your web browser.

You can also export multiple schedule tasks to a single scrip file. To do this, select the tasks, then select Tools > Export to Script on the task bar of the My Tasks page. In the Edit Script box, edit the schedule properties if you want and select OK.

## 
Importing a Script File From Disk to Generate a Scheduled Task

- In the Scheduled tab of the My Tasks page, select New Schedule on the task bar.

- In the New Schedule dialog box, select the option Import Script to Create Schedule.
    

- Select the Browse button to select the script file from the local disk, then select OK to import the specified script file.

- In the Edit Script box, you can modify the schedule properties.

- Select OK to generate a scheduled task.

If you just updated from an older version of Report Server, there may be some old scripts saved in your server. In order to use these old scripts, you can select the Import old script from server link in the New Schedule dialog box to select an old script to import it to generate a schedule task. To use this link, you must sign in to  Report Server as an administrator.
