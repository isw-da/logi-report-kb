---
title: "Accessing Data via MongoDB Connections"
id: 5735564769943
section: "Connecting to Your Data Sources - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735564769943-Accessing-Data-via-MongoDB-Connections
updated_at: 2022-11-02T04:29:05Z
---

# Accessing Data via MongoDB Connections

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735528205847-Accessing-Data-via-SOAP-Web-Service-Connections)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735499559063-How-Designer-Gets-Data-from-MongoDB-Databases)

# Accessing Data via MongoDB Connections

This topic introduces the workflow for Designer to get data from MongoDB databases, how you can set up and work with MongoDB connections in a catalog, and use imported APEs via MongoDB connections.

A MongoDB connection contains relational schemas that are transformed from the collections in a MongoDB database. From the transformed relational schemas, you can add tables to the catalog and access the tables in the same way as with [JDBC supplied tables](https://devnet.logianalytics.com/hc/en-us/articles/5735521508887-Using-Tables-Views-Synonyms).

In addition, for users who wish to write their own MongoDB aggregation pipeline expressions (also referred to as APE), Designer enables them to put the expressions into JSON files (.json) and then import the files to a catalog via the specified MongoDB connection. Designer can then load data from the MongoDB database by the expressions in the imported JSON files.

Designer supports MongoDB 1.8 and later.

Select the following links to view the topics:

* [How Designer Gets Data from MongoDB Databases](https://devnet.logianalytics.com/hc/en-us/articles/5735499559063-How-Designer-Gets-Data-from-MongoDB-Databases)
* [Working with MongoDB Connections in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/5735507864599-Working-with-MongoDB-Connections-in-a-Catalog)
* [Imported APEs](https://devnet.logianalytics.com/hc/en-us/articles/5735512889367-Using-Imported-APEs)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)Logi Report Engine can push down the calculation of the Distinct Count function of an aggregation to MongoDB for speeding up performance when there are a large number of records, as long as it is the only aggregation in a data component and is positioned at the lowest group level.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735528205847-Accessing-Data-via-SOAP-Web-Service-Connections)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735499559063-How-Designer-Gets-Data-from-MongoDB-Databases)
