---
title: "Create Table Dialog Box"
id: 4405664441879
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664441879-Create-Table-Dialog-Box
updated_at: 2022-03-28T07:00:37Z
---

# Create Table Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664440983-Create-Query-s-Username-and-Password-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661478039-Crosstab-Formula-Editor-Dialog-Box)

# Create Table Dialog Box

You can use the Create Table dialog box to [create a table](https://devnet.logianalytics.com/hc/en-us/articles/4405661401239-Inserting-Tables-in-a-Report) in a report. This topic describes the options in the dialog box.

Designer displays the Create Table dialog box when you choose a table type and select OK in the [Table Type dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661736215-Table-Type-Dialog-Box), or drag a table type icon from the Components panel into a report, and provides you with different options in the dialog box according to the type of the data resource used for the table: [business view](#BV) or [query resource](#Query).

## Create Table Dialog Box - Business View Based

When you use the Create Table dialog box to create tables using business views in web reports/library components, Designer displays different screens in the dialog box according to the type of the table: group table or summary table; there is no such difference when you use the dialog box for creating tables in page reports.

### For Table in Page Report and Group Table in Web Report/Library Component

When you use the Create Table dialog box for creating a table in a page report or creating a group table in a web report/library component using a business view, you see the following screens in the dialog box:

* [Data Screen](#BVData)
* [Display Screen](#BVDisplay)
* [Group Screen](#BVGroup)
* [Summary Screen](#BVSummary)
* [Filter Screen](#BVFilter)
* [Style Screen](#BVStyle)

You see these buttons in all the screens:

**Back**

Select to go back to the previous screen.

**Next**

Select to go to the next screen.

**Finish**

Select to finish your work and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

#### Data Screen

Use this screen to specify the dataset for the table. You can select from all the predefined business views in the current catalog and Designer automatically creates a dataset based on the business view you select.

![Create Table - Data](https://devnet.logianalytics.com/hc/article_attachments/4420410807831/crttbl_dt_bv1.gif)

**Inherit from the Parent**

Designer displays this option only when you have specified to insert the table into any of the following panels in a banded object: banded header panel, banded footer panel, group header panel, or group footer panel. Select it if you want the table to inherit the business view that its parent banded object uses.

#### Display Screen

Use this screen to specify the detail fields to display in the table.

![Create Table - Display](https://devnet.logianalytics.com/hc/article_attachments/4420410808087/crttbl_dsply_bv.gif)

**Title**

Specify the title for the table.

**Resources**

This box lists the resources in and related to the specified business view, which you can use as detail fields in the table.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420410583703/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box to the table.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420394644119/btn_rmvarrow.gif)**Remove button**

Select to remove the specified field from the table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420410588439/btn_mvup.gif)**Move Up button**

Select to move the specified field higher in the display order.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420410588695/btn_mvdwn.gif)**Move Down button**

Select to move the specified field lower in the display order.

**Display Fields**

This column shows the detail fields that you add to display in the table.

**Display Name**

This column shows the labels of the detail fields in the table, which by default are the display names of the added fields. You can select in the text boxes to edit the labels, or select the **Auto Map Field Name** checkboxes in the text boxes to apply the display names of the fields and map the labels to the dynamic display names of the fields at runtime if the Server administrator defines them.

**Sort Fields By**

Select to the [Sort Fields By dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661721239-Sort-Fields-By-Dialog-Box) to specify how to sort the detail data in the table.

#### Group Screen

Use this screen to specify the criteria for grouping data in the table.

![Create Table - Group](https://devnet.logianalytics.com/hc/article_attachments/4420410808343/crttbl_grp_bv.gif)

**Resources**

This box lists the resources in and related to the specified business view, which you can use as group-by fields in the table.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420410583703/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box as a group-by field in the table.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420394644119/btn_rmvarrow.gif)**Remove button**

Select to remove the specified group-by field from the table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420410588439/btn_mvup.gif)**Move Up button**

Select to move the specified group to a higher group level.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420410588695/btn_mvdwn.gif)**Move Down button**

Select to move the specified group to a lower group level.

**Group By**

This column shows the group-by fields on which you select to group data in the table.

**Sort**

This column shows how you specify to sort groups at each group level. You can select from the following options:

* **Ascend**  
  Select to sort groups at the specified group level in an ascending order (A, B, C).
* **Descend**  
  Select to sort groups at the specified group level in a descending order (C, B, A).
* **No Sort**  
  Select to sort groups at the specified group level in their original order in database.
* **Custom Sort**  
  Select to open the [Custom Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664443927-Custom-Sort-Dialog-Box) to set how to sort the groups at the specified group level.

**Select N**

Select to open the [Select N dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661712151-Select-N-Dialog-Box) to specify the Select N condition for the specified group level.

#### Summary Screen

Use this screen to specify the summaries to calculate data in the table.

![Create Table - Summary](https://devnet.logianalytics.com/hc/article_attachments/4420394833559/crttbl_sum_bv1.gif)

**Resources**

This box lists the resources in and related to the specified business view, which you can use to calculate data in the table.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420410583703/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box to calculate data in the table.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420394644119/btn_rmvarrow.gif)**Remove button**

Select to remove the specified summary from the table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420410588439/btn_mvup.gif)**Move Up button**

Select to move the specified summary higher in the display order.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420410588695/btn_mvdwn.gif)**Move Down button**

Select to move the specified summary lower in the display order.

**Summarized Fields**

This column shows the fields that you add to calculate data in the table.

**Position**

You can use this option together with the Column option to specify the location where to place a summary.

* **Footer**  
  Select to place the summary in the footer panel. When you add the summary for a specific group, Designer places it in the group's footer panel; if you add the summary for the Table level, Designer places it in the table footer panel.
* **Header**  
  Select to place the summary in the header panel. When you add the summary for a specific group, Designer places it in the group's header panel; if you add the summary for the Table level, Designer places it in the table header panel. Designer disables this option when the table type is Group Above.

**Column**

You can use this option together with the Position option to specify the location where to place a summary.

* **Detail**  
  Select to place the summary and its name label in the first two detail columns.
* **Summary**  
  Select to place the summary in a separate summary column. Designer disables this option when the table type is Group Above.

#### Filter Screen

Use this screen to narrow down the data to display in the table.

Designer displays the same options in the Filter screen as in the [Edit Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661510295-Edit-Filter-Dialog-Box).

![Create Table - Filter](https://devnet.logianalytics.com/hc/article_attachments/4420394833815/crttbl_fltr_bv1.gif)

#### Style Screen

Use this screen to specify the style of the table.

![Create Table - Style](https://devnet.logianalytics.com/hc/article_attachments/4420402503191/crttbl_sty.gif)

**Grow Report**

This box lists the layouts in which you can create the table.

* **Vertically**  
  Select to create a vertical table.
* **Horizontally**  
  Select to create a horizontal table. Designer displays this option only when you are creating the table in a page report.

**Style**

This box lists the styles that you can apply to the table. Select the style for the table.

**Preview**

This box displays a diagram illustrating the effect of the selected style on the table.

**Inherit Style**

Designer displays this option and selects it by default when you have specified to insert the table into a banded object. Clear it if you do not want the table to inherit the style of its parent.

### For Summary Table in Web Report/Library component

When you use the Create Table dialog box for creating a summary table in a web report/library component using a business view, you see the following screens in the dialog box:

* [Data Screen](#Data1)
* [Columns Screen](#Columns)
* [Summary Screen](#Summary1)
* [Filter Screen](#Filter1)
* [Style Screen](#Style1)

You see these buttons in all the screens:

**Back**

Select to go back to the previous screen.

**Next**

Select to go to the next screen.

**Finish**

Select to finish your work and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

#### Data Screen

Use this screen to specify the dataset for the table. You can select from all the predefined business views in the current catalog and Designer automatically creates a dataset based on the business view you select.

![Create Summary Table - Data](https://devnet.logianalytics.com/hc/article_attachments/4420410809111/crttbl_dt_bv2.gif)

**Inherit from the Parent**

Designer displays this option only when you have specified to insert the table into any of the following panels in a banded object: banded header panel, banded footer panel, group header panel, or group footer panel. Select it if you want the table to inherit the business view that its parent banded object uses.

#### Columns Screen

Use this screen to specify the fields to create columns in the table.

![Create Summary Table - Columns](https://devnet.logianalytics.com/hc/article_attachments/4420410809495/crttbl_clmn.gif)

**Resources**

This box lists the resources in and related to the specified business view, which you can use to create columns in the table. You can create detail columns from detail objects, group columns from group objects, and summary columns from aggregation objects.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420410583703/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box to create a column in the table.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420394644119/btn_rmvarrow.gif)**Remove button**

Select to remove the specified field from the table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420410588439/btn_mvup.gif)**Move Up button**

Select to move the specified field higher in the display order.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420410588695/btn_mvdwn.gif)**Move Down button**

Select to move the specified field lower in the display order.

**Column**

This column shows the fields that you add to create columns in the table.

**Sort**

For each group column, you can specify how to sort the groups at the group level using the following options:

* **Ascend**  
  Select to sort groups at the specified group level in an ascending order (A, B, C).
* **Descend**  
  Select to sort groups at the specified group level in a descending order (C, B, A).
* **No Sort**  
  Select to sort groups at the specified group level in their original order in database.
* **Custom Sort**  
  Select to open the [Custom Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664443927-Custom-Sort-Dialog-Box) to set how to sort the groups at the specified group level.

**Select N**

Select to open the [Select N dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661712151-Select-N-Dialog-Box) to specify the Select N condition for the specified group level.

#### Summary Screen

Use this screen to insert summaries to the header/footer panels of the table and groups.

![Create Summary Table - Summary](https://devnet.logianalytics.com/hc/article_attachments/4420394834839/crttbl_sum_bv2.gif)

**Resources**

This box lists the aggregation objects that you add to create summary columns in the table in the Columns screen.

**Summarized Fields**

This column shows the group objects that you add to create group columns in the table in the Columns screen.

**Header**

The checkboxes represent the table header and the group headers of the added groups. After selecting an aggregation object in the Resources box, you can select the checkboxes to insert it in the corresponding header panels.

**Footer**

The checkboxes represent the table footer and the group footers of the added groups. After select an aggregation object in the Resources box, you can select the checkboxes to insert it in the corresponding footer panels.

#### Filter Screen

Use this screen to narrow down the data to display in the table.

Designer displays the same options in the Filter screen as in the [Edit Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661510295-Edit-Filter-Dialog-Box).

![Create Summary Table - Filter](https://devnet.logianalytics.com/hc/article_attachments/4420410809879/crttbl_fltr_bv2.gif)

#### Style Screen

Use this screen to specify the style of the table.

![Create Summary Table - Style](https://devnet.logianalytics.com/hc/article_attachments/4420410810391/crttbl_sty_bv.gif)

**Grow Report**

This box displays in which layout to create the table, which can only be Vertically.

**Style**

This box lists the styles that you can apply to the table. Select the style for the table.

**Preview**

This box displays a diagram illustrating the effect of the selected style on the table.

**Inherit Style**

Designer displays this option and selects it by default when you have specified to insert the table into a banded object. Clear it if you do not want the table to inherit the style of its parent.

## Create Table Dialog Box - Query Based

When you use the Create Table dialog box for creating a table using a query resource, you see the following screens in the dialog box:

* [Data Screen](#Data)
* [Display Screen](#Display)
* [Group Screen](#Group)
* [Summary Screen](#Summary)
* [Filter Screen](#Filter)
* [Style Screen](#Style)

You see these buttons in all the screens:

**Back**

Select to go back to the previous screen.

**Next**

Select to go to the next screen.

**Finish**

Select to finish your work and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

### Data Screen

Use this screen to specify the dataset for the table.

![Create Table - Data](https://devnet.logianalytics.com/hc/article_attachments/4420410810775/crttbl_dt.gif)

**Data resource box**

This box lists the predefined data resources in the current catalog. Select one and Designer automatically creates a dataset based on it for the table.

**More Options**/**Less Options**

Select it to show or hide the options for specifying a dataset for the table.

* **New Dataset**  
  Select to create a dataset based on a data resource in the current catalog. If you select a query, Designer enables the Edit button at the bottom and you can select the button to edit the query in the [Query Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661685015-Query-Editor-Dialog-Box). You can also select the first item under a resource node to add or create a data resource of the type in the catalog and use it to create the dataset.
* **Existing Dataset**  
  Select to use a dataset from the ones that you have created in the current page report. You can select **Edit** to modify the specified dataset in the [Dataset Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661501079-Dataset-Editor-Dialog-Box), or select **<New Dataset...>** to create a dataset in the page report using the [New Dataset dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661656087-New-Dataset-Dialog-Box).

* **Current Dataset**  
  Designer enables this option when the parent object where you have specified to insert the table already applies a dataset. Select it if you want the table to inherit the dataset from its parent.

### Display Screen

Use this screen to specify the detail fields to display in the table.

![Create Table - Display](https://devnet.logianalytics.com/hc/article_attachments/4420394836375/crttbl_dsply.gif)

**Resources**

This box lists the data fields in and related to the specified query resource, which you can use as detail fields in the table.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420410583703/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box to the table.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420394644119/btn_rmvarrow.gif)**Remove button**

Select to remove the specified field from the table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420410588439/btn_mvup.gif)**Move Up button**

Select to move the specified field higher in the display order.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420410588695/btn_mvdwn.gif)**Move Down button**

Select to move the specified field lower in the display order.

**Display Fields**

This column shows the detail fields that you add to display in the table.

**Display Name**

This column shows the labels of the detail fields in the table, which by default are the display names of the added fields. You can select in the text boxes to edit the labels.

**Sort Fields By**

Select to open the [Sort Fields By dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661721239-Sort-Fields-By-Dialog-Box) to specify how to sort the detail data in the table.

### Group Screen

Use this screen to specify the criteria for grouping data in the table.

![Create Table - Group](https://devnet.logianalytics.com/hc/article_attachments/4420410811415/crttbl_grp.gif)

**Resources**

This box lists the data fields in and related to the specified query resource, which you can use as group-by fields in the table.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420410583703/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box as a group-by field in the table.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420394644119/btn_rmvarrow.gif)**Remove button**

Select to remove the specified group-by field from the table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420410588439/btn_mvup.gif)**Move Up button**

Select to move the specified group to a higher group level.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420410588695/btn_mvdwn.gif)**Move Down button**

Select to move the specified group to a lower group level.

**Group By**

This column shows the group-by fields on which you select to group data in the table.

**Sort**

This column shows how you want to sort groups at each group level. You can select from the following options:

* **Ascend**  
  Select to sort groups at the specified group level in an ascending order (A, B, C).
* **Descend**  
  Select to sort groups at the specified group level in a descending order (C, B, A).
* **No Sort**  
  Select to sort groups at the specified group level in their original order in database.
* **Special Group**  
  Select to open the [User Defined Group dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664591383-User-Defined-Group-Dialog-Box) to define grouping information.
* **Custom Sort**  
  Select to open the [Custom Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664443927-Custom-Sort-Dialog-Box) to set how to sort the groups at the specified group level.

**Special Function**

This column shows the [special functions](https://devnet.logianalytics.com/hc/en-us/articles/4405664404503-Grouping-the-Data-in-Tables#Function) that you select for the group-by fields of the Numeric, String, Date, and Time data types. Select a special function from the drop-down list to specify to which level to group the data of the specified field, or select Customize to set the function in the [Customized Function dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664448023-Customized-Function-Dialog-Box).

**Custom Sort**

Designer enables this button after you have selected Custom Sort from the Sort column to define the sort manner of groups for the specified group level. Select it to specify how to sort the groups.

**Special Group**

Designer enables this button after you have selected Special Group from the Sort column to define a special group. Select it to specify how to group your information.

**Select N**

Select to open the [Select N dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661712151-Select-N-Dialog-Box) to specify the Select N condition for the specified group level.

**Group Filter**

Select to open the [Group Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664515735-Group-Filter-Dialog-Box) to specify the group filter condition.

### Summary Screen

Use this screen to specify the fields on which to create summaries in the table.

![Create Table - Summary](https://devnet.logianalytics.com/hc/article_attachments/4420410811799/crttbl_sum.gif)

**Resources**

This box lists the data fields in and related to the specified query resource, which you can use to create summaries in the table.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420410583703/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box based on which to create a summary in the table.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420394644119/btn_rmvarrow.gif)**Remove button**

Select to remove the specified summary from the table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420410588439/btn_mvup.gif)**Move Up button**

Select to move the specified summary higher in the display order.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420410588695/btn_mvdwn.gif)**Move Down button**

Select to move the specified summary lower in the display order.

**Summarized Fields**

This column shows the fields that you add to create summaries in the table.

**Aggregate Function**

This column shows the [aggregate functions](https://devnet.logianalytics.com/hc/en-us/articles/4405661767063-Working-with-Summaries#Function) that you select to use for the summaries.

**Distinct On**

Designer enables this option and you should set it when you select DistinctSum as the aggregate function. Select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420402297111/btn_ellipsis2.gif) to select the fields according to whose unique values to calculate DistinctSum in the [Select Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664572951-Select-Fields-Dialog-Box).

**Break Field**

This column shows the groups on which to calculate the summaries. If you add a summary for the Table level, the break field is null and Designer calculates the summary based on the whole dataset.

**Position**

You can use this option together with the Column option to specify the location where to place a summary.

* **Footer**  
  Select to place the summary in the footer panel. When you add the summary for a specific group, Designer places it in the group's footer panel; if you add the summary for the Table level, Designer places it in the table footer panel.
* **Header**  
  Select to place the summary in the header panel. When you add the summary for a specific group, Designer places it in the group's header panel; if you add the summary for the Table level, Designer places it in the table header panel. Designer disables this option when the table type is Group Above.

**Column**

You can use this option together with the Position option to specify the location where to place a summary.

* **Detail**  
  Select to place the summary and its name label in the first two detail columns.
* **Summary**  
  Select to place the summary in a separate summary column. Designer disables this option when the table type is Group Above.

### Filter Screen

Use this screen to narrow down the data to display in the table.

Designer displays the same options in the Filter screen as in the [Edit Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661510295-Edit-Filter-Dialog-Box).

![Create Table - Filter](https://devnet.logianalytics.com/hc/article_attachments/4420410813079/crttbl_fltr.gif)

### Style Screen

Use this screen to specify the style of the table.

![Create Table - Style](https://devnet.logianalytics.com/hc/article_attachments/4420402503191/crttbl_sty.gif)

**Grow Report**

This box lists the layouts in which you can create the table.

* **Vertically**  
  Select to create a vertical table.
* **Horizontally**  
  Select to create a horizontal table.

**Style**

This box lists the styles that you can apply to the table. Select the style for the table.

**Preview**

This box displays a diagram illustrating the effect of the selected style on the table.

**Inherit Style**

Designer displays this option and selects it by default when you have specified to insert the table into a banded object. Clear it if you do not want the table to inherit the style of its parent.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664440983-Create-Query-s-Username-and-Password-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661478039-Crosstab-Formula-Editor-Dialog-Box)
