---
title: "Custom Sort Dialog Box Properties"
id: 4405690573719
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690573719-Custom-Sort-Dialog-Box-Properties
updated_at: 2022-01-27T07:59:13Z
---

# Custom Sort Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683793303-Cube-Status-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683804695-Customize-Chart-Value-Names-Dialog-Box-Properties)

# Custom Sort Dialog Box Properties

You can use the Custom Sort dialog box to [sort the detail data](https://devnet.logianalytics.com/hc/en-us/articles/4405684040855-Inserting-Components-in-Web-Report#Sort) in a table, [sort a specific group](https://devnet.logianalytics.com/hc/en-us/articles/4405684040855-Inserting-Components-in-Web-Report#GroupSort) in a table or chart, or sort the values of a parameter that is bound with a column, by sorting the values of other fields. This topic describes the properties in the dialog box.

Server displays the dialog box when you do one of the following:

* Select **Sort Fields By** in the Display tab of the [Table Wizard](https://devnet.logianalytics.com/hc/en-us/articles/4405690612631-Table-Wizard-Properties#Display) or [Insert Table dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683861655-Insert-Table-Dialog-Box-Properties#Display), or in the Display tab for table in the [Web Report Wizard](https://devnet.logianalytics.com/hc/en-us/articles/4405690615447-Web-Report-Wizard-Properties#Table).
* Select **Custom Sort** from the Sort column in the Group/Columns tab of the [Table Wizard](https://devnet.logianalytics.com/hc/en-us/articles/4405690612631-Table-Wizard-Properties), [Insert Table dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683861655-Insert-Table-Dialog-Box-Properties), or [Convert to Table dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683800343-Convert-to-Table-Dialog-Box-Properties), or in the Group/Columns tab for table in the [Web Report Wizard](https://devnet.logianalytics.com/hc/en-us/articles/4405690615447-Web-Report-Wizard-Properties#Table).
* Select **Sort Field By** in the Details tab for table in the [Web Report Wizard](https://devnet.logianalytics.com/hc/en-us/articles/4405690615447-Web-Report-Wizard-Properties#Table), or in the Details tab of the [Convert to Table dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683800343-Convert-to-Table-Dialog-Box-Properties).
* Select **Custom Sort** from the **Based On** list in the [Category Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683806743-Category-Options-Dialog-Box-Properties), [Group Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405690591895-Group-Options-Dialog-Box-Properties), or [Series Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683875351-Series-Options-Dialog-Box-Properties).
* Select **Sort By** from the Sort list in the [Add Parameter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683788823-Add-Parameter-Dialog-Box-Properties) and [Edit Parameter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405690577687-Edit-Parameter-Dialog-Box-Properties).

![Custom Sort dialog](https://devnet.logianalytics.com/hc/article_attachments/4420447077783/cstmsrt.gif)

**Resources**

Select a field whose values you want to sort. If you open the dialog box from the [Web Report Wizard](https://devnet.logianalytics.com/hc/en-us/articles/4405690615447-Web-Report-Wizard-Properties), Server also lists the dynamic resources in the Resources box.

![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4420447073943/btn_wbrpt_edit.gif)**Edit button**

Select to edit the selected dynamic resource.

![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4420453394455/btn_delete.gif)**Remove button**

Select to remove the selected dynamic resource.

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

Select to launch the search bar to search for fields.

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

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4420461488151/btn_additem.gif)**Add button**

Select to add the selected field as the sort-by field.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4420447082647/btn_rmvitem.gif)**Remove button**

Select to remove the selected sort-by field.

**Sort By**

Server lists the fields whose values you want to sort.

**Sort**

Select the order for sorting the values of a sort-by field.

* **Ascend**  
   Select if you want to sort the field values in ascending order.
* **Descend**  
   Select if you want to sort the field values in descending order.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420461479831/btn_mvup.gif)**Move Up button**

Select to move the selected item higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420453416727/btn_mvdown.gif)**Move Down button**

Select to move the selected item lower in the list.

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4420447202071/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420447202455/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683793303-Cube-Status-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683804695-Customize-Chart-Value-Names-Dialog-Box-Properties)
