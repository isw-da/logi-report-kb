---
title: "MongoDB Connections"
id: 1500009629601
section: "Connecting to Your Data Sources - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009629601-MongoDB-Connections
updated_at: 2021-07-24T16:05:06Z
---

# MongoDB Connections

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009629701-SOAP-Web-Service-Connections) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009606962-How-Logi-Report-Gets-Data-from-MongoDB-Databases)

# MongoDB Connections

You can set up MongoDB connections in Logi Report catalogs to get data from MongoDB databases. A MongoDB connection contains relational schemas which are transformed from the collections in a MongoDB database. From the transformed relational schemas, you can add tables to the Logi Report catalog, and the tables can then be accessed in the same way as [JDBC supplied tables](https://devnet.logianalytics.com/hc/en-us/articles/1500009629561-Tables-Views-Synonyms).

In addition, for users who wish to write their own MongoDB aggregation pipeline expressions (also referred to as APE), Logi Report Enables them to put the expressions into JSON files (.json) and then import the files to a catalog via the specified MongoDB connection. Logi Report can then load data from the MongoDB database by the expressions in the imported JSON files.

Logi Report Designer supports MongoDB 1.8 and above.

Select the following links to view the topics:

* [How Logi Report Gets Data from MongoDB Databases](https://devnet.logianalytics.com/hc/en-us/articles/1500009606962-How-Logi-Report-Gets-Data-from-MongoDB-Databases)
* [Working with MongoDB Connections in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009629621-Working-with-MongoDB-Connections-in-a-Catalog)
* [Imported APEs](https://devnet.logianalytics.com/hc/en-us/articles/1500009606942-Imported-APEs)

**![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404911621015/___newv17.jpg "New for version 17.")Note:** Logi Report can push down the calculation of the Distinct Count function of an aggregation to MongoDB for speeding up performance when there are a large number of records, as long as it is the only aggregation in a data component and is positioned at the lowest group level.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009629701-SOAP-Web-Service-Connections) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009606962-How-Logi-Report-Gets-Data-from-MongoDB-Databases)
