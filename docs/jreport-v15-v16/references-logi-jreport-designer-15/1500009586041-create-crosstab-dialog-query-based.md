---
title: "Create Crosstab Dialog (Query Based)"
id: 1500009586041
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009586041-Create-Crosstab-Dialog-Query-Based
updated_at: 2021-07-24T05:55:32Z
---

# Create Crosstab Dialog (Query Based)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009586021-Create-Crosstab-Dialog-Business-View-Based-)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009586061-Create-Data-Mapping-File-Dialog)

# Create Crosstab Dialog (Query Based)

The Create Crosstab dialog that is based on query resource appears when you select Insert > Crosstab in a page report that is created using query resources. It helps you to [create a crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500009583881-Inserting-a-Crosstab#Page) in the page report, and consists of the following screens:

* [Data](#Data)
* [Display](#Display)
* [Filter](#Filter)
* [Layout](#Layout)
* [Style](#Style)

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

## Data

Specifies the dataset that you want to use to create the crosstab. [See the screen](javascript:%20void(null)).

![Create Crosstab wizard based on query - Data screen](https://devnet.logianalytics.com/hc/article_attachments/4404889377175/crtcrstab_dt.gif)

**Resource box**

Lists the available data resources in the current catalog. Select one to create the crosstab.

**More Options**/**Less Options**

Shows or hides the dataset selection panel to choose a dataset for the crosstab.

* **New Dataset**  
   If checked, select a data source from the catalog resources to create a dataset that will be used to build the crosstab. When you choose to create the dataset from a query, you can select the Edit button to edit the query in the [Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009567142-Query-Editor-Dialog) if required.
* **Existing Dataset**   
   If checked, select a dataset from the ones existing in the open report to create the crosstab. Select the Edit button to edit the dataset in the [Dataset Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009586301-Dataset-Editor-Dialog) if required.
* **Current Dataset**  
   If checked, the current dataset used by the parent object will be applied to the crosstab.

## Display

Specifies the fields that you want to display in the crosstab. [See the screen](javascript:%20void(null)).

![Create Crosstab wizard based on query - Display screen](https://devnet.logianalytics.com/hc/article_attachments/4404893939095/crtcrstab_dsply.gif)

**Resources**

Lists all the available data resources.

![Add Columns button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)

Adds the selected field to be displayed on the columns of the crosstab.

![Add Rows button](https://devnet.logianalytics.com/hc/article_attachments/4404889377431/btn_addrow.gif)

Adds the selected field to be displayed on the rows of the crosstab.

![Add Summaries button](https://devnet.logianalytics.com/hc/article_attachments/4404889377687/btn_addsum.gif)

Adds the selected field on which to create summaries.

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

## Filter

Specifies to filter data displayed in the crosstab. [See the screen](javascript:%20void(null)).

![Create Crosstab wizard based on query - Filter screen](https://devnet.logianalytics.com/hc/article_attachments/4404893940119/crtcrstab_fltr.gif)

The options in the screen are the same as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009565242-Edit-Filter-Dialog) dialog.

## Layout

Specifies the layout of the crosstab. [See the screen](javascript:%20void(null)).

![Create Crosstab wizard based on query - Layout screen](https://devnet.logianalytics.com/hc/article_attachments/4404889378583/crtcrstab_layout.gif)

For details about options in the screen, refer to [Customizing Crosstab Layout](https://devnet.logianalytics.com/hc/en-us/articles/1500009563322-Customizing-the-Crosstab-Layout).

## Style

Specifies the style of the crosstab. [See the screen](javascript:%20void(null)).

![Create Crosstab wizard based on query - Style screen](https://devnet.logianalytics.com/hc/article_attachments/4404889378839/crtcrstab_sty.gif)

**Style**

Specifies the style of the crosstab.

**Preview**

Shows a sketch of the selected style.

**Inherit Style**

Specifies whether to make the crosstab take the style of its parent. Available only when the crosstab is to be inserted into a banded object.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009586021-Create-Crosstab-Dialog-Business-View-Based-)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009586061-Create-Data-Mapping-File-Dialog)
