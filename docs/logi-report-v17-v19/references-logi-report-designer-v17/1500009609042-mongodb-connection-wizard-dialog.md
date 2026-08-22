---
title: "MongoDB Connection Wizard Dialog"
id: 1500009609042
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009609042-MongoDB-Connection-Wizard-Dialog
updated_at: 2021-07-24T16:04:23Z
---

# MongoDB Connection Wizard Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009609022-Merge-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009632561-New-Aggregation-Dialog)

# MongoDB Connection Wizard Dialog

The MongoDB Connection Wizard helps you to [set up a MongoDB connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009629621-Working-with-MongoDB-Connections-in-a-Catalog#Set)  to get data from a MongoDB database. It appears when you select MongoDB and select OK in the [New Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009609222-New-Data-Source-Dialog) dialog, or in the Catalog Manager, right-click a data source and select New MongoDB Connection from the shortcut menu, or right-click an existing MongoDB connection and select Edit Connection from the shortcut menu.

The wizard contains the following screens:

* [MongoDB Connection Information](#Information)
* [Connection Options](#Option)
* [Add Database](#Database)
* [Collection Filter](#Filter)
* [Add Schema](#Schema)
* [Add Table](#Table)

**Back**

Goes back to the previous screen.

**Next**

Goes to the next screen.

**Finish**

Finishes confirming to transform MongoDB collections to relational schemas.

**Cancel**

Does not retain any changes and closes this wizard.

**Help**

Displays the help document about this feature.

## MongoDB Connection Information

Specifies in which way to connect to the MongoDB server. The connecting way cannot be changed when editing an existing MongoDB connection.

![MongoDB Connection Wizard - MongoDB Connection Information](https://devnet.logianalytics.com/hc/article_attachments/4404904253975/mngodb_infmtn.gif)

**Information**

Connects to the MongoDB server by host and port.

* **Host**  
   Specifies the host used to connect to the MongoDB server.
* **Port**  
   Specifies the port number used to connect to the MongoDB server.
* **User**  
   Specifies the user ID used to connect to the MongoDB server.
* **Password**  
   Specifies the password of the user used to connect to the MongoDB server.

**URI**

Connects to the MongoDB server by URI.

## Connection Options

Specifies conditional replica set members and options for the MongoDB connection. This screen is available when you have specified to connect to the MongoDB server by host and port.

![MongoDB Connection Wizard - Connection Options](https://devnet.logianalytics.com/hc/article_attachments/4404904254231/mngodb_optn.gif)

**Replica Set Members**

Lists all the replica set members of the MongoDB connection.

* **Host**  
   Specifies the URI of the replica set members for the MongoDB connection.
* **Port**  
   Specifies the port number of the members.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif)  
   Adds a new replica set member.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif)  
  Removes the selected replica set member.
* **Options**  
   Specifies the options of the MongoDB server.

## Add Database

Adds the databases you can access to the MongoDB connection. This screen is displayed when you have specified to connect to the MongoDB server by host and port but you do not have the privilege to access all the databases in the MongoDB data source.

![MongoDB Connection Wizard - Add Database](https://devnet.logianalytics.com/hc/article_attachments/4404904254487/mngodb_dtbs.gif)

**Add Database**

Lists the databases you can access in the MongoDB data source.

* **Database Name**   
   Specifies the names of the databases you can access in the MongoDB data source.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif)  
   Adds a new database you can access.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif)  
  Removes the selected database.

## Collection Filter

Specifies filter condition for the collections in the MongoDB database.

![MongoDB Connection Wizard - Collection Filter](https://devnet.logianalytics.com/hc/article_attachments/4404904254871/mngodb_fltr.gif)

**Collections**

Lists all available collections in the MongoDB database.

**Filter**

Specifies the filter condition for each collection to get the required collection structure, otherwise the first ten data records will be used to parse metadata.

* **$match**  
   Filters the documents to pass only the documents that match the specified conditions to the next pipeline stage. For the definition of $match, refer to <https://docs.mongodb.com/manual/reference/operator/aggregation/match/#pipe._S_match>.

**Apply the Filter to Run Reports**

Specifies whether to apply the filter conditions to reports created based on the collections at runtime.

## Add Schema

Adds the collections you want to transform to relational schemas. This screen is not available when you edit an existing MongoDB connection.

![MongoDB Connection Wizard - Add Schema](https://devnet.logianalytics.com/hc/article_attachments/4404904255127/mngodb_adschma.gif)

**Collections**

Lists the collections in the database for you to select.

**Added Schemas**

Lists the schemas transformed from the selected collections.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif)

Adds the selected collections you want to transform to relational schemas.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)

Removes the selected schemas from the Added Schema box.

## Add Table

Adds tables that are transformed from the relational schemas to the connection. This screen is not available when you edit an existing MongoDB connection.

![MongoDB Connection Wizard - Add Table](https://devnet.logianalytics.com/hc/article_attachments/4404916782359/mngodb_adtb.gif)

**Tables**

Lists the tables transformed from the relational schemas.

**Added Tables**

Lists the tables that you have added.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif)

Adds the selected tables.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)

Removes the selected tables from the Added Tables box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009609022-Merge-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009632561-New-Aggregation-Dialog)
