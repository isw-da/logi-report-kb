---
title: "Working with MongoDB Connections in a Catalog"
id: 1500010057802
section: "Connecting to Your Data Sources - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010057802-Working-with-MongoDB-Connections-in-a-Catalog
updated_at: 2021-07-23T19:14:57Z
---

# Working with MongoDB Connections in a Catalog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010095281-How-Designer-Gets-Data-from-MongoDB-Databases)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057782-Using-Imported-APEs)

# Working with MongoDB Connections in a Catalog

A MongoDB connection contains relational schemas which are transformed from the collections in a MongoDB database. This topic describes how you can set up MongoDB connections in a catalog, and add and manage schemas and tables transformed from MongoDB databases in the catalog via the connections.

This topic contains the following sections:

* [Setting Up MongoDB Connections in a Catalog](#Set)
* [Adding More Schemas and Tables to a MongoDB Connection](#Add)
* [Managing the Schemas in a MongoDB Connection](#Schema)
* [Managing the Tables in a MongoDB Connection](#Table)

## Setting Up MongoDB Connections in a Catalog

To connect a catalog to a MongoDB database, you can set up a MongoDB connection as follows:

1. [Create a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500010056622-Creating-Opening-and-Saving-Catalogs) or [open a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500010056622-Creating-Opening-and-Saving-Catalogs#Open), then in the Catalog Manager, right-click the node of a data source and select **New MongoDB Connection** from the shortcut menu.

   If you want to set up the connection in a new data source in the catalog, select any of the existing catalog data sources, select **New Data Source** on the Catalog Manager toolbar, then in the New Data source dialog box, specify the name of the data source, select the **MongoDB** connection type and select **OK**.

   Designer displays the [MongoDB Connection Wizard dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097901-MongoDB-Connection-Wizard-Dialog-Box).

   ![MongoDB Connection Wizard - MongoDB Connection Information](https://devnet.logianalytics.com/hc/article_attachments/4404848510231/mngodb_infmtn.gif)
2. In the **MongoDB Connection Information** screen, specify the necessary information to connect to the MongoDB server.
   * To connect by server host and port, select **Information**, then type the host and port of the MongoDB server, and the user ID and password to connect to the MongoDB server respectively.
   * To connect by URI, select **URI** and type the URI string.
3. Select **Next** to go to the next screen.
4. If you specify to connect to the MongoDB server by host and port, Designer displays the **Connection Options** screen.

   ![MongoDB Connection Wizard - Connection Options](https://devnet.logianalytics.com/hc/article_attachments/4404856909335/mngodb_optn.gif)

   Select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add lines to specify the conditional replica set members for the MongoDB connection. To delete a replica set member, select it and select the **Remove** button ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif).

   In the **Options** box, specify the options of the MongoDB server. The options are *name=value* pairs separated by "&". You can specify the following:

   * **slaveOk=true|false**  
     If true, the driver connected to a replica set sends reads to slaves/secondaries, or you can also read a slave/secondary database by adding its URI and port to the Replica Set Members box.
   * **safe=true|false**  
     If true, the driver sends a getLastError command after every update to ensure that the update succeed.
   * **w=n**  
     The driver adds { w : n } to the getLastError command. Implies safe=true.
   * **wtimeoutMS=ms**  
     The driver adds { wtimeout : ms } to the getLastError command. Implies safe=true.
   * **fsync=true|false**  
     If true, the driver adds { fsync : true } to the getLastError command. Implies safe=true.
   * **journal=true|false**  
     If true, sync to journal. Implies safe=true.
   * **connectTimeoutMS=ms**  
     How long a connection can take to be opened before timing out.
   * **socketTimeoutMS=ms**  
     How long a send or receive on a socket can take before timing out.
   * **authSource=<DataBase name>**  
     The database name associated with the credentials of the user ID if the user ID is specified in the
     MongoDB Connection Information screen.
   * **ssl=true|false**  
     If true, the SSL certificate is imported into the default JKS when you set up the connection via SSL.

     ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) When you create a MongoDB connection via SSL, to make the connection work at runtime, you need to add the *-Djavax.net.ssl.trustStore* parameter in Server's startup file JRServer.bat in `<server_install_root>\server\bin` (the MongoDB Java driver mongo-java-driver-3.12.7.jar is already included in the Logi Report applications), so that the SSL certificate can be loaded into Server.
5. Select **Next** to go to the next screen.
6. If you specify to connect to the MongoDB server by host and port and you do not have the privilege to access all the databases in the MongoDB database, Designer displays the **Add Database** screen. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add lines to specify the databases that you can access in the MongoDB database. To delete a database, select it and select ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif).

   ![MongoDB Connection Wizard - Add Database](https://devnet.logianalytics.com/hc/article_attachments/4404848510487/mngodb_dtbs.gif)
7. Select **Next**.
8. In the **Collection Filter** screen, Designer lists all the available collections in the MongoDB database.

   By default, Designer uses the first ten data records in each collection to parse metadata. If you want to edit the filter condition to get the required collection structure, select a collection in the **Collection** box, and then specify the filter in the text box by typing the part after "$match:", for example, type **{author:"dave"}** in the text box (for more information about the definition of $match, see <https://docs.mongodb.com/manual/reference/operator/aggregation/match/#pipe._S_match>). Select **Apply the Filter to Run Reports** if you want to apply the filter conditions to the reports which use the collections at runtime.

   ![MongoDB Connection Wizard - Collection Filter](https://devnet.logianalytics.com/hc/article_attachments/4404848510743/mngodb_fltr.gif)
9. In the **Add Schema** screen, add the collections you want to transform to relational schemas, in order to use them in the catalog.

   ![MongoDB Connection Wizard - Add Schema](https://devnet.logianalytics.com/hc/article_attachments/4404856909847/mngodb_adschma.gif)
10. Select **Next**.
11. In the **Add Table** screen, add the tables that Designer transforms from the specified schemas to the catalog. A table contains fields mapped to attributes, top level documents, simple elements, array elements, and other nodes in the MongoDB documents.

    ![MongoDB Connection Wizard - Add Table](https://devnet.logianalytics.com/hc/article_attachments/4404856910103/mngodb_adtb.gif)

    You can create [queries](https://devnet.logianalytics.com/hc/en-us/articles/1500010062562-Working-with-Queries) and [business views](https://devnet.logianalytics.com/hc/en-us/articles/1500010101021-Working-with-Business-Views) using these tables and a report is developed from a query (or something else which is functionally similar) or from a business view.
12. Select **Finish** to confirm the transformed result and complete the transformation process.

## Adding More Schemas and Tables to a MongoDB Connection

After you have set up a MongoDB connection in a catalog, you can add more schemas transformed from the collections in the specified MongoDB database and tables in the schemas to the catalog via the MongoDB connection.

**To add more schemas to the catalog via the MongoDB connection:**

1. Right-click the **Schemas** node or an existing schema in the MongoDB connection and select **Add Collection** from the shortcut. Designer displays the [Add Collection dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010057902-Add-Collection-Dialog-Box).

   ![Add Collection dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404857015063/addclctn.gif)
2. In the **Collections** box, select the required collections that you want to transform to relational schemas and select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif) to add them to the **Added Schemas** box.
3. After adding the required schemas, select **OK** to close the dialog box.

**To add more tables to the catalog via the MongoDB connection**:

1. Do one of the following:
   * Right-click the MongoDB connection and select **Add Tables** from the shortcut menu.
   * Right-click the **Tables** node of the MongoDB connection and select **Add Tables** from the shortcut menu.
   * Right-click an existing table in the MongoDB connection and select **Add Tables** from the shortcut menu.

   Designer displays the [Add Table](https://devnet.logianalytics.com/hc/en-us/articles/1500010095521-Add-Tables-Dialog-Box) dialog box.

   ![Add Tables dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848639255/addtbl_mngodb.gif)
2. In the **Tables** box, select the required tables transformed from the relational schemas and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif) to add them to the **Added Tables** box.
3. After adding the required tables, select **OK** to close the dialog box.

## Managing the Schemas in a MongoDB Connection

You can manage the schemas transformed from a MongoDB database via the MongoDB connection you set up in a catalog as follows:

* **Refreshing the schemas**  
  The schemas in your catalog are a temporary cache of metadata to improve performance when you design and test your report. Your database probably changes over the time; however, these changes cannot be reflected automatically in your catalog. To refresh all of the collection schema metadata from the MongoDB database, you can refresh the schema information using the **Refresh** command on the shortcut menu of the schema. When Designer finishes the refreshing job, it displays a reporting dialog box, summarizing the changes and operations that have been taken.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) If you want to add all the deleted or missing databases at one time, you can also refresh the schema, which refreshes all of the collection schema metadata from the MongoDB database.
* **Renaming databases of the schemas**  
  Right-click the database and select **Rename** from the shortcut menu, and then type the required database name in the text box.
  + If the renamed database exists in the MongoDB database, it connects to the new database.
  + If the renamed database does not exist in the MongoDB database, no data is retrieved.
* **Removing databases of the schemas**  
  Right-click the database and select **Delete** from the shortcut menu.

## Managing the Tables in a MongoDB Connection

For the tables that have been transformed from a MongoDB database and added into a catalog via a MongoDB connection, you can [refresh them](https://devnet.logianalytics.com/hc/en-us/articles/1500010057682-Using-Tables-Views-Synonyms#Refresh), [organize them into folders](https://devnet.logianalytics.com/hc/en-us/articles/1500010057682-Using-Tables-Views-Synonyms#Folder), and [remove and add the table columns](https://devnet.logianalytics.com/hc/en-us/articles/1500010057682-Using-Tables-Views-Synonyms#Remove) the same as you do with tables from a JDBC database.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010095281-How-Designer-Gets-Data-from-MongoDB-Databases)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057782-Using-Imported-APEs)
