---
title: "Specifying DBMS Schemas"
id: 5741395949719
section: "Configuring Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741395949719-Specifying-DBMS-Schemas
updated_at: 2022-10-31T17:16:00Z
---

# Specifying DBMS Schemas

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741387307799-Creating-Tables-in-a-Specified-Tablespace)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741387264663-Initializing-the-Database-System-as-a-Non-admin-Database-User)

# Specifying DBMS Schemas

Logi Report Server supports DBMS schemas to work well with databases that support schemas. Those DBMSs include Oracle, DB2, SQL Server, Sybase, PostgreSQL, InterSystems Caché, and EnterpriseDB. This topic describes how you can specify schema information in the **dbconfig.xml** file.

You can specify schema information in the **dbconfig.xml** file in `<install_root>\bin` by adding the <schema></schema> tags:

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741387307799-Creating-Tables-in-a-Specified-Tablespace)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741387264663-Initializing-the-Database-System-as-a-Non-admin-Database-User)
