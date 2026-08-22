---
title: "Link Data Container Dialog Box Properties"
id: 28891633049101
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891633049101-Link-Data-Container-Dialog-Box-Properties
updated_at: 2026-02-26T02:12:12Z
source_host: docs-report.zendesk.com
---
# 
Link Data Container Dialog Box Properties

This topic describes how you can use the Link Data Container dialog box to set up data relation between two data components that are in a parent-child relationship and apply different datasets.

Server displays the Link Data Container dialog box when you right-click a child data component that uses a different dataset from its parent's and select Data Container Link from the shortcut menu.

This topic contains the following sections:

- Condition Tab Properties

- Parameter Tab Properties

- Return Value Tab Properties

You see these elements on all the tabs:

Target Component

The child data component that you selected to open this dialog box.

Cancel

Select to close the dialog box without saving any changes.

OK

Select to apply any changes you made here and close the dialog box.

Help button

Select to view information about the dialog box.

Close button

Select to close the dialog box without saving any changes.

## 
Condition Tab Properties

Specify link conditions between the two parent-child data components.

Resources box

The box on the left lists the data fields in and related to the data resource from which the dataset the parent data component uses is created.

Add button

Select to add the specified field in the resources box (parent field) to set up a link condition based on the field.

Remove button

Select to remove the specified field from the Field box.

Field box

This box lists the fields in both the parent and child data components on which the link conditions are based.

- 
Fields (Parent)
This column shows the fields of the parent data component that you add to set up the link conditions.

- 
OP
This column shows the operators that you select to set up the link conditions. You can select from these operators:
				
- 
=
Equal to

- 
<>
Not equal to

- 
<
Less than

- 
>
Greater than

- 
<=
Less than or equal to

- 
>=
Greater than or equal to

- 
in
The operator causes an enumerated list of values to appear in the WHERE clause predicate, and is used for evaluating for a true condition. For the "in" operator, you can use multiple values separated by comma (,).

- 
Fields (Child)
This column shows the fields that you select from the child data component to set up the link conditions. Once you add a parent field, Server automatically displays the DBFields in the dataset of the child data component which are of the same data type in the drop-down list of the column. Select a child field to set up the link condition.

## 
Parameter Tab Properties

Server enables the Parameter tab when the child data component applies parameters. You can use it to assign values of the same-typed fields in the parent data component to the parameters.

Parameters (Child)

This column lists all parameters the dataset of the child data component applies.

Value (Parent)

This column shows the fields of the parent data component (parent fields) that you select to assign values to parameters of the child data component. For each parameter, Server displays the DBFields, formulas, summaries, and parameters  in the dataset of the parent data component that are of the same data type in the drop-down list of the column. Select a parent field to assign its  values to the parameter.

## 
Return Value Tab Properties

Server enables the Return Value tab when the parent data component is in a page report and it applies parameters. You can use it to specify same-typed fields  in the child data component to return their values to parameters of the parent data component.

Left box

This box lists the available fields in the child data component that you can use to return values to parameters of the parent data component.

Add button

Select to add the specified field in the left box to use its value for a parameter of the parent data component. 

Remove button

Select to remove the specified field from the right box.

Right box

This box lists the fields of the child data component that you add to return values to parameters of the parent data component.
    

- 
Fields (Child)
This column shows the fields that you add from the child data component.

- 
Parameters (Parent)
This column shows the parameters in the parent data component that you select to get values from the specified fields in the child data component. Once you add a field from the child data component, Server automatically displays the parameters in the parent data component that are of the same data type in the drop-down list of the column. Select a parameter to obtain its values from the child field.
