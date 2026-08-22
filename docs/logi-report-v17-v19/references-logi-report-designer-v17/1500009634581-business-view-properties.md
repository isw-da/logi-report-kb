---
title: "Business View Properties"
id: 1500009634581
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009634581-Business-View-Properties
updated_at: 2021-07-24T16:03:49Z
---

# Business View Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009634561-Catalog-Data-Object-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009611582-Aggregation-Properties)

# Business View Properties

This topic lists the properties of a Business View object in a catalog.

| Property Name | Description |
| --- | --- |
| This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.Auto Add Prefix in Display Names | Similar to the data source property [Use Mapping Name Prefix](https://devnet.logianalytics.com/hc/en-us/articles/1500009634641-Data-Source-Properties#Prefix) which controls whether the table names will be prefixed as "tablename\_" in the default mapping names of their columns, this property decides whether to automatically append the same prefix in the default display names of the view elements in the business view when adding view elements based on the columns. The two properties work independently from each another, which means you can have column names prefixed with corresponding table names in a data source automatically by setting Use Mapping Name Prefix to true, but choose not to have the prefix for view elements by setting Auto Add Prefix in Display Names to false. By default the property is false. In this case, when a column's mapping name contains the "tablename\_" prefix which however is not automatically generated but user customized and you add a view element based on the column, the prefix will still be removed from the display name of the view element.  You can also set this property via the [same-name menu option](https://devnet.logianalytics.com/hc/en-us/articles/1500009607342-Business-View-Editor-Dialog#Prefix) in the Business View Editor.  Data type: Boolean |
| Description | Specifies the description of the business view. Data type: String |
| Display Name | Specifies the display name of the business view. Data type: String |
| Maximum Duration | Specifies the maximum elapsed time allowed to fetch data from the data source when the business view runs, measured in seconds. If the value is set to zero or is blank, it means the time will be unlimited. For usage about the property, see [Limiting the query run time and number of records](https://devnet.logianalytics.com/hc/en-us/articles/1500009613182-Data-Manager#Limit).  Data type: Integer |
| Maximum Rows | Specifies the maximum number of rows that will be fetched from the data source when the business view runs. If the value is set to zero or is blank, it means the number will be unlimited. For usage about the property, see [Limiting the query run time and number of records](https://devnet.logianalytics.com/hc/en-us/articles/1500009613182-Data-Manager#Limit).  Data type: Integer |
| Prefetch | When the property is true, Logi Report will fetch all the columns from the raw database that are referenced by the business view into cache and reuse them afterwards when end users run web reports or dashboards that use the business view. This reduces the querying and connecting times to the database and can help improve the runtime performance. However Prefetch=true does not work when scheduling to run web reports, therefore you may get different report result when running the same web report in different ways. When the property is false, Logi Report will query data on demand. When several business view elements are based on the same columns, they will reuse the columns.  The property also affects the following:   * When it is true, the List<ColumnInfo> parameter in the implementation class of the [QueryOptimizer](https://devnet.logianalytics.com/hc/en-us/articles/1500009634701-JDBC-Hive-Connection-Properties#Optimizer) interface will include all columns in the business view, otherwise it will only include columns used by the report or dashboard. * When it is true, all the parameters used by the business view will be prompted in the UI for specifying the parameter values at runtime, otherwise only the parameters referenced by data objects that are used in the report or dashboard will be prompted.   Data type: Boolean |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009634561-Catalog-Data-Object-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009611582-Aggregation-Properties)
