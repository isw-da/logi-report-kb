---
title: "Create Table Dialog"
id: 1500009630281
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009630281-Create-Table-Dialog
updated_at: 2021-07-24T16:04:53Z
---

# Create Table Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009630261-Create-Query-s-Username-and-Password-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009607482-Crosstab-Formula-Editor-Dialog)

# Create Table Dialog

The Create Table wizard helps you to [create a table](https://devnet.logianalytics.com/hc/en-us/articles/1500009629281-Inserting-Tables-in-a-Report-) in a report. It appears when you choose a table type and select OK in the [Table Type](https://devnet.logianalytics.com/hc/en-us/articles/1500009610642-Table-Type-Dialog) dialog, or drag the desired table type button from the Components panel into a report.

The wizard varies with the data resource type used to create the table: [business view](#BV) or [query resource](#Query).

**Back**

Goes back to the previous screen.

**Next**

Goes to the next screen.

**Finish**

Finishes creating the table and closes this dialog.

**Cancel**

Does not retain changes and closes this dialog.

**Help**

Displays the help document about this feature.

## Create Table - Business View Based

When the wizard is used in a web report/library component, the screens available in the wizard vary according to the table type: group table and summary table.

### For table in page report and group table in web report/library component

When the wizard is used for creating a table in a page report or creating a group table in a web report/library component using a business view, it consists of the following screens: [Data](#BVData), [Display](#BVDisplay), [Group](#BVGroup), [Summary](#BVSummary), [Filter](#BVFilter) and [Style](#BVStyle).

#### Data

The screen lists all the predefined business views in the current catalog. Select the one using which to create the table.

![Create Table - Data](https://devnet.logianalytics.com/hc/article_attachments/4404904363031/crttbl_dt_bv1.gif)

**Inherit from the Parent**

Specifies to inherit data from the business view used by the parent object. Available only when the table is to be inserted into any of the following panels in a banded object in a web report: banded header panel, banded footer panel, group header panel and group footer panel.

#### Display

Specifies the detail fields to display in the table.

![Create Table - Display](https://devnet.logianalytics.com/hc/article_attachments/4404904363415/crttbl_dsply_bv.gif)

**Title**

Specifies the title for the table.

**Resources**

Lists the resources in and related to the specified business view, which can be used as detail fields in the table.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif)**

Adds the selected field in the Resources box to the table.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)**

Removes the selected field from the table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif)

Moves the selected field one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif)

Moves the selected field one step down.

**Display Fields**

Lists the detail fields of the table.

**Display Name**

Specifies the text of the labels of the detail columns, which by default are the display names of the added fields. You can select in the text boxes to edit the label text, or select the Auto Map Field Name checkboxes in the text boxes to automatically map the label text to the dynamic display names of the fields at runtime.

**Sort Fields By**

Opens the [Sort Fields By](https://devnet.logianalytics.com/hc/en-us/articles/1500009633661-Sort-Fields-By-Dialog) dialog to specify how to sort the detail data in the table.

#### Group

Specifies the criteria for grouping data in the table.

![Create Table - Group](https://devnet.logianalytics.com/hc/article_attachments/4404916808215/crttbl_grp_bv.gif)

**Resources**

Lists the resources in and related to the specified business view, which can be used as group-by fields in the table.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif)

Adds the selected field in the Resources box as a group-by field in the table.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)

Removes the selected group-by field from the table.

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

Specifies the summaries to calculate data in the table.

![Create Table - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404916808471/crttbl_sum_bv1.gif)

**Resources**

Lists the resources in and related to the specified business view, which can be used to calculate data in the table.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif)**

Adds the selected field in the Resources box to calculate data in the table.

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

Works together with the Position option to specify the location where a summary will be placed.

* **Detail**  
   The summary and its name label will be put in the first two detail columns.
* **Summary**  
   The summary will be displayed in a separate summary column. Not available when the table type is Group Above.

#### Filter

Specifies to filter data displayed in the table. The options in the screen are the same as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009607882-Edit-Filter-Dialog) dialog.

![Create Table - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404916808727/crttbl_fltr_bv1.gif)

