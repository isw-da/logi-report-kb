---
title: "Using User-Defined Data Sources"
id: 4405661435031
section: "Connecting to Your Data Sources - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661435031-Using-User-Defined-Data-Sources
updated_at: 2022-01-27T20:34:41Z
---

# Using User-Defined Data Sources

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661418007-Connecting-via-Elasticsearch-Connections)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664421655-User-Data-Source-API)

# Using User-Defined Data Sources

Designer can access data from an external data source, such as a Text file or Excel file which is not stored in a database, or when there is no JDBC driver available. This feature uses the User Data Source (UDS) API Logi Report provides. In addition, due to the unique nature of Oracle and Enterprise DB stored procedures, you are not able to add them into a catalog directly. As a substitute, Logi Report has developed a user data source class that can use stored procedures in Oracle and EnterpriseDB. This topic introduces the UDS API, and how you can add user-defined data sources into a catalog and use Oracle and Enterprise DB stored procedures via the UDS API.

You can use a user-defined data source to create page reports directly, and in this sense a user-defined data source functions the same as a [query](https://devnet.logianalytics.com/hc/en-us/articles/4405661915543-Working-with-Queries). Therefore, you can use the [Data Manager](https://devnet.logianalytics.com/hc/en-us/articles/4405664684439-Managing-the-Data-Retrieval-of-Queries) to control the data retrieval of user-defined data sources and create [cached result files](https://devnet.logianalytics.com/hc/en-us/articles/4405664683031-Working-with-Cached-Query-Results) for user-defined data sources the same as you do for queries. You can also use user-defined data sources to build queries and [business views](https://devnet.logianalytics.com/hc/en-us/articles/4405664680215-Working-with-Business-Views).

Select the following links to view the topics:

* [User Data Source API](https://devnet.logianalytics.com/hc/en-us/articles/4405664421655-User-Data-Source-API)
* [Adding User-Defined Data Sources to a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/4405661436055-Adding-User-Defined-Data-Sources-to-a-Catalog)
* [Oracle Stored Procedure UDS](https://devnet.logianalytics.com/hc/en-us/articles/4405661438615-Oracle-Stored-Procedure-UDS)
* [EnterpriseDB Stored Procedure UDS](https://devnet.logianalytics.com/hc/en-us/articles/4405661437591-EnterpriseDB-Stored-Procedure-UDS)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661418007-Connecting-via-Elasticsearch-Connections)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664421655-User-Data-Source-API)
