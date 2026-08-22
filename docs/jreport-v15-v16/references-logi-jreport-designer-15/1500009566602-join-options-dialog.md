---
title: "Join Options Dialog"
id: 1500009566602
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009566602-Join-Options-Dialog
updated_at: 2021-07-24T05:55:04Z
---

# Join Options Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009587681-Insert-UDO-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009587721-JSON-Connection-Wizard-Dialog)

# Join Options Dialog

The Join Options dialog appears when you double-click the join icon ![Join button](https://devnet.logianalytics.com/hc/article_attachments/4404893822743/btn_join.gif) of a data source pre-join, a business view join or a query join. It helps you to edit the conditions of the specified join. [See the dialog](javascript:%20void(null)).

![Join Options dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889297175/jnoptn.gif)

The following are details about options in the dialog:

**Join Mode**

Displays the mode of the join.

**Outer Join**

Specifies to make the join an [outer join](https://devnet.logianalytics.com/hc/en-us/articles/1500009583161-Defining-the-Join-Relationships-Between-Resources#OuterJoin).

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
   Specifies the objects to define the join condition. It can be a column in the two tables involved in the join, or a parameter or constant level formula in the current catalog data source. You can either select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404889276567/btn_chsr.gif) next to each text box to choose an object or type it in the text box manually. Parameters and formulas should be input in the format *@ParameterName* or *:ParameterName*.
* **Operator**  
  Specifies the operator to compose the join condition.
  + **=**  
     Displays values that are equal to each other.
  + **>**  
     Displays values that are greater on the left side.
  + **<**  
     Displays values that are greater on the right side.
  + **>=**  
     Displays values that are greater than or equal to the left side.
  + **<=**  
     Displays values that are greater than or equal to the right side.
  + **<>**  
     Displays values that are not equal to each other.
  + **[not] like**  
     Like string pattern matching operator is used to compare the first expression string value to the pattern string (the second expression). If you want to use wildcard character in the pattern string, only "\_" and "%" are supported.
  + **[not] in**  
     Causes an enumerated list of values to appear in the WHERE clause predicate, used for evaluating for a true condition. For operator "in" or "not in", multiple values separated by comma (,) are allowed.
  + **[not] between**  
     Allows the system to evaluate whether or not data values are located between a range of values indicated in the predicate. For operator "between" or "not between", there are two value text boxes for inputting the same type of values.
  + **is [not] null**  
     It is used in WHERE clause predicates to match null values occurring in a specified data field. For operator "is null" or "is not null", the value text box is hidden.
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

**Related topics:**

> * [Defining the Join Relationships Between Resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009583161-Defining-the-Join-Relationships-Between-Resources)
> * [Joining Tables in a Query](https://devnet.logianalytics.com/hc/en-us/articles/1500009592501-Joining-Tables-in-a-Query)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009587681-Insert-UDO-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009587721-JSON-Connection-Wizard-Dialog)
