---
title: "Creating Tables in a Specified Tablespace"
id: 28891504201869
section: "Configuring Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891504201869-Creating-Tables-in-a-Specified-Tablespace
updated_at: 2026-02-26T02:11:17Z
source_host: docs-report.zendesk.com
---
# 
Creating Tables in a Specified Tablespace 

Report Server supports creating tables in a user-specified tablespace in a database that supports tablespaces, such as DB2 and Oracle. This topic describes how you can configure tablespace in the dbconfig.xml file.

You can use a key-value pair tablespace to specify a tablespace into which Server will create database tables. This key-value pair is then passed to Server through the JDBC configuration. Server retrieves the tablespace information from the JDBC (data source) configuration, and then creates tables in the specified tablespace. 

You can configure tablespace in the dbconfig.xml file in <install_root>\bin by adding the <tablespace></tablespace> tags:

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
When you specify the server database using a JDBC or JNDI data source, you can also configure tablespace by adding the tablespace=table_space_name attribute in the JDBC or JNDI data source. 

- 
jdbc://[<jdbc-user>:<jdbc-password>@]<jdbc-url>[#<attribute-name=attribute-value>,]For example: 

jdbc://user:password@jdbc:odbc:jreport-realmtables#driver=sun.jdbc.odbc.JdbcOdbcDriver,tablespace=myTablespace

- 
jndi://[<jdbc-user>:<jdbc-password>@]<datasource-name>[#<attri-name=attri-value>,]For example:

jndi://jdbc/jreport-realmtables#tablespace=myTablespace
