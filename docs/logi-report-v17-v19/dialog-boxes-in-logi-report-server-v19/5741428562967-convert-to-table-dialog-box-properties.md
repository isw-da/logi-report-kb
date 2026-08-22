---
title: "Convert to Table Dialog Box Properties"
id: 5741428562967
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741428562967-Convert-to-Table-Dialog-Box-Properties
updated_at: 2022-10-31T17:17:16Z
---

# Convert to Table Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741449434903-Convert-to-Crosstab-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/7985324126999-Crosstab-Formula-Editor-Properties)

# Convert to Table Dialog Box Properties

This topic describes how you can use the Convert to Table dialog box to convert a table to another table. Server displays the dialog box when you focus on a table and then select the table icon ![Convert To Table button](https://devnet.logianalytics.com/hc/article_attachments/9905629271575/btn_wbrpt_2tbl.gif) on the visualization toolbar.

**Table Title**

Specify a title for the table.

![Font button](https://devnet.logianalytics.com/hc/article_attachments/9905615721239/btn_wbrpt_font.gif)

Select the button, and Server displays the following dialog box for you to edit the font properties of the table title:

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

Select a business view or dataset on which you want to build the table.

**Filter**

Select to open the [Edit Dataset Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/7985329714327-Edit-Dataset-Filter-Dialog-Box-Properties) to specify the filter you want to apply to the selected business view.

**Table type drop-down menu**

Specify the type of the table. The tabs available in the dialog box differ according to the selected table type. When you select a group table type, you can define the table in the Details, Group, and Summary tabs respectively; when you select the summary table type, only the Columns tab is available.

* **Group Above**  
   Select to create a table with group information above the detail row.
* **Group Left**Select to create a table with group information left to the detail row.
* **Group Left Above**  
   Select to create a table with group information left above the detail row.
* **Summary Table**  
   Select to create a table with only group and summary information.

**Show All Fields/Show Used Fields**

Select to show all the business view elements or only the ones that the current data component uses, in the Resources box. This pair of properties are not available when you select another business view to convert to table with.

**OK**

Select to convert to the specified table and close the dialog box.

**Cancel**

Select to close the dialog box without conversion.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to close the dialog box without conversion.

The tabs in the dialog box are different according to the following table types:

* [For Group Left, Group Above, and Group Left Above](#GroupTable)
* [For Summary Table](#SummaryTable)

## For Group Left, Group Above, and Group Left Above

The dialog box consists of the following tabs: [Details](#Display), [Group](#Group), and [Summary](#Summary).

### Details

Specify the detail fields that you want to display in the table.

![Convert To Table dialog - Details tab](https://devnet.logianalytics.com/hc/article_attachments/9905631061143/cnvttbl_dtl.gif)

**Resources**

Server displays all the group and detail objects in the selected business view or dataset.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/9905577646231/btn_sort.gif) **Sort button**

Select an order for sorting the resources in the business view. The order applies to all the resource trees where you see the business view in Web Report Studio.

The order can be one of the following:

* **Predefined Order**  
  Select if you want to sort the resources in the order as in the Business View Editor of Designer.
* **Resource Types**  
  Select if you want to sort the resources by the resource type. Namely, category objects come first, then group objects, then aggregation objects, and at last detail objects.
* **Alphabetical Order**  
  Select if you want to sort the resources in alphabetical order. Logi Report sorts the resources that are not in any category first, and then the categories. It also sorts the resources in each category alphabetically.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/9905577660311/btn_srch.gif) **Search button**

Select to launch the search bar to search for view elements.

See the following properties in the search bar:

![Quick Search Toolbar](https://devnet.logianalytics.com/hc/article_attachments/9905619099031/btn_srchtlbr.gif)

* **Text box**  
  Type the text you want to search in the text box. Server lists the values that contain the matched text.
* **![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905578411927/btn_delete.gif)****Close button**  
  Select to close the search bar.
* ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/9905631409303/btn_srchtlbr_adv.gif)**More Options button**  
  Select the button and Server displays more search options.
  + **Highlight All**   
    Select if you want to highlight all matched text.
  + **Match Case**   
    Select if you want to search for text that meets the case of the typed text.
  + **Match Whole Word**   
    Select if you want to search for text that looks the same as the typed text.
* ![Previous Text](https://devnet.logianalytics.com/hc/article_attachments/9905631449623/btn_srchtlbr_prv.gif) **Previous button**  
  Select to go to the previous matched text when you have selected **Highlight All**.
* ![Next Text](https://devnet.logianalytics.com/hc/article_attachments/9905619191959/btn_srchtlbr_nxt.gif)**Next button**  
   Select to go to the next matched text when you have selected **Highlight All**.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/9905612569111/btn_additem.gif)**Add button**

Select to add the selected object to display in the table.

![Remove Item](https://devnet.logianalytics.com/hc/article_attachments/9905574572823/btn_rmvitem.gif)**Remove button**

Select to remove the selected object you added.

**Field**

Server lists the objects that you have added to the table as the detail fields.

**Label**

Specify the text for the labels of the detail columns, which by default are the display names of the added objects. You can select a text box to edit the label, or select the **Auto Map Field Name** checkbox beside the text box to automatically map the label to the dynamic display name of the object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9905613125783/btn_mvup.gif)**Move Up button**

Select to move the selected item higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9905575169431/btn_mvdown.gif)**Move Down button**

Select to move the selected item lower in the list.

**Sort Field By**

Select to open the [Custom Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741457687831-Custom-Sort-Dialog-Box-Properties) to specify how to sort data in the table.

### Group

Specify the fields to group the data.

![Convert To Table dialog - Group tab](https://devnet.logianalytics.com/hc/article_attachments/9905734345495/cnvttbl_grp.gif)

**Resources**

Server displays all the available group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/9905617901719/btn_bvgrp.gif) you can use to group the data in the table.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/9905577646231/btn_sort.gif)**Sort button**

Select an [order](#Sort) for sorting the group objects.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/9905577660311/btn_srch.gif)**Search button**

Select to launch the [search bar](#Search) to search for view elements.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/9905612569111/btn_additem.gif)**Add button**

Select to add the selected group object as a group field.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/9905574572823/btn_rmvitem.gif)**Remove button**

Select to remove the selected group object.

**Field**

Server lists all the group objects that you have added as the group fields.

**Sort**

Specify the sort order for groups at the specific group level.

* **No Sort**  
   Select to sort a group in the same order as in the catalog.
* **Ascend**  
   Select to sort a group in an ascending order.
* **Descend**  
   Select to sort a group in a descending order.
* **Custom Sort**  
  Select to open the [Custom Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741457687831-Custom-Sort-Dialog-Box-Properties) to sort a group by sorting the values of other fields.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9905613125783/btn_mvup.gif)**Move Up button**

Select to move the selected item higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9905575169431/btn_mvdown.gif)**Move Down button**

Select to move the selected item lower in the list.

### Summary

Specify the fields on which you want to create summaries.

![Convert To Table dialog - Summary tab](https://devnet.logianalytics.com/hc/article_attachments/9905734373527/cnvttbl_sum.gif)

**Resources**

Server displays all the available aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/9905618017943/btn_bvaggrgtn.gif) you can use to create summaries in the table.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/9905577646231/btn_sort.gif) **Sort button**

Select an [order](#Sort) for sorting the aggregation objects.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/9905577660311/btn_srch.gif) **Search button**

Select to launch the [search bar](#Search) to search for view elements.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/9905612569111/btn_additem.gif)**Add button**

Select to add the selected aggregation object as the summary field.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/9905574572823/btn_rmvitem.gif)**Remove button**

Select to remove the selected aggregation object.

**Field**

Server lists the groups that you have added in the table and the aggregation objects you added to summarize data in each group.

**Row**

Specify to put the summary field in the header or footer row. If you want to calculate the summary on a group-by field, put it in the group header or footer of the corresponding group; To calculate the summary on the table, put it in the table header or footer. The Row column is available only when the table is Group Left type.

**Column**

Specify to put the summary field in the specified detail column. If you select no column, Server will display the summary field in a separate summary column. The Column column is available only when the table is Group Left type.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9905613125783/btn_mvup.gif)**Move Up button**

Select to move the selected item higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9905575169431/btn_mvdown.gif)**Move Down button**

