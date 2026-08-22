---
title: "Insert Table Dialog Box Properties"
id: 4405683861655
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683861655-Insert-Table-Dialog-Box-Properties
updated_at: 2022-01-27T07:59:24Z
---

# Insert Table Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683860631-Insert-Row-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690596631-KPI-Properties)

# Insert Table Dialog Box Properties

This topic describes how you can use the Insert Table dialog box to [insert a table](https://devnet.logianalytics.com/hc/en-us/articles/4405684040855-Inserting-Components-in-Web-Report#Table) to a report. Server displays the dialog box when you drag **Table** from the **Components** panel to the destination.

**Table Title**

Specifies a title for the table.

![Font button](https://devnet.logianalytics.com/hc/article_attachments/4420461453847/btn_wbrpt_font.gif)

Specifies the font properties of the table title. After you select the button, Server displays the following dialog box for you to edit the font properties:

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

Specifies the business view in the current catalog on which the table will be built.

* **<Inherit from the Parent>**  
   Specifies to inherit data from the business view used by the parent object. Available only when the table is to be inserted into any of the following panels in a banded object: banded header panel, banded footer panel, group header panel, and group footer panel.

**Filter**

Opens the [Query Filter](https://devnet.logianalytics.com/hc/en-us/articles/4405683872023-Query-Filter-Dialog-Box-Properties) dialog box to specify the filter which you want to apply to the selected business view.

**Table type drop-down menu**

Specifies the type of the table. The tabs available in the dialog box differ according to the selected table type. When a group table type is selected, you can define the table in the Details, Group and Summary tabs respectively; when the summary table type is selected, only the Columns tab is available.

* **Group Above**  
  Creates a table with group information above the detail row.
* **Group Left**  
  Creates a table with group information left to the detail row.
* **Group Left Above**  
  Creates a table with group information left above the detail row.
* **Summary Table**  
  Creates a table with only group and summary information.

**OK**

Inserts a table and closes the dialog box.

**Cancel**

Cancels the insertion and closes the dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4420447202071/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420447202455/btn_close.gif)

Ignores the setting and closes this dialog box.

The tabs in the dialog box are different according to the following table types:

* [For Group Left, Group Above, or Group Left Above](#GroupTable)
* [For Summary Table](#SummaryTable)

## For Group Left, Group Above, or Group Left Above

The dialog box consists of the following tabs: [Details](#Display), [Group](#Group) and [Summary](#Summary).

### Details

Specifies the detail fields that you want to display in the table.

![Insert Table dialog - Details](https://devnet.logianalytics.com/hc/article_attachments/4420461487767/insrttbl_dsply.gif)

**Resources**

Displays all the group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4420461474455/btn_bvgrp.gif) and detail objects ![Detail Object](https://devnet.logianalytics.com/hc/article_attachments/4420447067799/btn_bvdtl.gif) in the selected business view.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4420461453463/btn_sort.gif) **Sort button**

Select an order for sorting the resources in the business view. The order applies to all the resource trees where you see the business view.

The order can be one of the following:

* **Predefined Order**  
  Select if you want to sort the resources in the order as in the Business View Editor of Designer.
* **Resource Types**  
  Select if you want to sort the resources by the resource type. Namely, category objects come first, then group objects, then aggregation objects, and at last detail objects.
* **Alphabetical Order**  
  Select if you want to sort the resources in alphabetical order. Logi Report sorts the resources that are not in any category first, and then the categories. It also sorts the resources in each category alphabetically.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/4420453392407/btn_srch.gif)**Search button**

Select to launch the search bar to search for objects.

See the following properties in the search bar:

![Quick Search Toolbar](https://devnet.logianalytics.com/hc/article_attachments/4420453420055/btn_srchtlbr.gif)

* **Text box**  
  Type the text you want to search in the text box. Server lists the values that contain the matched text.
* **![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420453394455/btn_delete.gif)****Close button**  
  Select to close the search bar.
* ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/4420447073047/btn_srchtlbr_adv.gif)**More Options button**  
  Select the button and Server displays more search options.
  + **Highlight All**   
    Select if you want to highlight all matched text.
  + **Match Case**   
    Select if you want to search for text that meets the case of the typed text.
  + **Match Whole Word**   
    Select if you want to search for text that looks the same as the typed text.
* ![Previous Text](https://devnet.logianalytics.com/hc/article_attachments/4420453420311/btn_srchtlbr_prv.gif) **Previous button**  
  Select to go to the previous matched text when you have selected **Highlight All**.
* ![Next Text](https://devnet.logianalytics.com/hc/article_attachments/4420447073431/btn_srchtlbr_nxt.gif)**Next button**  
   Select to go to the next matched text when you have selected **Highlight All**.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4420461488151/btn_additem.gif)

Adds the selected object to be displayed in the table.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4420447082647/btn_rmvitem.gif)

Removes the selected object that is added.

**Field**

Lists the group and detail objects that have been added to the table as the detail fields.

**Label**

Specifies the text for the labels of the detail columns, which by default are the display names of the added objects. You can select a text box to edit the label, or select the **Auto Map Field Name** checkbox beside the text box to automatically map the label to the dynamic display name of the object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420461479831/btn_mvup.gif)**Move Up button**

Select to move the selected item higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420453416727/btn_mvdown.gif)**Move Down button**

Select to move the selected item lower in the list.

**Sort Fields By**

Opens the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/4405690573719-Custom-Sort-Dialog-Box-Properties) dialog box to specify how to sort data in the table.

### Group

Specifies the fields to group the data.

![Insert Table dialog - Group](https://devnet.logianalytics.com/hc/article_attachments/4420453427351/insrttbl_grp.gif)

**Resources**

Displays all the available group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4420461474455/btn_bvgrp.gif) you can use to group the data in the table.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4420461453463/btn_sort.gif)

Sorts the group objects in the specified [order](#Order) from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view elements are listed for this user.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/4420453392407/btn_srch.gif)

Launches the [search bar](#Search) to search for group objects.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4420461488151/btn_additem.gif)

Adds the selected group object as a group field.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4420447082647/btn_rmvitem.gif)

Removes the selected group object.

**Field**

Lists all the group objects that have been added as the group fields.

**Sort**

Specifies the sort order for groups at the specific group level.

* **Ascend**  
   Groups will be sorted in an ascending order (A, B, C).
* **Descend**  
   Groups will be sorted in a descending order (C, B, A).
* **No Sort**  
   Groups will be sorted in the original order in database.
* **Custom Sort**  
   Opens the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/4405690573719-Custom-Sort-Dialog-Box-Properties) dialog box to set how groups will be sorted.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420461479831/btn_mvup.gif)**Move Up button**

