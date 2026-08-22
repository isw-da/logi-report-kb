---
title: "Link Data Container Dialog Box"
id: 12480147918093
section: "References - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480147918093-Link-Data-Container-Dialog-Box
updated_at: 2026-02-25T23:49:07Z
source_host: docs-report.zendesk.com
---
# 
Link Data Container Dialog Box

You can use the Link Data Container dialog box to set up data relation between two data containers that are in a parent-child relationship and apply different datasets. This topic describes the options in the dialog box.
    

Designer displays the Link Data Container dialog box when you right-click a child data container that applies a different dataset than its parent's and select Data Container Link from the shortcut menu in a page or web report.

This dialog box contains the following tabs:

- Condition Tab

- Parameter Tab

- Return Value Tab

Designer displays these buttons in all the tabs:

OK

Select to apply your settings and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.

## 
Condition Tab

Use this tab to specify link conditions between two data containers.

Resource box

The box on the left lists the data fields in and related to the data resource from which the dataset the parent data container uses is created.

Add button

Select to add the specified field in the resource box (parent field) to set up a link condition based on the field.

Remove button

Select to remove the specified field from the Field box.

Field box

This box lists the fields in both the parent and child data containers on which the link conditions are based.

- 
Fields (Parent)
This column shows the fields of the parent data container that you add to set the link conditions.

- 
OP
This column shows the operators that you select to set up the link conditions. You can select from the following operators:

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

- 
Fields (Child)
This column shows the fields that you select from the child data container to set up the link conditions. Once you add a parent field, Designer automatically displays the DBFields in the dataset of the child data container which are of the same data type in the drop-down list of the column. Select a child field to set up the link condition.

## 
Parameter Tab

Designer enables the Parameter tab when the child data container applies parameters. You can use it to assign values of the same-typed fields in the parent data container to the parameters.

Parameters

This column lists all parameters the dataset of the child data container applies.

Value

This column shows the fields of the parent data container (parent fields) that you select to assign values to parameters of the child data container. For each parameter, Designer displays the DBFields, formulas, summaries, and parameters  in the dataset of the parent data container that are of the same data type in the drop-down list of the column. Select a parent field to assign its  values to the parameter.

## 
Return Value Tab

Designer enables the Return Value tab when the parent data container is in a page report and it applies parameters. You can use it to specify same-typed fields  in the child data container to return their values to parameters of the parent data container.

Field in Child Data Container

This box lists the available fields in the child data container that you can use to return values to parameters of the parent data container.

Add button

Select to add the specified field in the Field in Child Data Container box to use its value for a parameter of the parent data container. 

Remove button

Select to remove the specified field from the Return Value box.

Return Value

This box lists the fields of the child data container that you add to return values to parameters of the parent data container.
    

- 
Fields
This column shows the fields that you add from the child data container.

- 
Parameters
This column shows the parameters in the parent data container that you select to get values from the specified fields in the child data container. Once you add a field from the child data container, Designer automatically displays the parameters in the parent data container that are of the same data type in the drop-down list of the column. Select a parameter to obtain values for it from the child field.
