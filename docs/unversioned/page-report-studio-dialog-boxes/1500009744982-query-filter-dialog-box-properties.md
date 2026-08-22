---
title: "Query Filter Dialog Box Properties"
id: 1500009744982
section: "Page Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009744982-Query-Filter-Dialog-Box-Properties
updated_at: 2021-07-24T00:49:06Z
---

# Query Filter Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009772881-Printable-Version-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009772921-Quick-Schedule-Dialog-Box-Properties)

# Query Filter Dialog Box Properties

You can use the Query Filter dialog box to [apply a filter to the business view](https://devnet.logianalytics.com/hc/en-us/articles/1500009777561-Applying-Filters-to-Page-Report#BV) that the specified data component uses to narrow down its data scope. This topic describes the options in the dialog box.

**Advanced/Basic**

Switches the dialog box to the [advanced mode](#Advanced) or [basic mode](#Basic).

**OK**

Applies the settings and closes the dialog box.

**Cancel**

Closes the dialog box and discards any changes.

**Help**

Displays the help document about this feature.

## Basic Mode

The basic mode provides function for creating simple filter conditions which are connected by the AND and OR operators.

![Query Filter dialog - Basic mode](https://devnet.logianalytics.com/hc/article_attachments/4404885394839/qryfltr_basic.gif)

**Query Filter**

Specifies the filter you want to apply to the business view.

* **User Defined**  
   Specifies to create a user defined filter to apply to the business view.
* **Predefined filters**  
   The names of the predefined filters which were created on the business view in Logi Report Designer. You can choose one of them to apply.
  + **Edit**  
     Edits the selected predefined filter. Once a predefined filter is edited, it will be saved as a user defined filter in the business view.
  + **Description**  
     Displays the description of the selected predefined filter.

![Delete Condition Line](https://devnet.logianalytics.com/hc/article_attachments/4404880189847/btn_pgrpt_no.gif)

Deletes the current condition line.

**Field**

Specifies the field to be filtered.

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
   Causes an enumerated list of values to appear in the WHERE clause predicate, used for evaluating for a true condition. For the operator "in" or "not in", multiple values separated by comma (,) are allowed.
* **[not] like**  
   Like string pattern matching operator is used to compare the first expression string value to the pattern string (the second expression). If you want to use wildcard character in the pattern string, only "\_" and "%" are supported.
* **[not] between**  
   Allows the system to evaluate whether data values are located between a range of values indicated in the predicate. For the operator "between" or "not between", there are two value text boxes for typing the same type of values.
* **is [not] null**  
   It is used in WHERE clause predicates to match null values occurring in a specified data field. For the operator "is null" or "is not null", the value text box is hidden.

**Value**

Specifies the value of how to filter the field. You can either type the value manually in the text box or select a value from the drop-down list. Select ![Filter By Field](https://devnet.logianalytics.com/hc/article_attachments/4404880263959/btn_pgrpt_field.gif) or ![Filter By Value](https://devnet.logianalytics.com/hc/article_attachments/4404885395991/btn_pgrpt_value.gif) to switch to filter the field by field or value.

**Logic**

Lists the logic operator.

* **AND**  
   Logic operator AND which is applied to this and the next line.
* **OR**  
   Logic operator OR which is applied to this and the next line.

## Advanced Mode

The advanced mode enables the building of more complex filter conditions via the grouping of conditions.

![Query Filter dialog - Advanced mode](https://devnet.logianalytics.com/hc/article_attachments/4404880264343/qryfltr_advc.gif)

**Query Filter**

Specifies the filter you want to apply to the business view.

* **User Defined**  
   Specifies to create a user defined filter to apply to the business view.
* **Predefined filters**  
   The names of the predefined filters which were created on the business view in Logi Report Designer. You can choose one of them to apply.
  + **Edit**  
     Edits the selected predefined filter. Once a predefined filter is edited, it will be saved as a user defined filter in the business view.
  + **Description**  
     Displays the description of the selected predefined filter.

**Add Condition**

Adds a new condition line.

**Delete**

Deletes the selected condition line.

**Group**

Makes the selected conditions in one group. Conditions can also be added to an existing group by selecting the conditions and the group while holding the Ctrl button, and then selecting the Group button.

**Ungroup**

Makes the selected condition ungrouped.

**Up**

Moves the selected condition or group up to a higher level.

**Down**

Moves the selected condition or group down to a lower level.

**Logic**

Specifies the logic operator.

* **AND**  
   Logic operator AND which is applied to this and the next line.
* **OR**  
   Logic operator OR which is applied to this and the next line.
* **AND NOT**   
   Logic operator AND NOT which is applied to this and the next line.
* **OR NOT**   
   Logic operator OR NOT which is applied to this and the next line.

**Field**

Specifies the field to be filtered.

**Operator**

Specifies the [operator](#Operator) to compose the filter expression.

**Value**

Specifies the value of how to filter the field. You can either type the value manually in the text box or select a value from the drop-down list. Select ![Filter By Field](https://devnet.logianalytics.com/hc/article_attachments/4404880263959/btn_pgrpt_field.gif) or ![Filter By Value](https://devnet.logianalytics.com/hc/article_attachments/4404885395991/btn_pgrpt_value.gif) to switch to filter the field by field or value.

**Condition Expression**

Displays the SQL statement of the filter condition.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009772881-Printable-Version-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009772921-Quick-Schedule-Dialog-Box-Properties)
