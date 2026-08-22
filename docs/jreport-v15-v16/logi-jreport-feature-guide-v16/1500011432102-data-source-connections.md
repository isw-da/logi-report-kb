---
title: "Data Source Connections"
id: 1500011432102
section: "Logi JReport Feature Guide v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500011432102-Data-Source-Connections
updated_at: 2021-07-24T10:39:50Z
---

# Data Source Connections

![](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500011431942-Data-Mashup) [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011432082-JDBC-Connection)

# Data Source Connections

Logi JReport Designer requires access to your data source to retrieve data for reports, so before you can create reports in Logi JReport Designer you need to set up a connection to your data source. Connections are defined, named, and stored in the catalog along with the reports and other resources that use them.

Logi JReport Designer supports the following connection types:

| Connection Type | Description |
| --- | --- |
| JDBC | Connects to a relational database via a JDBC driver. |
| JSON | Connects to a JSON data source and transforms the schemas in the data source to relational schemas. |
| XML | Connects to and transforms an XML hierarchy model to a relational model. |
| SOAP Web Service | Connects to a SOAP Web Service data source by importing a WSDL file. Logi JReport Designer supports SOAP Web Services defined by WSDL 1.1 or WSDL 2.0 as data sources. |
| MongoDB | Connects to a MongoDB database and transforms the collections in the database to relational schemas. |
| Hive | Connects to a relational database stored in a Hive data warehouse via a JDBC connection. |
| Elasticsearch | Connects to an Elasticsearch data source and transforms the schemas in the data source to relational schemas. |
| User Defined | Through the User Data Source API, Logi JReport Designer can access data from an external data source, such as a text file or Excel file, which is not stored in a database or when there is no JDBC driver available. |
| Hierarchical | Logi JReport Designer directly supports XML format data source by wrapping the provided Hierarchical Data Source API. Logi JReport Designer's built-in classes can implement the XML format hierarchical data source interface. You can directly import an XML data source to a catalog. |

For detailed information about each connection type, see [Data Source Connections](https://devnet.logianalytics.com/hc/en-us/articles/1500010029402-Data-Source-Connections).

This topic explores the following connection types:

* [JDBC Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500011432082-JDBC-Connection)
* [XML Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500011431982-XML-Connection)
* [SOAP Web Service Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500011432002-SOAP-Web-Service-Connection)
* [MongoDB Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500011432042-MongoDB-Connection)
* [JSON Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500011432062-JSON-Connection)
* [EnterpriseDB Stored Procedure UDS](https://devnet.logianalytics.com/hc/en-us/articles/1500011432022-EnterpriseDB-Stored-Procedure-UDS)

![](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500011431942-Data-Mashup) [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011432082-JDBC-Connection)
