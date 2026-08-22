---
title: "To Crosstab Dialog Box Properties"
id: 4405690613527
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690613527-To-Crosstab-Dialog-Box-Properties
updated_at: 2022-01-27T07:59:30Z
---

# To Crosstab Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683892631-To-Chart-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683893911-Unique-Key-Dialog-Box-Properties)

# To Crosstab Dialog Box Properties

This topic describes how you can use the To Crosstab dialog box to specify settings for converting a chart into a crosstab. Server displays the dialog box when you right-click a chart and then select **To Crosstab** on the shortcut menu or select Menu > Edit > To Crosstab.

![To Crosstab dialog](https://devnet.logianalytics.com/hc/article_attachments/4420461479575/tocrstb.gif)

**Title**

Specifies a title for the crosstab.

![Font button](https://devnet.logianalytics.com/hc/article_attachments/4420461453847/btn_wbrpt_font.gif)

Specifies the font properties of the chart title. After you select the button, Server displays the following dialog box for you to edit the font properties:

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

**Resources**

Displays all the view elements used in the chart.

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

Select to launch the search bar to search for view elements.

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

Adds the selected group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4420461474455/btn_bvgrp.gif) to be displayed in the columns of the crosstab.

![Add Row button](https://devnet.logianalytics.com/hc/article_attachments/4420453428375/btn_addrow.gif)

Adds the selected group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4420461474455/btn_bvgrp.gif) to be displayed in the rows of the crosstab.

![Add Summary button](https://devnet.logianalytics.com/hc/article_attachments/4420461488791/btn_addsum.gif)

Adds the selected aggregation object ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4420461476503/btn_bvaggrgtn.gif) to be the summary field of the crosstab.

**Columns/Rows**

Lists the group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4420461474455/btn_bvgrp.gif) that will be displayed on the columns/rows of the crosstab.

* **Field**  
   Lists the group objects that you selected to display in the crosstab.
* **Label**  
   Specifies the text of the labels for the column/row headers. You can select a text box to edit the label, or select the **Auto Map Field Name** checkbox beside the text box to automatically map the label to the dynamic display name of the object.
* **Sort**  
   Specifies how the selected group objects will be sorted.

**Summaries**

Lists the aggregation/detail objects that will be the summary fields of the crosstab.

* **Field**  
   Lists the aggregation/detail objects that you selected to display in the crosstab.
* **Label**  
   Specifies the text of the labels for the summaries. You can select a text box to edit the label, or select the **Auto Map Field Name** checkbox beside the text box to automatically map the label to the dynamic display name of the object.
* **Aggregate**  
   Specifies the functions used to summarize data of the detail objects.
* **Distinct On**  
  Server enables this property when you select **DistinctSum** as the aggregate function, and you should set it. Select the ellipsis button ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4420461473943/btn_chsr.gif), and then in the [Select Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683879831-Select-Fields-Dialog-Box-Properties) select the fields according to whose unique values you want to calculate the DistinctSum function.
* **Comparison Function**  
   Opens the [Comparison Function](https://devnet.logianalytics.com/hc/en-us/articles/4405683795607-Comparison-Function-Dialog-Box-Properties) dialog box to add a comparison function as an aggregate for the crosstab.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420461479831/btn_mvup.gif)**Move Up button**

Select to move the selected item higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420453416727/btn_mvdown.gif)**Move Down button**

Select to move the selected item lower in the list.

![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4420453394455/btn_delete.gif)

Removes the selected view element.

**OK**

Applies the settings and closes the dialog box.

**Cancel**

Cancels the settings and closes the dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4420447202071/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420447202455/btn_close.gif)

Ignores the setting and closes this dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683892631-To-Chart-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683893911-Unique-Key-Dialog-Box-Properties)
