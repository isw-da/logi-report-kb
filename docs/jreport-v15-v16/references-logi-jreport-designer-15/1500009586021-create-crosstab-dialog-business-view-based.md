---
title: "Create Crosstab Dialog (Business View Based)"
id: 1500009586021
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009586021-Create-Crosstab-Dialog-Business-View-Based
updated_at: 2021-07-24T05:55:33Z
---

# Create Crosstab Dialog (Business View Based)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009586001-Create-Connection-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009586041-Create-Crosstab-Dialog-Query-Based-)

# Create Crosstab Dialog (Business View Based)

The Create Crosstab dialog that is based on business view appears when you select Insert > Crosstab, or drag the Crosstab button from the Components panel into a report that is created using business views. It helps you to [create a crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500009583881-Inserting-a-Crosstab#Web) in the report, and consists of the following screens:

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

Specifies the data source that you want to use to create the crosstab. [See the screen](javascript:%20void(null)).

![Create Crosstab wizard based on business view - Data screen](https://devnet.logianalytics.com/hc/article_attachments/4404889379095/crtcrstab_dt_wb.gif)

**Resources**

Lists all the business views in the current catalog. Specify the one you want to use.

## Display

Specifies the fields that you want to display in the crosstab. [See the screen](javascript:%20void(null)).

![Create Crosstab wizard based on business view - Display screen](https://devnet.logianalytics.com/hc/article_attachments/4404889379351/crtcrstab_dsply_wb.gif)

**Title**

Specifies the title of the crosstab.

**Resources**

Lists all the available data resources. You can also [create dynamic formulas and aggregations](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Dynamic) to use in the crosstab.

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

Moves the specified field one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404893939863/btn_mvdwn1.gif)

Moves the specified field one step down.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)

Removes the specified field that is not required from the crosstab.

## Filter

Specifies to filter data displayed in the crosstab. [See the screen](javascript:%20void(null)).

![Create Crosstab wizard based on business view - Filter screen](https://devnet.logianalytics.com/hc/article_attachments/4404893940375/crtcrstab_fltr_wb.gif)

The options in the screen are the same as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009565242-Edit-Filter-Dialog) dialog.

## Layout

Specifies the layout of the crosstab. [See the screen](javascript:%20void(null)).

![Create Crosstab wizard based on business view - Layout screen](https://devnet.logianalytics.com/hc/article_attachments/4404889378583/crtcrstab_layout.gif)

For details about options in the screen, refer to [Customizing Crosstab Layout](https://devnet.logianalytics.com/hc/en-us/articles/1500009563322-Customizing-the-Crosstab-Layout).

## Style

Specifies the style of the crosstab. [See the screen](javascript:%20void(null)).

![Create Crosstab wizard based on business view - Style screen](https://devnet.logianalytics.com/hc/article_attachments/4404893940631/crtcrstab_sty_wb.gif)

**Style**

Specifies the style of the crosstab.

**Preview**

Shows a sketch of the selected style.

**Inherit Style**

Specifies whether to make the crosstab take the style of its parent. This options is available only when the crosstab is inserted in a banded object in a page report.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009586001-Create-Connection-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009586041-Create-Crosstab-Dialog-Query-Based-)
