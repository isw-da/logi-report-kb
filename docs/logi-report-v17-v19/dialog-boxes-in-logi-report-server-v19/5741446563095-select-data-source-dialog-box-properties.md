---
title: "Select Data Source Dialog Box Properties"
id: 5741446563095
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741446563095-Select-Data-Source-Dialog-Box-Properties
updated_at: 2022-10-31T17:17:42Z
---

# Select Data Source Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741451626263-Select-Catalog-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741436598295-Select-Field-Dialog-Box-Properties)

# Select Data Source Dialog Box Properties

This topic describes how you can use the Select Data Source dialog box to select the business view fields to display in a report. The dialog box varies according to different sources that you opened it from.

---

When you do any of the following to [create a table report using the quick start method](https://devnet.logianalytics.com/hc/en-us/articles/5741476791831-Quick-Start-with-a-Table-Report):

* In the [Select Catalog dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741451626263-Select-Catalog-Dialog-Box-Properties), select the required catalog and select OK.
* In Web Report Studio, select Menu > File > New Report or select the New Report button![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905577927831/btn_newobj.gif) on the toolbar.
* On the Server Console, open the Resources page, browse to a folder that contains a catalog, and then select New > Web Report on the task bar.

The Select Data Source dialog box looks like this:

![Select Data Source for Report dialog](https://devnet.logianalytics.com/hc/article_attachments/9905577679511/slctdtsrc.gif)

**Data Source**

Select a data source or dataset in the specified catalog.

**Change Catalog**

Select to open the [Select Catalog dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741451626263-Select-Catalog-Dialog-Box-Properties) to choose another catalog to use for the report.

**Resources**

Select a business view in the selected data source or the business view of the dataset.

* ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/9905577646231/btn_sort.gif)**Sort button**  
   Select an order from the drop-down list to sort the listed business views with:
  + **Predefined Order**  
     Select to sort the business views in the order that you defined in the Business View Editor in Logi Report Designer.
  + **Alphabetical Ascending**  
     Select to sort the business views in alphabetically ascending order.
  + **Alphabetical Descending**  
     Select to sort the business views in alphabetically descending order.
* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/9905577660311/btn_srch.gif)**Search button**  
  Select to launch the search bar to search for business views.

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

**Fields**

Select the fields in the selected business view that you want to add to the table.

* **All**  
  Select/Clear all the fields in the selected business view.
* ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/9905577646231/btn_sort.gif)**Sort button**  
   Select an order from the drop-down list to sort the listed fields with:

  + **Predefined Order**  
     Select to sort the objects in the order that you defined in the Business View Editor in Logi Report Designer.
  + **Resource Types**  
     Select to sort the objects by resource type.
  + **Alphabetical Order**  
     Select to sort the objects in alphabetical order. Server first sort objects that are not in any category, then the categories, and the objects in each category alphabetically.

  ![Search button](https://devnet.logianalytics.com/hc/article_attachments/9905577660311/btn_srch.gif)**Search button**  
   Select to launch the [search bar](#Search) to search for objects listed in the box.

**OK**

Select to create a table report with the selected fields and close the dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the dialog box.

---

When you drag KPI from the Components panel or ![KPI button](https://devnet.logianalytics.com/hc/article_attachments/9905629364503/btn_kpi.gif) from the visualization toolbar to the destination, the Select Data Source dialog box helps you select a business view to bind to the KPI and looks like this:

![Select Data Source for KPI dialog](https://devnet.logianalytics.com/hc/article_attachments/9905632928663/slctdtsrc-kpi.gif)

**Data Source**

Select a data source or dataset in the specified catalog.

**Resources**

Select a business view in the selected data source or the business view of the dataset.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/9905577646231/btn_sort.gif)**Sort button**

Select an order from the drop-down list to sort the business views with:

* **Predefined Order**  
   Select to sort the business views in the order that you defined in the Business View Editor in Designer.
* **Alphabetical Ascending**   
   Select to sort the business views in alphabetically ascending order.
* **Alphabetical Descending**   
   Select to sort the business views in alphabetically descending order.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/9905577660311/btn_srch.gif)**Search button**

Select to launch the [search bar](#Search) to search for business views.

**OK**

Select to insert the KPI in the report while binding the business view to it and close the dialog box.

**Cancel**

Select to close the dialog box without inserting a KPI.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to close the dialog box without inserting a KPI.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741451626263-Select-Catalog-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741436598295-Select-Field-Dialog-Box-Properties)
