---
title: "Knowing About Catalogs"
id: 1500010094061
section: "Creating and Managing Catalogs - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010094061-Knowing-About-Catalogs
updated_at: 2021-07-23T19:14:32Z
---

# Knowing About Catalogs

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010056602-Creating-and-Managing-Catalogs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010056622-Creating-Opening-and-Saving-Catalogs)

# Knowing About Catalogs

A catalog is represented at the operating system level as a folder that contains the corresponding catalog file as well as the other report objects. This topic introduces the contents, benefits, and formats of the Logi Report catalogs.

This topic contains the following sections:

* [What Is in a Catalog File?](#What)
* [What Are the Advantages of Catalogs?](#Advantages)
* [Catalog File Formats](#Format)

## What Is in a Catalog File?

A catalog file stores all of the object definitions that you have created while developing the reports that are saved in the same catalog folder. This includes data resource definitions, component customizations, style definitions, and more. The following illustration summarizes the content of a catalog file:

![Illustration of a Catalog File](https://devnet.logianalytics.com/hc/article_attachments/4404857081879/ctlg_know.gif)

A database [connection](https://devnet.logianalytics.com/hc/en-us/articles/1500010057582-Connecting-to-Your-Data-Sources) defines the database information from which the catalog retrieves its raw data. For example, it specifies the driver such as a JDBC driver, data source name, connection URL, user ID, and password for connecting to the database, or other data source. In this way, a connection is the gateway to the raw database.

[Tables/Views/Synonyms](https://devnet.logianalytics.com/hc/en-us/articles/1500010057682-Using-Tables-Views-Synonyms), [stored procedures](https://devnet.logianalytics.com/hc/en-us/articles/1500010057662-Using-Stored-Procedures), and imported queries (including [imported SQLs](https://devnet.logianalytics.com/hc/en-us/articles/1500010095181-Using-Imported-SQLs) and [imported APEs](https://devnet.logianalytics.com/hc/en-us/articles/1500010057782-Using-Imported-APEs)) are all based on the database connection. Stored procedures are defined in the database. Imported SQLs and imported APEs are query statements in external files added to the catalog (you can also create SQL statements in the catalog directly and add them as imported SQLs). Stored procedures and imported queries only need to connect with your database (you do not necessarily have to add the database tables) and you can use them as data resources for reports.

[User data sources](https://devnet.logianalytics.com/hc/en-us/articles/1500010095301-Using-User-Defined-Data-Sources) (UDS) requires that users write the code for fetching the records. They are independent from the database connection.

[Queries](https://devnet.logianalytics.com/hc/en-us/articles/1500010062562-Working-with-Queries) are a higher-level object in a catalog. The concept is similar to that of views in the relational database but they are stored in the catalog file rather than the database itself. You can use queries to view, change, and analyze data in different ways, and Logi Report can help you with the building of various professional reports based on queries.

[Business views](https://devnet.logianalytics.com/hc/en-us/articles/1500010101021-Working-with-Business-Views) provide end users with an easily understandable data repository, which contains data resources pertinent to the creation or editing of interactive reports without exposing any underlying data structure to them.

[Parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500010099721-Working-with-Parameters) controls the report content at runtime. They are most often used for entering data selection criteria that is passed to the database in a query or stored procedure.

[Formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500010060962-Working-with-Formulas) and [summaries](https://devnet.logianalytics.com/hc/en-us/articles/1500010061062-Working-with-Summaries) are objects that are computed at runtime.

Containers, styles, special fields, and drawing objects can each be customized by setting a wide range of object properties.

## What Are the Advantages of Catalogs?

The main advantage of catalogs is that they provide a way to organize related reports and make it easy for these reports to share objects, have a consistent look and feel, and can be moved to different systems. Once you define the data source connections in a catalog and import the data resources from the connections, you can use the data resources to build many queries and business views, and then create reports on these queries and business views. Catalogs also provide these additional benefits:

* **Visual database - working off-line**  
  From a system that is offline from the database, you can still continue to develop the reports that will access it. This is because Designer stores the architecture of your database (tables/views, queries, and parameters) in the catalog.
* **Data mash-up**  
  In a catalog, you can mash up multiple data resources from different database connections into a single query or business view for more complex, deeper insights. You can combine tables, views, synonyms, imported SQLs, stored procedures, user-defined data sources, and other existing queries, and can create distributed joins to set up inter-relationships between the data resources. Distributed joins extend this by letting you access multiple data resources as one virtual data resource.
* **Default values for data objects**   
  You can set the default values for certain catalog data objects. Once set, you do not need to specify their values individually in a report after you insert them into the report. For example, each time you add a table, you can set the font face, font size, data format, and alignment once for its DBFields, then each report component you create will already have these attributes set.
* **Data security control**  
  You can control user access to different subsets of data and ensure that people only see what they are supposed to see by applying different [security controls](https://devnet.logianalytics.com/hc/en-us/articles/1500010094121-Defining-Report-Security) on your data objects. With Business View Security, you can limit user access to elements of the business views in a catalog. Record Level Security enables you to define which records are to be revealed to a given user, and Column Level Security enables you to define which report column is revealed to any given user.
* **Reference table**  
  Designer provides a [reference table](https://devnet.logianalytics.com/hc/en-us/articles/1500010056662-Clarifying-the-Reference-Relationships-Between-Resources-in-a-Catalog) that can keep track of all the objects used in all the reports in a catalog. This feature makes object name changes easier to manage.
* **Sharing defined data objects among reports**  
  Multiple reports can use data objects that have already been defined and saved in the catalog.
* **Publishing resources to Server**  
  Designer provides a convenient way to [publish an entire catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500010062722-Publishing-and-Downloading-Resources) along with all of the required reports and referenced resources such as image files in one action to Server.

## Catalog File Formats

Designer supports two formats of catalog files. One is the .cat file, which is in binary, and the other is the .cat.xml file, which is in XML. You can only manipulate (open, save, and edit) the .cat format catalog using Designer since it is a proprietary binary file. The XML catalog has many advantages. It has more readability and controllability. You can modify the catalog freely according to your requirements without using any other special editor. However, the operation of .cat.xml format catalog in Designer is the same as that of .cat format catalog. The difference between these two is the underlying structure in which they are organized. By default, Designer does not enable the XML Catalog feature. Contact Logi Analytics Support at [support@logianalytics.com](mailto:support@logianalytics.com) to upgrade your license key if you want to use it.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010056602-Creating-and-Managing-Catalogs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010056622-Creating-Opening-and-Saving-Catalogs)
