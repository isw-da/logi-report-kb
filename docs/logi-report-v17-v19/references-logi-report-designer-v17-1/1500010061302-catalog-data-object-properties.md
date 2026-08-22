---
title: "Catalog Data Object Properties"
id: 1500010061302
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010061302-Catalog-Data-Object-Properties
updated_at: 2021-07-23T19:16:19Z
---

# Catalog Data Object Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010101001-Wrapper-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010099841-Business-View-Properties)

# Catalog Data Object Properties

The properties for the data objects in a catalog are listed in the Properties sheet of the Catalog Manager. You can edit the properties here to customize the data objects.

The following lists the data objects that a catalog may contain with their child objects in alphabetical order:

* [Business View](https://devnet.logianalytics.com/hc/en-us/articles/1500010099841-Business-View-Properties)
  + [Aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500010099861-Aggregation-Properties)
  + [Category](https://devnet.logianalytics.com/hc/en-us/articles/1500010061322-Category-Properties)
  + [Detail](https://devnet.logianalytics.com/hc/en-us/articles/1500010061342-Detail-Properties)
  + [Group](https://devnet.logianalytics.com/hc/en-us/articles/1500010099881-Group-Properties)
* [Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500010061362-Data-Source-Properties)
* [Data Source Security](https://devnet.logianalytics.com/hc/en-us/articles/1500010061382-Data-Source-Security-Properties)
* [Formula](https://devnet.logianalytics.com/hc/en-us/articles/1500010061402-Formula-Properties)
* [Hierarchical Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500010099901-Hierarchical-Data-Source-Properties)
  + [HDS Table](https://devnet.logianalytics.com/hc/en-us/articles/1500010099921-HDS-Table-Properties)
    - [HDS Column](https://devnet.logianalytics.com/hc/en-us/articles/1500010099941-HDS-Column-Properties)
* [Imported APE](https://devnet.logianalytics.com/hc/en-us/articles/1500010099801-Imported-APE-Properties) 
  + [Imported APE Column](https://devnet.logianalytics.com/hc/en-us/articles/1500010099821-Imported-APE-Column-Properties)
* [Imported SQL](https://devnet.logianalytics.com/hc/en-us/articles/1500010100101-Imported-SQL-Properties)
  + [Imported SQL Column](https://devnet.logianalytics.com/hc/en-us/articles/1500010061542-Imported-SQL-Column-Properties)
* [JDBC/Hive Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500010099961-JDBC-Hive-Connection-Properties)
* [JSON/Elasticsearch Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500010061422-JSON-Elasticsearch-Connection-Properties)
  + [JSON/Elasticsearch Schema](https://devnet.logianalytics.com/hc/en-us/articles/1500010061442-JSON-Elasticsearch-Schema-Properties)
* [MongoDB Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500010099981-MongoDB-Connection-Properties)
  + [MongoDB Database](https://devnet.logianalytics.com/hc/en-us/articles/1500010061462-MongoDB-Database-Properties)
    - [MongoDB Collection](https://devnet.logianalytics.com/hc/en-us/articles/1500010100001-MongoDB-Collection-Properties)
      * [MongoDB Element](https://devnet.logianalytics.com/hc/en-us/articles/1500010100021-MongoDB-Element-Properties)
* [Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500010061522-Parameter-Properties)
* [Query](https://devnet.logianalytics.com/hc/en-us/articles/1500010100061-Query-Properties)
  + [Query Column](https://devnet.logianalytics.com/hc/en-us/articles/1500010100081-Query-Column-Properties)
* [Query Modifier](https://devnet.logianalytics.com/hc/en-us/articles/1500010100041-Query-Modifier-Properties)
* [Stored Procedure](https://devnet.logianalytics.com/hc/en-us/articles/1500010061482-Stored-Procedure-Properties)
  + [Stored Procedure Column](https://devnet.logianalytics.com/hc/en-us/articles/1500010061502-Stored-Procedure-Column-Properties)
* [Summary](https://devnet.logianalytics.com/hc/en-us/articles/1500010061562-Summary-Properties)
* [Table/View/Synonym](https://devnet.logianalytics.com/hc/en-us/articles/1500010100121-Table-View-Synonym-Properties)
  + [Table/View/Synonym Column](https://devnet.logianalytics.com/hc/en-us/articles/1500010061582-Table-View-Synonym-Column-Properties)
* [User-Defined Data Source (UDS)](https://devnet.logianalytics.com/hc/en-us/articles/1500010061622-User-Defined-Data-Source-UDS-Properties)
  + [UDS Column](https://devnet.logianalytics.com/hc/en-us/articles/1500010100141-UDS-Column-Properties)
* [User-Defined Function (UDF)](https://devnet.logianalytics.com/hc/en-us/articles/1500010061602-User-Defined-Function-UDF-Properties)
* [Web Service Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500010061642-Web-Service-Connection-Properties)
* [XML Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500010100161-XML-Connection-Properties)
  + [XML Schema](https://devnet.logianalytics.com/hc/en-us/articles/1500010061662-XML-Schema-Properties)

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4404856819991/criticalicon.gif)

* The default ones are the recommended values to be used, so it is better not to randomly modify other properties except the two properties - Name and Description. Make changes only after you are sure of the meaning of each property.
* Make sure that the precision set in the catalog is same as that in the database. This is to avoid inconsistency between the database data values and the displayed report result.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010101001-Wrapper-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010099841-Business-View-Properties)
