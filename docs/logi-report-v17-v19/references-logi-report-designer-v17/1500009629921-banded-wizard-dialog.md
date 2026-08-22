---
title: "Banded Wizard Dialog"
id: 1500009629921
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009629921-Banded-Wizard-Dialog
updated_at: 2021-07-24T16:05:00Z
---

# Banded Wizard Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009607282-Applet-Parameter-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009629941-Barcode-Expert-Dialog)

# Banded Wizard Dialog

The Banded Wizard helps you to [create a page report tab with a banded object in it](https://devnet.logianalytics.com/hc/en-us/articles/1500009613262-Creating-Reports#Page) or [modify an existing banded object](https://devnet.logianalytics.com/hc/en-us/articles/1500009628441-Modifying-Banded-Objects). It varies with the data resource type used for the banded object: [business view](#BV) or [query resource](#Query).

**Back**

Goes back to the previous screen.

**Next**

Goes to the next screen.

**Finish**

Finishes creating or modifying the banded object and closes this wizard.

**Cancel**

Does not retain changes and closes this wizard.

**Help**

Displays the help document about this feature.

## Banded Wizard - Business View Based

When the wizard is used for creating or editing a banded object using a business view, it consists of the following screens: [Data](#BVData), [Display](#BVDisplay), [Group](#BVGroup), [Summary](#BVSummary), [Filter](#BVFilter) and [Style](#BVStyle). Some screens are available only when the wizard is used for creating a banded object.

### Data

The screen lists all the predefined business views in the current catalog. Select the one you want to use for the banded object.

![Banded Wizard for business view - Data](https://devnet.logianalytics.com/hc/article_attachments/4404916818711/bdwzd_dt_bv.gif)

### Display

Specifies the detail fields to display in the banded object.

![Banded Wizard for business view - Display](https://devnet.logianalytics.com/hc/article_attachments/4404916818967/bdwzd_dsply_bv.gif)

**Resources**

Lists the resources in and related to the specified business view, which can be used as detail fields in the banded object.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif)**

Adds the selected field in the Resources box to the banded object.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)**

Removes the selected field from the banded object.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404904235927/btn_replace.gif)

Replaces the selected field in the banded object with the specified field in the Resources box. Available only when modifying a banded object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif)

Moves the selected field one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif)

Moves the selected field one step down.

**Show Banded Group Structure**

Specifies whether to show the group structure of the banded object. Available only when modifying a banded object.

**Display Fields**

Lists the detail fields of the banded object.

**Display Name**

Specifies the labels of the detail columns in the banded object, which by default are the display names of the added fields. You can select in the text boxes to edit the labels, or select the Auto Map Field Name checkboxes in the text boxes to automatically map the label text to the dynamic display names of the fields at runtime.

**Sort Fields By**

Opens the [Sort Fields By](https://devnet.logianalytics.com/hc/en-us/articles/1500009633661-Sort-Fields-By-Dialog) dialog to specify how to sort the detail data in the banded object.

### Group

Specifies the criteria for grouping data in the banded object.

![Banded Wizard for business view - Group](https://devnet.logianalytics.com/hc/article_attachments/4404904392599/bdwzd_grp_bv.gif)

**Resources**

Lists the resources in and related to the specified business view, which can be used as group-by fields in the banded object.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif)

Adds the selected field in the Resources box as a group-by field in the banded object.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)

Removes the selected group-by field from the banded object.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404904235927/btn_replace.gif)

Replaces the selected group-by field in the banded object with the specified field in the Resources box. Available only when modifying a banded object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif)

Moves the selected group one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif)

Moves the selected group one step down.

**Group By**

Lists the group-by fields of the banded object.

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

### Summary

Specifies the summaries to calculate data in the banded object. This screen is available only when you create a banded object.

![Banded Wizard for business view - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404904392855/bdwzd_smry_bv.gif)

**Resources**

Lists the resources in and related to the specified business view, which can be used to calculate data in the banded object.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif)**

Adds the selected field in the Resources box to calculate data in the banded object.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)**

Removes the selected summary from the banded object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif)

Moves the selected summary one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif)

Moves the selected summary one step down.

**Summarized Fields**

