---
title: "MongoDB Connection Properties"
id: 5735526093591
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735526093591-MongoDB-Connection-Properties
updated_at: 2022-11-02T08:09:45Z
---

# MongoDB Connection Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735532649367-JSON-Elasticsearch-Schema-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735516671127-MongoDB-Database-Properties)

# MongoDB Connection Properties

This topic describes the properties of a [MongoDB Connection object](https://devnet.logianalytics.com/hc/en-us/articles/5735564769943-Accessing-Data-via-MongoDB-Connections) in a catalog.

| Property Name | Description |
| --- | --- |
| Connection Options | Specifies the options used to connect to the MongoDB server, which are "name=value" pairs separated by "&". You can reference [parameters](https://devnet.logianalytics.com/hc/en-us/articles/5735532413719-Working-with-Parameters) and [constant level formulas](https://devnet.logianalytics.com/hc/en-us/articles/5735525461399-Formula-Levels#CLF) in the current catalog data source in the format *@FieldName*, and the special field "[User Name](https://devnet.logianalytics.com/hc/en-us/articles/5735564398999-Working-with-Special-Fields#UserName)" as *@username* in the value. Data type: String |
| Default | Specifies whether the connection is the default connection in the current catalog data source. By default, the first connection you create in a data source is the default connection of the data source. A data source can have zero or one default connection. Data type: Boolean |
| Description | Specifies the description of the connection. Data type: String |
| Name | Specifies the mapped name of the connection in the catalog. Data type: String |
| Password | Specifies the password for connecting to the MongoDB database. You can reference a parameter or constant level formula in the current catalog data source in the format *@FieldName*, or the special field "User Name" as *@username* in the password. If you save the catalog in XML, Designer encrypts the password using a internal algorithm and stores it in the XML catalog file. Designer decrypts the password when loading the XML catalog.  Data type: String |
| [Push Down Group Query](https://devnet.logianalytics.com/hc/en-us/articles/5735516614679-JDBC-Hive-Connection-Properties#PushDown) | Specifies whether to push down group level summary computations to the database at runtime.  * **true** Select to push down the group level summary computations to the database if it can perform the computations; otherwise, Logi Report Engine do the computations itself. * **false** Select to have Logi Report Engine perform the group level summary computations itself.   Data type: Boolean |
| Server Address | Shows a list of replica set members or MongoDBs, including IP/host name and port pairs. Read only. If the list contains no IP/host name and port pairs, it means connecting to the local host with the default MongoDB port. For each pair in the list, the IP/host name cannot be null, while the port can be. When the port is null, it means connecting to the MongoDB by the default port. |
| User | Specifies the user ID for connecting to the MongoDB database. You can reference a parameter or constant level formula in the current catalog data source in the format *@FieldName*, or the special field "User Name" as *@username* in the user ID. Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735532649367-JSON-Elasticsearch-Schema-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735516671127-MongoDB-Database-Properties)
