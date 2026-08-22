---
title: "Edit Filter Dialog Box"
id: 5735522539031
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735522539031-Edit-Filter-Dialog-Box
updated_at: 2022-11-02T04:14:58Z
---

# Edit Filter Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735500381463-Edit-Display-Name-for-Component-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735565634071-Edit-Filter-Control-Dialog-Box)

# Edit Filter Dialog Box

You can use the Edit Filter dialog box to [filter each data component](https://devnet.logianalytics.com/hc/en-us/articles/5735534181911-Filtering-Reports) in a page report that uses query resources. This topic describes the options in the dialog box.

Designer displays the Edit Filter dialog box when you right-click a data component in a query-based page report and select Edit Filter from the shortcut menu.

![Edit Filter dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898474463383/edtfltr.gif)

Designer displays these options:

**Add Condition**

Select to add a new condition.

**Delete**

Select to delete the specified condition.

**Group**

Select to add the specified conditions in a group. You can also add conditions to an existing group by selecting the conditions and the group while holding Ctrl on the keyboard and then selecting the Group button.

**Ungroup**

Select to ungroup the specified conditions.

**Up**

Select to move the specified condition or group up to a higher level.

**Down**

Select to move the specified condition or group down to a lower level.

**Logical operator drop-down menu**

Specify the logical operator to apply for the specified conditions. It can be
"And", "Or", "And Not", or "Or Not".

**Field drop-down list**

Specify the field on which to define the condition.

**Operator drop-down list**

Specify the operator to compose the condition.

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

Specify the value of how to filter the field.

**SQL Statement**

This box displays the SQL statement of the conditions.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735500381463-Edit-Display-Name-for-Component-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735565634071-Edit-Filter-Control-Dialog-Box)
