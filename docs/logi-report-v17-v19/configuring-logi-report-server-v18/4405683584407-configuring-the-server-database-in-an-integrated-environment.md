---
title: "Configuring the Server Database in an Integrated Environment"
id: 4405683584407
section: "Configuring Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683584407-Configuring-the-Server-Database-in-an-Integrated-Environment
updated_at: 2022-01-27T07:58:31Z
---

# Configuring the Server Database in an Integrated Environment

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683583383-Configuring-the-Server-Database-in-a-Standalone-Environment)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683587479-Creating-Tables-in-a-Specified-Tablespace)

# Configuring the Server Database in an Integrated Environment

This topic describes the format of the key-value pair for specify database configuration file, and how you can specify the server database information in the System Environment, dbconfig.xml, web.xml, and ejb-jar.xml, respectively.

When you integrate Logi Report Server with an application server, by default, Logi Report Server obtains the server database information from **dbconfig.xml** in the `<server_install_root>\bin` directory. However, you can use a key-value pair to specify another database configuration file, or to specify the server database directly in a JDBC or JNDI data source.

This topic contains the following sections:

* [Format of the Key-Value Pair](#Format)
* [Specifying the Server Database in the System Environment](#JVM)
* [Specifying the Server Database in dbconfig.xml](#XML)
* [Specifying the Server Database in web.xml (for the WAR Mode)](#Web)
* [Specifying the Server Database in ejb-jar.xml or web.xml (for the EAR Mode)](#EAR)

## Format of the Key-Value Pair

The name of the key must be jreport.datasource.systemtables, jreport.datasource.realmtables, or jreport.datasource.profile, where *systemtables*, *realmtables* and *profile* are Logi Report Server's inner database names for the system database, realm database and profiling database respectively. The value should be in the form of a URL as one of the following:

* Specify the path of another database configuration file:

  `file:///absolute_path_of_config_file`

  For example: `file:///LogiReport/dbconfig.xml`, or `file://D:\dbconfig.xml`
* Specify a JDBC data source:

  `jdbc://[<jdbc-user:jdbc-password>@]<jdbc-url>[#<attribute-name=attribute-value>,]`

  For example: `jdbc://user:password@jdbc:odbc:jreport-realmtables#driver=sun.jdbc.odbc.JdbcOdbcDriver`
* Specify a JNDI data source:

  `jndi://[<jdbc-user:jdbc-passoword>@]datasource_name[#<attribute-name=attribute-value>,]`

  For example: `jndi://jdbc/jreport-realmtables`

You can specify the server database information in multiple places or levels, such as the system environment using "-D" parameters, ejb-jar.xml, web.xml, and dbconfig.xml. The sequence to load the information is:

system environment > ejb-jar.xml (EAR mode) > web.xml (WAR mode) > dbconfig.xml

## Specifying the Server Database in the System Environment

To specify the key-value pair in the system environment, add the following "-D" parameters in the Logi Report Server startup file **JRServer.bat/JRServer.sh** in the `<server_install_root>\bin` directory:

`-Djreport.datasource.profiling=file:///absolute_path_of_config_file,-Djreport.datasource.systemtables=file:///absolute_path_of_config_file,-Djreport.datasource.realmtables=file:///absolute_path_of_config_file`

## Specifying the Server Database in dbconfig.xml

You can specify either a JDBC or JNDI data source using the <datasource></datasource> tags in dbconfig.xml.

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4420453448599/criticalicon.gif) <database name> must be Logi Report Server's inner database name.

For more information, see [Method 2: Specifying a JDBC Data Source Using the <datasource></datasource> Tags](https://devnet.logianalytics.com/hc/en-us/articles/4405683583383-Configuring-the-Server-Database-in-a-Standalone-Environment#JDBC).

The following example shows how to specify a JNDI data source:

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

## Specifying the Server Database in web.xml (for the WAR Mode)

When integrating Logi Report Server in a WAR package, you can specify the key-value pair in the WEB-INF/web.xml file using the <env-entry></env-entry> or <context-param></context-param> tags. The <env-entry></env-entry> tags are better since they are also supported in ejb-jar.xml if you call the Server API in your EJB.

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

## Specifying the Server Database in ejb-jar.xml or web.xml (for the EAR Mode)

When you use Logi Report Server with APIs by EJBs, you can specify the key-value pair either in META-INF/ejb-jar.xml or [WEB-INF/web.xml](#Web).

To specify the key-value pair in META-INF/ejb-jar.xml, use the <env-entry></env-entry> tags. For example, here is an EJB named firstEJB which creates the Logi Report Server instance. You can add the <env-entry></env-entry> tags to the EJB's configuration file META-INF/ejb-jar.xml as follows:

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

If the server database information is in a Web module, you should add the Logi Report Server context listener to WEB-INF/web.xml as follows:

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

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg)

* There is a limitation in WebSphere. You can configure Logi Report Server's database information in WEB-INF/web.xml with JNDI name but not Resource name. JBoss works fine for either one.
* Do not use reporthome, @, or # in the JNDI name or Resource name.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683583383-Configuring-the-Server-Database-in-a-Standalone-Environment)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683587479-Creating-Tables-in-a-Specified-Tablespace)
