---
title: " Advanced Version Topics About Version Structure and Storage"
id: 4405683943191
section: "Managing Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683943191--Advanced-Version-Topics-About-Version-Structure-and-Storage
updated_at: 2022-01-27T07:59:41Z
---

#  Advanced Version Topics About Version Structure and Storage

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690646167-Deleting-Versions)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683937303-Managing-Report-Running-Tasks)

# Advanced Version Topics About Version Structure and Storage

This topic describes advanced version topics for administrators and gives you an understanding of version structure and storage in depth.

Developers can also [use API to manage the resource versions](https://devnet.logianalytics.com/hc/en-us/articles/4405683568919-Working-with-Resource-Versions).

This topic contains the following sections:

* [Version Resource Structure in the Server Database](#Structure)
* [Storage of Versions on Disk](#Storage)

## Version Resource Structure in the Server Database

Server stores information about versions, folders, nodes, the security system, the completed table, and server runtime performance, in the specified server database. For production systems you should use the same DBMS as your database application so you can back up the server data with the rest of the application.

To open the Derby database, use Apache toolkit **ij**. ij is Derby's interactive JDBC scripting tool. It is a simple utility for running scripts or interactive queries against a Derby database. ij is a Java application that you start from a command window such as an MS-DOS Command Window or the UNIX shell. ij provides several non-SQL commands for use in accessing a variety of JDBC features for testing.

**To open the defaultRealm.\* files:**

1. Start **ij.bat** in `<install_root>\derby\bin`.
2. To connect to a Derby database, you need to perform a valid database connection URL. ij automatically loads the appropriate driver based on the syntax of the URL. The following example shows how to connect defaultRealm using the **Connect** command and the client driver:

   `D:>java org.apache.derby.tools.ij`  
   `ij version 10.5`  
   `ij> connect 'jdbc:derby://localhost:8886/defaultRealm';`  
   `ij>`
3. After Server connects to the database, ij enables the execution of Derby SQL statements interactively or via scripts.

   ![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4420453448599/criticalicon.gif)You must terminate all statements with a semicolon.

   **Example 1: Finding result version information from the database**

   Execute the command `SELECT * FROM RESULTVERSION_3 WHERE CREATOR='admin';` to retrieve result versions that the user 'admin' created.

   **Example 2: Finding catalog version information from the database**

   Execute the command `SELECT * FROM CATALOGVERSION_4;` to fetch all catalog versions.
4. For more information about Derby and ij, visit Apache website <http://db.apache.org/derby/>.

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4420453448599/criticalicon.gif)Do not delete, update, or insert data into the database. You should make all modifications to the database from Logi Report Server instead of in the DBMS tools. Otherwise, Logi Report Server might stop responding if it finds invalid data.

## Storage of Versions on Disk

Server has defined a working directory `<install_root>\history` for the system database to use. Rather than store all the actual resources in the DBMS, the DBMS stores only pointers to the actual files. Server uses this folder to store all the resources including parameter information and version files. By default, Server creates 100 folders in this history folder, and each of these folders can contain a further 3000 sub folders. These sub folders however cannot hold any further sub folders.

First, Server puts the history information, such as archive versions and parameter files in folder 1. When the amount of sub folders in folder 1 reaches the maximum sub folder amount, Server starts to put files in folder 2. When folder 2 fills up, Server uses folder 3, then folder 4, folder 5, and so on, until all 100 folders have filled up.

When all the 100 folders have filled up with sub folders, Server then creates another 100 folders, named 101 to 200, and will continue to store the history information in these folders, starting from folder 101. When the second 100 folders are full, Server creates another 100 folders, and so on.

**Changing the storage folder**

You can specify another folder other than  `<install_root>\history` to store the version files, by the **servlet.jrserver.initArgs** property in the **servlet.properties** file in `<install_root>\bin`. For example, set `servlet.jrserver.initArgs=D:\ServerData` to save version files to `D:\ServerData`.

For a [Logi Report Server Cluster](https://devnet.logianalytics.com/hc/en-us/articles/4405683570967-Logi-Report-Server-Cluster-Logi-Report-Server-v18), you can also use the **resource.share.hist.dir** property in the **server.properties** file to change the storage folder.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690646167-Deleting-Versions)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683937303-Managing-Report-Running-Tasks)