Lists the fields added to calculate data in the banded object.

**Position**

Displays the position of the summaries. A summary added for a group level is placed in the group's footer panel; if added for the Banded Object level, it will be placed in the banded footer panel.

**Column**

Displays in which column to place the summaries. By default the summaries and their name labels will be placed in the first two detail columns.

### Filter

Specifies to filter data displayed in the banded object. This screen is available only when you create a banded object, and it contains the same options as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009607882-Edit-Filter-Dialog) dialog.

![Banded Wizard for business view - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404904393111/bdwzd_fltr_bv.gif)

### Style

Specifies the style of the banded object.

![Banded Wizard for business view - Style](https://devnet.logianalytics.com/hc/article_attachments/4404904393367/bdwzd_sty_bv.gif)

**Style**

Specifies the style of the banded object.

**Preview**

Displays a diagram illustrating the effect of the selected style on the banded object.

**Inherit Style**

Specifies whether to make the banded object take the style of its parent. This option is available only when you modify a banded object which is inserted into another banded object in a page report.

**Page Setup**

Opens the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009609582-Page-Setup-Dialog) dialog to specify page properties. Available only when creating a banded object.

## Banded Wizard - Query Based

When the wizard is used for creating or editing a banded object using a query resource, it consists of the following screens: [Data](#Data), [Display](#Display), [Group](#Group), [Summary](#Summary), [Chart](#Chart), [Filter](#Filter) and [Style](#Style). Some screens are available only when the wizard is used for creating a banded object.

### Data

Specifies the dataset of the banded object.

![Banded Wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404904393623/bdwzd_dt.gif)

**Data resource box**

Lists the predefined data resources in the current catalog. Select one and a dataset based on it is created automatically for the banded object.

**More Options**/**Less Options**

Shows or hides the dataset selection panel to choose a dataset for the banded object.

* **New Dataset**  
   Specifies to create a dataset from the current catalog data resources. When a query is selected, you can select the Edit button to edit the query in the [Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009609882-Query-Editor-Dialog).
* **Existing Dataset**  
   Specifies to use a dataset from the ones existing in the current page report. You can select the Edit button to edit the dataset in the [Dataset Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009607762-Dataset-Editor-Dialog).
* **Current Dataset**  
   Specifies to inherit the dataset used by the parent object.

### Display

Specifies the detail fields to display in the banded object.

![Banded Wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4404916819223/bdwzd_dsply.gif)

**Resources**

Lists the data fields in and related to the specified query resource, which can be used as detail fields in the banded object.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif)**

Adds the selected field in the Resources box to the banded object.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)**

Removes the selected field from the banded object.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404904235927/btn_replace.gif)

Replaces the selected field in the banded object with the specified field in the Resources box. Available only when modifying a banded object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif)

Moves the selected field one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif)

Moves the selected field one step down.

**Show Banded Group Structure**

Specifies whether to show the group structure of the banded object. Available only when modifying a banded object.

**Display Fields**

Lists the detail fields of the banded object.

**Display Name**

Specifies the labels of the detail columns in the banded object, which by default are the display names of the added fields. You can select in the text boxes to edit the labels.

**Sort Fields By**

Opens the [Sort Fields By](https://devnet.logianalytics.com/hc/en-us/articles/1500009633661-Sort-Fields-By-Dialog) dialog to specify how to sort the detail data in the banded object.

### Group

Specifies the criteria for grouping data in the banded object.

![Banded Wizard - Group](https://devnet.logianalytics.com/hc/article_attachments/4404904393879/bdwzd_grp.gif)

**Resources**

Lists the data fields in and related to the specified query resource, which can be used as group-by fields in the banded object.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif)**

Adds the selected field in the Resources box as a group-by field in the banded object.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)**

Removes the selected group-by field from the banded object.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404904235927/btn_replace.gif)

Replaces the selected group-by field in the banded object with the specified field in the Resources box. Available only when modifying a banded object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif)

Moves the selected group one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif)

Moves the selected group one step down.

**Group By**

Lists the group-by fields of the banded object.

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

Specifies the fields on which to create summaries in the banded object. This screen is available only when you create a banded object.

![Banded Wizard - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404904394263/bdwzd_smry.gif)

**Resources**

Lists the data fields in and related to the specified query resource, which can be used to create summaries in the banded object.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif)**

Adds the selected field in the Resources box based on which to create a summary in the banded object.

**![Rremove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)**

Removes the selected summary from the banded object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif)

Moves the selected summary one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif)

Moves the selected summary one step down.

**Summarized Fields**

Lists the fields that have been added to create summaries in the banded object.

**Aggregate Function**

Specifies the [aggregate functions](https://devnet.logianalytics.com/hc/en-us/articles/1500009611182-Summaries#Function) used for the summaries.

**Distinct On**

Available and should be set when DistinctSum is selected as the aggregate function. It specifies the fields according to whose unique values to calculate DistinctSum. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904178967/btn_chsr.gif) in the text box to select the required fields in the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009633521-Select-Fields-Dialog) dialog.

**Break Field**

Displays the groups on which the summaries will be calculated. If a summary is added for the Banded Object level, the break field is null and the summary will be calculated on the whole dataset.

**Position**

Works together with the Column option to specify the location where a summary will be placed.

* **Header**  
   Specifies to put the summary in the header panel. If the summary is added for a specific group, it will be put in the group's header panel; if the summary is added for the Banded Object level, it will be put in the banded header panel.
* **Footer**  
   Specifies to put the summary in the footer panel. If the summary is added for a specific group, it will be put in the group's footer panel; if the summary is added for the Banded Object level, it will be put in the banded footer panel.

**Column**

Works together with the Position option to specify the location where a summary will be placed.

* **Detail**  
   The summary and its name label will be put in the first two detail columns.
* **Summary**  
   The summary will be displayed in a separate summary column.

### Chart

Specifies to create a chart together with the banded object, which will be placed in the banded header panel. This screen is available only when you create a banded object, and when there is at least one group and one summary added for this group in the banded object.

![Banded Wizard - Chart](https://devnet.logianalytics.com/hc/article_attachments/4404904394519/bdwzd_cht.gif)

**No Chart**

Specifies not to create a chart.

**Bar Chart**

Specifies to create a Clustered Bar 2-D chart together with the banded object.

**Line Chart**

Specifies to create a Line 2-D chart together with the banded object.

**Pie Chart**

Specifies to create a Clustered Pie chart together with the banded object.

**Category**

Lists the group-by fields of the banded object on which summaries are added. Choose the field you want to display on the category (X) axis of the chart from the drop-down list.

**Series**

Lists the fields that have been added as the group-by fields of the banded object. Choose the field you want to display on the series (Z) axis of the chart from the drop-down list.

**Show Values**

Lists the summaries which are calculated based on the field you choose to display on the category axis of the chart. Choose the value you want to display in the chart from the drop-down list.

### Filter

Specifies to filter data displayed in the banded object. This screen is available only when you create a banded object, and it contains the same options as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009607882-Edit-Filter-Dialog) dialog.

![Banded Wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404904395031/bdwzd_fltr.gif)

### Style

Specifies the style of the banded object.

![Banded Wizard - Style](https://devnet.logianalytics.com/hc/article_attachments/4404904395415/bdwzd_sty.gif)

**Style**

Specifies the style of the banded object.

* **<Custom>**  
   There is no style information on it and it is only used to support reports built with previous versions which did not bind any style or the bound style cannot be found in the style list.

**Preview**

Displays a diagram illustrating the effect of the selected style on the banded object.

**Inherit Style**

Specifies whether to make the banded object take the style of its parent. Available only when you modify a banded object and the banded object is inserted into another banded object.

**Create a Banded Report**

Creates a restricted version of a flow layout report, one that can contain a single banded object only. This layout option is intended to provide compatibility with Logi Report Version 7 report templates. Available only when creating a banded object.

**Create a Flow Layout Report Containing a Banded Object**

Creates a report that contains a banded object mapped to the specified dataset. Available only when creating a banded object.

**Page Setup**

Opens the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009609582-Page-Setup-Dialog) dialog to specify page properties. Available only when creating a banded object.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009607282-Applet-Parameter-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009629941-Barcode-Expert-Dialog)
