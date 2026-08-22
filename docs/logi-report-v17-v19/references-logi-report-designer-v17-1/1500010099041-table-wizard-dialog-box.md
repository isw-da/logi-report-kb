---
title: "Table Wizard Dialog Box"
id: 1500010099041
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010099041-Table-Wizard-Dialog-Box
updated_at: 2021-07-23T19:16:05Z
---

# Table Wizard Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099021-Table-Type-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010060742-Tabular-Wizard-Dialog-Box)

# Table Wizard Dialog Box

The Table Wizard dialog box helps you to [create a page report tab with a table in it](https://devnet.logianalytics.com/hc/en-us/articles/1500010101181-Creating-Reports#Page), [create a library component with a table in it](https://devnet.logianalytics.com/hc/en-us/articles/1500010101181-Creating-Reports#LC), or [edit an existing table](https://devnet.logianalytics.com/hc/en-us/articles/1500010057442-Modifying-Tables#Edit) in a report. It varies with the data resource type used by the table: [business view](#BV) or [query resource](#Query).

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

## Table Wizard - Business View Based

When the wizard is used in a web report/library component, the screens available in the wizard vary according to the table type: group table and summary table.

### For Table in Page Report and Group Table in Web Report/Library Component

When the wizard is used for creating/editing a table in a page report or creating/editing a group table in a web report/library component using a business view, it consists of the following screens: [Data](#Data-bv), [Display](#Display-bv), [Group](#Group-bv), [Summary](#Summary-bv), [Filter](#Filter-bv) and [Style](#Style-bv).

#### Data

The screen lists all the predefined business views in the current catalog. Select the one you want to use for the table.

![Table Wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404848486807/tblwzd_dt_bv1.gif)

**Inherit from the Parent**

Specifies to inherit data from the business view used by the parent object. Available only when the table is in any of the following panels in a banded object in a web report: banded header panel, banded footer panel, group header panel and group footer panel.

#### Display

Specifies the detail fields to display in the table.

![Table Wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4404848487063/tblwzd_dsply_bv.gif)

**Title**

Specifies the title for the table.

**Resources**

Lists the resources in and related to the specified business view, which can be used as detail fields in the table.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**

Adds the selected field in the Resources box to the table.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)

Removes the selected field from the table.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404856888855/btn_replace.gif)

Replaces the selected field in the table with the specified field in the Resources box. Available only when editing a table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)

Moves the selected field higher in the display order. Available only when creating a table.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)

Moves the selected field lower in the display order. Available only when creating a table.

**Show Table Group Structure**

Specifies whether to show the group structure of the table. Available only when editing a table.

**Display Fields**

Lists the detail fields of the table.

**Display Name**

Specifies the text of the labels of the detail columns, which by default are the display names of the added fields. You can select in the text boxes to edit the label text, or select the Auto Map Field Name checkboxes in the text boxes to automatically map the labels to the dynamic display names of the fields at runtime.

**Sort Fields By**

Opens the [Sort Fields By dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060542-Sort-Fields-By-Dialog-Box) to specify how to sort the detail data in the table.

#### Group

Specifies the criteria for grouping data in the table.

![Table Wizard - Group](https://devnet.logianalytics.com/hc/article_attachments/4404856889111/tblwzd_grp_bv.gif)

**Resources**

Lists the resources in and related to the specified business view, which can be used as group-by fields in the table.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)

Adds the selected field in the Resources box as a group-by field in the table.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)

Removes the selected group-by field from the table.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404856888855/btn_replace.gif)

Replaces the selected group-by field in the table with the specified field in the Resources box. Available only when editing a table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**

Select to move the specified group to a higher group level.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**

Select to move the specified group to a lower group level.

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
   Opens the [Custom Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095981-Custom-Sort-Dialog-Box) to set how groups will be sorted.

**Select N**

Opens the [Select N dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098701-Select-N-Dialog-Box) to specify the Select N condition.

#### Summary

Specifies the summaries to calculate data in the table. This screen is available only when you create a table.

![Table Wizard - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404848487831/tblwzd_sum_bv1.gif)

