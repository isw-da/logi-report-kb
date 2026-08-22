---
title: "Catalog Manager"
id: 4405661949847
section: "Setting Up the Report Designing Environment - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661949847-Catalog-Manager
updated_at: 2022-01-27T20:34:59Z
---

# Catalog Manager

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661950871-Data-Panel)

# Catalog Manager

The Catalog Manager is a useful interface that simplifies the [management of the data resources](https://devnet.logianalytics.com/hc/en-us/articles/4405664358679-Managing-the-Data-Resources-in-a-Catalog) you use for creating reports (to open it, navigate to **Home**/**View** > **Catalog Manager**, or select the name of the catalog file on the Designer top banner). This topic introduces the usages of the toolbar buttons, resource tree, and Properties sheet of the Catalog Manager.

![Catalog Manager](https://devnet.logianalytics.com/hc/article_attachments/4420550819735/rptenv_ctlgmngr.gif)

**Toolbar**

The toolbar contains the following commands:

* **New**  
  The first button on the toolbar, which changes according to the currently selected object. Usually, this button contains a plus sign. You can select it to create a new object of the specified type. For example, if you select a query, you can select this button to create a new query.
* **Parameter Order**  
  Designer displays this button when you select the Parameters node or a parameter. You can use it to adjust the order of the parameters in the parameter value specifying page when running any report that uses this catalog. However, the order specified here can be overridden by the order defined for any individual report. For more information, see [Customizing the Display Order of Parameters](https://devnet.logianalytics.com/hc/en-us/articles/4405661802903-Specifying-Parameter-Values#Order).
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
  Select to specify the data sources and resource types that you want Designer to monitor. By configuring the reference database, you can quickly find out where any resource is used. For more information, see [Clarifying the Reference Relationships Between Resources in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/4405661336215-Clarifying-the-Reference-Relationships-Between-Resources-in-a-Catalog).
* **Refresh Reference**  
  Select to refresh the reference relationship information in order to make it consistent with the catalog resources.
* **Export Reference**  
  Select to export the reference relationship information to a text file.
* **Options**  
  Select to open the [Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661667735-Options-Dialog-Box) to set options for editing a catalog or reports.
* **Data Source Drivers**  
  Select open the [Data Source Drivers dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661498903-Data-Source-Drivers-Dialog-Box) for [generating data source drivers for cached query results](https://devnet.logianalytics.com/hc/en-us/articles/4405664683031-Working-with-Cached-Query-Results#Manage).
* **Pre-join**  
  Select to define the pre-join paths formed by the relationships among the tables in the selected catalog data source. For more information, see [Editing Pre-joins in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/4405661331735-Editing-Pre-joins-in-a-Catalog).
* **Data Mapping Editor**  
  Select to map the data values of resources in a catalog to a certain language. For more information, see [Data Mapping Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661798039-Mapping-Data-Values-to-Different-Languages).
* **Filter View**  
  Select to exclude some elements from the view in the Catalog Manager. For more information, see [Filtering the data resources](https://devnet.logianalytics.com/hc/en-us/articles/4405664358679-Managing-the-Data-Resources-in-a-Catalog#Filter).
* **Search**  
  Select to [search the required data resources](https://devnet.logianalytics.com/hc/en-us/articles/4405664358679-Managing-the-Data-Resources-in-a-Catalog#Search) in the catalog in the advanced way.
* **Style**  
  Select to open the Style Editor to [create and edit XSD styles](https://devnet.logianalytics.com/hc/en-us/articles/4405661945495-Working-with-XSD-Styles).
* **Show**/**Hide Properties**  
  Select to expand or fold the Properties sheet of the Catalog Manager.
* **Resume**  
  Select to resume the guidance workflow. Designer displays an appropriate guidance dialog box according to the currently selected resource node context.  

  In order to get data ready for creating reports, you should set up a connection, add tables and create a query or business view. Designer connects all these tasks by guidance dialog boxes to guide you what you can do next. This would be helpful for the new users of Designer without worrying about the lack of reporting knowledge.

  The guidance workflow is enabled by default. You can stop it at any time when Designer displays the guidance dialog box, asking you to choose the next work once you finish something. To resume it, select **Resume** on the Catalog Manager toolbar and Designer displays the appropriate guidance dialog box according to your current data resource context. For example, if you just finish a business view and then you select Resume, the guidance dialog box contains options for creating a page report, a web report, or going on to create another business view.

  ![A Guidance Dialog](https://devnet.logianalytics.com/hc/article_attachments/4420542064407/rptenv_ctlgmngr_guide.gif)

![Sort icon](https://devnet.logianalytics.com/hc/article_attachments/4420542068375/btn_sort2.gif)**Sort icon**

Select to [sort the resources](https://devnet.logianalytics.com/hc/en-us/articles/4405664358679-Managing-the-Data-Resources-in-a-Catalog#Sort) in the catalog.

![Search icon](https://devnet.logianalytics.com/hc/article_attachments/4420542068631/btn_srch.gif)**Search icon**

Select to open the search box to [searches for data resources](https://devnet.logianalytics.com/hc/en-us/articles/4405664358679-Managing-the-Data-Resources-in-a-Catalog#Search) in the catalog in the quick way.

**Data resource box**

This box lists the data resources in the current catalog in a tree structure. You can add, edit, and remove any resources in the tree.

**Properties sheet**

This sheet lists the properties of the selected object. It is hidden by default. To display it, select **Show Properties** on the Catalog Manager toolbar, or right-click any object and select **Properties** from the shortcut menu.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661950871-Data-Panel)
