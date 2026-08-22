---
title: "Creating Tables in a Specified Tablespace"
id: 1500009744861
section: "Configure Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009744861-Creating-Tables-in-a-Specified-Tablespace
updated_at: 2021-07-25T07:20:16Z
---

# Creating Tables in a Specified Tablespace

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744801-Configuring-in-an-Integrated-Environment)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744841-Specifying-Schemas)

# Creating Tables in a Specified Tablespace

Logi Report Server supports creating tables in a user-specified tablespace in a database that supports tablespaces, such as DB2 and Oracle. A key-value pair tablespace is provided to specify a tablespace into which Logi Report Server will create database tables. This key-value pair is then passed to Logi Report Server through the JDBC configuration. Logi Report Server retrieves the tablespace information from the JDBC (data source) configuration, and then creates tables in the specified tablespace.

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744801-Configuring-in-an-Integrated-Environment)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744841-Specifying-Schemas)
