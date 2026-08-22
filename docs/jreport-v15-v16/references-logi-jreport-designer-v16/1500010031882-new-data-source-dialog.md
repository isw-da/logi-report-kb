---
title: "New Data Source Dialog"
id: 1500010031882
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010031882-New-Data-Source-Dialog
updated_at: 2021-07-24T10:38:35Z
---

# New Data Source Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010031902-New-Dataset-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010067221-New-General-Hierarchical-Data-Source-Dialog)

# New Data Source Dialog

The New Data Source dialog helps you to [create a data source in the current catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500010063141-Creating-Opening-and-Saving-Catalogs#DataSource) and select the type for the first connection in the data source. It appears when you select Home/File > New > Data Source, or select a data source and select New Data Source on the Catalog Manager toolbar.

![New Data Source dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909167895/nwdtsrc.gif)

The following are details about options in the dialog:

**Data Source Name**

Specifies the name of the new data source. Input the name directly in the text box, and make sure to follow the Java class naming rule.

**Connection Type**

Specifies the type of the first [connection](https://devnet.logianalytics.com/hc/en-us/articles/1500010029402-Data-Source-Connections) to create in the new data source:

* **Oracle**  
   Creates a JDBC connection to retrieve data stored in an Oracle database.
* **SQL Server**  
   Creates a JDBC connection to retrieve data stored in an SQL Server database.
* **MySQL**  
   Creates a JDBC connection to retrieve data stored in a MySQL database.
* **JDBC**  
   Creates a JDBC connection to retrieve data stored in a relational database.
* **JSON**  
   Creates a JSON connection to retrieve data stored in a JSON data source.
* **XML**  
   Creates an XML connection to retrieve data stored in an XML data source.  
  + **Relational Data Source**  
     Retrieves data stored in an XML data source by transforming an XML hierarchy model to a relational model.
  + **Hierarchical Data Source**  
     Retrieves data stored in an XML data source by importing an XML hierarchical data source.
* **Hierarchical**  
   Creates a hierarchical data source.
* **User Defined**   
   Creates a user defined data source.
* **SOAP Web Service**  
   Creates a web service connection to retrieve data stored in a SOAP Web Service data source.
* **MongoDB**  
   Creates a MongoDB connection to retrieve data stored in a MongoDB database.
* **Hive**  
   Creates a JDBC connection to retrieve data from a relational database stored in a Hive data source.
* **Elasticsearch**  
   Creates an Elasticsearch connection to retrieve data from an Elasticsearch data source.

**OK**

Applies the changes and closes the dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010031902-New-Dataset-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010067221-New-General-Hierarchical-Data-Source-Dialog)
