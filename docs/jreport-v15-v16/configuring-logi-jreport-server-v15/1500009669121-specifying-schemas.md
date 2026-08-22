---
title: "Specifying Schemas"
id: 1500009669121
section: "Configuring Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009669121-Specifying-Schemas
updated_at: 2021-07-24T20:55:21Z
---

# Specifying Schemas

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009669141-Creating-Tables-in-a-Specified-Tablespace)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644502-Initializing-the-Database-System-as-a-Non-admin-Database-User)

# Specifying Schemas

Logi JReport Server supports DBMS schemas in order to work well with DBMSs that are supported by Logi JReport Server and that support schemas. Those DBMSs include Oracle, DB2, SQL Server, Sybase, and PostgreSQL. You can specify schema information either in the dbconfig.xml file using the `<schema></schema>` tags, or in dsInfo by adding the attribute schema=schema\_name. If you are using Sybase, the schema name must use capital letters, for example, ABCDE.

**In dbconfig.xml**

Add the `<schema></schema>` tags in the dbconfig.xml file as follows:

|  |
| --- |
| ``` ... <workspace name="defaultRealm">      <database name="realmtables">         <driver classpath="...">jdbc_driver_name</driver>         <url>jdbc_url</url>         <user>jdbc_user</user>         <password>jdbc_password</password>         <schema>schema_name</schema>     </database> </workspace> ... ``` |

**In dsInfo**

Since dsInfo supports JNDI and JDBC protocols, you can add the attribute schema=schema\_name in the JNDI or JDBC statement. The JNDI approach is only available when deploying Logi JReport Server into a Java Application Server, not when it is running in standalone mode.

* jdbc://[<jdbc-user>:<jdbc-password>@]<jdbc-url>[#<attribute-name=attribute-value>,]

  For example:

  `jdbc://user:password@jdbc:odbc:Logi JReport-realmtables#driver=sun.jdbc.odbc.JdbcOdbcDriver,schema=db2admin`
* jndi://[<jdbc-user>:<jdbc-password>@]<datasource-name>[#<attri-name=attri-value>,]

  For example:

  `jndi://jdbc/Logi JReport-realmtables#schema=db2admin`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009669141-Creating-Tables-in-a-Specified-Tablespace)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644502-Initializing-the-Database-System-as-a-Non-admin-Database-User)
