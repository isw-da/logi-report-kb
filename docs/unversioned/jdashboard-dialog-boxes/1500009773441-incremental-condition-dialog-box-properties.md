---
title: "Incremental Condition Dialog Box Properties"
id: 1500009773441
section: "JDashboard Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009773441-Incremental-Condition-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:57Z
---

# Incremental Condition Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009773421-Hyperlink-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009773461-Insert-Filter-Control-Dialog-Box-Properties)

# Incremental Condition Dialog Box Properties

Use the Incremental Condition dialog box to specify conditions to filter the incremental data. This topic describes how to define Incremental Condition.

JDashboard displays the dialog box when you select Incremental Condition in the [Auto Refresh](https://devnet.logianalytics.com/hc/en-us/articles/1500009745342-Auto-Refresh-Dialog-Box-Properties) dialog box.

**Advanced**/**Basic**

Select **Advanced** or **Basic** to switch to the [advanced mode](#Advanced) or [basic mode](#Basic).

**OK**

Select **OK** to apply any changes you made here.

**Cancel**

Select **Cancel** to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Select this button to view information about the Incremental Condition dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Select this button to close the dialog box without saving any changes.

## Basic Mode

Use the basic mode to create simple condition expressions with the AND and OR operators.

![Incremental Condition dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880449047/incrmntlcndtn_basic.gif)

![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404880189847/btn_pgrpt_no.gif)

Select this button to delete the current condition line.

**Field**

Select the drop-down button ![More button](https://devnet.logianalytics.com/hc/article_attachments/4404885319191/btn_dshbrd_more1.gif) next to the text box and then select the field that you want to filter.

**Operator**

Select an operator to compose the filter expression.

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
   Select if you want to match null values occurring in a specified data field in WHERE clause predicates. For the operator "is null" or "is not null", Logi Report hides the value text box.

**Value**

Specify the value of how to filter the field using one of the following ways:

* Type the value manually in the text box.
* Select a resource field from the drop-down list.
* Select the button ![Toggle button](https://devnet.logianalytics.com/hc/article_attachments/4404880449815/btn_dshbrd_toggle.gif) and then select a value from the drop-down list as the value.

When you type multiple values manually, you should separate them with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".

**Logic**

Select a logic operator **AND** or **OR** to apply to this and the next line.

## Advanced Mode

Use the advanced mode to build more complex condition expressions by grouping the conditions.

![Incremental Condition dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885528983/incrmntlcndtn_advanced.gif)

**Add Condition**

Select **Add Condition** to add a condition line.

**Delete**

Select **Delete** to delete the selected condition line.

**Group**

Select **Group** to add the selected conditions in one group. You can add conditions to an existing group by selecting the conditions and the group while holding the Ctrl button, and then selecting **Group**.

**Ungroup**

Select **Ungroup** to make the selected condition leave its group.

**Up**

Select **Up** to move the selected condition or group up to a higher level.

**Down**

Select **Down** to move the selected condition or group down to a lower level.

**Logic**

Select an logic operator to apply to this and the next line: **AND**, **OR**, **AND NOT**, or **OR NOT**.

**Field**

Select ![More button](https://devnet.logianalytics.com/hc/article_attachments/4404885319191/btn_dshbrd_more1.gif) next to the text box and then select the field that you want to filter.

**Operator**

Select the [operator](#Operator) to compose the condition expression.

**Value**

Specify the value of how to filter the field using one of the following ways:

* Type the value manually in the text box.
* Select a resource field from the drop-down list.
* Select the button ![Toggle button](https://devnet.logianalytics.com/hc/article_attachments/4404880449815/btn_dshbrd_toggle.gif) and then select a value from the drop-down list as the value.

When you type multiple values manually, you should separate them with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".

You see the following options:

* **MaxExistValue**  
   Select if you want to use the maximum data value in the selected business view element from the last refresh time as the value to filter the business view element.
* **MinExistValue**  
   Select if you want to use the minimum data value in the selected business view element from the last refresh time as the value to filter the business view element.
* **LastRefreshTime**  
   Select if you want to use the previous refresh time as the value to filter the business view element.

**Condition Expression**

SQL statement of the condition.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009773421-Hyperlink-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009773461-Insert-Filter-Control-Dialog-Box-Properties)
