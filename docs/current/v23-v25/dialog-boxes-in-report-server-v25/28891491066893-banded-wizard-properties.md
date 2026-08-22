---
title: "Banded Wizard Properties"
id: 28891491066893
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891491066893-Banded-Wizard-Properties
updated_at: 2026-02-26T02:11:27Z
source_host: docs-report.zendesk.com
---
# 
Banded Wizard Properties 

You can use the Banded Wizard dialog box to create a banded report. This topic describes the properties in the dialog box.

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

Select to create the banded object and exit the wizard.

Cancel

Select to close the wizard without creating a banded object.

Help

Select to view information about the dialog box.

## 
Data Screen

Select the business view or dataset you want to use to create the banded object. Server hides this screen when there is only one business view or dataset in the current catalog.

Available Data Resources

Select a business view or dataset in the current catalog, which you use to create the banded object.

- 
Inherit from the Parent

Select if you want the data component to inherit the dataset of the parent object. Available only when you are inserting the data component into any of the following panels in a banded object: banded header panel, banded footer panel, group header panel, and group footer panel.

## 
Display Screen

Select the detail fields you want to display in the banded object.

Resources

Server displays all the group and detail objects in the selected business view or the business view of the dataset. To add an object to display as the detail field in the banded object, select it, and then select the Add button .

Display Fields

Server lists the group and detail objects you have added to display as detail fields in the banded object. To remove an added object, select it, and then select the Remove button . 

Display Name

Specify the labels of the detail fields, which by default are their display names. You can select a text box to edit the label, or select the Auto Map Field Name checkbox beside the text box to automatically map the label to the dynamic display name of the object.

The downward order of the added objects determines the order of the detail columns in the banded object from left to right. You can use the following two buttons to adjust the order. 

Move Up button

Select to move the selected item higher in the list.

Move Down button

Select to move the selected item lower in the list.

## 
Group Screen

Specify the fields to group the data in the banded object.

Resources

Server displays all the available group objects  you can use to group the data in the banded object. To add a group object as a group field, select it, and then select the Add button .

Group By 

Server lists all the group objects that you have added as the group fields. To cancel a group object from being a group field, select it, and then select the Remove button .

Sort

Select the sort order for each group: Ascend, Descend, or No Sort.

The downward order of the added group fields determines the order of the groups in the banded object from first to last. You can use the following two buttons to adjust the order. 

Move Up button

Select to move the selected item higher in the list.

Move Down button

Select to move the selected item lower in the list.

## 
Summary Screen

Specify summary fields that calculate data based on a group or on the whole banded object.

Resources

Server displays all the available aggregation objects  that you can use as summary fields. You can add summary fields for a group or for the whole banded object. To add for a group, first select the group field in the right box, then select the aggregation object you want in the left box, and select the Add button . To add for the whole banded object, first make sure you select no group fields in the right box, then select the aggregation you want in the left box, and select .

Summarized Fields

Server lists the groups in the banded object and the aggregation objects that you have added to summarize data in the groups and for the whole banded object. 

To remove an aggregation object, select it, and then select the Remove button .

Display Name

Specify the labels of the summary fields, which by default are their display names. You can select a text box to edit the label, or select the Auto Map Field Name checkbox beside the text box to automatically map the label to the dynamic display name of the object.

Move Up button

Select to move the selected item higher in the list.

Move Down button

Select to move the selected item lower in the list.

## 
Dataset Filter Screen

Specify the filter which you want to apply to the dataset of the banded object.

Server displays the predefined filters of the business view in the Filter list. You can choose one of them to apply. If you prefer to define a filter on your own, select User Defined from the list, and then define it.

If the selected business view contains parameters, Server displays the Enter Parameter Values dialog box  for you to specify the parameter values before displaying the Dataset Filter screen.

For more information, see the Edit Dataset Filter dialog box.

## 
Style Screen

Specify the style of the banded object. Server hides this screen when there is only one style available to the banded object.

Style

Select a style  you want to apply to the banded object.

Inherit Style

Select to take the style of the parent component. The property is available when you insert the banded object into another banded object.

Preview

Server shows a preview of the banded object in the selected style.
