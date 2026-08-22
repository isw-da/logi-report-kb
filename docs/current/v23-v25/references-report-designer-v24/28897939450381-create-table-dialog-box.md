---
title: "Create Table Dialog Box"
id: 28897939450381
section: "References - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897939450381-Create-Table-Dialog-Box
updated_at: 2024-09-30T09:11:16Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Create Table Dialog Box

You can use the Create Table dialog box to create a table in a report. This topic describes the options in the dialog box.
    

Designer displays the Create Table dialog box when you choose a table type and select OK in the Table Type dialog box, or drag a table type icon from the Components panel into a report,  and provides you with different options in the dialog box according to the type of the data resource you use for the table: business view or query resource.

## 
Create Table Dialog Box - Business View Based

When you use the Create Table dialog box to create tables using business views in web reports/library components, Designer displays different screens in the dialog box according to the type of the table: group table or summary table; there is no such difference when you use the dialog box for creating tables in page reports.

### For Table in Page Report and Group Table in Web Report/Library Component 

When you use the Create Table dialog box for creating a table in a page report or creating a group table in a web report/library component using a business view, Designer displays the following screens in the dialog box:

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

#### 
Data Screen

        Use this screen to specify the dataset for the table.

Business view box

This box lists the predefined business views in the current catalog. Select one and Designer automatically creates a dataset based on it for the table.

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
Designer enables this option when the parent object where you have specified to insert the table already applies a dataset. Select it if you want the table to inherit the dataset from its parent.

Edit

Select to  edit the specified business view in the Business View Editor dialog box or dataset  in the Dataset Editor dialog box. Designer does not display this button when you use the dialog box in a library component. 

#### 
Display Screen

Use this screen to specify the detail fields you want to display in the table.

Title

Specify the title of the table.

Resources

This box lists the available data fields that you can use as detail fields in the table.

Add button

Select to add the specified field in the Resources box to the table. 

Remove button

Select to remove the specified field from the table.

Move Up button

Select to move the specified field higher in the display order.

Move Down button

Select to move the specified field lower in the display order.

Display Fields 

This column shows the detail fields that you add to display in the table.

Display Name

This column shows the labels of the detail fields in the table, which by default are the display names of the added fields. You can select in the text boxes to edit the labels, or select the Auto Map Field Name checkboxes in the text boxes to apply the display names of the fields and map the labels to the dynamic display names of the fields at runtime if the Server administrator defines them.

Sort Fields By

Select to open the Sort Fields By dialog box to specify how to sort the detail data in the table. 

#### 
Group Screen

        Use this screen to specify the criteria for grouping data in the table.

Resources

This box lists the available data fields that you can use as group-by fields in the table. 

Add button

Select to add the specified  field in the Resources box as a group-by field in the table. 

Remove button

Select to remove the specified group-by field from the table. 

Move Up button

Select to move the specified group to a higher group level.

Move Down button

Select to move the specified group to a lower group level.

Group By

This column shows the group-by fields on which you select to group data in the table.

Sort

This column shows how you specify to sort groups at each group level. You can select from the following options:

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

#### 
Summary Screen

Use this screen to specify the summaries to calculate data in the table.

Resources

 This box lists the available data fields that you can use to calculate data in the table. 

Add button

Select to add the specified field in the Resources box to calculate data in the table.

Remove button

Select to remove the specified summary from the table.

Move Up button

Select to move the specified summary higher in the display order.

Move Down button

Select to move the specified summary lower in the display order.

Summarized Fields 

This column shows the fields that you add to calculate data in the table.

Position

You can use this option together with the Column option to specify the location where to place a summary.

- 
Footer
Select to place the summary in the footer panel. When you add the summary for a specific group, Designer places it in the group's footer panel; if you add the summary for the Table level, Designer places it in the table footer panel.

- 
Header
Select to place the summary in the header panel. When you add the summary for a specific group, Designer places it in the group's header panel; if you add the summary for the Table level, Designer places it in the table header panel. Designer disables this option when the table type is Group Above. 

Column

You can use this option together with the Position option to specify the location where to place a summary.

- 
Detail
Select to place the summary and its name label in the first two detail columns.

- 
Summary
Select to place the summary in a separate summary column. Designer disables this option when the table type is Group Above. 

#### 
Dataset Filter Screen

Use this screen to filter the dataset the table applies.

Designer displays the same options in the Dataset Filter screen as those in the Edit Dataset Filter dialog box.

#### 
Style Screen

Use this screen to specify the style of the table.

Grow Report

This box lists the layouts in which you can create the table.

- 
Vertically
Select to create a vertical table.

- 
Horizontally
Select to create a horizontal table. Designer displays this option when you are creating the table in a  page report.

Style

This box lists the styles you can apply. Select the style for the table.

Preview

This box displays a diagram illustrating the effect of the selected style on the table.

Inherit Style

Designer displays this option and selects it by default when  you have specified to insert the table into a banded object.  Clear it if you do not want the table to inherit the style of its parent. 

### 
For Summary Table in Web Report/Library component

When you use the Create Table dialog box for creating a summary table in a web report/library component using a business view, Designer displays the following screens in the dialog box:

- Data Screen

- Columns Screen

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

#### 
Data Screen

        Use this screen to specify the dataset for the table.

Business view box

This box lists the predefined business views in the current catalog. Select one and Designer automatically creates a dataset based on it for the table.

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
Designer enables this option when the parent object where you have specified to insert the table already applies a dataset. Select it if you want the table to inherit the dataset from its parent.

Edit

Select to  edit the specified business view in the Business View Editor dialog box or dataset  in the Dataset Editor dialog box. Designer does not display this button when you use the dialog box in a library component. 

#### 
Columns Screen

