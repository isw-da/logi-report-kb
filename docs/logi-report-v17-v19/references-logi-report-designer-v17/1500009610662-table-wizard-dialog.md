---
title: "Table Wizard Dialog"
id: 1500009610662
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009610662-Table-Wizard-Dialog
updated_at: 2021-07-24T16:04:03Z
---

# Table Wizard Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009610642-Table-Type-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009633901-Tabular-Wizard-Dialog)

# Table Wizard Dialog

The Table Wizard helps you to [create a page report tab with a table in it](https://devnet.logianalytics.com/hc/en-us/articles/1500009613262-Creating-Reports#Page), [create a library component with a table in it](https://devnet.logianalytics.com/hc/en-us/articles/1500009613262-Creating-Reports#LC), or [edit an existing table](https://devnet.logianalytics.com/hc/en-us/articles/1500009629301-Modifying-Tables#Edit) in a report. It varies with the data resource type used by the table: [business view](#BV) or [query resource](#Query).

**Back**

Goes back to the previous screen.

**Next**

Goes to the next screen.

**Finish**

Finishes creating or editing the table and closes this wizard.

**Cancel**

Does not retain changes and closes this wizard.

**Help**

Displays the help document about this feature.

## Table Wizard - business view based

When the wizard is used in a web report/library component, the screens available in the wizard vary according to the table type: group table and summary table.

### For table in page report and group table in web report/library component

When the wizard is used for creating/editing a table in a page report or creating/editing a group table in a web report/library component using a business view, it consists of the following screens: [Data](#Data-bv), [Display](#Display-bv), [Group](#Group-bv), [Summary](#Summary-bv), [Filter](#Filter-bv) and [Style](#Style-bv).

#### Data

The screen lists all the predefined business views in the current catalog. Select the one you want to use for the table.

![Table Wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404904235415/tblwzd_dt_bv1.gif)

**Inherit from the Parent**

Specifies to inherit data from the business view used by the parent object. Available only when the table is in any of the following panels in a banded object in a web report: banded header panel, banded footer panel, group header panel and group footer panel.

#### Display

Specifies the detail fields to display in the table.

![Table Wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4404904235671/tblwzd_dsply_bv.gif)

**Title**

Specifies the title for the table.

**Resources**

Lists the resources in and related to the specified business view, which can be used as detail fields in the table.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif)**

Adds the selected field in the Resources box to the table.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)**

Removes the selected field from the table.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404904235927/btn_replace.gif)

Replaces the selected field in the table with the specified field in the Resources box. Available only when editing a table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif)

Moves the selected field one step up. Available only when creating a table.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif)

Moves the selected field one step down. Available only when creating a table.

**Show Table Group Structure**

Specifies whether to show the group structure of the table. Available only when editing a table.

**Display Fields**

Lists the detail fields of the table.

**Display Name**

Specifies the text of the labels of the detail columns, which by default are the display names of the added fields. You can select in the text boxes to edit the label text, or select the Auto Map Field Name checkboxes in the text boxes to automatically map the label text to the dynamic display names of the fields at runtime.

**Sort Fields By**

Opens the [Sort Fields By](https://devnet.logianalytics.com/hc/en-us/articles/1500009633661-Sort-Fields-By-Dialog) dialog to specify how to sort the detail data in the table.

#### Group

Specifies the criteria for grouping data in the table.

![Table Wizard - Group](https://devnet.logianalytics.com/hc/article_attachments/4404904236183/tblwzd_grp_bv.gif)

**Resources**

Lists the resources in and related to the specified business view, which can be used as group-by fields in the table.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif)

Adds the selected field in the Resources box as a group-by field in the table.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)

Removes the selected group-by field from the table.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404904235927/btn_replace.gif)

Replaces the selected group-by field in the table with the specified field in the Resources box. Available only when editing a table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif)

Moves the selected group one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif)

Moves the selected group one step down.

**Group By**

Lists the group-by fields of the table.

**Sort**

Specifies how groups at the specific group level will be sorted.

* **Ascend**  
   Groups will be sorted in an ascending order (A, B, C).
* **Descend**  
   Groups will be sorted in a descending order (C, B, A).
* **No Sort**  
   Groups will be sorted in the original order in database.
* **Custom Sort**  
   Opens the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009607602-Custom-Sort-Dialog) dialog to set how groups will be sorted.

**Select N**

