---
title: "Viewing Scheduled Reports"
id: 45203993429901
section: "Running and Scheduling Reports Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203993429901-Viewing-Scheduled-Reports
updated_at: 2026-04-30T14:10:48Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Viewing Scheduled Reports 

When finishing a report schedule task, you can view the reports included in the task at any time. This topic describes how you can view scheduled reports that you published to different destinations.

This topic contains the following sections:

- 
Viewing Reports Scheduled to Version
- Via the Schedule Task Details

- Via the Version Table

- Viewing Reports Scheduled to Disk
                

- Viewing Reports Scheduled to Email/Printer/Fax/FTP
                

## 
Viewing Reports Scheduled to Version

There are two ways you can take to view the reports you published to the versioning system: via the schedule task details and via the version table.

### 
Via the Schedule Task Details

- On the Server Console, select My Tasks on the system toolbar.

- Select the Completed tab, where Server displays all the successfully scheduled tasks.
			    

- Locate the required task and do any of the following:
- Select the name of the task in the Schedule Name column.

- Select the Details button  on the floating toolbar of the task row.

- Select the task row and select Edit > Details on the task bar of the My Tasks page.

- In the Result Details list, the links to different report formats are available in the To Version section. Select the format links to view the reports.
    

You can further export Logi Report Result and Web Report Result to the HTML, PDF, Text, Excel, XML, RTF, and Postscript formats via Server. When you view a Logi Report Result or Web Report Result, Server displays the following dialog box for you to specify the export format and configure the format settings. For a Logi Report Result, you also need to  select the report tabs in the page report you want to export.

Server opens page report results in Page Report Studio which has permission control, so to view page report results successfully you need to have the Execute and/or Edit permissions on the results. To view a page report result, you can choose one of the following ways: 

- Select Page Report Result which is available when you have the Execute permission on the page report result. Server then opens the result in Page Report Studio in the mode specified by the Default View for Page Report Studio option in the server profile. If Default View is Interactive View but you do not have the Edit permission, you will get an error message. 

- Select the Run button  on the result row to access Basic View of Page Report Studio. You need the execute permission.

- Select the Edit button  on the result row to access Interactive View of Page Report Studio. You need the edit permission.

- Select the Advanced Run button  on the result row. In this way, you can customize the result resolution and the view mode of Page Report Studio: Basic View, Basic View Only, or Interactive View. You need the execute permission.

### 
Via the Version Table

Based on the different archive location that you have specified when creating the report schedule task, you will need to access the version table of a report in different ways.

- If the archive location is Built-in Version Folder:
    
- In the server resource tree, browse to the row that the original report is in.

- Do any of the following to open the Report Result Versions table:
        
- Select the report row and select Tools > Version on the task bar of the Resources page.

- Select the report row, right-click in the row and select Version from the shortcut menu.

- Put the mouse pointer over the report row and select the Version button  on the floating toolbar.

- In the  Results column of the version table, Server lists the reports of different formats. Select the format links to view the reports.

- If the archive location is the My Reports Folder or Public Reports Folder, which requires providing the path and name for the scheduled report in the server resource tree:
    
- In the server resource tree, browse to the row that the report is in based on the specified path and name information.

- Do any of the following to open the Result Versions table:
- Select the name of the report directly.

- Hover over the report row and select the Version button  on the floating toolbar.

- Select the report row, right-click in the row and select Version from the shortcut menu.

- Select the report row and select Tools > Version on the task bar of the Resources page.

- In the Results column of the version table, Server lists the reports of different formats. If the schedule task is based on multiple reports, Server lists the reports of different formats for each report tab in a page report and each web report. Select the format links to view the reports.

You can also use URL commands to view the reports that are published to version.

## 
Viewing Reports Scheduled to Disk

When you schedule to publish a report to disk, you can choose to publish the report to either the  server resource tree or  a server disk path, then after Server completes the schedule task:

- If you are to publish the report to the server resource tree, you can view the report files from the specified server resource tree folder.

- If you are to publish the report to a server disk path, you can find the report files in the specified location on the computer where you installed Report Server.

## 
Viewing Reports Scheduled to Email/Printer/Fax/FTP

When you schedule to publish a report to email, printer, fax, or FTP, you can view the scheduled report if the specified address or location is available to you.
