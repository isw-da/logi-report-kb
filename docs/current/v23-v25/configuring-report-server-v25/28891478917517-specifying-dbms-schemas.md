---
title: "Specifying DBMS Schemas"
id: 28891478917517
section: "Configuring Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891478917517-Specifying-DBMS-Schemas
updated_at: 2026-02-26T02:11:18Z
source_host: docs-report.zendesk.com
---
# 
Specifying DBMS Schemas 

Report Server supports DBMS schemas to work well with databases that support schemas. Those DBMSs include Oracle, DB2, SQL Server, Sybase, PostgreSQL, InterSystems Caché, and EnterpriseDB. This topic describes how you can specify schema information in the dbconfig.xml file.

You can specify schema information in the dbconfig.xml file in <install_root>\bin by adding the <schema></schema> tags:

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
When you specify the server database using a JDBC or JNDI data source, you can also specify schema information by adding the attribute schema=schema_name in the JDBC or JNDI data source. 

- 
jdbc://[<jdbc-user>:<jdbc-password>@]<jdbc-url>[#<attribute-name=attribute-value>,]For example: 

jdbc://user:password@jdbc:odbc:jreport-realmtables#driver=sun.jdbc.odbc.JdbcOdbcDriver,schema=db2admin

- 
jndi://[<jdbc-user>:<jdbc-password>@]<datasource-name>[#<attri-name=attri-value>,]For example:

jndi://jdbc/jreport-realmtables#schema=db2admin

If you are using Sybase, you must use capital letters in the schema name, for example, ABCDE.
