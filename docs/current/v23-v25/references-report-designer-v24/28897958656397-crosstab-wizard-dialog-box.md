---
title: "Crosstab Wizard Dialog Box"
id: 28897958656397
section: "References - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897958656397-Crosstab-Wizard-Dialog-Box
updated_at: 2024-09-30T09:11:17Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Crosstab Wizard Dialog Box

You can use the Crosstab Wizard dialog box to create a page report tab with a crosstab in it, create a library component with a crosstab in it, or edit an existing crosstab in a report. This topic describes the options in the dialog box.
    

Designer displays different options in the Crosstab Wizard dialog box according to the type of the data resource you use for the crosstab: business view or query resource.

## 
Crosstab Wizard Dialog Box - Business View Based

When you use the Crosstab Wizard dialog box for creating or editing a crosstab using a business view, Designer displays the following screens in the dialog box (Designer displays the Dataset Filter screen  only when you use the dialog box for creating a crosstab):

- Data Screen

- Display Screen

- Dataset Filter Screen

- Layout Screen

- Style Screen

Designer displays these buttons in all the screens:

Back

Select to go back to the previous screen.

Next

Select to go to the next screen.

Finish

Select to finish your work and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.

### 
Data Screen

        Use this screen to specify the dataset for the crosstab. 

Business view box

This box lists the predefined business views in the current catalog. Select one and Designer automatically creates a dataset based on it for the crosstab.

- 
<New Business View...>
Select to create a business view in the catalog using the Business View Editor dialog box. Designer does not display this option when you use the dialog box in a library component.
            

More Options/Less Options

Select to show or hide the options for specifying the dataset you want to use. Designer does not display this pair of buttons when you use the dialog box in a library component.

- 
New Dataset
Select to create a dataset based on a business view in the current catalog.

- 
Existing Dataset
Select to use a dataset from the ones that you have created in the current report.- 
<New Dataset...>
Select to create a dataset in the New Dataset dialog box.

- 
Current Dataset
Designer enables this option when you use the dialog box for editing a crosstab and the parent object containing the crosstab already applies a dataset. Select it if you want the crosstab to inherit the dataset from its parent.

Edit

Select to  edit the specified business view in the Business View Editor dialog box or dataset  in the Dataset Editor dialog box. Designer does not display this button when you use the dialog box in a library component. 

### 
Display Screen

Use this screen to specify the column, row, and aggregate fields to display in the crosstab.

Title

Specify the title of the crosstab.

Resources

 This box lists the available data fields that you can use to create the crosstab.

Add Column button

Select to add the specified field in the Resources box to display on the column header of the crosstab. 

Add Row button

Select to add the specified field in the Resources box to display on the row header of the crosstab.

Add Summary button

Select to add the specified field in the Resources box to create aggregations in the crosstab.

Columns/Rows

- 
Field
This column shows the fields that you add on the column/row headers of the crosstab.

- 
Label
This column shows the labels for the column/row headers. By default, Designer does not add labels for the column/row headers. You can double-click the text boxes to edit the labels, or select the Auto Map Field Name checkboxes in the text boxes to apply the display names of the fields and map the labels to the dynamic display names of the fields at runtime if the Server administrator defines them.

- 
Color
This column shows the background colors that you select for the fields. Double-click in the text box and select the color from the drop-down list.

- 
Sort button
Select a field  and select the button to specify the order to sort values of the field, ascending or descending.

Summaries

- 
Field
This column shows the fields that you add as aggregate fields to create aggregations in the crosstab.

- 
Aggregate
This column shows the aggregate functions that you select for the fields to calculate data.

- 
Distinct On
Designer enables this option and you should set it when you select DistinctSum as the aggregate function. Select the ellipsis  to select the fields according to whose unique values to calculate DistinctSum in the Select Fields dialog box.

- 
Label
This column shows the labels for the aggregations. By default, Designer does not add labels for the aggregations. You can double-click the text boxes to edit the labels, or select the Auto Map Field Name checkboxes in the text boxes to apply the display names of the fields and map the labels to the dynamic display names of the fields at runtime if the Server administrator defines them.

- 
Comparison Function
Select to open the Comparison Function dialog box to add a comparison function for the selected aggregate field.

Move Up button

Select to move the specified field higher in the display order.

Move Down button

Select to move the specified field lower in the display order.

Remove button

Select to delete the specified field from the crosstab.

### 
Dataset Filter Screen

Use this screen to filter the dataset the crosstab applies.

Designer displays the same options in the Dataset Filter screen as those in the Edit Dataset Filter dialog box.

### 
Layout Screen

Use this screen to specify the layout of the crosstab. For more information about the layout settings, see Customizing the Layout of a Crosstab.

### 
Style Screen

Use this screen to specify the style of the crosstab.

Style

This box lists the styles you can apply. Select the style for the crosstab.

- 
<Custom>
This style contains no information. Designer uses it to support reports that was built with previous versions which did not bind any style, or when Designer cannot find the bound style in the style list.
            

Preview

This box displays a diagram illustrating the effect of the selected style on the crosstab.

Inherit Style

Designer displays this option when you use the dialog box for editing a crosstab and the crosstab is inside a banded object. Select it if you want the crosstab to inherit the style of its parent. 

Page Setup

Designer displays this button when you use the dialog box for creating a crosstab in a page report tab. Select it to open the Page Setup dialog box to specify page properties for the report tab.

