---
title: "Edit Filter Dialog Box"
id: 4405661510295
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661510295-Edit-Filter-Dialog-Box
updated_at: 2022-01-27T20:38:12Z
---

# Edit Filter Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664457879-Edit-Display-Name-for-Component-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664459031-Edit-Filter-Control-Dialog-Box)

# Edit Filter Dialog Box

You can use the Edit Filter dialog box to [filter the data](https://devnet.logianalytics.com/hc/en-us/articles/4405664691735-Filtering-Reports) of the specified data component in a report. This topic describes the options in the dialog box.

Designer displays the Edit Filter dialog box when you right-click a data component in a report and select Format Filter from the shortcut menu.

![Edit Filter dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420550940439/edtfltr.gif)

You see the following options in the dialog box:

**Filter**

Designer displays this drop-down list when the data component uses a business view. It lists all the [predefined filters](https://devnet.logianalytics.com/hc/en-us/articles/4405664681111-Creating-Business-Views-in-a-Catalog#Filter) of the business view. Select one from the drop-down list to apply, or select User Defined to define a new filter.

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

Specify the logical operator to apply for the specified condition lines. It can be
"And", "Or", "And Not", or "Or Not".

**Field text box**

Specify the field on which to set the filter condition.

**Operator drop-down list**

Specify the operator to compose the filter condition.

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

This box displays the SQL statement of the filter conditions.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664457879-Edit-Display-Name-for-Component-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664459031-Edit-Filter-Control-Dialog-Box)
