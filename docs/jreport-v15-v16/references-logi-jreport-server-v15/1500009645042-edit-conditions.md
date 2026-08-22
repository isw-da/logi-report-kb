---
title: "Edit Conditions"
id: 1500009645042
section: "References Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009645042-Edit-Conditions
updated_at: 2021-07-24T20:55:12Z
---

# Edit Conditions

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009645062-Edit-Aggregation)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009669581-Edit-Filter-Control)

# Edit Conditions

The Edit Conditions dialog helps you to [edit a condition for adding conditional format](https://devnet.logianalytics.com/hc/en-us/articles/1500009649402-Adding-Conditional-Formats-to-Fields). It contains the following two modes:

* [Basic](#Basic)
* [Advanced](#Advanced)

**Advanced/Basic**

Switches the dialog to the advanced/basic mode.

**OK**

Applies the settings and exits the dialog.

**Cancel**

Cancels the settings and closes the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Basic Mode

The basic mode provides function for creating simple filter conditions which are connected by the AND and OR operators. [See the dialog](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920465303/edtcndtn_basic.gif)

![](https://devnet.logianalytics.com/hc/article_attachments/4404920398359/btn_pgrpt_no.gif)

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

**Logic**

Lists the logic operator.

* **AND**  
   Logic operator AND which is applied to this and the next line.
* **OR**  
   Logic operator OR which is applied to this and the next line.
* **END**  
   When this is the last line, use END to end the whole condition expression.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Advanced Mode

The advanced mode enables the building of more complex filter conditions via the grouping of conditions. [See the dialog](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920637207/edtcndtn_adv.gif)

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

**Condition Expression**

Displays the SQL statement of the filter condition.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009645062-Edit-Aggregation)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009669581-Edit-Filter-Control)
