---
title: "Data Source Connections"
id: 1500009627821
section: "Logi Report Feature Guide v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009627821-Data-Source-Connections
updated_at: 2021-07-24T16:05:41Z
---

# Data Source Connections

![](https://devnet.logianalytics.com/hc/article_attachments/4404911569687/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009627941-Data-Mash-up) [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404911569943/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009604802-JDBC-Connection)

# Data Source Connections

Logi Report Designer requires access to your data source to retrieve data for reports, so before you can create reports in Logi Report Designer you need to set up a connection to your data source. Connections are defined, named, and stored in the catalog along with the reports and other resources that use them.

Logi Report Designer supports the following connection types:

| Connection Type | Description |
| --- | --- |
| JDBC | Connects to a relational database via a JDBC driver. |
| JSON | Connects to a JSON data source and transforms the schemas in the data source to relational schemas. |
| XML | Connects to and transforms an XML hierarchy model to a relational model. |
| SOAP Web Service | Connects to a SOAP Web Service data source by importing a WSDL file. Logi Report Designer supports SOAP Web Services defined by WSDL 1.1 or WSDL 2.0 as data sources. |
| MongoDB | Connects to a MongoDB database and transforms the collections in the database to relational schemas. |
| Hive | Connects to a relational database stored in a Hive data warehouse via a JDBC connection. |
| Elasticsearch | Connects to an Elasticsearch data source and transforms the schemas in the data source to relational schemas. |
| User Defined | Through the User Data Source API, Logi Report Designer can access data from an external data source, such as a text file or Excel file, which is not stored in a database or when there is no JDBC driver available. |
| Hierarchical | Logi Report Designer directly supports XML format data source by wrapping the provided Hierarchical Data Source API. Logi Report Designer's built-in classes can implement the XML format hierarchical data source interface. You can directly import an XML data source to a catalog. |

For detailed information about each connection type, refer to in the *Logi Report Designer Guide*.

We will explore the following in this guide:

* [JDBC Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009604802-JDBC-Connection)
* [XML Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009604862-XML-Connection)
* [SOAP Web Service Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009627861-SOAP-Web-Service-Connection)
* [MongoDB Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009627841-MongoDB-Connection)
* [JSON Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009604822-JSON-Connection)
* [EnterpriseDB Stored Procedure UDS](https://devnet.logianalytics.com/hc/en-us/articles/1500009604842-EnterpriseDB-Stored-Procedure-UDS)

![](https://devnet.logianalytics.com/hc/article_attachments/4404911569687/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009627941-Data-Mash-up) [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404911569943/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009604802-JDBC-Connection)
