---
title: "Dataset Filter Dialog Box"
id: 4405661502359
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661502359-Dataset-Filter-Dialog-Box
updated_at: 2022-01-27T20:35:25Z
---

# Dataset Filter Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661501079-Dataset-Editor-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661498903-Data-Source-Drivers-Dialog-Box)

# Dataset Filter Dialog Box

You can use the Dataset Filter dialog box to [set filter conditions for a dataset](https://devnet.logianalytics.com/hc/en-us/articles/4405661914263-Creating-and-Managing-Datasets#Filter) that is based on a query resource. This topic describes the options in the dialog box.

Designer displays the Dataset Filter dialog box when you select Dataset Filter ![Filter button](https://devnet.logianalytics.com/hc/article_attachments/4420556086295/btn_filter.gif) on the toolbar of the Data panel.

![Dataset Filter dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420556205847/dtstfltr.gif)

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

Specify the logical operator to apply for the specified condition lines. It can be
"And", "Or", "And Not", or "Or Not".

**Field text box**

Specify the field on which to set the filter condition. This drop-down list contains all the DBFields in the query resource on which the dataset is created, and the parameters and valid formulas of these DBFields in the same catalog data source as the query resource. Select one to create the filter on it.

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

Specify the value of how to filter the field. You can either type the value in the text box or select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420550827287/btn_ellipsis2.gif) to specify the value using the [Expressions dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664472599-Expressions-Dialog-Box).

**SQL Statement**

This box displays the SQL statement of the filter conditions.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661501079-Dataset-Editor-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661498903-Data-Source-Drivers-Dialog-Box)
