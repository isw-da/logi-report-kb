---
title: "Unique Key Dialog Box Properties"
id: 5741447137815
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741447137815-Unique-Key-Dialog-Box-Properties
updated_at: 2022-10-31T17:17:49Z
---

# Unique Key Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741460447511-To-Crosstab-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741452184343-User-Defined-Function-Editor-Properties)

# Unique Key Dialog Box Properties

This topic describes how you can use the Unique Key dialog box to select a unique key for a real time chart.

Server displays the dialog box when you select **Incremental Fetch** in the **Bind Data** screen of a chart in the [Web Report Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5741437169815-Web-Report-Wizard-Properties#Chart), or select **Incremental Fetch** in the [Insert Chart dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741459162391-Insert-Chart-Dialog-Box-Properties), [Chart Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5741422293143-Chart-Wizard-Properties), or [Convert to Chart dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741449393815-Convert-to-Chart-Dialog-Box-Properties).

![Unique Key dialog](https://devnet.logianalytics.com/hc/article_attachments/9905620541335/unqkey.gif)

**Resources**

Server lists all the elements in the business view used by the real time chart.

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

Select to add the selected fields to the Unique Key box.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/9905574572823/btn_rmvitem.gif)**Remove button**

Select to remove the selected fields from the Unique Key box.

**Unique Key**

Server lists the fields you have added as the unique key, which is used to guarantee there are no two records with the same unique key value in the real time chart.

When you have specified a real time chart with a unique key, each time when the chart automatically updates itself, Server will filter the data that has the same unique key value as the previous loaded data records and only add data with different unique key value to the chart. For instance, if you add the fields Country and Product ID as the unique key of a real time chart, when Server has already loaded a record with the product ID 1 in USA into the chart, it will add no more records of this product ID in USA into the real time chart because they have the same unique key value. The most common usage is with a time field so when a time is part of the unique key the data in the chart will update each time you add new records to the database with more recent times.

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741460447511-To-Crosstab-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741452184343-User-Defined-Function-Editor-Properties)
