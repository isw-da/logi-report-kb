---
title: "Creating Tables in a Specified Tablespace"
id: 5741387307799
section: "Configuring Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741387307799-Creating-Tables-in-a-Specified-Tablespace
updated_at: 2022-10-31T17:15:59Z
---

# Creating Tables in a Specified Tablespace

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741395898263-Configuring-Server-Databases-for-Server-Metadata-in-an-Integrated-Environment)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741395949719-Specifying-DBMS-Schemas)

# Creating Tables in a Specified Tablespace

Logi Report Server supports creating tables in a user-specified tablespace in a database that supports tablespaces, such as DB2 and Oracle. This topic describes how you can configure tablespace in the **dbconfig.xml** file.

You can use a key-value pair tablespace to specify a tablespace into which Server will create database tables. This key-value pair is then passed to Server through the JDBC configuration. Server retrieves the tablespace information from the JDBC (data source) configuration, and then creates tables in the specified tablespace.

You can configure tablespace in the **dbconfig.xml** file in `<install_root>\bin` by adding the <tablespace></tablespace> tags:

```
...  
<workspace name="defaultRealm">  
    <database name="realmtables">  
        <driver classpath="...">jdbc_driver_name</driver>  
        <url>jdbc_url</url>  
        <user>jdbc_user</user>  
        <password>jdbc_password</password>  
        <tablespace>table_space_name</tablespace>  
    </database>
</workspace>
```

When you specify the server database using a JDBC or JNDI data source, you can also configure tablespace by adding the **tablespace=table\_space\_name** attribute in the JDBC or JNDI data source.

* `jdbc://[<jdbc-user>:<jdbc-password>@]<jdbc-url>[#<attribute-name=attribute-value>,]`

  For example:

  `jdbc://user:password@jdbc:odbc:jreport-realmtables#driver=sun.jdbc.odbc.JdbcOdbcDriver,tablespace=myTablespace`
* `jndi://[<jdbc-user>:<jdbc-password>@]<datasource-name>[#<attri-name=attri-value>,]`

  For example:

  `jndi://jdbc/jreport-realmtables#tablespace=myTablespace`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741395898263-Configuring-Server-Databases-for-Server-Metadata-in-an-Integrated-Environment)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741395949719-Specifying-DBMS-Schemas)
