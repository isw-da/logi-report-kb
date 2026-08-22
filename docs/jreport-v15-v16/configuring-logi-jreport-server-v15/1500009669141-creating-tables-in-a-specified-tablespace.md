---
title: "Creating Tables in a Specified Tablespace"
id: 1500009669141
section: "Configuring Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009669141-Creating-Tables-in-a-Specified-Tablespace
updated_at: 2021-07-24T20:55:20Z
---

# Creating Tables in a Specified Tablespace

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644482-Configuring-in-an-Integrated-Environment)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009669121-Specifying-Schemas)

# Creating Tables in a Specified Tablespace

Logi JReport Server supports creating tables in a user-specified tablespace in a database that supports tablespaces, such as DB2 and Oracle. A key-value pair tablespace is provided to specify a tablespace into which Logi JReport Server will create database tables. This key-value pair is then passed to Logi JReport Server through the JDBC configuration. Logi JReport Server retrieves the tablespace information from the JDBC (data source) configuration, and then creates tables in the specified tablespace.

Tablespace can be configured either in the dbconfig.xml file by using the `<tablespace></tablespace>` tags, or in dsInfo by adding the attribute tablespace=table\_space\_name.

#### In dbconfig.xml

Add the `<tablespace></tablespace>` tags in the dbconfig.xml file as follows:

|  |
| --- |
| ``` ... <workspace name="defaultRealm">     <database name="realmtables">         <driver classpath="...">jdbc_driver_name</driver>         <url>jdbc_url</url>         <user>jdbc_user</user>         <password>jdbc_password</password>         <tablespace>table_space_name</tablespace>     </database> </workspace> ... ``` |

#### **In dsInfo**

Since dsInfo supports JNDI and JDBC protocols, you can add the attribute tablespace=table\_space\_name in the JNDI or JDBC statement.

* jdbc://[<jdbc-user>:<jdbc-password>@]<jdbc-url>[#<attribute-name=attribute-value>,]

  For example:

  `jdbc://user:password@jdbc:odbc:Logi JReport-realmtables#driver=sun.jdbc.odbc.JdbcOdbcDriver,tablespace=myTablespace`
* jndi://[<jdbc-user>:<jdbc-password>@]<datasource-name>[#<attri-name=attri-value>,]

  For example:

  `jndi://jdbc/Logi JReport-realmtables#tablespace=myTablespace`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644482-Configuring-in-an-Integrated-Environment)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009669121-Specifying-Schemas)
