---
title: "Configuring the datasource.xml File"
id: 1500009669061
section: "Configuring Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009669061-Configuring-the-datasource-xml-File
updated_at: 2021-07-24T20:55:22Z
---

# Configuring the datasource.xml File

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009669041-Configuring-Dynamic-Connections)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644562-Configuring-Connection-Pool)

# Configuring the datasource.xml File

In order to enable you to conveniently set different connections in Logi JReport Server, a configuration file, datasource.xml, is provided with which you can change to another runtime JDBC or JNDI data source to run reports by setting up connection mapping information such as the JDBC driver, URL, or JNDI data source name, user and password, depending on the data source your application uses. This allows you to control the catalog data source connections in Logi JReport Server to connect dynamically to your production data sources.

The datasource.xml file is located in the `<install_root>\bin` directory. Change this file according to the data source you want to use. Two types of connections are supported by Logi JReport Server. They are JNDI data source connection and JDBC connection.

Below is a list of the sections covered in this topic:

* [Contents of datasource.xml](#Contents)
* [Reloading Connection Information From datasource.xml](#Reload)
* [Integrating Logi JReport Server With Your Java Application Server](#Integ)
* [Example 1: Using JNDI Data Source Connections of WebLogic Server](#Eg1)
* [Example 2: Using JNDI Data Source Connections of JBoss Server](#Eg2)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Contents of datasource.xml

There can be multiple <datasource></datasource> tags in datasource.xml. Each pair will map one of the connections in your catalog. You can define mapping connections for multiple connections for more than one catalog. The catalog connection name should be unique in the datasource.xml file, otherwise the latter <datasource> information will overwrite the previous ones.

The contents of the datasource.xml file is as follows:

|  |
| --- |
| ``` <?xml version="1.0" encoding="UTF-8"?> <datasource-mapping>     <datasource>         <catalog-connection-name>Connection1</catalog-connection-name>         <connection-type>JNDI</connection-type>         <jndi-datasource>Sample</jndi-datasource>     </datasource>     <datasource>         <catalog-connection-name>Connection2</catalog-connection-name>         <connection-type>JDBC</connection-type>         <driver>sun.jdbc.odbc.JdbcOdbcDriver</driver>         <url>jdbc:odbc:jinfonet</url>         <user>Username</user>         <password>Password</password>     </datasource> </datasource-mapping> ``` |

**Element descriptions**

* **catalog-connection-name**  
   Specifies the name of the catalog connection that you want to substitute. Note that this is the connection name that you can see in Logi JReport Catalog Browser. A unique connection name in a catalog is suggested.
* **connection-type**  
   Specifies the connection type, which can be either JNDI or JDBC.
* **jndi-datasource**  
   If you are using a JNDI data source, specify the JNDI data source name you defined in your Java application server which you want to use as the substitute connection.
* **driver & url**  
   If you are using a JDBC data source, specify the JDBC Driver and URL in these two attributes.
* **user & password**  
   Specifies the user name and the password.

  The <user> and <password> information is encrypted. The <user> and <password> tags will be replaced by the <encrypt-sign> tag after Logi JReport Server's startup as follows:

  `<encrypt-sign>enDkq7srM9cHhoUwzYXJ3NvcDIYk</encrypt-sign>`

  If you want to change user or password, delete the <encrypt-sign> tag and add the <user> and <password> tags in the datasource.xml file.

  You can choose whether to provide database user and password information for the JNDI connection, using the <user> and <password> tags. If the user and password information is provided in this file, it will be used to set up the connection regardless of the settings defined in your application server. Otherwise, the settings defined in your application server will be used. Specially, for WebLogic users, you should provide user name and password for WebLogic console instead of the database.
* **refresh-support-info**  
   Optional. If it is true, Logi JReport will get support information including reverse words, quote characters and so on from the driver each time fetching data from the database. If it is not set, the property will be treated as false. It is recommended that you set this property to true when connecting to a different database.
* **quote-character**  
   Optional. Specifies the quote characters.
* **extra-characters**  
   Optional. Specifies the extra characters.
* **date-format**  
   Optional. Specifies the date format.
* **datetime-format**  
   Optional. Specifies the datetime format.
* **time-format**  
   Optional. Specifies the time format.
* **transaction-readonly**  
   Optional. Specifies the transaction "read only" property. Possible value: default, Read only, or Read&Write. Ignore other values.
* **transaction-mode**  
   Optional. Specifies the transaction mode. Possible value: default, None, Read Uncommitted, Read Committed, Repeatable Read, or Serializable. Ignore other values.
* **char-to-be-replaced**  
   Optional. Specifies the characters that are to be replaced.
* **char-replaced-by**  
   Optional. Specifies the characters used to replace the characters specified by char-to-be-replaced.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Reloading Connection Information From datasource.xml

After you have made changes to the datasource.xml file, you need to reload it in Logi JReport Server. This file can be reloaded using either of the following ways:

* Log onto the Logi JReport Administration page, go to the **Configuration** > **Connection** page, and then select the **Reload** button.
* Call jet.server.api.admin.ConnectionInfoProviderService.reloadFile().

Then restart Logi JReport Server.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Integrating Logi JReport Server With Your Java Application Server

After updating the datasource.xml file, you can integrate Logi JReport Server with your application server.

If you are using a WAR file, make sure that the datasource.xml file is included in the WAR file. Before making the Logi JReport Server WAR file, in makewar.xml in the `<install_root>\bin` directory, add `<include name="datasource.xml" />` into the `<zipfileset dir="${installroot}/bin" prefix="workspace/bin">` section. Before you deploy the WAR file to a web server, make sure that the datasource.xml file is included in the `Logi JReport.war/WEB-INF/lib/jrenv.jar/workspace/bin` directory.

If you are integrating Logi JReport Server to an application using a non-Logi JReport WAR file, usually you need to specify the -Dreporthome parameter in the application server so that the application server can locate and load the resources it needs. Since the datasource.xml already exists in the bin directory, you do not need to do anything special for this file.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Example 1: Using JNDI Data Source Connections of WebLogic Server

Using WebLogic as an example, take the following steps:

1. Start WebLogic server, navigate to <YourProjectName> > Services > JDBC > Connection Pools. In the Configuration tab, make sure that the connection you are going to use is there and correctly set up.
2. Browse to  <YourProjectName> > Services > JDBC > Data Sources. In the Configuration tab, create a data source using the JNDI name MyJNDISample. Select the correct connection from the Pool Name drop-down list.
3. Open datasource.xml in the `<install_root>\bin` directory and add:

   |  |
   | --- |
   | ``` <datasource-mapping>     <datasource>         <catalog-connection-name>ConnectionName</catalog-connection-name>         <connection-type>JNDI</connection-type>         <jndi-datasource>MyJNDISample</jndi-datasource>         <user>youruserid</user>         <password>yourpassword</password>     </datasource> </datasource-mapping> ``` |
4. Build the Logi JReport Server WAR file using the makewar utility in the `<install_root>\bin` directory.
5. Deploy Logi JReport Server to WebLogic.
6. Run the report that uses this connection.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Example 2: Using JNDI Data Source Connections of JBoss Server

Using JBoss as an example, in this Example, DB2 is used, and JBoss is installed to `D:\jboss-4.0.1`, take the following steps:

1. Copy the DB2 driver to `D:\jboss-4.0.1\server\default\lib`.
2. Create a db2-ds.xml file in `D:\jboss-4.0.1\server\default\deploy`, and add the following content:

   |  |
   | --- |
   | ``` <?xml version="1.0" encoding="UTF-8"?> <datasources>     <local-tx-datasource>         <jndi-name>DB2DataSource</jndi-name>         <connection-url>jdbc:db2://dbs-b/sample</connection-url>         <driver-class>com.ibm.db2.jdbc.net.DB2Driver</driver-class>         <user-name>db2admin</user-name>         <password>db2admin</password>         <min-pool-size>0</min-pool-size>         <metadata>             <type-mapping>DB2</type-mapping>         </metadata>     </local-tx-datasource> </datasources> ``` |
3. Modify datasource.xml in `<install_root>\bin`. Make sure that the following are included:

   |  |
   | --- |
   | ``` <datasource-mapping>     <datasource>         <catalog-connection-name>ConnectionName</catalog-connection-name>         <connection-type>JNDI</connection-type>         <jndi-datasource>java:/DB2DataSource</jndi-datasource>     </datasource> </datasource-mapping> ``` |
4. Build the Logi JReport Server WAR file using the makewar.bat utility in the `<install_root>\bin` directory.
5. Deploy Logi JReport Server to JBoss.
6. Run the report that uses this connection.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009669041-Configuring-Dynamic-Connections)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644562-Configuring-Connection-Pool)
