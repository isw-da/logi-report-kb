---
title: "Query Properties"
id: 5735584895639
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735584895639-Query-Properties
updated_at: 2022-11-02T08:09:49Z
---

# Query Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735545728919-Parameter-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735584906647-Query-Column-Properties)

# Query Properties

This topic describes the properties of a [Query object](https://devnet.logianalytics.com/hc/en-us/articles/5735547120407-Working-with-Queries) in a catalog.

| Property Name | Description |
| --- | --- |
| Data Source Filter | Specifies whether to allow using the query to filter multiple queries. For more information, see [Using a Query to Filter Multiple Queries](https://devnet.logianalytics.com/hc/en-us/articles/5735547165591-Applying-the-Filter-of-a-Query-to-Multiple-Queries). Data type: Boolean |
| Description | Specifies the description of the query. Data type: String |
| Enable SQL Statement Creator | Specifies whether the query uses the dynamic query interface to get the result set. When you set this property to "true", Logi Report Engine can regenerate the query at runtime using the dynamic query interface. For more information, see [Dynamic Queries](https://devnet.logianalytics.com/hc/en-us/articles/5735586234007-Applying-Dynamic-Queries). Data type: Boolean |
| Maximum Duration | Specifies the maximum elapsed time allowed to fetch data from the data source when the query runs, measured in seconds. By default, the property value is blank, meaning, the time is unlimited. For more information, see [Limiting the Query Run Time and Number of Records](https://devnet.logianalytics.com/hc/en-us/articles/5735555374103-Managing-the-Data-Retrieval-of-Queries#Limit). Data type: Integer |
| Maximum Rows | Specifies the maximum number of rows to be fetched from the data source when the query runs. By default, the property value is blank, meaning, the number is unlimited. For more information, see [Limiting the Query Run Time and Number of Records](https://devnet.logianalytics.com/hc/en-us/articles/5735555374103-Managing-the-Data-Retrieval-of-Queries#Limit). Data type: Integer |
| Name | Specifies the mapped name of the query in the catalog. Data type: String |
| Path Name | Specifies the pre-join path the query applies. For more information, see [Creating Queries Using Pre-join](https://devnet.logianalytics.com/hc/en-us/articles/5735555451159-Using-Pre-joins-in-Queries#Create). Data type: String |
| [Push Down Group Query](https://devnet.logianalytics.com/hc/en-us/articles/5735516614679-JDBC-Hive-Connection-Properties#PushDown) | Specifies whether to push down group level summary computations in the reports that use the query to the database at runtime. Choose an option from the drop-down list.  * **default** Select to apply the setting of the same property for the JDBC connection based on which you create the query. * **true** Select to push down the group level summary computations to the database if it can perform the computations; otherwise, Logi Report Engine do the computations itself. * **false** Select to have Logi Report Engine perform the group level summary computations itself.   Data type: Enumeration |
| Read Only | Specifies whether the query is read only. Choose an option from the drop-down list.  * **default** Select to apply the setting from the database. * **read & write** Select to allow users to access the database in read-write mode. * **read only** Select to allow users to access the database in read-only mode. This option can speed up the transaction of the catalog.   Data type: Enumeration |
| Share | Specifies whether to share the query. For more information, see [Locking Queries](https://devnet.logianalytics.com/hc/en-us/articles/5735586251671-Locking-Queries). Data type: Boolean |
| Transaction Mode | Specifies the transaction mode for the query. Choose an option from the drop-down list.  * **default** Select to apply the setting from the database. * **none** Select to not use transactions for the query. * **read uncommitted** Select to allow dirty reads, non-repeatable reads, and phantom reads to occur for the query. This mode can speed up the transaction of the catalog. * **read committed** Select to prevent dirty reads, and allow non-repeatable reads and phantom reads to occur for the query. * **repeatable read** Select to prevent dirty reads and non-repeatable reads, and allow phantom reads to occur for the query. * **serializable** Select to prevent dirty reads, non-repeatable reads, and phantom reads for the query.   Data type: Enumeration |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735545728919-Parameter-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735584906647-Query-Column-Properties)