Select to move the selected item lower in the list.

## For Summary Table

The dialog box consists of the following tabs: [Columns](#Columns) and [Summary](#Summary1).

### Columns

Specify the fields to be the columns of the table.

![Convert To Table dialog - Columns tab](https://devnet.logianalytics.com/hc/article_attachments/9905756211863/cnvttbl_sumtable.gif)

**Resources**

Server displays all the available group and aggregation objects.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/9905577646231/btn_sort.gif) **Sort button**

Select an [order](#Sort) for sorting the view elements.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/9905577660311/btn_srch.gif) **Search button**

Select to launch the [search bar](#Search) to search for view elements.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/9905612569111/btn_additem.gif)**Add button**

Select to add the selected object to display in the table.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/9905574572823/btn_rmvitem.gif)**Remove button**

Select to remove the selected object you added.

**Column**

Server lists the objects that you have added to the table.

**Sort**

Specify the sort order for groups at the specific group level.

* **No Sort**  
   Select to sort a group in the same order as in the catalog.
* **Ascend**  
   Select to sort a group in an ascending order.
* **Descend**  
   Select to sort a group in a descending order.
* **Custom Sort**  
  Select to open the [Custom Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741457687831-Custom-Sort-Dialog-Box-Properties) to sort a group by sorting the values of other fields.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9905613125783/btn_mvup.gif)**Move Up button**

Select to move the selected item higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9905575169431/btn_mvdown.gif)**Move Down button**

Select to move the selected item lower in the list.

### Summary

Specify to insert aggregations to the header/footer rows of the table and groups.

![Convert To Table dialog - Summary tab](https://devnet.logianalytics.com/hc/article_attachments/9905734432407/cnvttbl_sum1.gif)

**Resources**

Server displays the aggregations you selected in the Columns tab.

**Summarized Fields**

Server displays the group fields you selected in the Columns tab under the Table node.

**Header**

The table header or the group header of a specific group. After selecting an aggregation in the Resources box, you can select the checkboxes in the column to insert the aggregation in the corresponding header rows.

**Footer**

The table footer or the group footer of a specific group. After selecting an aggregation in the Resources box, you can select the checkboxes in the column to insert the aggregation in the corresponding footer rows.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741449434903-Convert-to-Crosstab-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/7985324126999-Crosstab-Formula-Editor-Properties)
