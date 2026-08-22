---
title: "Catalog Data Object Properties"
id: 4405661804439
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661804439-Catalog-Data-Object-Properties
updated_at: 2022-01-27T20:36:12Z
---

# Catalog Data Object Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661910295-Wrapper-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664618903-Business-View-Properties)

# Catalog Data Object Properties

Designer lists the properties for the data objects in a catalog in the Properties sheet of the Catalog Manager. You can edit the properties there to customize the data objects. This topic introduces the data objects that a catalog may contain with their child objects in alphabetical order.

* [Business View](https://devnet.logianalytics.com/hc/en-us/articles/4405664618903-Business-View-Properties)
  + [Aggregation](https://devnet.logianalytics.com/hc/en-us/articles/4405664620055-Aggregation-Properties)
  + [Category](https://devnet.logianalytics.com/hc/en-us/articles/4405664621079-Category-Properties)
  + [Detail](https://devnet.logianalytics.com/hc/en-us/articles/4405664622359-Detail-Properties)
  + [Group](https://devnet.logianalytics.com/hc/en-us/articles/4405661809175-Group-Properties)
  + [Hierarchy](https://devnet.logianalytics.com/hc/en-us/articles/4405661810711-Hierarchy-Properties)
* [Data Source](https://devnet.logianalytics.com/hc/en-us/articles/4405661812375-Data-Source-Properties)
* [Formula](https://devnet.logianalytics.com/hc/en-us/articles/4405664627479-Formula-Properties)
* [Hierarchical Data Source](https://devnet.logianalytics.com/hc/en-us/articles/4405661813911-Hierarchical-Data-Source-Properties)
  + [HDS Table](https://devnet.logianalytics.com/hc/en-us/articles/4405661815063-HDS-Table-Properties)
    - [HDS Column](https://devnet.logianalytics.com/hc/en-us/articles/4405661816087-HDS-Column-Properties)
* [Imported APE](https://devnet.logianalytics.com/hc/en-us/articles/4405664616343-Imported-APE-Properties) 
  + [Imported APE Column](https://devnet.logianalytics.com/hc/en-us/articles/4405664617367-Imported-APE-Column-Properties)
* [Imported SQL](https://devnet.logianalytics.com/hc/en-us/articles/4405661823511-Imported-SQL-Properties)
  + [Imported SQL Column](https://devnet.logianalytics.com/hc/en-us/articles/4405661824663-Imported-SQL-Column-Properties)
* [JDBC/Hive Connection](https://devnet.logianalytics.com/hc/en-us/articles/4405664629143-JDBC-Hive-Connection-Properties)
* [JSON/Elasticsearch Connection](https://devnet.logianalytics.com/hc/en-us/articles/4405664630295-JSON-Elasticsearch-Connection-Properties)
  + [JSON/Elasticsearch Schema](https://devnet.logianalytics.com/hc/en-us/articles/4405661817367-JSON-Elasticsearch-Schema-Properties)
* [MongoDB Connection](https://devnet.logianalytics.com/hc/en-us/articles/4405661818391-MongoDB-Connection-Properties)
  + [MongoDB Database](https://devnet.logianalytics.com/hc/en-us/articles/4405664631575-MongoDB-Database-Properties)
    - [MongoDB Collection](https://devnet.logianalytics.com/hc/en-us/articles/4405664632471-MongoDB-Collection-Properties)
      * [MongoDB Element](https://devnet.logianalytics.com/hc/en-us/articles/4405664633367-MongoDB-Element-Properties)
* [Parameter](https://devnet.logianalytics.com/hc/en-us/articles/4405664635159-Parameter-Properties)
* [Query](https://devnet.logianalytics.com/hc/en-us/articles/4405664637207-Query-Properties)
  + [Query Column](https://devnet.logianalytics.com/hc/en-us/articles/4405664638103-Query-Column-Properties)
* [Query Modifier](https://devnet.logianalytics.com/hc/en-us/articles/4405664636311-Query-Modifier-Properties)
* [Security Entry](https://devnet.logianalytics.com/hc/en-us/articles/4405664639127-Security-Entry-Properties)
* [Stored Procedure](https://devnet.logianalytics.com/hc/en-us/articles/4405661820055-Stored-Procedure-Properties)
  + [Stored Procedure Column](https://devnet.logianalytics.com/hc/en-us/articles/4405661821079-Stored-Procedure-Column-Properties)
* [Summary](https://devnet.logianalytics.com/hc/en-us/articles/4405664640535-Summary-Properties)
* [Table/View/Synonym](https://devnet.logianalytics.com/hc/en-us/articles/4405661825943-Table-View-Synonym-Properties)
  + [Table/View/Synonym Column](https://devnet.logianalytics.com/hc/en-us/articles/4405661827095-Table-View-Synonym-Column-Properties)
* [User Defined Data Source (UDS)](https://devnet.logianalytics.com/hc/en-us/articles/4405661828503-User-Defined-Data-Source-Properties)
  + [UDS Column](https://devnet.logianalytics.com/hc/en-us/articles/4405664642711-UDS-Column-Properties)
* [User Defined Function (UDF)](https://devnet.logianalytics.com/hc/en-us/articles/4405664641687-User-Defined-Function-Properties)
* [Web Service Connection](https://devnet.logianalytics.com/hc/en-us/articles/4405661830039-Web-Service-Connection-Properties)
* [XML Connection](https://devnet.logianalytics.com/hc/en-us/articles/4405664643607-XML-Connection-Properties)
  + [XML Schema](https://devnet.logianalytics.com/hc/en-us/articles/4405664644503-XML-Schema-Properties)

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4420542088087/criticalicon.gif)

* You should use the default values of the properties except for the two properties - Name and Description. Make changes only after you are sure of the meaning of each property.
* Make sure that the precision set in the catalog is same as that in the database. This is to avoid inconsistency between the database data values and the report.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661910295-Wrapper-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664618903-Business-View-Properties)
