---
title: "Banded Wizard Dialog"
id: 1500010029822
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010029822-Banded-Wizard-Dialog
updated_at: 2021-07-24T10:39:08Z
---

# Banded Wizard Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010064821-Applet-Parameter-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010029842-Barcode-Expert-Dialog)

# Banded Wizard Dialog

The Banded Wizard helps you to [create a page report tab with a banded object in it](https://devnet.logianalytics.com/hc/en-us/articles/1500010034782-Creating-Reports#Page) or [modify an existing banded object](https://devnet.logianalytics.com/hc/en-us/articles/1500010063321-Modifying-Banded-Objects). It varies with the data resource type used for the banded object: [business view](#BV) or [query resource](#Query).

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

![Banded Wizard for business view - Data](https://devnet.logianalytics.com/hc/article_attachments/4404901292183/bdwzd_dt_bv.gif)

### Display

Specifies the detail fields to display in the banded object.

![Banded Wizard for business view - Display](https://devnet.logianalytics.com/hc/article_attachments/4404901292567/bdwzd_dsply_bv.gif)

**Resources**

Lists the resources in and related to the specified business view, which can be used as detail fields in the banded object.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif)**

Adds the selected field in the Resources box to the banded object.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404901121047/btn_rmvarrow.gif)**

Removes the selected field from the banded object.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404901173527/btn_replace.gif)

Replaces the selected field in the banded object with the specified field in the Resources box. Available only when modifying a banded object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif)

Moves the selected field one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif)

Moves the selected field one step down.

**Show Banded Group Structure**

Specifies whether to show the group structure of the banded object. Available only when modifying a banded object.

**Display Fields**

Lists the detail fields of the banded object.

**Display Name**

Specifies the labels of the detail columns in the banded object, which by default are the display names of the added fields. You can select in the text boxes to edit the labels, or check the Auto Map Field Name checkboxes in the text boxes to automatically map the label text to the dynamic display names of the fields at runtime.

**Sort Fields By**

Opens the [Sort Fields By](https://devnet.logianalytics.com/hc/en-us/articles/1500010067861-Sort-Fields-By-Dialog) dialog to specify how to sort the detail data in the banded object.

### Group

Specifies the criteria for grouping data in the banded object.

![Banded Wizard for business view - Group](https://devnet.logianalytics.com/hc/article_attachments/4404901292823/bdwzd_grp_bv.gif)

**Resources**

Lists the resources in and related to the specified business view, which can be used as group-by fields in the banded object.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif)

Adds the selected field in the Resources box as a group-by field in the banded object.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404901121047/btn_rmvarrow.gif)

Removes the selected group-by field from the banded object.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404901173527/btn_replace.gif)

Replaces the selected group-by field in the banded object with the specified field in the Resources box. Available only when modifying a banded object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif)

Moves the selected group one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif)

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
   Opens the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500010065201-Custom-Sort-Dialog) dialog to set how groups will be sorted.

**Select N**

Opens the [Select N](https://devnet.logianalytics.com/hc/en-us/articles/1500010067821-Select-N-Dialog) dialog to specify the Select N condition.

### Summary

Specifies the summaries to calculate data in the banded object. This screen is available only when you create a banded object.

![Banded Wizard for business view - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404909245335/bdwzd_smry_bv.gif)

**Resources**

Lists the resources in and related to the specified business view, which can be used to calculate data in the banded object.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif)**

Adds the selected field in the Resources box to calculate data in the banded object.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404901121047/btn_rmvarrow.gif)**

Removes the selected summary from the banded object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif)

Moves the selected summary one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif)

Moves the selected summary one step down.

**Summarized Fields**

Lists the fields added to calculate data in the banded object.

**Position**

Displays the position of the summaries. A summary added for a group level is placed in the group's footer panel; if added for the Banded Object level, it will be placed in the banded footer panel.

**Column**

