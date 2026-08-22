---
title: "Edit Conditions"
id: 1500009647222
section: "References Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009647222-Edit-Conditions
updated_at: 2021-07-24T20:54:34Z
---

# Edit Conditions

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009647202-Edit-Additional-Value)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009671661-Edit-Detail-Table)

# Edit Conditions

The Edit Conditions dialog appears when you select the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385047/btn_add1.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404920401943/btn_pgrpt_edit.gif) in the [Conditional Formatting](https://devnet.logianalytics.com/hc/en-us/articles/1500009671561-Conditional-Formatting) dialog, or select the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385047/btn_add1.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385303/btn_wbrpt_edit.gif) in the [Insert Link](https://devnet.logianalytics.com/hc/en-us/articles/1500009672201-Insert-Link) dialog or [Edit Link](https://devnet.logianalytics.com/hc/en-us/articles/1500009671701-Edit-Link) dialog if the Conditional Link checkbox in the dialog is checked. It helps you to add a new condition or edit an existing condition, and has the following two modes:

* [Basic](#Basic)
* [Advanced](#Advanced)

**Advanced/Basic**

Switches the dialog to the advanced/basic mode.

**OK**

Applies the settings and exits the dialog.

**Cancel**

Cancels the settings and closes the dialog.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920501783/btn_help.gif)

Displays the help document about this feature.

![](https://devnet.logianalytics.com/hc/article_attachments/4404926700311/btn_close.gif)

Ignores the setting and closes this dialog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Basic Mode

The basic mode provides function for creating simple filter conditions which are connected by AND and OR operators. [See the dialog](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920549655/edtcndtn_basic.gif)

![](https://devnet.logianalytics.com/hc/article_attachments/4404920398359/btn_pgrpt_no.gif)

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
  Causes an enumerated list of values to appear in the WHERE clause predicate, used for evaluating for a true condition.
* **[not] like**  
   Like string pattern matching operator is used to compare the first expression string value to the pattern string (the second expression). If you want to use wildcard character in the pattern string, only "\_" and "%" are supported.
* **[not] between**  
   Allows the system to evaluate whether or not data values are located between a range of values indicated in the predicate.
* **is [not] null**  
   It is used in WHERE clause predicates to match null values occurring in a specified data field.

**Value**

Specifies the value of how to filter the field. You can either enter the value manually in the text box or select a value from the drop-down list. When you type in the value manually, if multiple values are required, they should be separated with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".

**Logic**

Lists the logic operator.

* **AND**  
   Logic operator AND which is applied to this and the next line.
* **OR**  
   Logic operator OR which is applied to this and the next line.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Advanced Mode

The advanced mode enables the building of more complex filter conditions via the grouping of conditions. [See the dialog](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920549911/edtcndtn_adv.gif)

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

**Condition Expression**

Displays the SQL statement of the condition.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009647202-Edit-Additional-Value)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009671661-Edit-Detail-Table)
