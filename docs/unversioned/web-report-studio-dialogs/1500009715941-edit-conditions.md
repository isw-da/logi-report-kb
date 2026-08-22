---
title: "Edit Conditions"
id: 1500009715941
section: "Web Report Studio Dialogs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009715941-Edit-Conditions
updated_at: 2021-11-03T06:57:26Z
---

# Edit Conditions

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009689762-Edit-Additional-Value)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009715961-Edit-Detail-Table)

# Edit Conditions

The Edit Conditions dialog helps you to add a new condition or edit an existing condition.
This dialog appears when you select the button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4412131380631/btn_add1.gif) or ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4412131399959/btn_pgrpt_edit.gif) in the [Conditional Formatting](https://devnet.logianalytics.com/hc/en-us/articles/1500009715741-Conditional-Formatting) dialog, or select the button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4412131380631/btn_add1.gif) or ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4412131385239/btn_wbrpt_edit.gif) in the [Insert Link](https://devnet.logianalytics.com/hc/en-us/articles/1500009716601-Insert-Link) dialog or [Edit Link](https://devnet.logianalytics.com/hc/en-us/articles/1500009689802-Edit-Link) dialog if the Conditional Link checkbox in the dialog is checked.

**Advanced/Basic**

Switches the dialog to the advanced/basic mode.

**OK**

Applies the settings and exits the dialog.

**Cancel**

Cancels the settings and closes the dialog.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4412139537431/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4412112572951/btn_close.gif)

Ignores the setting and closes this dialog.

## Basic Mode

The basic mode provides function for creating simple filter conditions which are connected by AND and OR operators.

![Edit Conditions dialog - Basic mode](https://devnet.logianalytics.com/hc/article_attachments/4412112517015/edtcndtn_basic.gif)

![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4412112514327/btn_pgrpt_no.gif)

Delete the current condition line.

**Field**

Specifies the field to be filtered.

**Operator**

Specifies the operator to compose the filter expression.

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
   Causes an enumerated list of values to appear in the WHERE clause predicate, used for evaluating for a true condition. For the operator "in" or "not in", multiple values separated by comma (,) are allowed.
* **[not] like**  
   Like string pattern matching operator is used to compare the first expression string value to the pattern string (the second expression). If you want to use wildcard character in the pattern string, only "\_" and "%" are supported.
* **[not] between**  
   Allows the system to evaluate whether or not data values are located between a range of values indicated in the predicate. For the operator "between" or "not between", there are two value text boxes for inputting the same type of values.
* **is [not] null**  
   It is used in WHERE clause predicates to match null values occurring in a specified data field. For the operator "is null" or "is not null", the value text box is hidden.

**Value**

Specifies the value of how to filter the field. You can either enter the value manually in the text box or select a value from the drop-down list. When you type in the value manually, if multiple values are required, they should be separated with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".

When you are editing conditional formatting on a field in a crosstab, the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4412112517271/btn_fmla1.gif) is available. Select the button and you can choose an object from the value drop-down list to use its value in the condition.

**Logic**

Lists the logic operator.

* **AND**  
   Logic operator AND which is applied to this and the next line.
* **OR**  
   Logic operator OR which is applied to this and the next line.

## Advanced Mode

The advanced mode enables the building of more complex filter conditions via the grouping of conditions.

![Edit Conditions dialog - Advanced mode](https://devnet.logianalytics.com/hc/article_attachments/4412139558423/edtcndtn_adv.gif)

**Add Condition**

Adds a new condition line.

**Delete**

Deletes the selected condition line.

**Group**

Makes the selected conditions in a group. Conditions can also be added to an existing group by selecting the conditions and the group while holding the Ctrl button, and then selecting the Group button.

**Ungroup**

Makes the selected condition ungrouped.

**Up**

Moves the selected condition or group up to a higher level.

**Down**

Moves the selected condition or group down to a lower level.

**Logic**

Specifies the logic operator.

* **AND**  
   Logic operator AND which is applied to this and the next line.
* **OR**  
   Logic operator OR which is applied to this and the next line
* **AND NOT**  
   Logic operator AND NOT which is applied to this and the next line.
* **OR NOT**   
   Logic operator OR NOT which is applied to this and the next line.

**Field**

Specifies the field to be filtered.

**Operator**

Specifies the [operator](#Operator) to compose the filter expression.

**Value**

Specifies the value of how to filter the field. You can either enter the value manually in the text box or select a value from the drop-down list. When you type in the value manually, if multiple values are required, they should be separated with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".

When you are editing conditional formatting on a field in a crosstab, the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4412112517271/btn_fmla1.gif) is available. Select the button and you can choose an object from the value drop-down list to use its value in the condition.

**Condition Expression**

Displays the SQL statement of the condition.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009689762-Edit-Additional-Value)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009715961-Edit-Detail-Table)
