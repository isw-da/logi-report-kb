---
title: "Configuring in a Standalone Environment"
id: 1500009718822
section: "Configure Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009718822-Configuring-in-a-Standalone-Environment
updated_at: 2021-07-25T07:20:16Z
---

# Configuring in a Standalone Environment

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744781-Configuring-the-Server-Database)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744801-Configuring-in-an-Integrated-Environment)

# Configuring in a Standalone Environment

This topic demonstrates the two ways of configuring the server database in a standalone environment: via the Logi Report Server UI, or using the configuration file dbconfig.xml.

Select the following links to view the topics:

* [Configuring via Server UI](#Page)
* [Configuring in dbconfig.xml](#XML)

## Configuring via Server UI

1. In the Logi Report Server console, point to **Administration** on the system toolbar, and then select **Configuration** > **Server DB** > **System DB**/**Realm DB**/**Profiling DB** from the drop-down menu to open the corresponding page.
2. Select a realm if you are configuring the realm or profiling database from the Select Realm drop-down list at the top right corner.
3. In the Configuration tab, select a database driver from the Driver drop-down list.

   ![Configure System DB](https://devnet.logianalytics.com/hc/article_attachments/4404942608535/config_db_alone.gif)

   For SQL Server 2005 and later versions, select the driver com.microsoft.sqlserver.jdbc.SQLServerDriver from the drop-down list; select com.microsoft.jdbc.sqlserver.SQLServerDriver for versions earlier than SQL Server 2005.
4. In the Driver Class Location text box, type or select the **Browse** button to specify the location for the driver class.

   For the HSQLDB and Derby databases, you do not need to specify the driver class location. For all other databases, you will have to provide the driver class path information unless it has already been added to the class path during installation or by editing the setenv.bat file (setenv.sh on Unix) in `<install_root>\bin`.
5. Type a valid URL that can be used to establish a connection to the database. The valid format of the URL should be provided by the driver vendor.
6. ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404942452887/__newv17.jpg "New for version 17.")In the Connection Properties text box, you can add any properties supported by the database to serve your requirements. The input format is "key1=value1,key2=value2". For example, to control the socket timeout for the Oracle database connection, you can type the following: oracle.net.CONNECT\_TIMEOUT=60000,oracle.jdbc.ReadTimeout=60000.
7. Provide the user ID and password.
8. To test the connection, select **Test**. To update the database configuration and to apply the settings, select **Update** and then restart the server to finalize the function. All previously published reports and all other information on users, groups and roles will be lost when you restart.

## Configuring in dbconfig.xml

You can configure the server database in dbconfig.xml located in `<install_root>\bin` using either of the following two methods. Note that in dbconfig.xml, <database name> must be Logi Report Server's inner database name: *systemtables* for the system database, *realmtables* for the realm database, or *profile* for the profiling database.

**Method 1: Specifying the URL, driver, user and password respectively**

```
<database name="systemtables/realmtables/profile">  
    <url>...</url>  
    <driver>...</driver>  
    <user>...</user>  
    <password>...</password>  
</database>
```

The configuration via this method can also be modified [in the server console](#Page).

See the examples below:

* ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404942452887/__newv17.jpg "New for version 17.")The following example is for connecting to an Oracle database.

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
* ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404942452887/__newv17.jpg "New for version 17.")The following example is for connecting to an InterSystems IRIS database.

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

**Notes:**

* The <user> and <password> information is encrypted. They will be replaced by the <encrypt-sign> tag after Logi Report Server starts up as follows:

  `<encrypt-sign>enDkq7srM9cHhoUwzYXJ3NvcDIYk</encrypt-sign>`

  If you want to change user or password, delete the <encrypt-sign> tag and add the <user> and <password> tags in dbconfig.xml.
* For MySQL 5.0.xx, the letters in user name should all be lowercase.
* Because of the compatibility between the third party package Quartz used by Logi Report Server and the driver of Oracle database, the Quartz package will throw an exception when the class path of the Oracle database driver is added into dbconfig.xml. To avoid this problem, when Logi Report Server works with an Oracle database, do not set the database driver class path in dbconfig.xml.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744781-Configuring-the-Server-Database)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744801-Configuring-in-an-Integrated-Environment)
