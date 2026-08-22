---
title: "Connecting to Your Data Sources"
id: 4405661416727
section: "Connecting to Your Data Sources - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661416727-Connecting-to-Your-Data-Sources
updated_at: 2022-01-27T20:34:37Z
---

# Connecting to Your Data Sources

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664359703-Maintaining-Catalogs-with-the-Catalog-Doctor)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664412311-Connecting-via-JDBC-Connections)

# Connecting to Your Data Sources

Before you can create reports in Designer, you need to set up a connection in a catalog to enable Designer to retrieve data from your data source for the reports. Designer then stores the connection along with the reports and other resources that use it in the catalog. This topic introduces the connection types Designer supports and how you can create each of the connections in a catalog.

Designer is extremely efficient when working with data sources that are in a relational database (RDBMS). The Java Database Connectivity (JDBC) connections are the basic approaches for connecting to a database for data. Designer can also access other data source types.

You can set up connections of the following types in a catalog:

* [JDBC Connection](https://devnet.logianalytics.com/hc/en-us/articles/4405664412311-Connecting-via-JDBC-Connections): Connects to a relational database via a JDBC driver.
* [JSON Connection](https://devnet.logianalytics.com/hc/en-us/articles/4405664417047-Connecting-via-JSON-Connections): Connects to a JSON data source and transforms the schemas in the data source to relational schemas.
* [XML Connection](https://devnet.logianalytics.com/hc/en-us/articles/4405661440663-Connecting-via-XML-Connections): Connects to and transforms an XML hierarchy model to a relational model.
* [SOAP Web Service Connection](https://devnet.logianalytics.com/hc/en-us/articles/4405661439639-Connecting-via-SOAP-Web-Service-Connections): Connects to a SOAP Web Service data source by importing a WSDL file. Designer supports SOAP Web Services defined by WSDL 1.1 or WSDL 2.0 as data sources.
* [MongoDB Connection](https://devnet.logianalytics.com/hc/en-us/articles/4405661433495-Connecting-via-MongoDB-Connections): Connects to a MongoDB database and transforms the collections in the database to relational schemas.
* [Hive Connection](https://devnet.logianalytics.com/hc/en-us/articles/4405661421335-Connecting-via-Hive-Connections): Connects to a relational database stored in a Hive data warehouse via a JDBC connection.
* [Elasticsearch Connection](https://devnet.logianalytics.com/hc/en-us/articles/4405661418007-Connecting-via-Elasticsearch-Connections): Connects to an Elasticsearch data source and transforms the schemas in the data source to relational schemas.
* [User-Defined Data Source](https://devnet.logianalytics.com/hc/en-us/articles/4405661435031-Using-User-Defined-Data-Sources): Through the UDS API, Designer can access data from an external data source, such as a text file or Excel file, which is not stored in a database or when there is no JDBC driver available.
* [Hierarchical Data Source](https://devnet.logianalytics.com/hc/en-us/articles/4405664410263-Using-Hierarchical-Data-Sources): Designer directly supports XML data source by wrapping the provided HDS API. Designer's built-in classes can implement the XML hierarchical data source interface. You can directly import an XML data source to a catalog using the Catalog Manager.

**See an example:** The SampleComponents catalog, included with Designer, contains reports that have examples of different data source connections. Open the following report to see the connection examples: `<install_root>\Demo\Reports\SampleComponents\DataSourceConnections.cls.`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664359703-Maintaining-Catalogs-with-the-Catalog-Doctor)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664412311-Connecting-via-JDBC-Connections)
