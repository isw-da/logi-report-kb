---
title: "Edit Filter Dialog"
id: 1500009565242
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009565242-Edit-Filter-Dialog
updated_at: 2021-07-24T05:55:26Z
---

# Edit Filter Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009586421-Edit-Display-Name-for-Component-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009586441-Edit-Filter-Control-Dialog-for-Library-Component-)

# Edit Filter Dialog

The Edit Filter dialog appears when you right-click a data component in the design area and select Format Filter from the shortcut menu. It helps you to [filter the data](https://devnet.logianalytics.com/hc/en-us/articles/1500009584321-Filtering-the-Data) used in the data component. [See the dialog](javascript:%20void(null)).

![Edit Filter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893926423/edtfltr.gif)

The following are details about options in the dialog:

**Filter**

Available when the data component is created using a business view. It lists all the [predefined filters](https://devnet.logianalytics.com/hc/en-us/articles/1500009562662-Creating-Predefined-Filters) of the business view. Select one from the drop-down list to apply, or select User Defined and define a new filter according to your requirements.

**Add Condition**

Adds a new condition line.

**Delete**

Deletes the selected condition line.

**Group**

Makes the selected conditions in a group. Conditions can also be added to an existing group by selecting the conditions and the group while holding the Ctrl button, and then selecting the Group button.

**Ungroup**

Makes the selected condition ungrouped.

**Up**

Moves the selected condition or group up to a higher level.

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

Specifies the field on which the condition is set. You can select the desired one from the drop-down list.

**Operator**

Specifies the operator to compose the filter expression.

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
* **!=**  
   Not equal to
* **[not] in**  
   Causes an enumerated list of values to appear in the WHERE clause predicate, used for evaluating for a true condition. For operator "in" or "not in", multiple values separated by comma (,) are allowed.
* **[not] like**  
  Like string pattern matching operator is used to compare the first expression string value to the pattern string (the second expression). If you want to use wildcard character in the pattern string, only "\_" and "%" are supported.
* **[not] between**  
   Allows the system to evaluate whether or not data values are located between a range of values indicated in the predicate. For operator "between" or "not between", there are two value text boxes for inputting the same type of values.
* **is [not] null**  
   It is used in WHERE clause predicates to match null values occurring in a specified data field. For operator "is null" or "is not null", the value text box is hidden.

**Value**

Specifies the value of how to filter the field. You can type in the value manually if you are familiar with the values.

**SQL Statement**

Displays the SQL statement of the filter expressions.

**OK**

Applies the changes and closes the dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009586421-Edit-Display-Name-for-Component-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009586441-Edit-Filter-Control-Dialog-for-Library-Component-)