**Resources**

Lists the resources in and related to the specified business view, which can be used to calculate data in the table.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**

Adds the selected field to calculate data in the table.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)

Removes the selected summary from the table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**

Select to move the specified summary higher in the display order.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**

Select to move the specified summary lower in the display order.

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

Specifies to filter data displayed in the table. This screen is available only when you create a table, and it contains the same options as those in the [Edit Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058722-Edit-Filter-Dialog-Box).

![Table Wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404856889367/tblwzd_fltr_bv1.gif)

#### Style

Specifies the style of the table.

![Table Wizard - Style](https://devnet.logianalytics.com/hc/article_attachments/4404848488087/tblwzd_sty_bv1.gif)

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

Opens the [Page Setup dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060082-Page-Setup-Dialog-Box) to specify the page settings. Available only when creating a table in a page report.

### For Summary Table in Web Report/Library Component

When the wizard is used for creating/editing a summary table in a web report/library component using a business view, it consists of the following screens: [Data](#Data1), [Columns](#Columns), [Summary](#Summary1), [Filter](#Filter1) and [Style](#Style1).

#### Data

The screen lists all the predefined business views in the current catalog. Select the one you want to use for the table.

![Summary Table Wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404856889623/tblwzd_dt_bv2.gif)

**Inherit from the Parent**

Specifies to inherit data from the business view used by the parent object. Available only when the table is in any of the following panels in a banded object in a web report: banded header panel, banded footer panel, group header panel and group footer panel.

#### Columns

Specifies the fields to create the columns of the table.

![Summary Table Wizard - Columns](https://devnet.logianalytics.com/hc/article_attachments/4404848488599/tblwzd_clmn.gif)

**Resources**

Lists the resources in and related to the specified business view, which can be used to create the columns in the table.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)

Adds the selected field in the Resources box to create a column in the table.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)

Removes the selected field from the table.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404856888855/btn_replace.gif)

Replaces the selected field in the table with the specified field in the Resources box. Available only when editing a table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**

Select to move the specified field higher in the display order.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**

Select to move the specified field lower in the display order.

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
   Opens the [Custom Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095981-Custom-Sort-Dialog-Box) to set how groups will be sorted.

**Select N**

Opens the [Select N dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098701-Select-N-Dialog-Box) to specify the Select N condition for a group column.

#### Summary

Specifies to insert summaries to the header/footer panels of the table and groups.

![Summary Table Wizard - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404848488855/tblwzd_sum_bv2.gif)

**Resources**

Lists the aggregation objects that have been added to the table in the Columns screen.

**Summarized Fields**

Displays the group objects that have been added to the table in the Columns screen.

**Header**

Represents the table header or the group header of a specific group. After an object is selected in the Resources box, you can select the checkboxes in the column to insert it in the corresponding header panels.

**Footer**

Represents the table footer or the group footer of a specific group. After an object is selected in the Resources box, you can select the checkboxes in the column to insert it in the corresponding footer panels.

#### Filter

Specifies to filter data displayed in the table. This screen is available only when you create a table, and it contains the same options as those in the [Edit Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058722-Edit-Filter-Dialog-Box).

![Summary Table Wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404848489111/tblwzd_fltr_bv2.gif)

#### Style

Specifies the style of the table.

