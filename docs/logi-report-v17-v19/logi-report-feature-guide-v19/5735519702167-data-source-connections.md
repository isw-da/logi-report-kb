---
title: "Data Source Connections"
id: 5735519702167
section: "Logi Report Feature Guide v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735519702167-Data-Source-Connections
updated_at: 2022-11-02T04:11:48Z
---

# Data Source Connections

![](https://devnet.logianalytics.com/hc/article_attachments/9898403124503/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735526375703-Data-Mash-Up)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/9898403130775/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735511262615-JDBC-Connection)

# Data Source Connections

Before you can create reports in Designer, you need to set up a connection in a catalog to enable Designer to retrieve data from your data source for the reports. Designer then stores the connection along with the reports and other resources that use it in the catalog.

Designer supports the following connection types:

| Connection Type | Description |
| --- | --- |
| JDBC | Connects to a relational database via a JDBC driver. |
| JSON | Connects to a JSON data source and transforms the schema in the data source to relational schema. |
| XML | Connects to and transforms an XML hierarchy model to a relational model. |
| SOAP Web Service | Connects to a SOAP Web Service data source by importing a WSDL file. Designer supports SOAP Web Services defined by WSDL 1.1 or WSDL 2.0 as data sources. |
| MongoDB | Connects to a MongoDB database and transforms collections in the database to relational schemas. |
| Hive | Connects to a relational database stored in a Hive data warehouse via a JDBC connection. |
| Elasticsearch | Connects to an Elasticsearch data source and transforms the schema in the data source to relational schema. |
| User Defined | Through the User Data Source API, Designer can access data from an external data source, such as a text file or Excel file, which is not stored in a database or when there is no JDBC driver available. |
| Hierarchical | Designer directly supports XML format data source by wrapping the provided Hierarchical Data Source API. Designer's built-in classes can implement the XML format hierarchical data source interface. You can directly import an XML data source to a catalog. |

We will explore the following in this topic:

* [JDBC Connection](https://devnet.logianalytics.com/hc/en-us/articles/5735511262615-JDBC-Connection)
* [XML Connection](https://devnet.logianalytics.com/hc/en-us/articles/5735511294743-XML-Connection)
* [SOAP Web Service Connection](https://devnet.logianalytics.com/hc/en-us/articles/5735526307351-SOAP-Web-Service-Connection)
* [MongoDB Connection](https://devnet.logianalytics.com/hc/en-us/articles/5735526290967-MongoDB-Connection)
* [JSON Connection](https://devnet.logianalytics.com/hc/en-us/articles/5735511265815-JSON-Connection)
* [EnterpriseDB Stored Procedure UDS](https://devnet.logianalytics.com/hc/en-us/articles/5735497866903-EnterpriseDB-Stored-Procedure-UDS)

![](https://devnet.logianalytics.com/hc/article_attachments/9898403124503/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735526375703-Data-Mash-Up)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/9898403130775/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735511262615-JDBC-Connection)
