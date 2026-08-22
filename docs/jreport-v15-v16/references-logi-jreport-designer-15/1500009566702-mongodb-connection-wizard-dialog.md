---
title: "MongoDB Connection Wizard Dialog"
id: 1500009566702
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009566702-MongoDB-Connection-Wizard-Dialog
updated_at: 2021-07-24T05:55:04Z
---

# MongoDB Connection Wizard Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009566662-Merge-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009587861-New-Aggregation-Dialog)

# MongoDB Connection Wizard Dialog

The MongoDB Connection Wizard appears when you select MongoDB and select OK in the [New Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009587961-New-Data-Source-Dialog) dialog, or in the Catalog Manager, right-click a data source and select New MongoDB Connection from the shortcut menu, or right-click an existing MongoDB connection and select Edit Connection from the shortcut menu. It helps you to import [MongoDB collection](https://devnet.logianalytics.com/hc/en-us/articles/1500009585161-MongoDB-Connections) schemas and transform them to relational schemas for future use, and consists of the following screens:

* [MongoDB Connection Information](#Information)
* [Connection Options](#Option)
* [Add Database](#Database)
* [Add Schema](#Schema)
* [Add Table](#Table)

**Back**

Goes back to the previous screen.

**Next**

Goes to the next screen.

**Finish**

Finishes confirming to transform MongoDB schemas to relational schemas.

**Cancel**

Does not retain any changes and closes this wizard.

**Help**

Displays the help document about this feature.

## MongoDB Connection Information

Specifies the necessary information to connect to the MongoDB server. [See the screen](javascript:%20void(null)).

![MongoDB Connection Wizard - MongoDB Connection Information](https://devnet.logianalytics.com/hc/article_attachments/4404893867415/mngodb_infmtn.gif)

**Host**

Specifies the host used to connect to the MongoDB server.

**Port**

Specifies the port number used to connect to the MongoDB server.

**User**

Specifies the user ID used to connect to the MongoDB server.

**Password**

Specifies the password of the user used to connect to the MongoDB server.

## Connection Options

Specifies conditional replica set members and options for the MongoDB connection. [See the screen](javascript:%20void(null)).

![MongoDB Connection Wizard - Connection Options](https://devnet.logianalytics.com/hc/article_attachments/4404889328919/mngodb_optn.gif)

**Replica Set Members**

Lists all the replica set members of the MongoDB connection.

* **Host**  
   Specifies the URI of the replica set members for the MongoDB connection.
* **Port**  
   Specifies the port number of the members.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)  
   Adds a new replica set member.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)  
  Removes the selected replica set member.
* **Options**  
   Specifies the options of the MongoDB server. The options are name=value pairs and the pairs are separated by "&". What you can specify are listed as follows.
  + **slaveOk=true|false**  
     If true, the driver connected to a replica set will send reads to slaves/secondaries, or you can also read a slave/secondary database by adding its URI and port to the Replica Set Members box.
  + **safe=true|false**  
     If true, the driver sends a getLastError command after every update to ensure that the update succeed.
  + **w=n**  
     The driver adds { w : n } to the getLastError command. Implies safe=true.
  + **wtimeoutMS=ms**  
     The driver adds { wtimeout : ms } to the getLastError command. Implies safe=true.
  + **fsync=true|false**  
     If true, the driver adds { fsync : true } to the getLastError command. Implies safe=true.
  + **journal=true|false**  
     If true, sync to journal. Implies safe=true.
  + **connectTimeoutMS=ms**  
     How long a connection can take to be opened before timing out.
  + **socketTimeoutMS=ms**  
     How long a send or receive on a socket can take before timing out.

## Add Database

Adds the databases you can access to the MongoDB connection. This screen will be displayed only when you have no right to access all the databases in the MongoDB data source. [See the screen](javascript:%20void(null)).

![MongoDB Connection Wizard - Add Database](https://devnet.logianalytics.com/hc/article_attachments/4404889329175/mngodb_dtbs.gif)

**Add Database**

Lists the databases you can access in the MongoDB data source.

* **Database Name**   
   Specifies the names of the databases you can access in the MongoDB data source.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)  
   Adds
  a new database you can access.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)  
  Removes the selected database.

## Add Schema

Adds the collection schemas that will be transformed to relational schemas. This screen is not available when you edit an existing MongoDB connection. [See the screen](javascript:%20void(null)).

![MongoDB Connection Wizard - Add Schema](https://devnet.logianalytics.com/hc/article_attachments/4404889329431/mngodb_adschma.gif)

**Schemas**

Lists the schemas in the database for you to select.

**Added Schemas**

Lists the schemas that you have added.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)

Adds the selected schemas.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)

Removes the selected schemas from the Added Schema box.

## Add Table

Adds tables that are transformed from the relational schemas to the connection. This screen is not available when you edit an existing MongoDB connection. [See the screen](javascript:%20void(null)).

![MongoDB Connection Wizard - Add Table](https://devnet.logianalytics.com/hc/article_attachments/4404893867671/mngodb_adtb.gif)

**Tables**

Lists the tables transformed from the MongoDB schemas.

**Added Tables**

Lists the tables that you have added from the relational schemas.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)

Adds the selected tables.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)

Removes the selected tables from the Added Tables box.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009566662-Merge-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009587861-New-Aggregation-Dialog)
