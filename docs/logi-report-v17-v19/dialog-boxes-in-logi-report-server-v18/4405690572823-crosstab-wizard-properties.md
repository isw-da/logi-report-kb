---
title: "Crosstab Wizard Properties"
id: 4405690572823
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690572823-Crosstab-Wizard-Properties
updated_at: 2022-01-27T07:59:13Z
---

# Crosstab Wizard Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683803415-Crosstab-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683793303-Cube-Status-Dialog-Box-Properties)

# Crosstab Wizard Properties

This topic describes how you can use Crosstab Wizard to change data of a crosstab.

Server displays the wizard when you do one of the following:

* Select a crosstab, then select Menu > Edit > Wizard.
* Select a crosstab, then select the Crosstab Wizard button ![Crosstab Wizard button](https://devnet.logianalytics.com/hc/article_attachments/4420453396503/btn_wbrpt_wizard.gif) on the visualization toolbar.
* Right-click the icon ![Drag icon](https://devnet.logianalytics.com/hc/article_attachments/4420461463703/btn_pgrpt_drag.gif) of a crosstab and select Crosstab Wizard from the shortcut menu.

This topic contains the following sections:

* [Data Tab Properties](#Data)
* [Layout Tab Properties](#Layout)

You see these elements on both tabs:

**Crosstab Title**

Specify a title for the crosstab.

![Font button](https://devnet.logianalytics.com/hc/article_attachments/4420461453847/btn_wbrpt_font.gif)**Font button**

Select the button, and Server displays the following dialog box for you to edit the font properties of the crosstab title:

![](https://devnet.logianalytics.com/hc/article_attachments/4420461616279/fontprpty.gif "Font Properties")

* **Font**  
  Select the font face of the title.
* **Font Style**   
  Select the font style of the title: regular, bold, italic, and bold italic.
* **Size**  
  Specify the font size of the title.
* **Align**  
  Specify the position of the title to be left, right, center, or justify.
* **Font Color**  
  Specify the font color of the title.

  To change the color, select the color indicator. Server displays the color palette. Select a color, or select **More Colors** to access the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683802391-Color-Picker-Dialog-Box-Properties) in which you can specify a color within a wider range. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff.
* **Background Color**  
  Specify the background color of the title.
* **OK**  
  Select to apply any changes you made here and exit the dialog box.
* **Cancel**  
  Select to close the dialog box without saving any changes.

**Data Source**

Server displays the business view that the crosstab uses.

**Filter**

Select to open the [Query Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683872023-Query-Filter-Dialog-Box-Properties) to specify the filter which you want to apply to the selected business view.

**OK**

Select to apply any changes you made here and exit the wizard.

**Cancel**

Select to close the wizard without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4420447202071/btn_help.gif) **Help button**

Select to view information about the wizard.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420447202455/btn_close.gif) **Close button**

Select to close the wizard without saving any changes.

## Data Tab Properties

Specify the column, row, and aggregate fields to display in the crosstab.

![Crosstab Wizard - Data tab](https://devnet.logianalytics.com/hc/article_attachments/4420447064855/crstbwzd_data.gif)

**Resources**

Server displays the view elements in the selected business view.

* ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4420461453463/btn_sort.gif) **Sort button**

  Select an order for sorting the resources in the business view. The order applies to all the resource trees where you see the business view.

  The order can be one of the following:

  + **Predefined Order**  
    Select if you want to sort the resources in the order as in the Business View Editor of Designer.
  + **Resource Types**  
    Select if you want to sort the resources by the resource type. Namely, category objects come first, then group objects, then aggregation objects, and at last detail objects.
  + **Alphabetical Order**  
    Select if you want to sort the resources in alphabetical order. Logi Report sorts the resources that are not in any category first, and then the categories. It also sorts the resources in each category alphabetically.
* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4420453392407/btn_srch.gif) **Search button**  
   Select to launch the search bar to search for view elements.

See the following properties in the search bar:

![Quick Search Toolbar](https://devnet.logianalytics.com/hc/article_attachments/4420453420055/btn_srchtlbr.gif)

+ **Text box**  
  Type the text you want to search in the text box. Server lists the values that contain the matched text.
+ **![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420453394455/btn_delete.gif)****Close button**  
  Select to close the search bar.
+ ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/4420447073047/btn_srchtlbr_adv.gif)**More Options button**  
  Select the button and Server displays more search options.
  - **Highlight All**   
    Select if you want to highlight all matched text.
  - **Match Case**   
    Select if you want to search for text that meets the case of the typed text.
  - **Match Whole Word**   
    Select if you want to search for text that looks the same as the typed text.
+ ![Previous Text](https://devnet.logianalytics.com/hc/article_attachments/4420453420311/btn_srchtlbr_prv.gif) **Previous button**  
  Select to go to the previous matched text when you have selected **Highlight All**.
+ ![Next Text](https://devnet.logianalytics.com/hc/article_attachments/4420447073431/btn_srchtlbr_nxt.gif)**Next button**  
   Select to go to the next matched text when you have selected **Highlight All**.

**Columns/Rows**

Specify the column/row fields to display in the crosstab.

* **Field**  
   Server lists the group objects that will display in the columns/rows of the crosstab.
* **Label**  
   Specify the text of the labels for the column/row headers. You can select a text box to edit the label, or select the **Auto Map Field Name** checkbox beside the text box to automatically map the label to the dynamic display name of the object.
* **Sort**  
   Specify the sort order of the group objects.

**Summaries**

Specify the aggregate fields to display in the crosstab.

* **Field**  
   Server lists the aggregation/detail objects that you select to create summaries.
* **Label**  
   Specify the text of the labels for the summaries. You can select a text box to edit the label, or select the **Auto Map Field Name** checkbox beside the text box to automatically map the label to the dynamic display name of the object.
* **Aggregate**  
   Specify the functions for summarizing data of the detail objects.
* **Distinct On**  
  Server enables this property when you select **DistinctSum** as the aggregate function, and you should set it. Select the ellipsis button ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4420461473943/btn_chsr.gif), and then in the [Select Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683879831-Select-Fields-Dialog-Box-Properties) select the fields according to whose unique values you want to calculate the DistinctSum function.
* **Comparison Function**  
   Select to open the [Comparison Function dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683795607-Comparison-Function-Dialog-Box-Properties) to add a comparison function as an aggregate for the crosstab.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4420461488151/btn_additem.gif) **Add Column button**

Select to add the selected group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4420461474455/btn_bvgrp.gif) to display in the columns of the crosstab.

![](https://devnet.logianalytics.com/hc/article_attachments/4420453428375/btn_addrow.gif) **Add Row button**

Select to add the selected group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4420461474455/btn_bvgrp.gif) to display in the rows of the crosstab.

![](https://devnet.logianalytics.com/hc/article_attachments/4420461488791/btn_addsum.gif) **Add Summary button**

Select to add the selected aggregation object ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4420461476503/btn_bvaggrgtn.gif) or detail object ![Detail Object](https://devnet.logianalytics.com/hc/article_attachments/4420447067799/btn_bvdtl.gif) to be the summary field of the crosstab.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420461479831/btn_mvup.gif)**Move Up button**

Select to move the selected item higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420453416727/btn_mvdown.gif)**Move Down button**

Select to move the selected item lower in the list.

![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4420453394455/btn_delete.gif)**Remove button**

Select to remove the selected resource.

## Layout Tab Properties

Specify the layout of the crosstab.

![Crosstab Wizard -  Layout tab](https://devnet.logianalytics.com/hc/article_attachments/4420453585815/crstbwzd_layout.gif)

**Aggregate**

Specify the layout of the aggregate fields.

* **Vertical Layout**  
  Select this option to arrange the aggregate fields vertically.
  + **Number of Rows**  
     Specify the number of rows to hold the aggregate fields in the crosstab. By default, it is -1 which means that Server places each aggregate field in a row so that the aggregate fields are in one column vertically. Server treats a number equal to or larger than the number of aggregate fields in the crosstab as -1. If you set the number of rows (3 for example) less than the number of aggregate fields (6 for example), there will be 3 rows to hold the 6 fields with each row containing 2 fields.
* **Horizontal Layout**  
   Select this option to arrange the aggregate fields horizontally. When you have multiple aggregate fields in the crosstab, using horizontal layout can make the report more readable.
  + **Number of Columns**  
     Specify the number of columns to hold the aggregate fields in the crosstab. By default, it is -1 which means that Server places each aggregate field in a column so that the aggregate fields are in one row horizontally. Server treats a number equal to or larger than the number of aggregate fields in the crosstab as -1. If you set the number of columns (3 for example) less than the number of aggregate fields (6 for example), there will be 3 columns to hold the 6 fields with each column containing 2 fields.

**Suppress Row Grand Totals**

Select to show the grand total row in the crosstab.

**Suppress Column Grand Totals**

Select to show the grand total column in the crosstab.

**Suppress Row Subtotals**

Select to show the subtotals of the row fields in the crosstab. You can select the ellipsis button ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4420453521175/btn_chsr4.gif) to customize which subtotals of the row fields you want to suppress and which you want to show, in the [Suppress Row Subtotals dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405690606999-Suppress-Row-Subtotals-Dialog-Box-Properties).

**Suppress Column Subtotals**

Select to show the subtotals of the column fields in the crosstab. You can select the ellipsis button ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4420453521175/btn_chsr4.gif) to customize which subtotals of the column fields you want to suppress and which you want to show, in the [Suppress Column Subtotals dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683885207-Suppress-Column-Subtotals-Dialog-Box-Properties).

**Column Totals On**

Specify the position of subtotal and grand total columns on the left or right of the detail aggregations.

**Row Totals On**

Specify the position of subtotal and grand total rows on the top or bottom of the detail aggregations.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683803415-Crosstab-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683793303-Cube-Status-Dialog-Box-Properties)
