---
title: "Knowing About Catalogs"
id: 28897740650381
section: "Creating and Managing Catalogs - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897740650381-Knowing-About-Catalogs
updated_at: 2024-09-30T09:07:52Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Knowing About Catalogs

A catalog is represented at the operating system level as a folder that contains the corresponding catalog file and the other report object files. This topic introduces the content, benefits, and formats of the Report catalogs. 

This topic contains the following sections:

- What Is in a  Catalog File?

- What Are the Advantages of Catalogs?

- Catalog File Formats 

## 
What Is in a Catalog File?

A catalog file stores all of the object definitions that you have created while developing the reports that are saved in the same catalog folder. This includes data resource definitions, component customizations, style definitions, and more.

The following illustration summarizes the content of a catalog file. 

- 
Database Connections
A database connection defines the database information from which the catalog retrieves its raw data. For example, it specifies the driver such as a JDBC driver, data source name, connection URL, user ID, and password for connecting to the database, or other data source. In this way, a connection is the gateway to the raw database.

- 
Tables/Views, Stored Procedures, and Imported Queries
Tables/Views/Synonyms, stored procedures, and imported queries (including imported SQLs and imported APEs) are all based on the database connection. Stored procedures are defined in the database. Imported SQLs and imported APEs are query statements in external files added to the catalog (you can also create SQL statements in the catalog directly and add them as imported SQLs). Stored procedures and imported queries only need to connect with your database (you do not necessarily have to add the database tables) and you can use them  as data resources for reports.

- 
User Data Sources
User data sources (UDS) requires that users write the code for fetching the records. They are independent from the database connection.

- 
Queries
Queries are a higher-level object in a catalog. The concept is similar to that of views in the relational database but they are stored in the catalog file rather than the database itself. You can use queries to view, change, and analyze data in different ways, and Report can help you with the building of various professional reports based on queries.

- 
Business Views
Business views  provide end users with an easily understandable data repository, which contains data resources pertinent to the creation or editing of interactive reports without exposing any underlying data structure to them.

- 
Parameters
Parameters  are variables whose values are specified at runtime. You can use them to control the report content at runtime. They are most often used for entering data selection criteria that is passed to the database in a query or stored procedure.

- 
Formulas and Summaries
Formulas and summaries are objects that are computed at runtime.

- 
Customized Classes
Containers, styles, special fields, and drawing objects can each be customized by setting a wide range of object properties. 

## 
What Are the Advantages of Catalogs?

The main advantage of catalogs is that they provide a way to organize related reports and make it easy for these reports to share objects, have a consistent look and feel, and can be moved to different systems. Once you define the data source connections in a catalog and import the data resources from the connections, you can use the data resources to build many queries and business views, and then create reports on these queries and business views.

Catalogs also provide these additional benefits:

- 
Visual database - working off-line
From a system that is offline from the database, you can still continue to develop the reports that will access it. This is because Designer stores the architecture of your database (tables/views, queries, and parameters) in the catalog.

- 
Data mash-up
In a catalog, you can mash up multiple data resources from different database connections into a single query or business view for more complex, deeper insights. You can combine tables, views, synonyms, imported SQLs, stored procedures, user-defined data sources, and other existing queries, and can create distributed joins to set up inter-relationships between the data resources. Distributed joins extend this by letting you access multiple data resources as one virtual data resource.

- 
Default values for data objects 
You can set the default values for certain catalog data objects. Once set, you do not need to specify their values  individually  in a report after you insert them into the report. For example, each time you add a table, you can set the font face, font size, data format, and alignment once for its DBFields, then each report component you create will already have these attributes set.

- 
Data security control
You can control user access to different subsets of data and ensure that people only see what they are supposed to see by applying different security controls on your data objects. With Business View Security, you can limit user access to elements of the business views in a catalog. Record Level Security enables you to define which records are to be revealed to a given user, and Column Level Security enables you to define which report column is revealed to any given user.

- 
Reference table
Designer provides a reference table that can keep track of all the objects used in all the reports in a catalog. This feature makes object name changes easier to manage. 

- 
Sharing defined data objects among reports
Multiple reports can use data objects that have already been defined and saved in the catalog.

- 
Publishing resources to Server
Designer provides a convenient way to publish an entire catalog along with all of the required reports and referenced resources such as image files in one action to Server.

## 
Catalog File Formats 

Designer supports two formats of catalog files. One is the .cat file, which is in binary, and the other is the .cat.xml file, which is in XML. You can only manipulate (open, save, and edit) the .cat format catalog using Designer since it is a proprietary binary file. The XML catalog has many advantages. It has more readability and controllability. You can modify the catalog freely according to your requirements without using any other special editor. However, the operation of .cat.xml catalog in  Designer is the same as that of .cat catalog. The difference between these two is the underlying structure in which they are organized.

Previous Topic  Next Topic
