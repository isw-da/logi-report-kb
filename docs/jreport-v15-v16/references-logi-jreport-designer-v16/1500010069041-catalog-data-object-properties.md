---
title: "Catalog Data Object Properties"
id: 1500010069041
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010069041-Catalog-Data-Object-Properties
updated_at: 2021-07-24T10:38:08Z
---

# Catalog Data Object Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010070621-Wrapper-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010069061-Business-View-Properties)

# Catalog Data Object Properties

The properties for the data objects in a catalog are listed in the Properties sheet of the Catalog Manager. You can edit the properties here to customize the data objects.

The following lists the data objects that a catalog may contain with their child objects in alphabetical order:

* [Business View](https://devnet.logianalytics.com/hc/en-us/articles/1500010069061-Business-View-Properties)
  + [Aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500010033502-Aggregation-Properties)
  + [Category](https://devnet.logianalytics.com/hc/en-us/articles/1500010033522-Category-Properties)
  + [Detail](https://devnet.logianalytics.com/hc/en-us/articles/1500010069081-Detail-Properties)
  + [Group](https://devnet.logianalytics.com/hc/en-us/articles/1500010033562-Group-Properties)
* [Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500010033582-Data-Source-Properties)
* [Data Source Security](https://devnet.logianalytics.com/hc/en-us/articles/1500010069101-Data-Source-Security-Properties)
* [Formula](https://devnet.logianalytics.com/hc/en-us/articles/1500010069121-Formula-Properties)
* [Hierarchical Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500010069141-Hierarchical-Data-Source-Properties)
  + [HDS Table](https://devnet.logianalytics.com/hc/en-us/articles/1500010069161-HDS-Table-Properties)
    - [HDS Column](https://devnet.logianalytics.com/hc/en-us/articles/1500010033622-HDS-Column-Properties)
* [Imported APE](https://devnet.logianalytics.com/hc/en-us/articles/1500010033462-Imported-APE-Properties) 
  + [Imported APE Column](https://devnet.logianalytics.com/hc/en-us/articles/1500010033482-Imported-APE-Column-Properties)
* [Imported SQL](https://devnet.logianalytics.com/hc/en-us/articles/1500010069381-Imported-SQL-Properties)
  + [Imported SQL Column](https://devnet.logianalytics.com/hc/en-us/articles/1500010033742-Imported-SQL-Column-Properties)
* [JDBC/Hive Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500010069181-JDBC-Hive-Connection-Properties)
* [JSON/Elasticsearch Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500010033642-JSON-Elasticsearch-Connection-Properties)
  + [JSON/Elasticsearch Schema](https://devnet.logianalytics.com/hc/en-us/articles/1500010069201-JSON-Elasticsearch-Schema-Properties)
* [MongoDB Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500010069221-MongoDB-Connection-Properties)
  + [MongoDB Database](https://devnet.logianalytics.com/hc/en-us/articles/1500010069241-MongoDB-Database-Properties)
    - [MongoDB Collection](https://devnet.logianalytics.com/hc/en-us/articles/1500010069261-MongoDB-Collection-Properties)
      * [MongoDB Element](https://devnet.logianalytics.com/hc/en-us/articles/1500010033662-MongoDB-Element-Properties)
* [Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500010069321-Parameter-Properties)
* [Query](https://devnet.logianalytics.com/hc/en-us/articles/1500010069341-Query-Properties)
  + [Query Column](https://devnet.logianalytics.com/hc/en-us/articles/1500010069361-Query-Column-Properties)
* [Query Modifier](https://devnet.logianalytics.com/hc/en-us/articles/1500010033702-Query-Modifier-Properties)
* [Stored Procedure](https://devnet.logianalytics.com/hc/en-us/articles/1500010069281-Stored-Procedure-Properties)
  + [Stored Procedure Column](https://devnet.logianalytics.com/hc/en-us/articles/1500010069301-Stored-Procedure-Column-Properties)
* [Summary](https://devnet.logianalytics.com/hc/en-us/articles/1500010069401-Summary-Properties)
* [Table/View/Synonym](https://devnet.logianalytics.com/hc/en-us/articles/1500010069421-Table-View-Synonym-Properties)
  + [Table/View/Synonym Column](https://devnet.logianalytics.com/hc/en-us/articles/1500010069441-Table-View-Synonym-Column-Properties)
* [User Defined Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500010069481-User-Defined-Data-Source-Properties)
  + [UDS Column](https://devnet.logianalytics.com/hc/en-us/articles/1500010069501-UDS-Column-Properties)
* [User Defined Function](https://devnet.logianalytics.com/hc/en-us/articles/1500010069461-User-Defined-Function-Properties)
* [Web Service Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500010033762-Web-Service-Connection-Properties)
* [XML Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500010033782-XML-Connection-Properties)
  + [XML Schema](https://devnet.logianalytics.com/hc/en-us/articles/1500010033802-XML-Schema-Properties)

**Notes**:

* The default ones are the recommended values to be used, so it is better not to randomly modify other properties except the two properties - Name and Description. Make changes only after you are sure of the meaning of each property.
* Make sure that the precision set in catalog is same as that in database. This is to avoid inconsistency between the database data values and the displayed report result.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010070621-Wrapper-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010069061-Business-View-Properties)