Displays in which column to place the summaries. By default the summaries and their name labels will be placed in the first two detail columns.

### Filter

Specifies to filter data displayed in the banded object. This screen is available only when you create a banded object, and it contains the same options as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500010065601-Edit-Filter-Dialog) dialog.

![Banded Wizard for business view - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404909248791/bdwzd_fltr_bv.gif)

### Style

Specifies the style of the banded object.

![Banded Wizard for business view - Style](https://devnet.logianalytics.com/hc/article_attachments/4404901293079/bdwzd_sty_bv.gif)

**Style**

Specifies the style of the banded object.

**Preview**

Displays a diagram illustrating the effect of the selected style on the banded object.

**Inherit Style**

Specifies whether to make the banded object take the style of its parent. This option is available only when you modify a banded object which is inserted into another banded object in a page report.

**Page Setup**

Opens the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500010067381-Page-Setup-Dialog) dialog to specify page properties. Available only when creating a banded object.

## Banded Wizard - Query Based

When the wizard is used for creating or editing a banded object using a query resource, it consists of the following screens: [Data](#Data), [Display](#Display), [Group](#Group), [Summary](#Summary), [Chart](#Chart), [Filter](#Filter) and [Style](#Style). Some screens are available only when the wizard is used for creating a banded object.

### Data

Specifies the dataset of the banded object.

![Banded Wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404909249175/bdwzd_dt.gif)

**Data resource box**

Lists the predefined data resources in the current catalog. Select one and a dataset based on it is created automatically for the banded object.

**More Options**/**Less Options**

Shows or hides the dataset selection panel to choose a dataset for the banded object.

* **New Dataset**  
   Specifies to create a dataset from the current catalog data resources. When a query is selected, you can select the Edit button to edit the query in the [Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500010067501-Query-Editor-Dialog) if required.
* **Existing Dataset**  
   Specifies to use a dataset from the ones existing in the current page report. Select the Edit button to edit the dataset in the [Dataset Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500010030342-Dataset-Editor-Dialog) if required.
* **Current Dataset**  
   Specifies to inherit the dataset used by the parent object.

### Display

Specifies the detail fields to display in the banded object.

![Banded Wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4404901293335/bdwzd_dsply.gif)

**Resources**

Lists the data fields in and related to the specified query resource, which can be used as detail fields in the banded object.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif)**

Adds the selected field in the Resources box to the banded object.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404901121047/btn_rmvarrow.gif)**

Removes the selected field from the banded object.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404901173527/btn_replace.gif)

Replaces the selected field in the banded object with the specified field in the Resources box. Available only when modifying a banded object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif)

Moves the selected field one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif)

Moves the selected field one step down.

**Show Banded Group Structure**

Specifies whether to show the group structure of the banded object. Available only when modifying a banded object.

**Display Fields**

Lists the detail fields of the banded object.

**Display Name**

Specifies the labels of the detail columns in the banded object, which by default are the display names of the added fields. You can select in the text boxes to edit the labels if required.

**Sort Fields By**

Opens the [Sort Fields By](https://devnet.logianalytics.com/hc/en-us/articles/1500010067861-Sort-Fields-By-Dialog) dialog to specify how to sort the detail data in the banded object.

### Group

Specifies the criteria for grouping data in the banded object.

![Banded Wizard - Group](https://devnet.logianalytics.com/hc/article_attachments/4404901293591/bdwzd_grp.gif)

**Resources**

Lists the data fields in and related to the specified query resource, which can be used as group-by fields in the banded object.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif)**

Adds the selected field in the Resources box as a group-by field in the banded object.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404901121047/btn_rmvarrow.gif)**

Removes the selected group-by field from the banded object.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404901173527/btn_replace.gif)

Replaces the selected group-by field in the banded object with the specified field in the Resources box. Available only when modifying a banded object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif)

Moves the selected group one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif)

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
   Opens the [User Defined Group](https://devnet.logianalytics.com/hc/en-us/articles/1500010068301-User-Defined-Group-Dialog) dialog to define grouping information.
* **Custom Sort**  
   Opens the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500010065201-Custom-Sort-Dialog) dialog to set how groups will be sorted.

**Special Function**

For a group-by field of the Numeric/String/Date/Time type, you can select a [special function](https://devnet.logianalytics.com/hc/en-us/articles/1500010063921-Grouping-the-Data-in-Tables#Function) for it to specify to which level data will be grouped by. Select Customize to set the function in the [Customized Function](https://devnet.logianalytics.com/hc/en-us/articles/1500010065221-Customized-Function-Dialog) dialog.

**Custom Sort**

Specifies how to sort the groups. Activated only when you have selected Custom Sort from the Sort column to define the sort manner of groups for the selected group level.

**Special Group**

Specifies how to group your information. Activated only when you have selected Special Group from the Sort column to define a special group.

**Select N**

Opens the [Select N](https://devnet.logianalytics.com/hc/en-us/articles/1500010067821-Select-N-Dialog) dialog to specify the Select N condition.

**Group Filter**

Opens the [Group Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500010031302-Group-Filter-Dialog) dialog to specify the group filter condition.

### Summary

Specifies the fields on which to create summaries in the banded object. This screen is available only when you create a banded object.

![Banded Wizard - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404909249687/bdwzd_smry.gif)

**Resources**

Lists the data fields in and related to the specified query resource, which can be used to create summaries in the banded object.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif)**

Adds the selected field in the Resources box based on which to create a summary in the banded object.

**![Rremove button](https://devnet.logianalytics.com/hc/article_attachments/4404901121047/btn_rmvarrow.gif)**

Removes the selected summary from the banded object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif)

Moves the selected summary one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif)

Moves the selected summary one step down.

**Summarized Fields**

Lists the fields that have been added to create summaries in the banded object.

**Aggregate Function**

Specifies the [aggregate functions](https://devnet.logianalytics.com/hc/en-us/articles/1500010068581-Summaries#Function) used for the summaries.

**Distinct On**

Available and should be set when DistinctSum is selected as the aggregate function. It specifies the fields according to whose unique values to calculate DistinctSum. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404901122967/btn_chsr.gif) in the text box to select the required fields in the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500010032562-Select-Fields-Dialog) dialog.

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

![Banded Wizard - Chart](https://devnet.logianalytics.com/hc/article_attachments/4404909249943/bdwzd_cht.gif)

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

Specifies to filter data displayed in the banded object. This screen is available only when you create a banded object, and it contains the same options as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500010065601-Edit-Filter-Dialog) dialog.

![Banded Wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404901294103/bdwzd_fltr.gif)

### Style

Specifies the style of the banded object.

![Banded Wizard - Style](https://devnet.logianalytics.com/hc/article_attachments/4404901294359/bdwzd_sty.gif)

**Style**

Specifies the style of the banded object.

* **<Custom>**  
   There is no style information on it and it is only used to support reports built with previous versions which did not bind any style or the bound style cannot be found in the style list.

**Preview**

Displays a diagram illustrating the effect of the selected style on the banded object.

**Inherit Style**

Specifies whether to make the banded object take the style of its parent. Available only when you modify a banded object and the banded object is inserted into another banded object.

**Create a Banded Report**

Creates a restricted version of a flow layout report, one that can contain a single banded object only. This layout option is intended to provide compatibility with Logi JReport Version 7 report templates. Available only when creating a banded object.

**Create a Flow Layout Report Containing a Banded Object**

Creates a report that contains a banded object mapped to the specified dataset. Available only when creating a banded object.

**Page Setup**

Opens the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500010067381-Page-Setup-Dialog) dialog to specify page properties. Available only when creating a banded object.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010064821-Applet-Parameter-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010029842-Barcode-Expert-Dialog)
