---
title: "Knowing Catalogs"
id: 1500009562742
section: "Creating and Managing Catalogs - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009562742-Knowing-Catalogs
updated_at: 2021-07-24T05:56:14Z
---

# Knowing Catalogs

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583041-Creating-and-Managing-Catalogs)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562722-Creating-a-Catalog)

# Knowing Catalogs

This topic introduces catalogs and catalog files.

Below is a list of the sections covered in this topic:

> * [What is in a Catalog File](#What)
> * [Advantages of Catalogs](#Advantages)
> * [Catalog File Formats](#Format)

## What is in a Catalog File

A catalog file stores all of the object definitions that you have created while developing the reports that are stored in the catalog folder. This includes data resource definitions, component customizations, style definitions, and more. The following illustration summarizes the content of a catalog file:

![Catalog](https://devnet.logianalytics.com/hc/article_attachments/4404894010519/ctlg_know.gif)

A database connection defines the database information from which the catalog retrieves its raw data. For example, it specifies the driver such as a JDBC driver, data source name, connection URL, user ID and password for connecting to the database or other data source. In this way, a connection is the gateway to the raw database.

Tables/Views, stored procedures, and imported SQL files are all based on the JDBC connection. Stored procedures are defined in the database. Imported SQLs are SQL statements in an external file added to the catalog. Stored procedures and imported SQLs only need to connect with your database (you do not necessarily have to add the database tables) and can be used as data sources for reports.

User data sources (UDS) and hierarchical data sources (HDS) requires that users write the code for fetching the records. They are independent from the JDBC connection.

Queries are built using the interactive Query Editor and can contain multiple tables, views, synonyms, queries, imported SQLs, stored procedures and user data sources that are from different connections in the same catalog data source.

Business views are a semantic layer - a view of the data source that you create for a report developer to use to create reports that are interactive.

Parameters are used to control the report content at runtime. They are most often used for entering data selection criteria that is passed to the database in a query or stored procedure.

Formulas and summaries are objects that are computed at runtime.

Containers, styles, special fields, and drawing objects can each be customized by setting a wide range of object properties.

Catalogs which support a large number of reports can become very large and difficult to maintain. It is best to create a new catalog for each category of report types you create. For example, you may have reports on for sales, accounts receivable, customer information, inventory management, etc. If you include all of these types of reports in a single catalog it becomes more difficult to maintain and keep track of which formulas, summaries, etc. belong to which group of reports. A better way is to create a separate catalog for each group of reports which will use similar queries, formulas, summaries, etc.

## Advantages of Catalogs

The main advantage of catalogs is that they provide a way to organize related reports and make it easy for these reports to share objects, have a consistent look and feel, and can be moved to different systems. Once you define the data source connections in a catalog and import the tables, views, SQL files, stored procedures and user defined data sources, you can use them to build many queries and business views and then create reports on these queries and business views. You can even mash up data from different data source connections in a single query or business view. Catalogs also provide these additional benefits:

* **Visual database - working off-line**  
   From a system that is offline from the database, you can still continue to develop the reports that will access it. This is because the architecture of your database (tables/views, queries, and parameters) are stored in the catalog.
* **Sharing defined data objects among reports**  
   Multiple reports can use data objects that have already been defined and saved in the catalog.
* **Reference table**  
  Logi JReport provides a reference table that can keep track of all the objects used in all the reports in a catalog. In addition to helping you build well-designed reports, this feature makes object name changes easier to manage.
* **Default values for objects**  
   You can set the default values for certain catalog objects. Once set, their values do not need to be individually set in the report after they have been inserted. For example, each time you add a table, view, stored procedure or other data source object you can set the font face, font size, data format and alignment once for the fields and each report component you create will already have these attributes set.
* **Publishing resources to Logi JReport Server**   
  Logi JReport Designer provides a convenient way to [publish an entire catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009592601-Publishing-and-Downloading-Resources) along with all of the required reports and referenced resources such as image files in one action.

## Catalog File Formats

Logi JReport Designer supports two formats of catalog files. One is the .cat file, which is in binary, and the other is the .cat.xml file, which is in XML format. The .cat format catalog can be manipulated (opened, saved, and edited) only by Logi JReport Designer since it is a proprietary binary file. The XML format catalog has many advantages. It has more readability and controllability. You can modify the catalog freely according to your requirements without using any other special editor. However, the operation of .cat.xml format catalog in Logi JReport Designer is the same as that of .cat format catalog. The difference between these two is the underlying structure in which they are organized. By default, the XML format catalog feature is not enabled. Contact Jinfonet Support ([support@jinfonet.com](mailto:support@jinfonet.com)) to upgrade your license key if desired.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583041-Creating-and-Managing-Catalogs)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562722-Creating-a-Catalog)
