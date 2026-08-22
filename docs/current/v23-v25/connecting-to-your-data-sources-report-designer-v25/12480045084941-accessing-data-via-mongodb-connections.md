---
title: "Accessing Data via MongoDB Connections"
id: 12480045084941
section: "Connecting to Your Data Sources - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480045084941-Accessing-Data-via-MongoDB-Connections
updated_at: 2026-02-25T23:50:14Z
source_host: docs-report.zendesk.com
---
# Accessing Data via MongoDB Connections

 This topic introduces the workflow for Designer to get data from MongoDB databases, how you can set up and work with MongoDB connections in a catalog, and use imported APEs via MongoDB connections.

A MongoDB connection contains relational schemas that are transformed from the collections in a MongoDB database. From the transformed relational schemas, you can add tables to the catalog and access the tables  in the same way as with JDBC supplied tables.

In addition, for users who wish to write their own MongoDB aggregation pipeline expressions (also referred to as APE), Designer enables them to put the expressions into JSON files (.json) and then import the files to a catalog via the specified MongoDB connection. Designer can then load data from the MongoDB database by the expressions in the imported JSON files.  

Designer supports MongoDB 1.8 and later.

Select the following links to view the topics:

- How Designer Gets Data from MongoDB Databases

- Working with MongoDB Connections in a Catalog

- Imported APEs

Report Engine can push down the calculation of the Distinct Count function of an aggregation to MongoDB for speeding up performance when there are a large number of records, as long as it is the only aggregation in a data component and is positioned at the lowest group level.
