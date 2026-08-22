---
title: "Create Table Dialog (for Page Report)"
id: 1500009564962
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009564962-Create-Table-Dialog-for-Page-Report
updated_at: 2021-07-24T05:55:32Z
---

# Create Table Dialog (for Page Report)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564942-Create-Query-s-Username-and-Password-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009586101-Create-Table-Dialog-for-Web-Report-and-Library-Component-)

# Create Table Dialog (for Page Report)

The Create Table dialog for page report differs according to the data resource type used to create the table: [query resource](#Query) or [business view](#BV).

## When using a Query Resource

This wizard appears when you choose a table type and select OK in the [Table Type](https://devnet.logianalytics.com/hc/en-us/articles/1500009567762-Table-Type-Dialog) dialog, or drag the desired table type button from the Components panel into a page report that is created using query resources. It helps you to [create a table](https://devnet.logianalytics.com/hc/en-us/articles/1500009563682-Inserting-a-Table#Page) in the page report, and consists of the following screens:

* [Data](#Data)
* [Display](#Display)
* [Group](#Group)
* [Summary](#Summary)
* [Filter](#Filter)
* [Style](#Style)

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

## Data

Specifies the dataset that you want to use to create the table. [See the screen](javascript:%20void(null)).

![Create Table wizard for page report based on query - Data screen](https://devnet.logianalytics.com/hc/article_attachments/4404893934231/crttbl_dt.gif)

**Resource box**

Lists the available data resources in the current catalog. Select one to create the table.

**More Options/Less Options**

Shows or hides the dataset selection panel to choose a dataset for the table.

* **New Dataset**   
   If checked, select a data source from the catalog resources to create a dataset that will be used to build the table. When you choose to create the dataset from a query, you can select the Edit button to edit the query in the [Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009567142-Query-Editor-Dialog) if required.
* **Existing****Dataset**  
   If checked, select a dataset from the ones existing in the open report to create the table. You can select the Edit button to edit the dataset in the [Dataset Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009586301-Dataset-Editor-Dialog) if required.
* **Current****Dataset**  
   If checked, the current dataset used by the parent object will be applied to the table.

## Display

Specifies the fields that you want to display in the table. [See the screen](javascript:%20void(null)).

![Create Table wizard for page report based on query - Display screen](https://devnet.logianalytics.com/hc/article_attachments/4404893934487/crttbl_dsply.gif)

**Resources**

Lists all the available data resources.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)**

Adds the specified field to use in the table.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)**

Removes the specified field that is not required in the table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the specified field one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the specified field one step down.

**Display Fields**

Lists the fields that have been selected to display in the table.

**Display Name**

Shows the display names of the selected fields. You can select the name cells to edit them if required.

**Sort Fields By**

Opens the [Sort Fields By](https://devnet.logianalytics.com/hc/en-us/articles/1500009588961-Sort-Fields-By-Dialog) dialog to specify how to sort data in the table.

## Group

Specifies the fields that you want to use to group the data. [See the screen](javascript:%20void(null)).

![Create Table wizard for page report based on query - Group screen](https://devnet.logianalytics.com/hc/article_attachments/4404893934743/crttbl_grp.gif)

**Resources**

Lists all the available data resources.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)**

Adds the selected field as the group by field in the table.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)**

Removes the selected group by field that is not required.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the specified group one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the specified group one step down.

**Group By**

Lists the fields that are used to group data in the table.

**Sort**

Specifies how groups at the specific group level will be sorted.

* **Ascend**  
   Groups will be sorted in an ascending order (A, B, C).
* **Descend**  
   Groups will be sorted in a descending order (C, B, A).
* **No Sort**  
   Groups will be sorted in the original order in database.
* **Special Group**  
   Opens the [User Defined Group](https://devnet.logianalytics.com/hc/en-us/articles/1500009589181-User-Defined-Group-Dialog) dialog to define grouping information.

  For example, if you placed a field named Region for grouping, and this field contains all 50 states of the United States; and if you want to see the data between Maryland (MD) and New York (NY), you can define the criteria by selecting the between operator to further define your grouping information.
* **Custom Sort**  
   Opens the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009586161-Custom-Sort-Dialog) dialog to set how groups will be sorted.

**Special Function**

If the group by field is of Numeric/String/Date/Time type, you can select a [special function](https://devnet.logianalytics.com/hc/en-us/articles/1500009563662-Specifying-Special-Function-for-Group-by-Field) for the field in the Special Function column to further specify to which level the data will be grouped by.

If Customize is selected, the [Customized Function](https://devnet.logianalytics.com/hc/en-us/articles/1500009586201-Customized-Function-Dialog) dialog will be displayed, in which you can set the function by your own.

**Custom Sort**

Specifies how to sort the groups. Activated only when you have selected Custom Sort from the Sort column to define the sorting manner of groups for the selected group level.

**Special Group**

Specifies how to group your information. Activated only when you have selected Special Group from the Sort column to define a special group.

**Select N**

Opens the [Select N](https://devnet.logianalytics.com/hc/en-us/articles/1500009567482-Select-N-Dialog) dialog to specify the Select N condition.

**Group Filter**

Opens the [Group Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009566302-Group-Filter-Dialog) dialog to specify the group filter condition.

## Summary

Specifies the fields on which you want to create aggregate functions. [See the screen](javascript:%20void(null)).

![Create Table wizard for page report based on query - Summary screen](https://devnet.logianalytics.com/hc/article_attachments/4404889372951/crttbl_sum.gif)

**Resources**

Lists all the available data resources.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)**

Adds the selected field as the summary field to the table.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)**

Removes the selected summary field that is not required.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the specified summary field one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the specified summary field one step down.

**Summarized Fields**

Lists all the fields that you want to display and to be summarized in the table.

**Aggregate Function**

Specifies the function to summarize the selected field.

**Break Field**

Displays a defined field on which the summary will be calculated. If a summary field is added below the Table node, the break field is null and the summary will be calculated on the whole dataset.

**Position**

Works together with the Column option to specify the location where the summary field will be put. Not available when the table type is Group Above.

* **Header**  
   Specifies to put the summary field in the header row. If the summary is calculated on a group by field, it will be put in the group header row of the corresponding group; if the summary is calculated on the whole dataset, it will be put in the table header row.
* **Footer**  
   Specifies to put the summary field in the footer row. If the summary is calculated on a group by field, it will be put in the group footer row of the corresponding group; if the summary is calculated on the whole dataset, it will be put in the table footer row.

**Column**

Works together with the Position option to specify the location where the summary field will be put. Not available when the table type is Group Above.

* **Detail**  
   The summary field with its label will be put in the first two detail columns.
* **Summary**  
   The summary field will be displayed in a separate summary column.

## Filter

Specifies to filter data displayed in the table. [See the screen](javascript:%20void(null)).

![Create Table wizard for page report based on query - Filter screen](https://devnet.logianalytics.com/hc/article_attachments/4404893934999/crttbl_fltr.gif)

The options in the screen are the same as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009565242-Edit-Filter-Dialog) dialog.

## Style

Specifies the style of the table. [See the screen](javascript:%20void(null)).

![Create Table wizard for page report based on query - Style screen](https://devnet.logianalytics.com/hc/article_attachments/4404889373207/crttbl_sty.gif)

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

## When using a Business View

This wizard appears when you choose a table type and select OK in the [Table Type](https://devnet.logianalytics.com/hc/en-us/articles/1500009567762-Table-Type-Dialog) dialog, or drag the desired table type button from the Components panel into a page report that is created using business views. It helps you to [create a table](https://devnet.logianalytics.com/hc/en-us/articles/1500009563682-Inserting-a-Table#Web) in the page report, and consists of the following screens:

* [Data](#Data-bv)
* [Display](#Display-bv)
* [Group](#Group-bv)
* [Summary](#Summary-bv)
* [Filter](#Filter-bv)
* [Style](#Style-bv)

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

## Data

Specifies the dataset that you want to use to create the table. [See the screen](javascript:%20void(null)).

![Create Table wizard for page report based on business view - Data screen](https://devnet.logianalytics.com/hc/article_attachments/4404889373463/crttbl_dt-bv.gif)

**Resource box**

Lists the available business views in the current catalog. Select one to create the table.

## Display

Specifies the fields that you want to display in the table. [See the screen](javascript:%20void(null)).

![Create Table wizard for page report based on business view - Display screen](https://devnet.logianalytics.com/hc/article_attachments/4404889373719/crttbl_dsply-bv.gif)

**Title**

Specifies the title for the table.

**Resources**

Lists all the available data resources.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)**

Adds the specified field to use in the table.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)**

Removes the specified field that is not required in the table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the specified field one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the specified field one step down.

**Display Fields**

Lists the fields that have been selected to display in the table.

**Display Name**

Shows the display names of the selected fields. You can select the name cells to edit them if required.

**Sort Fields By**

Opens the [Sort Fields By](https://devnet.logianalytics.com/hc/en-us/articles/1500009588961-Sort-Fields-By-Dialog) dialog to specify how to sort data in the table.

## Group

Specifies the fields that you want to use to group the data. [See the screen](javascript:%20void(null)).

![Create Table wizard for page report based on business view - Group screen](https://devnet.logianalytics.com/hc/article_attachments/4404893935255/crttbl_grp-bv.gif)

**Resources**

Lists all the available data resources.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)**

Adds the selected field as the group by field in the table.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)**

Removes the selected group by field that is not required.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the specified group one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the specified group one step down.

**Group By**

Lists the fields that are used to group data in the table.

**Sort**

Specifies how groups at the specific group level will be sorted.

* **Ascend**  
   Groups will be sorted in an ascending order (A, B, C).
* **Descend**  
   Groups will be sorted in a descending order (C, B, A).
* **No Sort**  
   Groups will be sorted in the original order in database.
* **Custom Sort**  
   Opens the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009586161-Custom-Sort-Dialog) dialog to set how groups will be sorted.

**Select N**

Opens the [Select N](https://devnet.logianalytics.com/hc/en-us/articles/1500009567482-Select-N-Dialog) dialog to specify the Select N condition.

## Summary

Specifies the aggregations to display in the table. [See the screen](javascript:%20void(null)).

![Create Table wizard for page report based on business view - Summary screen](https://devnet.logianalytics.com/hc/article_attachments/4404893935511/crttbl_sum-bv.gif)

**Resources**

Lists all the available aggregations.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)**

Adds the selected aggregation to the table.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)**

Removes the selected aggregation that is not required.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the specified aggregation one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the specified aggregation one step down.

**Summarized Fields**

Lists all the aggregations that you want to display in the table. If an aggregation is added under the Table node, it will be displayed in the table panel. If an aggregation is added under the node of a specific group, it will be displayed in the corresponding group panel.

**Position**

Works together with the Column option to specify the location where the aggregation will be put.

* **Footer**  
   Specifies to put the aggregation in the footer row. If the aggregation is calculated on a group by field, it will be put in the group footer row of the corresponding group; if the aggregation is calculated on the whole dataset, it will be put in the table footer row.

**Column**

Works together with the Position option to specify the location where the aggregation will be put.

* **Detail**  
   The aggregation with its label will be put in in the first two detail columns.

## Filter

Specifies to filter data displayed in the table. [See the screen](javascript:%20void(null)).

![Create Table wizard for page report based on business view - Filter screen](https://devnet.logianalytics.com/hc/article_attachments/4404893935767/crttbl_fltr-bv.gif)

The options in the screen are the same as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009565242-Edit-Filter-Dialog) dialog.

## Style

Specifies the style of the table. [See the screen](javascript:%20void(null)).

![Create Table wizard for page report based on business view - Style screen](https://devnet.logianalytics.com/hc/article_attachments/4404889374231/crttbl_sty-bv.gif)

**Grow Report**

Specifies the layout of the table.

* **Vertically**  
   Creates a vertical table.

**Style**

Specifies the style of the table.

**Preview**

Displays the selected layout and style effects.

**Inherit Style**

Specifies whether to make the table take the style of its parent. Available only when the table is to be inserted into a banded object.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564942-Create-Query-s-Username-and-Password-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009586101-Create-Table-Dialog-for-Web-Report-and-Library-Component-)
