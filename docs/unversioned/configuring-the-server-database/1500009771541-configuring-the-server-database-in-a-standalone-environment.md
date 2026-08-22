---
title: "Configuring the Server Database in a Standalone Environment"
id: 1500009771541
section: "Configuring the Server Database"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009771541-Configuring-the-Server-Database-in-a-Standalone-Environment
updated_at: 2021-07-24T00:49:28Z
---

# Configuring the Server Database in a Standalone Environment

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009771521-Configuring-the-Server-Database)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009743642-Configuring-the-Server-Database-in-an-Integrated-Environment)

# Configuring the Server Database in a Standalone Environment

This topic describes the two ways of configuring the server database in a standalone environment: via the Logi Report Server UI or using the configuration file **dbconfig.xml**.

This topic contains the following sections:

* [Configuring the Server Database via Server UI](#Page)
* [Configuring the Server Database in dbconfig.xml](#XML)

## Configuring the Server Database via Server UI

1. In the Server Console, point to **Administration** on the system toolbar, and then select **Configuration** > **Server DB** > **System DB**/**Realm DB**/**Profiling DB** from the drop-down menu. Server displays the corresponding page.
2. Select a realm if you are configuring the realm or profiling database from the **Select Realm** drop-down list at the top right corner.
3. In the **Configuration** tab, select a database driver from the **Driver** drop-down list.

   ![Configure System DB](https://devnet.logianalytics.com/hc/article_attachments/4404885608343/config_db_alone.gif)

   For SQL Server 2005 and later versions, select the driver **com.microsoft.sqlserver.jdbc.SQLServerDriver** from the drop-down list; select **com.microsoft.jdbc.sqlserver.SQLServerDriver** for versions earlier than SQL Server 2005.
4. In the **Driver Class Location** text box, select the **Browse** button to specify the location for the driver class.
   You can also type the location.

   For the HSQLDB and Derby databases, you do not need to specify the driver class location. For all other databases, you will have to provide the driver class path information unless you have already added it to the class path during installation or by editing the setenv.bat file (setenv.sh on Unix) in `<install_root>\bin`.
5. Type a valid URL to establish a connection to the database. You should follow the valid format of the URL according to the driver vendor.
6. In the **Connection Properties** text box, you can add any properties supported by the database to serve your requirements. The input format is "key1=value1,key2=value2". For example, to control the socket timeout for the Oracle database connection, you can type the following: oracle.net.CONNECT\_TIMEOUT=60000,oracle.jdbc.ReadTimeout=60000.
7. Provide the user ID and password.
8. To test the connection, select **Test**.
9. To update the database configuration and to apply the settings, select **Update** and then restart the server to finalize the function. You will lose all previously published reports and all other information on users, groups and roles when you restart.

## Configuring the Server Database in dbconfig.xml

You can configure the server database in **dbconfig.xml** in `<install_root>\bin` using either of the following two methods.

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4404885352855/criticalicon.gif)In dbconfig.xml, <database name> must be Logi Report Server's inner database name: *systemtables* for the system database, *realmtables* for the realm database, or *profile* for the profiling database.

**Method 1: Specifying the URL, driver, user, and password respectively**

```
<database name="systemtables/realmtables/profile">  
    <url>...</url>  
    <driver>...</driver>  
    <user>...</user>  
    <password>...</password>  
</database>
```

You can modify the configuration via this method [in the Server Console](#Page).

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

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)

* Logi Report Server encrypts the <user> and <password> information. It replaces them with the <encrypt-sign> tag after it starts up as follows:

  `<encrypt-sign>enDkq7srM9cHhoUwzYXJ3NvcDIYk</encrypt-sign>`

  If you want to change the user or password, delete the <encrypt-sign> tag and add the <user> and <password> tags in **dbconfig.xml**.
* For MySQL 5.0.xx, the letters in user name should all be lowercase.
* If you want to use special characters such as <, >, &, ', and " as text in the values in the dbconfig.xml file, you should follow the XML specifications. You can either use their corresponding escape characters or put a value that contains special characters into the CDATA block.
* Because of the compatibility between the third-party package **Quartz** in Logi Report Server and the driver of Oracle database, the Quartz package throws an exception when you add the class path of the Oracle database driver into **dbconfig.xml**. To avoid the problem, when Logi Report Server works with an Oracle database, do not set the database driver class path in dbconfig.xml.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009771521-Configuring-the-Server-Database)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009743642-Configuring-the-Server-Database-in-an-Integrated-Environment)
