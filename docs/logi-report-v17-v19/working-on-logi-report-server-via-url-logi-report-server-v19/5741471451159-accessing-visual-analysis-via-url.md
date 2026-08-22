---
title: "Accessing Visual Analysis via URL"
id: 5741471451159
section: "Working on Logi Report Server via URL Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741471451159-Accessing-Visual-Analysis-via-URL
updated_at: 2022-10-31T17:18:40Z
---

# Accessing Visual Analysis via URL

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741491211159-Working-with-Dashboards-via-URL)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741464843927-URL-Properties-for-Running-Scheduling-and-Viewing-Reports-via-URL)

# Accessing Visual Analysis via URL

This topic describes how you can create a new visual analysis session and open an existing analysis template via URL.

All the properties are encapsulated as JSON (JavaScript Object Notation) objects. It will help if you obtain some knowledge on JSON to understand the syntax more clearly.

This topic contains the following sections:

* [Creating a New Visual Analysis Session via URL](#Create)
* [Opening an Existing Analysis Template via URL](#Open)

## Creating a New Visual Analysis Session via URL

**Parameters**

* jrd\_catalog={ // A ResourceDef object to describe a catalog.   
  "name":"/SampleReports/SampleReports.cat", // Required. The name and the full path of the catalog. The path could be a disk path or a server resource tree path. For the latter, it could be either in the Public Reports folder - "/", or in the My Reports folder - "/USERFOLDERPATH/*username*/" (change *username* to the real username with which you sign in to Logi Report Server).  
  "ver":-1, // Optional. The version number of the catalog.  
  "real":false // Optional. true means the catalog path is a real disk path and false means a server resource tree path. When it is a real path, you need to add **"real":true**.  
   }
* jrd\_datasource={ // A DataSource object to describe a data source.  
  "catalog":{"name":"/SampleReports/SampleReports.cat","ver":-1,"real":false}, // A [ResourceDef](#ResourceDef) object to describe a catalog.   
  "ds:"Data Source 1", // Data source name.
    
  "bv":"WorldWideSalesBV" // Business view name.  
   }
* jrd\_catpath={"name":"/SampleReports"} // The catalog path in the server resource tree.

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

## Opening an Existing Analysis Template via URL

**Parameter**

* jrd\_resext={   
   "active":0,  
  "reslst":[ // The analysis template you want to open.
  > {
  >
  > "name":"/SampleReports/VisualComponent 1.va", // The analysis template file name with its full path. The path could be a disk path or a server resource tree path. For the latter, it could be either in the Public Reports folder - "/", or in the My Reports folder - "/USERFOLDERPATH/*username*/" (change *username* to the real username with which you sign in to Logi Report Server).  
  >  "ver":-1, // Optional: The version number of the analysis template. -1 means the latest version.  
  >  "real":false, // Optional. Value: true/false. **true** means the resource path is a real disk path and **false** means a server resource tree path. When it is a real path, you need to add **"real":true**.   
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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741491211159-Working-with-Dashboards-via-URL)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741464843927-URL-Properties-for-Running-Scheduling-and-Viewing-Reports-via-URL)
