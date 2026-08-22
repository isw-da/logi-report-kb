---
title: "Data Source Connections"
id: 1500009629461
section: "Connecting to Your Data Sources - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009629461-Data-Source-Connections
updated_at: 2021-07-24T16:05:09Z
---

# Data Source Connections

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009605322-Maintaining-Catalogs-with-the-Catalog-Doctor) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009629541-JDBC-Connections)

# Data Source Connections

Before you can create reports in Logi Report Designer, you need to set up a connection to allow Logi Report Designer to retrieve data from your data source for the reports. If you are using SQL queries Logi Report needs to import the database schema, which allows Logi Report to run the queries that provide the data for reports. Connections are defined, named, and stored in the catalog along with the reports and other resources that use them.

Logi Report is extremely efficient when working with data sources that are in a relational database (RDBMS). The Java Database Connectivity (JDBC) connections are the basic approaches for connecting to a database for data. Other data source types can also be accessed.

This topic describes the following connection types:

* [JDBC Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009629541-JDBC-Connections): Connects to a relational database via a JDBC driver.
* [JSON Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009606902-JSON-Connections): Connects to a JSON data source and transforms the schemas in the data source to relational schemas.
* [XML Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009607042-XML-Connections): Connects to and transforms an XML hierarchy model to a relational model.
* [SOAP Web Service Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009629701-SOAP-Web-Service-Connections): Connects to a SOAP Web Service data source by importing a WSDL file. Logi Report Designer supports SOAP Web Services defined by WSDL 1.1 or WSDL 2.0 as data sources.
* [MongoDB Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009629601-MongoDB-Connections): Connects to a MongoDB database and transforms the collections in the database to relational schemas.
* [Hive Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009606762-Hive-Connections): Connects to a relational database stored in a Hive data warehouse via a JDBC connection.
* [Elasticsearch Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009629481-Elasticsearch-Connections-): Connects to an Elasticsearch data source and transforms the schemas in the data source to relational schemas.
* [User Defined Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009606982-User-Defined-Data-Sources): Through the UDS API, Logi Report Designer can access data from an external data source, such as a text file or Excel file, which is not stored in a database or when there is no JDBC driver available.
* [Hierarchical Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009606722-Hierarchical-Data-Sources): Logi Report Designer directly supports XML format data source by wrapping the provided HDS API. Logi Report Designer's built-in classes can implement the XML format hierarchical data source interface. You can directly import an XML data source to a catalog using the Catalog Manager.

**See an example:** The SampleComponents catalog, included with Logi Report Designer, contains reports that have examples of different data source connections. Open the following report to see the connection examples: `<install_root>\Demo\Reports\SampleComponents\DataSourceConnections.cls.`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009605322-Maintaining-Catalogs-with-the-Catalog-Doctor) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009629541-JDBC-Connections)
