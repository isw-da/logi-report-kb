---
title: "Configuring in a Standalone Environment"
id: 1500009669101
section: "Configuring Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009669101-Configuring-in-a-Standalone-Environment
updated_at: 2021-07-24T20:55:21Z
---

# Configuring in a Standalone Environment

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009669081-Configuring-the-Server-Database)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644482-Configuring-in-an-Integrated-Environment)

# Configuring in a Standalone Environment

When Logi JReport Server is running in a standalone environment, you can configure the database for it remotely on the Logi JReport Administration page. Also, since the server database configuration information is stored in the dbconfig.xml file in the directory `<install_root>\bin`, you can also configure the server database in this file. When you first install Logi JReport Server it will be using the Derby database by default. It is better to change the database while installing if you have the information to do so. If you are currently using Derby it needs to be changed using one of the following procedures. Do not use Derby in a production environment.

The following presents the two ways of configuring the server database in a standalone environment:

* [Configuring on the Logi JReport Administration Page](#Page)
* [Configuring in the dbconfig.xml File](#XML)

## Configuring on the Logi JReport Administration Page

1. Log onto the Logi JReport Administration page, select **Data** on the system toolbar and then select **System DB**, **Realm DB**, or **Profiling DB** from the drop-down menu to open the corresponding Data page.
2. Select a realm if you are configuing the realm or profiling database from the Select Realm drop-down list at the top right corner.
3. In the Configuration tab, select a DBDriver from the Driver drop-down list.

   For Microsoft SQL Server 2005 and later versions, select the driver com.microsoft.sqlserver.jdbc.SQLServerDriver from the drop-down list; select com.microsoft.jdbc.sqlserver.SQLServerDriver for versions earlier than Microsoft SQL Server 2005.

   ![Configure System DB](https://devnet.logianalytics.com/hc/article_attachments/4404920653079/config_db_alone.gif)
4. In the Driver Class Location text field, type or select the **Browse** button to specify the location for the driver class.

   For HSQLDB and Derby databases, you do not need to specify the driver class location. For all other databases, you will have to provide the driver class path information unless it has already been added to the class path of setenv.bat (setenv.sh on Unix) file during installation or by editing the setenv.bat file.
5. Type a valid URL that can be used to establish a connection to the database. The valid format of the URL should be provided by the DBDriver vendor.
6. Provide the user ID and password.
7. To test the connection, select **Test**. To update the database configuration and to apply the settings, select **Update** and then restart the server to finalize the function. All previously published reports and all other information on users, groups and roles will be lost when you restart.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Configuring in the dbconfig.xml File

In dbconfig.xml, you can configure the server database using one of two methods. One is to specify the URL, driver, user and password individually. This method of configuration can be modified through the Logi JReport Administration page. For example:

|  |
| --- |
| ``` <database name="systemtables/realmtables/profile">     <url>...</url>     <driver>...</driver>     <user>...</user>     <password>...</password> </database> ``` |

**Note:** The <user> and <password> information is encrypted. The <user> and <password> tags will be replaced by the <encrypt-sign> tag after Logi JReport Server's startup as follows:

`<encrypt-sign>enDkq7srM9cHhoUwzYXJ3NvcDIYk</encrypt-sign>`

If you want to change user or password, delete the <encrypt-sign> tag and add the <user> and <password> tags in the dbconfig.xml file.

The other is to use the <datasource> tag. For example:

|  |
| --- |
| ``` <database name="systemtables/realmtables/profile">     <datasource>         jdbc://user:password@jdbc:odbc:Logi JReport-realmtables#driver=sun.jdbc.odbc.JdbcOdbcDriver     </datasource> </database> ``` |

Here are two examples for your reference:

* The following example is for Oracle. Modify the dbconfig.xml file as follows:

  |  |
  | --- |
  | ``` <?xml version="1.0" encoding="UTF-8"?> <dbconfig>     <workspace name="systemRealm">         <database name="systemtables">             <url>jdbc:oracle:thin:@dbhost:1521:SystemDB</url>             <user>test</user>             <password>1234</password>              <driver>oracle.jdbc.OracleDriver</driver>         </database>     </workspace>     <workspace name="defaultRealm">         <database name="realmtables">             <url>jdbc:oracle:thin:@dbhost:1521:RealmDB</url>             <user>test</user>             <password>1234</password>              <driver>oracle.jdbc.OracleDriver</driver>         </database>     </workspace> </dbconfig> ``` |
* The following example is for a DataDirect driver. Modify the dbconfig.xml file as follows:

  |  |
  | --- |
  | ``` <?xml version="1.0" encoding="UTF-8"?> <dbconfig>         <workspace name="systemRealm">         <database name="systemtables">             <url>                 jdbc:datadirect:sqlserver://dbhost:1433;DatabaseName=SystemDB             </url>             <user>test</user>              <password>1234</password>              <driver>                 com.ddtek.jdbc.sqlserver.SQLServerDriver             </driver>             <dbtype>Microsoft SQLServer</dbtype>         </database>      </workspace>      <workspace name="defaultRealm">          <database name="realmtables">             <url>                 jdbc:datadirect:sqlserver://dbhost:1433;DatabaseName=RealmDB             </url>             <user>test</user>              <password>1234</password>              <driver>                 com.ddtek.jdbc.sqlserver.SQLServerDriver             </driver>             <dbtype>Microsoft SQLServer</dbtype>         </database>      </workspace>  </dbconfig> ``` |

**Notes:**

* For MySql 5.0.xx, the letters in user name should all be lowercase.
* Because of the compatibility between the third party package Quartz used by Logi JReport Server and the driver of Oracle database, the Quartz package will throw an exception when the class path of oracle database driver is added into dbconfig.xml. To avoid this problem, when the Logi JReport server works with an Oracle database, do not set database driver class path in dbconfig.xml.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009669081-Configuring-the-Server-Database)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644482-Configuring-in-an-Integrated-Environment)
