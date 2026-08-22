---
title: "Crosstab Wizard Properties"
id: 1500009775081
section: "Web Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009775081-Crosstab-Wizard-Properties
updated_at: 2021-07-24T00:48:33Z
---

# Crosstab Wizard Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746862-Crosstab-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009774981-Cube-Status-Dialog-Box-Properties)

# Crosstab Wizard Properties

This topic describes how you can use Crosstab Wizard to change data of a crosstab.

Server displays the wizard when you do one of the following:

* Select a crosstab, then select Menu > Edit > Wizard.
* Select a crosstab, then select the Crosstab Wizard button ![Crosstab Wizard button](https://devnet.logianalytics.com/hc/article_attachments/4404885314711/btn_wbrpt_wizard.gif) on the visualization toolbar.
* Right-click the icon ![Drag icon](https://devnet.logianalytics.com/hc/article_attachments/4404880145943/btn_pgrpt_drag.gif) of a crosstab and select Crosstab Wizard from the shortcut menu.

This topic contains the following sections:

* [Data Tab Properties](#Data)
* [Layout Tab Properties](#Layout)

You see these elements on both tabs:

**Crosstab Title**

Specifies a title for the crosstab.

![Font button](https://devnet.logianalytics.com/hc/article_attachments/4404885319959/btn_wbrpt_font.gif)

Specifies the font properties of the crosstab title. After you select the button, Server displays the following dialog box for you to edit the font properties:

![](https://devnet.logianalytics.com/hc/article_attachments/4404880315543/fontprpty.gif "Font Properties")

* **Font**  
  Specifies the font face of the title.
* **Font Style**   
  Specifies the font style of the title. It can be one of the following: regular, bold, italic, and bold italic.
* **Size**  
  Specifies the font size of the title.
* **Align**  
  Specifies the position of the title to be left, right, center, or justify.
* **Font Color**  
  Specifies the font color of the title.
* **Background Color**  
  Specifies the background color of the title.

  To specify a color, select the color image to select a color from the color palette, or select **More Colors** in the color palette to select a color using the [Color Picker](../dlg_wbrpt_colorpkr.htm) dialog box.
* **OK**  
  Accepts the font settings and closes the dialog box.
* **Cancel**  
  Cancels editing the font properties and closes the dialog box.

**Data Source**

Displays the business view used by the crosstab.

**Filter**

Opens the [Query Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009747922-Query-Filter-Dialog-Box-Properties) dialog box to specify the filter which you want to apply to the selected business view.

**OK**

Applies the changes and closes the wizard.

**Cancel**

Does not retain changes and closes the wizard.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Ignores the setting and closes this dialog box.

## Data Tab Properties

Specifies the column, row and aggregate fields to display in the crosstab.

![Crosstab Wizard - Data tab](https://devnet.logianalytics.com/hc/article_attachments/4404885323287/crstbwzd_data.gif)

**Resources**

Displays the view elements in the selected business view.

* ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404880135447/btn_sort.gif)  
   Sorts the view elements in the specified order from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view elements are listed for this user.
  + **Predefined Order**  
    Select if you want to sort the view elements in the order as in the Business View Editor of Designer.
  + **Resource Types**  
    Select if you want to sort the view elements by resource type. Namely, category objects come first, then group objects, then aggregation objects, and at last detail objects.
  + **Alphabetical Order**  
    Select if you want to sort the view elements in alphabetical order. Logi Report sorts the elements that are not in any category first, and then the categories. It also sorts the elements in each category alphabetically.
* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404880135831/btn_srch.gif)  
   Launches the search bar to search for view elements.

See the following options in the search bar:

![Quick Search Toolbar](https://devnet.logianalytics.com/hc/article_attachments/4404880162071/btn_srchtlbr.gif)

+ **Text box**  
  Type the text you want to search in the text box. Server lists the values that contain the matched text.
+ **X**  
  Select to close the search bar or clear the typed text.
+ ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/4404885330071/btn_srchtlbr_adv.gif)  
  Select the button and Server displays more search options.
  - **Highlight All**   
    Select if you want to highlight all matched text.
  - **Match Case**   
    Select if you want to search for text that meets the case of the typed text.
  - **Match Whole Word**   
    Select if you want to search for text that looks the same as the typed text.
+ ![Previous Text](https://devnet.logianalytics.com/hc/article_attachments/4404880162711/btn_srchtlbr_prv.gif)  
  When you selected **Highlight All**, you can use this button to go to the previous matched text.
+ ![Next Text](https://devnet.logianalytics.com/hc/article_attachments/4404880162967/btn_srchtlbr_nxt.gif)  
   When you selected **Highlight All**, you can use this button to go to the next matched text.

**Columns/Rows**

Specifies the column/row fields to display in the crosstab.

* **Field**  
   Lists the group objects that will be displayed in the columns/rows of the crosstab.
* **Label**  
   Specifies the text of the labels for the column/row headers. You can select the text boxes to edit the label text, or select the Auto Map Field Name check boxes beside the text boxes to automatically map the label text to the dynamic display names of the objects.
* **Sort**  
   Specifies the sort order of the group objects.

**Summaries**

Specifies the aggregate fields to display in the crosstab.

* **Field**  
   Lists the aggregation/detail objects that you select to create summaries.
* **Label**  
   Specifies the text of the labels for the summaries. You can select the text boxes to edit the label text, or select the Auto Map Field Name check boxes beside the text boxes to automatically map the label text to the dynamic display names of the objects.
* **Aggregate**  
   Specifies the functions used to summarize data of the detail objects.
* **Distinct On**  
  Available and should be set when DistinctSum is selected as the aggregate function. It specifies the detail objects according to whose unique values to calculate DistinctSum. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404885320983/btn_chsr.gif) to select the detail objects in the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009776261-Select-Fields-Dialog-Box-Properties) dialog box.
* **Comparison Function**  
   Opens the [Comparison Function](https://devnet.logianalytics.com/hc/en-us/articles/1500009775041-Comparison-Function-Dialog-Box-Properties) dialog box to add a comparison function as an aggregate for the crosstab.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404880170519/btn_additem.gif)

Adds the selected group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) to be displayed on the columns of the crosstab.

![](https://devnet.logianalytics.com/hc/article_attachments/4404880172823/btn_addrow.gif)

Adds the selected group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) to be displayed on the rows of the crosstab.

![](https://devnet.logianalytics.com/hc/article_attachments/4404880173207/btn_addsum.gif)

Adds the selected aggregation object ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151959/btn_bvaggrgtn.gif) or detail object ![Detail Object](https://devnet.logianalytics.com/hc/article_attachments/4404885323799/btn_bvdtl.gif) to be the summary field of the crosstab.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif)

Moves the selected view element one level up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif)

Moves the selected view element one level down.

![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404885309335/btn_delete.gif)

Removes the selected resource.

## Layout Tab Properties

Specifies the layout of the crosstab.

![Crosstab Wizard -  Layout tab](https://devnet.logianalytics.com/hc/article_attachments/4404885489559/crstbwzd_layout.gif)

**Aggregate**

Specifies the layout of the aggregate fields.

* **Vertical Layout**  
  Select this option to arrange the aggregate fields vertically.
  + **Number of Rows**  
     Specifies the number of rows to hold the aggregate fields in the crosstab. By default, it is -1 which means that each aggregate field is placed in a row so that the aggregate fields are positioned in one column vertically. A number equal to or larger than the number of aggregate fields in the crosstab are treated as -1. If you set the number of rows (3 for example) less than the number of aggregate fields (6 for example), there will be 3 rows to hold the 6 fields with each row containing 2 fields.
* **Horizontal Layout**  
   Select this option to arrange the aggregate fields horizontally. When you have multiple aggregate fields in the crosstab, using horizontal layout can make the report more readable.
  + **Number of Columns**  
     Specifies the number of columns to hold the aggregate fields in the crosstab. By default, it is -1 which means that each aggregate field is placed in a column so that the aggregate fields are positioned in one row horizontally. A number equal to or larger than the number of aggregate fields in the crosstab are treated as -1. If you set the number of columns (3 for example) less than the number of aggregate fields (6 for example), there will be 3 columns to hold the 6 fields with each column containing 2 fields.

**Suppress Row Grand Totals**

Specifies whether to show the grand total row in the crosstab.

**Suppress Column Grand Totals**

Specifies whether to show the grand total column in the crosstab.

**Suppress Row Subtotals**

Specifies whether to show the subtotals of the row fields in the crosstab. You can select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404885411479/btn_chsr4.gif) to customize which subtotals of the row fields will be suppressed and which will be shown in the [Suppress Row Subtotals](https://devnet.logianalytics.com/hc/en-us/articles/1500009748102-Suppress-Row-Subtotals-Dialog-Box-Properties) dialog box.

**Suppress Column Subtotals**

Specifies whether to show the subtotals of the column fields in the crosstab. You can select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404885411479/btn_chsr4.gif) to customize which subtotals of the column fields will be suppressed and which will be shown in the [Suppress Column Subtotals](https://devnet.logianalytics.com/hc/en-us/articles/1500009776321-Suppress-Column-Subtotals-Dialog-Box-Properties) dialog box.

**Column Totals On**

Specifies the position of subtotal and grand total columns on the left or right of the detail aggregations.

**Row Totals On**

Specifies the position of subtotal and grand total rows on the top or bottom of the detail aggregations.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746862-Crosstab-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009774981-Cube-Status-Dialog-Box-Properties)
