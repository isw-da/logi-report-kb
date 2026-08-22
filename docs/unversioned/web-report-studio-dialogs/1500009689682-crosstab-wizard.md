---
title: "Crosstab Wizard"
id: 1500009689682
section: "Web Report Studio Dialogs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009689682-Crosstab-Wizard
updated_at: 2021-11-03T06:57:27Z
---

# Crosstab Wizard

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009689662-Crosstab-Properties)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009715661-Cube-Status)

# Crosstab Wizard

The Crosstab Wizard helps you to change data of the crosstab, and contains the [Data](#Data) and  [Layout](#Layout) tabs.

This wizard appears when you do one of the following:

* Select a crosstab, then select Menu > Edit > Wizard.
* Select a crosstab, then select the Crosstab Wizard button ![Crosstab Wizard button](https://devnet.logianalytics.com/hc/article_attachments/4412131378455/btn_wbrpt_wizard.gif) on the visualization toolbar.
* Right-click the icon ![Drag icon](https://devnet.logianalytics.com/hc/article_attachments/4412139489175/btn_pgrpt_drag.gif) of a crosstab and select Crosstab Wizard from the shortcut menu.

**Crosstab Title**

Specifies a title for the crosstab.

![Font button](https://devnet.logianalytics.com/hc/article_attachments/4412131381399/btn_wbrpt_font.gif)

Specifies the font properties of the crosstab title.

* **Font**  
   Lists all the available font faces that can be selected to apply to the title.
* **Font Style**   
   Specifies the font style of the title. It can be one of the following: plain, bold, italic, and bold italic.
* **Size**  
   Specifies the font size of the title.
* **Align**  
   Specifies the position of the title to be left, right, center or justify.
* **Font Color**  
   Specifies the font color of the title.
* **Background Color**  
   Specifies the background color of the title.

**Data Source**

Displays the business view used by the crosstab.

**Filter**

Opens the [Query Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009716841-Query-Filter) dialog to specify the filter which you want to apply to the selected business view.

**OK**

Applies the changes and closes the wizard.

**Cancel**

Does not retain changes and closes the wizard.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4412139537431/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4412112572951/btn_close.gif)

Ignores the setting and closes this dialog.

## Data Tab

Specifies the column, row and aggregate fields to display in the crosstab.

![Crosstab Wizard - Data tab](https://devnet.logianalytics.com/hc/article_attachments/4412112493975/crstbwzd_data.gif)

**Resources**

Displays the view elements in the selected business view.

* ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4412112481943/btn_sort.gif)  
   Sorts the view elements in the specified order from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view elements are listed for this user.
  + **Predefined Order**  
     Sorts the view elements in the order defined in the Business View Editor on Logi JReport Designer.
  + **Resource Types**  
     Sorts the view elements by resource type, namely category objects come first, then group objects, then aggregation objects, and at last detail objects.
  + **Alphabetical Order**  
     Sorts the view elements in alphabetical order. Elements that are not in any category will be sorted first, then the categories, and the elements in each category will also be sorted alphabetically.
* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4412131375383/btn_srch.gif)  
   Launches the search bar to search for view elements. For the usage of the search bar, see [Search](https://devnet.logianalytics.com/hc/en-us/articles/1500009690702-Select-Resource#Search).

**Columns/Rows**

Specifies the column/row fields to display in the crosstab.

* **Field**  
   Lists the group objects that will be displayed in the columns/rows of the crosstab.
* **Label**  
   Specifies the text of the labels for the column/row headers. You can select the text boxes to edit the label text, or check the Auto Map Field Name checkboxes beside the text boxes to automatically map the label text to the dynamic display names of the objects.
* **Sort**  
   Specifies the sort order of the group objects.

**Summaries**

Specifies the aggregate fields to display in the crosstab.

* **Field**  
   Lists the aggregation/detail objects that you select to create summaries.
* **Label**  
   Specifies the text of the labels for the summaries. You can select the text boxes to edit the label text, or check the Auto Map Field Name checkboxes beside the text boxes to automatically map the label text to the dynamic display names of the objects.
* **Aggregate**  
   Specifies the functions used to summarize data of the detail objects.
* **Distinct On**  
  Available and should be set when DistinctSum is selected as the aggregate function. It specifies the detail objects according to whose unique values to calculate DistinctSum. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4412112493207/btn_chsr.gif) to select the detail objects in the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009716981-Select-Fields) dialog.
* **Comparison Function**  
   Opens the [Comparison Function](https://devnet.logianalytics.com/hc/en-us/articles/1500009715701-Comparison-Function) dialog to add a comparison function as an aggregate for the crosstab.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4412131391639/btn_additem.gif)

Adds the selected group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4412112493463/btn_bvgrp.gif) to be displayed on the columns of the crosstab.

![](https://devnet.logianalytics.com/hc/article_attachments/4412131392151/btn_addrow.gif)

Adds the selected group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4412112493463/btn_bvgrp.gif) to be displayed on the rows of the crosstab.

![](https://devnet.logianalytics.com/hc/article_attachments/4412112504343/btn_addsum.gif)

Adds the selected aggregation object ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4412131382167/btn_bvaggrgtn.gif) or detail object ![Detail Object](https://devnet.logianalytics.com/hc/article_attachments/4412139491991/btn_bvdtl.gif) to be the summary field of the crosstab.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4412112497431/btn_mvup.gif)

Moves the selected view element one level up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4412112497687/btn_mvdown.gif)

Moves the selected view element one level down.

![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4412112484759/btn_delete.gif)

Removes the selected resource.

## Layout Tab

Specifies the layout of the crosstab.

![Crosstab Wizard -  Layout tab](https://devnet.logianalytics.com/hc/article_attachments/4412139559703/crstbwzd_layout.gif)

**Aggregate**

Specifies properties of the aggregate fields.

* **Vertical Layout**  
   If selected, the aggregate fields will be arranged vertically.
  + **Number of Rows**  
     Specifies the number of rows to hold the aggregate fields in the crosstab. By default, it is -1 which means that each aggregate field is placed in a row so that the aggregate fields are positioned in one column vertically. 0 and a number equal to or larger than the number of aggregate fields in the crosstab are treated as -1. If you set the number of rows (3 for example) less than the number of aggregate fields (6 for example), there will be 3 rows to hold the 6 fields with each row containing 2 fields.
* **Horizontal Layout**  
   If selected, the aggregate fields will be arranged horizontally. When you have multiple aggregate fields in the crosstab, using horizontal layout can make the report more readable.
  + **Number of Columns**  
     Specifies the number of columns to hold the aggregate fields in the crosstab. By default, it is -1 which means that each aggregate field is placed in a column so that the aggregate fields are positioned in one row horizontally. 0 and a number equal to or larger than the number of aggregate fields in the crosstab are treated as -1. If you set the number of columns (3 for example) less than the number of aggregate fields (6 for example), there will be 3 columns to hold the 6 fields with each column containing 2 fields.

**Suppress Row Grand Totals**

Specifies whether or not to show the grand total row in the crosstab.

**Suppress Column Grand Totals**

Specifies whether or not to show the grand total column in the crosstab.

**Suppress Row Subtotals**

Specifies whether or not to show the subtotals of the row fields in the crosstab. You can select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4412139533719/btn_chsr4.gif) to customize which subtotals of the row fields will be suppressed and which will be shown in the [Suppress Row Subtotals](https://devnet.logianalytics.com/hc/en-us/articles/1500009717041-Suppress-Row-Subtotals) dialog.

**Suppress Column Subtotals**

Specifies whether or not to show the subtotals of the column fields in the crosstab. You can select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4412139533719/btn_chsr4.gif) to customize which subtotals of the column fields will be suppressed and which will be shown in the [Suppress Column Subtotals](https://devnet.logianalytics.com/hc/en-us/articles/1500009690762-Suppress-Column-Subtotals) dialog.

**Column Totals On**

Specifies the position of subtotal and grand total columns on the left or right of the detail aggregations.

**Row Totals On**

Specifies the position of subtotal and grand total rows on the top or bottom of the detail aggregations.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009689662-Crosstab-Properties)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009715661-Cube-Status)
