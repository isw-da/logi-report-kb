---
title: "Filter Dialog Box Properties"
id: 5741449994391
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741449994391-Filter-Dialog-Box-Properties
updated_at: 2022-10-31T17:17:23Z
---

# Filter Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741423011735-Filter-Control-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741429092119-Filter-Inspector-Dialog-Box-Properties)

# Filter Dialog Box Properties

You can use the Filter dialog box to set criteria for [filtering records](https://devnet.logianalytics.com/hc/en-us/articles/5741470839191-Applying-Filters-in-Web-Report#Dialog).
This topic describes the properties in the dialog box.

Server displays the dialog box when you select Menu > Edit > Filter, or the **Filter** button ![Filter button](https://devnet.logianalytics.com/hc/article_attachments/9905578238359/btn_filter.gif) on the toolbar.

**Advanced/Basic**

Select to switch between [advanced mode](#Advanced) or [basic mode](#Basic).

You see these elements in both modes:

**Apply to**

Select the data component which you want to apply the filter to.

**Inspector**

Select to open the [Filter Inspector dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741429092119-Filter-Inspector-Dialog-Box-Properties).

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

## Basic Mode

You can create simple filter conditions using the AND/OR logic.

![Filter dialog box - Basic mode](https://devnet.logianalytics.com/hc/article_attachments/9905654923287/fltr_basic.gif)

![Delete button](https://devnet.logianalytics.com/hc/article_attachments/9905575282199/btn_pgrpt_no.gif)**Remove button**

Select to delete the current condition line.

**Field**

Select the field you want to filter.

**Operator**

Select the operator to compose the filter expression.

* **=**  
   Equal to
* **>**  
   Greater than
* **>=**  
   Greater than or equal to
* **<**  
   Less than
* **<=**  
   Less than or equal to
* **!=**  
   Not equal to
* **[not] in**  
   Select if you want to display an enumerated list of values in the WHERE clause predicate, for evaluating for a true condition. You can separate multiple values by comma (,).
* **[not] like**  
  Select if you want to compare the first expression string value to the pattern string (the second expression). To use wildcard character in the pattern string, you can only use "\_" and "%".
* **[not] between**  
   Select if you want the system to evaluate whether data values are between a range of values in the predicate. You can use the two value text boxes for typing the same type of values.
* **is [not] null**  
   Select if you want to match null values occurring in a specified data field in WHERE clause predicates. For the operator "is null" or "is not null", Server hides the value text box.

**Value**

Specify the value of the field using one of the following ways:

* Select a value from the list. When you see **More...** at the end of the value list, you can select it to open the [Select Values dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741446661015-Select-Values-Dialog-Box-Properties), which lists more values, and select the values you want.
* Type the value manually in the text box. When you type multiple values, you should separate them with a comma",". If you want to include a comma "," or a backslash "\" in the values, write it as "\," or "\\".
* Select the **Toggle to Parameter** button ![Enter Parameter Values button](https://devnet.logianalytics.com/hc/article_attachments/9905575308823/btn_dshbrd_prm.gif) and select a parameter from the list.

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

![Filter dialog box - Advanced mode](https://devnet.logianalytics.com/hc/article_attachments/9905755401495/fltr_adv.gif)

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

Select the [operator](#Operator) to compose the filter expression.

**Value**

Specify the value of the field using one of the following ways:

* Select a value from the list. When you see **More...** at the end of the value list, you can select it to open the [Select Values dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741446661015-Select-Values-Dialog-Box-Properties), which lists more values, and select the values you want.
* Type the value manually in the text box. When you type multiple values, you should separate them with a comma",". If you want to include a comma "," or a backslash "\" in the values, write it as "\," or "\\".
* Select the **Toggle to Parameter** button ![Enter Parameter Values button](https://devnet.logianalytics.com/hc/article_attachments/9905575308823/btn_dshbrd_prm.gif) and select a parameter from the list.

**Condition Expression**

Server displays the SQL statement of the filter condition.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741423011735-Filter-Control-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741429092119-Filter-Inspector-Dialog-Box-Properties)
