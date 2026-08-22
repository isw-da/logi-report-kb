---
title: "JDBC Connections"
id: 1500010064301
section: "Connecting to Your Data Sources - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010064301-JDBC-Connections
updated_at: 2021-07-24T10:39:15Z
---

# JDBC Connections

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010029402-Data-Source-Connections) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010064401-Setting-Up-JDBC-Connections-in-a-Catalog)

# JDBC Connections

JDBC is a Java API for executing SQL statements. It consists of a set of classes and interfaces written in the Java programming language which enables SQL statements to be executed against virtually any relational database as well as other types of data that also support JDBC. By setting up JDBC connections in a Logi JReport catalog, you can retrieve data from the relational databases for your reports.

Logi JReport Designer also provides connection plugins for the most commonly used relational databases: Oracle, MySQL, SQL Server and PostgreSQL, for an easy connection setup procedure.

This section contains the following topics:

* [Setting Up JDBC Connections in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500010064401-Setting-Up-JDBC-Connections-in-a-Catalog)
* [JDBC Connection Plugins](https://devnet.logianalytics.com/hc/en-us/articles/1500010029442-JDBC-Connection-Plugins)
* [DBMS Objects in JDBC Connections](https://devnet.logianalytics.com/hc/en-us/articles/1500010064321-DBMS-Objects-in-JDBC-Connections)
* [Using Data Sources via OOJDBC](https://devnet.logianalytics.com/hc/en-us/articles/1500010064381-Using-Data-Sources-via-OOJDBC)

**Notes:**

* In Logi JReport Designer, not all the data types supported by JDBC can be used. The data types that are supported in Logi JReport Designer are: Bit, Tinyint, Smallint, Integer, Bigint, Float, Real, Double, Numeric, Decimal, Char, VarChar, LongVarChar, Date, Time, Timestamp, Binary, LongVarBinary, Blob, Clob, Array, and nVarChar.
* For the Blob, Clob, and Array types, you cannot browse their data in the Catalog Manager; however, the Blob data type can be used to display images.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010029402-Data-Source-Connections) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010064401-Setting-Up-JDBC-Connections-in-a-Catalog)
