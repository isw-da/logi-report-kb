---
title: "Edit Conditions Dialog Box Properties"
id: 4405683809047
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683809047-Edit-Conditions-Dialog-Box-Properties
updated_at: 2022-01-27T07:59:14Z
---

# Edit Conditions Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690575511-Edit-Additional-Value-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683810071-Edit-Detail-Table-Dialog-Box-Properties)

# Edit Conditions Dialog Box Properties

This topic describes how you can use the Edit Conditions dialog box to add a new condition or edit an existing condition.

Server displays the dialog box when you select the Add button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420447073687/btn_add1.gif) or Edit button ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4420461515287/btn_pgrpt_edit.gif) in the [Conditional Formatting dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683796631-Conditional-Formatting-Dialog-Box-Properties), or select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420447073687/btn_add1.gif) or ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4420447073943/btn_wbrpt_edit.gif) in the [Insert Link dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683857175-Insert-Link-Dialog-Box-Properties) or [Edit Link dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683813143-Edit-Link-Dialog-Box-Properties) if you have selected **Conditional Link** in the dialog box.

**Advanced/Basic**

Select to switch between the [advanced mode](#Advanced) and [basic mode](#Basic).

You see these elements in both modes:

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4420447202071/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420447202455/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

## Basic Mode

You can create simple conditions using the AND/OR logic.

![Edit Conditions dialog - Basic mode](https://devnet.logianalytics.com/hc/article_attachments/4420447094167/edtcndtn_basic.gif)

![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4420447089175/btn_pgrpt_no.gif)**Remove button**

Select to delete the current condition line.

**Field**

Select the field that you want to filter.

**Operator**

Select the operator to compose the expression. See [Operator](https://devnet.logianalytics.com/hc/en-us/articles/4405683818007-Filter-Dialog-Box-Properties#Operator).

**Value**

Specify the value of the field. You can either type the value manually in the text box or select a value from the drop-down list. When you type multiple values manually, you should separate them with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".

When you are editing conditional formatting on a field in a crosstab, the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4420447094423/btn_fmla1.gif) is available. Select the button and you can choose an object from the value drop-down list to use its value in the condition.

**Logic**

Select a logic operator.

* **AND**  
   Select to connect this line with the next line using the **AND** logic.
* **OR**  
   Select to connect this line with the next line using the **OR** logic.
* **END**  
   Select to end the whole condition expression.

## Advanced Mode

You can build more complex conditions by grouping conditions.

![Edit Conditions dialog - Advanced mode](https://devnet.logianalytics.com/hc/article_attachments/4420453585047/edtcndtn_adv.gif)

**Add Condition**

Select to add a new condition line. Each condition line contains an expression which is composed of a field, an operator, and a value.

**Delete**

Select to delete the selected condition lines or groups.

**Group**

Select to make the selected condition lines become a group. A group can only have one logic operator to connect all its condition lines. For example, a group contains three conditions lines, which are expression A, B, and C, and the group's logic operator is OR, then the group's expression is: A OR B OR C.

You can also add condition lines to an existing group. Select the condition lines and the group while selecting **Ctrl**, and then select **Group**.

**Ungroup**

Select to move the selected condition lines and groups out of a group or disband a group.

**Up**

Select to move the selected condition line or group higher.

**Down**

Select to move the selected condition line or group lower.

**Logic**

Specify the logic operator of a condition group. Each time you select the logic button, Server displays the next item following the order below.

* **AND**  
   Select to connect all the condition lines and groups in the group using the **AND** logic.
* **OR**  
   Select to connect all the condition lines and groups in the group using the **OR** logic.
* **AND NOT**   
   Select to connect all the condition lines and groups in the group using the **AND NOT** logic.
* **OR NOT**   
   Select to connect all the condition lines and groups in the group using the **OR NOT** logic.

* line.

**Field**

Specify the field you want to filter.

**Operator**

Specify the [operator](#Operator) to compose the expression.

**Value**

Specify the value of the field. You can either type the value manually in the text box or select a value from the drop-down list. When you type multiple values manually, you should separate them with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".

When you are editing conditional formatting on a field in a crosstab, the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4420447094423/btn_fmla1.gif) is available. Select the button and you can choose an object from the value drop-down list to use its value in the condition.

**Condition Expression**

Server displays the SQL statement of the condition.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690575511-Edit-Additional-Value-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683810071-Edit-Detail-Table-Dialog-Box-Properties)