#### Style

Specifies the style of the table.

![Create Table - Style](https://devnet.logianalytics.com/hc/article_attachments/4404904364311/crttbl_sty_bv1.gif)

**Grow Report**

Specifies the layout of the table, which can only be Vertically.

**Style**

Specifies the style of the table.

**Preview**

Displays the selected layout and style effects.

**Inherit Style**

Specifies whether to make the table take the style of its parent. Available only when the table is to be inserted into a banded object.

### For summary table in web report/library component

When the wizard is used for creating a summary table in a web report/library component using a business view, it consists of the following screens: [Data](#Data1), [Columns](#Columns), [Summary](#Summary1), [Filter](#Filter1) and [Style](#Style1).

#### Data

The screen lists all the predefined business views in the current catalog. Select the one using which to create the table.

![Create Summary Table - Data](https://devnet.logianalytics.com/hc/article_attachments/4404904364567/crttbl_dt_bv2.gif)

**Inherit from the Parent**

Specifies to inherit data from the business view used by the parent object. Available only when the table is to be inserted into any of the following panels in a banded object in a web report: banded header panel, banded footer panel, group header panel and group footer panel.

#### Columns

Specifies the fields to create the columns of the table.

![Create Summary Table - Columns](https://devnet.logianalytics.com/hc/article_attachments/4404904364823/crttbl_clmn.gif)

**Resources**

Lists the resources in and related to the specified business view, which can be used to create the columns in the table.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif)**

Adds the selected field in the Resources box to create a column in the table.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)**

Removes the selected field from the table.

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

![Create Summary Table - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404904365079/crttbl_sum_bv2.gif)

**Resources**

Lists the aggregation objects that have been added to the table in the Columns screen.

**Summarized Fields**

Displays the group objects that have been added to the table in the Columns screen.

**Header**

Represents the table header or the group header of a specific group. After an object is selected in the Resources box, you can select the checkboxes in the column to insert it in the corresponding header panels.

**Footer**

Represents the table footer or the group footer of a specific group. After an object is selected in the Resources box, you can select the checkboxes in the column to insert it in the corresponding footer panels.

#### Filter

Specifies to filter data displayed in the table. The options in the screen are the same as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009607882-Edit-Filter-Dialog) dialog.

![Create Summary Table - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404916809111/crttbl_fltr_bv2.gif)

#### Style

Specifies the style of the table.

![Create Summary Table - Style](https://devnet.logianalytics.com/hc/article_attachments/4404904365591/crttbl_sty_bv2.gif)

**Grow Report**

Specifies the layout of the table, which can only be Vertically.

**Style**

Specifies the style of the table.

**Preview**

Displays the selected layout and style effects.

## Create Table - Query Based

When the wizard is used for creating a table using a query resource, it consists of the following screens: [Data](#Data), [Display](#Display), [Group](#Group), [Summary](#Summary), [Filter](#Filter) and [Style](#Style).

### Data

Specifies the dataset using which to create the table.

![Create Table - Data](https://devnet.logianalytics.com/hc/article_attachments/4404904366359/crttbl_dt.gif)

**Data resource box**

Lists the predefined data resources in the current catalog. Select one and a dataset based on it is created automatically for the table.

**More Options/Less Options**

Shows or hides the dataset selection panel to choose a dataset for the table.

* **New Dataset**  
   Specifies to create a dataset from the current catalog data resources. When a query is selected, you can select the Edit button to edit the query in the [Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009609882-Query-Editor-Dialog).
* **Existing Dataset**  
   Specifies to use a dataset from the ones existing in the current page report. You can select the Edit button to edit the dataset in the [Dataset Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009607762-Dataset-Editor-Dialog).
* **Current Dataset**  
   Specifies to inherit the dataset used by the parent object.

### Display

Specifies the detail fields to display in the table.

![Create Table - Display](https://devnet.logianalytics.com/hc/article_attachments/4404916809367/crttbl_dsply.gif)

**Resources**

Lists the data fields in and related to the specified query resource, which can be used as detail fields in the table.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif)**

Adds the selected field in the Resources box to the table.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)**

Removes the selected field from the table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif)

Moves the selected field one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif)

Moves the selected field one step down.

**Display Fields**

Lists the detail fields of the table.

**Display Name**

Specifies the labels of the detail columns, which by default are the display names of the added fields. You can select in the text boxes to edit the labels.

**Sort Fields By**

Opens the [Sort Fields By](https://devnet.logianalytics.com/hc/en-us/articles/1500009633661-Sort-Fields-By-Dialog) dialog to specify how to sort the detail data in the table.

### Group

Specifies the criteria for grouping data in the table.

![Create Table - Group](https://devnet.logianalytics.com/hc/article_attachments/4404904367127/crttbl_grp.gif)

**Resources**

Lists the data fields in and related to the specified query resource, which can be used as group-by fields in the table.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif)

Adds the selected field in the Resources box as a group-by field in the table.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)

Removes the selected group-by field from the table.

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

Specifies how to sort the groups. Activated only when you have selected Custom Sort from the Sort column to define the sort manner of groups for the selected group level.

**Special Group**

Specifies how to group your information. Activated only when you have selected Special Group from the Sort column to define a special group.

**Select N**

Opens the [Select N](https://devnet.logianalytics.com/hc/en-us/articles/1500009610362-Select-N-Dialog) dialog to specify the Select N condition.

**Group Filter**

Opens the [Group Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009631861-Group-Filter-Dialog) dialog to specify the group filter condition.

### Summary

Specifies the fields on which to create summaries in the table.

![Create Table - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404904367383/crttbl_sum.gif)

**Resources**

Lists the data fields in and related to the specified query resource, which can be used to create summaries in the table.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif)**

Adds the selected field in the Resources box based on which to create a summary in the table.

**![Rremove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)**

Removes the selected summary from the table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif)

