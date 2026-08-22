---
title: "Table Filter Condition Dialog"
id: 1500009610622
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009610622-Table-Filter-Condition-Dialog
updated_at: 2021-07-24T16:04:03Z
---

# Table Filter Condition Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009610522-Suppress-Row-Subtotals-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009610642-Table-Type-Dialog)

# Table Filter Condition Dialog

The Table Filter Condition dialog helps you [filter a query based on a specified table](https://devnet.logianalytics.com/hc/en-us/articles/1500009635981-Creating-Queries-in-a-Catalog#Filter). It appears when you select ![Table Filter button](https://devnet.logianalytics.com/hc/article_attachments/4404911636247/btn_tblfltr.gif) on the title bar of a table in the [Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009609882-Query-Editor-Dialog).

![Table Filter Condition dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904238487/tblfltrcndtn.gif)

The following are details about option in the dialog:

**Add Condition**

Adds a new condition line.

**Delete**

Deletes the selected condition line.

**Group**

Makes the selected conditions in one group. Conditions can also be added to an existing group by selecting the conditions and the group while holding the Ctrl button, and then selecting the Group button.

**Ungroup**

Makes the selected condition ungrouped.

**Up**

Moves the selected condition up to a higher level.

**Down**

Moves the selected condition or group down to a lower level.

**Logic**

Lists the logic operator.

* **And**  
   Logic operator And which is applied to this and the next line.
* **Or**  
   Logic operator Or which is applied to this and the next line.
* **And Not**  
   Logic operator And Not which is applied to this and the next line.
* **Or Not**  
   Logic operator Or Not which is applied to this and the next line.

**Field**

Specifies the field to be filtered. You can either type in the field manually or select **![](https://devnet.logianalytics.com/hc/article_attachments/4404904178967/btn_chsr.gif)** to specify the field in the [Expressions](https://devnet.logianalytics.com/hc/en-us/articles/1500009631041-Expressions-Dialog) dialog.

**Operator**

Lists all the operators that can be used in the filter condition:

* **=**  
   Equal to
* **>**  
   Greater than
* **<**  
   Less than
* **>=**  
   Greater than or equal to
* **<=**  
   Less than or equal to
* **<>**  
   Not equal to
* **[not] between**  
   Allows the system to evaluate whether or not data values are located between a range of values indicated in the predicate. For the operator "between" or "not between", there are two value text boxes for inputting the same type of values.
* **[not] exists**  
   It is used to test if a subselect retrieves any records.
* **[not] in**  
   Causes an enumerated list of values to appear in the WHERE clause predicate, used for evaluating for a true condition. For the operator "in" or "not in", multiple values separated by comma (,) are allowed.
* **[not] like**  
   Like string pattern matching operator is used to compare the first expression string value to the pattern string (the second expression). If you want to use wildcard character in the pattern string, only "\_" and "%" are supported.
* **sounds like**  
   Sound like operator uses a soundex algorithm to pattern match strings that sound alike.
* **is [not] null**  
   It is used in WHERE clause predicates to match null values occurring in a specified data column. For the operator "is null" or "is not null", the value text box is hidden.

**Value**

Specifies the value of how to filter the field. You can either type the value in the text box manually or select ![](https://devnet.logianalytics.com/hc/article_attachments/4404904178967/btn_chsr.gif) next to the text box to specify the value using the [Expressions](https://devnet.logianalytics.com/hc/en-us/articles/1500009631041-Expressions-Dialog) dialog.

**SQL Statement**

Displays the SQL statement of the filter condition.

**OK**

Applies all changes and closes the dialog.

**Cancel**

Closes the dialog, leaving any changes unsaved.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009610522-Suppress-Row-Subtotals-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009610642-Table-Type-Dialog)
