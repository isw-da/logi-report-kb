---
title: "Create Crosstab Dialog"
id: 1500010030102
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010030102-Create-Crosstab-Dialog
updated_at: 2021-07-24T10:39:04Z
---

# Create Crosstab Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010030082-Create-Connection-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010030122-Create-Data-Mapping-File-Dialog)

# Create Crosstab Dialog

The Create Crosstab wizard helps you to [create a crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500010063721-Inserting-Crosstabs-in-a-Report) in a report. It appears when you select Insert > Crosstab, or drag the Crosstab button from the Components panel into a report.

The wizard varies with the data resource type used to create the crosstab: [business view](#BV) or [query resource](#Query).

**Back**

Goes back to the previous screen.

**Next**

Goes to the next screen.

**Finish**

Finishes creating the crosstab and closes this dialog.

**Cancel**

Does not retain changes and closes this dialog.

**Help**

Displays the help document about this feature.

## Create Crosstab - Business View Based

When the wizard is used for creating a crosstab using a business view, it consists of the following screens: [Data](#BVData), [Display](#BVDisplay), [Filter](#BVFilter), [Layout](#BVLayout) and [Style](#BVStyle).

### Data

The screen lists all the predefined business views in the current catalog. Select the one using which to create the crosstab.

![Create Crosstab - Data](https://devnet.logianalytics.com/hc/article_attachments/4404901279639/crtcrstab_dt_bv.gif)

**Inherit from the Parent**

Specifies to inherit data from the business view used by the parent object. Available only when the crosstab is to be inserted into any of the following panels in a banded object in a web report: banded header panel, banded footer panel, group header panel and group footer panel.

### Display

Specifies the column, row and aggregate fields to display in the crosstab.

![Create Crosstab - Display](https://devnet.logianalytics.com/hc/article_attachments/4404901279895/crtcrstab_dsply_bv.gif)

**Title**

Specifies the title of the crosstab.

**Resources**

Lists the resources in and related to the specified business view, which can be used to create the crosstab.

![Add Columns button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif)

Adds the selected field in the Resources box to display on the column header of the crosstab.

![Add Rows button](https://devnet.logianalytics.com/hc/article_attachments/4404901280151/btn_addrow.gif)

Adds the selected field in the Resources box to display on the row header of the crosstab.

![Add Summaries button](https://devnet.logianalytics.com/hc/article_attachments/4404901280407/btn_addsum.gif)

Adds the selected field in the Resources box to create aggregations in the crosstab.

**Columns/Rows**

* **Field**  
   Lists the fields that will be displayed on the column/row headers of the crosstab.
* **Label**  
   Specifies the text of the labels for the column/row headers. By default no labels will be created for the column/row headers. double-click the text boxes to edit the label text, or check the Auto Map Field Name checkboxes in the text boxes to automatically map the label text to the dynamic display names of the fields at runtime.
* **Color**  
   Specifies the background color of the fields.

**Summaries**

* **Field**  
   Lists the fields added as aggregate fields to create aggregations in the crosstab.
* **Aggregate**  
   Specifies the [functions](https://devnet.logianalytics.com/hc/en-us/articles/1500010068581-Summaries#Function) used to calculate data of the fields.
* **Distinct On**  
   Available and should be set when DistinctSum is selected as the aggregate function. It specifies the fields according to whose unique values to calculate DistinctSum. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404901122967/btn_chsr.gif) in the text box to select the required fields in the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500010032562-Select-Fields-Dialog) dialog.
* **Label**  
   Specifies the text of the labels for the aggregations. By default no labels will be created for the aggregations. double-click the text boxes to edit the label text, or check the Auto Map Field Name checkboxes in the text boxes to automatically map the label text to the dynamic display names of the fields at runtime.
* **Comparison Function**  
   Opens the [Comparison Function](https://devnet.logianalytics.com/hc/en-us/articles/1500010064961-Comparison-Function-Dialog) dialog to add a comparison function for the selected aggregate field.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404909234583/btn_sort1.gif)

Specifies in which manner to sort the field values.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif)

Moves the specified field one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif)

Moves the specified field one step down.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif)

Removes the specified field from the crosstab.

### Filter

Specifies to filter data displayed in the crosstab. The options in the screen are the same as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500010065601-Edit-Filter-Dialog) dialog.

![Create Crosstab - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404901280663/crtcrstab_fltr_bv.gif)

### Layout

Specifies the layout of the crosstab. For details about the layout settings, refer to [Customizing the layout of a crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500010063741-Modifying-Crosstabs#Layout).

![Create Crosstab - Layout](https://devnet.logianalytics.com/hc/article_attachments/4404901280919/crtcrstab_layout.gif)

### Style

Specifies the style of the crosstab.

![Create Crosstab - Style](https://devnet.logianalytics.com/hc/article_attachments/4404901281175/crtcrstab_sty.gif)

**Style**

Specifies the style of the crosstab.

**Preview**

Shows a sketch of the selected style.

**Inherit Style**

Specifies whether to make the crosstab take the style of its parent. Available only when the crosstab is inserted in a banded object in a page report.

## Create Crosstab - Query Based

When the wizard is used for creating a crosstab using a query resource, it consists of the following screens: [Data](#Data), [Display](#Display), [Filter](#Filter), [Layout](#Layout) and [Style](#Style).

### Data

Specifies the dataset using which to create the crosstab.

![Create Crosstab - Data](https://devnet.logianalytics.com/hc/article_attachments/4404909234839/crtcrstab_dt.gif)

**Resource box**

Lists the predefined data resources in the current catalog. Select one and a dataset based on it is created automatically for the crosstab.

**More Options**/**Less Options**

Shows or hides the dataset selection panel to choose a dataset for the crosstab.

* **New Dataset**  
   Specifies to create a dataset from the current catalog data resources. When a query is selected, you can select the Edit button to edit the query in the [Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500010067501-Query-Editor-Dialog) if required.
* **Existing Dataset**  
   Specifies to use a dataset from the ones existing in the current page report. Select the Edit button to edit the dataset in the [Dataset Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500010030342-Dataset-Editor-Dialog) if required.
* **Current Dataset**  
   Specifies to inherit the dataset used by the parent object.

### Display

Specifies the column, row and aggregate fields to display in the crosstab.

![Create Crosstab - Display](https://devnet.logianalytics.com/hc/article_attachments/4404909235095/crtcrstab_dsply.gif)

**Resources**

Lists the resources in and related to the specified query resource, which can be used to create the crosstab.

![Add Columns button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif)

Adds the selected field in the Resources box to display on the column header of the crosstab.

![Add Rows button](https://devnet.logianalytics.com/hc/article_attachments/4404901280151/btn_addrow.gif)

Adds the selected field in the Resources box to display on the row header of the crosstab.

![Add Summaries button](https://devnet.logianalytics.com/hc/article_attachments/4404901280407/btn_addsum.gif)

Adds the selected field in the Resources box on which to create aggregations in the crosstab.

**Columns/Rows**

* **Field**  
   Lists the fields that will be displayed on the column/row headers of the crosstab.
* **Label**  
   Specifies the labels for the column/row headers. By default no labels will be created for the column/row headers. double-click the text boxes to edit the labels.
* **Color**  
   Specifies the background color of the fields.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404909235351/btn_addparal.gif)  
   Adds a compound column/row group.

**Summaries**

* **Field**  
   Lists the fields added as aggregate fields to create aggregations in the crosstab.
* **Aggregate**  
   Specifies the [functions](https://devnet.logianalytics.com/hc/en-us/articles/1500010068581-Summaries#Function) used to calculate data of the fields.
* **Distinct On**  
   Available and should be set when DistinctSum is selected as the aggregate function. It specifies the fields according to whose unique values to calculate DistinctSum. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404901122967/btn_chsr.gif) in the ext box to select the required fields in the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500010032562-Select-Fields-Dialog) dialog.
* **Label**  
   Specifies the labels for the aggregations. By default no labels will be created for the aggregations. double-click the text boxes to edit the labels.
* **Comparison Function**  
   Opens the [Comparison Function](https://devnet.logianalytics.com/hc/en-us/articles/1500010064961-Comparison-Function-Dialog) dialog to add a comparison function for the selected aggregate field.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404909234583/btn_sort1.gif)

Specifies in which manner to sort the field values.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif)

Moves the selected field or compound group one step up. For fields in a compound group, their order can be changed within the current group only.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif)

Moves the selected field or compound group one step down. For fields in a compound group, their order can be changed within the current group only.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif)

Removes the selected field or compound group from the crosstab.

### Filter

Specifies to filter data displayed in the crosstab. The options in the screen are the same as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500010065601-Edit-Filter-Dialog) dialog.

![Create Crosstab - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404909235607/crtcrstab_fltr.gif)

### Layout

Specifies the layout of the crosstab. For details about the layout settings, refer to [Customizing the layout of a crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500010063741-Modifying-Crosstabs#Layout).

![Create Crosstab - Layout](https://devnet.logianalytics.com/hc/article_attachments/4404901280919/crtcrstab_layout.gif)

### Style

Specifies the style of the crosstab.

![Create Crosstab - Style](https://devnet.logianalytics.com/hc/article_attachments/4404901281175/crtcrstab_sty.gif)

**Style**

Specifies the style of the crosstab.

**Preview**

Shows a sketch of the selected style.

**Inherit Style**

Specifies whether to make the crosstab take the style of its parent. Available only when the crosstab is to be inserted into a banded object.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010030082-Create-Connection-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010030122-Create-Data-Mapping-File-Dialog)
