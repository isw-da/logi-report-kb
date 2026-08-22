---
title: "Query Properties"
id: 1500009634861
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009634861-Query-Properties
updated_at: 2021-07-24T16:03:45Z
---

# Query Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009634841-Parameter-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009611742-Query-Column-Properties)

# Query Properties

This topic lists the properties of a Query object in a catalog.

| Property Name | Description |
| --- | --- |
| Data Source Filter | Specifies whether the query can be used in data source filters.  * **true** - The query can be used to filter multiple queries. See [Using a Query to Filter Multiple Queries](https://devnet.logianalytics.com/hc/en-us/articles/1500009636021-Using-a-Query-to-Filter-Multiple-Queries) for details. * **false** - The query is a normal query. It is the default value.   Data type: Boolean |
| Description | Specifies the description of the query. Data type: String |
| Enable SQL Statement Creator | Specifies whether or not the query uses the dynamic query interface to get the result set. When it is set to true, the query can be re-generated at runtime using the dynamic query interface (for more information, see [Dynamic Queries](https://devnet.logianalytics.com/hc/en-us/articles/1500009636001-Dynamic-Queries)). Data type: Boolean |
| Maximum Duration | Specifies the maximum elapsed time allowed to fetch data from the data source when the query runs, measured in seconds. If the value is set to zero or is blank, it means the time will be unlimited. For usage about the property, see [Limiting the Query Run Time and Number of Records](https://devnet.logianalytics.com/hc/en-us/articles/1500009613182-Data-Manager#Limit).  Data type: Integer |
| Maximum Rows | Specifies the maximum number of rows that will be fetched from the data source when the query runs. If the value is set to zero or is blank, it means the number will be unlimited. For usage about the property, see [Limiting the Query Run Time and Number of Records](https://devnet.logianalytics.com/hc/en-us/articles/1500009613182-Data-Manager#Limit).  Data type: Integer |
| Name | Specifies the name of the query. Data type: String |
| Path Name | Specifies the path in pre-join that the query is created on (for more information, see [Creating Queries Using Pre-join](https://devnet.logianalytics.com/hc/en-us/articles/1500009636061-Using-Pre-joins-in-Queries#Create)). Data type: String |
| [Push Down Group Query](https://devnet.logianalytics.com/hc/en-us/articles/1500009634701-JDBC-Hive-Connection-Properties#PushDown) | Specifies whether to push down group level summary computations in reports that are created based on the query to the DBMS at runtime. Choose an option from the drop-down list.  * default - The setting of the Push Down Group Query property on the JDBC connection where the query is created will be applied. * true - Logi Report will push down the group level summary computations to the DBMS if the DBMS can do the computations, otherwise, Logi Report will do the computations itself. * false - Logi Report will do the group level summary computations itself.   Data type: Boolean |
| Read Only | Specifies whether or not the query will be read only. Data type: Enumeration |
| Share | Specifies whether or not to share the query (for details, see [Locking Queries](https://devnet.logianalytics.com/hc/en-us/articles/1500009613222-Locking-Queries)). Data type: Boolean |
| Transaction Mode | Specifies the transaction mode for the query. Choose an option from the drop-down list.  * **default** - Indicates the transaction information cannot be got from JDBC connection. * **none** - Indicates that transactions are not supported. * **read uncommitted** - Dirty reads, non-repeatable reads and phantom reads can occur. This mode will speed up the transaction of the catalog. * **read committed** - Dirty reads are prevented; non-repeatable reads and phantom reads can occur. * **repeatable read** - Dirty reads and non-repeatable reads are prevented; phantom reads can occur. * **serializable** - Dirty reads, non-repeatable reads and phantom reads are prevented.   Data type: Enumeration |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009634841-Parameter-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009611742-Query-Column-Properties)
