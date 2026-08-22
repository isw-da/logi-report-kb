---
title: "Using User-Defined Data Sources"
id: 5735521621399
section: "Connecting to Your Data Sources - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735521621399-Using-User-Defined-Data-Sources
updated_at: 2022-11-02T08:16:22Z
---

# Using User-Defined Data Sources

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735564552471-Accessing-Data-via-Elasticsearch-Connections)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735521631127-User-Data-Source-API)

# Using User-Defined Data Sources

Designer can access data from an external data source, such as a Text file or Excel file which is not stored in a database, or when there is no JDBC driver available. This feature uses the User Data Source (UDS) API Logi Report provides. In addition, due to the unique nature of Oracle and Enterprise DB stored procedures, you are not able to add them into a catalog directly. As a substitute, Logi Report has developed a user data source class that can use stored procedures in Oracle and EnterpriseDB. This topic introduces the UDS API, and how you can add user-defined data sources into a catalog and use Oracle and Enterprise DB stored procedures via the UDS API.

You can use a user-defined data source to create page reports directly, and in this sense a user-defined data source functions the same as a [query](https://devnet.logianalytics.com/hc/en-us/articles/5735547120407-Working-with-Queries). Therefore, you can use the [Data Manager](https://devnet.logianalytics.com/hc/en-us/articles/5735555374103-Managing-the-Data-Retrieval-of-Queries) to control the data retrieval of user-defined data sources and create [cached result files](https://devnet.logianalytics.com/hc/en-us/articles/5735586187287-Working-with-Cached-Query-Results) for user-defined data sources the same as you do for queries. You can also use user-defined data sources to build queries and [business views](https://devnet.logianalytics.com/hc/en-us/articles/5735547021975-Working-with-Business-Views).

Select the following links to view the topics:

* [User Data Source API](https://devnet.logianalytics.com/hc/en-us/articles/5735521631127-User-Data-Source-API)
* [Adding User-Defined Data Sources to a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/5735499573911-Adding-User-Defined-Data-Sources-to-a-Catalog)
* [Oracle Stored Procedure UDS](https://devnet.logianalytics.com/hc/en-us/articles/5735507895319-Oracle-Stored-Procedure-UDS)
* [EnterpriseDB Stored Procedure UDS](https://devnet.logianalytics.com/hc/en-us/articles/5735507886999-EnterpriseDB-Stored-Procedure-UDS)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735564552471-Accessing-Data-via-Elasticsearch-Connections)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735521631127-User-Data-Source-API)
