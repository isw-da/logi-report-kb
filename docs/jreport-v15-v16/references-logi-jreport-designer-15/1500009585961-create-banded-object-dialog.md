---
title: "Create Banded Object Dialog"
id: 1500009585961
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009585961-Create-Banded-Object-Dialog
updated_at: 2021-07-24T05:55:33Z
---

# Create Banded Object Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564802-Connect-to-SQL-Server-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564882-Create-Chart-Dialog-Business-View-Based-)

# Create Banded Object Dialog

The Create Banded Object wizard differs according to the data resource type used to create the banded object: [query resource](#Query) or [business view](#BV).

## When using a Query Resource

This wizard appears when you select Insert > Banded Object in a page report that is created using query resources. It helps you to [insert a banded object](https://devnet.logianalytics.com/hc/en-us/articles/1500009583281-Inserting-a-Banded-Object) into the page report, and consists of the following screens:

* [Data](#Data)
* [Display](#Display)
* [Group](#Group)
* [Summary](#Summary)
* [Filter](#Filter)
* [Style](#Layout)

**Back**

Goes back to the previous screen.

**Next**

Goes to the next screen.

**Finish**

Finishes creating the banded object and closes this dialog.

**Cancel**

Does not retain changes and closes this dialog.

**Help**

Displays the help document about this feature.

## Data

Specifies the dataset that you want to use to create the banded report. [See the screen](javascript:%20void(null)).

![Create Banded Object wizard based on query - Data screen](https://devnet.logianalytics.com/hc/article_attachments/4404889383191/crtbdobj_dt.gif)

**Resource box**

Lists the available data resources in the current catalog. Select one to create the banded object.

**More Options/Less Options**

Shows or hides the dataset selection panel to choose a dataset for the banded object.

* **New Dataset**  
   If checked, select a data source from the catalog resources to create a dataset that will be used to build the banded object. When you choose to create the dataset from a query, you can select the Edit button to edit the query in the [Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009567142-Query-Editor-Dialog) if required.
* **Existing Dataset**  
   If checked, select a dataset from the ones existing in the open report to create the banded object. Select the Edit button to edit the dataset in the [Dataset Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009586301-Dataset-Editor-Dialog) if required.
* **Current Dataset**  
   If checked, the current dataset used by the parent object will be applied to the banded object.

## Display

Specifies the data fields that you want to display in the banded object. [See the screen](javascript:%20void(null)).

![Create Banded Object wizard based on query - Display screen](https://devnet.logianalytics.com/hc/article_attachments/4404893944343/crtbdobj_dsply.gif)

**Resources**

Lists all the available data resources.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)**

Adds the specified field to use in the banded object.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)**

Removes the specified field that is not required in the banded object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the specified field one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the specified field one step down.

**Display Fields**

Lists the fields that have been selected to display in the banded object.

**Display Name**

Shows the display names of the selected fields. You can select the name cells to edit them if required.

**Sort Fields By**

Opens the [Sort Fields By](https://devnet.logianalytics.com/hc/en-us/articles/1500009588961-Sort-Fields-By-Dialog) dialog to specify how to sort data in the banded object.

## Group

Specifies the data fields that are used to group the data. [See the screen](javascript:%20void(null)).

![Create Banded Object wizard based on query - Group screen](https://devnet.logianalytics.com/hc/article_attachments/4404893944599/crtbdobj_grp.gif)

**Resources**

Lists all the available data resources.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)**

Adds the selected field as the group by field in the banded object.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)**

Removes the selected group by field that is not required.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the specified group one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the specified group one step down.

**Group By**

Lists the fields that are used to group data in the banded object.

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

![Create Banded Object wizard based on query - Summary screen](https://devnet.logianalytics.com/hc/article_attachments/4404889383703/crtbdobj_sum.gif)

**Resources**

Lists all the available data resources.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)**

Adds the selected field as the summary field to the banded object.

**![Rremove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)**

Removes the selected summary field that is not required.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the specified summary field one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the specified summary field one step down.

**Summarized Fields**

Lists all the fields that you want to display and to be summarized in the banded object. If an aggregation is added under the Banded Object node, it will be displayed in the banded panel. If an aggregation is added under the node of a specified group, it will be displayed in the corresponding group panel.

**Aggregate Function**

Specifies the function to summarize the selected field.

**Break Field**

Displays a defined field on which the summary will be calculated. If a summary field is added below the Banded Object node, the break field is null and the summary will be calculated on the whole dataset.

**Position**

Works together with the Column option to specify the location where the summary field will be put.

* **Header**  
   Specifies to put the summary field in the header row. If the summary is calculated on a group by field, it will be put in the group header row of the corresponding group; if the summary is calculated on the whole dataset, it will be put in the table header row.
* **Footer**  
   Specifies to put the summary field in the footer row. If the summary is calculated on a group by field, it will be put in the group footer row of the corresponding group; if the summary is calculated on the whole dataset, it will be put in the table footer row.

**Column**

Works together with the Position option to specify the location where the summary field will be put.

* **Detail**  
   The summary field with its label will be put in in the first two detail columns.
* **Summary**  
   The summary field will be displayed in a separate summary column.

## Filter

Specifies to filter data displayed in the banded object. [See the screen](javascript:%20void(null)).

![Create Banded Object wizard based on query - Filter screen](https://devnet.logianalytics.com/hc/article_attachments/4404889383959/crtbdobj_fltr.gif)

The options in the screen are the same as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009565242-Edit-Filter-Dialog) dialog.

## Style

Specifies the style of the banded object. [See the screen](javascript:%20void(null)).

![Create Banded Object wizard based on query - Style screen](https://devnet.logianalytics.com/hc/article_attachments/4404893944855/crtbdobj_sty.gif)

**Grow Report**

Specifies the layout of the banded object.

* **Vertically**  
   Creates a vertical banded object.
* **Horizontally**  
   Creates a horizontal banded object.
* **Mailing Label Format**  
   Creates a cross banded object in the form of a mailing label layout.

**Style**

Specifies the style of the banded object.

**Preview**

Displays the selected layout and style effects.

**Inherit Style**

Specifies whether to make the banded object take the style of its parent. Available only when the banded object is to be inserted into another banded object.

## When using a Business View

This wizard appears when you select Insert > Banded Object in a page report that is creating using business views. It helps you to [insert a banded object](https://devnet.logianalytics.com/hc/en-us/articles/1500009583281-Inserting-a-Banded-Object) into a report, and consists of the following screens:

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

Finishes creating the banded object and closes this wizard.

**Cancel**

Does not retain changes and closes this wizard.

**Help**

Displays the help document about this feature.

### Data

Specifies a business view for the banded object. [See the screen](javascript:%20void(null)).

![Create Banded Object wizard based on business view - Data screen](https://devnet.logianalytics.com/hc/article_attachments/4404889384215/crtbdobj_dt-bv.gif)

**Resources**

Lists all the business views in the current catalog. Specify the one you want to use.

### Display

Specifies the data fields to display in the banded object. [See the screen](javascript:%20void(null)).

![Create Banded Object wizard based on business view - Display screen](https://devnet.logianalytics.com/hc/article_attachments/4404889384471/crtbdobj_dsply-bv.gif)

**Resources**

Lists all the available data resources.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)**

Adds the specified field to use in the banded object.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)**

Removes the specified field that is not required in the banded object.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404889314711/btn_replace.gif)

Replaces the selected field in the banded object with the specified field in the Resources box.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the specified field one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the specified field one step down.

**Display Fields**

Lists the fields that you have selected to display in the banded object.

**Display Name**

Shows the display names of the selected fields. You can select the name cells to edit them if required.

**Sort Fields By**

Opens the [Sort Fields By](https://devnet.logianalytics.com/hc/en-us/articles/1500009588961-Sort-Fields-By-Dialog) dialog to specify how to sort data in the banded object.

### Group

Specifies the fields to group the data. [See the screen](javascript:%20void(null)).

![Create Banded Object wizard based on business view - Group screen](https://devnet.logianalytics.com/hc/article_attachments/4404893945111/crtbdobj_grp-bv.gif)

**Resources**

Lists all the available data resources.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)**

Adds the selected field as the group by field in the banded object.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)**

Removes the selected group by field that is not required.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404889314711/btn_replace.gif)

Replaces the selected group by field in the banded object with the specified field in the Resources box.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the specified group one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the specified group one step down.

**Group By**

Lists the fields that are used to group data in the banded object.

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

### Summary

Specifies the aggregations to display in the banded object. [See the screen](javascript:%20void(null)).

![Create Banded Object based on business view - Summary screen](https://devnet.logianalytics.com/hc/article_attachments/4404893945367/crtbdobj_sum-bv.gif)

**Resources**

Lists all the available aggregations.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)**

Adds the selected aggregation to the banded object.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)**

Removes the selected aggregation that is not required.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the specified aggregation one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the specified aggregation one step down.

**Summarized Fields**

Lists all the aggregations that you want to display in the banded object. If an aggregation is added under the Banded Object node, it will be displayed in the banded panel. If an aggregation is added under the node of a specific group, it will be displayed in the corresponding group panel.

**Position**

Works together with the Column option to specify the location where the aggregation will be put.

* **Footer**  
   Specifies to put the aggregation in the footer row. If the aggregation is calculated on a group by field, it will be put in the group footer row of the corresponding group; if the aggregation is calculated on the whole dataset, it will be put in the banded footer row.

**Column**

Works together with the Position option to specify the location where the aggregation will be put.

* **Detail**  
   The aggregation with its label will be put in in the first two detail columns.

### Filter

Specifies to filter data displayed in the banded object. [See the screen](javascript:%20void(null)).

![Create Banded Object wizard based on business view - Filter screen](https://devnet.logianalytics.com/hc/article_attachments/4404889384855/crtbdobj_fltr-bv.gif)

The options in the screen are the same as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009565242-Edit-Filter-Dialog) dialog.

### Style

Specifies the style of the banded object. [See the screen](javascript:%20void(null)).

![Create Banded Object wizard based on business view - Style screen](https://devnet.logianalytics.com/hc/article_attachments/4404893945623/crtbdobj_sty-bv.gif)

**Grow Report**

Specifies the layout of the banded object.

* **Vertically**  
   Creates a vertical banded object.
* **Mailing Label Format**  
   Creates a cross banded object in the form of a mailing label layout.

**Style**

Specifies the style of the banded object.

**Preview**

Displays a diagram illustrating the effect of the selected style on the banded object.

**Inherit Style**

Specifies whether to make the banded object take the style of its parent. Available only when the banded object is to be inserted into another banded object.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564802-Connect-to-SQL-Server-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564882-Create-Chart-Dialog-Business-View-Based-)