Use this screen to specify the fields to create columns in the table.

Resources

This box lists the available data fields that you can use to create columns in the table. You can create detail columns from detail objects, group columns from group objects, and summary columns from aggregation objects.

Add button

Select to add the specified field in the Resources box to create a column in the table.

Remove button

Select to remove the specified field from the table. 

Move Up button

Select to move the specified field higher in the display order.

Move Down button

Select to move the specified field lower in the display order.

Column

This column shows the fields that you add to create columns in the table.

Sort

For each group column, you can specify how to sort the groups at the group level using the following options:

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

#### 
Summary Screen

Use this screen to insert summaries to the header/footer panels of the table and groups.

Resources

This box lists the aggregation objects that you add to create summary columns in the table in the Columns screen.

Summarized Fields

This column shows the group objects that you add to create group columns in the table in the Columns screen.

Header

The checkboxes represent the table header and the group headers of the added groups. After selecting an aggregation object in the Resources box, you can select the checkboxes to insert it in the corresponding header panels.

Footer

The checkboxes represent the table footer and the group footers of the added groups. After select an aggregation object in the Resources box, you can select the checkboxes to insert it in the corresponding footer panels.

#### 
Dataset Filter Screen

Use this screen to filter the dataset the table applies.

Designer displays the same options in the Dataset Filter screen as those in the Edit Dataset Filter dialog box.

#### 
Style Screen

Use this screen to specify the style of the table.

Grow Report

This box displays in which layout to create the table, which can only be Vertically.

Style

This box lists the styles you can apply. Select the style for the table.

Preview

This box displays a diagram illustrating the effect of the selected style on the table.

Inherit Style

Designer displays this option and selects it by default when you have specified to insert the table into a banded object.  Clear it if you do not want the table to inherit the style of its parent. 

## 
Create Table Dialog Box - Query Based

When you use the Create Table dialog box for creating a table using a query resource, Designer displays the following screens in the dialog box:

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

        Use this screen to specify the dataset for the table.

Data resource box

This box lists the predefined data resources in the current catalog. Select one and Designer automatically creates a dataset based on it for the table.

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
Designer enables this option when the parent object where you have specified to insert the table already applies a dataset. Select it if you want the table to inherit the dataset from its parent.

Edit

Select to  edit the specified query in the Query Editor dialog box or dataset in the Dataset Editor dialog box.

### 
Display Screen

Use this screen to specify the detail fields you want to display in the table.

Resources

This box lists the available data fields that you can use as detail fields in the table.

Add button

Select to add the specified field in the Resources box to the table.

Remove button

Select to remove the specified field from the table.

Move Up button

Select to move the specified field higher in the display order.

Move Down button

Select to move the specified field lower in the display order.

Display Fields

This column shows the detail fields that you add to display in the table.

Display Name

This column shows the labels of the detail fields in the table, which by default are the display names of the added fields. You can select in the text boxes to edit the labels.

Sort Fields By

Select to open the Sort Fields By dialog box to specify how to sort the detail data in the table.

### 
Group Screen

        Use this screen to specify the criteria for grouping data in the table.

Resources

This box lists the available data fields that you can use as group-by fields in the table.

Add button

Select to add the specified field in the Resources box as a group-by field in the table.

Remove button

Select to remove the specified group-by field from the table.

Move Up button

Select to move the specified group to a higher group level.

Move Down button

Select to move the specified group to a lower group level.

Group By

This column shows the group-by fields on which you select to group data in the table.

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

Use this screen to specify the fields on which to create summaries in the table. 

Resources

This box lists the available data fields that you can use to create summaries in the table. 

Add button

Select to add the specified field in the Resources box based on which to create a summary in the table.

Remove button

Select to remove the specified summary from the table.

Move Up button

Select to move the specified summary higher in the display order.

Move Down button

Select to move the specified summary lower in the display order.

Summarized Fields 

This column shows the fields that you add to create summaries in the table.

Aggregate Function

This column shows the aggregate functions that you select to use for the summaries. 

Distinct On

Designer enables this option and you should set it when you select DistinctSum as the aggregate function. Select the ellipsis  to select the fields according to whose unique values to calculate DistinctSum in the Select Fields dialog box.

Break Field

This column shows the groups on which  to calculate the summaries. If you add a summary for the Table level, the break field is null and Designer calculates the summary based on the whole dataset.

Position

You can use this option together with the Column option to specify the location where to place a summary.

- 
Footer
Select to place  the summary in the footer panel. When you add the summary for a specific group, Designer places it in the group's footer panel; if you add the summary for the Table level, Designer places it in the table footer panel.

- 
Header
Select to place the summary in the header panel. When you add the summary for a specific group, Designer places it in the group's header panel; if you add the summary for the Table level, Designer places it in the table header panel. Designer disables this option when the table type is Group Above.

Column

You can use this option together with the Position option to specify the location where to place a summary.

- 
Detail
Select to place the summary and its name label in the first two detail columns.

- 
Summary
Select to place the summary  in a separate summary column. Designer disables this option when the table type is Group Above.

### 
Filter Screen

Use this screen to narrow down the data to display in the table.

Designer displays the same options in the Filter screen as those in the Edit Filter dialog box.

### 
Style Screen

Use this screen to specify the style of the table.

Grow Report

This box lists the layouts in which you can create the table.

- 
Vertically
Select  to create a vertical table.

- 
Horizontally
Select to create a horizontal table.

Style

This box lists the styles you can apply. Select the style for the table.

Preview

This box displays a diagram illustrating the effect of the selected style on the table.

Inherit Style

Designer displays this option and selects it by default when you have specified to insert the table into a banded object. Clear it if you do not want the table to inherit the style of its parent.

Previous Topic  Next Topic