Opens the [Select N](https://devnet.logianalytics.com/hc/en-us/articles/1500009610362-Select-N-Dialog) dialog to specify the Select N condition.

#### Summary

Specifies the summaries to calculate data in the table. This screen is available only when you create a table.

![Table Wizard - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404904236439/tblwzd_sum_bv1.gif)

**Resources**

Lists the resources in and related to the specified business view, which can be used to calculate data in the table.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif)**

Adds the selected field to calculate data in the table.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)**

Removes the selected summary from the table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif)

Moves the selected summary one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif)

Moves the selected summary one step down.

**Summarized Fields**

Lists the fields added to calculate data in the table.

**Position**

Works together with the Column option to specify the location where a summary will be put.

* **Footer**  
   Specifies to put the summary in the footer panel. A summary added for a group level is placed in the group's footer panel; if added for the Table level, it will be placed in the table footer panel.
* **Header**  
   Specifies to put the summary in the header panel. A summary added for a group level is placed in the group's header panel; if added for the Table level, it will be placed in the table header panel. Not available when the table type is Group Above.

**Column**

Works together with the Position option to specify the location where a summary will be put.

* **Detail**  
   The summaries and their name labels will be put in in the first two detail columns.
* **Summary**  
   The summary field will be displayed in a separate summary column. Not available when the table type is Group Above.

#### Filter

Specifies to filter data displayed in the table. This screen is available only when you create a table, and it contains the same options as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009607882-Edit-Filter-Dialog) dialog.

![Table Wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404904236695/tblwzd_fltr_bv1.gif)

#### Style

Specifies the style of the table.

![Table Wizard - Style](https://devnet.logianalytics.com/hc/article_attachments/4404904236951/tblwzd_sty_bv1.gif)

**Grow Report**

Specifies the layout of the table, which can only be Vertically. Available only when creating a table.

**Style**

Specifies the style of the table.

* **<Custom>**  
   There is no style information on it and it is only used to support reports built with previous versions which did not bind any style or the bound style cannot be found in the style list.

**Preview**

Displays the selected layout and style effects.

**Inherit Style**

Specifies whether to make the table take the style of its parent. This option is available only when you edit a table and the table is inserted into a banded object of a page report.

**Page Setup**

Opens the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009609582-Page-Setup-Dialog) dialog to specify the page settings. Available only when creating a table in a page report.

### For summary table in web report/library component

When the wizard is used for creating/editing a summary table in a web report/library component using a business view, it consists of the following screens: [Data](#Data1), [Columns](#Columns), [Summary](#Summary1), [Filter](#Filter1) and [Style](#Style1).

#### Data

The screen lists all the predefined business views in the current catalog. Select the one you want to use for the table.

![Summary Table Wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404904237207/tblwzd_dt_bv2.gif)

**Inherit from the Parent**

Specifies to inherit data from the business view used by the parent object. Available only when the table is in any of the following panels in a banded object in a web report: banded header panel, banded footer panel, group header panel and group footer panel.

#### Columns

Specifies the fields to create the columns of the table.

![Summary Table Wizard - Columns](https://devnet.logianalytics.com/hc/article_attachments/4404911677719/tblwzd_clmn.gif)

**Resources**

Lists the resources in and related to the specified business view, which can be used to create the columns in the table.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif)**

Adds the selected field in the Resources box to create a column in the table.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)**

Removes the selected field from the table.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404904235927/btn_replace.gif)

Replaces the selected field in the table with the specified field in the Resources box. Available only when editing a table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif)

Moves the selected field one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif)

Moves the selected field one step down.

**Column**

Lists the columns of the table.

**Sort**

For a group column you can specify how groups at the specific group level will be sorted.

* **Ascend**  
   Groups will be sorted in an ascending order (A, B, C).
* **Descend**  
   Groups will be sorted in a descending order (C, B, A).
* **No Sort**  
   Groups will be sorted in the original order in database.
* **Custom Sort**  
   Opens the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009607602-Custom-Sort-Dialog) dialog to set how groups will be sorted.

**Select N**

Opens the [Select N](https://devnet.logianalytics.com/hc/en-us/articles/1500009610362-Select-N-Dialog) dialog to specify the Select N condition for a group column.

#### Summary

Specifies to insert summaries to the header/footer panels of the table and groups.

![Summary Table Wizard - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404904237463/tblwzd_sum_bv2.gif)

**Resources**

Lists the aggregation objects that have been added to the table in the Columns screen.

**Summarized Fields**

Displays the group objects that have been added to the table in the Columns screen.

**Header**

Represents the table header or the group header of a specific group. After an object is selected in the Resources box, you can select the checkboxes in the column to insert it in the corresponding header panels.

**Footer**

Represents the table footer or the group footer of a specific group. After an object is selected in the Resources box, you can select the checkboxes in the column to insert it in the corresponding footer panels.

#### Filter

Specifies to filter data displayed in the table. This screen is available only when you create a table, and it contains the same options as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009607882-Edit-Filter-Dialog) dialog.

