---
title: "Stored Procedure Properties"
id: 4405661820055
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661820055-Stored-Procedure-Properties
updated_at: 2022-01-27T20:38:04Z
---

# Stored Procedure Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664639127-Security-Entry-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661821079-Stored-Procedure-Column-Properties)

# Stored Procedure Properties

This topic describes the properties of a [Stored Procedure object](https://devnet.logianalytics.com/hc/en-us/articles/4405661423383-Using-Stored-Procedures) in a catalog.

| Property Name | Description |
| --- | --- |
| Connection Name | Specifies the connection to execute the stored procedure. Data type: String |
| Description | Specifies the description of the stored procedure. Data type: String |
| Maximum Duration | Specifies the maximum elapsed time allowed to fetch data from the data source when the stored procedure runs, measured in seconds. By default, the property value is blank, meaning the time is unlimited. For more information, see [Limiting the Query Run Time and Number of Records](https://devnet.logianalytics.com/hc/en-us/articles/4405664684439-Managing-the-Data-Retrieval-of-Queries#Limit). Data type: Integer |
| Maximum Rows | Specifies the maximum number of rows to be fetched from the data source when the stored procedure runs. By default, the property value is blank, meaning the number is unlimited. For more information, see [Limiting the Query Run Time and Number of Records](https://devnet.logianalytics.com/hc/en-us/articles/4405664684439-Managing-the-Data-Retrieval-of-Queries#Limit). Data type: Integer |
| Name | Specifies the mapped name of the stored procedure in the catalog. Data type: String |
| Procedure Name | Specifies the stored procedure name in the raw database. Data type: String |
| Qualifier | Specifies the name of the database catalog for the stored procedure. Data type: String |
| Read Only | Specifies whether the stored procedure is read only. Choose an option from the drop-down list.  * **default** - Select to apply the setting from the database. * **read & write** - Select to allow users to access the database in read-write mode. * **read only** - Select to allow users to access the database in read-only mode. This option can speed up the transaction of the catalog.   Data type: Enumeration |
| Schema | Specifies the stored procedure schema. Data type: String |
| Transaction Mode | Specifies the transaction mode for the stored procedure. Choose an option from the drop-down list.  * **default** Select to apply the setting from the database. * **none** Select to not use transactions for the stored procedure. * **read uncommitted** Select to allow dirty reads, non-repeatable reads, and phantom reads to occur for the stored procedure. This mode can speed up the transaction of the catalog. * **read committed** Select to prevent dirty reads, and allow non-repeatable reads and phantom reads to occur for the stored procedure. * **repeatable read** Select to prevent dirty reads and non-repeatable reads, and allow phantom reads to occur for the stored procedure. * **serializable** Select to prevent dirty reads, non-repeatable reads, and phantom reads for the stored procedure.   Data type: Enumeration |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664639127-Security-Entry-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661821079-Stored-Procedure-Column-Properties)
