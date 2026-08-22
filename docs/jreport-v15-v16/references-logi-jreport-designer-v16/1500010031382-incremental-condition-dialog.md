---
title: "Incremental Condition Dialog"
id: 1500010031382
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010031382-Incremental-Condition-Dialog
updated_at: 2021-07-24T10:38:41Z
---

# Incremental Condition Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010066841-Import-from-JReport-Server-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010066861-Information-Bus-Dialog)

# Incremental Condition Dialog

The Incremental Condition dialog helps you to specify conditions to [filter the incremental data](https://devnet.logianalytics.com/hc/en-us/articles/1500010069881-Refresh-Object-Properties#AutoRefresh). It appears when you select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404909121559/btn_chsr1.gif) in the value cell of the Incremental Fetch property of a refresh object in a library component in the Report Inspector.

![Incremental Condition dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909135767/incrmntlcndtn.gif)

The following are details about options in the dialog:

**Add Condition**

Adds a condition line.

**Delete**

Deletes the selected condition line.

**Group**

Makes the selected conditions in one group.

**Ungroup**

Makes the selected condition ungrouped.

**Up**

Moves the selected condition or group up to a higher level.

**Down**

Moves the selected condition or group down to a lower level.

**Field**

Specifies the business view element on which the filter condition is based. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404901122967/btn_chsr.gif) next to the text box to select the business view element.

**Operator**

Specifies the operator to compose the condition expression.

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
   Causes an enumerated list of values which will appear in the WHERE clause predicate to be evaluated for a true condition. For operator "in" or "not in", multiple values separated by comma (,) are allowed.
* **[not] like**  
   Like string pattern matching operator is used to compare the first expression string value to the pattern string (the second expression). If you want to use wildcard character in the pattern string, only "\_" and "%" are supported.
* **[not] between**  
   Allows the system to evaluate whether or not data values are located between a range of values indicated in the predicate. For operator "between" or "not between", there are two value text boxes for inputting the same type of values.
* **is [not] null**  
   It is used in WHERE clause predicates to match null values occurring in a specified data field. For operator "is null" or "is not null", the value text box is hidden.

**Value**

Specifies the value of how to filter the business view element. You can select ![](https://devnet.logianalytics.com/hc/article_attachments/4404901122967/btn_chsr.gif) next to the drop-down list to specify the value, type in the value manually, or select any of the following from the drop-down list.

* **MaxExistValue**  
   If selected, the maximum data value in the specified business view element from the last refresh time will be used as the value to filter the business view element.
* **MinExistValue**  
   If selected, the minimum data value in the specified business view element from the last refresh time will be used as the value to filter the business view element.
* **LastRefreshTime**  
   If selected, the previous refresh time will be used as the value to filter the business view element.

**SQL**

Statement Displays the SQL statement of the condition expression.

**OK**

Applies the changes and closes this dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010066841-Import-from-JReport-Server-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010066861-Information-Bus-Dialog)
