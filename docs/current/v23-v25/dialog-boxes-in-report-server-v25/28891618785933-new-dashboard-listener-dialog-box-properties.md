---
title: "New Dashboard Listener Dialog Box Properties"
id: 28891618785933
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891618785933-New-Dashboard-Listener-Dialog-Box-Properties
updated_at: 2026-02-26T02:12:21Z
source_host: docs-report.zendesk.com
---
# 
New Dashboard Listener Dialog Box Properties

This topic describes how you can use the New Dashboard Listener dialog box to upload and register an implementation of the Dashboard Listener API.

The dialog box includes two phases, one for specifying the implementation file and the other for specifying target dashboards. Server displays the dialog box when an administrator selects New Dashboard Listener in the Administration > Other > Dashboard Listeners page on the Server Console. 

When an administrator selects an implementation class and then select Properties, Server displays the Specifying Target Dashboards Phase.

## 
Specifying the Implementation File Phase

Add an implementation file of the Dashboard Listener API.

Source File

Select Browse to upload an implementation class file of the Dashboard Listener API, which could be a .zip or .jar file. 

Next

Select to move forward to the next step of specifying the target resources. 

Cancel

Select to close the dialog box without doing anything. 

Help

Select to view information about the dialog box.

## 
Specifying Target Dashboards Phase 

Specify the dashboards which you want the implementation to take effect on. 

Class Name

   Server lists the class names defined in the specified implementation file. Select a class name from the list or type the name manually.

Target

Specify the dashboards you want the implementation to take effect on. If the target box is empty, the implementation will not take effect.

- 
 Add button
    Select to open the Select Target dialog box for adding dashboards or folders that contains dashboards.

- 
Remove button
    Select to remove the selected items.

Description

Specify the description of the implementation.

Enabled

Select if you want to enable the implementation. The enabled implementations will take effect.

Back

Select to return to the step of specifying an implementation file.

Finish

Select to add the implementation and close the dialog box.

Cancel

Select to close the dialog box without adding an implementation.

Help

Select to view information about the dialog box.
