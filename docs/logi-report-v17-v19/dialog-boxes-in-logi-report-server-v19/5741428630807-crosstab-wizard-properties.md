---
title: "Crosstab Wizard Properties"
id: 5741428630807
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741428630807-Crosstab-Wizard-Properties
updated_at: 2022-10-31T17:17:17Z
---

# Crosstab Wizard Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741434505367-Crosstab-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741422256407-Cube-Status-Dialog-Box-Properties)

# Crosstab Wizard Properties

This topic describes how you can use Crosstab Wizard to change data of a crosstab.

Server displays the wizard when you do one of the following:

* Select a crosstab, then select Menu > Edit > Wizard.
* Select a crosstab, then select the Crosstab Wizard button ![Crosstab Wizard button](https://devnet.logianalytics.com/hc/article_attachments/9905629192215/btn_wbrpt_wizard.gif) on the visualization toolbar.
* Right-click the icon ![Drag icon](https://devnet.logianalytics.com/hc/article_attachments/9905629613463/btn_pgrpt_drag.gif) of a crosstab and select Crosstab Wizard from the shortcut menu.

This topic contains the following sections:

* [Data Tab Properties](#Data)
* [Layout Tab Properties](#Layout)

You see these elements on both tabs:

**Crosstab Title**

Specify a title for the crosstab.

![Font button](https://devnet.logianalytics.com/hc/article_attachments/9905615721239/btn_wbrpt_font.gif)**Font button**

Select the button, and Server displays the following dialog box for you to edit the font properties of the crosstab title:

![](https://devnet.logianalytics.com/hc/article_attachments/9905716575255/fontprpty.gif "Font Properties")

* **Font**  
  Select the font face of the title.
* **Font Style**   
  Select the font style of the title: regular, bold, italic, or bold italic.
* **Size**  
  Specify the font size of the title.
* **Align**  
  Specify the position of the title to be left, right, center, or justify.
* **Font Color**  
  Specify the font color of the title.

  To change the color, select the color indicator. Server displays the color palette. Select a color, or select **More Colors** to access the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428592023-Color-Picker-Dialog-Box-Properties) in which you can specify a color within a wider range. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff.
* **Background Color**  
  Specify the background color of the title.
* **OK**  
  Select to apply any changes you made here and close the dialog box.
* **Cancel**  
  Select to close the dialog box without saving any changes.

**Data Source**

Server displays the dataset that the crosstab uses.

**Filter**

Select to open the [Edit Dataset Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/7985329714327-Edit-Dataset-Filter-Dialog-Box-Properties) to specify the filter which you want to apply to the dataset.

**OK**

Select to apply any changes you made here and exit the wizard.

**Cancel**

Select to close the wizard without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif) **Help button**

Select to view information about the wizard.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif) **Close button**

Select to close the wizard without saving any changes.

## Data Tab Properties

Specify the column, row, and aggregate fields to display in the crosstab.

![Crosstab Wizard - Data tab](https://devnet.logianalytics.com/hc/article_attachments/9905630243991/crstbwzd_data.gif)

**Resources**

Server displays the view elements in the selected business view or dataset.

* ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/9905577646231/btn_sort.gif) **Sort button**

  Select an order for sorting the resources in the business view. The order applies to all the resource trees where you see the business view in Web Report Studio.

  The order can be one of the following:

  + **Predefined Order**  
    Select if you want to sort the resources in the order as in the Business View Editor of Designer.
  + **Resource Types**  
    Select if you want to sort the resources by the resource type. Namely, category objects come first, then group objects, then aggregation objects, and at last detail objects.
  + **Alphabetical Order**  
    Select if you want to sort the resources in alphabetical order. Logi Report sorts the resources that are not in any category first, and then the categories. It also sorts the resources in each category alphabetically.
* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/9905577660311/btn_srch.gif) **Search button**  
   Select to launch the search bar to search for view elements.

See the following properties in the search bar:

![Quick Search Toolbar](https://devnet.logianalytics.com/hc/article_attachments/9905619099031/btn_srchtlbr.gif)

+ **Text box**  
  Type the text you want to search in the text box. Server lists the values that contain the matched text.
+ **![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905578411927/btn_delete.gif)****Close button**  
  Select to close the search bar.
+ ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/9905631409303/btn_srchtlbr_adv.gif)**More Options button**  
  Select the button and Server displays more search options.
  - **Highlight All**   
    Select if you want to highlight all matched text.
  - **Match Case**   
    Select if you want to search for text that meets the case of the typed text.
  - **Match Whole Word**   
    Select if you want to search for text that looks the same as the typed text.
+ ![Previous Text](https://devnet.logianalytics.com/hc/article_attachments/9905631449623/btn_srchtlbr_prv.gif) **Previous button**  
  Select to go to the previous matched text when you have selected **Highlight All**.
+ ![Next Text](https://devnet.logianalytics.com/hc/article_attachments/9905619191959/btn_srchtlbr_nxt.gif)**Next button**  
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
  Server enables this property when you select **DistinctSum** as the aggregate function, and you should set it. Select the ellipsis button ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/9905630122007/btn_chsr.gif), and then in the [Select Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741466688151-Select-Fields-Dialog-Box-Properties) select the fields according to whose unique values you want to calculate the DistinctSum function.
* **Comparison Function**  
   Select to open the [Comparison Function dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741457488535-Comparison-Function-Dialog-Box-Properties) to add a comparison function as an aggregate for the crosstab.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/9905612569111/btn_additem.gif) **Add Column button**

Select to add the selected group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/9905617901719/btn_bvgrp.gif) to display in the columns of the crosstab.

![](https://devnet.logianalytics.com/hc/article_attachments/9905620190103/btn_addrow.gif) **Add Row button**

Select to add the selected group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/9905617901719/btn_bvgrp.gif) to display in the rows of the crosstab.

![](https://devnet.logianalytics.com/hc/article_attachments/9905620225559/btn_addsum.gif) **Add Summary button**

Select to add the selected aggregation object ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/9905618017943/btn_bvaggrgtn.gif) or detail object ![Detail Object](https://devnet.logianalytics.com/hc/article_attachments/9905630361111/btn_bvdtl.gif) to be the summary field of the crosstab.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9905613125783/btn_mvup.gif)**Move Up button**

Select to move the selected item higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9905575169431/btn_mvdown.gif)**Move Down button**

Select to move the selected item lower in the list.

![Delete button](https://devnet.logianalytics.com/hc/article_attachments/9905578411927/btn_delete.gif)**Remove button**

Select to remove the selected resource.

## Layout Tab Properties

Specify the layout of the crosstab.

![Crosstab Wizard -  Layout tab](https://devnet.logianalytics.com/hc/article_attachments/9905755919255/crstbwzd_layout.gif)

**Aggregate**

Specify the layout of the aggregate fields.

* **Vertical Layout**  
  Select to arrange the aggregate fields vertically.
  + **Number of Rows**  
     Specify the number of rows to hold the aggregate fields in the crosstab. By default, it is -1 which means that Server places each aggregate field in a row so that the aggregate fields are in one column vertically. Server treats a number equal to or larger than the number of aggregate fields in the crosstab as -1. If you set the number of rows (3 for example) less than the number of aggregate fields (6 for example), there will be 3 rows to hold the 6 fields with each row containing 2 fields.
* **Horizontal Layout**  
   Select to arrange the aggregate fields horizontally. When you have multiple aggregate fields in the crosstab, using horizontal layout can make the report more readable.
  + **Number of Columns**  
     Specify the number of columns to hold the aggregate fields in the crosstab. By default, it is -1 which means that Server places each aggregate field in a column so that the aggregate fields are in one row horizontally. Server treats a number equal to or larger than the number of aggregate fields in the crosstab as -1. If you set the number of columns (3 for example) less than the number of aggregate fields (6 for example), there will be 3 columns to hold the 6 fields with each column containing 2 fields.

**Suppress Row Grand Totals**

Select to show the grand total row in the crosstab.

**Suppress Column Grand Totals**

Select to show the grand total column in the crosstab.

**Suppress Row Subtotals**

Select to show the subtotals of the row fields in the crosstab. You can select the ellipsis button ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/9905675890327/btn_chsr4.gif) to customize which subtotals of the row fields you want to suppress and which you want to show, in the [Suppress Row Subtotals dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741460082583-Suppress-Row-Subtotals-Dialog-Box-Properties).

**Suppress Column Subtotals**

Select to show the subtotals of the column fields in the crosstab. You can select the ellipsis button ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/9905675890327/btn_chsr4.gif) to customize which subtotals of the column fields you want to suppress and which you want to show, in the [Suppress Column Subtotals dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741451841175-Suppress-Column-Subtotals-Dialog-Box-Properties).

**Column Totals On**

Specify the position of subtotal and grand total columns on the left or right of the detail aggregations.

**Row Totals On**

Specify the position of subtotal and grand total rows on the top or bottom of the detail aggregations.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741434505367-Crosstab-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741422256407-Cube-Status-Dialog-Box-Properties)
