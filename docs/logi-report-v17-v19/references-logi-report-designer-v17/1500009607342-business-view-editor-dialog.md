---
title: "Business View Editor Dialog"
id: 1500009607342
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009607342-Business-View-Editor-Dialog
updated_at: 2021-07-24T16:04:59Z
---

# Business View Editor Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009607322-Bursting-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009630421-Category-Options-Dialog)

# Business View Editor Dialog

The Business View Editor helps you to create or edit a [business view](https://devnet.logianalytics.com/hc/en-us/articles/1500009613102-Creating-Business-Views-in-a-Catalog). It appears when you do one of the following:

* Right-click the Business Views node in the Catalog Manager, select New Business View from the shortcut menu, type a name in the displayed dialog and select OK. Then in the Add Tables/Views/Queries dialog, select one resource and then select OK.

  Or if you select more than one resource in the Add Tables/Views/Queries dialog and select OK, then in the Query Editor select the required table columns and join the tables and select OK.
* In the Catalog Manager right-click a business view and select Edit from its shortcut menu.
* Right-click a business view or an element in it and select Edit from the shortcut menu in the Resources box of the Display screen in the map wizard.

![Business View Editor](https://devnet.logianalytics.com/hc/article_attachments/4404911639063/bvedtr.gif)

The following are details about options in the editor:

**Menu**

* **File**
  + **Save**  
     Saves the business view with all the changes made in this editor.
  + **Save As**  
     Saves a copy of the business view with a different name.
  + **Close**  
     Exits this window.
* **New**
  + **Category**  
     Opens the [Category Property](https://devnet.logianalytics.com/hc/en-us/articles/1500009630441-Category-Property-Dialog) dialog to add a category into the business view.
  + **Group**  
     Opens the [New View Element](https://devnet.logianalytics.com/hc/en-us/articles/1500009632741-New-View-Element-Dialog) dialog to add a group object into the business view.
  + **Aggregation**  
     Opens the [New View Element](https://devnet.logianalytics.com/hc/en-us/articles/1500009632741-New-View-Element-Dialog) dialog to add an aggregation object into the business view.
  + **Detail**  
     Opens the [New View Element](https://devnet.logianalytics.com/hc/en-us/articles/1500009632741-New-View-Element-Dialog) dialog to add a detail object into the business view.
  + **Hierarchy**  
     Prompts you to provide a name for the new hierarchy you are going to create.
* **Tools**
  + **Security Configuration**  
    Opens the [Edit Business View Security](https://devnet.logianalytics.com/hc/en-us/articles/1500009607842-Edit-Business-View-Security-Dialog) dialog to configure security for all the business views in the current catalog data source.
  + **Query Editor**  
     Opens the [Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009609882-Query-Editor-Dialog) to edit the data resources used for the business view.
  + **Predefined Filter**  
     Opens the [Predefined Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009609682-Predefined-Filter-Dialog) dialog to add predefined filters to the business view.
* **![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404911621015/___newv17.jpg "New for version 17.")Options**
  + **Auto Add Prefix in Display Names**  
     Similar to the data source property [Use Mapping Name Prefix](https://devnet.logianalytics.com/hc/en-us/articles/1500009634641-Data-Source-Properties#Prefix) which controls whether the table names will be prefixed as "tablename\_" in the default mapping names of their columns, this property decides whether to automatically append the same prefix in the default display names of the view elements in the business view when adding view elements based on the columns. The two properties work independently from each another, which means you can have column names prefixed with corresponding table names in a data source automatically by setting Use Mapping Name Prefix to true, but choose not to have the prefix for view elements by clearing Auto Add Prefix in Display Names.

  By default the property is false. In this case, when a column's mapping name contains the "tablename\_" prefix which however is not automatically generated but user customized and you add a view element based on the column, the prefix will still be removed from the display name of the view element.

  You can also set this option via the [same-name property](https://devnet.logianalytics.com/hc/en-us/articles/1500009634581-Business-View-Properties) of the business view.
* **Help**  
   Displays the help document about this feature.

**Toolbar**

* **Save**  
   Saves the business view with all the changes made in this editor.
* **Delete**  
   Deletes the selected categories, groups, aggregations or details from the business view.
* **New Category**  
   Creates a category in the business view.
* **New Group**   
   Creates a group object in the business view.
* **New Aggregation**  
   Creates an aggregation object in the business view.
* **New Detail**  
   Creates a detail object in the business view.
* **New Hierarchy**  
   Prompts you to provide a name for the new hierarchy you are going to create.
* **![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404911621015/___newv17.jpg "New for version 17.")Select Filter Resources**  
   Opens the [Select Filter Resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009633541-Select-Filter-Resources-Dialog) dialog to customize the view elements that are available when filtering reports created based on the business view.
* **Query Editor**  
   Opens the [Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009609882-Query-Editor-Dialog) to edit the data resources used for the business view.
* **Predefined Filter**  
   Adds predefined filters to the business view.
* **Help**  
   Displays the help document about this feature.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif)  
   Moves the selected objects one step up.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif)  
   Moves the selected objects one step down.

**Resource Objects**

Lists all the data resources that can be used for the business view.

* ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404911593495/btn_sort2.gif)  
   Displays the Sort drop-down menu to sort the resources in the ascending or descending order. The default sort order is controlled by the [Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009609482-Options-Dialog#Sort) option in the Catalog category of the Options dialog. When Sort is not selected in the Options dialog, No Sort is selected by default in the drop-down menu which means the resources are listed in their original order in the database. The change of sort order here is a one-off action and will not be remembered after you exit the Business View Editor.

  **Note:** The logic folder nodes Formulas and Summaries for holding corresponding resources always display together. The sort will be applied separately on them from the other folders in the panel.
* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404911593751/btn_srch.gif)**Search**  
   Opens the search box to search for resources in the panel. To start the search, type in the text you want to search for and the resources containing the matched text will be listed.

  In the search box, there are the following options:

  + ![More Search Option button](https://devnet.logianalytics.com/hc/article_attachments/4404911683351/btn_srchbox_adv.gif)  
     Lists more search options.
    - **Highlight All**   
       Specifies whether to highlight all matched text.
    - **Match Case**   
       Specifies whether to search for text that meets the case of the typed text.
    - **Match Whole Word**   
       Specifies whether to search for text that looks the same as the typed text.
  + ![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404904186775/btn_close1.gif)  
     Closes the search box and cancels the search.
* ![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404904186775/btn_close1.gif)  
   Closes the panel. To display the panel again, select the expand arrow on the left of the Business View panel.

**Business View**

You can add or edit the resources of a business view in this panel. The resources are arranged in a tree structure. Under the root category, categories, view elements and hierarchies can be added. Categories are used as virtual folders to hold sub categories and view elements. View elements and hierarchies can be added in any categories including the root category.

* ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404911593495/btn_sort2.gif)  
  ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404911621015/___newv17.jpg "New for version 17.") Displays the Sort drop-down menu to sort the resources excluding the elements in hierarchies in the ascending or descending order.
* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404911593751/btn_srch.gif)**[Search](#Search)**  
   Opens the search box to search for resources in the panel.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009607322-Bursting-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009630421-Category-Options-Dialog)
