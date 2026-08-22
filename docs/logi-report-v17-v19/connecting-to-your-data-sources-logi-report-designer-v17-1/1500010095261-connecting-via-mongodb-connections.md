---
title: "Connecting via MongoDB Connections"
id: 1500010095261
section: "Connecting to Your Data Sources - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010095261-Connecting-via-MongoDB-Connections
updated_at: 2021-07-23T19:14:56Z
---

# Connecting via MongoDB Connections

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057862-Connecting-via-SOAP-Web-Service-Connections)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010095281-How-Designer-Gets-Data-from-MongoDB-Databases)

# Connecting via MongoDB Connections

This topic introduces the workflow for Designer to get data from MongoDB database, how you can set up and work with MongoDB connections in a catalog, and use imported APEs via MongoDB connections.

A MongoDB connection contains relational schemas which are transformed from the collections in a MongoDB database. From the transformed relational schemas, you can add tables to the catalog and access the tables in the same way as with [JDBC supplied tables](https://devnet.logianalytics.com/hc/en-us/articles/1500010057682-Using-Tables-Views-Synonyms).

In addition, for users who wish to write their own MongoDB aggregation pipeline expressions (also referred to as APE), Designer enables them to put the expressions into JSON files (.json) and then import the files to a catalog via the specified MongoDB connection. Designer can then load data from the MongoDB database by the expressions in the imported JSON files.

Designer supports MongoDB 1.8 and above.

Select the following links to view the topics:

* [How Designer Gets Data from MongoDB Databases](https://devnet.logianalytics.com/hc/en-us/articles/1500010095281-How-Designer-Gets-Data-from-MongoDB-Databases)
* [Working with MongoDB Connections in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500010057802-Working-with-MongoDB-Connections-in-a-Catalog)
* [Imported APEs](https://devnet.logianalytics.com/hc/en-us/articles/1500010057782-Using-Imported-APEs)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) Logi Report Engine can push down the calculation of the Distinct Count function of an aggregation to MongoDB for speeding up performance when there are a large number of records, as long as it is the only aggregation in a data component and is positioned at the lowest group level.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057862-Connecting-via-SOAP-Web-Service-Connections)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010095281-How-Designer-Gets-Data-from-MongoDB-Databases)
