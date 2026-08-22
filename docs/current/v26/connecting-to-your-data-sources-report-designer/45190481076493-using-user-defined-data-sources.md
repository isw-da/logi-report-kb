---
title: "Using User-Defined Data Sources"
id: 45190481076493
section: "Connecting to Your Data Sources - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190481076493-Using-User-Defined-Data-Sources
updated_at: 2026-04-30T15:12:37Z
source_host: logi-report-v26.insightsoftware.com
---
# Using User-Defined Data Sources

            Designer can access data from an external data source, such as a Text file or Excel file which is not stored in a database, or when there is no JDBC driver available. This feature uses the User Data Source (UDS) API Report provides. In addition, due to the unique nature of Oracle and Enterprise DB stored procedures, you are not able to add them into a catalog directly. As a substitute, Report has developed a user data source class that can use stored procedures in Oracle and EnterpriseDB. This topic introduces the UDS API, and how you can add user-defined data sources into a catalog and use Oracle and Enterprise DB stored procedures via the UDS API.

You can use a user-defined data source  to create page reports directly, and in this sense a user-defined data source functions the same as a query. Therefore, you can use the Data Manager to control the data retrieval of user-defined data sources and create cached result files for user-defined data sources the same as you do for queries. You can also use user-defined data sources to build queries and business views.

Select the following links to view the topics:

- User Data Source API

- Adding User-Defined Data Sources to a Catalog 

- Oracle Stored Procedure UDS

- EnterpriseDB Stored Procedure UDS
