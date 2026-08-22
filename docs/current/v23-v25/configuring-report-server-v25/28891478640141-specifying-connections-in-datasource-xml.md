---
title: "Specifying Connections in datasource.xml"
id: 28891478640141
section: "Configuring Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891478640141-Specifying-Connections-in-datasource-xml
updated_at: 2026-02-26T02:11:16Z
source_host: docs-report.zendesk.com
---
# 
Specifying Connections in datasource.xml 

You can conveniently set different connections in Report Server, using a configuration file datasource.xml.  This topic describes how you can modify the contents of datasource.xml, reload connection information from the file, integrate Report Server into your application server with the updated datasource.xml, and use JNDI data source connections of WebLogic and JBoss Servers.

You can change the datasource.xml file to use another runtime JDBC, JNDI, or MongoDB data source to run reports, depending on the data source your application uses. In this way, you can control the catalog data source connections in Report Server to dynamically connect to your production data sources.

This topic contains the following sections:

- Contents of datasource.xml

- Reloading Connection Information from datasource.xml

- Integrating Report Server with Your Java Application Server

- Example 1: Using JNDI Data Source Connections of WebLogic Server

- Example 2: Using JNDI Data Source Connections of JBoss Server

## 
Contents of datasource.xml

 You can configure three types of connections in Report Server using the datasource.xml file: JNDI data source connection, JDBC connection, and MongoDB connection. The datasource.xml file is in the <install_root>\bin directory.

You can add multiple <datasource></datasource> tags in datasource.xml. Each pair maps one of the connections in your catalog. You can define multiple connections for more than one catalog. The catalog connection name should be unique in the datasource.xml file. Otherwise, the latter <datasource> information will overwrite the previous ones with the same name.

The content of the datasource.xml file are:

<?xml version="1.0" encoding="UTF-8"?>
<datasource-mapping>
        <!-- Specify catalog connection to use JNDI data source -->
    <datasource>
        <catalog-connection-name>ConnectionName1</catalog-connection-name>
        <connection-type>jndi</connection-type>
        <jndi-datasource>Sample</jndi-datasource>
    </datasource>
        <!-- Specify catalog connection to use JDBC data source -->
    <datasource>
        <catalog-connection-name>ConnectionName2</catalog-connection-name>
        <connection-type>jdbc</connection-type>
        <driver>org.hsqldb.jdbcDriver</driver>
        <url>jdbc:hsqldb:demo</url>
        <user>Username</user>
        <password>Password</password>
    </datasource>
    <datasource>
        <catalog-connection-name>ConnectionName3</catalog-connection-name>
        <connection-type>MongoDB</connection-type>
        <driver>toolkit.db.mongo.MongoDriver</driver>
        <user>Username</user>
        <password>Password</password>
        <url>mongodb://192.127.000.1:27017</url>
        <databases>
            <database>
                <catalog-database-name>test</catalog-database-name>
                <database-name>test1</database-name>
                <collections>
                    <collection>
                        <catalog-collection-name>Areas</catalog-collection-name>
                        <collection-name>Areas1</collection-name>
                    </collection>
                </collections>
            </database>
        </databases>
    </datasource>
</datasource-mapping>
The table describes the elements in the datasource.xml file.

| Element | Description |
| --- | --- |
| catalog-connection-name | The name of the catalog connection that you want to substitute. This is the connection name that you can see in the Report Designer Catalog Manager. You should use a unique connection name in a catalog. |
| connection-type | The connection type can be JNDI, JDBC, or MongoDB. |
| jndi-datasource | If you are using a JNDI data source, provide the JNDI data source name you defined in your Java application server which you want to use as the substitute connection. |
| driver & url | If you are using a JDBC or MongoDB data source, specify the JDBC or MongoDB Driver and URL in these two attributes. |
| user & password | The username and password. Report Server encrypts the  and  information. It replaces the  and  tags with the  tag after it starts: enDkq7srM9cHhoUwzYXJ3NvcDIYk If you want to change the user or password, delete the  tag and add the  and  tags in the datasource.xml file. You can choose whether to provide database user and password information for the JNDI connection, using the  and  tags. If you provide the user and password information in this file, Server uses it to set up the connection regardless of the settings you defined in your application server. Otherwise, Server uses the settings defined in your application server. Specially, for WebLogic users, you should provide username and password for WebLogic console instead of the database. |
| refresh-support-info | Optional. Set the option to true if you want Report to get support information like reverse words and quote characters from the driver each time fetching data from the database, and when connecting to a different database. |
| quote-character | Optional. The quote characters. |
| extra-characters | Optional. The extra characters. |
| date-format | Optional. The date format. |
| datetime-format | Optional. The datetime format. |
| time-format | Optional. The time format. |
| transaction-readonly | Optional. The transaction "read only" property. Possible values: default, read only, or read & write. |
| transaction-mode | Optional. The transaction mode. Possible values: default, none, read uncommitted, read committed, repeatable read, or serializable. |
| char-to-be-replaced | Optional. The characters that you want to replace. |
| char-replaced-by | Optional. The characters that you use to replace the characters specified by char-to-be-replaced. |
| databases | The database list in the MongoDB connection. |
| database | A MongoDB database. |
| catalog-database-name | The database name you defined in the catalog for MongoDB. |
| database-name | The new database name you want to use at runtime to replace the original database name you defined in MongoDB APE. |
| collections | The collection list in a MongoDB database. |
| collection | A MongoDB collection. |
| catalog-collection-name | The collection name you defined in the catalog for MongoDB. |
| collection-name | The new collection name you want to use at runtime to replace the original collection name you defined in MongoDB APE. |

