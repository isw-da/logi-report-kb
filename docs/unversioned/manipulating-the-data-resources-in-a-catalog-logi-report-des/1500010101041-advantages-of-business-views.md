---
title: "Advantages of Business Views"
id: 1500010101041
section: "Manipulating the Data Resources in a Catalog - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010101041-Advantages-of-Business-Views
updated_at: 2021-07-23T19:16:45Z
---

# Advantages of Business Views

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010101021-Working-with-Business-Views)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010101081-Business-View-Elements)

# Advantages of Business Views

This topic introduces the advantages of business views as compared with the traditional query resources.

In Logi Report, queries and business view are the data resources for creating report in Designer, and end users can use business views to create ad hoc reports in Server. Different from query resources, business views provide end users with an easily understandable data repository, which contains data resources pertinent to the creation or editing of interactive reports without exposing any underlying data structure to them. They internally contain database connections and relationships between view elements that are required for creating reports but display data to end users in an easy to use flat structure. Business views shield end users from having to understand the underlying data structure, while enabling them to create complex reports containing multiple components. All reports created from a business view automatically include all of the interactivity built into that business view. For example, they can include things like drill down and drill up, so that end users are able to switch data from one group to another; they can allow end users to exchange the columns and rows of a crosstab, and to convert a chart to a crosstab and vice verse.

A business view can contain mashed-up data resources such as tables, stored procedures, queries, and user-defined data sources from different connections, and distributed joins that defines the inter-relationships between the data resources, thus it is able to provide more complex and deeper insights of your data. Data mash-up makes it possible to integrate multiple separated application systems in your enterprise so as to get more comprehensive and objective data for decision making. Distributed joins extend this by letting you access multiple data resources as one virtual data resource. However, mixed data resources cannot get the performance optimization as can single data resource by [pushing down group query](https://devnet.logianalytics.com/hc/en-us/articles/1500010099961-JDBC-Hive-Connection-Properties#PushDown); while, by using Server's in-memory cubes, Logi Report can still guarantee the performance even with big data retrieval.

Business views also support the [Cached Query Result](https://devnet.logianalytics.com/hc/en-us/articles/1500010101101-Working-with-Cached-Query-Results) feature, which enables you to retrieve data to reports from your machine instead of getting data from the database.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010101021-Working-with-Business-Views)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010101081-Business-View-Elements)
