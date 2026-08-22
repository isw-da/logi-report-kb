---
title: "Edit Conditions"
id: 1500009712961
section: "Page Report Studio Dialogs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009712961-Edit-Conditions
updated_at: 2021-11-03T06:58:16Z
---

# Edit Conditions

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009712941-Edit-Aggregation)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009712981-Edit-Filter-Control)

# Edit Conditions

The Edit Conditions dialog helps you to [edit a condition for adding conditional format](https://devnet.logianalytics.com/hc/en-us/articles/1500009691622-Adding-Conditional-Formats-to-Fields).

**Advanced/Basic**

Switches the dialog to the advanced/basic mode.

**OK**

Applies the settings and exits the dialog.

**Cancel**

Cancels the settings and closes the dialog.

**Help**

Displays the help document about this feature.

## Basic Mode

The basic mode provides function for creating simple filter conditions which are connected by the AND and OR operators.

![Edit Conditions dialog - Basic mode](https://devnet.logianalytics.com/hc/article_attachments/4412131425943/edtcndtn_basic.gif)

![Delete Condition Line](https://devnet.logianalytics.com/hc/article_attachments/4412112514327/btn_pgrpt_no.gif)

Deletes the current condition line. Each condition line contains an expression with a logic operator which either connects the current expression with the following one or ends when it is the last line. An expression is composed of a field, an operator, and a value.

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

**Value**

Specifies the value of how to filter the field. You can either enter the value manually in the text box or select a value from the drop-down list. When you type in the value manually, if multiple values are required, they should be separated with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".

When you are editing conditional formatting on a field in a crosstab, the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4412112517271/btn_fmla1.gif) is available. Select the button and you can choose an object from the value drop-down list to use its value in the condition.

**Logic**

Lists the logic operator.

* **AND**  
   Logic operator AND which is applied to this and the next line.
* **OR**  
   Logic operator OR which is applied to this and the next line.
* **END**  
   When this is the last line, use END to end the whole condition expression.

## Advanced Mode

The advanced mode enables the building of more complex filter conditions via the grouping of conditions.

![Edit Conditions dialog - Advanced mode](https://devnet.logianalytics.com/hc/article_attachments/4412112627479/edtcndtn_adv.gif)

**Add Condition**

Adds a new condition line. Each condition line contains an expression which is composed of a field, an operator, and a value.

**Delete**

Deletes the selected condition lines and groups.

**Group**

Makes the selected condition lines become a group. A group can have one logic operator to connect all of its condition lines, for example, a group contains three conditions lines which are expression A, B and C and the group's logic operator is OR, then the group's expression is: A OR B OR C.

Condition lines can also be added to an existing group by selecting the condition lines and the group while holding the Ctrl button, and then selecting the Group button.

**Ungroup**

Makes the selected condition lines and groups out of a group or disbands a group.

**Up**

Moves the selected condition line or group up to a higher level.

**Down**

Moves the selected condition line or group down to a lower level.

**Logic**

Specifies the logic operator of a condition group. By selecting the logic button the following items will be rolled one by one.

* **AND**  
   Logic operator AND which is used to connect all of the condition lines in the group.
* **OR**  
   Logic operator OR which is used to connect all of the condition lines in the group.
* **AND NOT**   
   Logic operator AND NOT which is used to connect all of the condition lines in the group.
* **OR NOT**   
   Logic operator OR NOT which is used to connect all of the condition lines in the group.

**Field**

Specifies the field to be filtered.

**Operator**

Specifies the [operator](#Operator) to compose the filter expression.

**Value**

Specifies the value of how to filter the field. You can either enter the value manually in the text box or select a value from the drop-down list. When you type in the value manually, if multiple values are required, they should be separated with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".

When you are editing conditional formatting on a field in a crosstab, the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4412112517271/btn_fmla1.gif) is available. Select the button and you can choose an object from the value drop-down list to use its value in the condition.

**Condition Expression**

Displays the SQL statement of the filter condition.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009712941-Edit-Aggregation)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009712981-Edit-Filter-Control)
