---
title: "Crosstab Wizard Dialog"
id: 1500009630181
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009630181-Crosstab-Wizard-Dialog
updated_at: 2021-07-24T16:04:55Z
---

# Crosstab Wizard Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009607482-Crosstab-Formula-Editor-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009630301-CSS-Editor-Dialog)

# Crosstab Wizard Dialog

The Crosstab Wizard helps you to [create a page report tab with a crosstab in it](https://devnet.logianalytics.com/hc/en-us/articles/1500009613262-Creating-Reports#Page), [create a library component with a crosstab in it,](https://devnet.logianalytics.com/hc/en-us/articles/1500009613262-Creating-Reports#LC) or [edit an existing crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500009629061-Modifying-Crosstabs#Edit) in a report.

The wizard varies with the data resource type used by the crosstab: [business view](#BV) or [query resource](#Query).

**Back**

Goes back to the previous screen.

**Next**

Goes to the next screen.

**Finish**

Finishes creating or editing the crosstab and closes this wizard.

**Cancel**

Does not retain changes and closes this wizard.

**Help**

Displays the help document about this feature.

## Crosstab Wizard - Business View Based

When the wizard is used for creating or editing a crosstab using a business view, it consists of the following screens: [Data](#BVData), [Display](#BVDisplay), [Filter](#BVFilter)， [Layout](#BVLayout) and [Style](#BVStyle). The Filter screen is available only when the wizard is used for creating a crosstab.

### Data

The screen lists all the predefined business views in the current catalog. Select the one you want to use for the crosstab.

![Crosstab Wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404916814487/crstbwzd_dt_bv.gif)

**Inherit from the Parent**

Specifies to inherit data from the business view used by the parent object. Available only when the crosstab is in any of the following panels in a banded object in a web report: banded header panel, banded footer panel, group header panel and group footer panel.

### Display

Specifies the column, row and aggregate fields to display in the crosstab.

![Crosstab Wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4404916814743/crstbwzd_dsply_bv.gif)

**Title**

Specifies the title of the crosstab.

**Resources**

Lists the resources in and related to the specified business view, which can be used to create or edit the crosstab.

![Add Columns button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif)

Adds the selected field in the Resources box to display on the column header of the crosstab.

![Add Rows button](https://devnet.logianalytics.com/hc/article_attachments/4404904372247/btn_addrow.gif)

Adds the selected field in the Resources box to display on the row header of the crosstab.

![Add Summaries button](https://devnet.logianalytics.com/hc/article_attachments/4404904372631/btn_addsum.gif)

Adds the selected field in the Resources box to create aggregations in the crosstab.

**Columns/Rows**

* **Field**  
   Lists the fields that will be displayed on the column/row headers of the crosstab.
* **Label**  
   Specifies the text of the labels for the column/row headers. By default no labels will be created for the column/row headers. double-click the text boxes to edit the label text, or select the Auto Map Field Name checkboxes in the text boxes to automatically map the label text to the dynamic display names of the fields at runtime.
* **Color**  
   Specifies the background color of the fields.

**Summaries**

* **Field**  
   Lists the fields added as aggregate fields to create aggregations in the crosstab.
* **Aggregate**  
   Specifies the [functions](https://devnet.logianalytics.com/hc/en-us/articles/1500009611182-Summaries#Function) used to calculate data of the fields.
* **Distinct On**  
   Available and should be set when DistinctSum is selected as the aggregate function. It specifies the fields according to whose unique values to calculate DistinctSum. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904178967/btn_chsr.gif) in the text box to select the required fields in the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009633521-Select-Fields-Dialog) dialog.
* **Label**  
   Specifies the text of the labels for the aggregations. By default no labels will be created for the aggregations. double-click the text boxes to edit the label text, or select the Auto Map Field Name checkboxes in the text boxes to automatically map the label text to the dynamic display names of the fields at runtime.
* **Comparison Function**  
   Opens the [Comparison Function](https://devnet.logianalytics.com/hc/en-us/articles/1500009607422-Comparison-Function-Dialog) dialog to add a comparison function for the selected aggregate field.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404904373143/btn_sort1.gif)

Specifies in which manner to sort the field values.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif)

Moves the specified field one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif)

Moves the specified field one step down.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif)

Removes the specified field from the crosstab.

### Filter

Specifies to filter data displayed in the crosstab. This screen is available only when you create a crosstab, and it contains the same options as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009607882-Edit-Filter-Dialog) dialog.

![Crosstab Wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404904382615/crstbwzd_fltr_bv.gif)

### Layout

Specifies the layout of the crosstab. For details about options in the screen, refer to [Customizing the layout of a crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500009629061-Modifying-Crosstabs#Layout).

![Crosstab Wizard - Layout](https://devnet.logianalytics.com/hc/article_attachments/4404904382871/crstbwzd_layout_bv.gif)

### Style

Specifies the style of the crosstab.

![Crosstab Wizard - Style](https://devnet.logianalytics.com/hc/article_attachments/4404904383127/crstbwzd_sty_bv.gif)

**Style**

Specifies the style of the crosstab.

* **<Custom>**  
   There is no style information on it and it is only used to support reports built with previous versions which did not bind any style or the bound style cannot be found in the style list.

**Preview**

Shows a sketch of the selected style.

**Inherit Style**

Specifies whether to make the crosstab take the style of its parent. Available only when the crosstab is inserted in a banded object in a page report.

**Page Setup**

Opens the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009609582-Page-Setup-Dialog) dialog to specify page properties. Available only when you create a crosstab in a page report.

## Crosstab Wizard - Query Based

When the wizard is used for creating or editing a crosstab using a query resource, it consists of the following screens: [Data](#Data), [Display](#Display), [Chart](#Chart), [Filter](#Filter)， [Layout](#Layout) and [Style](#Style). Some screens are available only when the wizard is used for creating a crosstab.

### Data

Specifies the dataset of the crosstab.

![Crosstab Wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404904383383/crstbwzd_dt.gif)

**Data resource box**

Lists the predefined data resources in the current catalog. Select one and a dataset based on it is created automatically for the crosstab.

**More Options**/**Less Options**

Shows or hides the dataset selection panel to choose a dataset for the crosstab.

* **New Dataset**  
   Specifies to create a dataset from the current catalog data resources. When a query is selected, you can select the Edit button to edit the query in the [Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009609882-Query-Editor-Dialog).
* **Existing Dataset**  
   Specifies to use a dataset from the ones existing in the current page report. You can select the Edit button to edit the dataset in the [Dataset Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009607762-Dataset-Editor-Dialog).
* **Current Dataset**  
   Specifies to inherit the dataset used by the parent object.

### Display

Specifies the column, row and aggregate fields to display in the crosstab.

![Crosstab Wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4404916814999/crstbwzd_dsply.gif)

**Resources**

Lists the data fields in and related to the specified query resource, which can be used to create or edit the crosstab.

![Add Columns button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif)

Adds the selected field in the Resources box to display on the column header of the crosstab.

![Add Rows button](https://devnet.logianalytics.com/hc/article_attachments/4404904372247/btn_addrow.gif)

Adds the selected field in the Resources box to display on the row header of the crosstab.

![Add Summaries button](https://devnet.logianalytics.com/hc/article_attachments/4404904372631/btn_addsum.gif)

Adds the selected field in the Resources box on which to create aggregations in the crosstab.

**Columns/Rows**

* **Field**  
   Lists the fields that will be displayed on the column/row headers of the crosstab.
* **Label**  
   Specifies the labels for the column/row headers. By default no labels will be created for the column/row headers. double-click the text boxes to edit the labels.
* **Color**  
   Specifies the background color of the fields.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904375447/btn_addparal.gif)  
   Adds a compound column/row group.

**Summaries**

* **Field**  
   Lists the fields added as aggregate fields to create aggregations in the crosstab.
* **Aggregate**  
   Specifies the [functions](https://devnet.logianalytics.com/hc/en-us/articles/1500009611182-Summaries#Function) used to calculate data of the fields.
* **Distinct On**  
   Available and should be set when DistinctSum is selected as the aggregate function. It specifies the fields according to whose unique values to calculate DistinctSum. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904178967/btn_chsr.gif) in the text box to select the required fields in the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009633521-Select-Fields-Dialog) dialog.
* **Label**  
   Specifies the labels for the aggregations. By default no labels will be created for the aggregations. double-click the text boxes to edit the labels.
* **Comparison Function**  
   Opens the [Comparison Function](https://devnet.logianalytics.com/hc/en-us/articles/1500009607422-Comparison-Function-Dialog) dialog to add a comparison function for the selected aggregate field.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404904373143/btn_sort1.gif)

Specifies in which manner to sort the field values.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif)

Moves the selected field or compound group one step up. For fields in a compound group, their order can be changed within the current group only.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif)

Moves the selected field or compound group one step down. For fields in a compound group, their order can be changed within the current group only.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif)

Removes the selected field or compound group from the crosstab.

### Chart

Specifies to create a chart together with the crosstab, which will be placed above the crosstab in the report body. This screen is available only when you create a crosstab, and when there is at least one field inserted on the column or row headers and one aggregate field added in the crosstab.

![Crosstab Wizard - Chart](https://devnet.logianalytics.com/hc/article_attachments/4404904383767/crstbwzd_cht.gif)

**No Chart**

Specifies not to create a chart.

**Bar Chart**

Specifies to create a Clustered Bar 2-D chart together with the crosstab.

**Line Chart**

Specifies to create a Line 2-D chart together with the crosstab.

**Pie Chart**

Specifies to create a Clustered Pie chart together with the crosstab.

**Category**

Lists the fields that have been added to the column and row headers of the crosstab. Choose the field you want to display on the category (X) axis of the chart from the drop-down list.

**Series**

Lists the fields that have been added to the column and row headers of the crosstab. Choose the field you want to display on the series (Z) axis of the chart from the drop-down list.

**Show Values**

Lists the fields that have been added as aggregate field in the crosstab. Choose the value you want to display in the chart from the drop-down list.

### Filter

Specifies to filter data displayed in the crosstab. This screen is available only when you create a crosstab, and it contains the same options as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009607882-Edit-Filter-Dialog) dialog.

![Crosstab Wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404904384023/crstbwzd_fltr.gif)

### Layout

Specifies the layout of the crosstab. For details about the layout settings, refer to [Customizing the layout of a crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500009629061-Modifying-Crosstabs#Layout).

![Crosstab Wizard - Layout](https://devnet.logianalytics.com/hc/article_attachments/4404904384407/crstbwzd_layout.gif)

### Style

Specifies the style of the crosstab.

![Crosstab Wizard - Style](https://devnet.logianalytics.com/hc/article_attachments/4404916815255/crstbwzd_sty.gif)

**Style**

Specifies the style of the crosstab.

* **<Custom>**  
   There is no style information on it and it is only used to support reports built with previous versions which did not bind any style or the bound style cannot be found in the style list.

**Preview**

Shows a sketch of the selected style.

**Inherit Style**

Specifies whether to make the crosstab take the style of its parent. Available only when you edit a crosstab and the crosstab is to be inserted into a banded object.

**Page Setup**

Opens the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009609582-Page-Setup-Dialog) dialog to specify page properties. Available only when creating a crosstab.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009607482-Crosstab-Formula-Editor-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009630301-CSS-Editor-Dialog)
