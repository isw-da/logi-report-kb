---
title: "Convert to Table Dialog Box Properties"
id: 1500009746822
section: "Web Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009746822-Convert-to-Table-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:34Z
---

# Convert to Table Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746802-Convert-to-Crosstab-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009746862-Crosstab-Properties)

# Convert to Table Dialog Box Properties

This topic describes how you can use the Convert to Table dialog box to convert a table to another table. Server displays the dialog box when you focus on a table and then select ![Convert To Table button](https://devnet.logianalytics.com/hc/article_attachments/4404880143255/btn_wbrpt_2tbl.gif) on the visualization toolbar.

**Table Title**

Specifies a title for the table.

![Font button](https://devnet.logianalytics.com/hc/article_attachments/4404885319959/btn_wbrpt_font.gif)

Specifies the font properties of the table title. After you select the button, Server displays the following dialog box for you to edit the font properties:

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

Specifies the business view in the current catalog on which the table will be built.

**Filter**

Opens the [Query Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009747922-Query-Filter-Dialog-Box-Properties) dialog box to specify the filter which you want to apply to the selected business view.

**Table type drop-down menu**

Specifies the type of the table. The tabs available in the dialog box differ according to the selected table type. When a group table type is selected, you can define the table in the Details, Group and Summary tabs respectively; when the summary table type is selected, only the Columns tab is available.

* **Group Above**  
   Creates a table with group information above the detail row.
* **Group Left**Creates a table with group information left to the detail row.
* **Group Left Above**  
   Creates a table with group information left above the detail row.
* **Summary Table**  
   Creates a table with only group and summary information.

**Show All Fields/Show Used Fields**

Specifies to show all the business view objects or only the ones used in the current table in the Resources box. Not available when you select another business view to convert the table with.

**OK**

Converts to the specified table and closes the dialog box.

**Cancel**

Cancels the conversion and closes the dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Ignores the setting and closes this dialog box.

The tabs in the dialog box are different according to the following table types:

* [For Group Left, Group Above, and Group Left Above](#GroupTable)
* [For Summary Table](#SummaryTable)

## For Group Left, Group Above, and Group Left Above

The dialog box consists of the following tabs: [Details](#Display), [Group](#Group) and [Summary](#Summary).

### Details

Specifies the detail fields that you want to display in the table.

![Convert To Table dialog - Details tab](https://devnet.logianalytics.com/hc/article_attachments/4404880158231/cnvttbl_dtl.gif)

**Resources**

Displays all the group and detail objects in the selected business view.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404880135447/btn_sort.gif)

Sorts the view elements in the specified order from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view elements are listed for this user.

* **Predefined Order**  
  Select if you want to sort the view elements in the order as in the Business View Editor of Designer.
* **Resource Types**  
  Select if you want to sort the view elements by resource type. Namely, category objects come first, then group objects, then aggregation objects, and at last detail objects.
* **Alphabetical Order**  
  Select if you want to sort the view elements in alphabetical order. Logi Report sorts the elements that are not in any category first, and then the categories. It also sorts the elements in each category alphabetically.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404880135831/btn_srch.gif)

Launches the search bar to search for view elements.

See the following options in the search bar:

![Quick Search Toolbar](https://devnet.logianalytics.com/hc/article_attachments/4404880162071/btn_srchtlbr.gif)

* **Text box**  
  Type the text you want to search in the text box. Server lists the values that contain the matched text.
* **X**  
  Select to close the search bar or clear the typed text.
* ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/4404885330071/btn_srchtlbr_adv.gif)  
  Select the button and Server displays more search options.
  + **Highlight All**   
    Select if you want to highlight all matched text.
  + **Match Case**   
    Select if you want to search for text that meets the case of the typed text.
  + **Match Whole Word**   
    Select if you want to search for text that looks the same as the typed text.
* ![Previous Text](https://devnet.logianalytics.com/hc/article_attachments/4404880162711/btn_srchtlbr_prv.gif)  
  When you selected **Highlight All**, you can use this button to go to the previous matched text.
* ![Next Text](https://devnet.logianalytics.com/hc/article_attachments/4404880162967/btn_srchtlbr_nxt.gif)  
   When you selected **Highlight All**, you can use this button to go to the next matched text.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404880170519/btn_additem.gif)

Adds the selected object to be displayed in the table.

![Remove Item](https://devnet.logianalytics.com/hc/article_attachments/4404885336599/btn_rmvitem.gif)

Removes the selected object that is added.

**Field**

Lists the objects that have been added to the table as the detail fields.

**Label**

Specifies the text for the labels of the detail columns, which by default are the display names of the added objects. You can select in the text boxes to edit the label text, or select the Auto Map Field Name check boxes beside the text boxes to automatically map the label text to the dynamic display names of the objects.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif)**Move Up button**

Moves the selected object higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif)**Move Down button**

Moves the selected object lower in the list.

**Sort Field By**

Opens the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009775101-Custom-Sort-Dialog-Box-Properties) dialog box to specify how to sort data in the table.

### Group

Specifies the fields to group the data.

![Convert To Table dialog - Group tab](https://devnet.logianalytics.com/hc/article_attachments/4404885491351/cnvttbl_grp.gif)

**Resources**

Displays all the available group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) you can use to group the data in the table.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404880135447/btn_sort.gif)

Sorts the group objects in the specified [order](#Order) from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view elements are listed for this user.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404880135831/btn_srch.gif)

Launches the [search bar](#Search) to search for view elements.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404880170519/btn_additem.gif)

Adds the selected group object as a group field.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4404885336599/btn_rmvitem.gif)

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
   Opens the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009775101-Custom-Sort-Dialog-Box-Properties) dialog box to set how groups will be sorted.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif)**Move Up button**

Moves the selected group higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif)**Move Down button**

