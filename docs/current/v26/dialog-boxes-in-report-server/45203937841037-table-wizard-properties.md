---
title: "Table Wizard Properties"
id: 45203937841037
section: "Dialog Boxes in Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203937841037-Table-Wizard-Properties
updated_at: 2026-04-30T14:08:41Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Table Wizard Properties 

You can use the Table Wizard to create a table report. This topic describes the properties in the wizard.

This topic contains the following sections:

- Data Screen

- Display Screen

- Group Screen

- Summary Screen

- Dataset Filter Screen

- Style Screen

You see these elements on all the screens:

Back

Select to return to the previous screen.

Next

Select to go to the next screen.

Finish

Select to create the table and exit the wizard.

Cancel

Select to close the wizard without creating a table.

Help

Select to view information about the dialog box.

## 
Data Screen

Select the business view or dataset you want to use to create the table. Server hides this screen when there is only one business view or dataset in the current catalog.

Available Data Resources

Select a business view or dataset in the current catalog, which you use to create the table.

- 
Inherit from the Parent

Select if you want the data component to inherit the dataset of the parent object. Available only when you are inserting the data component into any of the following panels in a banded object: banded header panel, banded footer panel, group header panel, and group footer panel.

## 
Display Screen

Select the detail fields you want to display in the table.

Resources

Server displays all the group and detail objects in the selected business view or the business view of the selected dataset. To add an object to display as the detail field in the table, select it, and then select the Add button .

Display Fields

Server lists the group and detail objects you have added to display as detail fields in the table. To remove an added object, select it, and then select the Remove button . 

Display Name

Specify the labels of the detail fields, which by default are their display names. You can select a text box to edit the label, or select the Auto Map Field Name checkbox beside the text box to automatically map the label to the dynamic display name of the object.

Move Up button

Select to move the selected item higher in the list.

Move Down button

Select to move the selected item lower in the list.

## 
Group Screen

Specify the fields to group the data in the table. 

Resources

Server displays all the available group objects  you can use to group the data in the table. To add a group object as a group field, select it, and then select the Add button .

Group By 

Server lists all the group objects that you have added as the group fields. To cancel a group object from being a group field, select it, and then select the Remove button .

Sort

Specify the sort order for each group: Ascend, Descend, or No Sort.

Move Up button

Select to move the selected item higher in the list.

Move Down button

Select to move the selected item lower in the list.

## 
Summary Screen

Specify summary fields that calculate data based on a group or on the whole table.

Resources

Server displays all the available aggregation objects  that you can use as summary fields. You can add summary fields for a group or for the whole table. To add for a group, first select the group field in the right box, next select the aggregation object you want in the left box, and then select the Add button . To add for the whole table, first make sure you select no group fields in the right box, next select the aggregation you want in the left box, and then select .

Summarized Fields

Server lists the groups in the table and the aggregation objects that you have added to summarize data in the groups and for the whole table. 

To remove an aggregation object, select it, and then select the Remove button .

Display Name

Specify the labels of the summary fields, which by default are their display names. You can select a text box to edit the label, or select the Auto Map Field Name checkbox beside the text box to automatically map the label to the dynamic display name of the object. Available only when the table is not Group Left type.

Row

Specify to place the summary field in the header or footer row. If the summary is for a group-by field, Server places it in the group header or footer; if the summary is for the table, Server places it in the table header or footer. 

This property is available only when the table is Group Left type.

Column

Select a detail column where you want to place a summary field. This property is available only when the table is Group Left type.

Move Up button

Select to move the selected item higher in the list.

Move Down button

Select to move the selected item lower in the list.

## 
Dataset Filter Screen

Specify the filter which you want to apply to the dataset of the table.

Server displays the predefined filters of the business view in the Filter list. You can choose one of them to apply. If you prefer to define a filter on your own, select User Defined from the list, and then define it.

If the selected business view contains parameters, Server displays the Enter Parameter Values dialog box  for you to specify the parameter values before displaying the Dataset Filter screen.

For more information, see the Edit Dataset Filter dialog box.

## 
Style Screen

Specify the style of the table. Server hides this screen when there is only one style available to the table.

Style

Select a style  you want to apply to the table.

Inherit Style

Select to take the style of the parent component. The property is available when you insert the table into a banded object.

Preview

Server shows a preview of the table in the selected style.
