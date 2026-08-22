---
title: "User Defined Data Sources"
id: 1500009606982
section: "Connecting to Your Data Sources - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009606982-User-Defined-Data-Sources
updated_at: 2021-07-24T16:05:05Z
---

# User Defined Data Sources

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009629481-Elasticsearch-Connections-) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009607022-User-Data-Source-API)

# User Defined Data Sources

Logi Report Designer can access data from an external data source, such as a text file, or Excel file, which is not stored in a database, or when there is no JDBC driver available. This feature uses the user data source API provided by Logi Report. In addition, due to the unique nature of Oracle and Enterprise DB stored procedures, you will not be able to add them into a Logi Report catalog directly. As a substitute, Logi Report has developed a user data source class that can use stored procedures in Oracle and EnterpriseDB.

A user defined data source itself can be used to create page reports directly, and in this sense it functions the same as a [query](https://devnet.logianalytics.com/hc/en-us/articles/1500009613142-Queries). Therefore, you can use the [Data Manager](https://devnet.logianalytics.com/hc/en-us/articles/1500009613182-Data-Manager) to control the data retrieval of user defined data sources and create [cached result files](https://devnet.logianalytics.com/hc/en-us/articles/1500009635961-Cached-Query-Results) for user defined data sources the same as you do for queries. User defined data sources can also be used to build queries and [business views](https://devnet.logianalytics.com/hc/en-us/articles/1500009635921-Business-Views).

Select the following links to view the topics:

* [User Data Source API](https://devnet.logianalytics.com/hc/en-us/articles/1500009607022-User-Data-Source-API)
* [Adding User Defined Data Sources to a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009607002-Adding-User-Defined-Data-Sources-to-a-Catalog)
* [Oracle Stored Procedure UDS](https://devnet.logianalytics.com/hc/en-us/articles/1500009629681-Oracle-Stored-Procedure-UDS)
* [EnterpriseDB Stored Procedure UDS](https://devnet.logianalytics.com/hc/en-us/articles/1500009629661-EnterpriseDB-Stored-Procedure-UDS)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009629481-Elasticsearch-Connections-) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009607022-User-Data-Source-API)
