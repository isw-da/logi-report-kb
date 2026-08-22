---
title: "Join Options Dialog"
id: 1500010067001
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010067001-Join-Options-Dialog
updated_at: 2021-07-24T10:38:38Z
---

# Join Options Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010031542-Insert-UDO-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010031582-JSON-Connection-Wizard-Dialog)

# Join Options Dialog

The Join Options dialog helps you to edit the conditions of a [catalog pre-join](https://devnet.logianalytics.com/hc/en-us/articles/1500010028522-Editing-Pre-joins-in-a-Catalog) or a [query join](https://devnet.logianalytics.com/hc/en-us/articles/1500010034642-Creating-Queries-in-a-Catalog#Join). It appears when you double-click the join icon ![Join button](https://devnet.logianalytics.com/hc/article_attachments/4404901142935/btn_join.gif) of the join.

![Join Options dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909131671/jnoptn.gif)

The following are details about options in the dialog:

**Join Mode**

Displays the mode of the join.

**Outer Join**

Specifies to make the join an [outer join](https://devnet.logianalytics.com/hc/en-us/articles/1500010028522-Editing-Pre-joins-in-a-Catalog#OuterJoin).

* **Left**  
   All rows are retrieved from the left table in a left outer join.
* **Right**  
   All rows are retrieved from the right table in a right outer join.
* **Full**  
   All rows are retrieved from both left and right tables in a full outer join.

**Condition**

Specifies the join conditions.

* **Join Table**  
   Displays the tables on which the join is set up.
* **Add Condition**  
   Adds a new condition line.
* **Delete**  
   Deletes the selected condition line.
* **Group**  
   Makes the selected conditions in one group. Conditions can also be added to an existing group by selecting the conditions and the group while holding the Ctrl button, and then selecting the Group button.
* **Ungroup**  
   Makes the selected condition ungrouped.
* **Up**  
   Moves the selected condition up to a higher level.
* **Down**  
   Moves the selected condition or group down to a lower level.
* **Logic**  
   Lists the logic operator.
  + **And**  
     Logic operator And which is applied between this and the next line or between more than two lines of a group.
  + **Or**  
     Logic operator Or which is applied to this and the next line.
  + **And Not**  
     Logic operator And Not which is applied to this and the next line.
  + **Or Not**  
     Logic operator Or Not which is applied to this and the next line.
* **Text boxes**  
   Specifies the objects to define the join condition. It can be a column in the two tables involved in the join, or a parameter or constant level formula in the current catalog data source. You can either select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404901122967/btn_chsr.gif) next to each text box to choose an object or type it in the text box manually. Parameters and formulas should be input in the format *@ParameterName* or *:ParameterName*.
* **Operator**  
  Specifies the operator to compose the join condition.
  + **=**  
     Equal to
  + **>**  
     Greater than
  + **<**  
     Less than
  + **>=**  
     Greater than or equal to
  + **<=**  
     Less than or equal to
  + **<>**  
     Not equal to
  + **[not] like**  
     Like string pattern matching operator is used to compare the first expression string value to the pattern string (the second expression). If you want to use wildcard character in the pattern string, only "\_" and "%" are supported.
  + **[not] in**  
     Causes an enumerated list of values to appear in the WHERE clause predicate, used for evaluating for a true condition. For the operator "in" or "not in", multiple values separated by comma (,) are allowed.
  + **[not] between**  
     Allows the system to evaluate whether or not data values are located between a range of values indicated in the predicate. For the operator "between" or "not between", there are two text boxes on the right for specifying the same type of values.
  + **is [not] null**  
     It is used in WHERE clause predicates to match null values occurring in a specified data field. For the operator "is null" or "is not null", the right text box is hidden.
* **SQL Statement**  
   Displays the SQL statement of the join condition.

**Delete Join**

Deletes the join.

**OK**

Applies the changes and closes the dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010031542-Insert-UDO-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010031582-JSON-Connection-Wizard-Dialog)
