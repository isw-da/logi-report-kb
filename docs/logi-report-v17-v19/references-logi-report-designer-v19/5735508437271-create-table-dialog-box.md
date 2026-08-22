---
title: "Create Table Dialog Box"
id: 5735508437271
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735508437271-Create-Table-Dialog-Box
updated_at: 2022-11-02T08:16:39Z
---

# Create Table Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735522220695-Create-Query-s-Username-and-Password-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735522106391-Crosstab-Formula-Editor-Dialog-Box)

# Create Table Dialog Box

You can use the Create Table dialog box to [create a table](https://devnet.logianalytics.com/hc/en-us/articles/5735521199255-Inserting-Tables-in-a-Report) in a report. This topic describes the options in the dialog box.

Designer displays the Create Table dialog box when you choose a table type and select OK in the [Table Type dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735525106967-Table-Type-Dialog-Box), or drag a table type icon from the Components panel into a report, and provides you with different options in the dialog box according to the type of the data resource you use for the table: [business view](#BV) or [query resource](#Query).

## Create Table Dialog Box - Business View Based

When you use the Create Table dialog box to create tables using business views in web reports/library components, Designer displays different screens in the dialog box according to the type of the table: group table or summary table; there is no such difference when you use the dialog box for creating tables in page reports.

### For Table in Page Report and Group Table in Web Report/Library Component

When you use the Create Table dialog box for creating a table in a page report or creating a group table in a web report/library component using a business view, Designer displays the following screens in the dialog box:

* [Data Screen](#BVData)
* [Display Screen](#BVDisplay)
* [Group Screen](#BVGroup)
* [Summary Screen](#BVSummary)
* [Dataset Filter Screen](#BVFilter)
* [Style Screen](#BVStyle)

Designer displays these buttons in all the screens:

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

Use this screen to specify the dataset for the table.

![Create Table - Data](https://devnet.logianalytics.com/hc/article_attachments/9898515688855/crttbl_dt_bv1.gif)

**Business view box**

This box lists the predefined business views in the current catalog. Select one and Designer automatically creates a dataset based on it for the table.

* ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")**<New Business View...>**  
  Select to create a business view in the catalog using the [Business View Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552449687-Query-Editor-Dialog-Box). Designer does not display this option when you use the dialog box in a library component.

![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")**More Options**/**Less Options**

Select to show or hide the options for specifying the dataset you want to use. Designer does not display this pair of buttons when you use the dialog box in a library component.

* **New Dataset**  
  Select to create a dataset based on a business view in the current catalog.
* **Existing Dataset**  
  Select to use a dataset from the ones that you have created in the current report.
  + **<New Dataset...>**  
    Select to create a dataset in the [New Dataset dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735566804375-New-Dataset-Dialog-Box).

* **Current Dataset**  
  Designer enables this option when the parent object where you have specified to insert the table already applies a dataset. Select it if you want the table to inherit the dataset from its parent.

![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")**Edit**

Select to edit the specified business view in the [Business View Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552449687-Query-Editor-Dialog-Box) or dataset in the [Dataset Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735529002007-Dataset-Editor-Dialog-Box). Designer does not display this button when you use the dialog box in a library component.

#### Display Screen

Use this screen to specify the detail fields you want to display in the table.

![Create Table - Display](https://devnet.logianalytics.com/hc/article_attachments/9898515699607/crttbl_dsply_bv.gif)

**Title**

Specify the title of the table.

**Resources**

This box lists the available data fields that you can use as detail fields in the table.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box to the table.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/9898422552599/btn_rmvarrow.gif)**Remove button**

Select to remove the specified field from the table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif)**Move Up button**

Select to move the specified field higher in the display order.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif)**Move Down button**

Select to move the specified field lower in the display order.

**Display Fields**

This column shows the detail fields that you add to display in the table.

**Display Name**

This column shows the labels of the detail fields in the table, which by default are the display names of the added fields. You can select in the text boxes to edit the labels, or select the **Auto Map Field Name** checkboxes in the text boxes to apply the display names of the fields and map the labels to the dynamic display names of the fields at runtime if the Server administrator defines them.

**Sort Fields By**

Select to open the [Sort Fields By dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735567421591-Sort-Fields-By-Dialog-Box) to specify how to sort the detail data in the table.

#### Group Screen

Use this screen to specify the criteria for grouping data in the table.

![Create Table - Group](https://devnet.logianalytics.com/hc/article_attachments/9898515705367/crttbl_grp_bv.gif)

**Resources**

This box lists the available data fields that you can use as group-by fields in the table.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box as a group-by field in the table.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/9898422552599/btn_rmvarrow.gif)**Remove button**

Select to remove the specified group-by field from the table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif)**Move Up button**

Select to move the specified group to a higher group level.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif)**Move Down button**

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
  Select to open the [Custom Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565346071-Custom-Sort-Dialog-Box) to set how to sort the groups at the specified group level.

**Select N**

Select to open the [Select N dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735567350807-Select-N-Dialog-Box) to specify the Select N condition for the specified group level.

#### Summary Screen

Use this screen to specify the summaries to calculate data in the table.

![Create Table - Summary](https://devnet.logianalytics.com/hc/article_attachments/9898515717655/crttbl_sum_bv1.gif)

**Resources**

This box lists the available data fields that you can use to calculate data in the table.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box to calculate data in the table.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/9898422552599/btn_rmvarrow.gif)**Remove button**

Select to remove the specified summary from the table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif)**Move Up button**

Select to move the specified summary higher in the display order.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif)**Move Down button**

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

#### Dataset Filter Screen

Use this screen to filter the dataset the table applies.

Designer displays the same options in the Dataset Filter screen as those in the [Edit Dataset Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522534039-Edit-Dataset-Filter-Dialog-Box).

![Create Table - Filter](https://devnet.logianalytics.com/hc/article_attachments/9898465079191/crttbl_fltr_bv1.gif)

#### Style Screen

Use this screen to specify the style of the table.

![Create Table - Style](https://devnet.logianalytics.com/hc/article_attachments/9898465084183/crttbl_sty_bv1.gif)

**Grow Report**

This box lists the layouts in which you can create the table.

* **Vertically**  
  Select to create a vertical table.
* **Horizontally**  
  Select to create a horizontal table. Designer displays this option when you are creating the table in a page report.

**Style**

This box lists the styles you can apply. Select the style for the table.

**Preview**

This box displays a diagram illustrating the effect of the selected style on the table.

**Inherit Style**

Designer displays this option and selects it by default when you have specified to insert the table into a banded object. Clear it if you do not want the table to inherit the style of its parent.

### For Summary Table in Web Report/Library component

When you use the Create Table dialog box for creating a summary table in a web report/library component using a business view, Designer displays the following screens in the dialog box:

* [Data Screen](#Data1)
* [Columns Screen](#Columns)
* [Summary Screen](#Summary1)
* [Dataset Filter Screen](#Filter1)
* [Style Screen](#Style1)

Designer displays these buttons in all the screens:

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

Use this screen to specify the dataset for the table.

![Create Summary Table - Data](https://devnet.logianalytics.com/hc/article_attachments/9898465091351/crttbl_dt_bv2.gif)

**Business view box**

This box lists the predefined business views in the current catalog. Select one and Designer automatically creates a dataset based on it for the table.

* ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")**<New Business View...>**  
  Select to create a business view in the catalog using the [Business View Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552449687-Query-Editor-Dialog-Box). Designer does not display this option when you use the dialog box in a library component.

![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")**More Options**/**Less Options**

Select to show or hide the options for specifying the dataset you want to use. Designer does not display this pair of buttons when you use the dialog box in a library component.

* **New Dataset**  
  Select to create a dataset based on a business view in the current catalog.
* **Existing Dataset**  
  Select to use a dataset from the ones that you have created in the current report.
  + **<New Dataset...>**  
    Select to create a dataset in the [New Dataset dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735566804375-New-Dataset-Dialog-Box).

* **Current Dataset**  
  Designer enables this option when the parent object where you have specified to insert the table already applies a dataset. Select it if you want the table to inherit the dataset from its parent.

![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")**Edit**

Select to edit the specified business view in the [Business View Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552449687-Query-Editor-Dialog-Box) or dataset in the [Dataset Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735529002007-Dataset-Editor-Dialog-Box). Designer does not display this button when you use the dialog box in a library component.

#### Columns Screen

Use this screen to specify the fields to create columns in the table.

![Create Summary Table - Columns](https://devnet.logianalytics.com/hc/article_attachments/9898465095831/crttbl_clmn.gif)

**Resources**

This box lists the available data fields that you can use to create columns in the table. You can create detail columns from detail objects, group columns from group objects, and summary columns from aggregation objects.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box to create a column in the table.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/9898422552599/btn_rmvarrow.gif)**Remove button**

Select to remove the specified field from the table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif)**Move Up button**

Select to move the specified field higher in the display order.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif)**Move Down button**

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
  Select to open the [Custom Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565346071-Custom-Sort-Dialog-Box) to set how to sort the groups at the specified group level.

**Select N**

Select to open the [Select N dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735567350807-Select-N-Dialog-Box) to specify the Select N condition for the specified group level.

#### Summary Screen

Use this screen to insert summaries to the header/footer panels of the table and groups.

![Create Summary Table - Summary](https://devnet.logianalytics.com/hc/article_attachments/9898465100695/crttbl_sum_bv2.gif)

**Resources**

This box lists the aggregation objects that you add to create summary columns in the table in the Columns screen.

**Summarized Fields**

This column shows the group objects that you add to create group columns in the table in the Columns screen.

**Header**

The checkboxes represent the table header and the group headers of the added groups. After selecting an aggregation object in the Resources box, you can select the checkboxes to insert it in the corresponding header panels.

**Footer**

The checkboxes represent the table footer and the group footers of the added groups. After select an aggregation object in the Resources box, you can select the checkboxes to insert it in the corresponding footer panels.

#### Dataset Filter Screen

Use this screen to filter the dataset the table applies.

Designer displays the same options in the Dataset Filter screen as those in the [Edit Dataset Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522534039-Edit-Dataset-Filter-Dialog-Box).

![Create Summary Table - Filter](https://devnet.logianalytics.com/hc/article_attachments/9898465105815/crttbl_fltr_bv2.gif)

#### Style Screen

Use this screen to specify the style of the table.

![Create Summary Table - Style](https://devnet.logianalytics.com/hc/article_attachments/9898515810839/crttbl_sty_bv2.gif)

**Grow Report**

This box displays in which layout to create the table, which can only be Vertically.

**Style**

This box lists the styles you can apply. Select the style for the table.

**Preview**

This box displays a diagram illustrating the effect of the selected style on the table.

**Inherit Style**

Designer displays this option and selects it by default when you have specified to insert the table into a banded object. Clear it if you do not want the table to inherit the style of its parent.

## Create Table Dialog Box - Query Based

When you use the Create Table dialog box for creating a table using a query resource, Designer displays the following screens in the dialog box:

* [Data Screen](#Data)
* [Display Screen](#Display)
* [Group Screen](#Group)
* [Summary Screen](#Summary)
* [Filter Screen](#Filter)
* [Style Screen](#Style)

Designer displays these buttons in all the screens:

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

![Create Table - Data](https://devnet.logianalytics.com/hc/article_attachments/9898515843735/crttbl_dt.gif)

**Data resource box**

This box lists the predefined data resources in the current catalog. Select one and Designer automatically creates a dataset based on it for the table.

* **<New XXX...>**/**<Add XXX...>**  
  Select to create or add a data resource of the same type in the catalog.

**More Options**/**Less Options**

Select to show or hide the options for specifying the dataset you want to use.

* **New Dataset**  
  Select to create a dataset based on a data resource in the current catalog.
* **Existing Dataset**  
  Select to use a dataset from the ones that you have created in the current report.
  + **<New Dataset...>**  
    Select to create a dataset using the [New Dataset dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735566804375-New-Dataset-Dialog-Box).

* **Current Dataset**  
  Designer enables this option when the parent object where you have specified to insert the table already applies a dataset. Select it if you want the table to inherit the dataset from its parent.

**Edit**

Select to edit the specified query in the [Query Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552449687-Query-Editor-Dialog-Box) or dataset in the [Dataset Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735529002007-Dataset-Editor-Dialog-Box).

### Display Screen

Use this screen to specify the detail fields you want to display in the table.

![Create Table - Display](https://devnet.logianalytics.com/hc/article_attachments/9898515850647/crttbl_dsply.gif)

**Resources**

This box lists the available data fields that you can use as detail fields in the table.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box to the table.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/9898422552599/btn_rmvarrow.gif)**Remove button**

Select to remove the specified field from the table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif)**Move Up button**

Select to move the specified field higher in the display order.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif)**Move Down button**

Select to move the specified field lower in the display order.

**Display Fields**

This column shows the detail fields that you add to display in the table.

**Display Name**

This column shows the labels of the detail fields in the table, which by default are the display names of the added fields. You can select in the text boxes to edit the labels.

**Sort Fields By**

Select to open the [Sort Fields By dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735567421591-Sort-Fields-By-Dialog-Box) to specify how to sort the detail data in the table.

### Group Screen

Use this screen to specify the criteria for grouping data in the table.

![Create Table - Group](https://devnet.logianalytics.com/hc/article_attachments/9898515868823/crttbl_grp.gif)

**Resources**

This box lists the available data fields that you can use as group-by fields in the table.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box as a group-by field in the table.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/9898422552599/btn_rmvarrow.gif)**Remove button**

Select to remove the specified group-by field from the table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif)**Move Up button**

Select to move the specified group to a higher group level.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif)**Move Down button**

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
  Select to open the [User Defined Group dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735544779031-User-Defined-Group-Dialog-Box) to define grouping information.
* **Custom Sort**  
  Select to open the [Custom Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565346071-Custom-Sort-Dialog-Box) to set how to sort the groups at the specified group level.

**Special Function**

This column shows the [special functions](https://devnet.logianalytics.com/hc/en-us/articles/5735527697943-Grouping-Data-in-Tables#Function) that you select for the group-by fields of the Numeric, String, Date, and Time data types. Select a special function from the drop-down list to specify to which level to group the data of the specified field, or select Customize to set the function in the [Customized Function dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522295831-Customized-Function-Dialog-Box).

**Custom Sort**

Designer enables this button after you have selected Custom Sort from the Sort column to define the sort manner of groups for the specified group level. Select it to specify how to sort the groups.

**Special Group**

Designer enables this button after you have selected Special Group from the Sort column to define a special group. Select it to specify how to group your information.

**Select N**

Select to open the [Select N dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735567350807-Select-N-Dialog-Box) to specify the Select N condition for the specified group level.

**Group Filter**

Select to open the [Group Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735530070167-Group-Filter-Dialog-Box) to specify the group filter condition.

### Summary Screen

Use this screen to specify the fields on which to create summaries in the table.

![Create Table - Summary](https://devnet.logianalytics.com/hc/article_attachments/9898532287255/crttbl_sum.gif)

**Resources**

This box lists the available data fields that you can use to create summaries in the table.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box based on which to create a summary in the table.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/9898422552599/btn_rmvarrow.gif)**Remove button**

Select to remove the specified summary from the table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif)**Move Up button**

Select to move the specified summary higher in the display order.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif)**Move Down button**

Select to move the specified summary lower in the display order.

**Summarized Fields**

This column shows the fields that you add to create summaries in the table.

**Aggregate Function**

This column shows the [aggregate functions](https://devnet.logianalytics.com/hc/en-us/articles/5735532118039-Working-with-Summaries#Function) that you select to use for the summaries.

**Distinct On**

Designer enables this option and you should set it when you select DistinctSum as the aggregate function. Select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898422868887/btn_ellipsis2.gif) to select the fields according to whose unique values to calculate DistinctSum in the [Select Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524767255-Select-Fields-Dialog-Box).

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

Designer displays the same options in the Filter screen as those in the [Edit Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522539031-Edit-Filter-Dialog-Box).

![Create Table - Filter](https://devnet.logianalytics.com/hc/article_attachments/9898515890455/crttbl_fltr.gif)

### Style Screen

Use this screen to specify the style of the table.

![Create Table - Style](https://devnet.logianalytics.com/hc/article_attachments/9898515894423/crttbl_sty.gif)

**Grow Report**

This box lists the layouts in which you can create the table.

* **Vertically**  
  Select to create a vertical table.
* **Horizontally**  
  Select to create a horizontal table.

**Style**

This box lists the styles you can apply. Select the style for the table.

**Preview**

This box displays a diagram illustrating the effect of the selected style on the table.

**Inherit Style**

Designer displays this option and selects it by default when you have specified to insert the table into a banded object. Clear it if you do not want the table to inherit the style of its parent.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735522220695-Create-Query-s-Username-and-Password-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735522106391-Crosstab-Formula-Editor-Dialog-Box)
