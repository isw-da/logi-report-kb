---
title: "Incremental Condition Dialog Box Properties"
id: 28891514180237
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891514180237-Incremental-Condition-Dialog-Box-Properties
updated_at: 2026-02-26T02:12:02Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Incremental Condition Dialog Box Properties 

You can use the Incremental Condition dialog box to specify conditions to filter the incremental data. This topic describes the properties in the dialog box.

Server displays the dialog box when you select Incremental Condition in the Auto Refresh dialog box.

Advanced/Basic

Select to switch between advanced mode or basic mode. 

You see these elements in both modes:

OK

Select to apply any changes you made here and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help button

Select to view information about the dialog box.

Close button

Select to close the dialog box without saving any changes.

## 
Basic Mode

You can create simple filter conditions using the AND/OR logic.

Remove button

Select to remove the current condition line.

Field

Select the arrow button  next to the text box, and then select the field that you want to filter.

Operator

Select the operator to compose the filter expression.

Value

Specify the value of the field using one of the following ways:

- Select a field from the value list. You see these items in the value list:
			  
- 
MaxExistValue
    Select if you want to use the maximum data value in the selected business view element from the last refresh time as the value to filter the business view element.

- 
MinExistValue
 Select if you want to use the minimum data value in the selected business view element from the last refresh time as the value to filter the business view element. 

- 
LastRefreshTime
 Select if you want to use the previous refresh time as the value to filter the business view element.

- Type the value manually in the text box. When you type multiple values, you should separate them with a comma",". If you want to include a comma "," or a backslash "\" in the values, write it as "\," or "\\".

- Select the Toggle to Normal button  and select a value from the list. When you see More... at the end of the value list, you can select it to open the Select Values dialog box, which lists more values, and select the values you want.

Logic

Select a logic operator.

- 
AND

 Select to connect this line with the next line using the AND logic.

- 
OR

 Select to connect this line with the next line using the OR logic.

- 
END

 Select to end the whole condition expression.

## 
Advanced Mode 

You can build more complex condition expressions by grouping the conditions.

Add Condition

Select to add a new condition line. Each condition line contains an expression which is composed of a field, an operator, and a value.

Delete

Select to delete the selected condition lines or groups.

Group

Select to make the selected condition lines become a group. A group can only have one logic operator to connect all its condition lines. For example, a group contains three conditions lines, which are expression A, B, and C, and the group's logic operator is OR, then the group's expression is: A OR B OR C.

You can also add condition lines to an existing group. Select the condition lines and the group while selecting Ctrl, and then select Group.

Ungroup

Select to move the selected condition lines and groups out of a group or disband a group. 

Up

Select to move the selected condition line or group higher.

Down

Select to move the selected condition line or group lower.

Logic

Specify the logic operator of a condition group. Each time you select the logic button, Server displays the next item following the order below.

- 
AND

  Select to connect all the condition lines and groups in the group using the AND logic.

- 
OR

     Select to connect all the condition lines and groups in the group using the OR logic.

- 
AND NOT 

  Select to connect all the condition lines and groups in the group using the AND NOT logic.

- 
OR NOT 

     Select to connect all the condition lines and groups in the group using the OR NOT logic.

Field

Select the arrow button  next to the text box, and then select the field that you want to filter.

Operator

Select the operator to compose the condition expression.

Value 

Specify the value of the field.

Condition Expression

Server displays the SQL statement of the filter condition.