![Summary Table Wizard - Style](https://devnet.logianalytics.com/hc/article_attachments/4404856889879/tblwzd_sty_bv2.gif)

**Grow Report**

Specifies the layout of the table, which can only be Vertically. Available only when creating a table.

**Style**

Specifies the style of the table.

**Preview**

Displays the selected layout and style effects.

## Table Wizard - Query Based

When the wizard is used to create/edit a table using a query resource, it consists of the following screens: [Data](#Data), [Display](#Display), [Group](#Group), [Summary](#Summary), [Chart](#Chart), [Filter](#Filter) and [Style](#Style).

### Data

Specifies the dataset of the table.

![Table Wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404856890135/tblwzd_dt.gif)

**Data resource box**

Lists the predefined data resources in the current catalog. Select one and a dataset based on it is created automatically for the table.

**More Options**/**Less Options**

Shows or hides the dataset selection panel to choose a dataset for the table.

* **New Dataset**  
   Specifies to create a dataset from the current catalog data resources. When a query is selected, you can select the Edit button to edit the query in the [Query Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098321-Query-Editor-Dialog-Box).
* **Existing Dataset**  
   Specifies to use a dataset from the ones existing in the current page report. You can select the Edit button to edit the dataset in the [Dataset Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058622-Dataset-Editor-Dialog-Box).
* **Current Dataset**  
   Specifies to inherit the dataset used by the parent object.

### Display

Specifies the detail fields to display in the table.

![Table Wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4404848489495/tblwzd_dsply.gif)

**Resources**

Lists the data fields in and related to the specified query resource, which can be used as detail fields in the table.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**

Adds the selected field in the Resources box to the table.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)

Removes the selected field from the table.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404856888855/btn_replace.gif)

Replaces the selected field in the table with the specified field in the Resources box. Available only when editing a table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)

Moves the selected field higher in the display order. Available only when creating a table.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)

Moves the selected field lower in the display order. Available only when creating a table.

**Show Table Group Structure**

Specifies whether to show the group structure of the table. Available only when editing a table.

**Display Fields**

Lists the detail fields of the table.

**Display Name**

Specifies the labels of the detail columns, which by default are the display names of the added fields. You can select in the text boxes to edit the labels.

**Sort Fields By**

Opens the [Sort Fields By dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060542-Sort-Fields-By-Dialog-Box) to specify how to sort the detail data in the table.

### Group

Specifies the criteria for grouping data in the table.

![Table Wizard - Group](https://devnet.logianalytics.com/hc/article_attachments/4404848489751/tblwzd_grp.gif)

**Resources**

The box lists the data fields in and related to the specified query resource, which you can use as group-by fields in the table.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add button**

Adds the selected field in the Resources box as a group-by field in the table.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)**Remove button**

Removes the selected group-by field from the table.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404856888855/btn_replace.gif)**Replace button**

Replaces the selected group-by field in the table with the specified field in the Resources box. Designer displays the button only when you use the dialog box for modifying a table.

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

### Summary

Specifies the fields on which to create aggregate functions. This screen is available only when you create a table.

![Table Wizard - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404848490135/tblwzd_sum.gif)

**Resources**

Lists the data fields in and related to the specified query resource, which can be used to create summaries in the table.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)

Adds the selected field in the Resources box based on which to create a summary in the table.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)

Removes the selected summary from the table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**

Select to move the specified summary higher in the display order.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**

Select to move the specified summary lower in the display order.

**Summarized Fields**

Lists the fields that have been added to create summaries in the table.

**Aggregate Function**

Specifies the [aggregate functions](https://devnet.logianalytics.com/hc/en-us/articles/1500010061062-Working-with-Summaries#Function) used for the summaries.

**Distinct On**

Designer enables the option and you should set it when you select DistinctSum as the aggregate function. Select the ellipsis button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404848397591/btn_ellipsis.gif) to select the fields according to whose unique values to calculate DistinctSum in the [Select Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060462-Select-Fields-Dialog-Box).

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

### Chart

Specifies to create a chart together with the table, which will be placed above the table in the report body. This screen is available only when you create a table, and when there is at least one group and one summary added for this group in the table.

![Table Wizard - Chart](https://devnet.logianalytics.com/hc/article_attachments/4404848490391/tblwzd_cht.gif)

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

### Filter

Specifies to filter data displayed in the table. This screen is available only when you create a table, and it contains the same options as those in the [Edit Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058722-Edit-Filter-Dialog-Box).

![Table Wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404848491031/tblwzd_fltr.gif)

## Style

Specifies the style of the table.

![Table Wizard - Style](https://devnet.logianalytics.com/hc/article_attachments/4404856891031/tblwzd_sty.gif)

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

Opens the [Page Setup dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060082-Page-Setup-Dialog-Box) to specify the page settings. Available only when creating a table.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099021-Table-Type-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010060742-Tabular-Wizard-Dialog-Box)
