---
title: "To Crosstab Dialog Box Properties"
id: 45203914703245
section: "Dialog Boxes in Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203914703245-To-Crosstab-Dialog-Box-Properties
updated_at: 2026-04-30T14:08:42Z
source_host: logi-report-v26.insightsoftware.com
---
# 
To Crosstab Dialog Box Properties 

You can use the To Crosstab dialog box to convert a chart into a crosstab. This topic describes the properties in the dialog box.

This topic contains the following sections:

- Display Tab Properties

- Style Tab Properties

You see these elements on both tabs:

Back

Select to go to the previous tab.

Next

Select to go to the next tab.

OK

Select to convert the chart to a crosstab.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.

## 
Display Tab Properties

Specify the data fields you want to display in the crosstab.

Resources

Server displays all the view elements used in the chart. Select a field, and then select the Add button  beside the Columns, Rows, or Summaries box to add it into the corresponding box. 

Columns/Rows

- 
Field
    Server lists the group objects you added to display on the column/row headers of the crosstab. To remove an object from a box, select it and select the Remove button  on the left.

- 
Display Name
    Specify the labels for the column/row headers. You can select a text box to edit the label, or select the Auto Map Field Name checkbox beside the text box to automatically map the label to the dynamic display name of the object.  

- 
Sort
    Select the sort order of a group object.

- 
 Add Compound Group button
Select to add a column/row compound group.

Summaries

- 
Field
 Server lists the aggregation objects you added as the aggregate fields of the crosstab. To remove an object from the box, select it and select the Remove button  on the left.

- 
Display Name
    Specify the labels for the aggregations. You can select a text box to edit the label, or select the Auto Map Field Name checkbox beside the text box to automatically map the label to the dynamic display name of the object.

Move Up button

Select to move the selected item higher in the list.

Move Down button

Select to move the selected item lower in the list.

## 
Style Tab Properties

Specify the style of the crosstab. Server hides this tab when there is only one style available.

Style

Select the style you want to apply to the component.

- 
Custom

  There is no style information in this style. Server only uses it to support reports you created in previous versions when they do not bind any style or their styles are not in the style list.

Preview

Server displays a diagram to illustrate the effect of the selected style on the component. 

Inherit Style

Select  to take the style of the parent component. The property is available when the chart is in a table or banded object.
