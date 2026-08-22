---
title: "Filter Dialog Box Properties"
id: 5741402520855
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741402520855-Filter-Dialog-Box-Properties
updated_at: 2022-10-31T17:16:15Z
---

# Filter Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741410480023-Fill-Effects-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741402536087-Filter-Control-Properties)

# Filter Dialog Box Properties

You can use the Filter dialog box to [set criteria for filtering records](https://devnet.logianalytics.com/hc/en-us/articles/5741469268887-Applying-Filters-to-Page-Report#Component) in a report.
This topic describes the properties in the dialog box.

**Advanced/Basic**

Select to switch between [advanced mode](#Advanced) or [basic mode](#Basic).

You see these elements in both modes:

**Apply to**

Select the data component to which you want to apply the filter.

**OK**

Select to apply any changes you made here and exit the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Apply**

Select to apply any changes you made here and regenerate the filter result.

**Reset**

Select to restore this dialog box to its opening status.

**Help**

Select to view information about the dialog box.

## Basic Mode

You can create simple filter conditions using the AND/OR logic.

![Filter dialog - Basic mode](https://devnet.logianalytics.com/hc/article_attachments/9905673720343/filter_basic.gif)

![Delete Condition Line](https://devnet.logianalytics.com/hc/article_attachments/9905575282199/btn_pgrpt_no.gif)**Remove button**

Select to delete the current condition line.

**Field**

Select the field you want to filter.

**Operator**

Select the [operator](https://devnet.logianalytics.com/hc/en-us/articles/5741449994391-Filter-Dialog-Box-Properties#Operator) to compose the filter expression.

**Value**

Specify the value of the field. You can either type the value manually in the text box or select a value from the list.

**Logic**

Select a logic operator.

* **AND**  
   Select to connect this line with the next line using the **AND** logic.
* **OR**  
   Select to connect this line with the next line using the **OR** logic.
* **END**  
   Select to end the whole condition expression.

## Advanced Mode

You can build more complex filter conditions by grouping conditions.

![Filter dialog - Advanced mode](https://devnet.logianalytics.com/hc/article_attachments/9905777488919/filter_advc.gif)

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

**Field**

Select the field you want to filter.

**Operator**

Select the [operator](https://devnet.logianalytics.com/hc/en-us/articles/5741449994391-Filter-Dialog-Box-Properties#Operator) to compose the filter expression.

**Value**

Specify the value of the field. You can either type the value manually in the text box or select a value from the list.

**Condition Expression**

Server displays the SQL statement of the filter condition.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741410480023-Fill-Effects-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741402536087-Filter-Control-Properties)
