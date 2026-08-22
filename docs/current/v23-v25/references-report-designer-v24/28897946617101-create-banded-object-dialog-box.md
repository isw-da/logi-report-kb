---
title: "Create Banded Object Dialog Box"
id: 28897946617101
section: "References - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897946617101-Create-Banded-Object-Dialog-Box
updated_at: 2024-09-30T09:13:23Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Create Banded Object Dialog Box

You can use the Create Banded Object dialog box to create a banded object in a report. This topic describes the options in the dialog box.
    

 Designer displays the Create Banded Object dialog box when you navigate to Insert > Banded Object, and provides you with different options in the dialog box according to the type of the data resource you use for the banded object: business view or query resource.

## 
Create Banded Object Dialog Box - Business View Based 

When you use the Create Banded Object dialog box for creating a banded object using a business view, Designer displays the following screens in the dialog box:

- Data Screen

- Display Screen

- Group Screen

- Summary Screen

- Dataset Filter Screen

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

        Use this screen to specify the dataset for the banded object.

Business view box

This box lists the predefined business views in the current catalog. Select one and Designer automatically creates a dataset based on it for the banded object.

- 
<New Business View...>
Select to create a business view in the catalog using the Business View Editor dialog box.

More Options/Less Options

Select to show or hide the options for specifying the dataset you want to use. 

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
Designer enables this option when the parent object where you have specified to insert the banded object already applies a dataset. Select it if you want the banded object to inherit the dataset from its parent.

Edit

Select to  edit the specified business view in the Business View Editor dialog box or dataset  in the Dataset Editor dialog box. 

### 
Display Screen

Use this screen to specify the detail fields you want to display in the banded object.

Resources

This box lists the available data fields that you can use as detail fields in the banded object.

Add button

Select to add the specified field in the Resources box to the banded object.

Remove button

Select to remove the specified field from the banded object.

Move Up button

Select to move the specified field higher in the display order.

Move Down button

Select to move the specified field lower in the display order.

Display Fields 

This column shows the detail fields that you add to display in the banded object.

Display Name

This column shows the labels of the detail fields in the banded object, which by default are the display names of the added fields. You can select in the text boxes to edit the labels, or select the Auto Map Field Name checkboxes in the text boxes to apply the display names of the fields and map the labels to the dynamic display names of the fields at runtime if the Server administrator defines them.

Sort Fields By

Select  to open the Sort Fields By dialog box to specify how to sort the detail data in the banded object.

### 
Group Screen

        Use this screen to specify the criteria for grouping data in the banded object.

Resources

This box lists the available data fields that you can use as group-by fields in the banded object. 

Add button

Select to add the specified field in the Resources box as a group-by field in the banded object.

Remove button

Select to remove the specified group-by field from the banded object.

Move Up button

Select to move the specified group to a higher group level.

Move Down button

Select to move the specified group to a lower group level.

Group By 

This column shows the group-by fields on which you select to group data in the banded object.

Sort

This column shows how you want to sort groups at each group level. You can select from the following options:

- 
Ascend
Select to sort groups at the specified group level in an ascending order (A, B, C).

- 
Descend
Select to sort groups at the specified group level in a descending order (C, B, A).

- 
No Sort
Select to sort groups at the specified group level  in their original order in database.

- 
Custom Sort
Select to open the Custom Sort dialog box to set how to sort the groups at the specified group level.

Select N

Select to open the Select N dialog box to specify the Select N condition for the specified group level.

### 
Summary Screen

Use this screen to specify the summaries to calculate data in the banded object.

Resources

This box lists the available data fields that you can use to calculate data in the banded object.

Add button

Select to add the specified field in the Resources box to calculate data in the banded object.

Remove button

Select to remove the specified summary from the banded object.

Move Up button

Select to move the specified summary higher in the display order.

Move Down button

Select to move the specified summary lower in the display order.

Summarized Fields

This column shows the fields that you add to calculate data in the banded object.

Position

This column shows the position of the summaries. Designer places the summary added for a group level in the group's footer panel; if you add a summary for the Banded Object level, Designer places it in the banded footer panel. 

Column

This column shows where to place the summaries. By default, Designer places the summaries and their name labels in the first two detail columns.

### 
Dataset Filter Screen

Use this screen to filter the dataset the banded object applies.

Designer displays the same options in the Dataset Filter screen as those in the Edit Dataset Filter dialog box.

### 
Style Screen

Use this screen to specify the style of the banded object.

Grow Report

This box displays in which layout to create the banded object, which can only be Vertically.

Style

This box lists the styles you can apply. Select the style for the banded object.

Preview

This box displays a diagram illustrating the effect of the selected style on the banded object.

Inherit Style

Designer displays this option and selects it by default when  you have specified to insert the banded object  into another banded object.  Clear it if you do not want the banded object to inherit the style of its parent. 

## 
Create Banded Object Dialog Box - Query Based 

When you use the Create Banded Object dialog box for creating a banded object using a query resource, Designer displays the following screens in the dialog box:

- Data Screen

- Display Screen

- Group Screen

- Summary Screen

- Filter Screen

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

        Use this screen to specify the dataset for the banded object.

