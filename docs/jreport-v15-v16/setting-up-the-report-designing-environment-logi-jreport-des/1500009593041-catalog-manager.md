---
title: "Catalog Manager"
id: 1500009593041
section: "Setting Up the Report Designing Environment - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009593041-Catalog-Manager
updated_at: 2021-07-24T05:53:46Z
---

# Catalog Manager

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009571102-Data-Panel)

# Catalog Manager

The Catalog Manager is a useful interface which simplifies the [management of the actual resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009583101-Managing-Data-Resources-in-a-Catalog) you use for creating reports (to open it, select **Home** > **Catalog Manager**, or ****View** > **Catalog Manager****).

![Catalog Manager](https://devnet.logianalytics.com/hc/article_attachments/4404893800599/rptenv_ctlgmngr.gif)

**Toolbar**

* **New**  
   The first button on the toolbar, which may change according to the currently selected object. Usually, this button contains a plus sign. Select this button to create a new object of the selected type. For example, if a query is currently selected, you can select this button to create a new query.
* **Parameter Order**   
   Adjusts the order of parameters displayed in the parameter value specifying page when running any report that uses this catalog. By default parameters are displayed in alphabetic order so End Date would be displayed before Start Date. Since this would be confusing to users, by setting the order in the catalog any report that uses these parameters will see them displayed in the specified order. However, the order specified here can be overridden by specifying the parameter order in the individual report by using Report > Parameter Order. This button is available when the Parameters node or a parameter is selected. For details, see [Editing the Display Sequence of Parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500009590101-Editing-the-Display-Sequence-of-Parameters).
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
   Rename the selected entity
* **Configure Reference**  
   Allows you to select data sources and resource types that you want Logi JReport Designer to monitor. By configuring the reference database you can quickly find out where any resource is used. For details, see [Using a Reference Table to Clarify Resource Relationships](https://devnet.logianalytics.com/hc/en-us/articles/1500009583141-Using-a-Reference-Table-to-Clarify-Resource-Relationships).
* **Refresh Reference**  
   Refreshes the reference relationship information in order to make it consistent with the catalog resources.
* **Export Reference**  
   Exports the reference relationship information to a text file.
* **Options**  
   Opens the [Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009588081-Options-Dialog) dialog to set options for editing a catalog or reports.
* **Data Source Drivers**  
   Manages cached query results. For details, see [Managing cached query results](https://devnet.logianalytics.com/hc/en-us/articles/1500009570622-Cached-Query-Results#Manage).
* **Pre-join**  
   Defines the pre-join paths formed by the relationships among the tables in the selected catalog data source. For details, see [Defining the join relationships between tables](https://devnet.logianalytics.com/hc/en-us/articles/1500009583161-Defining-the-Join-Relationships-Between-Resources).
* **Data Mapping Editor**Maps the data values of resources in a catalog to a certain language. For details, see [Data Mapping Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009590001-Mapping-Data-Values-to-Different-Languages).
* **Filter View**  
   Excludes some elements from the view in the Catalog Manager. For details, see [Filtering Resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009562782-Filtering-Resources).
* **Search**  
   Searches the required data resources in the current catalog. For details, see [Searching for Resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009583201-Searching-for-Resources).
* **Style**  
   Opens the Style Editor for you to [create and edit XSD styles](https://devnet.logianalytics.com/hc/en-us/articles/1500009593261-XSD-Styles). We recommend that you use CSS styles rather than XSD styles.
* **Show**/**Hide Properties**  
   Expands or folds the Properties sheet of the Catalog Manager.
* **Resume**  
   Resumes the guidance workflow. An appropriate guidance dialog is prompted according to the currently selected resource node context.  

  In order to get data ready for creating reports, you should set up a connection, add tables and create a query or business view. All these tasks are now be connected by guidance dialogs to guide users what can be done next. This would be helpful for the new users of Logi JReport Designer without worrying about the lack of reporting knowledge.

  The guidance workflow is enabled by default. You can stop it at any time when you are prompted with the guidance dialog asking you to choose the next work once you finish something. To resume it, select **Resume** on the Catalog Manager toolbar and Logi JReport will prompt you the appropriate guidance dialog according to your current data resource context. For example, if you just finish a business view and then you select Resume, the guidance dialog will be that with options for creating a page report, a web report or going on to create another business view as follows:

  ![A Guidance Dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893800855/rptenv_ctlgmngr_guide.gif)

**Data resources tree**

Lists the data resources in the current catalog in a tree structure. You can add, edit and remove any resources in the tree.

**Properties sheet**

Lists the properties of the selected object. This sheet is hidden by default. To display it, select **Show Properties**  on the Catalog Manager toolbar, or right-click any object and select **Properties** from the shortcut menu.

In order to edit the property values in the Catalog Manager, you need to uncheck **Forbid editing data object properties** in the Catalog category of the Options dialog (this option is checked by default). By unchecking it Logi JReport will remember your choice the next time you open the catalog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009571102-Data-Panel)
