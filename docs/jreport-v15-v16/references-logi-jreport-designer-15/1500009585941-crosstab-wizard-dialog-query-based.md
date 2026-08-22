---
title: "Crosstab Wizard Dialog (Query Based)"
id: 1500009585941
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009585941-Crosstab-Wizard-Dialog-Query-Based
updated_at: 2021-07-24T05:55:33Z
---

# Crosstab Wizard Dialog (Query Based)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564862-Crosstab-Wizard-Dialog-Business-View-Based-)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009586141-CSS-Editor-Dialog)

# Crosstab Wizard Dialog (Query Based)

The Crosstab Wizard dialog that is based on query resource helps you to [create](https://devnet.logianalytics.com/hc/en-us/articles/1500009592821-Creating-a-Page-Report) or [modify](https://devnet.logianalytics.com/hc/en-us/articles/1500009583901-Modifying-a-Crosstab) a crosstab based on a query resource in a page report. It appears when you do either of the following:

* In the [Select Component for Page Report Tab](https://devnet.logianalytics.com/hc/en-us/articles/1500009588661-Select-Component-for-Page-Report-Tab-Dialog) dialog or [Select Component for Page Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009567422-Select-Component-for-Page-Report-Dialog) dialog, select the Crosstab component and then select OK.
* Right-click a crosstab created on a query and select Crosstab Wizard on the shortcut menu.

The wizard consists of the following screens:

* [Data](#Data)
* [Display](#Display)
* [Chart](#Chart)
* [Filter](#Filter)
* [Layout](#Layout)
* [Style](#Style)

**Back**

Goes back to the previous screen.

**Next**

Goes to the next screen.

**Finish**

Finishes creating or modifying the crosstab and closes this wizard.

**Cancel**

Does not retain changes and closes this wizard.

**Help**

Displays the help document about this feature.

## Data

Specifies the dataset for the crosstab. [See the screen](javascript:%20void(null)).

![Crosstab Wizard for Page Report - Data](https://devnet.logianalytics.com/hc/article_attachments/4404893945879/crstbwzd_dt.gif)

**Resource box**

Lists the available data resources in the current catalog. Select one to create the crosstab.

**More Options**/**Less Options**

Shows or hides the dataset selection panel to choose a dataset for the crosstab.

* **New Dataset**   
   If checked, select a data source from the catalog resources to create a dataset that will be used to build the crosstab. When you choose to create the dataset from a query, you can select the Edit button to edit the query in the [Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009567142-Query-Editor-Dialog) if required.
* **Existing****Dataset**  
   If checked, select a dataset from the ones existing in the open report to create the crosstab. Select the Edit button to edit the dataset in the [Dataset Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009586301-Dataset-Editor-Dialog) if required.
* **Current****Dataset**  
   If checked, the current dataset used by the parent object will be applied to the crosstab.

## Display

Specifies the fields to display in the crosstab. [See the screen](javascript:%20void(null)).

![Crosstab Wizard for Page Report - Display](https://devnet.logianalytics.com/hc/article_attachments/4404893946135/crstbwzd_dsply.gif)

**Resources**

Lists all the available data resources.

![Add Columns button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)

Adds the selected field to be displayed on the columns of the crosstab.

![Add Rows button](https://devnet.logianalytics.com/hc/article_attachments/4404889377431/btn_addrow.gif)

Adds the selected field to be displayed on the rows of the crosstab.

![Add Summaries button](https://devnet.logianalytics.com/hc/article_attachments/4404889377687/btn_addsum.gif)

Adds the selected field on which to create summaries.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404889314711/btn_replace.gif)

Replaces the selected field in the crosstab with the specified field in the Resources box.

**Columns/Rows**

* **Field**  
   Lists the fields that will be displayed on the columns/rows of the crosstab.
* **Label**  
   Specifies the display names for the selected fields. By default these are blank and no names will be created for the fields to label the columns/rows. You can double-click the cells to edit them if required.
* **Color**  
   Specifies the background color of the selected fields.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404889377943/btn_addparal.gif)  
  Adds a compound column/row group.

**Summaries**

* **Field**  
   Lists the fields that you select to create summaries.
* **Aggregate**  
   Specifies the functions used to summarize data of the selected fields. For details about each function, see [Math functions](https://devnet.logianalytics.com/hc/en-us/articles/1500009589541-Math-Functions).
* **Label**  
   Specifies the display names for the selected fields. By default these are blank and no names will be created for the fields to label the summaries. You can double-click the cells to edit them if required.
* **Comparison Function**  
   Opens the [Comparison Function](https://devnet.logianalytics.com/hc/en-us/articles/1500009585881-Comparison-Function-Dialog) dialog to add a comparison function as an aggregate for the crosstab.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404893939351/btn_sort1.gif)

Specifies in which manner to sort the field values.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893939607/btn_mvup1.gif)

Moves the selected field or compound group one step up. For fields in a compound group, their order can be changed within the current group only.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404893939863/btn_mvdwn1.gif)

Moves the selected field or compound group one step down. For fields in a compound group, their order can be changed within the current group only.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)

Removes the selected field or compound group that is not required from the crosstab.

## Chart

Specifies to create a chart together with the crosstab, which will be placed above the crosstab in the report body. This screen is available only when you create a crosstab, and when there is at least one field inserted in the columns or rows, and with at least one summary field in the crosstab. [See the screen](javascript:%20void(null)).

![Crosstab Wizard for Page Report - Chart](https://devnet.logianalytics.com/hc/article_attachments/4404893805335/crstbwzd_cht.gif)

**No Chart**

Specifies not to create a chart.

**Bar Chart**

Specifies to create a Clustered Bar 2-D chart together with the crosstab.

**Line Chart**

Specifies to create a Line 2-D chart together with the crosstab.

**Pie Chart**

Specifies to create a Clustered Pie chart together with the crosstab.

**Category**

Lists the fields that have been added to the columns and rows of the crosstab. Choose the field you want to display on the category (X) axis of the chart from the drop-down list.

**Series**

Lists the fields that have been added to the columns and rows of the crosstab. Choose the field you want to display on the series (Z) axis of the chart from the drop-down list.

**Show Values**

Lists the fields that have been selected to create summaries in the crosstab. Choose the value you want to display in the chart from the drop-down list.

## Filter

Specifies to filter data displayed in the crosstab. This screen is available only when you create a crosstab. [See the screen](javascript:%20void(null)).

![Crosstab Wizard for Page Report - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404893946391/crstbwzd_fltr.gif)

The options in the screen are the same as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009565242-Edit-Filter-Dialog) dialog.

## Layout

Specifies the layout of the crosstab. [See the screen](javascript:%20void(null)).

![Crosstab Wizard for Page Report - Layout](https://devnet.logianalytics.com/hc/article_attachments/4404893946647/crstbwzd_layout.gif)

For details about options in the screen, refer to [Customizing Crosstab Layout](https://devnet.logianalytics.com/hc/en-us/articles/1500009563322-Customizing-the-Crosstab-Layout).

## Style

Specifies the style of the crosstab. [See the screen](javascript:%20void(null)).

![Style](https://devnet.logianalytics.com/hc/article_attachments/4404893946903/crstbwzd_sty.gif)

**Style**

Specifies the style of the crosstab.

* **<Custom>**  
   There is no style information on it and it is only used to support reports built with previous versions which did not bind any style or the bound style cannot be found in the style list.

**Preview**

Displays a diagram illustrating the effect of the selected style on the crosstab.

**Inherit Style**

Specifies whether to make the crosstab take the style of its parent. This options is available only when you modify a crosstab and the crosstab is inserted into a banded object.

**Page Setup**

Opens the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009588121-Page-Setup-Dialog) dialog to specify page properties. Available only when creating a crosstab.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564862-Crosstab-Wizard-Dialog-Business-View-Based-)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009586141-CSS-Editor-Dialog)
