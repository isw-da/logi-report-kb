---
title: "Incremental Condition Dialog Box"
id: 4405664520343
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664520343-Incremental-Condition-Dialog-Box
updated_at: 2022-01-27T20:35:22Z
---

# Incremental Condition Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661620887-Imported-SQL-Editor-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661623063-Information-Bus-Dialog-Box)

# Incremental Condition Dialog Box

You can use the Incremental Condition dialog box to specify conditions to [filter the incremental data](https://devnet.logianalytics.com/hc/en-us/articles/4405661885207-Refresh-Object-Properties#AutoRefresh). This topic describes the options in the dialog box.

Designer displays the Incremental Condition dialog box when you select the the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420550841879/btn_ellipsis1.gif) in the value cell of the Incremental Fetch property of a refresh object in a library component in the Report Inspector.

![Incremental Condition dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420542117399/incrmntlcndtn.gif)

You see the following options in the dialog box:

**Add Condition**

Select to add a new condition line.

**Delete**

Select to delete the specified condition line.

**Group**

Select to add the specified conditions in a group. You can also add conditions to an existing group by selecting the conditions and the group while holding Ctrl on the keyboard and then selecting the Group button.

**Ungroup**

Select to ungroup the specified conditions.

**Up**

Select to move the specified condition or group up to a higher level.

**Down**

Select to move the specified condition or group down to a lower level.

**Logical operator drop-down menu**

Select the logical operator to apply for the specified condition lines. It can be
"And" or "Or".

**Field text box**

Specify the business view element on which to set the condition. Select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420550827287/btn_ellipsis2.gif) next to the text box to select the business view element.

**Operator drop-down list**

Select the operator to compose the condition expression.

* **=**  
  Equal to
* **>=**  
  Greater than or equal to
* **>**  
  Greater than
* **<**  
  Less than
* **<=**  
  Less than or equal to
* **!=**/**<>**  
  Not equal to
* **[not] in**  
  The operator causes an enumerated list of values to appear in the WHERE clause predicate, and is used for evaluating for a true condition. For the operator "in" or "not in", you can use multiple values separated by comma (,).
* **[not] like**  
  The like string pattern matching operator is used to compare the first expression string value to the pattern string (the second expression). If you want to use wildcard character in the pattern string, you can only use "\_" and "%".
* **[not] between**  
  The operator allows the system to evaluate whether data values are located between a range of values indicated in the predicate. For the operator "between" or "not between", Designer displays two value text boxes for inputting the same type of values.
* **is [not] null**  
  The operator is used in the WHERE clause predicates to match null values occurring in a specified data field. For the operator "is null" or "is not null", Designer does not display the value text box.

**Value text box**

Specify the value of how to filter the business view element. You can select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420550827287/btn_ellipsis2.gif) next to the drop-down list to specify the value, type the value in the text box, or select any of the following from the drop-down list.

* **MaxExistValue**  
  Select to use the maximum data value in the specified business view element from the last refresh time as the value to filter the business view element.
* **MinExistValue**  
  Select to use the minimum data value in the specified business view element from the last refresh time as the value to filter the business view element.
* **LastRefreshTime**  
  Select to use the previous refresh time as the value to filter the business view element.

**SQL Statement**

This box displays the SQL statement of the condition expressions.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661620887-Imported-SQL-Editor-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661623063-Information-Bus-Dialog-Box)
