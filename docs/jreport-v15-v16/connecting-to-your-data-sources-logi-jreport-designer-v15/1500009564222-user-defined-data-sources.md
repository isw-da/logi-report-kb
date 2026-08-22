---
title: "User Defined Data Sources"
id: 1500009564222
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009564222-User-Defined-Data-Sources
updated_at: 2021-07-24T05:55:45Z
---

# User Defined Data Sources

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585381-Example-Developing-Reports-from-a-Web-Service-Data-Source)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585281-User-Data-Source-API)

# User Defined Data Sources

Logi JReport Designer can access data from an external data source, such as a text file, or Excel file, which is not stored in a database, or when there is no JDBC driver available. This feature uses the user data source API provided by Logi JReport. In addition, due to the unique nature of Oracle and Enterprise DB stored procedures, you will not be able to add them into a Logi JReport catalog directly. As a substitute, Logi JReport has developed a user data source class that can use stored procedures in Oracle and EnterpriseDB.

[Queries](https://devnet.logianalytics.com/hc/en-us/articles/1500009592441-Queries) and [business views](https://devnet.logianalytics.com/hc/en-us/articles/1500009562582-Business-Views) can be built on user defined data sources and a report is developed from a query (or something else which is functionally similar) or from a business view.

A user defined data source itself can be used to create page reports directly, and in this sense it functions the same as a query. Therefore you can use the [Data Manager](https://devnet.logianalytics.com/hc/en-us/articles/1500009592481-Data-Manager) to control the data retrieval of user defined data sources, including the number of rows to be displayed and the duration allowed for the retrieval, and use the manager to keep access information from previous runs of a UDS. You can also create [cached result files](https://devnet.logianalytics.com/hc/en-us/articles/1500009570622-Cached-Query-Results) for user defined data sources and save the result files somewhere in your machine, then when you view reports based on the UDSs, you can choose to use the data from the cached query result files as opposed to the database.

The following topics describe tasks associated with User Defined Data Sources:

> * [User Data Source API](https://devnet.logianalytics.com/hc/en-us/articles/1500009585281-User-Data-Source-API)
> * [Adding a UDS to a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009585221-Adding-a-UDS-to-a-Catalog)
> * [Oracle Stored Procedure UDS](https://devnet.logianalytics.com/hc/en-us/articles/1500009585301-Oracle-Stored-Procedure-UDS)
> * [EnterpriseDB Stored Procedure UDS](https://devnet.logianalytics.com/hc/en-us/articles/1500009564282-EnterpriseDB-Stored-Procedure-UDS)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585381-Example-Developing-Reports-from-a-Web-Service-Data-Source)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585281-User-Data-Source-API)
