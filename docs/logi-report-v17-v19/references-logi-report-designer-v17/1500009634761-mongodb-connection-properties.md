---
title: "MongoDB Connection Properties"
id: 1500009634761
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009634761-MongoDB-Connection-Properties
updated_at: 2021-07-24T16:03:46Z
---

# MongoDB Connection Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009634741-JSON-Elasticsearch-Schema-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009634781-MongoDB-Database-Properties)

# MongoDB Connection Properties

This topic lists the properties of a MongoDB Connection object in a catalog.

| Property Name | Description |
| --- | --- |
| Connection Options | Specifies the options used to connect to the MongoDB server. The options are name=value pairs and the pairs are separated by "&". Data type: String |
| Default | Specifies whether the connection is the default connection in the current data source. By default, the first added connection in a data source is the default connection of the data source. A data source can have zero or one default connection. Data type: Boolean |
| Description | Specifies the description of the MongoDB connection. Data type: String |
| Name | Specifies the name of the MongoDB connection. If the name has already been used, a number starting from 1 will be appended to the name. For example, if aa exists, the new name will be aa1, and if both aa and aa1 exits, it will be aa2, and so on. If you change the name, the imported SQL and stored procedures that reference the connection will be automatically updated to use the new name. Data type: String |
| Password | Specifies the password for connecting to the MongoDB database, which is determined by the database administrator. When the catalog is saved as xml format, the password will be encrypted by an algorithm and stored in an xml catalog file, and it will be decrypted when the xml format catalog is loaded.  Data type: String |
| [Push Down Group Query](https://devnet.logianalytics.com/hc/en-us/articles/1500009634701-JDBC-Hive-Connection-Properties#PushDown) | Specifies whether to push down group level summary computations in reports to the DBMS at runtime. Choose an option from the drop-down list.  * **true** - Logi Report will push down the group level summary computations to the DBMS if the DBMS can do the computations, otherwise, Logi Report will do the computations itself. * **false** - Logi Report will do the group level summary computations itself.   Data type: Boolean |
| Server Address | Displays a list of replica set members or MongoDBs, including IP/host name and port pairs. This property is read only. If the list contains no IP/host name and port pairs, it means connecting to the local host with the default port of MongoDB. For each pair in the list, the IP/host name cannot be null, while, the port can be null. When the port is null, it means connecting to the MongoDB by the default port. |
| User | Specifies the user name for connecting to the database, which is determined by the database administrator. Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009634741-JSON-Elasticsearch-Schema-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009634781-MongoDB-Database-Properties)
