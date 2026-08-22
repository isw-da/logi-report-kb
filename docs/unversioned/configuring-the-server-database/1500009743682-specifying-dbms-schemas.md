---
title: "Specifying DBMS Schemas"
id: 1500009743682
section: "Configuring the Server Database"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009743682-Specifying-DBMS-Schemas
updated_at: 2021-07-24T00:49:27Z
---

# Specifying DBMS Schemas

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009771601-Creating-Tables-in-a-Specified-Tablespace)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009771561-Initializing-the-Database-System-as-a-Non-admin-Database-User)

# Specifying DBMS Schemas

Logi Report Server supports DBMS schemas to work well with databases that support schemas. Those DBMSs include Oracle, DB2, SQL Server, Sybase, PostgreSQL, InterSystems Caché, and EnterpriseDB. This topic describes how you can specify schema information in the **dbconfig.xml** file.

You can specify schema information in the **dbconfig.xml** file in `<install_root>\bin` by adding the <schema></schema> tags as follows:

```
...  
<workspace name="defaultRealm">  
 
    <database name="realmtables">  
        <driver classpath="...">jdbc_driver_name</driver>  
        <url>jdbc_url</url>  
        <user>jdbc_user</user>  
        <password>jdbc_password</password>  
        <schema>schema_name</schema>  
    </database>  
</workspace>  
...
```

When you specify the server database using a JDBC or JNDI data source, you can also specify schema information by adding the attribute **schema=schema\_name** in the JDBC or JNDI data source.

* `jdbc://[<jdbc-user>:<jdbc-password>@]<jdbc-url>[#<attribute-name=attribute-value>,]`

  For example:

  `jdbc://user:password@jdbc:odbc:jreport-realmtables#driver=sun.jdbc.odbc.JdbcOdbcDriver,schema=db2admin`
* `jndi://[<jdbc-user>:<jdbc-password>@]<datasource-name>[#<attri-name=attri-value>,]`

  For example:

  `jndi://jdbc/jreport-realmtables#schema=db2admin`

If you are using Sybase, you must use capital letters in the schema name, for example, ABCDE.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009771601-Creating-Tables-in-a-Specified-Tablespace)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009771561-Initializing-the-Database-System-as-a-Non-admin-Database-User)
