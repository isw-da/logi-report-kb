---
title: "Imported SQL Properties"
id: 1500010100101
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010100101-Imported-SQL-Properties
updated_at: 2021-07-23T19:16:25Z
---

# Imported SQL Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099821-Imported-APE-Column-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010061542-Imported-SQL-Column-Properties)

# Imported SQL Properties

This topic lists the properties of an Imported SQL object in a catalog.

| Property Name | Description |
| --- | --- |
| Connection Name | Specifies the connection to execute the imported SQL. Data type: String |
| Description | Specifies the description of the imported SQL. Data type: String |
| Maximum Duration | Specifies the maximum elapsed time allowed to fetch data from the data source when the imported SQL runs, measured in seconds. If the value is set to zero or is blank, it means the time will be unlimited. For usage about the property, see [Limiting the Query Run Time and Number of Records](https://devnet.logianalytics.com/hc/en-us/articles/1500010062602-Managing-the-Data-Retrieval-of-Queries#Limit).  Data type: Integer |
| Maximum Rows | Specifies the maximum number of rows that will be fetched from the data source when the imported SQL runs. If the value is set to zero or is blank, it means the number will be unlimited. For usage about the property, see [Limiting the Query Run Time and Number of Records](https://devnet.logianalytics.com/hc/en-us/articles/1500010062602-Managing-the-Data-Retrieval-of-Queries#Limit).  Data type: Integer |
| Name | Specifies the name of the imported SQL. Data type: String |
| Qualifier | Specifies the database's catalog name of the imported SQL. Data type: String |
| Read Only | Specifies whether or not the imported SQL will be read only. Data type: Enumeration |
| Transaction Mode | Specifies the transaction mode for the imported SQL. Choose an option from the drop-down list.  * **default** - Indicates the transaction information cannot be got from JDBC connection. * **none** - Indicates that transactions are not supported. * **read uncommitted** - Dirty reads, non-repeatable reads and phantom reads can occur. This mode will speed up the transaction of the catalog. * **read committed** - Dirty reads are prevented; non-repeatable reads and phantom reads can occur. * **repeatable read** - Dirty reads and non-repeatable reads are prevented; phantom reads can occur. * **serializable** - Dirty reads, non-repeatable reads and phantom reads are prevented.   Data type: Enumeration |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099821-Imported-APE-Column-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010061542-Imported-SQL-Column-Properties)
