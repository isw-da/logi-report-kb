---
title: "Stored Procedure Properties"
id: 1500009568902
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009568902-Stored-Procedure-Properties
updated_at: 2021-07-24T05:54:25Z
---

# Stored Procedure Properties

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590541-Query-Modifier-Properties)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590521-Stored-Procedure-Column-Properties)

# Stored Procedure Properties

The properties of a stored procedure are as follows:

| Property Name | Description |
| --- | --- |
| Connection Name | Specifies the connection to execute the stored procedure. Data type: String |
| Description | Specifies the description of the stored procedure. Data type: String |
| Maximum Duration | Specifies the maximum elapsed time allowed to fetch data from the data source when the stored procedure runs, measured in seconds. If the value is set to zero or is blank, it means the time will be unlimited. For usage about the property, see [Limiting the Query Run Time and Number of Records](https://devnet.logianalytics.com/hc/en-us/articles/1500009592481-Data-Manager#Limit).  Data type: Integer |
| Maximum Rows | Specifies the maximum number of rows that will be fetched from the data source when the stored procedure runs. If the value is set to zero or is blank, it means the number will be unlimited. For usage about the property, see [Limiting the Query Run Time and Number of Records](https://devnet.logianalytics.com/hc/en-us/articles/1500009592481-Data-Manager#Limit).  Data type: Integer |
| Name | Specifies the name of the stored procedure. Data type: String |
| Procedure Name | Specifies the stored procedure name in the raw database. Data type: String |
| Qualifier | Specifies the database's catalog name of the stored procedure. Data type: String |
| Read Only | Specifies whether or not the stored procedure will be read only. Choose an option from the drop-down list.  * **read&write** - Users will be able to access the database in read-write mode. * **default** - Accepts the settings from the database that you are connecting to. * **read only** - Users will only be able to access the database in read-only mode. Setting the property value to read only will speed up the transaction of the catalog.   Data type: Enumeration |
| Schema | Specifies the stored procedure schema. Data type: String |
| Transaction Mode | Specifies the transaction mode for the stored procedure. Choose an option from the drop-down list.  * **default** - Indicates the transaction information cannot be got from JDBC connection. * **none** - Indicates that transactions are not supported. * **read uncommitted** - Dirty reads, non-repeatable reads and phantom reads can occur. This mode will speed up the transaction of the catalog. * **read committed** - Dirty reads are prevented; non-repeatable reads and phantom reads can occur. * **repeatable read** - Dirty reads and non-repeatable reads are prevented; phantom reads can occur. * **serializable** - Dirty reads, non-repeatable reads and phantom reads are prevented.   Data type: Enumeration |

A stored procedure contains several columns, the properties of which are shown in the following topic: [Stored Procedure Column](https://devnet.logianalytics.com/hc/en-us/articles/1500009590521-Stored-Procedure-Column-Properties).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590541-Query-Modifier-Properties)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590521-Stored-Procedure-Column-Properties)
