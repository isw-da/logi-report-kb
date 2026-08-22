---
title: "Connecting to Your Data Sources"
id: 1500009563942
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009563942-Connecting-to-Your-Data-Sources
updated_at: 2021-07-24T05:55:51Z
---

# Connecting to Your Data Sources

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562802-Maintaining-Catalogs-with-the-Catalog-Doctor)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563982-JDBC-Connections)

# Connecting to Your Data Sources

Logi JReport Designer requires access to your data source to retrieve data for reports. If you are using SQL queries Logi JReport needs to import the database schema, which allows Logi JReport to run the queries that provide the data for reports. Data source connections are defined, named, and stored in the catalog along with the reports and other resources that use them.

Logi JReport is extremely efficient when working with data sources that are in a relational database (RDBMS). The Java Database Connectivity (JDBC) connections are the basic approaches for connecting to a database for data. Other data source types can also be accessed.

This topic describes the following categories of data source connection-related tasks:

* [JDBC connections](https://devnet.logianalytics.com/hc/en-us/articles/1500009563982-JDBC-Connections): Connects to a relational database via a JDBC driver.
* [XML connections](https://devnet.logianalytics.com/hc/en-us/articles/1500009585421-XML-Connections): Connects to and transforms an XML hierarchy model to a relational model.
* [MongoDB connections](https://devnet.logianalytics.com/hc/en-us/articles/1500009585161-MongoDB-Connections): Connects to a MongoDB data source and transforms the collection schemas in the data source to relational schemas.
* [HIVE connections](https://devnet.logianalytics.com/hc/en-us/articles/1500009584781-HIVE-Connections): Connects to a relational database stored in a HIVE data source via a JDBC connection.
* [JSON connections](https://devnet.logianalytics.com/hc/en-us/articles/1500009585081-JSON-Connections): Connects to a JSON data source and transforms the schemas in the data source to relational schemas.
* [Web service data sources](https://devnet.logianalytics.com/hc/en-us/articles/1500009564342-Web-Service-Data-Sources): Logi JReport Designer supports SOAP web services defined by WSDL 1.1 or WSDL 2.0 as a data source. You can directly add a SOAP web service data source to a catalog by importing a WSDL file.
* [User defined data sources](https://devnet.logianalytics.com/hc/en-us/articles/1500009564222-User-Defined-Data-Sources): Through the UDS API, Logi JReport Designer can access data from an external data source, such as a text file or Excel file, which is not stored in a database or when there is no JDBC driver available.
* [Hierarchical data sources](https://devnet.logianalytics.com/hc/en-us/articles/1500009584721-Hierarchical-Data-Sources): Logi JReport Designer directly supports XML format data source by wrapping the provided HDS API. Logi JReport Designer's built-in classes can implement the XML format hierarchical data source interface. You can directly import an XML data source to a catalog using the Catalog Manager.
* [Connection plugins](https://devnet.logianalytics.com/hc/en-us/articles/1500009564202-Connection-Plugins): Connects to a database through a customized plugin.

**See an example:** The SampleComponents catalog, included with Logi JReport Designer, contains reports that have examples of different data source connections. Open the following report to see the connection examples: `<install_root>\Demo\Reports\SampleComponents\DataSourceConnections.cls.`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562802-Maintaining-Catalogs-with-the-Catalog-Doctor)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563982-JDBC-Connections)
