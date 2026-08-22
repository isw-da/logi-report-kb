---
title: "Connecting via JDBC Connections"
id: 4405664412311
section: "Connecting to Your Data Sources - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664412311-Connecting-via-JDBC-Connections
updated_at: 2022-01-27T20:34:40Z
---

# Connecting via JDBC Connections

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661416727-Connecting-to-Your-Data-Sources)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661427991-Setting-Up-JDBC-Connections-in-a-Catalog)

# Connecting via JDBC Connections

JDBC is a Java API for executing SQL statements. It consists of a set of classes and interfaces written in the Java programming language, which enables SQL statements to be executed against virtually any relational database and other types of data that also support JDBC. This topic introduces how you can set up JDBC connections in a catalog to retrieve data from relational databases for your reports, use the connection plug-ins to create connections in an easy way, work with the DBMS objects got via the connections, and run the Model Wizard to import data via OOJDBC data sources.

Select the following links to view the topics:

* [Setting Up JDBC Connections in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/4405661427991-Setting-Up-JDBC-Connections-in-a-Catalog)
* [Creating JDBC Connections via Plug-ins](https://devnet.logianalytics.com/hc/en-us/articles/4405664415895-Creating-JDBC-Connections-via-Plug-ins)
* [Using the DBMS Objects via JDBC Connections](https://devnet.logianalytics.com/hc/en-us/articles/4405664413207-Using-DBMS-Objects-via-JDBC-Connections)
* [Using Data Sources via OOJDBC in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/4405661426711-Using-Data-Sources-via-OOJDBC-in-a-Catalog)

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4420542088087/criticalicon.gif) You cannot use all the data types supported by JDBC in Designer. The data types Designer supports are: Bit, Tinyint, Smallint, Integer, Bigint, Float, Real, Double, Numeric, Decimal, Char, VarChar, LongVarChar, Date, Time, Timestamp, Binary, LongVarBinary, Blob, Clob, Array, and nVarChar. For the Blob, Clob, and Array types, you cannot browse their data in the Catalog Manager; however, you can use the Blob data type to display images.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661416727-Connecting-to-Your-Data-Sources)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661427991-Setting-Up-JDBC-Connections-in-a-Catalog)
