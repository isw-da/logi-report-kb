---
title: "Business View Properties"
id: 1500009590341
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009590341-Business-View-Properties
updated_at: 2021-07-24T05:54:28Z
---

# Business View Properties

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590321-Catalog-Data-Object-Properties)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568702-Aggregation-Object-Properties)

# Business View Properties

The properties of a business view are as follows:

| Property Name | Description |
| --- | --- |
| Description | Specifies the description of the business view, which will be shown when you hover the mouse pointer over the business view in the Resources panel of Web Report Studio or the Resource View panel of Page Report Studio. Data type: String |
| Display Name | Specifies the display name of the business view. Data type: String |
| Maximum Duration | Specifies the maximum elapsed time allowed to fetch data from the data source when the business view runs, measured in seconds. If the value is set to zero or is blank, it means the time will be unlimited. For usage about the property, see [Limiting the Query Run Time and Number of Records](https://devnet.logianalytics.com/hc/en-us/articles/1500009592481-Data-Manager#Limit).  Data type: Integer |
| Maximum Rows | Specifies the maximum number of rows that will be fetched from the data source when the business view runs. If the value is set to zero or is blank, it means the number will be unlimited. For usage about the property, see [Limiting the Query Run Time and Number of Records](https://devnet.logianalytics.com/hc/en-us/articles/1500009592481-Data-Manager#Limit).  Data type: Integer |
| Prefetch | If true, when end user runs a report or dashboard created on the business view, Logi JReport will fetch all used data from the business view and reuse them afterwards. If false, Logi JReport will query data on demand. When several business view elements are based on the same columns, they will reuse the columns.  The property works on Logi JReport Server.  When the property is true, the List<ColumnInfo> parameter in the implementation class of the [QueryOptimizer](https://devnet.logianalytics.com/hc/en-us/articles/1500009590441-JDBC-HIVE-Connection-Properties#Optimizer) interface will include all columns in the business view, otherwise, it will only include columns used by the report or dashboard.  For business views in MongoDB and HIVE connections, the default value is false; for those in other connections, the default value is true.  Data type: Boolean |

The following topics show properties of the business view elements:

> * [Aggregation Object](https://devnet.logianalytics.com/hc/en-us/articles/1500009568702-Aggregation-Object-Properties)
> * [Category](https://devnet.logianalytics.com/hc/en-us/articles/1500009590361-Category-Properties)
> * [Detail Object](https://devnet.logianalytics.com/hc/en-us/articles/1500009590381-Detail-Object-Properties)
> * [Group Object](https://devnet.logianalytics.com/hc/en-us/articles/1500009568722-Group-Object-Properties)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590321-Catalog-Data-Object-Properties)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568702-Aggregation-Object-Properties)
