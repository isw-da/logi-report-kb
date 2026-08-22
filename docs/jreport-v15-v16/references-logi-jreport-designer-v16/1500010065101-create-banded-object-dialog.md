---
title: "Create Banded Object Dialog"
id: 1500010065101
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010065101-Create-Banded-Object-Dialog
updated_at: 2021-07-24T10:39:06Z
---

# Create Banded Object Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010065061-Connect-to-SQL-Server-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010030062-Create-Chart-Dialog)

# Create Banded Object Dialog

The Create Banded Object wizard helps you to [create a banded object](https://devnet.logianalytics.com/hc/en-us/articles/1500010063301-Inserting-a-Banded-Object) in a report. It appears when you select Insert > Banded Object.

The wizard varies with the data resource type used to create the banded object: [business view](#BV) or [query resource](#Query).

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

## Create Banded Object - Business View Based

When the wizard is used for creating a banded object using a business view, it consists of the following screens: [Data](#BVData), [Display](#BVDisplay), [Group](#BVGroup), [Summary](#BVSummary), [Filter](#BVFilter) and [Style](#BVStyle).

### Data

The screen lists all the predefined business views in the current catalog. Select the one using which to create the banded object.

![Create Banded Object - Data](https://devnet.logianalytics.com/hc/article_attachments/4404909237655/crtbdobj_dt_bv.gif)

### Display

Specifies the detail fields to display in the banded object.

![Create Banded Object - Display](https://devnet.logianalytics.com/hc/article_attachments/4404901283607/crtbdobj_dsply_bv.gif)

**Resources**

Lists the resources in and related to the specified business view, which can be used as detail fields in the banded object.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif)**

Adds the selected field in the Resources box to the banded object.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404901121047/btn_rmvarrow.gif)**

Removes the selected field from the banded object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif)

Moves the selected field one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif)

Moves the selected field one step down.

**Display Fields**

Lists the detail fields of the banded object.

**Display Name**

Specifies the labels of the detail columns in the banded object, which by default are the display names of the added fields. You can select in the text boxes to edit the labels, or check the Auto Map Field Name checkboxes in the text boxes to automatically map the label text to the dynamic display names of the fields at runtime.

**Sort Fields By**

Opens the [Sort Fields By](https://devnet.logianalytics.com/hc/en-us/articles/1500010067861-Sort-Fields-By-Dialog) dialog to specify how to sort the detail data in the banded object.

### Group

Specifies the criteria for grouping data in the banded object.

![Create Banded Object - Group](https://devnet.logianalytics.com/hc/article_attachments/4404909237911/crtbdobj_grp_bv.gif)

**Resources**

Lists the resources in and related to the specified business view, which can be used as group-by fields in the banded object.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif)

Adds the selected field in the Resources box as a group-by field in the banded object.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404901121047/btn_rmvarrow.gif)

Removes the selected group-by field from the banded object.

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

Specifies the summaries to calculate data in the banded object.

![Create Banded Object - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404909238167/crtbdobj_sum_bv.gif)

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

Specifies to filter data displayed in the banded object. The options in the screen are the same as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500010065601-Edit-Filter-Dialog) dialog.

![Create Banded Object - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404901283863/crtbdobj_fltr_bv.gif)

### Style

Specifies the style of the banded object.

![Create Banded Object - Style](https://devnet.logianalytics.com/hc/article_attachments/4404901284119/crtbdobj_sty_bv.gif)

**Grow Report**

Specifies the layout of the banded object.

* **Vertically**  
   Creates a vertical banded object.

**Style**

Specifies the style of the banded object.

**Preview**

Displays a diagram illustrating the effect of the selected style on the banded object.

**Inherit Style**

Specifies whether to make the banded object take the style of its parent. Available only when the banded object is to be inserted into another banded object in a page report.

## Create Banded Object - Query Based

When the wizard is used for creating a banded object using a query resource, it consists of the following screens: [Data](#Data), [Display](#Display), [Group](#Group), [Summary](#Summary), [Filter](#Filter) and [Style](#Layout).

### Data

Specifies the dataset using which to create the banded object.

![Create Banded Object - Data](https://devnet.logianalytics.com/hc/article_attachments/4404909238423/crtbdobj_dt.gif)

**Data resource box**

Lists the predefined data resources in the current catalog. Select one and a dataset based on it is created automatically for the banded object.

**More Options/Less Options**

Shows or hides the dataset selection panel to choose a dataset for the banded object.

* **New Dataset**  
   Specifies to create a dataset from the current catalog data resources. When a query is selected, you can select the Edit button to edit the query in the [Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500010067501-Query-Editor-Dialog) if required.
* **Existing Dataset**  
   Specifies to use a dataset from the ones existing in the current page report. Select the Edit button to edit the dataset in the [Dataset Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500010030342-Dataset-Editor-Dialog) if required.
* **Current Dataset**  
   Specifies to inherit the dataset used by the parent object.

### Display

Specifies the detail fields to display in the banded object.

![Create Banded Object - Display](https://devnet.logianalytics.com/hc/article_attachments/4404901284375/crtbdobj_dsply.gif)

**Resources**

Lists the resources in and related to the specified dataset, which can be used as detail fields in the banded object.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif)**

Adds the selected field in the Resources box to the banded object.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404901121047/btn_rmvarrow.gif)**

Removes the selected field from the banded object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif)

Moves the selected field one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif)

Moves the selected field one step down.

**Display Fields**

Lists the detail fields of the banded object.

**Display Name**

Specifies the labels of the detail columns in the banded object, which by default are the display names of the added fields. You can select in the text boxes to edit the labels if required.

**Sort Fields By**

Opens the [Sort Fields By](https://devnet.logianalytics.com/hc/en-us/articles/1500010067861-Sort-Fields-By-Dialog) dialog to specify how to sort the detail data in the banded object.

### Group

Specifies the criteria for grouping data in the banded object.

![Create Banded Object - Group](https://devnet.logianalytics.com/hc/article_attachments/4404901284887/crtbdobj_grp.gif)

**Resources**

Lists the resources in and related to the specified dataset, which can be used as group-by fields in the banded object.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif)

Adds the selected field in the Resources box as a group-by field in the banded object.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404901121047/btn_rmvarrow.gif)

Removes the selected group-by field from the banded object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif)

Moves the specified group one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif)

Moves the specified group one step down.

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

Specifies the fields on which to create summaries in the banded object.

![Create Banded Object - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404909238679/crtbdobj_sum.gif)

**Resources**

Lists the resources in and related to the specified dataset, which can be used to create summaries in the banded object.

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

### Filter

Specifies to filter data displayed in the banded object. The options in the screen are the same as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500010065601-Edit-Filter-Dialog) dialog.

![Create Banded Object - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404909239063/crtbdobj_fltr.gif)

### Style

Specifies the layout and style of the banded object.

![Create Banded Object - Style](https://devnet.logianalytics.com/hc/article_attachments/4404909239319/crtbdobj_sty.gif)

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010065061-Connect-to-SQL-Server-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010030062-Create-Chart-Dialog)
