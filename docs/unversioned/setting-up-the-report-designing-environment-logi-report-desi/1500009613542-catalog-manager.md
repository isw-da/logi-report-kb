---
title: "Catalog Manager"
id: 1500009613542
section: "Setting Up the Report Designing Environment - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009613542-Catalog-Manager
updated_at: 2021-07-24T16:03:18Z
---

# Catalog Manager

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009636281-Data-Panel)

# Catalog Manager

The Catalog Manager is a useful interface which simplifies the [management of the data resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009605302-Managing-the-Data-Resources-in-a-Catalog) you use for creating reports (to open it, select **Home**/**View** > **Catalog Manager**, or the name of the catalog file on the Logi Report Designer title bar).

![Catalog Manager](https://devnet.logianalytics.com/hc/article_attachments/4404911592727/rptenv_ctlgmngr.gif)

**Toolbar**

* **New**  
   The first button on the toolbar, which may change according to the currently selected object. Usually, this button contains a plus sign. Select this button to create a new object of the selected type. For example, if a query is currently selected, you can select this button to create a new query.
* **Parameter Order**  
   This button is available when the Parameters node or a parameter is selected. It helps you to adjust the order of parameters displayed in the parameter value specifying page when running any report that uses this catalog. However, the order specified here can be overridden by specifying the parameter order in the individual report by using Report > Parameter Order. For details, see [Customizing the display order of parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500009634541-Specifying-Parameter-Values#Order).
* **Save Catalog**  
   Saves the current catalog.
* **Paste**  
   Fetches the entity from the clipboard and pastes it in a suitable node.
* **Edit**  
   Open the corresponding editor or dialog for you to edit the selected entity.
* **Copy**  
   Copies the selected entity to the clipboard.
* **Delete**  
   Deletes the selected entity.
* **Rename**  
   Rename the selected entity.
* **Configure Reference**  
   Allows you to select data sources and resource types that you want Logi Report Designer to monitor. By configuring the reference database you can quickly find out where any resource is used. For details, see [Clarifying the Reference Relationships Between Resources in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009605342-Clarifying-the-Reference-Relationships-Between-Resources-in-a-Catalog).
* **Refresh Reference**  
   Refreshes the reference relationship information in order to make it consistent with the catalog resources.
* **Export Reference**  
   Exports the reference relationship information to a text file.
* **Options**  
   Opens the [Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009609482-Options-Dialog) dialog to set options for editing a catalog or reports.
* **Data Source Drivers**  
   Opens the [Data Source Drivers](https://devnet.logianalytics.com/hc/en-us/articles/1500009630541-Data-Source-Drivers-Dialog) dialog for [generating data source drivers for cached query results](https://devnet.logianalytics.com/hc/en-us/articles/1500009635961-Cached-Query-Results#Manage).
* **Pre-join**  
   Defines the pre-join paths formed by the relationships among the tables in the selected catalog data source. For details, see [Editing Pre-joins in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009605262-Editing-Pre-joins-in-a-Catalog).
* **Data Mapping Editor**  
   Maps the data values of resources in a catalog to a certain language. For details, see [Data Mapping Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009634461-Mapping-Data-Values-to-Different-Languages).
* **Filter View**  
   Excludes some elements from the view in the Catalog Manager. For details, see [Filtering the data resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009605302-Managing-the-Data-Resources-in-a-Catalog#Filter).
* **Search**  
  [Searches the required data resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009605302-Managing-the-Data-Resources-in-a-Catalog#Search) in the catalog in the advanced way.
* **Style**  
   Opens the Style Editor for you to [create and edit XSD styles](https://devnet.logianalytics.com/hc/en-us/articles/1500009613482-XSD-Styles). We recommend that you use CSS styles rather than XSD styles.
* **Show**/**Hide Properties**  
   Expands or folds the Properties sheet of the Catalog Manager.
* **Resume**  
   Resumes the guidance workflow. An appropriate guidance dialog is prompted according to the currently selected resource node context.  

  In order to get data ready for creating reports, you should set up a connection, add tables and create a query or business view. All these tasks are now be connected by guidance dialogs to guide users what can be done next. This would be helpful for the new users of Logi Report Designer without worrying about the lack of reporting knowledge.

  The guidance workflow is enabled by default. You can stop it at any time when you are prompted with the guidance dialog asking you to choose the next work once you finish something. To resume it, select **Resume** on the Catalog Manager toolbar and Logi Report will prompt you the appropriate guidance dialog according to your current data resource context. For example, if you just finish a business view and then you select Resume, the guidance dialog will be that with options for creating a page report, a web report or going on to create another business view as follows:

  ![A Guidance Dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911592983/rptenv_ctlgmngr_guide.gif)

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404911593495/btn_sort2.gif)**Sort**

[Sorts the resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009605302-Managing-the-Data-Resources-in-a-Catalog#Sort) in the catalog.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404911593751/btn_srch.gif)**Search**

Opens the search bar to [searches for data resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009605302-Managing-the-Data-Resources-in-a-Catalog#Search) in the catalog in the quick way.

**Data resource tree**

Lists the data resources in the current catalog in a tree structure. You can add, edit and remove any resources in the tree.

**Properties sheet**

Lists the properties of the selected object. This sheet is hidden by default. To display it, select **Show Properties**  on the Catalog Manager toolbar, or right-click any object and select **Properties** from the shortcut menu.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009636281-Data-Panel)
