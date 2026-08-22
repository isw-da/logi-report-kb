---
title: "Configuring in an Integrated Environment"
id: 1500009644482
section: "Configuring Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009644482-Configuring-in-an-Integrated-Environment
updated_at: 2021-07-24T20:55:21Z
---

# Configuring in an Integrated Environment

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009669101-Configuring-in-a-Standalone-Environment)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009669141-Creating-Tables-in-a-Specified-Tablespace)

# Configuring in an Integrated Environment

Logi JReport Server supports connecting an RDBMS to access its system data via JDBC. The JDBC configuration information is stored in the file dbconfig.xml in `<install_root>\bin`. You can create a database connection according to this configuration file. Also, with the Java EE Data Source Support feature, in a Java EE environment, Logi JReport Server can get the predefined javax.sql.DataSource by JNDI APIs.

Here, the term dsInfo is used to indicate where Logi JReport Server can obtain the JDBC connection information. It is a key-value pair. The name and value for dsInfo are defined as follows:

* The name should be: Logi JReport.datasource.<dbname>, where, <dbname> is Logi JReport Server's inner database name. It must be systemtables, realmtables, or profile. For example, the dsInfo name is Logi JReport.datasource.realmtables.
* The value should be in the form of a URL. There are three protocols supported by Logi JReport Server:
  + `file:///absolute_path_of_config_file` 

    For example: `file:///Logi JReport/Server/bin/dbconfig.xml`
  + `jdbc://[<jdbc-user:jdbc-password>@]<jdbc-url>[#<attribute-name=attribute-value>,]`

    For example: `jdbc://user:password@jdbc:odbc:Logi JReport-realmtables#driver=sun.jdbc.odbc.JdbcOdbcDriver`
  + `jndi://[<jdbc-user:jdbc-passoword>@]datasource_name[#<attribute-name=attribute-value>,]`

    For example: `jndi://jdbc/Logi JReport-realmtables`

The dsInfo can be specified in several places or levels, such as VM properties, ejb-jar.xml, web.xml and <install\_root>\bin\dbconfig.xml. The sequence to load the information is:

VM system environment > ejb-jar.xml (EAR mode) > web.xml (WAR mode) > dbconfig.xml.

**Notes:**

* The Logi JReport.ear file that Logi JReport Server creates does not specify any Java EE information. By default it will load from the dbconfig.xml file.
* There is a limitation in WebSphere. Logi JReport Server's dsInfo can be configured to the WEB-INF/web.xml with JNDI name but not RESOURCE name. JBoss works fine for either one.
* Do not use reporthome, @ or # in the JNDI name or Resource name.

The following shows specifying the dsInfo in web.xml, ejb-jar.xml, and dbconfig.xml respectively:

* [Specifying Data Source in web.xml (for the WAR Mode)](#Web)
* [Specifying Data Source in ejb-jar.xml or web.xml (for the EAR Mode)](#EAR)
* [Specifying Data Source in dbconfig.xml](#XML)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Specifying Data Source in web.xml (for the WAR Mode)

When integrating the Logi JReport Server in a WAR package, you can specify the dsInfo in the WEB-INF/web.xml file using the `<env-entry></env-entry>` or `<context-param></context-param>` tags. However, the use of the `<env-entry></env-entry>` tags is the recommended way since the tags are also supported in ejb-jar.xml (if you call the Server API in your EJB).

The following is an example of specifying the dsInfo in WEB-INF/web.xml using the `<env-entry></env-entry>` tags:

|  |
| --- |
| ``` <web-app>     ...     <env-entry>         <env-entry-name>Logi JReport.datasource.realmtables</env-entry-name>         <env-entry-value>jndi://java:/resource-name</env-entry-value>         <env-entry-type>java.lang.String</env-entry-type>     </env-entry> </web-app> ``` |

The following is an example of specifying the dsInfo in WEB-INF/web.xml using the `<context-param></context-param>` tags:

|  |
| --- |
| ``` <web-app>     <context-param>         <param-name>Logi JReport.datasource.realmtables</param-name>          <param-value>jndi://datasource_name_which_is_predefined</param-value>     </context-param>      ... </web-app> ``` |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Specifying Data Source in ejb-jar.xml or web.xml (for the EAR Mode)

When the Logi JReport Server is used with APIs by EJBs, you can specify the dsInfo either in the file ejb-jar.xml in `/META-INF` or web.xml in `/WEB-INF`.

For information about specifying a data source in the web.xml file, see [Specifying data source in web.xml (for the WAR mode)](#Web).

**Note:** If the dsInfo is stored in a Web module, you should add the Logi JReport Server context listener to the WEB-INF/web.xml file. Here is an example:

|  |
| --- |
| ```  <web-app>     <listener>         <listener-class>              jet.server.servlets.JRServerContextListener              </listnener-class>      </listener>     ...  </web-app> ``` |

You can specify the dsInfo in the META-INF/ejb-jar.xml file using the `<env-entry></env-entry>` tags. For example, here is an EJB named firstEJB which creates the Logi JReport Server instance. You can add the `<env-entry></env-entry>` tags to the EJB's configuration file - META-INF/ejb-jar.xml as follows:

|  |
| --- |
| ``` <ejb-jar>     <enterprise-beans>         <session>              <ejb-name>firstEJB</ejb-name>             ...             <env-entry>                 <env-entry-name>Logi JReport.datasource.realmtables</env-entry-name>                 <env-entry-value>jndi://java:/resource_name</env-entry-value>                 <env-entry-type>java.lang.String</env-entry-type>              </env-entry>         </session>          ...     </enterprise-beans>      ... </ejb-jar> ``` |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Specifying Data Source in dbconfig.xml

By default, Logi JReport Server assumes that Logi JReport.datasource.realmtables=file:///${rpthome}/bin/dbconfig.xml. You can specify either a JDBC or JNDI data source using the `<datasource></datasource>` tags in the dbconfig.xml file.

For details about configuring the JDBC data source, see [Configuring in a Standalone Environment](https://devnet.logianalytics.com/hc/en-us/articles/1500009669101-Configuring-in-a-Standalone-Environment).

The following is an example of specifying the JNDI data source:

|  |
| --- |
| ``` <?xml version="1.0" encoding="UTF-8"?> <dbconfig>         <workspace name="systemRealm">         <database name="systemtables">                         <datasource>jndi://datasource-name</datasource>          </database>      </workspace>      <workspace name="defaultRealm">          <database name="realmtables">              <datasource>jndi://datasource-name</datasource>          </database>      </workspace>  </dbconfig> ``` |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009669101-Configuring-in-a-Standalone-Environment)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009669141-Creating-Tables-in-a-Specified-Tablespace)
