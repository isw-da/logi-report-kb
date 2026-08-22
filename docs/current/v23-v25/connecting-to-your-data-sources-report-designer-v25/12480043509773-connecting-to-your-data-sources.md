---
title: "Connecting to Your Data Sources"
id: 12480043509773
section: "Connecting to Your Data Sources - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480043509773-Connecting-to-Your-Data-Sources
updated_at: 2026-02-25T23:50:19Z
source_host: docs-report.zendesk.com
---
# 
Connecting to Your Data Sources

Before you can create reports in Designer, you need to set up a connection in a catalog to enable Designer to retrieve data from your data source for the reports. Designer then stores the connection along with the reports and other resources that use it in the catalog. This topic introduces the connection types Designer supports and how you can  create each of the connections in a catalog. 

Designer is extremely efficient when working with data sources that are in a relational database (RDBMS). The Java Database Connectivity (JDBC) connections are the basic approaches for connecting to a database for data. Designer can also access other data source types.

You can set up connections of the following types in a catalog:

- 
JDBC Connection: Connects to a relational database via a JDBC driver.

- 
JSON Connection: Connects to a JSON data source and transforms the schema in the data source to relational schema.

- 
XML Connection: Connects to and transforms an XML hierarchy model to a relational model.

- 
SOAP Web Service Connection: Connects to a SOAP Web Service data source by importing a WSDL file. Designer supports SOAP Web Services defined by WSDL 1.1 or WSDL 2.0 as data sources.

- 
MongoDB Connection: Connects to a MongoDB database and transforms collections in the database to relational schemas.

- 
Hive Connection: Connects to a relational database stored in a Hive data warehouse via a JDBC connection.  

- 
Elasticsearch Connection: Connects to an Elasticsearch data source and transforms the schema in the data source to relational schema.

- 
User-Defined Data Source: Through the UDS API,  Designer can access data from an external data source, such as a text file or Excel file, which is not stored in a database or when there is no JDBC driver available.

- 
Hierarchical Data Source: Designer directly supports XML data source by wrapping the provided HDS API. Designer's built-in classes can implement the XML hierarchical data source interface. You can directly import an XML data source to a catalog using the Catalog Manager.

See an example: The SampleComponents catalog, included with  Designer, contains reports that have examples of different data source connections. Open the following report to see the connection examples: <install_root>\Demo\Reports\SampleComponents\DataSourceConnections.cls.
