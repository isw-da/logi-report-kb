---
title: "Creating Tables in a Specified Tablespace"
id: 1500009771601
section: "Configuring the Server Database"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009771601-Creating-Tables-in-a-Specified-Tablespace
updated_at: 2021-07-24T00:49:27Z
---

# Creating Tables in a Specified Tablespace

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009743642-Configuring-the-Server-Database-in-an-Integrated-Environment)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009743682-Specifying-DBMS-Schemas)

# Creating Tables in a Specified Tablespace

Logi Report Server supports creating tables in a user-specified tablespace in a database that supports tablespaces, such as DB2 and Oracle. This topic describes how you can configure tablespace in the **dbconfig.xml** file.

You can use a key-value pair tablespace to specify a tablespace into which Logi Report Server will create database tables. This key-value pair is then passed to Logi Report Server through the JDBC configuration. Logi Report Server retrieves the tablespace information from the JDBC (data source) configuration, and then creates tables in the specified tablespace.

You can configure tablespace in the **dbconfig.xml** file in `<install_root>\bin` by adding the <tablespace></tablespace> tags as follows:

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

When you specify the server database using a JDBC or JNDI data source, you can also configure tablespace by adding the attribute **tablespace=table\_space\_name** in the JDBC or JNDI data source.

* `jdbc://[<jdbc-user>:<jdbc-password>@]<jdbc-url>[#<attribute-name=attribute-value>,]`

  For example:

  `jdbc://user:password@jdbc:odbc:jreport-realmtables#driver=sun.jdbc.odbc.JdbcOdbcDriver,tablespace=myTablespace`
* `jndi://[<jdbc-user>:<jdbc-password>@]<datasource-name>[#<attri-name=attri-value>,]`

  For example:

  `jndi://jdbc/jreport-realmtables#tablespace=myTablespace`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009743642-Configuring-the-Server-Database-in-an-Integrated-Environment)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009743682-Specifying-DBMS-Schemas)
