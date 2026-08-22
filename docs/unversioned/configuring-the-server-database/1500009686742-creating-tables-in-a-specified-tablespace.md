---
title: "Creating Tables in a Specified Tablespace"
id: 1500009686742
section: "Configuring the Server Database"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009686742-Creating-Tables-in-a-Specified-Tablespace
updated_at: 2021-11-03T06:58:26Z
---

# Creating Tables in a Specified Tablespace

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686702-Configuring-in-an-Integrated-Environment)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009712461-Specifying-Schemas)

# Creating Tables in a Specified Tablespace

Logi JReport Server supports creating tables in a user-specified tablespace in a database that supports tablespaces, such as DB2 and Oracle. A key-value pair tablespace is provided to specify a tablespace into which Logi JReport Server will create database tables. This key-value pair is then passed to Logi JReport Server through the JDBC configuration. Logi JReport Server retrieves the tablespace information from the JDBC (data source) configuration, and then creates tables in the specified tablespace.

Tablespace can be configured in the dbconfig.xml file located in `<install_root>\bin` by adding the <tablespace></tablespace> tags as follows:

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

When the server database is specified using a JDBC or JNDI data source, you can also configure tablespace by adding the attribute tablespace=table\_space\_name in the JDBC or JNDI data source.

* `jdbc://[<jdbc-user>:<jdbc-password>@]<jdbc-url>[#<attribute-name=attribute-value>,]`

  For example:

  `jdbc://user:password@jdbc:odbc:jreport-realmtables#driver=sun.jdbc.odbc.JdbcOdbcDriver,tablespace=myTablespace`
* `jndi://[<jdbc-user>:<jdbc-password>@]<datasource-name>[#<attri-name=attri-value>,]`

  For example:

  `jndi://jdbc/jreport-realmtables#tablespace=myTablespace`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686702-Configuring-in-an-Integrated-Environment)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009712461-Specifying-Schemas)