## 
 Crosstab Wizard Dialog Box - Query Based

When you use the Crossatab Wizard dialog box for creating or editing a crosstab using a query resource, Designer displays the following screens in the dialog box (Designer displays some screens only when you use the dialog box for creating a crosstab): 

- Data Screen

- Display Screen

- Chart Screen

- Filter Screen

- Layout Screen

- Style Screen

Designer displays these buttons in all the screens:

Back

Select to go back to the previous screen.

Next

Select to go to the next screen.

Finish

Select to finish your work and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.

### 
Data Screen

        Use this screen to specify the dataset for the crosstab.

Data resource box

This box lists the predefined data resources in the current catalog. Select one and Designer automatically creates a dataset based on it for the crosstab.

- 
<New XXX...>/<Add XXX...>
Select to create or add a data resource of the same type in the catalog.

More Options/Less Options

Select to show or hide the options for specifying the dataset you want to use.

- 
New Dataset
Select to create a dataset based on a data resource in the current catalog.

- 
Existing Dataset
Select to use a dataset from the ones that you have created in the current report.- 
<New Dataset...>
Select  to create a dataset using the New Dataset dialog box.

- 
Current Dataset
Designer enables this option when you use the dialog box for editing a crosstab and the parent object containing the crosstab already applies a dataset. Select it if you want the crosstab to inherit the dataset from its parent.

Edit

Select to  edit the specified query in the Query Editor dialog box or dataset in the Dataset Editor dialog box.

### 
Display Screen

Use this screen to specify the column, row, and aggregate fields to display in the crosstab.

Resources

This box lists the resources in and related to the specified query resource, which you can use to create the crosstab.

Add Column button

Select to add the specified field in the Resources box to display on the column header of the crosstab. 

Add Row button

Select to add the specified field in the Resources box to display on the row header of the crosstab.

Add Summary button

Select to add the specified field in the Resources box on which to create aggregations in the crosstab.

Columns/Rows

- 
Field
This column shows the fields that you add to display on the column/row headers of the crosstab.

- 
Label
This column shows the labels for the column/row headers. By default, Designer does not add labels for the column/row headers. You can double-click the text boxes to edit the labels.

- 
Color
This column shows the background colors that you select for the fields. Double-click in the text box and select the color from the drop-down list.

- 
Sort button
Select a field and select the button to specify the order to sort values of the field, ascending or descending.

- 
Add Compound Group button
Select to add a compound column/row group.
  

Summaries

- 
Field
This column shows the fields that you add as aggregate fields to create aggregations in the crosstab.

- 
Aggregate
This column shows the aggregate functions that you select for the fields to calculate data. Double-click in the text box and select the function from the drop-down list.

- 
Distinct On
Designer enables this option and you should set it when you select DistinctSum as the aggregate function. Select the ellipsis  to select the fields according to whose unique values to calculate DistinctSum in the Select Fields dialog box.

- 
Label
This column shows the labels for the aggregations. By default, Designer does not add labels for the aggregations. You can double-click the text boxes to edit the labels.

- 
Comparison Function
Select to open the Comparison Function dialog box to add a comparison function for the selected aggregate field.

Move Up button

Select to move the specified field or compound group higher in the display order. For fields in a compound group, you can change their order within the current group only.

Move Down button

Select to move the specified  field or compound group lower in the display order. For fields in a compound group, you can change their order within the current group only.

Remove button

Select to delete the specified field or compound group from the crosstab.

### 
Chart Screen

Designer displays the Chart screen when you use the dialog box for creating a crosstab, and enables the options in the screen when you have added at least one field on the column or row header and one aggregate field in the crosstab. You can use the screen to create a chart together with the crosstab, which Designer places above the crosstab in the report body

No Chart

Select if you do not want to create the chart.

Bar Chart

Select to create a Clustered Bar 2-D chart together with the crosstab.

Line Chart

Select to create a Line 2-D chart together with the crosstab.

Pie Chart

Select to create a Clustered Pie chart together with the crosstab.

Category

This drop-down list contains the fields that you add to the column and row headers of the crosstab. Select the field you want to display on the category (X) axis of the chart.

Series

This drop-down list contains the fields that you add to the column and row headers of the crosstab. Select the field you want to display on the series (Z) axis of the chart.

Show Values

This drop-down list contains the fields that you add as aggregate fields in the crosstab. Select the value you want to display in the chart.

### 
Filter Screen

Use this screen to narrow down the data to display in the crosstab. 

Designer displays the same options in the Filter screen as those in the Edit Filter dialog box.

### 
Layout Screen

Use this screen to specify the layout of the crosstab. For more information about the layout settings, see Customizing the Layout of a Crosstab.

### 
Style Screen

Use this screen to specify the style of the crosstab.

Style

This box lists the styles you can apply. Select the style for the crosstab.

- 
<Custom>
This style contains no information. Designer uses it to support reports that was built with previous versions which did not bind any style, or when Designer cannot find the bound style in the style list.
            

Preview

This box displays a diagram illustrating the effect of the selected style on the crosstab.

Inherit Style

Designer displays this option when  you use the dialog box for editing a crosstab and the crosstab is inside a banded object. Select it if you want the crosstab to inherit the style of its parent. 

Page Setup

Designer displays this button when you use the dialog box for creating a crosstab in a page report tab. Select it to open the Page Setup dialog box to specify page properties for the report tab.

Previous Topic  Next Topic
