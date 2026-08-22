---
title: "Chart Wizard Properties"
id: 28891640522637
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891640522637-Chart-Wizard-Properties
updated_at: 2026-02-26T02:11:27Z
source_host: docs-report.zendesk.com
---
# 
Chart Wizard Properties 

You can use the Chart Wizard dialog box to create a chart report. This topic describes the properties in the dialog box.

This topic contains the following sections:

- Data Screen

- Type Screen

- Display Screen

- Dataset Filter Screen

- Style Screen

Back

Select to return to the previous screen.

Next

Select to go to the next screen.

Finish

Select to create the chart and exit the wizard.

Cancel

Select to close the wizard without creating a chart.

Help

Select to view information about the dialog box.

## 
Data Screen

Select the business view or dataset you want to use to create the chart. Server hides this screen when there is only one business view or dataset in the current catalog.

Available Data Resources

Select a business view or dataset in the current catalog, which you use to create the chart.

- 
Inherit from the Parent

Select if you want the data component to inherit the dataset of the parent object. Available only when you are inserting the data component into any of the following panels in a banded object: banded header panel, banded footer panel, group header panel, and group footer panel.

## 
Type Screen

Specify the type of the chart.

Chart Type

Select a chart type.

Subtype

Select a subtype of the selected chart type.

Chart Type Groups

Server lists the subtype you selected for the chart.

If you want to create a combo chart, select <Add Combo Type> under Primary Axis or Secondary Axis. Server adds an additional subtype. To change the additional subtype, select it, then select another chart type and its subtype respectively. To add more subtypes, repeat the procedure. 

Remove button

Select to remove the selected subtype. At least one type should remain for the Primary Axis to create the chart. 

## 
Display Screen

Specify the fields you want to display in the chart.

Resources

Server displays the view elements in the selected business view or the business view of the dataset. Select one non-folder resource, and then select the Add button  beside the Category, Series, or Show Values box to add it into the corresponding box. 

Category

Server lists the group object  you want to display on the category axis of the chart. If you do not want the current resource, select it, and then select the Remove button  on the left to remove it. 

Series

Server lists the group object  you want to display on the series axis of the chart. If you do not want the current resource, select it, and then select the Remove button  on the left to remove it. 

Show Values

Server lists the aggregation objects  and additional values  you want to display on the value axis of the chart. 

For a combo chart, specify resources for each chart type. To add a resource to a chart type, first select the resource and the chart type separately, then select the Add button .

For an additional value, you can select the Edit button to open the Edit Additional Value dialog box.

To remove a resource from the box, select it and select the Remove button  on the left.

Order/Select N

Select to open the Order/Select N dialog box to define the sort order and Select N condition in the chart.

## 
Dataset Filter Screen

Specify the filter which you want to apply to the dataset of the chart.

Server displays the predefined filters of the business view in the Filter list. You can choose one of them to apply. If you prefer to define a filter on your own, select User Defined from the list, and then define it.

If the selected business view contains parameters, Server displays the Enter Parameter Values dialog box  for you to specify the parameter values before displaying the Dataset Filter screen.

For more information, see the Edit Dataset Filter dialog box.

## 
Style Screen

Select a style for the chart. Server hides this screen when there is only one style available.

Style

Select the style you want to apply to the chart.

Inherit Style

Specify to take the style of the parent component. The property is available when you insert the chart into a banded object or table.

Preview

Server displays a diagram to illustrate the effect of the selected style on the component.
