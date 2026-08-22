---
title: "JDBC Connections"
id: 1500009563982
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009563982-JDBC-Connections
updated_at: 2021-07-24T05:55:50Z
---

# JDBC Connections

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563942-Connecting-to-Your-Data-Sources)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584801-Setting-Up-the-JDBC-Driver)

# JDBC Connections

JDBC is a Java API for executing SQL statements. It consists of a set of classes and interfaces written in the Java programming language which enables SQL statements to be executed against virtually any relational database as well as other types of data that also support JDBC. All RDBMS software companies provide their own JDBC Driver and unique driver class and URL to access their database. Usually you can download these for free from the database vendors web site. Logi JReport only includes a JDBC drivers for the HSQLDB and Derby databases.

**Notes:**

* In Logi JReport Designer, not all the data types supported by JDBC can be used. The data types that are supported in Logi JReport Designer are: Bit, Tinyint, Smallint, Integer, Bigint, Float, Real, Double, Numeric, Decimal, Char, VarChar, LongVarChar, Date, Time, TimeStamp, Binary, LongVarBinary, Blob, Clob, Array, and nVarChar.
* For the Blob, Clob, and Array types, you cannot browse their data in the Catalog Manager; however, the Blob data type can be used to display images.

The following topics describe tasks related to JDBC connections:

> * [Setting Up the JDBC Driver](https://devnet.logianalytics.com/hc/en-us/articles/1500009584801-Setting-Up-the-JDBC-Driver)
> * [Setting Up a JDBC Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009584941-Setting-Up-a-JDBC-Connection)
> * [Setting Up OOJDBC Connections](https://devnet.logianalytics.com/hc/en-us/articles/1500009584841-Setting-Up-OOJDBC-Connections)
> * [DBMS Objects in a JDBC Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009564002-DBMS-Objects-in-a-JDBC-Connection)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563942-Connecting-to-Your-Data-Sources)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584801-Setting-Up-the-JDBC-Driver)
