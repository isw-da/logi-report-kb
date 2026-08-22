---
title: "Configuring in an Integrated Environment"
id: 1500009686702
section: "Configuring the Server Database"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009686702-Configuring-in-an-Integrated-Environment
updated_at: 2021-11-03T06:58:27Z
---

# Configuring in an Integrated Environment

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686682-Configuring-in-a-Standalone-Environment)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009686742-Creating-Tables-in-a-Specified-Tablespace)

# Configuring in an Integrated Environment

This topic demonstrates how to specify the dsInfo in web.xml, ejb-jar.xml, and dbconfig.xml, respectively. When integrated with an application server, by default Logi JReport Server obtains the server database information from dbconfig.xml located in the `<server_install_root>\bin` directory. However, you can make use of a key-value pair to specify another database configuration file, or to specify the server database directly in a JDBC or JNDI data source.

Below is a list of the sections covered in this topic:

* [Format of the Key-Value Pair](#Format)
* [Specifying in the System Environment](#JVM)
* [Specifying in dbconfig.xml](#XML)
* [Specifying in web.xml (for the WAR Mode)](#Web)
* [Specifying in ejb-jar.xml or web.xml (for the EAR Mode)](#EAR)

## Format of the Key-Value Pair

The name of the key must be jreport.datasource.systemtables, jreport.datasource.realmtables or jreport.datasource.profile, where *systemtables*, *realmtables* and *profile* are Logi JReport Server's inner database names for the system database, realm database and profiling database respectively. The value should be in the form of a URL as one of the following:

* Specify the path of another database configuration file:

  `file:///absolute_path_of_config_file`

  For example: `file:///JReport/dbconfig.xml`, or `file://D:\dbconfig.xml`
* Specify a JDBC data source:

  `jdbc://[<jdbc-user:jdbc-password>@]<jdbc-url>[#<attribute-name=attribute-value>,]`

  For example: `jdbc://user:password@jdbc:odbc:jreport-realmtables#driver=sun.jdbc.odbc.JdbcOdbcDriver`
* Specify a JNDI data source:

  `jndi://[<jdbc-user:jdbc-passoword>@]datasource_name[#<attribute-name=attribute-value>,]`

  For example: `jndi://jdbc/jreport-realmtables`

The server database information can be specified in several places or levels, such as the system environment using "-D" parameters, ejb-jar.xml, web.xml and dbconfig.xml. The sequence to load the information is:

system environment > ejb-jar.xml (EAR mode) > web.xml (WAR mode) > dbconfig.xml

## Specifying in the System Environment

To specify the key-value pair in the system environment, add the following "-D" parameters in the Logi JReport Server startup file JRServer.bat/JRServer.sh in the `<server_install_root>\bin` directory:

`-Djreport.datasource.profiling=file:///absolute_path_of_config_file,-Djreport.datasource.systemtables=file:///absolute_path_of_config_file,-Djreport.datasource.realmtables=file:///absolute_path_of_config_file`

## Specifying in dbconfig.xml

You can specify either a JDBC or JNDI data source using the <datasource></datasource> tags in dbconfig.xml. Note that in dbconfig.xml, <database name> must be Logi JReport Server's inner database name.

For details about configuring a JDBC data source, see [Method 2: Specifying a JDBC Data Source Using the <datasource></datasource> Tags](https://devnet.logianalytics.com/hc/en-us/articles/1500009686682-Configuring-in-a-Standalone-Environment#JDBC).

The following shows an example of specifying a JNDI data source:

```
<?xml version="1.0" encoding="UTF-8"?>  
<dbconfig>  
    
    <workspace name="systemRealm">  
        
        <database name="systemtables">  
            
        <datasource>jndi://datasource-name</datasource>  
        </database>  
  
    </workspace>  
  
    <workspace name="defaultRealm">  
  
        <database name="realmtables">   
 
            <datasource>jndi://datasource-name</datasource>  
 
        </database>   
 
    </workspace>  
  
</dbconfig>
```

## Specifying in web.xml (for the WAR Mode)

When integrating Logi JReport Server in a WAR package, you can specify the key-value pair in the WEB-INF/web.xml file using the <env-entry></env-entry> or <context-param></context-param> tags. The <env-entry></env-entry> tags are more recommended since they are also supported in ejb-jar.xml if you call the Server API in your EJB.

The following example uses the <env-entry></env-entry> tags:

```
<web-app>  
 
    ...  
  
 
    <env-entry>  
 
        <env-entry-name>jreport.datasource.realmtables</env-entry-name>  
 
        <env-entry-value>jndi://java:/resource-name</env-entry-value>  
 
        <env-entry-type>java.lang.String</env-entry-type>  
 
    </env-entry>  
 
</web-app>
```

The following example uses the <context-param></context-param> tags:

```
<web-app>  
 
    <context-param>  
 
        <param-name>jreport.datasource.realmtables</param-name>  
  
        <param-value>jndi://datasource_name_which_is_predefined</param-value>  
 
    </context-param>  
  
    ...  
  

</web-app>
```

## Specifying in ejb-jar.xml or web.xml (for the EAR Mode)

When Logi JReport Server is used with APIs by EJBs, you can specify the key-value pair either in META-INF/ejb-jar.xml or [WEB-INF/web.xml](#Web).

To specify the key-value pair in META-INF/ejb-jar.xml, use the <env-entry></env-entry> tags. For example, here is an EJB named firstEJB which creates the Logi JReport Server instance. You can add the <env-entry></env-entry> tags to the EJB's configuration file META-INF/ejb-jar.xml as follows:

```
<ejb-jar>  
 
    <enterprise-beans>  
 
        <session>  
  
            <ejb-name>firstEJB</ejb-name>  
 
            ...  
 
            <env-entry>  
 
                <env-entry-name>jreport.datasource.realmtables</env-entry-name>  
 
                <env-entry-value>jndi://java:/resource_name</env-entry-value>  
 
                <env-entry-type>java.lang.String</env-entry-type>  
  
            </env-entry>  
 
        </session>   
 
        ...  
  

    </enterprise-beans>   
 
    ...  
  

</ejb-jar>
```

If the server database information is stored in a Web module, you should add the Logi JReport Server context listener to WEB-INF/web.xml as follows:

```
<web-app>  
 
    <listener>  
 
        <listener-class>  
 
            jet.server.servlets.JRServerContextListener  
 
        </listnener-class>  
  
    </listener>  
 
    ...   
 
</web-app>
```

**Notes:**

* There is a limitation in WebSphere. Logi JReport Server's database information can be configured in WEB-INF/web.xml with JNDI name but not Resource name. JBoss works fine for either one.
* Do not use reporthome, @ or # in the JNDI name or Resource name.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686682-Configuring-in-a-Standalone-Environment)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009686742-Creating-Tables-in-a-Specified-Tablespace)
