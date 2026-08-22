---
title: "Business View Editor Dialog"
id: 1500010064841
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010064841-Business-View-Editor-Dialog
updated_at: 2021-07-24T10:39:08Z
---

# Business View Editor Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010029862-Bursting-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010065241-Category-Options-Dialog)

# Business View Editor Dialog

The Business View Editor helps you to create or edit a [business view](https://devnet.logianalytics.com/hc/en-us/articles/1500010034562-Creating-Business-Views-in-a-Catalog). It appears when you do one of the following:

* Right-click the Business Views node in the Catalog Manager, select New Business View from the shortcut menu, input a name in the displayed dialog and select OK. Then in the Add Tables/Views/Queries dialog, select one resource and then select OK.

  Or if you select more than one resource in the Add Tables/Views/Queries dialog and select OK, then in the Query Editor select the required table columns and join the tables and select OK.
* In the Catalog Manager right-click a business view and select Edit from its shortcut menu.
* Right-click a business view or an element in it and select Edit from the shortcut menu in the Resources box of the Display screen in the map wizard.

![Business View Editor](https://devnet.logianalytics.com/hc/article_attachments/4404901145751/bvedtr.gif)

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
     Opens the [Category Property](https://devnet.logianalytics.com/hc/en-us/articles/1500010065261-Category-Property-Dialog) dialog to add a category into the business view.
  + **Group**  
     Opens the [New View Element](https://devnet.logianalytics.com/hc/en-us/articles/1500010067281-New-View-Element-Dialog) dialog to add a group object into the business view.
  + **Aggregation**  
     Opens the [New View Element](https://devnet.logianalytics.com/hc/en-us/articles/1500010067281-New-View-Element-Dialog) dialog to add an aggregation object into the business view.
  + **Detail**  
     Opens the [New View Element](https://devnet.logianalytics.com/hc/en-us/articles/1500010067281-New-View-Element-Dialog) dialog to add a detail object into the business view.
  + **Hierarchy**  
     Prompts you to provide a name for the new hierarchy you are going to create.
* **Tools**
  + **Security Configuration**  
    Opens the [Edit Business View Security](https://devnet.logianalytics.com/hc/en-us/articles/1500010065501-Edit-Business-View-Security-Dialog) dialog to configure security for all the business views in the current catalog data source.
  + **Query Editor**  
     Opens the [Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500010067501-Query-Editor-Dialog) to edit the data resources used for the business view.
  + **Predefined Filter**  
     Opens the [Predefined Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500010032042-Predefined-Filter-Dialog) dialog to add predefined filters to the business view.
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
* **Query Editor**  
   Opens the [Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500010067501-Query-Editor-Dialog) to edit the data resources used for the business view.
* **Predefined Filter**  
   Adds predefined filters to the business view.
* **Help**  
   Displays the help document about this feature.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif)  
   Moves the selected object one step up. Disabled when the sort order in the Business View panel is set to Ascending or Descending.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif)  
   Moves the selected object one step down. Disabled when the sort order in the Business View panel is set to Ascending or Descending.

**Resource Objects**

Lists all the data resources that can be used for the business view.

* ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404909114391/btn_sort2.gif)  
   Sorts the resources in the ascending or descending order or following the original order as in the database. The default sort order in the panel is controlled by the [Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500010031962-Options-Dialog#Sort) option in the Catalog category of the Options dialog. When Sort is not checked in the Options dialog, the default sort order is No Sort. The change of sort order here is a one-off action and will not be remembered after you exit the Business View Editor.

  **Note:** The logic folder nodes Formulas and Summaries for holding corresponding resources always display together. The sort will be applied separately on them from the other folders in the panel.
* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404909114647/btn_srch.gif)**Search**  
   Opens the search bar to search for resources in the panel. To start the search, type in the text you want to search for and the resources containing the matched text will be listed.
  + ![More Search Option button](https://devnet.logianalytics.com/hc/article_attachments/4404909124247/btn_srchtlbr_adv.gif)  
     Lists more search options.
    - **Highlight All**   
       Specifies whether to highlight all matched text.
    - **Match Case**   
       Specifies whether to search for text that meets the case of the typed text.
    - **Match Whole Word**   
       Specifies whether to search for text that looks the same as the typed text.
  + ![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404901130519/btn_close1.gif)  
     Closes the search bar and cancels the search.
* ![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404901130519/btn_close1.gif)  
   Closes the panel. To display the panel again, select the expand arrow on the left of the Business View panel.

**Business View**

You can add or edit the resources of a business view in this panel. The resources are arranged in a tree structure. Under the root category, categories, view elements and hierarchies can be added. Categories are used as virtual folders to hold sub categories and view elements. View elements and hierarchies can be added in any categories including the root category.

* ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404909114391/btn_sort2.gif)  
   Sorts the resources excluding the elements in hierarchies in the ascending or descending order or following the original order as in the database. The change of sort order here is a one-off action and will not be remembered after you exit the Business View Editor.
* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404909114647/btn_srch.gif)**[Search](#Search)**  
   Opens the search bar to search for resources in the panel.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010029862-Bursting-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010065241-Category-Options-Dialog)
