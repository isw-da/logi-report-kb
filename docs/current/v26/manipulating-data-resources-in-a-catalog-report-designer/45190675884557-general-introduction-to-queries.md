---
title: "General Introduction to Queries"
id: 45190675884557
section: "Manipulating Data Resources in a Catalog - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190675884557-General-Introduction-to-Queries
updated_at: 2026-04-30T15:16:01Z
source_host: logi-report-v26.insightsoftware.com
---
# 
General Introduction to Queries

This topic describes the features of the Report queries generally.

The concept of queries in Report is similar to that of views in the database but they are stored in the catalog file rather than the database itself. In this way, a query is independent from the raw database since Report uses a mapping name that is unique instead of the "table.column" syntax of SQL. You can use queries to view, change, and analyze data in different ways, and Report can help you with the building of various professional reports based on queries. When creating a query, you can place criteria or restrictions on the data to extract only the required data from the database. For example, instead of having to view all the customers of your company, you can view just the customers from Japan.

You can mash up multiple data resources such as tables, imported SQLs, stored procedures, and user-defined data sources from different connections into a single query for more complex, deeper insights, and create distributed joins to set up inter-relationships between the data resources. Data mash-up makes it possible to integrate multiple separated application systems in your enterprise so as to get more comprehensive and objective data for decision making. Distributed joins extend this by letting you access multiple data resources as one virtual data resource. Report treats all the data resources added to a query  the same as tables.

Designer includes an interactive query designer - the Query Editor, to build any queries. However, Report queries support a limited set of SQL 92 functions that are common to all database systems. Each vendor has many extensions to these basic functions and if you want to use them, it is best to use either imported SQLs or stored procedures. When you create a query using the Query Editor and do not add features Report does not know how to parse, you can take advantage of Push Down Group Query to allow Report to add aggregation functions and a GROUP BY clause to specify the groups required based on the groups in the component being used. This is a big performance advantage when you use queries instead of imported SQLs, stored procedures, and other query types.

In addition, Report supports the Multiple Query Engine to provide smart query processing, which automatically detects schemas and splits large queries into multiple small queries that greatly improve performance. It is activated when the following conditions are satisfied:

- You have predefined links between primary keys and foreign keys in your database.

- The query contains data resources from a single connection only. 

- The Push Down Group Query property is enabled.
