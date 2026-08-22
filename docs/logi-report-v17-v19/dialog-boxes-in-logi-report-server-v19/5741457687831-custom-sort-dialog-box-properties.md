---
title: "Custom Sort Dialog Box Properties"
id: 5741457687831
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741457687831-Custom-Sort-Dialog-Box-Properties
updated_at: 2022-10-31T17:17:18Z
---

# Custom Sort Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741422256407-Cube-Status-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741457709079-Customize-Chart-Value-Names-Dialog-Box-Properties)

# Custom Sort Dialog Box Properties

You can use the Custom Sort dialog box to [sort the detail data](https://devnet.logianalytics.com/hc/en-us/articles/5741476545943-Inserting-Components-in-Web-Report#Sort) in a table, [sort a specific group](https://devnet.logianalytics.com/hc/en-us/articles/5741476545943-Inserting-Components-in-Web-Report#GroupSort) in a table or chart, or sort the values of a parameter that is bound with a column, by sorting the values of other fields. This topic describes the properties in the dialog box.

Server displays the dialog box when you do one of the following:

* Select **Sort Fields By** in the Display tab of the [Table Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5741447063959-Table-Wizard-Properties#Display) or [Insert Table dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741451225111-Insert-Table-Dialog-Box-Properties#Display), or in the Display tab for table in the [Web Report Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5741437169815-Web-Report-Wizard-Properties#Table).
* Select **Custom Sort** from the Sort column in the Group/Columns tab of the [Table Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5741447063959-Table-Wizard-Properties), [Insert Table dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741451225111-Insert-Table-Dialog-Box-Properties), or [Convert to Table dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428562967-Convert-to-Table-Dialog-Box-Properties), or in the Group/Columns tab for table in the [Web Report Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5741437169815-Web-Report-Wizard-Properties#Table).
* Select **Sort Field By** in the Details tab for table in the [Web Report Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5741437169815-Web-Report-Wizard-Properties#Table), or in the Details tab of the [Convert to Table dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428562967-Convert-to-Table-Dialog-Box-Properties).
* Select **Custom Sort** from the **Based On** list in the [Category Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741434586391-Category-Options-Dialog-Box-Properties), [Group Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741459041175-Group-Options-Dialog-Box-Properties), or [Series Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741459816727-Series-Options-Dialog-Box-Properties).
* Select **Sort By** from the Sort list in the [Add Parameter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428253975-Add-Parameter-Dialog-Box-Properties) and [Edit Parameter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741449845271-Edit-Parameter-Dialog-Box-Properties).

![Custom Sort dialog](https://devnet.logianalytics.com/hc/article_attachments/9905632102039/cstmsrt.gif)

**Resources**

Select a field whose values you want to sort. If you open the dialog box from the [Web Report Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5741437169815-Web-Report-Wizard-Properties), Server also lists the dynamic resources in the Resources box.

![Edit button](https://devnet.logianalytics.com/hc/article_attachments/9905619243799/btn_wbrpt_edit.gif)**Edit button**

Select to edit the selected dynamic resource.

![Delete button](https://devnet.logianalytics.com/hc/article_attachments/9905578411927/btn_delete.gif)**Remove button**

Select to remove the selected dynamic resource.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/9905577646231/btn_sort.gif) **Sort button**

Select an order for sorting the resources in the business view. The order applies to all the resource trees where you see the business view in Web Report Studio.

The order can be one of the following:

* **Predefined Order**  
  Select if you want to sort the resources in the order as in the Business View Editor of Designer.
* **Resource Types**  
  Select if you want to sort the resources by the resource type. Namely, category objects come first, then group objects, then aggregation objects, and at last detail objects.
* **Alphabetical Order**  
  Select if you want to sort the resources in alphabetical order. Logi Report sorts the resources that are not in any category first, and then the categories. It also sorts the resources in each category alphabetically.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/9905577660311/btn_srch.gif)**Search button**

Select to launch the search bar to search for fields.

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

Select to add the selected field as the sort-by field.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/9905574572823/btn_rmvitem.gif)**Remove button**

Select to remove the selected sort-by field.

**Sort By**

Server lists the fields whose values you want to sort.

**Sort**

Select the order for sorting the values of a sort-by field.

* **Ascend**  
   Select if you want to sort the field values in ascending order.
* **Descend**  
   Select if you want to sort the field values in descending order.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9905613125783/btn_mvup.gif)**Move Up button**

Select to move the selected item higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9905575169431/btn_mvdown.gif)**Move Down button**

Select to move the selected item lower in the list.

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741422256407-Cube-Status-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741457709079-Customize-Chart-Value-Names-Dialog-Box-Properties)
