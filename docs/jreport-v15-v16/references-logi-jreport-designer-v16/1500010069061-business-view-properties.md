---
title: "Business View Properties"
id: 1500010069061
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010069061-Business-View-Properties
updated_at: 2021-07-24T10:38:07Z
---

# Business View Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010069041-Catalog-Data-Object-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010033502-Aggregation-Properties)

# Business View Properties

This topic lists the properties of a Business View object in a catalog.

| Property Name | Description |
| --- | --- |
| Description | Specifies the description of the business view. Data type: String |
| Display Name | Specifies the display name of the business view. Data type: String |
| Maximum Duration | Specifies the maximum elapsed time allowed to fetch data from the data source when the business view runs, measured in seconds. If the value is set to zero or is blank, it means the time will be unlimited. For usage about the property, see [Limiting the query run time and number of records](https://devnet.logianalytics.com/hc/en-us/articles/1500010034662-Data-Manager#Limit).  Data type: Integer |
| Maximum Rows | Specifies the maximum number of rows that will be fetched from the data source when the business view runs. If the value is set to zero or is blank, it means the number will be unlimited. For usage about the property, see [Limiting the query run time and number of records](https://devnet.logianalytics.com/hc/en-us/articles/1500010034662-Data-Manager#Limit).  Data type: Integer |
| Prefetch | When the property is true, Logi JReport will fetch all the columns from the raw database that are referenced by the business view into cache and reuse them afterwards when end users run web reports or dashboards that use the business view. This reduces the querying and connecting times to the database and can help improve the runtime performance. However Prefetch=true does not work when scheduling to run web reports, therefore you may get different report result when running the same web report in different ways. When the property is false, Logi JReport will query data on demand. When several business view elements are based on the same columns, they will reuse the columns.  The property also affects the following:   * When it is true, the List<ColumnInfo> parameter in the implementation class of the [QueryOptimizer](https://devnet.logianalytics.com/hc/en-us/articles/1500010069181-JDBC-Hive-Connection-Properties#Optimizer) interface will include all columns in the business view, otherwise it will only include columns used by the report or dashboard. * When it is true, all the parameters used by the business view will be prompted in the UI for specifying the parameter values at runtime, otherwise only the parameters referenced by data objects that are used in the report or dashboard will be prompted.   Data type: Boolean |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010069041-Catalog-Data-Object-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010033502-Aggregation-Properties)
