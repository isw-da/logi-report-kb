---
title: "Query Filter Dialog Box Properties"
id: 1500009747922
section: "Web Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009747922-Query-Filter-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:15Z
---

# Query Filter Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009776181-Printer-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009747902-Quick-Schedule-Dialog-Box-Properties)

# Query Filter Dialog Box Properties

This topic describes how you can use the Query Filter dialog box to [apply a filter to the business view](https://devnet.logianalytics.com/hc/en-us/articles/1500009778741-Applying-Filters-in-Web-Report#BV) that the specified data component uses to narrow down data scope.

**Advanced/Basic**

Switch the dialog box to the [advanced mode](#Advanced)/[basic mode](#Basic).

You see these elements in both modes:

**OK**

Select **OK** to apply the filter.

**Cancel**

Select **Cancel** to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Select to view information about the Query Filter dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Select to close the dialog box without saving any changes.

## Basic Mode

The basic mode provides function for creating simple filter conditions which are connected by AND and OR operators.

![Query Filter dialog - Basic mode](https://devnet.logianalytics.com/hc/article_attachments/4404880189207/qryfltr_basic.gif)

**Apply To**

Specifies the data component to apply the filter to the business view the data component uses. Not available when the dialog box is accessed by selecting the Filter button in the report wizard.

**Query Filter**

Specifies the filter you want to apply to the business view.

* **User Defined**  
   Specifies to create a user defined filter to apply to the business view.
* **Predefined filters**  
   The names of the predefined filters which were created on the business view in Logi Report Designer. You can choose one of them to apply.

![](https://devnet.logianalytics.com/hc/article_attachments/4404880189847/btn_pgrpt_no.gif)

Deletes the selected condition line.

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
   Allows the system to evaluate whether data values are located between a range of values indicated in the predicate. For the operator "between" or "not between", there are two value text boxes for inputting the same type of values.
* **is [not] null**  
   It is used in WHERE clause predicates to match null values occurring in a specified data field. For the operator "is null" or "is not null", the value text box is hidden.

**Value**

Specifies the value of how to filter the field. You can either type the value manually in the text box or select a value from the drop-down list, or select the button ![Enter Parameter Values button](https://devnet.logianalytics.com/hc/article_attachments/4404880189463/btn_dshbrd_prm.gif) and then select a parameter from the drop-down list as the value.

**Logic**

Lists the logic operator.

* **AND**  
   Logic operator AND which is applied to this and the next line.
* **OR**  
   Logic operator OR which is applied to this and the next line.

## Advanced Mode

The advanced mode enables the building of more complex filter conditions via the grouping of conditions.

![Query Filter dialog - Advanced mode](https://devnet.logianalytics.com/hc/article_attachments/4404880190231/qryfltr_adv.gif)

**Apply To**

Specifies the data component to apply the filter to the business view the data component uses. Not available when the dialog box is accessed by selecting the Filter button in the report wizard.

**Query Filter**

Specifies the filter you want to apply to the business view.

* **User Defined**  
   Specifies to create a user defined filter to apply to the business view.
* **Predefined filters**  
   The names of the predefined filters which were created on the business view in Logi Report Designer. You can choose one of them to apply.

**Add Condition**

Adds a new condition line.

**Delete**

Deletes the selected condition line.

**Group**

Makes the selected conditions in a group. Conditions can also be added to an existing group by selecting the conditions and the group while holding the Ctrl button, and then selecting the Group button.

**Ungroup**

Makes the selected group leave the group.

**Up**

Moves the selected condition or group up to a higher level.

**Down**

Moves the selected condition or group down to a lower level.

**Logic**

Logic operator that applies to this and the next line: AND, OR, AND NOT, and OR NOT.

**Field**

Specifies the field to be filtered.

**Operator**

Specifies the [operator](#Operator) to compose the filter expression.

**Value**

Specifies the value of how to filter the field. You can either type the value manually in the text box or select a value from the drop-down list, or select the button ![Enter Parameter Values button](https://devnet.logianalytics.com/hc/article_attachments/4404880189463/btn_dshbrd_prm.gif) and then select a parameter from the drop-down list as the value.

**Condition Expression**

Displays the SQL statement of the condition.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009776181-Printer-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009747902-Quick-Schedule-Dialog-Box-Properties)
