---
title: "Join Options Dialog Box"
id: 1500010097781
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010097781-Join-Options-Dialog-Box
updated_at: 2021-07-23T19:15:41Z
---

# Join Options Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010097741-Insert-UDO-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010097801-JSON-Connection-Wizard-Dialog-Box)

# Join Options Dialog Box

You can use the Join Options dialog box to edit the conditions of a [catalog pre-join](https://devnet.logianalytics.com/hc/en-us/articles/1500010094041-Editing-Pre-joins-in-a-Catalog) or a [query join](https://devnet.logianalytics.com/hc/en-us/articles/1500010062582-Creating-Queries-in-a-Catalog#Join). This topic describes the options in the dialog box.

Designer displays the Join Options dialog box when you double-click the join icon ![Join button](https://devnet.logianalytics.com/hc/article_attachments/4404848434327/btn_join.gif) of the join.

![Join Options dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848434711/jnoptn.gif)

You see the following options in the dialog box:

**Join Mode**

The text box shows the mode of the join.

**Outer Join**

Select to make the join an [outer join](https://devnet.logianalytics.com/hc/en-us/articles/1500010094041-Editing-Pre-joins-in-a-Catalog#OuterJoin).

* **Left**  
  Select to retrieve all rows from the left table in a left outer join.
* **Right**  
  Select to retrieve all rows from the right table in a right outer join.
* **Full**  
  Select to retrieve all rows from both left and right tables in a full outer join.

**Condition**

You can specify the conditions of the join in the panel.

* **Join Table**  
  The option shows the tables on which to set up the join.
* **Add Condition**  
  Select to add a new condition line.
* **Delete**  
  Select to remove the specified condition line.
* **Group**  
  Select to add the specified conditions in one group. You can also add conditions to an existing group by selecting the conditions and the group while holding the Ctrl button, and then selecting the Group button.
* **Ungroup**  
  Select to ungroup the specified conditions.
* **Up**  
  Select to move the specified condition up to a higher level.
* **Down**  
  Select to move the specified condition or group down to a lower level.
* **Logical operator drop-down menu**  
  Specify the logical operator to apply for the specified condition lines. It can be
  "And", "Or", "And Not", or "Or Not".
* **Text boxes**  
  Specify the objects to define the join condition. It can be a column in the two tables involved in the join, or a parameter or constant level formula in the current catalog data source. You can either select the ellipsis button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404848397591/btn_ellipsis.gif) next to each text box to choose an object or type it in the text box. You should reference parameters and formulas in the format *@ParameterName* or *:ParameterName*.
* **Operator drop-down list**  
  Specify the operator to compose the join condition.

+ **=**  
  Equal to
+ **>=**  
  Greater than or equal to
+ **>**  
  Greater than
+ **<**  
  Less than
+ **<=**  
  Less than or equal to
+ **!=**/**<>**  
  Not equal to
+ **[not] in**  
  The operator causes an enumerated list of values to appear in the WHERE clause predicate, and is used for evaluating for a true condition. For the operator "in" or "not in", you can use multiple values separated by comma (,).
+ **[not] like**  
  The like string pattern matching operator is used to compare the first expression string value to the pattern string (the second expression). If you want to use wildcard character in the pattern string, you can only use "\_" and "%".
+ **[not] between**  
  The operator allows the system to evaluate whether or not data values are located between a range of values indicated in the predicate. For the operator "between" or "not between", Designer displays two value text boxes for inputting the same type of values.
+ **is [not] null**  
  The operator is used in the WHERE clause predicates to match null values occurring in a specified data field. For the operator "is null" or "is not null", Designer does not display the value text box.

* **SQL Statement**  
  The box displays the SQL statement of the join conditions.

**Delete Join**

Select to delete the join.

**OK**

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010097741-Insert-UDO-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010097801-JSON-Connection-Wizard-Dialog-Box)
