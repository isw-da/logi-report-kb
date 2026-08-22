---
title: "Setting Up OOJDBC Connections"
id: 1500009584841
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009584841-Setting-Up-OOJDBC-Connections
updated_at: 2021-07-24T05:55:49Z
---

# Setting Up OOJDBC Connections

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585041-Example-10-Via-RedShift)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584901-Using-XML-File-as-a-Data-Source-via-OOJDBC)

# Setting Up OOJDBC Connections

OOJDBC (Object Oriented Java Database Connection) is defined to cover an OODS (Object Oriented Data Source) with a JDBC interface. It is similar to a JDBC driver and is based on a Java application, EJB (Enterprise Java Bean), LDAP (Light Weight Directory Access Protocol), which can be defined as a database. Logi JReport has also developed a tool named Model Wizard, which you can run to import data via an OOJDBC data source.

Here is the main frame for OOJDBC:

![](https://devnet.logianalytics.com/hc/article_attachments/4404889399063/cnctn_jdbc_oojdbc.gif)

OOJDBC includes Model Wizard and OOJDBC Driver.

* **Model Wizard**  
   Open/Save model file  
   Define a Java class as a table  
   Define a method as a column  
   How to access the instance of the class
* **OOJDBC Driver**  
   Read the table/column definitions from model file  
   Return meta-data to Logi JReport  
   Construct QUERY data  
   Return record to Logi JReport

The following setopics explain how to import different kinds of data sources via OOJDBC into a Logi JReport catalog:

> * [Using XML File as a Data Source via OOJDBC](https://devnet.logianalytics.com/hc/en-us/articles/1500009584901-Using-XML-File-as-a-Data-Source-via-OOJDBC)
> * [Using Class File as a Data Source via OOJDBC](https://devnet.logianalytics.com/hc/en-us/articles/1500009584861-Using-Class-File-as-a-Data-Source-via-OOJDBC)
> * [Using CSV File as a Data Source via OOJDBC](https://devnet.logianalytics.com/hc/en-us/articles/1500009584881-Using-CSV-File-as-a-Data-Source-via-OOJDBC)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585041-Example-10-Via-RedShift)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584901-Using-XML-File-as-a-Data-Source-via-OOJDBC)
