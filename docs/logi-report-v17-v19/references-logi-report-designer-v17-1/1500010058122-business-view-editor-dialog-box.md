---
title: "Business View Editor Dialog Box"
id: 1500010058122
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010058122-Business-View-Editor-Dialog-Box
updated_at: 2021-07-23T19:15:04Z
---

# Business View Editor Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058102-Bursting-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058442-Category-Options-Dialog-Box)

# Business View Editor Dialog Box

You can use the Business View Editor dialog box to create or edit a [business view](https://devnet.logianalytics.com/hc/en-us/articles/1500010101061-Creating-Business-Views-in-a-Catalog). This topic describes the options in the dialog box.

Designer displays the Business View Editor dialog box when you do one of the following:

* Right-click the Business Views node in the Catalog Manager, select New Business View from the shortcut menu, type a name in the displayed dialog box and select OK. Then in the Add Tables/Views/Queries dialog box, select one resource and select OK.

  Or if you select more than one resource in the Add Tables/Views/Queries dialog box and select OK, then in the Query Editor dialog box, select the required table columns and join the tables and select OK.
* In the Catalog Manager, right-click a business view and select Edit from its shortcut menu.
* Right-click a business view or an element in it and select Edit from the shortcut menu in the Resources box of the Display screen in the map wizard.

![Business View Editor](https://devnet.logianalytics.com/hc/article_attachments/4404848440087/bvedtr.gif)

You see the following options in the dialog box:

**Menu**

* **File**
  + **Save**  
    Select to save the business view with all the changes made in this editor.
  + **Save As**  
    Select to save a copy of the business view with a different name.
  + **Close**  
    Select to exit the dialog box.
* **New**
  + **Category**  
    Select to open the [Category Property dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058462-Category-Property-Dialog-Box) to add a category into the business view.
  + **Group**  
    Select to open the [New View Element dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098101-New-View-Element-Dialog-Box) to add a group object into the business view.
  + **Aggregation**  
    Select to open the [New View Element dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098101-New-View-Element-Dialog-Box) to add an aggregation object into the business view.
  + **Detail**  
    Select to open the [New View Element dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098101-New-View-Element-Dialog-Box) to add a detail object into the business view.
  + **Hierarchy**  
    Select it and Designer prompts you to provide a name for the new hierarchy you are going to create.
* **Tools**
  + **Security Configuration**  
    Select to open the [Edit Business View Security dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096181-Edit-Business-View-Security-Dialog-Box) to configure security for all the business views in the current catalog data source.
  + **Query Editor**  
    Select to open the [Query Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098321-Query-Editor-Dialog-Box) to edit the data resources used for the business view.
  + **Predefined Filter**  
    Select to open the [Predefined Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060142-Predefined-Filter-Dialog-Box) to add predefined filters to the business view.
* **Options**
  + **Auto Add Prefix in Display Names**  
    Similar to the data source property [Use Mapping Name Prefix](https://devnet.logianalytics.com/hc/en-us/articles/1500010061362-Data-Source-Properties#Prefix) which controls whether to add "tablename\_" as the prefix of the table names in the default mapping names of their columns, this property determines whether to automatically append the same prefix in the default display names of the view elements in the business view when you add view elements based on the columns. The two properties work independently from each another, which means you can have column names prefixed with corresponding table names in a data source automatically by setting Use Mapping Name Prefix to true, but choose not to have the prefix for view elements by clearing Auto Add Prefix in Display Names.

  By default, this option is unselected. In this case, when a column's mapping name contains the "tablename\_" prefix which however is not automatically generated but user customized and you add a view element based on the column, Designer still removes the prefix from the display name of the view element.

  You can also set this option via the [same-name property](https://devnet.logianalytics.com/hc/en-us/articles/1500010099841-Business-View-Properties) of the business view.
* **Help**  
  Select to view information about the dialog box.

**Toolbar**

* **Save**  
  Select to save the business view with all the changes made in this editor.
* **Delete**  
  Select to delete the specified categories, groups, aggregations, or details from the business view.
* **New Category**  
  Select to create a category in the business view.
* **New Group**   
  Select to create a group object in the business view.
* **New Aggregation**  
  Select to create an aggregation object in the business view.
* **New Detail**  
  Select to create a detail object in the business view.
* **New Hierarchy**  
  Select it and Designer prompts you to provide a name for the new hierarchy you are going to create.
* **Select Filter Resources**  
  Select to open the [Select Filter Resources dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098681-Select-Filter-Resources-Dialog-Box) to customize the view elements that are available when you filter reports which use the business view.
* **Query Editor**  
  Select to open the [Query Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098321-Query-Editor-Dialog-Box) to edit the data resources used for the business view.
* **Predefined Filter**  
  Select to add predefined filters to the business view.
* **Help**  
  Select to view information about the dialog box.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**  
  Select to move the specified objects to a higher position.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**  
  Select to move the specified objects to a lower position.

**Resource Objects**

The panel lists all the data resources that you can use for the business view.

* ![Sort icon](https://devnet.logianalytics.com/hc/article_attachments/4404848378007/btn_sort2.gif)**Sort icon**  
  Select to display the Sort drop-down menu to sort the resources in the ascending or descending order. The default sort order is controlled by the [Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500010098161-Options-Dialog-Box#Sort) option in the Catalog category of the Options dialog box. If you do not select Sort in the Options dialog box, Designer selects No Sort by default in the drop-down menu which means the resources are listed in their original order in the database. The change of sort order here is a one-off action, meaning Designer does not save it after you exit the dialog box.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) The logic folder nodes Formulas and Summaries for holding corresponding resources always display together. Designer applies the sort separately on them from the other folders in the panel.
* ![Search icon](https://devnet.logianalytics.com/hc/article_attachments/4404856807959/btn_srch.gif)**Search icon**  
  Select to open the search box to search for resources in the panel. To start searching, type the text you want to search for in the search box and Designer lists the resources containing the matched text.

  You can make use of the following options in the search box:

  + ![More Search Option button](https://devnet.logianalytics.com/hc/article_attachments/4404848393111/btn_srchbox_adv.gif)**Drop-down icon**  
    Select to list more search options.
    - **Highlight All**   
      Select to highlight all matched text.
    - **Match Case**   
      Select to search for text that meets the case of the typed text.
    - **Match Whole Word**   
      Select to search for text that looks the same as the typed text.
  + ![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404856816535/btn_close1.gif)**Delete icon**  
    Select to close the search box and cancel the search.
* ![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404856816535/btn_close1.gif)  
  Select to close the panel. To display the panel again, select the expand arrow on the left of the Business View panel.

**Business View**

You can add or edit the resources of a business view in this panel. Designer arranges the resources in a tree structure. Under the root category, you can add categories, view elements, and hierarchies. You can use categories as virtual folders to hold sub categories and view elements. You can add view elements and hierarchies in any categories including the root category.

* ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404848378007/btn_sort2.gif)**Sort icon**  
  Select to display the Sort drop-down menu to sort the resources excluding the elements in hierarchies in the ascending or descending order.
* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404856807959/btn_srch.gif)**Search icon**  
  Select to open the search box to search for resources in the panel. To start searching, type the text you want to search in the search box for and Designer lists the resources containing the matched text.

You can make use of the following options in the search box:

+ ![More Search Option button](https://devnet.logianalytics.com/hc/article_attachments/4404848393111/btn_srchbox_adv.gif)**Drop-down icon**  
  Select to list more search options.
  - **Highlight All**   
    Select to highlight all matched text.
  - **Match Case**   
    Select to search for text that meets the case of the typed text.
  - **Match Whole Word**   
    Select to search for text that looks the same as the typed text.
+ ![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404856816535/btn_close1.gif)**Delete icon**  
  Select to close the search box and cancel the search.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058102-Bursting-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058442-Category-Options-Dialog-Box)
