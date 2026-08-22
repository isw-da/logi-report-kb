---
title: "Unique Key Dialog Box Properties"
id: 4405683893911
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683893911-Unique-Key-Dialog-Box-Properties
updated_at: 2022-01-27T07:59:31Z
---

# Unique Key Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690613527-To-Crosstab-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690614423-User-Defined-Function-Editor-Properties)

# Unique Key Dialog Box Properties

This topic describes how you can use the Unique Key dialog box to select a unique key for a real time chart.

Server displays the dialog box when you select the **Incremental Fetch** button in the **Bind Data** screen of a chart in the [Web Report Wizard](https://devnet.logianalytics.com/hc/en-us/articles/4405690615447-Web-Report-Wizard-Properties#Chart), or select the button in the [Insert Chart](https://devnet.logianalytics.com/hc/en-us/articles/4405690593815-Insert-Chart-Dialog-Box-Properties) dialog box, [Chart Wizard](https://devnet.logianalytics.com/hc/en-us/articles/4405683794583-Chart-Wizard-Properties), or [Convert to Chart](https://devnet.logianalytics.com/hc/en-us/articles/4405683797655-Convert-to-Chart-Dialog-Box-Properties) dialog box.

![Unique Key dialog](https://devnet.logianalytics.com/hc/article_attachments/4420447082903/unqkey.gif)

**Resources**

Lists all the elements in the business view used by the real time chart.

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

Adds the selected fields to the Unique Key box.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4420447082647/btn_rmvitem.gif)

Removes the selected from the Unique Key box if they are not required.

**Unique Key**

Lists the fields you have added as the unique key, which is used to guarantee there are no two records with the same unique key value in the real time chart.

When a real time chart is specified with a unique key, each time when the chart automatically updates itself, the data that has the same unique key value as the previous loaded data records will be filtered and only data with different unique key value will be added to the chart. For instance, if you add the fields Country and Product ID as the unique key of a real time chart, when a record with the product ID 1 in USA has already been loaded into the chart, no more records of this product ID in USA will be added to the real time chart because they have the same unique key value. The most common usage is with a time field so when a time is part of the unique key the data in the chart will be updated each time new records are added to the database with more recent times.

**OK**

Applies the settings and closes this dialog box.

**Cancel**

Cancels the settings and closes this dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4420447202071/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420447202455/btn_close.gif)

Ignores the setting and closes this dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690613527-To-Crosstab-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690614423-User-Defined-Function-Editor-Properties)
