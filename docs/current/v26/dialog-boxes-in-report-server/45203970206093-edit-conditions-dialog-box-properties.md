---
title: "Edit Conditions Dialog Box Properties"
id: 45203970206093
section: "Dialog Boxes in Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203970206093-Edit-Conditions-Dialog-Box-Properties
updated_at: 2026-04-30T14:09:35Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Edit Conditions Dialog Box Properties

This topic describes how you can use the Edit Conditions dialog box to add a new condition or edit an existing condition.

Server displays the dialog box when you select the Add button  or Edit button  in the Conditional Formatting dialog box, or select  or  in the Insert Link dialog box or Edit Link dialog box if you have selected Conditional Link in the dialog box. 

Advanced/Basic

Select to switch between the advanced mode and basic mode.

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

You can create simple conditions using the AND/OR logic.

Remove button

Select to delete the current condition line.

Field

Select the field that you want to filter.

Operator

Select the operator to compose the expression. See Operator.

Value

Specify the value of the field. You can either type the value manually in the text box or select a value from the drop-down list. When you type multiple values manually, you should separate them with ",", and if "," or "\" is contained in the values, write it as "\," or "\\". 

When you are editing conditional formatting on a field in a crosstab, the the Toggle to Formula button button  is available. Select the button and you can choose a field from the value drop-down list to use its value in the condition. 

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

You can build more complex conditions by grouping conditions.

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

- line.

Field

Specify the field you want to filter.

Operator

Specify the operator to compose the expression.

Value

Specify the value of the field. You can either type the value manually in the text box or select a value from the drop-down list. When you type multiple values manually, you should separate them with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".

When you are editing conditional formatting on a field in a crosstab, the button  is available. Select the button and you can choose an object from the value drop-down list to use its value in the condition.

Condition Expression

Server displays the SQL statement of the condition.
