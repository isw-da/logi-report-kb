---
title: "Dataset Filter Dialog Box"
id: 45190486903565
section: "References - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190486903565-Dataset-Filter-Dialog-Box
updated_at: 2026-04-30T15:13:07Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Dataset Filter Dialog Box

You can use the Dataset Filter dialog box to specify filter conditions for a dataset. This topic describes the options in the dialog box.
    

Designer displays the Dataset Filter dialog box when you select Dataset Filter  on the toolbar of the Data panel, and provides you with different options in the dialog box according to the type of the data resource on which the dataset is based: business view or query resource.

## 
For Business View-Based Dataset

When you use the Dataset Filter dialog box to filter a dataset that is created from a business view, Designer displays the same options in the dialog box as those in the Edit Dataset Filter dialog box.

 

## 
For Query-Based Dataset

When you use the Dataset Filter dialog box to filter a dataset that is created from a query resource, Designer displays the following options in the dialog box:

Add Condition

Select to add a new condition.

Delete

Select to delete the specified condition.

Group

Select to add the specified conditions in a group. You can also add conditions to an existing group by selecting the conditions and the group while holding Ctrl on the keyboard and then selecting the Group button.

Ungroup

Select to ungroup the specified conditions.

Up

Select to move the specified condition or group up to a higher level.

Down 

Select to move the specified condition or group down to a lower level.

Logical operator drop-down menu

Specify the logical operator to apply for the specified conditions. It can be 
"And", "Or", "And Not", or "Or Not".    

Field drop-down list

Specify the field on which to define the condition.

Operator drop-down list

Specify the operator to compose the condition.

- 
=

Equal to

- 
>=

Greater than or equal to

- 
>

Greater than

- 
<

Less than

- 
<=

Less than or equal to

- 
!=/<>

Not equal to

- 
[not] in

The operator causes an enumerated list of values to appear in the WHERE clause predicate, and is used for evaluating for a true condition. For the operator "in" or "not in", you can use multiple values separated by comma (,).

- 
[not] like

The like string pattern matching operator is used to compare the first expression string value to the pattern string (the second expression). If you want to use wildcard character in the pattern string, you can only use "_" and "%".

- 
[not] between

The operator allows the system to evaluate whether  data values are located between a range of values indicated in the predicate. For the operator "between" or "not between", Designer displays two value text boxes for inputting the same type of values.

- 
is [not] null

The operator is used in the WHERE clause predicates to match null values occurring in a specified data field. For the operator "is null" or "is not null", Designer does not display the value text box.

Value text box

Specify the value of how to filter the field. Select the ellipsis  to specify the value using the Expressions dialog box.

SQL Statement

This box displays the SQL statement of the conditions.

OK

Select to apply your settings and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.
