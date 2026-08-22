---
title: "Create Table Dialog Box"
id: 1500010095941
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010095941-Create-Table-Dialog-Box
updated_at: 2022-03-28T09:19:18Z
---

# Create Table Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010095921-Create-Query-s-Username-and-Password-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010095821-Crosstab-Formula-Editor-Dialog-Box)

# Create Table Dialog Box

You can use the Create Table dialog box to [create a table](https://devnet.logianalytics.com/hc/en-us/articles/1500010057422-Inserting-Tables-in-a-Report) in a report. This topic describes the options in the dialog box.

Designer displays the Create Table dialog box when you choose a table type and select OK in the [Table Type dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010099021-Table-Type-Dialog-Box), or drag the desired table type icon from the Components panel into a report, and provides you with different options in the dialog box according to the type of the data resource used for the table: [business view](#BV) or [query resource](#Query).

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

Select to finish creating the table and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

#### Data Screen

Use this screen to specify the business view using which to create the table. You can select from all the predefined business views in the current catalog.

![Create Table - Data](https://devnet.logianalytics.com/hc/article_attachments/4404856986775/crttbl_dt_bv1.gif)

**Inherit from the Parent**

Designer displays the option only when you have specified to insert the table into any of the following panels in a banded object: banded header panel, banded footer panel, group header panel, or group footer panel. Select it if you want the table to inherit the business view that its parent banded object uses.

#### Display Screen

Use this screen to specify the detail fields to display in the table.

![Create Table - Display](https://devnet.logianalytics.com/hc/article_attachments/4404856987031/crttbl_dsply_bv.gif)

**Title**

Specify the title for the table.

**Resources**

The box lists the resources in and related to the specified business view, which you can use as detail fields in the table.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box to the table.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)**Remove button**

Select to remove the specified field from the table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**

Select to move the specified field higher in the display order.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**

Select to move the specified field lower in the display order.

**Display Fields**

The column shows the detail fields that you add to display in the table.

**Display Name**

The column shows the labels of the detail fields in the table , which by default are the display names of the added fields. You can select in the text boxes to edit the labels, or select the Auto Map Field Name checkboxes in the text boxes to automatically map the labels to the dynamic display names of the fields at runtime.

**Sort Fields By**

Select to the [Sort Fields By dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060542-Sort-Fields-By-Dialog-Box) to specify how to sort the detail data in the table.

#### Group Screen

Use this screen to specify the criteria for grouping data in the table.

![Create Table - Group](https://devnet.logianalytics.com/hc/article_attachments/4404848594327/crttbl_grp_bv.gif)

**Resources**

The box lists the resources in and related to the specified business view, which you can use as group-by fields in the table.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box as a group-by field in the table.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)**Remove button**

Select to remove the specified group-by field from the table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**

Select to move the specified group to a higher group level.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**

Select to move the specified group to a lower group level.

**Group By**

The column shows the group-by fields on which you select to group data in the table.

**Sort**

The column shows how you specify to sort groups at each group level. You can select from the following options:

* **Ascend**  
  Select to sort groups at the specified group level in an ascending order (A, B, C).
* **Descend**  
  Select to sort groups at the specified group level in a descending order (C, B, A).
* **No Sort**  
  Select to sort groups at the specified group level in their original order in database.
* **Custom Sort**  
  Select to open the [Custom Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095981-Custom-Sort-Dialog-Box) to set how to sort the groups at the specified group level.

**Select N**

Select to open the [Select N dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098701-Select-N-Dialog-Box) to specify the Select N condition for the specified group level.

#### Summary Screen

Use this screen to specify the summaries to calculate data in the table.

![Create Table - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404856987415/crttbl_sum_bv1.gif)

**Resources**

The box lists the resources in and related to the specified business view, which you can use to calculate data in the table.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box to calculate data in the table.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)**Remove button**

Select to remove the specified summary from the table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**

Select to move the specified summary higher in the display order.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**

Select to move the specified summary lower in the display order.

**Summarized Fields**

The column shows the fields that you add to calculate data in the table.

**Position**

You can use the option together with the Column option to specify the location where to place a summary.

* **Footer**  
  Select it to place the summary in the footer panel. If you add the summary for a specific group, Designer places it in the group's footer panel; if you add the summary for the Table level, Designer places it in the table footer panel.
* **Header**  
  Select it to place the summary in the header panel. If you add the summary for a specific group, Designer places it in the group's header panel; if you add the summary for the Table level, Designer places it in the table header panel. Designer disables the option when the table type is Group above.

**Column**

You can use the option together with the Position option to specify the location where to place a summary.

* **Detail**  
  Select it to place the summary and its name label in the first two detail columns.
* **Summary**  
  Select it to place the summary in a separate summary column. Designer disables the option when the table type is Group above.

#### Filter Screen

Use this screen to narrow down the data to display in the table.

Designer displays the same options in the Filter screen as in the [Edit Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058722-Edit-Filter-Dialog-Box).

![Create Table - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404856987671/crttbl_fltr_bv1.gif)

#### Style Screen

Use this screen to specify the style of the table.

![Create Table - Style](https://devnet.logianalytics.com/hc/article_attachments/4404848594839/crttbl_sty_bv1.gif)

**Grow Report**

The box displays in which layout to create the table, which can only be Vertically.

**Style**

The box lists the styles that you can apply to the table. Select the style for the table.

**Preview**

The box displays a diagram illustrating the effect of the selected style on the table.

**Inherit Style**

Designer displays the option and selects it by default if you have specified to insert the table into a banded object. Clear it if you do not want the table to inherit the style of its parent.

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

Select to finish creating the table and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

#### Data Screen

Use this screen to specify the business view using which to create the table. You can select from all the predefined business views in the current catalog.

![Create Summary Table - Data](https://devnet.logianalytics.com/hc/article_attachments/4404856987927/crttbl_dt_bv2.gif)

**Inherit from the Parent**

Designer displays the option only when you have specified to insert the table into any of the following panels in a banded object: banded header panel, banded footer panel, group header panel, or group footer panel. Select it if you want the table to inherit the business view that its parent banded object uses.

#### Columns Screen

Use this screen to specify the fields to create the columns in the table.

![Create Summary Table - Columns](https://devnet.logianalytics.com/hc/article_attachments/4404856988183/crttbl_clmn.gif)

**Resources**

The box lists the resources in and related to the specified business view, which you can use to create columns in the table. You can create detail columns from detail objects, group columns from group objects, and summary columns from aggregation objects.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box to create a column in the table.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)**Remove button**

Select to remove the specified field from the table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**

Select to move the specified field higher in the display order.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**

Select to move the specified field lower in the display order.

**Column**

The column shows the fields that you add to create columns in the table.

**Sort**

Designer enables this option for group columns. You can specify how you want to sort groups at each group level. You can select from the following options:

* **Ascend**  
  Select to sort groups at the specified group level in an ascending order (A, B, C).
* **Descend**  
  Select to sort groups at the specified group level in a descending order (C, B, A).
* **No Sort**  
  Select to sort groups at the specified group level in their original order in database.
* **Custom Sort**  
  Select to open the [Custom Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095981-Custom-Sort-Dialog-Box) to set how to sort the groups at the specified group level.

**Select N**

Select to open the [Select N dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098701-Select-N-Dialog-Box) to specify the Select N condition for the specified group level.

#### Summary Screen

Use this screen to insert summaries to the header/footer panels of the table and groups.

![Create Summary Table - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404856988439/crttbl_sum_bv2.gif)

**Resources**

The box lists the aggregation objects that you add to create summary columns in the table in the Columns screen.

**Summarized Fields**

The column shows the group objects that you add to create group columns in the table in the Columns screen.

**Header**

The checkboxes represent the table header and the group headers of the added groups. After selecting an aggregation object in the Resources box, you can select the checkboxes to insert it in the corresponding header panels.

**Footer**

The checkboxes represent the table footer and the group footers of the added groups. After select an aggregation object in the Resources box, you can select the checkboxes to insert it in the corresponding footer panels.

#### Filter Screen

Use this screen to narrow down the data to display in the table.

Designer displays the same options in the Filter screen as in the [Edit Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058722-Edit-Filter-Dialog-Box).

![Create Summary Table - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404856988951/crttbl_fltr_bv2.gif)

#### Style

Use this screen to specify the style of the table.

![Create Summary Table - Style](https://devnet.logianalytics.com/hc/article_attachments/4404848595095/crttbl_sty_bv2.gif)

**Grow Report**

The box displays in which layout to create the table, which can only be Vertically.

**Style**

The box lists the styles that you can apply to the table. Select the style for the table.

**Preview**

The box displays a diagram illustrating the effect of the selected style on the table.

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

Select to finish creating the table and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

### Data Screen

Use this screen to specify the dataset for the table.

![Create Table - Data](https://devnet.logianalytics.com/hc/article_attachments/4404848595351/crttbl_dt.gif)

**Data resource box**

The box lists the predefined data resources in the current catalog. Select one and Designer automatically creates a dataset based on it for the table.

**More Options**/**Less Options**

Select it to show or hide the options for specifying a dataset for the table.

* **New Dataset**  
  Select to create a dataset based on the current catalog data resources. When you select a query, Designer enables the Edit button at the bottom and you can select the button to edit the query in the [Query Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098321-Query-Editor-Dialog-Box).
* **Existing Dataset**  
  Select to use a dataset from the ones that you have created in the current page report. You can select the Edit button to edit the specified dataset in the [Dataset Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058622-Dataset-Editor-Dialog-Box), or select <New Dataset...> to create a dataset in the page report using the [New Dataset dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098001-New-Dataset-Dialog-Box).

* **Current Dataset**  
  Designer enables this option when the parent object where you have specified to insert the table already applies a dataset. Select it if you want the table to inherit the dataset from its parent.

### Display Screen

Use this screen to specify the detail fields to display in the table.

![Create Table - Display](https://devnet.logianalytics.com/hc/article_attachments/4404848595607/crttbl_dsply.gif)

**Resources**

The box lists the data fields in and related to the specified query resource, which you can use as detail fields in the table.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box to the table.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)**Remove button**

Select to remove the specified field from the table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**

Select to move the specified field higher in the display order.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**

Select to move the specified field lower in the display order.

**Display Fields**

The column shows the detail fields that you add to display in the table.

**Display Name**

The column shows the labels of the detail fields in the table, which by default are the display names of the added fields. You can select in the text boxes to edit the labels.

**Sort Fields By**

Select to open the [Sort Fields By dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060542-Sort-Fields-By-Dialog-Box) to specify how to sort the detail data in the table.

### Group Screen

Use this screen to specify the criteria for grouping data in the table.

![Create Table - Group](https://devnet.logianalytics.com/hc/article_attachments/4404848595863/crttbl_grp.gif)

**Resources**

The box lists the data fields in and related to the specified query resource, which you can use as group-by fields in the table.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box as a group-by field in the table.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)**Remove button**

Select to remove the specified group-by field from the table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**

Select to move the specified group to a higher group level.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**

Select to move the specified group to a lower group level.

**Group By**

The column shows the group-by fields on which you select to group data in the table.

**Sort**

The column shows how you want to sort groups at each group level. You can select from the following options:

* **Ascend**  
  Select to sort groups at the specified group level in an ascending order (A, B, C).
* **Descend**  
  Select to sort groups at the specified group level in a descending order (C, B, A).
* **No Sort**  
  Select to sort groups at the specified group level in their original order in database.
* **Special Group**  
  Select to open the [User Defined Group dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060782-User-Defined-Group-Dialog-Box) to define grouping information.
* **Custom Sort**  
  Select to open the [Custom Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095981-Custom-Sort-Dialog-Box) to set how to sort the groups at the specified group level.

**Special Function**

The column shows the [special functions](https://devnet.logianalytics.com/hc/en-us/articles/1500010094941-Grouping-the-Data-in-Tables#Function) that you select for the group-by fields of the Numeric, String, Date, and Time data types. Select a special function from the drop-down list to specify to which level to group the data of the specified field, or select Customize to set the function in the [Customized Function dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096021-Customized-Function-Dialog-Box).

**Custom Sort**

Designer enables the button after you have selected Custom Sort from the Sort column to define the sort manner of groups for the specified group level. Select it to specify how to sort the groups.

**Special Group**

Designer enables the button after you have selected Special Group from the Sort column to define a special group. Select it to specify how to group your information.

**Select N**

Select to open the [Select N dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098701-Select-N-Dialog-Box) to specify the Select N condition for the specified group level.

**Group Filter**

Select to open the [Group Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097461-Group-Filter-Dialog-Box) to specify the group filter condition.

### Summary Screen

Use this screen to specify the fields on which to create summaries in the table.

![Create Table - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404856989719/crttbl_sum.gif)

**Resources**

The box lists the data fields in and related to the specified query resource, which you can use to create summaries in the table.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box based on which to create a summary in the table.

![Rremove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)**Remove button**

Select to remove the specified summary from the table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**

Select to move the specified summary higher in the display order.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**

Select to move the specified summary lower in the display order.

**Summarized Fields**

The column shows the fields that you add to create summaries in the table.

**Aggregate Function**

The column shows the [aggregate functions](https://devnet.logianalytics.com/hc/en-us/articles/1500010061062-Working-with-Summaries#Function) that you select to use for the summaries.

**Distinct On**

Designer enables the option and you should set it when you select DistinctSum as the aggregate function. Select the ellipsis button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404848397591/btn_ellipsis.gif) to select the fields according to whose unique values to calculate DistinctSum in the [Select Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060462-Select-Fields-Dialog-Box).

**Break Field**

The column shows the groups on which to calculate the summaries. If you add a summary for the Table level, the break field is null and Designer calculates the summary based on the whole dataset.

**Position**

You can use the option together with the Column option to specify the location where to place a summary.

* **Footer**  
  Select it to place the summary in the footer panel. If you add the summary for a specific group, Designer places it in the group's footer panel; if you add the summary for the Table level, Designer places it in the table footer panel.
* **Header**  
  Select it to place the summary in the header panel. If you add the summary for a specific group, Designer places it in the group's header panel; if you add the summary for the Table level, Designer places it in the table header panel. Designer disables the option when the table type is Group Above.

**Column**

You can use the option together with the Position option to specify the location where to place a summary.

* **Detail**  
  Select it to place the summary and its name label in the first two detail columns.
* **Summary**  
  Select it to place the summary in a separate summary column. Designer disables the option when the table type is Group Above.

### Filter Screen

Use this screen to narrow down the data to display in the table.

Designer displays the same options in the Filter screen as in the [Edit Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058722-Edit-Filter-Dialog-Box).

![Create Table - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404848596119/crttbl_fltr.gif)

### Style Screen

Use this screen to specify the style of the table.

![Create Table - Style](https://devnet.logianalytics.com/hc/article_attachments/4404856989975/crttbl_sty.gif)

**Grow Report**

The box lists the layouts in which you can create the table.

* **Vertically**  
  Select to create a vertical table.
* **Horizontally**  
  Select to create a horizontal table.

**Style**

The box lists the styles that you can apply to the table. Select the style for the table.

**Preview**

The box displays a diagram illustrating the effect of the selected style on the table.

**Inherit Style**

Designer displays the option and selects it by default if you have specified to insert the table into a banded object. Clear it if you do not want the table to inherit the style of its parent.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010095921-Create-Query-s-Username-and-Password-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010095821-Crosstab-Formula-Editor-Dialog-Box)
