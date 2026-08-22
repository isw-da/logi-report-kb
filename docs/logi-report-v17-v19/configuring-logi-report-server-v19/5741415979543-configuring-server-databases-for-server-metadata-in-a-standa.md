---
title: "Configuring Server Databases for Server Metadata in a Standalone Environment"
id: 5741415979543
section: "Configuring Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741415979543-Configuring-Server-Databases-for-Server-Metadata-in-a-Standalone-Environment
updated_at: 2022-10-31T17:15:59Z
---

# Configuring Server Databases for Server Metadata in a Standalone Environment

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741387194519-Configuring-Server-Databases-for-Server-Metadata)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741395898263-Configuring-Server-Databases-for-Server-Metadata-in-an-Integrated-Environment)

# Configuring Server Databases for Server Metadata in a Standalone Environment

This topic describes the two ways of configuring server databases for server metadata in a standalone environment: via the Logi Report Server UI or using the configuration file **dbconfig.xml**.

This topic contains the following sections:

* [Configuring Server Databases for Server Metadata via Server UI](#Page)
* [Configuring Server Databases for Server Metadata in dbconfig.xml](#XML)

## Configuring Server Databases for Server Metadata via Server UI

1. On the system toolbar of the Server Console, navigate to **Administration** > **Configuration** > **Server DB** > **System DB**/**Realm DB**/**Profiling DB**. Server displays the corresponding page.
2. Select a realm if you are configuring the realm or profiling database from the **Select Realm** drop-down list at the upper-right corner.
3. In the **Configuration** tab, select a database driver from the **Driver** drop-down list.

   ![Configure System DB](https://devnet.logianalytics.com/hc/article_attachments/9905779982615/config_db_alone.gif)

   For SQL Server 2005 and later versions, select the driver **com.microsoft.sqlserver.jdbc.SQLServerDriver** from the drop-down list; select **com.microsoft.jdbc.sqlserver.SQLServerDriver** for versions earlier than SQL Server 2005.
4. In the **Driver Class Location** text box, select the **Browse** button to specify the location for the driver class.
   You can also type the location.

   For the HSQLDB and Derby databases, you do not need to specify the driver class location. For all other databases, you will have to provide the driver class path information unless you have already added it to the class path during installation or by editing the setenv.bat file (setenv.sh on UNIX) in `<install_root>\bin`.
5. Type a valid URL to establish a connection to the database. You should follow the valid format of the URL according to the driver vendor.
6. In the **Connection Properties** text box, you can add any properties supported by the database to serve your requirements. The input format is "key1=value1,key2=value2". For example, to control the socket timeout for the Oracle database connection, you can type the following: oracle.net.CONNECT\_TIMEOUT=60000,oracle.jdbc.ReadTimeout=60000.
7. Provide the user ID and password.
8. To test the connection, select **Test**.
9. To update the database configuration and to apply the settings, select **Update** and then restart the server to finalize the function. You will lose all previously published reports and all other information on users, groups and roles when you restart.

## Configuring Server Databases for Server Metadata in dbconfig.xml

You can configure the server database in **dbconfig.xml** in `<install_root>\bin` using either of the following two methods.

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/9905614395415/criticalicon.gif) In dbconfig.xml, <database name> must be Logi Report Server's inner database name: *systemtables* for the system database, *realmtables* for the realm database, or *profile* for the profiling database.

**Method 1: Specifying the URL, driver, user, and password respectively**

```
<database name="systemtables/realmtables/profile">  
    <url>...</url>  
    <driver>...</driver>  
    <user>...</user>  
    <password>...</password>  
</database>
```

You can modify the configuration via this method [on the Server Console](#Page).

**Examples**

* The following example is for connecting to an Oracle database.

  ```
  <?xml version="1.0" encoding="UTF-8"?>  
  <dbconfig>  
      <workspace name="systemRealm">  
          <database name="systemtables">  
              <url>jdbc:oracle:thin:@dbhost:1521:SystemDB</url>  
              <user>test</user>
              <password>1234</password>  
              <driver>oracle.jdbc.OracleDriver</driver>  
              <connection oracle.net.CONNECT_TIMEOUT="60000" oracle.jdbc.ReadTimeout="60000"/>  
          </database>  
      </workspace>  
      <workspace name="defaultRealm">  
          <database name="realmtables">  
              <url>jdbc:oracle:thin:@dbhost:1521:RealmDB</url>  
              <user>test</user>  
              <password>1234</password>  
              <driver>oracle.jdbc.OracleDriver</driver>  
              <connection oracle.net.CONNECT_TIMEOUT="60000" oracle.jdbc.ReadTimeout="60000"/>  
          </database>  
      </workspace>  
  </dbconfig>
  ```
* The following example is for using the DataDirect driver to connect to a SQL Server database.

  ```
  <?xml version="1.0" encoding="UTF-8"?>  
  <dbconfig>  
      <workspace name="systemRealm">  
          <database name="systemtables">  
              <url>jdbc:datadirect:sqlserver://dbhost:1433;DatabaseName=SystemDB</url>  
              <user>test</user>  
              <password>1234</password>  
              <driver>com.ddtek.jdbc.sqlserver.SQLServerDriver</driver>  
              <dbtype>Microsoft SQLServer</dbtype>  
          </database>   
      </workspace>  
      <workspace name="defaultRealm">   
          <database name="realmtables">  
              <url>jdbc:datadirect:sqlserver://dbhost:1433;DatabaseName=RealmDB</url>  
              <user>test</user>  
              <password>1234</password>  
              <driver>com.ddtek.jdbc.sqlserver.SQLServerDriver</driver>  
              <dbtype>Microsoft SQLServer</dbtype>  
           </database>  
      </workspace>  
  </dbconfig>
  ```
* The following example is for connecting to an InterSystems IRIS database.

  ```
  <?xml version="1.0" encoding="UTF-8"?>  
  <dbconfig>  
      <workspace name="systemRealm">  
          <database name="systemtables">  
              <url>jdbc:IRIS://192.168.3.2:51773/NameSpace</url>  
              <user>test</user>  
              <password>1234</password>  
              <driver>com.intersystems.jdbc.IRISDriver</driver>  
          </database>   
      </workspace>  
      <workspace name="defaultRealm">   
          <database name="realmtables">  
              <url>jdbc:IRIS://192.168.3.2:51773/NameSpace</url>  
              <user>test</user>  
              <password>1234</password>  
              <driver>com.intersystems.jdbc.IRISDriver</driver>  
           </database>  
           <database name="profile">  
              <url>jdbc:IRIS://192.168.3.2:51773/NameSpace</url>  
              <user>test</user>  
              <password>1234</password>  
              <driver>com.intersystems.jdbc.IRISDriver</driver>  
           </database>  
      </workspace>  
  </dbconfig>
  ```

**Method 2: Specifying a JDBC data source using the <datasource></datasource> tags**

The URL format of a JDBC data source is:

`jdbc://[<jdbc-user:jdbc-password>@]<jdbc-url>[#<attribute-name=attribute-value>,]`

For example:

```
<database name="systemtables/realmtables/profile">  
    <datasource>  
        jdbc://user:password@jdbc:odbc:jreport-realmtables#driver=sun.jdbc.odbc.JdbcOdbcDriver  
    </datasource>  
</database>
```

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)

* Logi Report Server encrypts the <user> and <password> information. It replaces them with the <encrypt-nsign> tag after it starts:

  `<encrypt-nsign>enDkq7srM9cHhoUwzYXJ3NvcDIYk</encrypt-nsign>`

  If you want to change the user or password, delete the <encrypt-nsign> tag and add the <user> and <password> tags in **dbconfig.xml**.
* For MySQL 5.0.xx, the letters in username should all be lowercase.
* If you want to use special characters such as <, >, &, ', and " as text in the values in the dbconfig.xml file, you should follow the XML specifications. You can either use their corresponding escape characters or put a value that contains special characters into the CDATA block.
* Because of the compatibility between the third-party package **Quartz** in Logi Report Server and the driver of Oracle database, the Quartz package throws an exception when you add the class path of the Oracle database driver into **dbconfig.xml**. To avoid the problem, when Logi Report Server works with an Oracle database, do not set the database driver class path in dbconfig.xml.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741387194519-Configuring-Server-Databases-for-Server-Metadata)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741395898263-Configuring-Server-Databases-for-Server-Metadata-in-an-Integrated-Environment)