Moves the selected group lower in the list.

### Summary

Specifies the fields on which to create summaries.

![Convert To Table dialog - Summary tab](https://devnet.logianalytics.com/hc/article_attachments/4404880400407/cnvttbl_sum.gif)

**Resources**

Displays all the available aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151959/btn_bvaggrgtn.gif) you can use to create summaries in the table.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404880135447/btn_sort.gif)

Sorts the aggregation objects in the specified [order](#Order) from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view elements are listed for this user.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404880135831/btn_srch.gif)

Launches the [search bar](#Search) to search for view elements.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404880170519/btn_additem.gif)

Adds the selected aggregation object as the summary field.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4404885336599/btn_rmvitem.gif)

Removes the selected aggregation object.

**Field**

Lists the groups that have been added in the table and the aggregation objects added to summarize data in each group.

**Row**

Specifies to put the summary field in the header or footer row. If the summary is calculated on a group-by field, it will be put in the group header or footer of the corresponding group; if the summary is calculated on the table, it will be put in the table header or footer. Available only when the table is Group Left type.

**Column**

Specifies to put the summary field in the specified detail column. If no column is selected, the summary field will be displayed in a separate summary column. Available only when the table is Group Left type.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif)**Move Up button**

Moves the selected aggregation object higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif)**Move Down button**

Moves the selected aggregation object lower in the list.

## For Summary Table

The dialog box consists of the following tabs: [Columns](#Columns) and [Summary](#Summary1).

### Columns

Specifies the fields to be displayed as the columns of the table.

![Convert To Table dialog - Columns tab](https://devnet.logianalytics.com/hc/article_attachments/4404880400791/cnvttbl_sumtable.gif)

**Resources**

Displays all the available group and aggregation objects.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404880135447/btn_sort.gif)

Sorts the view elements in the specified [order](#Order) from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view elements are listed for this user.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404880135831/btn_srch.gif)

Launches the [search bar](#Search) to search for view elements.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404880170519/btn_additem.gif)

Adds the selected object to be displayed in the table.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4404885336599/btn_rmvitem.gif)

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
   Opens the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009775101-Custom-Sort-Dialog-Box-Properties) dialog box to set how groups will be sorted.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif)**Move Up button**

Moves the selected object higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif)**Move Down button**

Moves the selected object lower in the list.

### Summary

Specifies to insert aggregations to the header/footer rows of the table and groups.

![Convert To Table dialog - Summary tab](https://devnet.logianalytics.com/hc/article_attachments/4404880401175/cnvttbl_sum1.gif)

**Resources**

Displays the aggregations selected in the Columns tab.

**Summarized Fields**

Displays the group fields selected in the Columns tab under the Table node.

**Header**

Represents the table header or the group header of a specific group. After an aggregation is selected in the Resources box, you can select the check boxes in the column to insert the aggregation in the corresponding header rows.

**Footer**

Represents the table footer or the group footer of a specific group. After an aggregation is selected in the Resources box, you can select the check boxes in the column to insert the aggregation in the corresponding footer rows.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746802-Convert-to-Crosstab-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009746862-Crosstab-Properties)
