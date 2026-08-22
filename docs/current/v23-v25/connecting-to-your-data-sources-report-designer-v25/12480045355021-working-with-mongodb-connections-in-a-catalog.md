---
title: "Working with MongoDB Connections in a Catalog"
id: 12480045355021
section: "Connecting to Your Data Sources - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480045355021-Working-with-MongoDB-Connections-in-a-Catalog
updated_at: 2026-02-25T23:50:13Z
source_host: docs-report.zendesk.com
---
# 
Working with MongoDB Connections in a Catalog

A MongoDB connection contains relational schemas that are transformed from the collections in a MongoDB database. This topic describes how you can set up MongoDB connections in a catalog, and add and manage the schemas and tables transformed from MongoDB databases in the catalog via the connections.

This topic contains the following sections:

- Setting Up MongoDB Connections in a Catalog

- Adding More Schemas and Tables to a MongoDB Connection

- 
Managing Schemas in a MongoDB Connection
- Refreshing Schemas

- Renaming Databases of Schemas

- Removing Databases of Schemas

- Managing Tables in a MongoDB Connection

## 
Setting Up MongoDB Connections in a Catalog

To set up a MongoDB connection to connect a catalog to a MongoDB database, take the following steps:

- 
Create a catalog or open a catalog

- In the Catalog Manager, do either of the following:
- To set up the connection in an existing data source in the catalog, right-click the data source node and select New MongoDB Connection from the shortcut menu.

- To set up the connection in a new data source in the catalog, select any of the existing catalog data sources, select New Data Source on the Catalog Manager toolbar, then in the New Data source dialog box, specify the name of the data source, select the MongoDB connection type and select OK.

Designer displays the MongoDB Connection Wizard dialog box.

- In the MongoDB Connection Information screen, specify the information to connect to the MongoDB server.
    
- To connect by server host and port, select Information, then type the host and port of the MongoDB server, and the user ID and password to connect to the MongoDB server respectively. 

- To connect by URI, select URI and type the URI string. If a URI string contains characters, such as "@", ":", "?", and "&", or other strings that do not need to be parsed, you should quote them with double quotation marks.

You can reference a parameter or constant level formula in the current catalog data source in the format @FieldName, or the User Name special field as @username when specifying the user ID and password, and use a combination of the three when specifying the host or URI string, to dynamically specify the information to connect to the MongoDB database.  Select New Parameter to create the parameter  and reference it if the predefined parameters cannot meet your requirement.

- Select Next. If you specify to connect to the MongoDB server by host and port, Designer displays the Connection Options screen.
    

- Select Add to add lines to specify the conditional replica set members for the MongoDB connection. To delete a replica set member, select it and select Remove.

- 
In the Options box, specify the options of the MongoDB server. The options are name=value pairs separated by "&". You can specify the following:
- 
slaveOk=true|false
If true, the driver connected to a replica set sends reads to slaves/secondaries, or you can also read a slave/secondary database by adding its URI and port to the Replica Set Members box.

- 
safe=true|false
If true, the driver sends a getLastError command after every update to ensure that the update succeeds.

- 
w=n
The driver adds { w : n } to the getLastError command. Implies safe=true.

- 
wtimeoutMS=ms
The driver adds { wtimeout : ms } to the getLastError command. Implies safe=true.

- 
fsync=true|false
If true, the driver adds { fsync : true } to the getLastError command. Implies safe=true.

- 
journal=true|false
If true, sync to journal. Implies safe=true.

- 
connectTimeoutMS=ms
How long a connection can take to be opened before timing out.

- 
socketTimeoutMS=ms
How long a send or receive on a socket can take before timing out.

- 
authSource=<DataBase name>
The database name associated with the credentials of the user ID if the user ID is specified in the 
MongoDB Connection Information screen.

- 
ssl=true|false
If true, the SSL certificate is imported into the default JKS when you set up the connection via SSL.
         When you create a MongoDB connection via SSL, to make the connection work at runtime, you need to add the -Djavax.net.ssl.trustStore option in the startup file of Server, JRServer.bat, in <server_install_root>\server\bin, so that the SSL certificate can be loaded into Server.

- Select Next. Designer displays the Collection Filter screen. 

- The Collection box displays all available collections in the MongoDB database. Designer uses the first ten records in each collection to parse metadata by default. If you want to edit the filter condition to get the required collection structure, select a collection in the Collection box, and then specify the filter in the text box by typing the part after "$match:", for example, type {author:"dave"} in the text box. For more information about the definition of $match, go to docs.mongodb.com/manual/reference/operator/aggregation/match/#pipe._S_match. Select Apply the Filter to Run Reports to apply the filter conditions to reports that use the collections at runtime.

- Select Next. Designer displays the Add Schema screen. 

- In the Collections box, select the collections you want to transform to relational schemas  and select Add to add them to the Added Schemas box.

- Select Next. Designer displays the Add Table screen. 

- The Tables box lists the tables Designer transforms from the specified schemas. A table contains fields mapped to attributes, top level documents, simple elements, array elements, and other nodes in the MongoDB documents. Select the tables you want to use in the connection and select Add to add them to the Added Tables box. You can create queries and business views using these tables and then develop reports based on the queries and business views. 

- Select Finish to complete the transformation process.

## 
Adding More Schemas and Tables to a MongoDB Connection

After you have set up a MongoDB connection in a catalog, you can add more schemas transformed from the collections in the specified MongoDB database and tables in the schemas to the catalog via the connection.

To add schemas to a MongoDB connection

- Right-click the Schemas node or an existing schema in the MongoDB connection and select Add Collection from the shortcut. Designer displays the Add Collection dialog box.
    

- In the Collections box, select the collections that you want to transform to relational schemas and select Add to add them to the Added Schemas box. 

- Select OK to finish adding the schemas and close the dialog box.

To add tables to a MongoDB connection

- Do one of the following:
    
- Right-click the MongoDB connection and select Add Tables from the shortcut menu.

- Right-click the Tables node of the MongoDB connection and select Add Tables from the shortcut menu.

- Right-click an existing table in the MongoDB connection and select Add Tables from the shortcut menu.

Designer displays the Add Table dialog box.

- In the Tables box, select the required tables  transformed from the relational schemas  and select Add to add them to the Added Tables box.

- Select OK to finish adding the tables and close the dialog box.

## 
Managing Schemas in a MongoDB Connection

You can manage the schemas transformed from a MongoDB database via the MongoDB connection you set up in a catalog.

### 
Refreshing Schemas

The schemas in your catalog are a temporary cache of metadata to improve performance when you design and test your report. Your database probably changes over the time, but these changes cannot be reflected automatically in your catalog. To refresh all collection schema metadata from the MongoDB database, you can refresh the schema information using the Refresh command on the shortcut menu of the schema. When Designer finishes the refreshing job, it displays a dialog box, summarizing the changes and operations that have been taken.
    

 If you want to add all the deleted or missing databases at one time, you can also refresh the schema, which refreshes all of the collection schema metadata from the MongoDB database.

### 
Renaming Databases of Schemas

- Right-click the database and select Rename from the shortcut menu.

- Type the new database name in the text box, then,            
- If the renamed database exists in the MongoDB database, Designer connects  to the new database.

- If the renamed database does not exist in the MongoDB database, no data is retrieved.

### 
Removing Databases of Schemas

To remove a database, right-click the database and select Delete on the shortcut menu.

## 
Managing Tables in a MongoDB Connection

For the tables you have transformed from a MongoDB database and added into a catalog via a MongoDB connection, you can refresh them, organize them into folders, and remove and add the table columns the same as you do with tables from a JDBC database.
