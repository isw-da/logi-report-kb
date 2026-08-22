---
title: "Working with MongoDB Connections in a Catalog"
id: 1500010029522
section: "Connecting to Your Data Sources - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010029522-Working-with-MongoDB-Connections-in-a-Catalog
updated_at: 2021-07-24T10:39:13Z
---

# Working with MongoDB Connections in a Catalog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010064461-How-Logi-JReport-Gets-Data-from-MongoDB-Databases) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010064441-Imported-APEs)

# Working with MongoDB Connections in a Catalog

You can set up MongoDB connections in Logi JReport catalogs to get data from MongoDB databases. A MongoDB connection contains relational schemas which are transformed from the collections in a MongoDB database. From the transformed relational schemas, you can add tables to the Logi JReport catalog.

Below is a list of the sections covered in this topic:

* [Setting Up MongoDB Connections in a Catalog](#Set)
* [Adding More Schemas and Tables to a MongoDB Connection](#Add)
* [Managing the Schemas in a MongoDB Connection](#Schema)
* [Managing the Tables in a MongoDB Connection](#Table)

## Setting Up MongoDB Connections in a Catalog

To connect a Logi JReport catalog to a MongoDB database, you can set up a MongoDB connection as follows:

1. [Create a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500010063141-Creating-Opening-and-Saving-Catalogs) or [open a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500010063141-Creating-Opening-and-Saving-Catalogs#Open), then in the Catalog Manager, right-click the node of a data source and select **New MongoDB Connection** from the shortcut menu.

   If you want to set up the connection in a new data source in the catalog, select any of the existing catalog data sources, select **New Data Source** on the Catalog Manager toolbar, then in the New Data source dialog, specify the name of the data source, select the **MongoDB** connection type and select **OK**.

   The [MongoDB Connection Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500010031662-MongoDB-Connection-Wizard-Dialog) appears.

   ![MongoDB Connection Wizard - MongoDB Connection Information](https://devnet.logianalytics.com/hc/article_attachments/4404901196951/mngodb_infmtn.gif)
2. In the MongoDB Connection Information screen, specify the necessary information to connect to the MongoDB server.
   * To connect by server host and port, check **Information**, then type in the host and port of the MongoDB server, and the user ID and password to connect to the MongoDB server respectively.
   * To connect by URI, check **URI** and enter the URI string.
3. Select **Next** to go to the next screen.
4. If you specified to connect to the MongoDB server by host and port, the Connection Options screen is displayed.

   ![MongoDB Connection Wizard - Connection Options](https://devnet.logianalytics.com/hc/article_attachments/4404909169303/mngodb_optn.gif)

   Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif) to add lines to specify the conditional replica set members for the MongoDB connection. To remove a replica set member, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif).

   In the Options box, specify the options of the MongoDB server. The options are *name=value* pairs separated by "&". You can specify the following:

   * **slaveOk=true|false**  
      If true, the driver connected to a replica set will send reads to slaves/secondaries, or you can also read a slave/secondary database by adding its URI and port to the Replica Set Members box.
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
      If true, the SSL certificate will be imported into the default JKS when setting up the connection via SSL.

     **Note:** When a MongoDB connection is set up via SSL, to make the connection work at runtime, you need to add the *-Djavax.net.ssl.trustStore* parameter in Logi JReport Server's startup file JRServer.bat in `<server_install_root>\server\bin` (the MongoDB Java driver mongo-java-driver-3.4.0.jar is already within Logi JReport), so that the SSL certificate can be loaded into Logi JReport Server.
5. Select **Next** to go to the next screen.
6. If you specified to connect to the MongoDB server by host and port but you do not have the privilege to access all the databases in the MongoDB database, the Add Database screen is displayed. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif) to add lines to specify the databases you can access in the MongoDB database. To remove a database, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif). Select **Next**.

   ![MongoDB Connection Wizard - Add Database](https://devnet.logianalytics.com/hc/article_attachments/4404909169559/mngodb_dtbs.gif)
7. In the Collection Filter screen, all available collections in the MongoDB database are listed. By default, Logi JReport will use the first ten data records in each collection to parse metadata. If you want to edit the filter condition to get the required collection structure, select a collection in the Collection box, and then specify the filter in the text box by typing the part after "$match:", for example, input **{author:"dave"}** in the text box (for the definition of $match, refer to <https://docs.mongodb.com/manual/reference/operator/aggregation/match/#pipe._S_match>). Check **Apply the Filter to Run Reports** if you want to apply the filter conditions to reports created based on the collections at runtime.

   ![MongoDB Connection Wizard - Collection Filter](https://devnet.logianalytics.com/hc/article_attachments/4404901197207/mngodb_fltr.gif)
8. In the Add Schema screen, add the collections you want to transform to relational schemas so as to use in the Logi JReport catalog. Select **Next**.

   ![MongoDB Connection Wizard - Add Schema](https://devnet.logianalytics.com/hc/article_attachments/4404909169815/mngodb_adschma.gif)
9. In the Add Table screen, add the tables transformed from the specified schemas to the Logi JReport catalog. A table contains fields mapped to attributes, top level documents, simple elements, array elements and other nodes in the MongoDB documents.

   ![MongoDB Connection Wizard - Add Table](https://devnet.logianalytics.com/hc/article_attachments/4404909170071/mngodb_adtb.gif)

   [Queries](https://devnet.logianalytics.com/hc/en-us/articles/1500010070681-Queries) and [business views](https://devnet.logianalytics.com/hc/en-us/articles/1500010070641-Business-Views) can be created based on these tables and a report is developed from a query (or something else which is functionally similar) or from a business view.
10. Select **Finish** to confirm the transformed result and complete the transformation process.

## Adding More Schemas and Tables to a MongoDB Connection

When a MongoDB connection is set up, you can add more schemas transformed from the collections in the specified MongoDB database and tables in the schemas to the Logi JReport catalog  via the MongoDB connection.

**To add more schemas to the catalog via the MongoDB connection:**

1. Right-click the **Schemas** node or an existing schema in the MongoDB connection and select **Add Collection**  from the shortcut. The [Add Collection](https://devnet.logianalytics.com/hc/en-us/articles/1500010029602-Add-Collection-Dialog) dialog appears.

   ![Add Collection dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909256471/addclctn.gif)
2. Select the required collections that you want to transform to relational schemas in the Collections box and then select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif) to add them to the Added Schemas box.
3. After adding the required schemas, select **OK** to close the dialog.

**To add more tables to the catalog via the MongoDB connection**:

1. Do either of the following:
   * Right-click the MongoDB connection and select **Add Tables** from the shortcut menu.
   * Right-click the **Tables** node of the MongoDB connection and select **Add Tables**from the shortcut menu.
   * Right-click an existing table in the MongoDB connection and select **Add Tables**from the shortcut menu.

   The [Add Table](https://devnet.logianalytics.com/hc/en-us/articles/1500010029762-Add-Tables-Dialog) dialog appears.

   ![Add Tables dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901297815/addtbl_mngodb.gif)
2. Select the required tables that are transformed from the relational schemas in the Tables box and then select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif) to add them to the Added Tables box.
3. After adding the required tables, select **OK** to close the dialog.

## Managing the Schemas in a MongoDB Connection

You can manage the schemas transformed from a MongoDB database via the MongoDB connection you set up in a Logi JReport catalog as follows:

* **Refreshing the schemas**  
   The schemas in your catalog are a temporary cache of metadata to improve performance when you design and test your report. Your database will probably change over the time; however these changes will not be reflected automatically in your catalog. To refresh all of the collection schema metadata from the MongoDB database, you can refresh the schema information using the Refresh command on the shortcut menu of the schema. When the refreshing job is done, a reporting dialog will be shown, summarizing the changes and operations that have been taken.

  **Tip:** If you want to add all the deleted or missing databases at one time, you can also refresh the schema, which refreshes all of the collection schema metadata from the MongoDB database.
* **Renaming databases of the schemas**  
   Right-click the database and select **Rename** from the shortcut menu, and then input the required database name in the text box.
  + If the renamed database exists in the MongoDB database, it will connect to the new database.
  + If the renamed database does not exist in the MongoDB database, no data will be retrieved.
* **Removing databases of the schemas**  
   Right-click the database and select **Delete** from the shortcut menu.

## Managing the Tables in a MongoDB Connection

When the tables transformed from a MongoDB database have been added into the Logi JReport catalog via the specified MongoDB connection, you can [refresh them](https://devnet.logianalytics.com/hc/en-us/articles/1500010064361-Tables-Views-Synonyms#Refresh), [organize them into folders](https://devnet.logianalytics.com/hc/en-us/articles/1500010064361-Tables-Views-Synonyms#Folder), and [remove and add the table columns](https://devnet.logianalytics.com/hc/en-us/articles/1500010064361-Tables-Views-Synonyms#Remove) the same as you do on tables from a JDBC database.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010064461-How-Logi-JReport-Gets-Data-from-MongoDB-Databases) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010064441-Imported-APEs)
