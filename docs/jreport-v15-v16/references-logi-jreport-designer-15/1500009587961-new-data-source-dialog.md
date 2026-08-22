---
title: "New Data Source Dialog"
id: 1500009587961
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009587961-New-Data-Source-Dialog
updated_at: 2021-07-24T05:55:02Z
---

# New Data Source Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009566802-New-Dataset-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009588001-New-General-Hierarchical-Data-Source-Dialog)

# New Data Source Dialog

The New Data Source dialog appears when you select Home/File > New > Data Source, or select a data source and select New Data Source on the Catalog Manager toolbar. It helps you to create a data source by selecting a [connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009563942-Connecting-to-Your-Data-Sources) type. [See the dialog](javascript:%20void(null)).

![New Data Source dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893864599/nwdtsrc.gif)

The following are details about options in the dialog:

**Data Source Name**

Specifies the name of the new data source. Input the name directly in the text box, and make sure to follow the Java class naming rule.

**Connection Type**

Specifies the type of the connection to create in the new data source:

* **Oracle**  
   If selected, an Oracle JDBC connection will be created and data stored in the database can be accessed via the connection.
* **SQL Server**  
   If selected, an SQL Server JDBC connection will be created and data stored in the database can be accessed via the connection.
* **MySQL**  
   If selected, a MySQL JDBC connection will be created and data stored in the database can be accessed via the connection.
* **JDBC**  
   If selected, a JDBC connection will be created and data stored in JDBC database can be accessed via the connection.
* **JSON**  
   If selected, a JSON connection will be created.
* **XML**  
   If selected, an XML data source connection will be created and data stored in XML instance can be accessed via XML data transformation.
  + **Use XML as**  
     Specifies to create an XML connection as a relational one or a hierarchical one.   
    - **Relational Data Source**  
       Specifies to create an XML data source connection by transforming an XML instance.
    - **Hierarchical Data Source**  
       Specifies to import an XML hierarchical data source.
* **Hierarchical**  
   If selected, a new hierarchical data source connection will be created.
* **User Defined**   
   If selected, a new user defined data source connection will be created.
* **SOAP Web Service**  
   If selected, a new SOAP web service data source connection will be created and the data can be retrieved through a SOAP web service.
* **MongoDB**  
   If selected, a new MongoDB data source connection will be created and data stored in the data source can be accessed via data transformation.
* **HIVE**  
   If selected, a new HIVE data source connection will be created and data stored in the data source can be accessed via a JDBC connection.

**OK**

Applies the changes and closes the dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009566802-New-Dataset-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009588001-New-General-Hierarchical-Data-Source-Dialog)
