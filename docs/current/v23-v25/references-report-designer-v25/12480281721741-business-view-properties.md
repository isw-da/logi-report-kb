---
title: "Business View Properties"
id: 12480281721741
section: "References - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480281721741-Business-View-Properties
updated_at: 2026-02-25T23:51:10Z
source_host: docs-report.zendesk.com
---
# 
Business View Properties

This topic describes the properties of a Business View object in a catalog.

| Property Name | Description |
| --- | --- |
| Auto Add Prefix in Display Names | Similar to the data source property Use Mapping Name Prefix which controls whether to add "tablename_" as the prefix of the table names in the default mapping names of their columns, this property determines whether to automatically append the same prefix in the default display names of the view elements in the business view when you add view elements based on the columns. The two properties work independently from each another, meaning, you can set Use Mapping Name Prefix to "true" to automatically prefix column names with corresponding table names in a data source, but choose not to have the prefix for view elements by setting Auto Add Prefix in Display Names to "false". By default, the property is "false". In this case, when a column's mapping name contains the "tablename_" prefix which however is not automatically generated but user customized and you add a view element based on the column, Designer still removes the prefix from the display name of the view element. You can also set this property via the same-name menu command in the Business View Editor. Data type: Boolean |
| Description | Specifies the description of the business view. Data type: String |
| Display Name | Specifies the display name of the business view. Data type: String |
| Maximum Duration | Specifies the maximum elapsed time allowed to fetch data from the data source when the business view runs, measured in seconds. By default, the property value is blank, meaning the time is unlimited. For more information, see Limiting the Query Run Time and Number of Records. Data type: Integer |
| Maximum Rows | Specifies the maximum number of rows to be fetched from the data source when the business view runs. By default, the property value is blank, meaning the number is unlimited. For more information, see Limiting the Query Run Time and Number of Records. Data type: Integer |
| Prefetch | When this property is "true", Report Engine fetches all the columns from the raw database which the business view references into cache and reuses them afterwards when users run web reports and dashboards that apply the business view at runtime. This reduces the querying and connecting times to the database and can help improve the runtime performance. However, "Prefetch=true" does not work when users schedule to run web reports, therefore they may get different results when running the same web report in different ways. When this property is "false", Report Engine queries data on demand at runtime. When several business view elements are based on the same columns, they reuse the columns. This property also affects the following: When it is "true", the List parameter in the implementation class of the QueryOptimizer interface includes all columns in the business view; otherwise, it only includes columns that the report or dashboard uses. When it is "true", Server displays all the parameters that the business view applies in the UI for specifying the parameter values at runtime; otherwise, it only displays the parameters the data objects in the report or dashboard reference. Data type: Boolean |
| Shortest Path First | • Specifies whether queries on this Business View should utilize the shortest join path strategy to fetch data.

Priority Rule:
This property interacts with the global system option -Dsystem.shortestPathFirst:
 • If -Dsystem.shortestPathFirst=true: The shortest join path is enforced for all Business Views, overriding this property.
 • If -Dsystem.shortestPathFirst=false (or is unspecified): The setting defined in this property takes effect. |
