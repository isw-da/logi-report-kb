---
title: "Dataset Filter Dialog"
id: 1500010030362
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010030362-Dataset-Filter-Dialog
updated_at: 2021-07-24T10:39:00Z
---

# Dataset Filter Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010030342-Dataset-Editor-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010030322-Data-Source-Drivers-Dialog)

# Dataset Filter Dialog

The Dataset Filter dialog helps you to [set filter conditions for a dataset](https://devnet.logianalytics.com/hc/en-us/articles/1500010070661-Creating-and-Managing-Datasets#Filter) created from a query resource. It appears when you select the Dataset Filter button ![Filter button](https://devnet.logianalytics.com/hc/article_attachments/4404909113495/btn_filter.gif) on the toolbar of the Data panel.

![Dataset Filter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909227031/dtstfltr.gif)

The following are details about options in this dialog:

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

Specifies the field to be filtered. The drop-down list contains all the DBFields in the query resource on which the dataset is created, as well as the parameters and valid formulas of these DBFields in the same catalog data source as the query resource. Select one to create the filter on it.

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
  Causes an enumerated list of values which will appear in the WHERE clause predicate to be evaluated for a true condition. For operator "in" or "not in", multiple values separated by comma (,) are allowed.
* **[not] like**  
   Like string pattern matching operator is used to compare the first expression string value to the pattern string (the second expression). If you want to use wildcard character in the pattern string, only "\_" and "%" are supported.
* **[not] between**  
   Allows the system to evaluate whether or not data values are located between a range of values indicated in the predicate. For operator "between" or "not between", there are two value text boxes for inputting the same type of values.
* **is [not] null**  
   It is used in WHERE clause predicates to match null values occurring in a specified data field. For operator "is null" or "is not null", the value text box is hidden.

**Value**

Specifies the value of how to filter the field. You can either type in the value manually or select ![](https://devnet.logianalytics.com/hc/article_attachments/4404901122967/btn_chsr.gif) next to the text box to specify the value in the [Expressions](https://devnet.logianalytics.com/hc/en-us/articles/1500010065881-Expressions-Dialog) dialog.

**SQL Statement**

Displays the SQL statement of the filter expressions.

**OK**

Applies the changes and closes the dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010030342-Dataset-Editor-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010030322-Data-Source-Drivers-Dialog)
