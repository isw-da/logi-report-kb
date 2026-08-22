---
title: "MongoDB Connection Wizard Dialog Box"
id: 5735551938071
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735551938071-MongoDB-Connection-Wizard-Dialog-Box
updated_at: 2022-11-02T04:39:44Z
---

# MongoDB Connection Wizard Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735543595799-Merge-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735514877719-New-Aggregation-Dialog-Box)

# MongoDB Connection Wizard Dialog Box

You can use the MongoDB Connection Wizard dialog box to [set up or edit a MongoDB connection in a catalog](https://devnet.logianalytics.com/hc/en-us/articles/5735507864599-Working-with-MongoDB-Connections-in-a-Catalog#Set) to get data from a MongoDB database. This topic describes the options in the dialog box.

Designer displays the MongoDB Connection Wizard dialog box when you select MongoDB and select OK in the [New Data Source dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735530467735-New-Data-Source-Dialog-Box); or in the Catalog Manager, right-click a data source and select New MongoDB Connection from the shortcut menu, or right-click an existing MongoDB connection and select Edit Connection from the shortcut menu.

The dialog box contains the following screens:

* [MongoDB Connection Information Screen](#Information)
* [Connection Options Screen](#Option)
* [Collection Filter Screen](#Filter)
* [Add Schema Screen](#Schema)
* [Add Table Screen](#Table)

Designer displays these buttons in all the screens:

**Back**

Select to go back to the previous screen.

**Next**

Select to go to the next screen.

**Finish**

Select to finish your work and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## MongoDB Connection Information Screen

Use this screen to specify the information to connect to the MongoDB server. You cannot change the connecting way when you use the dialog box for editing an existing MongoDB connection.

![MongoDB Connection Wizard - MongoDB Connection Information](https://devnet.logianalytics.com/hc/article_attachments/9898461654551/mngodb_infmtn.gif)

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

**Parameter**

Select to open the [New Parameter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552101271-New-Parameter-Dialog-Box) to create a parameter in the current catalog data source. You can then reference the parameter to dynamically specify the host, user ID, password, or URI.

## Connection Options Screen

Designer displays the Connection Options screen when you specify to connect to the MongoDB server by host and port.
You can use it to specify the conditional replica set members and options for the MongoDB connection.

![MongoDB Connection Wizard - Connection Options](https://devnet.logianalytics.com/hc/article_attachments/9898478741015/mngodb_optn.gif)

**Replica Set Members**

This box lists all the replica set members of the MongoDB connection.

* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif)**Add button**  
  Select to add a new replica set member.
* ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif)**Remove button**  
  Select to delete the specified replica set member.
* **Host**  
  This column shows the URIs that you specify for the replica set members.
* **Port**  
  This column shows the port numbers that you specify for the replica set members.

**Options**

You can specify the MongoDB server options in this box, which are *name=value* pairs separated by "&".

## Collection Filter Screen

Use this screen to specify filter condition for the collections in the MongoDB database.

![MongoDB Connection Wizard - Collection Filter](https://devnet.logianalytics.com/hc/article_attachments/9898478744983/mngodb_fltr.gif)

**Collections**

This box lists all available collections in the MongoDB database.

**Filter**

Specify the filter condition for each collection to get the required collection structure; otherwise, Designer applies the first ten records to parse metadata.

* **$match**  
  Specify to filter the documents to pass only the documents that match the specified conditions to the next pipeline stage. For the definition of $match, see <https://docs.mongodb.com/manual/reference/operator/aggregation/match/#pipe._S_match>.

**Apply the Filter to Run Reports**

Select to apply the filter conditions to the reports that use the collections at runtime.

## Add Schema Screen

Use this screen to add the collections that you want to transform to relational schemas. Designer does not display this screen when you use the dialog box for editing an existing MongoDB connection.

![MongoDB Connection Wizard - Add Schema](https://devnet.logianalytics.com/hc/article_attachments/9898461682839/mngodb_adschma.gif)

**Collections**

This box lists the collections in the MongoDB database.

**Added Schemas**

This box lists the schemas that Designer transforms from the selected collections.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif)**Add button**

Select to add the specified collections in the Collections box to transform them to relational schemas.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/9898422552599/btn_rmvarrow.gif)**Remove button**

Select to remove the specified schemas from the Added Schemas box.

## Add Table Screen

Use this screen to add tables that Designer transforms from the MongoDB database to the connection. Designer does not display this screen when you use the dialog box for editing an existing MongoDB connection.

![MongoDB Connection Wizard - Add Table](https://devnet.logianalytics.com/hc/article_attachments/9898461696535/mngodb_adtb.gif)

**Tables**

This box lists the tables that Designer transforms from the MongoDB database.

**Added Tables**

This box lists the tables that you add to use in the MongoDB connection.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif)**Add button**

Select to add the specified tables in the Tables box to the MongoDB connection.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/9898422552599/btn_rmvarrow.gif)**Remove button**

Select to remove the specified tables from the Added Tables box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735543595799-Merge-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735514877719-New-Aggregation-Dialog-Box)