Select to move the selected item higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420453416727/btn_mvdown.gif)**Move Down button**

Select to move the selected item lower in the list.

### Summary

Specifies the fields on which to create summaries.

![Insert Table dialog - Summary](https://devnet.logianalytics.com/hc/article_attachments/4420453427607/insrttbl_sum.gif)

**Resources**

Displays all the available aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4420461476503/btn_bvaggrgtn.gif) you can use to create summaries in the table.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4420461453463/btn_sort.gif)

Sorts the aggregation objects in the specified [order](#Order) from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view elements are listed for this user.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/4420453392407/btn_srch.gif)

Launches the [search bar](#Search) to search for aggregation objects.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4420461488151/btn_additem.gif)

Adds the selected aggregation object as the summary field.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4420447082647/btn_rmvitem.gif)

Removes the selected aggregation object.

**Field**

Lists the groups that have been added in the table and the aggregation objects added to summarize data in each group.

**Row**

Specifies to put the summary field in the header or footer row. If the summary is calculated on a group-by field, it will be put in the group header or footer of the corresponding group; if the summary is calculated on the table, it will be put in the table header or footer. Available only when the table is Group Left type.

**Column**

Specifies to put the summary field in the specified detail column. If no column is selected, the summary field will be displayed in a separate summary column. Available only when the table is Group Left type.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420461479831/btn_mvup.gif)**Move Up button**

Select to move the selected item higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420453416727/btn_mvdown.gif)**Move Down button**

Select to move the selected item lower in the list.

## For Summary Table

The dialog box consists of the following tabs: [Columns](#Columns) and [Summary](#Summary1).

### Columns

Specifies the fields to be displayed as the columns of the table.

![Insert Table dialog - Summary Table - Columns](https://devnet.logianalytics.com/hc/article_attachments/4420447078807/insrttbl_clmn.gif)

**Resources**

Displays all the group and aggregation objects in the selected business view.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4420461453463/btn_sort.gif)

Sorts the view elements in the specified [order](#Order) from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view objects are listed for this user.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/4420453392407/btn_srch.gif)

Launches the [search bar](#Search) to search for objects.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4420461488151/btn_additem.gif)

Adds the selected object to be displayed in the table.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4420447082647/btn_rmvitem.gif)

Removes the selected object that is added.

**Column**

Lists the objects that have been added to the table.

**Sort**

Specifies the sort order for groups at the specific group level.

* **Ascend**  
   Groups will be sorted in an ascending order (A, B, C).
* **Descend**  
   Groups will be sorted in a descending order (C, B, A).
* **No Sort**  
   Groups will be sorted in the original order in database.
* **Custom Sort**  
   Opens the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/4405690573719-Custom-Sort-Dialog-Box-Properties) dialog box to set how groups will be sorted.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420461479831/btn_mvup.gif)**Move Up button**

Select to move the selected item higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420453416727/btn_mvdown.gif)**Move Down button**

Select to move the selected item lower in the list.

### Summary

Specifies to insert aggregations to the header/footer rows of the table and groups.

![Insert Table dialog - Summary Table - Summary](https://devnet.logianalytics.com/hc/article_attachments/4420453427991/insrttbl_sum1.gif)

**Resources**

Displays the aggregations selected in the Columns tab.

**Summarized Fields**

Displays the group fields selected in the Columns tab under the Table node.

**Header**

Represents the table header or the group header of a specific group. After an aggregation is selected in the Resources box, you can select the checkboxes in the column to insert the aggregation in the corresponding header rows.

**Footer**

Represents the table footer or the group footer of a specific group. After an aggregation is selected in the Resources box, you can select the checkboxes in the column to insert the aggregation in the corresponding footer rows.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683860631-Insert-Row-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690596631-KPI-Properties)
