---
title: "Knowing Catalogs"
id: 1500009605282
section: "Creating and Managing Catalogs - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009605282-Knowing-Catalogs
updated_at: 2021-07-24T16:05:26Z
---

# Knowing Catalogs

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009628281-Catalogs) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009628301-Creating-Opening-and-Saving-Catalogs)

# Knowing Catalogs

A catalog file stores all of the object definitions that you have created while developing the reports that are stored in the catalog folder. This topic introduces the contents, benefits, and formats of the Logi Report catalog.

This topic includes the following sections:

* [What Is in a Catalog File?](#What)
* [What Are the Advantages of Catalogs?](#Advantages)
* [Catalog File Formats](#Format)

## What Is in a Catalog File?

A catalog file stores all of the object definitions that you have created while developing the reports that are stored in the same catalog folder. This includes data resource definitions, component customizations, style definitions, and more. The following illustration summarizes the content of a catalog file:

![Illustration of a Catalog File](https://devnet.logianalytics.com/hc/article_attachments/4404904481431/ctlg_know.gif)

A database [connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009629461-Data-Source-Connections) defines the database information from which the catalog retrieves its raw data. For example, it specifies the driver such as a JDBC driver, data source name, connection URL, user ID and password for connecting to the database or other data source. In this way, a connection is the gateway to the raw database.

[Tables/Views/Synonyms](https://devnet.logianalytics.com/hc/en-us/articles/1500009629561-Tables-Views-Synonyms), [stored procedures](https://devnet.logianalytics.com/hc/en-us/articles/1500009606802-Stored-Procedures), and imported queries (including [imported SQLs](https://devnet.logianalytics.com/hc/en-us/articles/1500009606822-Creating-and-Importing-SQL-Statements) and [imported APEs](https://devnet.logianalytics.com/hc/en-us/articles/1500009606942-Imported-APEs)) are all based on the database connection. Stored procedures are defined in the database. Imported SQLs and imported APEs are query statements in external files added to the catalog. Stored procedures and imported queries only need to connect with your database (you do not necessarily have to add the database tables) and can be used as data sources for reports.

[User data sources](https://devnet.logianalytics.com/hc/en-us/articles/1500009606982-User-Defined-Data-Sources) (UDS) requires that users write the code for fetching the records. They are independent from the database connection.

[Queries](https://devnet.logianalytics.com/hc/en-us/articles/1500009613142-Queries) are a higher-level object in a catalog. The concept is similar to that of views in the relational database but they are stored in the catalog file rather than the database itself. You can use queries to view, change and analyze data in different ways, and Logi Report can help you with the building of various professional reports based on queries.

[Business views](https://devnet.logianalytics.com/hc/en-us/articles/1500009635921-Business-Views) provide end users with an easily understandable data repository which contains data resources pertinent to the creation or editing of interactive reports without exposing any underlying data structure to them.

[Parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500009611462-Parameters) are used to control the report content at runtime. They are most often used for entering data selection criteria that is passed to the database in a query or stored procedure.

[Formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009611122-Formulas) and [summaries](https://devnet.logianalytics.com/hc/en-us/articles/1500009611182-Summaries) are objects that are computed at runtime.

Containers, styles, special fields, and drawing objects can each be customized by setting a wide range of object properties.

However catalogs which support a large number of reports can become very large and difficult to maintain, so it is best to create a new catalog for each category of report types you create. For example, you may have reports for sales, accounts receivable, customer information, inventory management, and so on. If you include all of these types of reports in a single catalog it becomes more difficult to maintain and keep track of which formulas, summaries belong to which group of reports. A better way is to create a separate catalog for each group of reports which will use similar queries, formulas, summaries, and so on.

## What Are the Advantages of Catalogs?

The main advantage of catalogs is that they provide a way to organize related reports and make it easy for these reports to share objects, have a consistent look and feel, and can be moved to different systems. Once you define the data source connections in a catalog and import the data resources from the connections, you can use the data resources to build many queries and business views and then create reports on these queries and business views. Catalogs also provide these additional benefits:

* **Visual database - working off-line**  
   From a system that is offline from the database, you can still continue to develop the reports that will access it. This is because the architecture of your database (tables/views, queries, and parameters) are stored in the catalog.
* **Data mashup**  
  In a catalog, you can mash up multiple data resources from different database connections into a single query or business view for more complex, deeper insights. You can combine tables, views, synonyms, imported SQLs, stored procedures, user defined data sources and other existing queries, and can create distributed joins to set up inter-relationships between the data resources. Distributed joins extend this by letting you access multiple data resources as one virtual data resource.
* **Default values for data objects**   
   You can set the default values for certain catalog data objects. Once set, their values do not need to be individually set in the report after they have been inserted. For example, each time you add a table you can set the font face, font size, data format and alignment once for its DBFields and each report component you create will already have these attributes set.
* **Data security control**  
   You can control user access to different subsets of data and ensure that people only see what they are supposed to see by applying different security controls on your data objects. With Business View Security, you can limit user access to elements of the business views in a catalog. Record Level Security allows you to define which records are to be revealed to a given user, and Column Level Security allows you to define which report column is revealed to any given user.
* **Reference table**  
   Logi Report provides a reference table that can keep track of all the objects used in all the reports in a catalog. This feature makes object name changes easier to manage.
* **Sharing defined data objects among reports**  
   Multiple reports can use data objects that have already been defined and saved in the catalog.
* **Publishing resources to Logi Report Server  
  Logi Report**Designer provides a convenient way to [publish an entire catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009636101-Publishing-and-Downloading-Resources) along with all of the required reports and referenced resources such as image files in one action to Logi Report Server.

## Catalog File Formats

Logi ReportDesigner supports two formats of catalog files. One is the .cat file, which is in binary, and the other is the .cat.xml file, which is in XML format. The .cat format catalog can be manipulated (opened, saved, and edited) only by Logi Report Designer since it is a proprietary binary file. The XML format catalog has many advantages. It has more readability and controllability. You can modify the catalog freely according to your requirements without using any other special editor. However, the operation of .cat.xml format catalog in Logi Report Designer is the same as that of .cat format catalog. The difference between these two is the underlying structure in which they are organized. By default, the XML Format Catalog feature is not enabled. Contact Logi Analytics Support at [support@logianalytics.com](mailto:support@logianalytics.com) to upgrade your license key if desired.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009628281-Catalogs) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009628301-Creating-Opening-and-Saving-Catalogs)