Data resource box

This box lists the predefined data resources in the current catalog. Select one and Designer automatically creates a dataset based on it for the banded object.

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
Designer enables this option when the parent object where you have specified to insert the banded object already applies a dataset. Select it if you want the banded object to inherit the dataset from its parent.

Edit

Select to  edit the specified query in the Query Editor dialog box or dataset in the Dataset Editor dialog box.

### 
Display Screen

Use this screen to specify the detail fields you want to display in the banded object.

Resources

This box lists the available data fields that you can use as detail fields in the banded object.

Add button

Select to add the specified field in the Resources box to the banded object.

Remove button

Select to remove the specified field from the banded object.

Move Up button

Select to move the specified field higher in the display order.

Move Down button

Select to move the specified field lower in the display order.

Display Fields

This column shows the detail fields that you add to display in the banded object.

Display Name

This column shows the labels of the detail fields in the banded object, which by default are the display names of the added fields. You can select in the text boxes to edit the labels.

Sort Fields By

Select to open the Sort Fields By dialog box to specify how to sort the detail data in the banded object.

### 
Group Screen

        Use this screen to specify the criteria for grouping data in the banded object.

Resources

This box lists the available data fields that you can use as group-by fields in the banded object.

Add button

Select to add the specified field in the Resources box as a group-by field in the banded object.

Remove button

Select to remove the specified group-by field from the banded object.

Move Up button

Select to move the specified group to a higher group level.

Move Down button

Select to move the specified group to a lower group level.

Group By

This column shows the group-by fields on which you select to group data in the banded object.

Sort

This column shows how you want to sort groups at each group level. You can select from the following options:

- 
Ascend
Select to sort groups at the specified group level in an ascending order (A, B, C).

- 
Descend
Select to sort groups at the specified group level in a descending order (C, B, A).

- 
No Sort
Select to sort groups at the specified group level  in their original order in database.

- 
Special Group
Select to open the User Defined Group dialog box to define grouping information.

- 
Custom Sort
Select to open the Custom Sort dialog box to set how to sort the groups at the specified group level.

Special Function

This column shows the special functions that you select for the group-by fields of the Numeric, String, Date, and Time data types. Select a special function from the drop-down list to specify to which level to  group the data of the specified field, or select Customize to set the function in the Customized Function dialog box.

Custom Sort

 Designer enables this button after you have selected Custom Sort from the Sort column to define the sort manner of groups for the specified group level. Select it to specify how to sort the groups.

Special Group 

Designer enables this button after you have selected Special Group from the Sort column to define a special group. Select it to specify how to group your information. 

Select N

Select to open the Select N dialog box to specify the Select N condition for the specified group level.

Group Filter

Select to open the Group Filter dialog box to specify the group filter condition.

### 
Summary Screen

Use this screen to specify the fields on which to create summaries in the banded object. 

Resources

This box lists the available data fields that you can use to create summaries in the banded object. 

Add button

Select to add the specified field in the Resources box based on which to create a summary in the banded object.

Remove button

Select to remove the specified summary from the banded object.

Move Up button

Select to move the specified summary higher in the display order.

Move Down button

Select to move the specified summary lower in the display order.

Summarized Fields 

This column shows the fields that you add to create summaries in the banded object.

Aggregate Function

This column shows the aggregate functions that you select to use for the summaries. 

Distinct On

Designer enables this option and you should set it when you select DistinctSum as the aggregate function. Select the ellipsis  to select the fields according to whose unique values to calculate DistinctSum in the Select Fields dialog box.

Break Field

This column shows the groups on which  to calculate the summaries. If you add a summary for the Banded Object level, the break field is null and Designer calculates the summary based on the whole dataset.

Position

You can use this option together with the Column option to specify the location where to place a summary.

- 
Header
Select to place the summary in the header panel. When you add the summary for a specific group, Designer places it in the group's header panel; if you add the summary for the Banded Object level, Designer places it in the banded header panel.

- 
Footer
Select to place the summary in the footer panel. When you add the summary for a specific group, Designer places it in the group's footer panel; if you add the summary for the Banded Object level, Designer places it in the banded footer panel.

Column

You can use this option together with the Position option to specify the location where to place a summary.

- 
Detail
Select to place the summary and its name label in the first two detail columns.

- 
Summary
Select to place the summary  in a separate summary column.

### 
Filter Screen

Use this screen to narrow down the data to display in the banded object. 

Designer displays the same options in the Filter screen as those in the Edit Filter dialog box.

### 
Style Screen

Use this screen to specify the style of the banded object.

Grow Report

This box lists the layouts in which you can create the banded object.

- 
Vertically
Select to create a vertical banded object.

- 
Horizontally
Select  to create a horizontal banded object.

- 
Mailing Label Format
Select  to create a cross banded object in the form of a mailing label layout.

Style

This box lists the styles you can apply. Select the style for the banded object.

Preview

This box displays a diagram illustrating the effect of the selected style on the banded object.

Inherit Style

Designer displays this option and selects it by default when you have specified to insert the banded object into another banded object. Clear it if you do not want the banded object to inherit the style of its parent.

Previous Topic  Next Topic
