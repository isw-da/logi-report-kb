---
title: "Data Source Connections"
id: 1500010056262
section: "Logi Report Feature Guide v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010056262-Data-Source-Connections
updated_at: 2021-08-02T02:46:17Z
---

# Data Source Connections

![](https://devnet.logianalytics.com/hc/article_attachments/4404856777623/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010056342-Data-Mash-up)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404848352023/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010093361-JDBC-Connection)

# Data Source Connections

Designer requires access to your data source to retrieve data for reports, so before you can create reports in Designer, you need to set up a connection to your data source. Connections are defined, named, and stored in the catalog along with the reports and other resources that use them.

Designer supports the following connection types:

| Connection Type | Description |
| --- | --- |
| JDBC | Connects to a relational database via a JDBC driver. |
| JSON | Connects to a JSON data source and transforms the schemas in the data source to relational schemas. |
| XML | Connects to and transforms an XML hierarchy model to a relational model. |
| SOAP Web Service | Connects to a SOAP Web Service data source by importing a WSDL file. Designer supports SOAP Web Services defined by WSDL 1.1 or WSDL 2.0 as data sources. |
| MongoDB | Connects to a MongoDB database and transforms the collections in the database to relational schemas. |
| Hive | Connects to a relational database stored in a Hive data warehouse via a JDBC connection. |
| Elasticsearch | Connects to an Elasticsearch data source and transforms the schemas in the data source to relational schemas. |
| User Defined | Through the User Data Source API, Designer can access data from an external data source, such as a text file or Excel file, which is not stored in a database or when there is no JDBC driver available. |
| Hierarchical | Designer directly supports XML format data source by wrapping the provided Hierarchical Data Source API. Designer's built-in classes can implement the XML format hierarchical data source interface. You can directly import an XML data source to a catalog. |

We will explore the following in this guide:

* [JDBC Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500010093361-JDBC-Connection)
* [XML Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500010056282-XML-Connection)
* [SOAP Web Service Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500010093441-SOAP-Web-Service-Connection)
* [MongoDB Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500010093401-MongoDB-Connection)
* [JSON Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500010093381-JSON-Connection)
* [EnterpriseDB Stored Procedure UDS](https://devnet.logianalytics.com/hc/en-us/articles/1500010093421-EnterpriseDB-Stored-Procedure-UDS)

![](https://devnet.logianalytics.com/hc/article_attachments/4404856777623/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010056342-Data-Mash-up)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404848352023/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010093361-JDBC-Connection)
