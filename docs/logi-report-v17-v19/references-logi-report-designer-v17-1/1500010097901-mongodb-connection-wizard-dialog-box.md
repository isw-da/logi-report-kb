---
title: "MongoDB Connection Wizard Dialog Box"
id: 1500010097901
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010097901-MongoDB-Connection-Wizard-Dialog-Box
updated_at: 2021-07-23T19:15:44Z
---

# MongoDB Connection Wizard Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010059742-Merge-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010059902-New-Aggregation-Dialog-Box)

# MongoDB Connection Wizard Dialog Box

You can use the MongoDB Connection Wizard dialog box to [set up or edit a MongoDB connection in a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500010057802-Working-with-MongoDB-Connections-in-a-Catalog#Set) in order to get data from a MongoDB database. This topic describes the options in the dialog box.

Designer displays the MongoDB Connection Wizard dialog box when you select MongoDB and select OK in the [New Data Source dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059982-New-Data-Source-Dialog-Box), or in the Catalog Manager, right-click a data source and select New MongoDB Connection from the shortcut menu, or right-click an existing MongoDB connection and select Edit Connection from the shortcut menu.

The dialog box contains the following screens:

* [MongoDB Connection Information Screen](#Information)
* [Connection Options Screen](#Option)
* [Add Database Screen](#Database)
* [Collection Filter Screen](#Filter)
* [Add Schema Screen](#Schema)
* [Add Table Screen](#Table)

You see these buttons in all the screens:

**Back**

Select to go back to the previous screen.

**Next**

Select to go to the next screen.

**Finish**

Select to finish transforming the MongoDB collections to relational schemas.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## MongoDB Connection Information Screen

Use this screen to specify in which way to connect to the MongoDB server. You cannot change the connecting way when you use the dialog box for editing an existing MongoDB connection.

![MongoDB Connection Wizard - MongoDB Connection Information](https://devnet.logianalytics.com/hc/article_attachments/4404848510231/mngodb_infmtn.gif)

**Information**

Select to connect to the MongoDB server by host and port.

* **Host**  
  Specify the host for connecting to the MongoDB server.
* **Port**  
  Specify the port number for connecting to the MongoDB server.
* **User**  
  Specify the user ID for connecting to the MongoDB server.
* **Password**  
  Specify the password of the user for connecting to the MongoDB server.

**URI**

Select to connect to the MongoDB server by the specified URI.

## Connection Options Screen

Designer displays the Connection Options screen when you specify to connect to the MongoDB server by host and port.
You can use it to specify the conditional replica set members and options for the MongoDB connection.

![MongoDB Connection Wizard - Connection Options](https://devnet.logianalytics.com/hc/article_attachments/4404856909335/mngodb_optn.gif)

**Replica Set Members**

The box lists all the replica set members of the MongoDB connection.

* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**  
  Select to add a new replica set member.
* ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**  
  Select to delete the specified replica set member.
* **Host**  
  The column shows the URIs that you specify for the replica set members.
* **Port**  
  The column shows the port numbers that you specify for the replica set members.

**Options**

You can specify the options of the MongoDB server in the box, which are *name=value* pairs separated by "&".

## Add Database Screen

Designer displays the Add Database screen if you specify to connect to the MongoDB server by host and port and you do not have the privilege to access all the databases in the MongoDB database. You can use it to add the databases that you can access to the MongoDB connection.

![MongoDB Connection Wizard - Add Database](https://devnet.logianalytics.com/hc/article_attachments/4404848510487/mngodb_dtbs.gif)

**Add Database**

The box lists the databases that you add to the MongoDB connection.

* **Database Name**   
  Specify the names of the databases that you can access in the MongoDB database.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**  
  Select to add a new database that you can access to the MongoDB connection.
* ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**  
  Select to delete the selected database.

## Collection Filter Screen

Use it to specify the filter condition for the collections in the MongoDB database.

![MongoDB Connection Wizard - Collection Filter](https://devnet.logianalytics.com/hc/article_attachments/4404848510743/mngodb_fltr.gif)

**Collections**

The box lists all the available collections in the MongoDB database.

**Filter**

Specify the filter condition for each collection to get the required collection structure; otherwise, Designer applies the first ten data records to parse metadata.

* **$match**  
  Specify to filter the documents to pass only the documents that match the specified conditions to the next pipeline stage. For the definition of $match, see <https://docs.mongodb.com/manual/reference/operator/aggregation/match/#pipe._S_match>.

**Apply the Filter to Run Reports**

Select to apply the filter conditions to the reports which use the collections at runtime.

## Add Schema Screen

Use this screen to add the collections that you want to transform to relational schemas. Designer does not display this screen when you use the dialog box for editing an existing MongoDB connection.

![MongoDB Connection Wizard - Add Schema](https://devnet.logianalytics.com/hc/article_attachments/4404856909847/mngodb_adschma.gif)

**Collections**

The box lists the collections in the MongoDB database for you to select.

**Added Schemas**

The box lists the schemas that Designer transforms from the selected collections.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add button**

Select to add the specified collections which you want to transform to relational schemas.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)**Remove button**

Select to remove the specified schemas from the Added Schemas box.

## Add Table Screen

Use this screen to add tables that Designer transforms from the relational schemas to the MongoDB connection. Designer does not display this screen when you use the dialog box for editing an existing MongoDB connection.

![MongoDB Connection Wizard - Add Table](https://devnet.logianalytics.com/hc/article_attachments/4404856910103/mngodb_adtb.gif)

**Tables**

The box lists the tables that Designer transforms from the relational schemas.

**Added Tables**

The box lists the tables that you select to add to the MongoDB connection.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add button**

Select to add the specified tables to the MongoDB connection.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)**Remove button**

Select to remove the specified tables from the Added Tables box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010059742-Merge-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010059902-New-Aggregation-Dialog-Box)
