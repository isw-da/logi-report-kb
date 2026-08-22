---
title: "Catalog Data Object Properties"
id: 1500009634561
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009634561-Catalog-Data-Object-Properties
updated_at: 2021-07-24T16:03:50Z
---

# Catalog Data Object Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009613082-Wrapper-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009634581-Business-View-Properties)

# Catalog Data Object Properties

The properties for the data objects in a catalog are listed in the Properties sheet of the Catalog Manager. You can edit the properties here to customize the data objects.

The following lists the data objects that a catalog may contain with their child objects in alphabetical order:

* [Business View](https://devnet.logianalytics.com/hc/en-us/articles/1500009634581-Business-View-Properties)
  + [Aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500009611582-Aggregation-Properties)
  + [Category](https://devnet.logianalytics.com/hc/en-us/articles/1500009634601-Category-Properties)
  + [Detail](https://devnet.logianalytics.com/hc/en-us/articles/1500009634621-Detail-Properties)
  + [Group](https://devnet.logianalytics.com/hc/en-us/articles/1500009611602-Group-Properties)
* [Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009634641-Data-Source-Properties)
* [Data Source Security](https://devnet.logianalytics.com/hc/en-us/articles/1500009634661-Data-Source-Security-Properties)
* [Formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009611622-Formula-Properties)
* [Hierarchical Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009611642-Hierarchical-Data-Source-Properties)
  + [HDS Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009611662-HDS-Table-Properties)
    - [HDS Column](https://devnet.logianalytics.com/hc/en-us/articles/1500009634681-HDS-Column-Properties)
* [Imported APE](https://devnet.logianalytics.com/hc/en-us/articles/1500009611542-Imported-APE-Properties) 
  + [Imported APE Column](https://devnet.logianalytics.com/hc/en-us/articles/1500009611562-Imported-APE-Column-Properties)
* [Imported SQL](https://devnet.logianalytics.com/hc/en-us/articles/1500009611762-Imported-SQL-Properties)
  + [Imported SQL Column](https://devnet.logianalytics.com/hc/en-us/articles/1500009634881-Imported-SQL-Column-Properties)
* [JDBC/Hive Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009634701-JDBC-Hive-Connection-Properties)
* [JSON/Elasticsearch Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009634721-JSON-Elasticsearch-Connection-Properties)
  + [JSON/Elasticsearch Schema](https://devnet.logianalytics.com/hc/en-us/articles/1500009634741-JSON-Elasticsearch-Schema-Properties)
* [MongoDB Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009634761-MongoDB-Connection-Properties)
  + [MongoDB Database](https://devnet.logianalytics.com/hc/en-us/articles/1500009634781-MongoDB-Database-Properties)
    - [MongoDB Collection](https://devnet.logianalytics.com/hc/en-us/articles/1500009611682-MongoDB-Collection-Properties)
      * [MongoDB Element](https://devnet.logianalytics.com/hc/en-us/articles/1500009611702-MongoDB-Element-Properties)
* [Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009634841-Parameter-Properties)
* [Query](https://devnet.logianalytics.com/hc/en-us/articles/1500009634861-Query-Properties)
  + [Query Column](https://devnet.logianalytics.com/hc/en-us/articles/1500009611742-Query-Column-Properties)
* [Query Modifier](https://devnet.logianalytics.com/hc/en-us/articles/1500009611722-Query-Modifier-Properties)
* [Stored Procedure](https://devnet.logianalytics.com/hc/en-us/articles/1500009634801-Stored-Procedure-Properties)
  + [Stored Procedure Column](https://devnet.logianalytics.com/hc/en-us/articles/1500009634821-Stored-Procedure-Column-Properties)
* [Summary](https://devnet.logianalytics.com/hc/en-us/articles/1500009634901-Summary-Properties)
* [Table/View/Synonym](https://devnet.logianalytics.com/hc/en-us/articles/1500009634921-Table-View-Synonym-Properties)
  + [Table/View/Synonym Column](https://devnet.logianalytics.com/hc/en-us/articles/1500009611782-Table-View-Synonym-Column-Properties)
* [User Defined Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009634941-User-Defined-Data-Source-Properties)
  + [UDS Column](https://devnet.logianalytics.com/hc/en-us/articles/1500009634981-UDS-Column-Properties)
* [User Defined Function](https://devnet.logianalytics.com/hc/en-us/articles/1500009611802-User-Defined-Function-Properties)
* [Web Service Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009611842-Web-Service-Connection-Properties)
* [XML Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009611882-XML-Connection-Properties)
  + [XML Schema](https://devnet.logianalytics.com/hc/en-us/articles/1500009611902-XML-Schema-Properties)

**Notes**:

* The default ones are the recommended values to be used, so it is better not to randomly modify other properties except the two properties - Name and Description. Make changes only after you are sure of the meaning of each property.
* Make sure that the precision set in catalog is same as that in database. This is to avoid inconsistency between the database data values and the displayed report result.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009613082-Wrapper-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009634581-Business-View-Properties)
