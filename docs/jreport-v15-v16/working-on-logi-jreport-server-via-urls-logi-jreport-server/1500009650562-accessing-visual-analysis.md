---
title: "Accessing Visual Analysis"
id: 1500009650562
section: "Working on Logi JReport Server via URLs Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009650562-Accessing-Visual-Analysis
updated_at: 2021-07-24T20:53:30Z
---

# Accessing Visual Analysis

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650422-Working-With-Dashboards)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009667961-Embedding-Logi-JReport-Server-Guide-v15-With-JavaScript-APIs)

# Accessing Visual Analysis

All the properties are encapsulated as JSON (JavaScript Object Notation) objects. It will help if you obtain some knowledge on JSON to understand the syntax more clearly.

Below is a list of the sections covered in this topic:

* [Creating a New Visual Analysis Session](#Create)
* [Opening an Existing Analysis Template](#Open)

## Creating a New Visual Analysis Session

**Parameters**

* jrd\_catalog={ // A ResourceDef object to describe a catalog.   
  "name":"/SampleReports/SampleReports.cat", // Required. The name and the full path of the catalog. The path could be a disk path or a server resource tree path. For the latter, it could be either in the My Reports folder (/USERFOLDERPATH/admin/) or in the Public Reports folder (/).  
  "ver":"-1", // Optional. The version number of the catalog.  
  "real":"false" // Optional. true means the catalog path is a real disk path and false means a server resource tree path. When it is a real path, "real":"true" must be specified.   
   }
* jrd\_datasource={ // A DataSource object to describe a data source.  
  "catalog":{"name":"/SampleReports/SampleReports.cat","ver":"-1","real":"false"}, // A [ResourceDef](#ResourceDef) object to describe a catalog.   
  "ds:"Data Source 1", // Data source name.  
  "query":"Query1", // Query name.  
  "bv":"WorldWideSalesBV" // Business view name.  
   }
* jrd\_catpath={"name":"/SampleReports"} // The catalog path in the server resouce tree.

**Examples**

* Create a new session with specified business view information. The data source selection panel will not pop up.

  `http://localhost:8888/webos/app/designer/run.jsp?jrd_datasource={"catalog":{"name":"/SampleReports/SampleReports.cat"},"ds":"Data Source 1","query":"WorldWideSales","bv":"WorldWideSalesBV"}`
* Create a new session with specified catalog. This entry will pop data source panel and only include business views which belong to the specified catalog.

  `http://localhost:8888/webos/app/designer/run.jsp?jrd_catalog={"name":"/SampleReports/SampleReports.cat","ver":"-1","real":"false"}`
* Create a new session with specified catalog path. This entry will pop data source panel and include all catalogs and business views in them which are under the specified catalog path and its sub folders.

  `http://localhost:8888/webos/app/designer/run.jsp?jrd_catpath={"name":"/SampleReports"`}
* Create a new session without any data source information:

  `http://localhost:8888/webos/app/designer/run.jsp`

  It is equal to the following:

  `http://localhost:8888/webos/app/designer/run.jsp?jrd_catpath={"name":"/"`}

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Opening an Existing Analysis Template

**Parameter**

* jrd\_resext={   
   "active":0,  
  "reslst":[ // Specifies the analysis template to open.

```
```
{  
"name":"/SampleReports/VisualComponent 1.va", // The analysis template file name with its full path. The path could be a disk path or a server resource tree path. For the latter, it could be either in the My Reports folder (/USERFOLDERPATH/admin/) or in the Public Reports folder (/).  
      "ver":"-1", // Optional: The version number of the analysis template. -1 means the latest version.  
      "real":"false", // Optional. Value: true/false. true means the resource path is a real disk path and false means a server resource tree path. When it is a real path, "real":"true" must be specified.   
    DataSource: {



```
"catalog":{"name":"/SampleReports/SampleReports.cat","ver":"-1","real":"false"}, // A ResourceDef object to describe a catalog.   
        "ds:"Data Source 1", // Data source name.  
        "query":"Query1", // Query name.  
        "bv":"WorldWideSalesBV" // Business view name.



}
```



}



]
```



}
```

**Example**

* `http://localhost:8888/webos/app/designer/run.jsp?jrd_resext={"reslst":[{"name":"/SampleReports/VisualComponent 1.va","ver":"-1","real":"false"}],"active":"0"}`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650422-Working-With-Dashboards)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009667961-Embedding-Logi-JReport-Server-Guide-v15-With-JavaScript-APIs)
