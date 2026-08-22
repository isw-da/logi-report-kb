---
title: "Select Data Source Dialog Box Properties"
id: 1500009776221
section: "Web Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009776221-Select-Data-Source-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:13Z
---

# Select Data Source Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748002-Select-Catalog-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009776241-Select-Field-Dialog-Box-Properties)

# Select Data Source Dialog Box Properties

This topic describes how you can use the Select Data Source dialog box to select the business view fields to display in a report. The dialog box varies according to different sources that you opened it from.

---

When you do any of the following to [create a web report in the quick start way](https://devnet.logianalytics.com/hc/en-us/articles/1500009778861-Quick-Start-with-a-Table-Report):

* In the [Select Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009748002-Select-Catalog-Dialog-Box-Properties) dialog box, select the required catalog and select OK.
* In Web Report Studio, select Menu > File > New Report or select the ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404885307031/btn_newobj.gif) button on the toolbar.
* In the Server Console, open the Resources page, browse to a folder that contains a catalog, and then select New > Web Report on the task bar.

The Select Data Source dialog box contains the following options:

![Select Data Source for Report dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885306135/slctdtsrc.gif)

**Data Source**

Lists the data sources in the specified catalog.

**Change Catalog**

Opens the [Select Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009748002-Select-Catalog-Dialog-Box-Properties) dialog box to choose another catalog to use for the report.

**Resources**

Lists the business views in the selected data source.

* ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404880135447/btn_sort.gif)  
   Sorts the business views listed in the box below in the specified order from the drop-down list:
  + **Predefined Order**  
     Sorts the business views in the order defined in the Business View Editor on Logi Report Designer.
  + **Alphabetical Ascending**   
     Sorts the business views in alphabetically ascending order.
  + **Alphabetical Descending**   
     Sorts the business views in alphabetically descending order.
* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404880135831/btn_srch.gif)  
  Launches the search bar to search for business views.

  See the following options in the search bar:

  ![Quick Search Toolbar](https://devnet.logianalytics.com/hc/article_attachments/4404880162071/btn_srchtlbr.gif)

  + **Text box**  
    Type the text you want to search in the text box. Server lists the values that contain the matched text.
  + **X**  
    Select to close the search bar or clear the typed text.
  + ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/4404885330071/btn_srchtlbr_adv.gif)  
    Select the button and Server displays more search options.
    - **Highlight All**   
      Select if you want to highlight all matched text.
    - **Match Case**   
      Select if you want to search for text that meets the case of the typed text.
    - **Match Whole Word**   
      Select if you want to search for text that looks the same as the typed text.
  + ![Previous Text](https://devnet.logianalytics.com/hc/article_attachments/4404880162711/btn_srchtlbr_prv.gif)  
    When you selected **Highlight All**, you can use this button to go to the previous matched text.
  + ![Next Text](https://devnet.logianalytics.com/hc/article_attachments/4404880162967/btn_srchtlbr_nxt.gif)  
     When you selected **Highlight All**, you can use this button to go to the next matched text.

**Fields**

Select the fields in the selected business view to add to the table.

* **All**Selects/Unselects all the fields in the selected business view.
* ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404880135447/btn_sort.gif)  
   Sorts the objects listed in the box below in the specified order from the drop-down list:

  + **Predefined Order**  
     Sorts the objects in the order defined in the Business View Editor on Logi Report Designer.
  + **Resource Types**  
     Sorts the objects by resource type.
  + **Alphabetical Order**  
     Sorts the objects in alphabetical order. Objects that are not in any category will be sorted first, then the categories, and the objects in each category will also be sorted alphabetically.

  ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404880135831/btn_srch.gif)  
   Launches the [search bar](#Search) to search for objects listed in the box below.

**OK**

Create a table report with the selected fields and closes this dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Displays the help document about this feature.

---

When you drag KPI from the Components panel or ![KPI button](https://devnet.logianalytics.com/hc/article_attachments/4404885316119/btn_kpi.gif) from the visualization toolbar to the destination, the Select Data Source dialog box helps you to select a business view to bind to the KPI and contains the following options:

![Select Data Source for KPI dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885337111/slctdtsrc-kpi.gif)

**Data Source**

Lists the data sources in the specified catalog.

**Resources**

Lists the business views in the selected data source.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404880135447/btn_sort.gif)

Sorts the business views in the specified order from the drop-down list:

* **Predefined Order**  
   Sorts the business views in the order defined in the Business View Editor on Logi Report Designer.
* **Alphabetical Ascending**   
   Sorts the business views in alphabetically ascending order.
* **Alphabetical Descending**   
   Sorts the business views in alphabetically descending order.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404880135831/btn_srch.gif)

Launches the [search bar](#Search) to search for business views.

**OK**

Inserts the KPI in the report while binding the business view to it and closes this dialog box.

**Cancel**

Cancels the insertion of a KPI and closes this dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Cancels the insertion of a KPI and closes this dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748002-Select-Catalog-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009776241-Select-Field-Dialog-Box-Properties)
