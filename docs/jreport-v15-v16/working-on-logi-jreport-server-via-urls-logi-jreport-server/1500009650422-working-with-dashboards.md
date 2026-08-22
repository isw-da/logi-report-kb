---
title: "Working With Dashboards"
id: 1500009650422
section: "Working on Logi JReport Server via URLs Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009650422-Working-With-Dashboards
updated_at: 2021-07-24T20:53:32Z
---

# Working With Dashboards

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650442-Working-With-Page-Reports)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009650562-Accessing-Visual-Analysis)

# Working With Dashboards

Similar to reports, dashboards can be created or run directly from your application. JDashboard uses `/{context_root}/dashboard/app/entry/run.jsp` as the URL entry. Here {context\_root} is the servlet's context root when deployed in a WAR or EAR file as a servlet.

Below is a list of the sections covered in this topic:

* [Creating a New Dashboard](#Create)
* [Visiting a Dashboard as the Server Home Page](#Visit)
* [Opening Specific Dashboards](#Open)
* [Opening Dashboards and Reports via One URL](#One)

## Creating a New Dashboard

To create a new dashboard from URL, simply use `/{context_root}/dashboard/app/entry/run.jsp`.

For example, run the URL `http://localhost:8888/dashboard/app/entry/run.jsp`, and JDashboard will be opened with a new blank dashboard in it. You can then begin to [build your dashboards](https://devnet.logianalytics.com/hc/en-us/articles/1500009644642-Creating-Dashboards).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Visiting a Dashboard as the Server Home Page

After a dashboard has been [set as the user console home page](https://devnet.logianalytics.com/hc/en-us/articles/1500009644682-Setting-a-Dashboard-as-the-Server-Home-Page), you can use a URL to access the home page.

Property: jrd\_lastsession  
Value: true/false  
Examples:

* `http://localhost:8888/dashboard/app/entry/run.jsp?jrd_lastsession=true`
* `http://<IP>:<port>/Logi JReport/dashboard/app/entry/run.jsp?jrd_lastsession=true`, here Logi JReport is the servlet context root.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Opening Specific Dashboards

Logi JReport provides properties for developer users to run dashboards via URLs. Some properties are encapsulated as JSON (JavaScript Object Notation) objects. Therefore, it will help if you obtain some knowledge on JSON to understand the syntax more clearly. When composing the URL, you need to use URL encoding to avoid errors. To encode URLs by JavaScript, the function encodeURI is recommended.

* jrd\_resext={  
  "active":0, // The index number of the dashboard that will be active once the JDashboard is loaded. 0 means the first dashboard specified in the value list of the property "reslst", 1 the second dashboard, 2 the third, and so on.   
  "reslst":[   
   // Specify the dashboards to open. The order of the dashboards specified here reflects the order they are displayed in the JDashboard.

  ```
  {"name":"DashboardFileNameWithFullPath", // The dashboard file name with its full path. The path could be a disk path or a server resource tree path. For the latter, it could be either in the My Reports folder (/USERFOLDERPATH/admin/) or in the Public Reports folder (/).  
          "ver":"-1", // Optional: The version number of the dashboard. -1 means the latest version.  
          "real":"false", // Optional. Value: true/false. true means the resource path is a real disk path and false means a server resource tree path. When it is a real path, "real":"true" must be specified.   
          "type":"40", // Indicates it 
   is a dashboard.  
          "param_page":"true", // Optional. Value: true/false. Specify whether to pop up the parameter dialog if the dashboard uses parameters.   
          "dsh_params":[  
          // Specify the parameter values used in the dashboard.



  ```
  {  
  "lc_names":["lc1","lc2",...], // Optional: lc1 and lc2 can be either of the following:
  ```
  ```

  + The names of the library components in the dashboard, with full path in the server resource tree, either in the My Components folder (/USERFOLDERPATH/admin/) or in the Public Components folder (/COMPONENT\_LIB/). For example, /COMPONENT\_LIB/SampleReports/Sales Bar.lc.
  + The IDs of the library components. The ID of a library component can be known in the library component's About panel. To access the panel, hover the mouse over the component's title bar, then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920355095/btn_dshbrd_more.gif) that appears on the title bar and select About from the drop-down list.

  "jrd\_params":{"parameter1":"value1","parameter2":["value1","value2",...]} // If lc\_names and jrd\_params are specified together, the parameters here are applied to the library components given by lc\_names, otherwise to the dashboard. When both dashboard level and library component level parameters exist in the URL, the order to apply parameters will be: the dashboard first, and then the library components. When several library components are the same in the dashboard, the parameters specified to one of them will also work on the others. In the case when the URL does not specify parameters for a specific library component but the dashboard level parameters are available, if later a new library component is added into the dashboard, it will use the parameter values in the URL. When a library component is set to use a new connection in the URL, then when adding it into the current dashboard, the library component uses the new connection.

  }

  ],

  "dsh\_datasources":[  
   // Specify the data source used in the dashboard.

  ```
  {



  "lc_names":["lc1","lc2",...], // Optional.  
  "jrd_datasources":[{datasource1},{datasource2},...] // If lc_names and jrd_datasources are specified together, the data sources here are applied to the library components given by lc_names, otherwise to the dashboard. When both dashboard level and library component level data sources exist 
   in the URL, the order to apply data sources will be: the dashboard first, and then the library components. When several library components are the same in the dashboard, the data source specified to one of them will also work on the others. The property "ds" is optional. If "ds" is not specified, the new connection here applies to all involved data sources. If "ds" is specified, the new connection applies only to the same data source as that specified by "ds".



  }
  ```

  ]

  `},`

  ... // Specify more dashboards following the above format.

  ]

  }
* jrd\_dashboard\_mode  
   // Optional. Specify which mode is available in JDashboard. The value could be:
  + view - Opens JDashboard in the view mode. [Execute permission](https://devnet.logianalytics.com/hc/en-us/articles/1500009674981-Managing-Permissions) is required.
  + edit - Opens JDashboard in the edit mode. [Edit permission](https://devnet.logianalytics.com/hc/en-us/articles/1500009674981-Managing-Permissions) is required.If you do not have the corresponding permission on the dashboard, the dashboard will fail to run. When this property is not provided in the URL, the [default mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#JDashboardMode) of JDashboard specified in the server profile will be applied.
* catalog\_security=[  
   // Optional. Specify the [security file](https://devnet.logianalytics.com/hc/en-us/articles/1500009674921-Dynamic-Security) you want to apply to a catalog when running dashoard.

  ```
  {



  "catalog_name":"resource path of the catalog",  
          "security_file_name":"name of the security file"



  }
  ```

  ]

**Examples:**

* `http://localhost:8888/dashboard/app/entry/run.jsp?jrd_resext={"active":0,"reslst":[{"name":"/SampleReports/Coffee Sales Dashboard.dsh","ver":"-1"}]}`
* `http://<IP>:<port>/Logi JReport/dashboard/app/entry/run.jsp?jrd_resext={"active":0,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard 1.dsh","ver":"-1"}]}`, here Logi JReport is the servlet context root.
* `http://localhost:8888/dashboard/app/entry/run.jsp?jrd_resext={"active":1,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard 2.dsh"},{"name":"/USERFOLDERPATH/admin/Dashboard 1.dsh"}]}`

  In this case, after JDashboard is displayed, Dashboard 2.dsh and Dashboard 1.dsh are open and follow the order from left to right, and Dashboard 1.dsh is active by default.
* `http://localhost:8888/dashboard/app/entry/run.jsp?jrd_resext={"active":1,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard 2.dsh"},{"name":"/USERFOLDERPATH/admin/Dashboard 1.dsh"}]}&jrd_dashboard_mode=view`

  The difference between this example and the second one above is that this URL runs JDashboard in the view mode while the above example runs JDashboard in the mode set in the server preference.
* Set parameters for dashboard only:

  `http://localhost:8888/dashboard/app/entry/run.jsp?jrd_resext={"active":0,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard 1.dsh","dsh_params":[{"jrd_params":{"P_StartDate":"01/01/2006","P_EndDate":"12/31/2007"}}]}]}`
* Set parameters for library components only:

  `http://localhost:8888/dashboard/app/entry/run.jsp?jrd_resext={"active":0,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard 1.dsh","dsh_params":[{"lc_names":["/COMPONENT_LIB/SampleReports/Country Sales by Category.lc","/COMPONENT_LIB/SampleReports/Sales Bar.lc"],"jrd_params":{"P_StartDate":"01/01/2006","P_EndDate":"12/31/2007"}}]}]}`
* Set parameters for both dashboard and library components:

  `http://localhost:8888/dashboard/app/entry/run.jsp?jrd_resext={"active":0,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard 1.dsh","dsh_params":[{"jrd_params":{"P_StartDate":"01/01/2006","P_EndDate":"12/31/2007"}},{"lc_names":["/COMPONENT_LIB/SampleReports/Country Sales by Category.lc","/COMPONENT_LIB/SampleReports/Sales Bar.lc"],"jrd_params":{"P_StartDate":"01/01/2006","P_EndDate":"12/31/2007"}}]}]}`
* Run a dashboard from the real path:

  `http://localhost:8888/dashboard/app/entry/run.jsp?jrd_resext={"active":0,"reslst":[{"name":"/home/admin/Jinfonet/Server/history/1/admin959238972/demo1.dsh","ver":"-1","real":"true"}]}&jrs.authorization=YWRtaW46YWRtaW4%3D`
* Run a dashboard with a security file:

  `http://localhost:8888/dashboard/app/entry/run.jsp?jrd_resext={"active":1,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard .dsh"}]}&catalog_security=[{"catalog_name":"/USERFOLDERPATH/admin/demo.cat","security_file_name":"demo.xml"}]`
* Run a dashboard using another data source connection:

  `http://localhost:8888/dashboard/app/entry/run.jsp?jrd_resext={"active":0,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard 1.dsh","dsh_datasources":[{"jrd_datasources":[{"ds":"Data Source 1","uid":"test","pwd":"1234","type":"0","url":"jdbc:oracle:thin:@127.0.0.1:1521:ora8i","driver":"oracle.jdbc.driver.OracleDriver"}]},{"lc_names":["/COMPONENT_LIB/SampleReports/Country Sales by Category.lc","/COMPONENT_LIB/SampleReports/Sales Bar.lc"],"jrd_datasources":[{"ds":"Data Source 1","uid":"test","pwd":"1234","type":"0", "url":"jdbc:oracle:thin:@127.0.0.1:1521:ora8i","driver":"oracle.jdbc.driver.OracleDriver"}]}]}]}`

  **Note:** In the case when the URL does not specify a data source connection for a specific library component but a dashboard level connection is available, if later a new library component is added into the dashboard, it will use the connection in the URL.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Opening Dashboards and Reports via One URL

It is similar to opening multiple dashboards.

```
jrd_resext={
	"active":0, // The index number of the dashboard/report that will be active once the JDashboard is loaded. 0 means the first dashboard/report specified in the value list of the property "reslst", 1 the second, 2 the third, and so on.   
	"reslst":[ 
// Specify the dashboards and reports to open. The order of them specified here reflects the order they are displayed in the JDashboard. 
{
	"name":"ResourceFileNameWithFullPath", // The dashboard/report file name with its full path. The path could be a disk path or a server resource tree path. For the latter, it could be either in the My Reports folder (/USERFOLDERPATH/admin/) or in the Public Reports folder (/).  
		"ver":"-1", // Optional: The version number of the dashboard/report. -1 means the latest version.  
		"real":"false", // Optional. Value: true/false. true means the resource path is a real disk path and false means a server resource tree path. When it is a real path, "real":"true" must be specified.   
		"type":"xx", // Indicates the type of the resource. Value: 40/44/45. 40 means it is a dashboard, 44 a web report, and 45 a page report.   
		"param_page":"true", // Optional. Value: true/false. Specify whether to pop up the parameter dialog if the report uses parameters.   
		"dependence":{ // For reports only. 

		"catalog":{ // Specify the catalog of the report.
			"name":"ResourcePath/CatalogName", // The resource path of the catalog used by the report. It could be a disk path or a server resource tree path.  
			"ver":"-1", // Optional: The version number of the catalog. -1 means the latest version.  
			"real":"false" // Optional: true means the resource path is a real disk path and false means a server resource tree path.	
			}
},  
	"dsh_datasources":[  
		// Specify the data source used in the dashboard/report. For a dashboard, one or more groups can be specified. For a report, only one can be specified.
		{ 
			"lc_names":["lc1","lc2",...], // Optional. Only for dashboards.   
			"jrd_datasources":[{datasource1},{datasource2},...] // Select here for more information about using the property for web report.	
		}	
		],   
	"dsh_params":[  
		// Specify the parameter values used in the dashboard/report. For a dashboard, one or more groups can be specified. For a report, only one can be specified.
		{
			"lc_names":["lc1","lc2",...], // Optional. Only for dashboards.   
			"jrd_params":{"parameter1":"value1","parameter2":["value1","value2",...]}
		}
		]
}
...
// Another way to specify a report to open.
{
	"name":"a part of running report URL", // Specify a part of a URL as the value. The URL should be the one used for running the report via the tryView.jsp or runReport.jsp. The value extracts the URL part started with "tryView.jsp" or 
"runReport.jsp" and encodes the URL reserved words such as "?" and "&". For example, the extracted original URL is "tryView.jsp?jrs.cmd=jrs.try_vw&jrs.report=%2fSampleReports%2fShipmentStatus.wls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=8", 
the encoded URL that can be set as the value will be "tryView.jsp%3Fjrs.cmd%3Djrs.try_vw%26jrs.report%3D%2FSampleReports%2FShipmentStatus.wls%26jrs.catalog%3D%2FSampleReports%2FSampleReports.cat%26jrs.result_type%3D8". 
	"type":"46/47" // The type of the report. Value: 46/47. 46 means it is a web report, 47 a page report.
	}
	]
}
```

**Examples:**

* Open a dashboard and a report:

  `http://localhost:8888/dashboard/app/entry/run.jsp?jrd_resext={"active":1,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard 2.dsh","ver":"-1"},{"name":"/SampleReports/ShipmentStatus.wls","ver":"-1","type":"44","param_page":"true","dependence":{"catalog":{"name":"/SampleReports/SampleReports.cat","ver":"-1"}}}]}&jrs.authorization=YWRtaW46YWRtaW4%3D`
* Open a dashboard, a web report, and a page report:

  `http://localhost:8888/dashboard/app/entry/run.jsp?jrd_resext={"active":1,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard 2.dsh","ver":"-1"},{"name":"/SampleReports/Coffee Sales.wls","ver":"-1","type":"44","dependence":{"catalog":{"name":"/SampleReports/SampleReports.cat","ver":"-1"}}},{"name":"/SampleReports/Cascading Parameters.cls","ver":"-1","type":"45","dependence":{"catalog":{"name":"/SampleReports/SampleReports.cat","ver":"-1"}}}]}&jrs.authorization=YWRtaW46YWRtaW4%3D`
* Open two dashboards and a report in the view mode of JDashboard:

  `http://localhost:8888/dashboard/app/entry/run.jsp?jrd_resext={"active":0,"reslst":[{"name":"%2fSampleReports%2fBanded_Link.cls","ver":"-1","real":"false","type":"45"},{"name":"/SampleReports/Medicare Dashboard.dsh","ver":"-1"},{"name":"%2fSampleReports%2fCoffee%20Sales.wls","ver":"-1","real":"false","type":"44"}]}&jrd_dashboard_mode=view&jrs.authorization=YWRtaW46YWRtaW4%3D`
* Open a dashboard by specifying the name and path and two reports by specifying the URL:

  `http://localhost:8888/dashboard/app/entry/run.jsp?jrd_resext={"active":1,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard 2.dsh","ver":"-1"},{"name":"tryView.jsp%3Fjrs.cmd%3Djrs.try_vw%26jrs.report%3D%2FSampleReports%2FShipmentStatus.wls%26jrs.catalog%3D%2FSampleReports%2FSampleReports.cat%26jrs.result_type%3D8","type":"46"},{"name":"tryView.jsp%3Fjrs.cmd%3Djrs.try_vw%26jrs.report%3D%2fSampleReports%2fCorporate+Overview.cls%26jrs.catalog%3D%2fSampleReports%2fSampleReports.cat%26jrs.result_type=8","type":"47"}]}&jrs.authorization=YWRtaW46YWRtaW4%3D`

  `http://localhost:8888/dashboard/app/entry/run.jsp?jrd_resext={"active":1,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard 2.dsh","ver":"-1"},{"name":"runReport.jsp%3Fjrs.cmd%3Djrs.try_vw%26jrs.report%3D%2FSampleReports%2FShipmentStatus.wls%26jrs.catalog%3D%2FSampleReports%2FSampleReports.cat%26jrs.result_type%3D8","type":"46"},{"name":"runReport.jsp%3Fjrs.cmd%3Djrs.try_vw%26jrs.report%3D%2fSampleReports%2fCorporate+Overview.cls%26jrs.catalog%3D%2fSampleReports%2fSampleReports.cat%26jrs.result_type=8","type":"47"}]}&jrs.authorization=YWRtaW46YWRtaW4%3D`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650442-Working-With-Page-Reports)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009650562-Accessing-Visual-Analysis)
