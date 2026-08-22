---
title: "Incremental Condition"
id: 1500009720162
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009720162-Incremental-Condition
updated_at: 2021-07-25T07:19:49Z
---

# Incremental Condition

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009720142-Hyperlink)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009720182-Insert-Filter-Control)

# Incremental Condition

The Incremental Condition dialog box is used to specify conditions to filter the incremental data. It appears when you select Incremental Condition in the [Auto Refresh](https://devnet.logianalytics.com/hc/en-us/articles/1500009746741-Auto-Refresh) dialog box.

**Advanced**/**Basic**

Switches the dialog box to the [advanced mode](#Advanced)/[basic mode](#Basic).

**OK**

Applies the settings and exits the dialog box.

**Cancel**

Cancels the settings and closes the dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404936816535/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404942519575/btn_close.gif)

Ignores the setting and closes this dialog box.

## Basic Mode

The basic mode provides the function for creating simple condition expressions which are connected by AND and OR operators.

![Incremental Condition dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942571671/incrmntlcndtn_basic.gif)

![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404936748823/btn_pgrpt_no.gif)

Delete the current condition line.

**Field**

Specifies the field to be filtered. Select ![More button](https://devnet.logianalytics.com/hc/article_attachments/4404942452631/btn_dshbrd_more1.gif) next to the text box to select the field.

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
   Allows the system to evaluate whether or not data values are located between a range of values indicated in the predicate. For the operator "between" or "not between", there are two value text boxes for typing the same type of values.
* **is [not] null**  
   It is used in WHERE clause predicates to match null values occurring in a specified data field. For the operator "is null" or "is not null", the value text box is hidden.

**Value**

Specifies the value of how to filter the field. You can either type the value manually in the text box or select a resource field from the drop-down list, or select the button ![Toggle button](https://devnet.logianalytics.com/hc/article_attachments/4404942571927/btn_dshbrd_toggle.gif) and then select value from the drop-down list as the value. When you type the value manually, if multiple values are required, they should be separated with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".

**Logic**

Lists the logic operator.

* **AND**  
   Logic operator AND which is applied to this and the next line.
* **OR**  
   Logic operator OR which is applied to this and the next line.

## Advanced Mode

The advanced mode enables the building of more complex condition expressions via the grouping of conditions.

![Incremental Condition dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942572183/incrmntlcndtn_advanced.gif)

**Add Condition**

Adds a condition line.

**Delete**

Deletes the selected condition line.

**Group**

Makes the selected conditions in one group. Conditions can also be added to an existing group by selecting the conditions and the group while holding the Ctrl button, and then selecting the Group button.

**Ungroup**

Makes the selected condition ungrouped.

**Up**

Moves the selected condition or group up to a higher level.

**Down**

Moves the selected condition or group down to a lower level.

**Logic**

Specifies the logic operator.

* **AND**  
   Logic operator And which is applied to this and the next line.
* **OR**  
   Logic operator Or which is applied to this and the next line.
* **AND NOT**  
   Logic operator And Not which is applied to this and the next line.
* **OR NOT**  
   Logic operator Or Not which is applied to this and the next line.

**Field**

Specifies the field to be filtered. Select ![More button](https://devnet.logianalytics.com/hc/article_attachments/4404942452631/btn_dshbrd_more1.gif) next to the text box to select the field.

**Operator**

Specifies the [operator](#Operator) to compose the condition expression.

**Value**

Specifies the value of how to filter the field. You can either type the value manually in the text box or select a resource field from the drop-down list, or select the button![Toggle button](https://devnet.logianalytics.com/hc/article_attachments/4404942571927/btn_dshbrd_toggle.gif)and then select value from the drop-down list as the value. When you type the value manually, if multiple values are required, they should be separated with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".

* **MaxExistValue**  
   If selected, the maximum data value in the selected business view element from the last refresh time will be used as the value to filter the business view element.
* **MinExistValue**  
   If selected, the minimum data value in the selected business view element from the last refresh time will be used as the value to filter the business view element.
* **LastRefreshTime**  
   If selected, the previous refresh time will be used as the value to filter the business view element.

**Condition Expression**

Displays the SQL statement of the condition.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009720142-Hyperlink)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009720182-Insert-Filter-Control)