Moves the selected summary one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif)

Moves the selected summary one step down.

**Summarized Fields**

Lists the fields that have been added to create summaries in the table.

**Aggregate Function**

Specifies the [aggregate functions](https://devnet.logianalytics.com/hc/en-us/articles/1500009611182-Summaries#Function) used for the summaries.

**Distinct On**

Available and should be set when DistinctSum is selected as the aggregate function. It specifies the fields according to whose unique values to calculate DistinctSum. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904178967/btn_chsr.gif) in the text box to select the required fields in the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009633521-Select-Fields-Dialog) dialog.

**Break Field**

Displays the groups on which the summaries will be calculated. If a summary is added for the Table level, the break field is null and the summary will be calculated on the whole dataset.

**Position**

Works together with the Column option to specify the location where the summary field will be placed.

* **Footer**  
   Specifies to put the summary in the footer panel. If the summary is added for a specific group, it will be put in the group's footer panel; if the summary is added for the Table level, it will be put in the table footer panel.
* **Header**  
   Specifies to put the summary in the header panel. If the summary is added for a specific group, it will be put in the group's header panel; if the summary is added for the Table level, it will be put in the table header panel. Not available when the table type is Group Above.

**Column**

Works together with the Position option to specify the location where the summary will be placed.

* **Detail**  
   The summary and its name label will be put in the first two detail columns.
* **Summary**  
   The summary will be displayed in a separate summary column. Not available when the table type is Group Above.

### Filter

Specifies to filter data displayed in the table. The options in the screen are the same as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009607882-Edit-Filter-Dialog) dialog.

![Create Table - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404904367639/crttbl_fltr.gif)

### Style

Specifies the style of the table.

![Create Table - Style](https://devnet.logianalytics.com/hc/article_attachments/4404904367895/crttbl_sty.gif)

**Grow Report**

Specifies the layout of the table.

* **Vertically**  
   Creates a vertical table.
* **Horizontally**  
   Creates a horizontal table.

**Style**

Specifies the style of the table.

**Preview**

Displays the selected layout and style effects.

**Inherit Style**

Specifies whether to make the table take the style of its parent. Available only when the table is to be inserted into a banded object.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009630261-Create-Query-s-Username-and-Password-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009607482-Crosstab-Formula-Editor-Dialog)
