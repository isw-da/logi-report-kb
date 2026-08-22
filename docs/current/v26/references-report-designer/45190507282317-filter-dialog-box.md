---
title: "Filter Dialog Box"
id: 45190507282317
section: "References - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190507282317-Filter-Dialog-Box
updated_at: 2026-04-30T15:13:26Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Filter Dialog Box

You can use the Filter dialog box to define to filter data of the current library component as a response to the message the library component receives at runtime. This topic describes the options in the dialog box.
    

Designer displays the Filter dialog box in two scenarios and you can use it for different purposes.

- When you open the dialog box by selecting 0001 - Filter from the drop-down list of the Message ID column and selecting the ellipsis  in the Actions column of the Receive Message dialog box, you can use it to define to receive the built-in Filter message at runtime.

- When you open the dialog box by selecting a user-defined message from the drop-down list of the Message ID column, selecting the ellipsis  in the Actions column of the Receive Message dialog box, and then selecting *Filter and selecting OK in the Web Action List dialog box, you can use it to define to receive the user-defined Filter message at runtime.

Designer displays these options:

Add button

Select to add a new filter condition.

Remove button

Select to delete the specified filter condition.

Move Up button

Select to move the specified filter condition higher in the list.

Move Down button

Select to move the specified filter condition lower in the list.

Filter On

This column shows the fields that you select to perform the filter on.

Operator

This column shows the operators that you select to compose the filter expressions.

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
in

The operator causes an enumerated list of values to appear in the WHERE clause predicate, and is used for evaluating for a true condition. For the "in" operator, you can use multiple values separated by comma (,).

Value

This column shows the values using which you specify to filter the fields.

More

This column shows the relationship that you select for the conditions, which can be "And", "Or", or "End".

OK

Select to apply your settings and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.