## 
Reloading Connection Information from datasource.xml

After you make changes to the datasource.xml file, you need to reload it in Report Server, using either of the ways:

- On the Server Console, go to the Administration > Connection > Reload Connection page, and then select Reload. 

- Call jet.server.api.admin.ConnectionInfoProviderService.reloadFile().

## 
Integrating Report Server with Your Java Application Server

After updating the datasource.xml file, you can integrate Report Server with your application server.

If you are using a WAR file, make sure to include the datasource.xml file in the WAR file. To do this, 

- Before making the Report Server WAR file, in makewar.xml in the <install_root>\bin directory, add <include name="datasource.xml" /> into the <zipfileset dir="${installroot}/bin" prefix="workspace/bin"> section. 

- Before you deploy the WAR file to a web server, make sure to include the datasource.xml file in the jreport.war/WEB-INF/lib/jrenv.jar/workspace/bin directory.

If you are integrating Report Server with an application using a non-Report WAR file, usually you need to specify the -Dreporthome parameter in the application server so that the application server can locate and load the resources it needs. Since the datasource.xml already exists in the bin directory, you do not need to do anything special for this file.

## 
Example 1: Using JNDI Data Source Connections of WebLogic Server

Using WebLogic as an example, take the following steps:

- Start WebLogic server.

- Navigate to <YourProjectName> > Services > JDBC > Connection Pools. 

- In the Configuration tab, make sure that the connection you are going to use is there and correctly set up.

- Browse to <YourProjectName> > Services > JDBC > Data Sources. 

- In the Configuration tab, create a data source using the JNDI name MyJNDISample. 

- Select the correct connection from the Pool Name drop-down list.

- Open datasource.xml in the <LogiReportServer_install_root>\bin directory and add the following:
    

<datasource-mapping>
    <datasource>
        <catalog-connection-name>ConnectionName</catalog-connection-name>
        <connection-type>JNDI</connection-type>
        <jndi-datasource>MyJNDISample</jndi-datasource>
        <user>youruserid</user>
        <password>yourpassword</password>
    </datasource>
</datasource-mapping>

- Build the Report Server WAR file using the makewar utility in the <LogiReportServer_install_root>\bin directory.

- Deploy Report Server to WebLogic.

- Run the report that uses this connection to check the result.

## 
Example 2: Using JNDI Data Source Connections of JBoss Server

We will use JBoss as an example. In this example, we use DB2, and installed JBoss to D:\jboss. Take the following steps:

- Copy the DB2 driver to D:\jboss\server\default\lib.

- Create a db2-ds.xml file in D:\jboss\server\default\deploy, and add the following contents:
    

<?xml version="1.0" encoding="UTF-8"?>
<datasources>
    <local-tx-datasource>
        <jndi-name>DB2DataSource</jndi-name>
        <connection-url>jdbc:db2://dbs-b/sample</connection-url>
        <driver-class>com.ibm.db2.jdbc.net.DB2Driver</driver-class>
        <user-name>db2admin</user-name>
        <password>db2admin</password>
        <min-pool-size>0</min-pool-size>
        <metadata>
            <type-mapping>DB2</type-mapping>
        </metadata>
    </local-tx-datasource>
</datasources>

- Modify datasource.xml in <LogiReportServer_install_root>\bin to include the following:
    

<datasource-mapping>
    <datasource>
        <catalog-connection-name>ConnectionName</catalog-connection-name>
        <connection-type>JNDI</connection-type>
        <jndi-datasource>java:/DB2DataSource</jndi-datasource>
    </datasource>
</datasource-mapping>

- Build the Report Server WAR file using the makewar.bat utility in the <LogiReportServer_install_root>\bin directory.

- Deploy Report Server to JBoss.

- Run the report that uses this connection to view it.
