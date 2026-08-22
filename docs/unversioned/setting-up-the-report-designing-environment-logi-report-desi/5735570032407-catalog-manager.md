---
title: "Catalog Manager"
id: 5735570032407
section: "Setting Up the Report Designing Environment - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735570032407-Catalog-Manager
updated_at: 2022-11-02T08:23:15Z
---

# Catalog Manager

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735576969879-Data-Panel)

# Catalog Manager

The Catalog Manager is a useful interface that simplifies the [management of the data resources](https://devnet.logianalytics.com/hc/en-us/articles/5735526919831-Managing-the-Data-Resources-in-a-Catalog) you use for creating reports (to open it, navigate to **Home**/**View** > **Catalog Manager**, or select the name of the catalog file on the Designer top banner). This topic introduces the usages of the toolbar buttons, resource tree, and Properties sheet of the Catalog Manager.

![Catalog Manager](https://devnet.logianalytics.com/hc/article_attachments/9898421864087/rptenv_ctlgmngr.gif)

**Toolbar**

The toolbar contains the following commands:

* **New**  
  The first button on the toolbar, which changes according to the currently selected object. Usually, this button contains a plus sign. You can select it to create a new object of the specified type. For example, if you select a query, you can select this button to create a new query.
* **Parameter Order**  
  Designer displays this button when you select the Parameters node or a parameter. You can use it to [adjust the order of the parameters](https://devnet.logianalytics.com/hc/en-us/articles/5735525892247-Specifying-Parameter-Values#Order) in the parameter value specifying page when running any report that uses this catalog. However, the order specified here can be overridden by the order defined for any individual report.
* **Save Catalog**  
  Select to save the current catalog.
* **Paste**  
  Select to fetch the entity from the clipboard and pastes it in a suitable node.
* **Edit**  
  Select to open the corresponding dialog box for you to edit the selected entity.
* **Copy**  
  Select to copy the specified entity to the clipboard.
* **Delete**  
  Select to delete the specified entity.
* **Rename**  
  Select to rename the specified entity.
* **Configure Reference**  
  Select to specify the data sources and resource types that you want Designer to monitor. By configuring the reference table, you can quickly find out where any resource is used. See [Clarifying Resource Reference Relationships in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/5735526938391-Clarifying-the-Reference-Relationships-Between-Resources-in-a-Catalog).
* **Refresh Reference**  
  Select to refresh the reference relationship information in order to make it consistent with the catalog resources.
* **Export Reference**  
  Select to export the reference relationship information to a text file.
* **Options**  
  Select to open the [Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524192535-Options-Dialog-Box) to set options for editing a catalog or reports.
* **Data Source Drivers**  
  Select open the [Data Source Drivers dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735528973335-Data-Source-Drivers-Dialog-Box) for [generating data source drivers for cached query results](https://devnet.logianalytics.com/hc/en-us/articles/5735586187287-Working-with-Cached-Query-Results#Manage).
* **Pre-join**  
  Select to define the pre-join paths formed by relationships between tables in the selected catalog data source. See [Editing Pre-joins in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/5735511752087-Editing-Pre-joins-in-a-Catalog).
* **Data Mapping Editor**  
  Select to map the data values of resources in a catalog to a certain language. See [Data Mapping Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735553821719-Mapping-Data-Values-to-Different-Languages).
* **Filter View**  
  Select to [exclude some elements](https://devnet.logianalytics.com/hc/en-us/articles/5735526919831-Managing-the-Data-Resources-in-a-Catalog#Filter) from the view in the Catalog Manager.
* **Search**  
  Select to [search the required data resources](https://devnet.logianalytics.com/hc/en-us/articles/5735526919831-Managing-the-Data-Resources-in-a-Catalog#Search) in the catalog in the advanced way.
* **Style**  
  Select to open the Style Editor to [create and edit XSD styles](https://devnet.logianalytics.com/hc/en-us/articles/5735576944407-Working-with-XSD-Styles).
* **Show**/**Hide Properties**  
  Select to expand or fold the Properties sheet of the Catalog Manager.
* **Resume**  
  Select to resume the guidance workflow. Designer displays an appropriate guidance dialog box according to the currently selected resource node context.  

  In order to get data ready for creating reports, you should set up a connection, add tables and create a query or business view. Designer connects all these tasks by guidance dialog boxes to guide you what you can do next. This would be helpful for the new users of Designer without worrying about the lack of reporting knowledge.

  The guidance workflow is enabled by default. You can stop it at any time when Designer displays the guidance dialog box, asking you to choose the next work once you finish something. To resume it, select **Resume** on the Catalog Manager toolbar and Designer displays the appropriate guidance dialog box according to your current data resource context. For example, if you just finish a business view and then you select Resume, the guidance dialog box contains options for creating a page report, a web report, or going on to create another business view.

  ![A Guidance Dialog](https://devnet.logianalytics.com/hc/article_attachments/9898405123991/rptenv_ctlgmngr_guide.gif)

![Sort icon](https://devnet.logianalytics.com/hc/article_attachments/9898421887383/btn_sort2.gif)**Sort icon**

Select to [sort the resources](https://devnet.logianalytics.com/hc/en-us/articles/5735526919831-Managing-the-Data-Resources-in-a-Catalog#Sort) in the catalog.

![Search icon](https://devnet.logianalytics.com/hc/article_attachments/9898421903255/btn_srch.gif)**Search icon**

Select to open the search box to [searches for data resources](https://devnet.logianalytics.com/hc/en-us/articles/5735526919831-Managing-the-Data-Resources-in-a-Catalog#Search) in the catalog in the quick way.

**Data resource box**

This box lists the data resources in the current catalog in a tree structure. You can add, edit, and remove any resources in the tree.

**Properties sheet**

This sheet lists the properties of the selected object. It is hidden by default. To display it, select **Show Properties** on the Catalog Manager toolbar, or right-click any object and select **Properties** from the shortcut menu.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735576969879-Data-Panel)
