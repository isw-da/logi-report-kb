---
title: "Query Properties"
id: 1500009568942
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009568942-Query-Properties
updated_at: 2021-07-24T05:54:24Z
---

# Query Properties

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568922-Parameter-Properties)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590561-Query-Column-Properties)

# Query Properties

The properties of a query are as follows:

| Property Name | Description |
| --- | --- |
| Data Source Filter | Specifies whether the query can be used in data source filters.  * true - The query can be used to filter multiple queries. See [Using a Query to Filter Multiple Queries](https://devnet.logianalytics.com/hc/en-us/articles/1500009592541-Using-a-Query-to-Filter-Multiple-Queries) for details. * false - The query is a normal query. It is the default value.   Data type: Boolean |
| Description | Specifies the description of the query. Data type: String |
| Enable SQL Statement Creator | Specifies whether or not the query uses the dynamic query interface to get the result set. When it is set to true, the query can be re-generated at runtime using the dynamic query interface (for more information, see [Dynamic Queries](https://devnet.logianalytics.com/hc/en-us/articles/1500009570642-Dynamic-Query)). Data type: Boolean |
| Maximum Duration | Specifies the maximum elapsed time allowed to fetch data from the data source when the query runs, measured in seconds. If the value is set to zero or is blank, it means the time will be unlimited. For usage about the property, see [Limiting the Query Run Time and Number of Records](https://devnet.logianalytics.com/hc/en-us/articles/1500009592481-Data-Manager#Limit).  Data type: Integer |
| Maximum Rows | Specifies the maximum number of rows that will be fetched from the data source when the query runs. If the value is set to zero or is blank, it means the number will be unlimited. For usage about the property, see [Limiting the Query Run Time and Number of Records](https://devnet.logianalytics.com/hc/en-us/articles/1500009592481-Data-Manager#Limit).  Data type: Integer |
| Name | Specifies the name of the query. Data type: String |
| Path Name | Specifies the path in pre-join that the query is created on (for more information, see [Creating Queries Using Pre-join](https://devnet.logianalytics.com/hc/en-us/articles/1500009592581-Using-Pre-joins-in-Queries#Create)). Data type: String |
| [Push Down Group Query](https://devnet.logianalytics.com/hc/en-us/articles/1500009590441-JDBC-HIVE-Connection-Properties#PushDown) | Specifies whether to push down group level summary computations in reports that are created based on the query to the DBMS at runtime. Choose an option from the drop-down list.  * default - The setting of the Push Down Group Query property on the JDBC connection where the query is created will be applied. * true - Logi JReport will push down the group level summary computations to the DBMS if the DBMS can do the computations, otherwise, Logi JReport will do the computations itself. * false - Logi JReport will do the group level summary computations itself.   Data type: Boolean |
| Read Only | Specifies whether or not the query will be read only. Data type: Enumeration |
| Share | Specifies whether or not to share the query (for details, see [Locking Queries](https://devnet.logianalytics.com/hc/en-us/articles/1500009570782-Locking-Queries)). Data type: Boolean |
| Transaction Mode | Specifies the transaction mode for the query. Choose an option from the drop-down list.  * **default** - Indicates the transaction information cannot be got from JDBC connection. * **none** - Indicates that transactions are not supported. * **read uncommitted** - Dirty reads, non-repeatable reads and phantom reads can occur. This mode will speed up the transaction of the catalog. * **read committed** - Dirty reads are prevented; non-repeatable reads and phantom reads can occur. * **repeatable read** - Dirty reads and non-repeatable reads are prevented; phantom reads can occur. * **serializable** - Dirty reads, non-repeatable reads and phantom reads are prevented.   Data type: Enumeration |

A query contains several columns, the properties of which are shown in the following topic: [Query Column](https://devnet.logianalytics.com/hc/en-us/articles/1500009590561-Query-Column-Properties).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568922-Parameter-Properties)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590561-Query-Column-Properties)
