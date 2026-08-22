---
title: "Scheduling to Run Multiple Reports"
id: 45204024598285
section: "Running and Scheduling Reports Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45204024598285-Scheduling-to-Run-Multiple-Reports
updated_at: 2026-06-29T20:08:27Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Scheduling to Run Multiple Reports 

For page reports and web reports that are in the same folder in the server resource tree and use the same catalog, you can schedule to run them all at a time. This topic describes how you can schedule to run multiple reports.

However, in this case, you can only publish the reports to Report Server's versioning system and by email. 

- In the Resources page of the Server Console, browse to the folder that contains the reports you want to schedule to run.

- Select the reports to be scheduled, then do either of the following:
- Select Run > Schedule on the task bar of the Resources page. 

- Right-click in any of the selected report row and select Schedule from the shortcut menu.

Server displays the 
    Schedule dialog box.

- In the General tab, type the name for the task in the Schedule Name text box, type the description for the task in the Name Description box, and specify the priority of the task as required. You can expand the top section to view the details about the reports included in the schedule task.
			

- In the Parameter tab, specify the parameter values if the reports have parameters. All the parameters used in the selected reports are listed in the tab.

- In the Publish tab,  specify the types of the task: To Version and To E-mail, then select the report formats for each task type and set the format settings. For more information about the task types, see the examples in Examples of Scheduling Reports.

- Specify the settings in the Conditions, Notification and Duration tabs as you would do when scheduling to run a single report.

- Select Finish, and Report Server will then perform the task.