![Summary Table Wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404911677975/tblwzd_fltr_bv2.gif)

#### Style

Specifies the style of the table.

![Summary Table Wizard - Style](https://devnet.logianalytics.com/hc/article_attachments/4404911678231/tblwzd_sty_bv2.gif)

**Grow Report**

Specifies the layout of the table, which can only be Vertically. Available only when creating a table.

**Style**

Specifies the style of the table.

**Preview**

Displays the selected layout and style effects.

## Table Wizard - query based

When the wizard is used to create/edit a table using a query resource, it consists of the following screens: [Data](#Data), [Display](#Display), [Group](#Group), [Summary](#Summary), [Chart](#Chart), [Filter](#Filter) and [Style](#Style).

### Data

Specifies the dataset of the table.

![Table Wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404911678487/tblwzd_dt.gif)

**Data resource box**

Lists the predefined data resources in the current catalog. Select one and a dataset based on it is created automatically for the table.

**More Options**/**Less Options**

Shows or hides the dataset selection panel to choose a dataset for the table.

* **New Dataset**  
   Specifies to create a dataset from the current catalog data resources. When a query is selected, you can select the Edit button to edit the query in the [Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009609882-Query-Editor-Dialog).
* **Existing Dataset**  
   Specifies to use a dataset from the ones existing in the current page report. You can select the Edit button to edit the dataset in the [Dataset Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009607762-Dataset-Editor-Dialog).
* **Current Dataset**  
   Specifies to inherit the dataset used by the parent object.

## Display

Specifies the detail fields to display in the table.

![Table Wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4404904237719/tblwzd_dsply.gif)

**Resources**

Lists the data fields in and related to the specified query resource, which can be used as detail fields in the table.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif)**

Adds the selected field in the Resources box to the table.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)**

Removes the selected field from the table.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404904235927/btn_replace.gif)

Replaces the selected field in the table with the specified field in the Resources box. Available only when editing a table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif)

Moves the selected field one step up. Available only when creating a table.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif)

Moves the selected field one step down. Available only when creating a table.

**Show Table Group Structure**

Specifies whether to show the group structure of the table. Available only when editing a table.

**Display Fields**

Lists the detail fields of the table.

**Display Name**

Specifies the labels of the detail columns, which by default are the display names of the added fields. You can select in the text boxes to edit the labels.

**Sort Fields By**

Opens the [Sort Fields By](https://devnet.logianalytics.com/hc/en-us/articles/1500009633661-Sort-Fields-By-Dialog) dialog to specify how to sort the detail data in the table.

## Group

Specifies the criteria for grouping data in the table.

![Table Wizard - Group](https://devnet.logianalytics.com/hc/article_attachments/4404911678871/tblwzd_grp.gif)

**Resources**

Lists the data fields in and related to the specified query resource, which can be used as group-by fields in the table.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif)**

Adds the selected field in the Resources box as a group-by field in the table.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)**

Removes the selected group-by field from the table.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404904235927/btn_replace.gif)

Replaces the selected group-by field in the table with the specified field in the Resources box.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif)

Moves the selected group one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif)

Moves the selected group one step down.

**Group By**

Lists the group-by fields of the table.

**Sort**

Specifies how groups at the specific group level will be sorted.

* **Ascend**  
   Groups will be sorted in an ascending order (A, B, C).
* **Descend**  
   Groups will be sorted in a descending order (C, B, A).
* **No Sort**  
   Groups will be sorted in the original order in database.
* **Special Group**  
   Opens the [User Defined Group](https://devnet.logianalytics.com/hc/en-us/articles/1500009610722-User-Defined-Group-Dialog) dialog to define grouping information.
* **Custom Sort**  
   Opens the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009607602-Custom-Sort-Dialog) dialog to set how groups will be sorted.

**Special Function**

For a group-by field of the Numeric/String/Date/Time type, you can select a [special function](https://devnet.logianalytics.com/hc/en-us/articles/1500009606502-Grouping-the-Data-in-Tables#Function) for it to specify to which level data will be grouped by. Select Customize to set the function in the [Customized Function](https://devnet.logianalytics.com/hc/en-us/articles/1500009630341-Customized-Function-Dialog) dialog.

**Custom Sort**

Specifies how to sort the groups. Activated only when you have selected Custom Sort from the Sort column to define the sorting manner of groups for the selected group level.

**Special Group**

Specifies how to group your information. Activated only when you have selected Special Group from the Sort column to define a special group.

**Select N**

Opens the [Select N](https://devnet.logianalytics.com/hc/en-us/articles/1500009610362-Select-N-Dialog) dialog to specify the Select N condition.

**Group Filter**

Opens the [Group Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009631861-Group-Filter-Dialog) dialog to specify the group filter condition.

## Summary

Specifies the fields on which to create aggregate functions. This screen is available only when you create a table.

![Table Wizard - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404911679127/tblwzd_sum.gif)

**Resources**

Lists the data fields in and related to the specified query resource, which can be used to create summaries in the table.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif)**

Adds the selected field in the Resources box based on which to create a summary in the table.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)**

Removes the selected summary from the table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif)

Moves the selected summary field one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif)

Moves the selected summary field one step down.

**Summarized Fields**

Lists the fields that have been added to create summaries in the table.

**Aggregate Function**

Specifies the [aggregate functions](https://devnet.logianalytics.com/hc/en-us/articles/1500009611182-Summaries#Function) used for the summaries.

**Distinct On**

Available and should be set when DistinctSum is selected as the aggregate function. It specifies the fields according to whose unique values to calculate DistinctSum. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904178967/btn_chsr.gif) in the text box to select the required fields in the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009633521-Select-Fields-Dialog) dialog.

**Break Field**

Displays the groups on which the summaries will be calculated. If a summary is added for the Table level, the break field is null and the summary will be calculated on the whole dataset.

**Position**

Works together with the Column option to specify the location where the summary field will be put. Not available when the table type is Group Above.

* **Header**  
   Specifies to put the summary field in the header panel. A summary added for a group level is placed in the group's header panel; if added for the Table level, it will be placed in the table header panel. Not available when the table type is Group Above.
* **Footer**  
   Specifies to put the summary field in the footer panel. A summary added for a group level is placed in the group's footer panel; if added for the Table level, it will be placed in the table footer panel.

**Column**

Works together with the Position option to specify the location where the summary will be placed.

* **Detail**  
   The summary field with its label will be put in in the first two detail columns.
* **Summary**  
   The summary field will be displayed in a separate summary column. Not available when the table type is Group Above.

## Chart

Specifies to create a chart together with the table, which will be placed above the table in the report body. This screen is available only when you create a table, and when there is at least one group and one summary added for this group in the table.

![Table Wizard - Chart](https://devnet.logianalytics.com/hc/article_attachments/4404904237975/tblwzd_cht.gif)

**No Chart**

Specifies not to create a chart.

**Bar Chart**

Specifies to create a Clustered Bar 2-D chart together with the table.

**Line Chart**

Specifies to create a Line 2-D chart together with the table.

**Pie Chart**

Specifies to create a Clustered Pie chart together with the table.

**Category**

Lists the group-by fields of the table on which summaries are added. Choose the field you want to display on the category (X) axis of the chart from the drop-down list.

**Series**

Lists the fields that have been added as the group-by fields of the table. Choose the field you want to display on the series (Z) axis of the chart from the drop-down list.

**Show Values**

Lists the summaries which are calculated based on the field you choose to display on the category axis of the chart. Choose the value you want to display in the chart from the drop-down list.

## Filter

Specifies to filter data displayed in the table. This screen is available only when you create a table, and it contains the same options as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009607882-Edit-Filter-Dialog) dialog.

![Table Wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404911679383/tblwzd_fltr.gif)

## Style

Specifies the style of the table.

![Table Wizard - Style](https://devnet.logianalytics.com/hc/article_attachments/4404904238231/tblwzd_sty.gif)

**Grow Report**

Specifies the layout of the table. Available only when creating a table.

* **Vertically**  
   Creates a vertical table.
* **Horizontally**  
   Creates a horizontal table.

**Style**

Specifies the style of the table.

* **<Custom>**  
   There is no style information on it and it is only used to support reports built with previous versions which did not bind any style or the bound style cannot be found in the style list.

**Preview**

Displays the selected layout and style effects.

**Inherit Style**

Specifies whether to make the table take the style of its parent. This option is available only when you edit a table and the table is inserted into a banded object.

**Page Setup**

Opens the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009609582-Page-Setup-Dialog) dialog to specify the page settings. Available only when creating a table.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009610642-Table-Type-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009633901-Tabular-Wizard-Dialog)
