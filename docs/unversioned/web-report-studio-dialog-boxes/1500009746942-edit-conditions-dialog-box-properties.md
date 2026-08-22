---
title: "Edit Conditions Dialog Box Properties"
id: 1500009746942
section: "Web Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009746942-Edit-Conditions-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:31Z
---

# Edit Conditions Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746922-Edit-Additional-Value-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009746962-Edit-Detail-Table-Dialog-Box-Properties)

# Edit Conditions Dialog Box Properties

This topic describes how you can use the Edit Conditions dialog box to add a new condition or edit an existing condition.

Server displays the dialog box when you select the button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404880163351/btn_add1.gif) or ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404880196759/btn_pgrpt_edit.gif) in the [Conditional Formatting](https://devnet.logianalytics.com/hc/en-us/articles/1500009746762-Conditional-Formatting-Dialog-Box-Properties) dialog box, or select the button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404880163351/btn_add1.gif) or ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404880163863/btn_wbrpt_edit.gif) in the [Insert Link](https://devnet.logianalytics.com/hc/en-us/articles/1500009747642-Insert-Link-Dialog-Box-Properties) dialog box or [Edit Link](https://devnet.logianalytics.com/hc/en-us/articles/1500009775181-Edit-Link-Dialog-Box-Properties) dialog box if you have selected the Conditional Link check box in the dialog box.

**Advanced/Basic**

Switches the dialog box to the [advanced mode](#Advanced)/[basic mode](#Basic).

**OK**

Applies the settings and exits the dialog box.

**Cancel**

Cancels the settings and closes the dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Ignores the setting and closes this dialog box.

## Basic Mode

The basic mode provides function for creating simple filter conditions which are connected by AND and OR operators.

![Edit Conditions dialog - Basic mode](https://devnet.logianalytics.com/hc/article_attachments/4404880196119/edtcndtn_basic.gif)

![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404880189847/btn_pgrpt_no.gif)

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
   Allows the system to evaluate whether data values are located between a range of values indicated in the predicate. For the operator "between" or "not between", there are two value text boxes for typing the same type of values.
* **is [not] null**  
   It is used in WHERE clause predicates to match null values occurring in a specified data field. For the operator "is null" or "is not null", the value text box is hidden.

**Value**

Specifies the value of how to filter the field. You can either type the value manually in the text box or select a value from the drop-down list. When you type multiple values manually, you should separate them with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".

When you are editing conditional formatting on a field in a crosstab, the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404880196503/btn_fmla1.gif) is available. Select the button and you can choose an object from the value drop-down list to use its value in the condition.

**Logic**

Lists the logic operator.

* **AND**  
   Logic operator AND which is applied to this and the next line.
* **OR**  
   Logic operator OR which is applied to this and the next line.

## Advanced Mode

The advanced mode enables the building of more complex filter conditions via the grouping of conditions.

![Edit Conditions dialog - Advanced mode](https://devnet.logianalytics.com/hc/article_attachments/4404885488407/edtcndtn_adv.gif)

**Add Condition**

Adds a new condition line.

**Delete**

Deletes the selected condition line.

**Group**

Makes the selected conditions in a group. You can add conditions to an existing group by selecting the conditions and the group while holding the Ctrl button, and then selecting the Group button.

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

Specifies the value of how to filter the field. You can either type the value manually in the text box or select a value from the drop-down list. When you type multiple values manually, you should separate them with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".

When you are editing conditional formatting on a field in a crosstab, the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404880196503/btn_fmla1.gif) is available. Select the button and you can choose an object from the value drop-down list to use its value in the condition.

**Condition Expression**

Displays the SQL statement of the condition.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746922-Edit-Additional-Value-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009746962-Edit-Detail-Table-Dialog-Box-Properties)
