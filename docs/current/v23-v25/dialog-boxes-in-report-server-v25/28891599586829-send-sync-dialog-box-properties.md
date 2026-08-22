---
title: "Send Sync Dialog Box Properties"
id: 28891599586829
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891599586829-Send-Sync-Dialog-Box-Properties
updated_at: 2026-02-26T02:12:07Z
source_host: docs-report.zendesk.com
---
# 
Send Sync Dialog Box Properties 

Use the Send Sync dialog box to customize the synchronization message you want to send out when selecting the object. This topic describes how to send synchronization message.

Server displays the dialog box when you right-click an object in a data component of a dashboard and select Send Sync > Customize from the shortcut menu.

Sender

Name of the trigger object from which Server sends out the synchronization message.

Add button

Select to add a new message line.

Remove button

Select to remove the selected message line.

Enable

Clear to disable a message.

- 
Lock button
 It indicates that the message is predefined in Report Designer.

Message Name

Type the name of a message. 

Message Type

Select the type of the message you want to send out.

- 
Filter
 Select Filter to send out the built-in Filter message, which will ask the data component who receives the message to filter itself according to the filter condition defined in the message.
    
- 
Column Name
          Select the field whose records you want to filter. To make the condition dynamic, select the values under the Dynamic Key node.

- 
Operator
Select the operator to compose the condition.

- 
Filter Value
Select the value of the field. To make the condition dynamic, select the values under the Dynamic Key node.

- 
Sort
  Select Sort to send out the built-in Sort message, which will ask the data component who receives the message to sort itself according to the sorting condition defined in the message.
    
- 
Sort On 
        Select the field whose records you want to sort. To make the condition dynamic, select the values under the Dynamic Key node.

- 
Sort Order 
        Select the Ascending or Descending order to sort the field.

- 
Parameter
Select Parameter to send out the built-in Parameter message, which will ask the library component containing the data component that receives the message to re-run itself using the parameter value defined in the message.
    
- 
Parameter Name  
        Select the name of the parameter. To make the condition dynamic, select the values under the Dynamic Key node.

- 
Parameter Value  
        Select the value of the parameter. To make the condition dynamic, select the values under the Dynamic Key node.

- 
On-screen Filter
    Select On-screen Filter to send out the built-in On-screen Filter message, which will ask the data component who receives the message to filter itself according to the filter condition defined in the message.
    
- 
Column Name
        Select the field on which to filter the records. To make the condition dynamic, select the values under the Dynamic Key node.

- 
Filter Value
         Select the value of the field. To make the condition dynamic, select the values under the Dynamic Key node.

- 
User Defined
    Select if you want to send out a user defined message.
      
- 
Add button
          Select to add a message key-value line.

- 
Remove button
 Select to remove the selected message key-value line.

- 
Key Name
          Select the key to the message.

- 
Value
          Select the value of the key.

OK

Select to send the message.

Cancel

Select to close the dialog box without sending the message.

Help button

Select to view information about the Send Sync dialog box.

Close button

Select to close the dialog box without sending the message.
