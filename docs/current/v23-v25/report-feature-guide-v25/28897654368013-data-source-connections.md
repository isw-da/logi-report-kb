---
title: "Data Source Connections"
id: 28897654368013
section: "Report Feature Guide v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897654368013-Data-Source-Connections
updated_at: 2026-02-26T02:10:45Z
source_host: docs-report.zendesk.com
---
# 
Data Source Connections

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

- JDBC Connection

- XML Connection

- SOAP Web Service Connection

- MongoDB Connection

- JSON Connection

- EnterpriseDB Stored Procedure UDS
