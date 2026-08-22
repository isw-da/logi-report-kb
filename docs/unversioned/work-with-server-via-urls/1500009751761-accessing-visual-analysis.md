---
title: "Accessing Visual Analysis"
id: 1500009751761
section: "Work With Server via URLs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009751761-Accessing-Visual-Analysis
updated_at: 2021-07-25T07:18:30Z
---

# Accessing Visual Analysis

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009724982-Working-with-Dashboards)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744101-Embedding-Logi-Report-Server-Console-and-Reports-in-Your-Applications-via-JavaScript-APIs)

# Accessing Visual Analysis

This topic introduces how to create a new visual analysis session and open an existing analysis template via URL. All the properties are encapsulated as JSON (JavaScript Object Notation) objects. It will help if you obtain some knowledge on JSON to understand the syntax more clearly.

Select the following links to view the topics:

* [Creating a New Visual Analysis Session](#Create)
* [Opening an Existing Analysis Template](#Open)

## Creating a New Visual Analysis Session

**Parameters**

* jrd\_catalog={ // A ResourceDef object to describe a catalog.   
  "name":"/SampleReports/SampleReports.cat", // Required. The name and the full path of the catalog. The path could be a disk path or a server resource tree path. For the latter, it could be either in the Public Reports folder - "/", or in the My Reports folder - "/USERFOLDERPATH/*username*/" (change *username* to the real user name with which you log onto Logi Report Server).  
  "ver":-1, // Optional. The version number of the catalog.  
  "real":false // Optional. true means the catalog path is a real disk path and false means a server resource tree path. When it is a real path, *"real":true* must be specified.   
   }
* jrd\_datasource={ // A DataSource object to describe a data source.  
  "catalog":{"name":"/SampleReports/SampleReports.cat","ver":-1,"real":false}, // A [ResourceDef](#ResourceDef) object to describe a catalog.   
  "ds:"Data Source 1", // Data source name.
    
  "bv":"WorldWideSalesBV" // Business view name.  
   }
* jrd\_catpath={"name":"/SampleReports"} // The catalog path in the server resouce tree.

**Examples**

* Create a new session with specified business view information. The data source selection panel will not pop up.

  `http://localhost:8888/webos/app/designer/run.jsp?jrd_datasource={"catalog":{"name":"/SampleReports/SampleReports.cat"},"ds":"Data Source 1","bv":"WorldWideSalesBV"}`
* Create a new session with specified catalog. This entry will pop data source panel and only include business views which belong to the specified catalog.

  `http://localhost:8888/webos/app/designer/run.jsp?jrd_catalog={"name":"/SampleReports/SampleReports.cat","ver":-1,"real":false}`
* Create a new session with specified catalog path. This entry will pop data source panel and include all catalogs and business views in them which are under the specified catalog path and its subfolders.

  `http://localhost:8888/webos/app/designer/run.jsp?jrd_catpath={"name":"/SampleReports"`}
* Create a new session without any data source information:

  `http://localhost:8888/webos/app/designer/run.jsp`

  It is equal to the following:

  `http://localhost:8888/webos/app/designer/run.jsp?jrd_catpath={"name":"/"`}

## Opening an Existing Analysis Template

**Parameter**

* jrd\_resext={   
   "active":0,  
  "reslst":[ // Specifies the analysis template to open.
  > {
  >
  > "name":"/SampleReports/VisualComponent 1.va", // The analysis template file name with its full path. The path could be a disk path or a server resource tree path. For the latter, it could be either in the Public Reports folder - "/", or in the My Reports folder - "/USERFOLDERPATH/*username*/" (change *username* to the real user name with which you log onto Logi Report Server).  
  >  "ver":-1, // Optional: The version number of the analysis template. -1 means the latest version.  
  >  "real":false, // Optional. Value: true/false. true means the resource path is a real disk path and false means a server resource tree path. When it is a real path, "real":true must be specified.   
  >  DataSource: {
  >
  > > "catalog":{"name":"/SampleReports/SampleReports.cat","ver":-1,"real":false}, // A [ResourceDef](#ResourceDef) object to describe a catalog.   
  > >  "ds:"Data Source 1", // Data source name.  
  > >  "query":"Query1", // Query name.  
  > >  "bv":"WorldWideSalesBV" // Business view name.
  > >
  > > }
  >
  > }
  >
  > ]

  }

**Example**

* `http://localhost:8888/webos/app/designer/run.jsp?jrd_resext={"reslst":[{"name":"/SampleReports/VisualComponent1.va","ver":-1,"real":false}],"active":0}`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009724982-Working-with-Dashboards)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744101-Embedding-Logi-Report-Server-Console-and-Reports-in-Your-Applications-via-JavaScript-APIs)
