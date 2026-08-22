---
title: "Specifying Schemas"
id: 1500009744841
section: "Configure Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009744841-Specifying-Schemas
updated_at: 2021-07-25T07:20:16Z
---

# Specifying Schemas

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744861-Creating-Tables-in-a-Specified-Tablespace)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744821-Initializing-the-Database-System-as-a-Non-admin-Database-User)

# Specifying Schemas

Logi Report Server supports DBMS schemas in order to work well with databases that support schemas. Those DBMSs include Oracle, DB2, SQL Server, Sybase, PostgreSQL, InterSystems Caché and EnterpriseDB. You can specify schema information in the dbconfig.xml file located in `<install_root>\bin` by adding the <schema></schema> tags as follows:

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

When the server database is specified using a JDBC or JNDI data source, you can also specify schema information by adding the attribute schema=schema\_name in the JDBC or JNDI data source.

* `jdbc://[<jdbc-user>:<jdbc-password>@]<jdbc-url>[#<attribute-name=attribute-value>,]`

  For example:

  `jdbc://user:password@jdbc:odbc:jreport-realmtables#driver=sun.jdbc.odbc.JdbcOdbcDriver,schema=db2admin`
* `jndi://[<jdbc-user>:<jdbc-password>@]<datasource-name>[#<attri-name=attri-value>,]`

  For example:

  `jndi://jdbc/jreport-realmtables#schema=db2admin`

If you are using Sybase, the schema name must use capital letters, for example, ABCDE.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744861-Creating-Tables-in-a-Specified-Tablespace)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744821-Initializing-the-Database-System-as-a-Non-admin-Database-User)
