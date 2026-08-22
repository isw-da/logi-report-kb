---
title: "Catalog Data Object Properties"
id: 5735532468887
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735532468887-Catalog-Data-Object-Properties
updated_at: 2022-11-02T08:07:52Z
---

# Catalog Data Object Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735569560215-Wrapper-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735525923095-Business-View-Properties)

# Catalog Data Object Properties

Designer lists the properties for the data objects in a catalog in the Properties sheet of the Catalog Manager. You can edit the properties there to customize the data objects. This topic introduces the data objects that a catalog may contain in alphabetical order, including their child objects if any.

* [Business View](https://devnet.logianalytics.com/hc/en-us/articles/5735525923095-Business-View-Properties)
  + [Aggregation](https://devnet.logianalytics.com/hc/en-us/articles/5735532496151-Aggregation-Properties)
  + [Detail](https://devnet.logianalytics.com/hc/en-us/articles/5735545483031-Detail-Properties)
  + [Group](https://devnet.logianalytics.com/hc/en-us/articles/5735568409367-Group-Properties)
  + [Category](https://devnet.logianalytics.com/hc/en-us/articles/5735545472279-Category-Properties)
  + [Hierarchy](https://devnet.logianalytics.com/hc/en-us/articles/5735532546071-Hierarchy-Properties)
* [Data Source](https://devnet.logianalytics.com/hc/en-us/articles/5735553934359-Data-Source-Properties)
* [Formula](https://devnet.logianalytics.com/hc/en-us/articles/5735568430103-Formula-Properties)
* [Hierarchical Data Source](https://devnet.logianalytics.com/hc/en-us/articles/5735553949335-Hierarchical-Data-Source-Properties)
  + [HDS Table](https://devnet.logianalytics.com/hc/en-us/articles/5735516592535-HDS-Table-Properties)
  + [HDS Column](https://devnet.logianalytics.com/hc/en-us/articles/9898557646103-HDS-Column-Properties)
* [Imported APE](https://devnet.logianalytics.com/hc/en-us/articles/5735532472983-Imported-APE-Properties) 
  + [Imported APE Column](https://devnet.logianalytics.com/hc/en-us/articles/5735568391959-Imported-APE-Column-Properties)
* [Imported SQL](https://devnet.logianalytics.com/hc/en-us/articles/5735584919575-Imported-SQL-Properties)
  + [Imported SQL Column](https://devnet.logianalytics.com/hc/en-us/articles/5735532770199-Imported-SQL-Column-Properties)
* [JDBC/Hive Connection](https://devnet.logianalytics.com/hc/en-us/articles/5735516614679-JDBC-Hive-Connection-Properties)
* [JSON/Elasticsearch Connection](https://devnet.logianalytics.com/hc/en-us/articles/5735526054167-JSON-Elasticsearch-Connection-Properties)
  + [JSON/Elasticsearch Schema](https://devnet.logianalytics.com/hc/en-us/articles/5735532649367-JSON-Elasticsearch-Schema-Properties)
* [MongoDB Connection](https://devnet.logianalytics.com/hc/en-us/articles/5735526093591-MongoDB-Connection-Properties)
  + [MongoDB Database](https://devnet.logianalytics.com/hc/en-us/articles/5735516671127-MongoDB-Database-Properties)
  + [MongoDB Collection](https://devnet.logianalytics.com/hc/en-us/articles/9898540247703-MongoDB-Collection-Properties)
  + [MongoDB Element](https://devnet.logianalytics.com/hc/en-us/articles/9898540259095-MongoDB-Element-Properties)
* [Parameter](https://devnet.logianalytics.com/hc/en-us/articles/5735545728919-Parameter-Properties)
* [Query](https://devnet.logianalytics.com/hc/en-us/articles/5735584895639-Query-Properties)
  + [Query Column](https://devnet.logianalytics.com/hc/en-us/articles/5735584906647-Query-Column-Properties)
* [Query Modifier](https://devnet.logianalytics.com/hc/en-us/articles/5735554081815-Query-Modifier-Properties)
* [Security Entry](https://devnet.logianalytics.com/hc/en-us/articles/5735568601495-Security-Entry-Properties)
* [Stored Procedure](https://devnet.logianalytics.com/hc/en-us/articles/5735532707607-Stored-Procedure-Properties)
  + [Stored Procedure Column](https://devnet.logianalytics.com/hc/en-us/articles/5735516709271-Stored-Procedure-Column-Properties)
* [Summary](https://devnet.logianalytics.com/hc/en-us/articles/5735584933143-Summary-Properties)
* [Table/View/Synonym](https://devnet.logianalytics.com/hc/en-us/articles/5735554128919-Table-View-Synonym-Properties)
  + [Table/View/Synonym Column](https://devnet.logianalytics.com/hc/en-us/articles/5735554133527-Table-View-Synonym-Column-Properties)
* [User Defined Data Source (UDS)](https://devnet.logianalytics.com/hc/en-us/articles/5735516825495-User-Defined-Data-Source-Properties)
  + [UDS Column](https://devnet.logianalytics.com/hc/en-us/articles/5735545814039-UDS-Column-Properties)
* [User Defined Function (UDF)](https://devnet.logianalytics.com/hc/en-us/articles/5735532797207-User-Defined-Function-Properties)
* [Web Service Connection](https://devnet.logianalytics.com/hc/en-us/articles/5735532819095-Web-Service-Connection-Properties)
* [XML Connection](https://devnet.logianalytics.com/hc/en-us/articles/5735532825111-XML-Connection-Properties)
  + [XML Schema](https://devnet.logianalytics.com/hc/en-us/articles/5735568669079-XML-Schema-Properties)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)

* You should use the default values of the properties except for the two properties - Name and Description. Make changes only after you are sure of the meaning of each property.
* Make sure that the precision you specify in the catalog is same as that in the database. This is to avoid inconsistency between the database data values and the report.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735569560215-Wrapper-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735525923095-Business-View-Properties)
