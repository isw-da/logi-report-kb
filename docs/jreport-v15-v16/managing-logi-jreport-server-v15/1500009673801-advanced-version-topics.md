---
title: "Advanced Version Topics"
id: 1500009673801
section: "Managing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009673801-Advanced-Version-Topics
updated_at: 2021-07-24T20:54:00Z
---

# Advanced Version Topics

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673761-Deleting-Versions)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673681-Managing-Tasks)

# Advanced Version Topics

This topic introduces advanced version topics for administrators. It will give you an understanding of version structure in depth. Developers can also [use API to manage the resource versions](https://devnet.logianalytics.com/hc/en-us/articles/1500009668841-Working-With-Resource-Versions).

Below is a list of the sections covered in this topic:

* [Version Resource Structure in the Server Database](#Structure)
* [Storage of Versions on Disk](#Storage)

## Version Resource Structure in the Server Database

Information about versions, folders, nodes, the security system, the completed table, and server runtime performance are all stored in the specified database of Logi JReport Server. For production systems it is recommended to use the same DBMS as your database application so the server data will be backed up with the rest of the application.

To open the Derby database, use Apache toolkit ij. ij is Derby's interactive JDBC scripting tool. It is a simple utility for running scripts or interactive queries against a Derby database. ij is a Java application that you start from a command window such as an MS-DOS Command Window or the Unix shell. ij provides several non-SQL commands for use in accessing a variety of JDBC features for testing.

**To open the defaultRealm.\* files:**

1. Start ij.bat in `<install_root>\derby\bin`.
2. Connect to the database. To connect to a Derby database, you need to perform a valid database connection URL. ij automatically loads the appropriate driver based on the syntax of the URL. The following example shows how to connect defaultRealm by using the Connect command and the client driver:

   `D:>java org.apache.derby.tools.ij`  
   `ij version 10.5`  
   `ij> connect 'jdbc:derby://localhost:8886/defaultRealm';`  
   `ij>`
3. After connected to the database successfully, ij allows the execution of Derby SQL statements interactively or via scripts.

   **Note:** All statements must be terminated with a semicolon.

   **Example 1: Finding result version information from the database**

   Execute the command `SELECT * FROM RESULTVERSION_3 WHERE CREATOR='admin';` to retrieve result versions which were created by the user 'admin'.

   **Example 2: Finding catalog version information from the database**

   Execute the command `SELECT * FROM CATALOGVERSION_4;` to fetch all catalog versions.
4. For more information about Derby and ij, please visit Apache website <http://db.apache.org/derby/>.

**Note:** Do not delete, update or insert data into the database. It is recommended that all modifications to the database be done from Logi JReport Server instead of in the DBMS tools. Otherwise, it may result in Logi JReport Server crashing if invalid data is found.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Storage of Versions on Disk

A working directory `<install_root>\history` has been defined for use by the system database. Rather than store all the actual resources in the DBMS, the DBMS stores only pointers to the actual files. Logi JReport Server uses this folder to store all of the resources including parameter information and version files. By default, Logi JReport Server creates 100 folders in this history folder, and each of these folders can contain a further 3000 subfolders. These subfolders however cannot hold any further subfolders.

First, Logi JReport Server puts the history information, such as archive versions and parameter files in folder 1. When the amount of subfolders in folder 1 reaches the maximum subfolder amount, it starts to put files in folder 2. When folder 2 is filled up, folder 3 will be used, then folder 4, folder 5, and so on, until all 100 folders have been filled up.

When all the 100 folders have been filled up with subfolders, Logi JReport Server will then create another 100 folders, named 101 to 200, and will continue to store the history information in these folders, starting from folder 101. When the second 100 folders are full, another 100 folders will be created, and so on.

**Changing the storage folder**

You can specify another folder other than  `<install_root>\history` to store the version files by the servlet.jrserver.initArgs property in the servlet.properties file in `<install_root>\bin`. For example, set `servlet.jrserver.initArgs=D:\ServerData` to save version files to `D:\ServerData`.

For a [Logi JReport Server Cluster](https://devnet.logianalytics.com/hc/en-us/articles/1500009644262-Logi-JReport-Server-Guide-v15-Server-Cluster), you can also use the resource.share.hist.dir property in the server.properties file to change the storage folder.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673761-Deleting-Versions)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673681-Managing-Tasks)
