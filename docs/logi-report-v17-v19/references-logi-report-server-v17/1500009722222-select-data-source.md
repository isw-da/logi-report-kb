---
title: "Select Data Source"
id: 1500009722222
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009722222-Select-Data-Source
updated_at: 2021-07-25T07:19:12Z
---

# Select Data Source

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009722202-Select-Catalog)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009749341-Select-Field)

# Select Data Source

The Select Data Source dialog box is used to select the business view fields to display in a report. It varies according to different sources it is opened from.

---

When you do any of the following to [create a web report in the quick start way](https://devnet.logianalytics.com/hc/en-us/articles/1500009751621-Quick-Start-with-a-Table-Report):

* In the [Select Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009722202-Select-Catalog) dialog box, select the required catalog and select OK.
* In Web Report Studio, select Menu > File > New Report or select the ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936714519/btn_newobj.gif) button on the toolbar.
* In the Logi Report Server console, open the Resources page, browse to a folder that contains a catalog, and then select New > Web Report on the task bar.

The Select Data Source dialog box contains the following options:

![Select Data Source for Report dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936713879/slctdtsrc.gif)

**Data Source**

Lists the data sources in the specified catalog.

**Change Catalog**

Opens the [Select Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009722202-Select-Catalog) dialog box to choose another catalog to use for the report.

**Resources**

Lists the business views in the selected data source.

* ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404936713367/btn_sort.gif)  
   Sorts the business views listed in the box below in the specified order from the drop-down list:
  + **Predefined Order**  
     Sorts the business views in the order defined in the Business View Editor on Logi Report Designer.
  + **Alphabetical Ascending**   
     Sorts the business views in alphabetically ascending order.
  + **Alphabetical Descending**   
     Sorts the business views in alphabetically descending order.
* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404936713623/btn_srch.gif)  
  Launches the search bar to search for business views.

  The following shows the options in the search bar:

  ![Quick Search Toolbar](https://devnet.logianalytics.com/hc/article_attachments/4404936734231/btn_srchtlbr.gif)

  + **Text box**  
    Type in the text you want to search in the text box and the values containing the matched text will be listed.
  + **X**  
    Closes the search bar.
  + ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/4404942460951/btn_srchtlbr_adv.gif)  
    Lists more search options.
    - **Highlight All**   
      Specifies whether to highlight all matched text.
    - **Match Case**   
       Specifies whether to search for text that meets the case of the typed text.
    - **Match Whole Word**   
      Specifies whether to search for text that looks the same as the typed text.
  + ![Previous Text](https://devnet.logianalytics.com/hc/article_attachments/4404936734487/btn_srchtlbr_prv.gif)  
    When Highlight All is selected, you can use this button to go to the previous matched text.
  + ![Next Text](https://devnet.logianalytics.com/hc/article_attachments/4404936734743/btn_srchtlbr_nxt.gif)  
     When Highlight All is selected, you can use this button to go to the next matched text.

**Fields**

Select the fields in the selected business view to add to the table.

* **All**Selects/Unselects all the fields in the selected business view.
* ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404936713367/btn_sort.gif)  
   Sorts the objects listed in the box below in the specified order from the drop-down list:

  + **Predefined Order**  
     Sorts the objects in the order defined in the Business View Editor on Logi Report Designer.
  + **Resource Types**  
     Sorts the objects by resource type.
  + **Alphabetical Order**  
     Sorts the objects in alphabetical order. Objects that are not in any category will be sorted first, then the categories, and the objects in each category will also be sorted alphabetically.

  ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404936713623/btn_srch.gif)  
   Launches the [search bar](#Search) to search for objects listed in the box below.

**OK**

Create a table report with the selected fields and closes this dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404936816535/btn_help.gif)

Displays the help document about this feature.

---

When you drag KPI from the Components panel or ![KPI button](https://devnet.logianalytics.com/hc/article_attachments/4404936743063/btn_kpi.gif) from the visualization toolbar to the destination, the Select Data Source dialog box helps you to select a business view to bind to the KPI and contains the following options:

![Select Data Source for KPI dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942465047/slctdtsrc-kpi.gif)

**Data Source**

Lists the data sources in the specified catalog.

**Resources**

Lists the business views in the selected data source.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404936713367/btn_sort.gif)

Sorts the business views in the specified order from the drop-down list:

* **Predefined Order**  
   Sorts the business views in the order defined in the Business View Editor on Logi Report Designer.
* **Alphabetical Ascending**   
   Sorts the business views in alphabetically ascending order.
* **Alphabetical Descending**   
   Sorts the business views in alphabetically descending order.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404936713623/btn_srch.gif)

Launches the [search bar](#Search) to search for business views.

**OK**

Inserts the KPI in the report while binding the business view to it and closes this dialog box.

**Cancel**

Cancels the insertion of a KPI and closes this dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404936816535/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404942519575/btn_close.gif)

Cancels the insertion of a KPI and closes this dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009722202-Select-Catalog)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009749341-Select-Field)
