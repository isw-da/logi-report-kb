---
title: "Working with Dashboards via URL"
id: 1500009750342
section: "Working on Logi Report Server via URL Logi Report Server v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009750342-Working-with-Dashboards-via-URL
updated_at: 2021-07-24T00:47:27Z
---

# Working with Dashboards via URL

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750382-Working-with-Server-via-URL)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750402-Accessing-Visual-Analysis-via-URL)

# Working With Dashboards via URL

Similar to reports, you can create or run dashboards directly from your application. This topic describes how you can use URL to create and open dashboards, access a dashboard as the server home page, and open both dashboards and reports in one URL.

JDashboard uses `/{context_root}/dashboard/app/entry/run.jsp` as the URL entry. Here {context\_root} is the servlet's context root when deployed in a WAR or EAR file as a servlet.

This topic contains the following sections:

* [Creating a New Dashboard via URL](#Create)
* [Visiting a Dashboard as the Server Home Page via URL](#Visit)
* [Opening Specific Dashboards via URL](#Open)
* [Opening Dashboards and Reports via One URL](#One)

## Creating a New Dashboard via URL

To create a new dashboard from URL, simply use `/{context_root}/dashboard/app/entry/run.jsp`.

For example, run the URL `http://localhost:8888/dashboard/app/entry/run.jsp`, and JDashboard will be opened with a new blank dashboard in it. You can then begin to [build your dashboards](https://devnet.logianalytics.com/hc/en-us/articles/1500009771761-Creating-and-Saving-Dashboards).

## Visiting a Dashboard as the Server Home Page via URL

After you set a dashboard [as the Server Console home page](https://devnet.logianalytics.com/hc/en-us/articles/1500009771801-General-Operations-in-JDashboard#HomePage), you can use a URL to access the home page.

Property: jrd\_lastsession  
Value: true/false  
Examples:

* `http://localhost:8888/dashboard/app/entry/run.jsp?jrd_lastsession=true`
* `http://<IP>:<port>/jreport/dashboard/app/entry/run.jsp?jrd_lastsession=true`, here jreport is the servlet context root.

## Opening Specific Dashboards via URL

Logi Report provides properties for developer users to run dashboards via URL. Some properties are encapsulated as JSON (JavaScript Object Notation) objects. Therefore, it will help if you obtain some knowledge on JSON to understand the syntax more clearly. When composing the URL, you need to use URL encoding to avoid errors. To encode URLs by JavaScript, you should use the function **encodeURI**.

* jrd\_resext={  
  "active":0, // The index number of the dashboard that will be active once JDashboard is loaded. 0 means the first dashboard specified in the value list of the property "reslst", 1 the second dashboard, 2 the third, and so on.   
  "reslst":[   
   // The dashboards you want to open. The order of the dashboards specified here reflects the order they are displayed in JDashboard.  
  > {  
  >  "name":"DashboardFileNameWithFullPath", // The dashboard file name with its full path. The path could be a disk path or a server resource tree path. For the latter, it could be either in the Public Reports folder - "/", or in the My Reports folder - "/USERFOLDERPATH/*username*/" (change *username* to the real user name with which you log onto Logi Report Server).  
  >  "ver":-1, // Optional. The version number of the dashboard. -1 means the latest version.  
  >  "real":false, // Optional. Value: true/false. "true" means the resource path is a real disk path and "false" means a server resource tree path. When it is a real path, "real":true must be specified.   
  >  "type":40, // Indicates it
  > is a dashboard.  
  >  "param\_page":true, // Optional. Value: true/false. It specifies whether to pop up the parameter dialog box if the dashboard uses parameters.   
  > "dsh\_params":[  
  >  // The parameter values used in the dashboard.

  > > {  
  > > "lc\_names":["lc1","lc2",...], // Optional. lc1 and lc2 can be either of the following:
  > >
  > > + The names of the library components in the dashboard, with full path in the server resource tree, either in the Public Components folder - "/COMPONENT\_LIB/", or in the My Components folder - "/USERFOLDERPATH/*username*/" (change *username* to the real user name with which you log onto Logi Report Server). For example, /COMPONENT\_LIB/SampleReports/Sales Bar.lc, /USERFOLDERPATH/admin/Shipments Table.lc
  > > + The IDs of the library components. The ID of a library component can be known in the library component's About panel. To access the panel, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404880135063/btn_dshbrd_more.gif) on the title bar of the library component and select About from the drop-down list.
  > >
  > > "jrd\_params":{"parameter1":"value1","parameter2":["value1","value2",...]} // If lc\_names and jrd\_params are specified together, the parameters here are applied to the library components given by lc\_names, otherwise to the dashboard. When both dashboard level and library component level parameters exist in the URL, the order to apply parameters will be: the dashboard first, and then the library components. When several library components are the same in the dashboard, the parameters specified to one of them will also work on the others. In the case when the URL does not specify parameters for a specific library component but the dashboard level parameters are available, if later a new library component is added into the dashboard, it will use the parameter values in the URL. When a library component is set to use a new connection in the URL, then when adding it into the current dashboard, the library component uses the new connection.
  > >
  > > }

  > ],
  >
  > "dsh\_datasources":[  
  >  // The data source used in the dashboard.

  > > {   
  > > ["lc\_names"](#lc_names):["lc1","lc2",...], // Optional.  
  > > "jrd\_datasources":[{datasource1},{datasource2},...] // If lc\_names and jrd\_datasources are specified together, the data sources here are applied to the library components given by lc\_names, otherwise to the dashboard. When both dashboard level and library component level data sources exist
  > > in the URL, the order to apply data sources will be: the dashboard first, and then the library components. When several library components are the same in the dashboard, the data source specified to one of them will also work on the others. The property "ds" is optional. If "ds" is not specified, the new connection here applies to all involved data sources. If "ds" is specified, the new connection applies only to the same data source as that specified by "ds".
  > >
  > > }

  > ],
  >
  > "dsh\_filters":{

  > > "osf":[   
  > > // Values of the on-screen filters in the dashboard. There are two ways to designate an on-screen filter. One is by the field that is bound with the filter (recommended) and the other by the instance name of the filter.

  > > > {  
  > > > "field":{   
  > > >  // A field that is bound with an on-screen filter and the values of the field.
  > > >
  > > > > "type":2, // Indicates that the data resource type is business view.  
  > > > >  "ds":"DataSource 1", // The data source name.
  > > > >   
  > > > >  "bv":"BV 1", // The business view name.  
  > > > >  "name":"Customers.Country" // The qualified display name of the field.

  > > > },   
  > > >  "reverse":false, // Optional. If true, the values of the field are those not specified in the "values" property below.  
  > > >  "selectAll":false, // Optional. If true, it means to apply all the values at runtime and ignore the "values" property below.  
  > > >  "values":["USA","China"] // The values of the field.  
  > > >  },
  > > >
  > > > {   
  > > > // An on-screen filter and its values.
  > > >
  > > > "name":"fc1", // The instance name of an on-screen filter. For a runtime filter control, that is a filter control created in JDashboard, the name is a fixed value "RFC". When there are more than one runtime filter control in the dashboard, you need to specify the "lc\_names" property below to avoid empty data components, because runtime filter controls have the same instance name, and if library components are not specified, the values specified by the "values" property below will be applied to all the runtime filter controls in the dashboard and this will result in that the runtime on-screen filters the value lists of which do not contain the specified values retrieve no data to the corresponding data components.  
  > > > "reverse":false, // Optional. If true, the values of the on-screen filter are those not specified in the "values" property below.  
  > > > "selectAll":false, // Optional. If true, it means to apply all the values at runtime and ignore the "values" property below.  
  > > > ["lc\_names"](#lc_names):["lc1","lc2",...], // Optional. The library components to which the on-screen filter belongs. If the property is not provided, the scope is the dashboard.  
  > > > "values":["USA","China"] // The values of the on-screen filter.  
  > > >  },

  > > ]

  > }
  >
  > },
  >
  > ... // You can specify more dashboards following the above format.

  ]

  }
* jrd\_dashboard\_mode  
   // Optional. The mode available in JDashboard. The value could be:
  + view - Opens JDashboard in the view mode. [Execute permission](https://devnet.logianalytics.com/hc/en-us/articles/1500009778641-Managing-Permissions) is required.
  + edit - Opens JDashboard in the edit mode. [Edit permission](https://devnet.logianalytics.com/hc/en-us/articles/1500009778641-Managing-Permissions) is required.If you do not have the corresponding permission on the dashboard, the dashboard will fail to run. When this property is not provided in the URL, the [default mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009743782-Configuring-Server-Profile#JDashboardMode) of JDashboard specified in the server profile will be applied.
* jrd\_responsive  
  // Optional. Set this property to **false** to turn off [Responsive View](https://devnet.logianalytics.com/hc/en-us/articles/1500009771801-General-Operations-in-JDashboard#Responsive) in the view mode of JDashboard on computers.
* jrd\_userinfo={ // Optional.  
   "user":"xxx", // User name.  
   "country":"us", // The locale that represents the region part for running dashboards, following locale naming specification.  
   "language":"en", // The locale that represents the language part for running dashboards, following locale naming specification.  
   "encoding":"UTF-8", // The encoding for running dashboards.  
   "resolution":"96" // The resolution for displaying dashboards.  
  ![Marks content and feature updates for Logi Report v17.1. New feature new content.](https://devnet.logianalytics.com/hc/article_attachments/4404885305367/___newv17.1.jpg "New for Logi Report v17.1.")"prefer":{  
    "rpt\_timezone":"CST" // The time zone for displaying date and time in dashboards.  
    }  
   }
* catalog\_security=[  
   // Optional. The [security file](https://devnet.logianalytics.com/hc/en-us/articles/1500009778541-Dynamic-Security) you want to apply to a catalog when running dashboard.
  > {
  >
  > "catalog\_name":"resource path of the catalog",  
  >  "security\_file\_name":"name of the security file"
  >
  > }

  ]

**Examples:**

* `http://localhost:8888/dashboard/app/entry/run.jsp?jrd_resext={"active":0,"reslst":[{"name":"/SampleReports/Dashboard - Sales by Country.dsh","ver":-1}]}`
* `http://<IP>:<port>/jreport/dashboard/app/entry/run.jsp?jrd_resext={"active":0,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard 1.dsh","ver":-1}]}`, here jreport is the servlet context root.
* `http://localhost:8888/dashboard/app/entry/run.jsp?jrd_resext={"active":1,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard 2.dsh"},{"name":"/USERFOLDERPATH/admin/Dashboard 1.dsh"}]}`

  In this case, JDashboard displays Dashboard 2.dsh and Dashboard 1.dsh following the order from left to right, and Dashboard 1.dsh is active by default.
* `http://localhost:8888/dashboard/app/entry/run.jsp?jrd_resext={"active":1,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard 2.dsh"},{"name":"/USERFOLDERPATH/admin/Dashboard 1.dsh"}]}&jrd_dashboard_mode=view`

  The difference between this example and the second one above is that this URL runs JDashboard in the view mode while the above example runs JDashboard in the mode set in the server preference.
* Set parameters for dashboard only:

  `http://localhost:8888/dashboard/app/entry/run.jsp?jrd_resext={"active":0,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard 1.dsh","dsh_params":[{"jrd_params":{"P_StartDate":"01/01/2006","P_EndDate":"12/31/2007"}}]}]}`
* Set parameters for library components only:

  `http://localhost:8888/dashboard/app/entry/run.jsp?jrd_resext={"active":0,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard 1.dsh","dsh_params":[{"lc_names":["/COMPONENT_LIB/SampleReports/Country Sales by Category.lc","/COMPONENT_LIB/SampleReports/Sales Bar.lc"],"jrd_params":{"P_StartDate":"01/01/2006","P_EndDate":"12/31/2007"}}]}]}`
* Set parameters for both dashboard and library components:

  `http://localhost:8888/dashboard/app/entry/run.jsp?jrd_resext={"active":0,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard 1.dsh","dsh_params":[{"jrd_params":{"P_StartDate":"01/01/2006","P_EndDate":"12/31/2007"}},{"lc_names":["/COMPONENT_LIB/SampleReports/Country Sales by Category.lc","/COMPONENT_LIB/SampleReports/Sales Bar.lc"],"jrd_params":{"P_StartDate":"01/01/2006","P_EndDate":"12/31/2007"}}]}]}`
* Set on-screen filter values:

  `http://localhost:8888/dashboard/app/entry/run.jsp?jrd_resext={"active":0,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard 1.dsh","dsh_filters":{"osf":[{"field":{"type":2,"ds":"DataSource 1","bv":"BV 1","name":"Customers.Country"},"values":["USA","China"]}]}}]}`
* Run a dashboard from the real path:

  `http://localhost:8888/dashboard/app/entry/run.jsp?jrd_resext={"active":0,"reslst":[{"name":"/home/admin/Jinfonet/Server/history/1/admin959238972/demo1.dsh","ver":-1,"real":true}]}&jrs.authorization=YWRtaW46YWRtaW4%3D`
* Run a dashboard with a security file:

  `http://localhost:8888/dashboard/app/entry/run.jsp?jrd_resext={"active":1,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard 1.dsh"}]}&catalog_security=[{"catalog_name":"/USERFOLDERPATH/admin/demo.cat","security_file_name":"demo.xml"}]`
* ![Marks content and feature updates for Logi Report v17.1. New feature new content.](https://devnet.logianalytics.com/hc/article_attachments/4404885305367/___newv17.1.jpg "New for Logi Report v17.1.")Run a dashboard with time zone:

  `http://localhost:8888/dashboard/app/entry/run.jsp?jrd_resext={"active":1,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard 1.dsh"}]}&jrd_userinfo={"prefer":{"rpt_timezone":"CST"}}`
* Run a dashboard using another data source connection:

  `http://localhost:8888/dashboard/app/entry/run.jsp?jrd_resext={"active":0,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard 1.dsh","dsh_datasources":[{"jrd_datasources":[{"ds":"Data Source 1","uid":"test","pwd":"1234","type":0,"url":"jdbc:oracle:thin:@127.0.0.1:1521:ora8i","driver":"oracle.jdbc.driver.OracleDriver"}]},{"lc_names":["/COMPONENT_LIB/SampleReports/Country Sales by Category.lc","/COMPONENT_LIB/SampleReports/Sales Bar.lc"],"jrd_datasources":[{"ds":"Data Source 1","uid":"test","pwd":"1234","type":0, "url":"jdbc:oracle:thin:@127.0.0.1:1521:ora8i","driver":"oracle.jdbc.driver.OracleDriver"}]}]}]}`

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)In the case when the URL does not specify a data source connection for a specific library component but a dashboard level connection is available, if later you add a new library component into the dashboard, it will use the connection in the URL.

## Opening Dashboards and Reports via One URL

It is similar to opening multiple dashboards.

jrd\_resext={

> "active":0, // The index number of the dashboard/report that will be active once JDashboard is loaded. 0 means the first dashboard/report specified in the value list of the property "reslst", 1 the second, 2 the third, and so on.   
>  "reslst":[
>
> // The dashboards and reports you want to open. The order of them specified here reflects the order they are displayed in JDashboard.
>
> {

> > "name":"ResourceFileNameWithFullPath", // The dashboard/report file name with its full path. The path could be a disk path or a server resource tree path. For the latter, it could be either in the My Reports folder (/USERFOLDERPATH/admin/) or in the Public Reports folder (/).  
> >  "ver":-1, // Optional: The version number of the dashboard/report. -1 means the latest version.  
> >  "real":false, // Optional. Value: true/false. true means the resource path is a real disk path and false means a server resource tree path. When it is a real path, "real":true must be specified.   
> >  "type":xx, // Indicates the type of the resource. Value: 40/44/45. 40 means it
> > is a dashboard, 44 a web report, and 45 a page report.   
> >  "param\_page":true, // Optional. Value: true/false. It specifies whether to pop up the parameter dialog box if the report uses parameters.   
> >  "dependence":{ // For reports only.
> >
> > > "catalog":{ // The catalog of the report.
> > >
> > > > "name":"ResourcePath/CatalogName", // The resource path of the catalog used by the report. It could be a disk path or a server resource tree path.  
> > > >  "ver":-1, // Optional. The version number of the catalog. -1 means the latest version.  
> > > >  "real":false // Optional. "true" means the resource path is a real disk path and "false" means a server resource tree path.
> > >
> > > }
> >
> > },  
> >  "[dsh\_datasources](#dsh_datasources)":[  
> >  // The data source used in the dashboard/report. For a dashboard, one or more groups can be specified. For a report, only one can be specified.

> > > {
> > >
> > > "lc\_names":["lc1","lc2",...], // Optional. Only for dashboards.   
> > >  "jrd\_datasources":[{datasource1},{datasource2},...] // See [Opening Web Reports in Web Report Studio Via JSON](https://devnet.logianalytics.com/hc/en-us/articles/1500009750362-Running-Reports-via-URL#JSON)for more information about using the property for web report.
> > >
> > > }
> >
> > ],
> >
> > "[dsh\_params](#dsh_params)":[  
> >  // The parameter values used in the dashboard/report. For a dashboard, one or more groups can be specified. For a report, only one can be specified.

> > > {
> > >
> > > "lc\_names":["lc1","lc2",...], // Optional. Only for dashboards.   
> > >  "jrd\_params":{"parameter1":"value1","parameter2":["value1","value2",...]}
> > >
> > > }
> >
> > ]
>
> },
>
> > ...
>
> // Another way to specify a report to open.
>
> {

> > "name":"a part of running report URL", // A part of a URL as the value. The URL should be the one used for running the report via the tryView.jsp or runReport.jsp. The value extracts the URL part started with "tryView.jsp" or "runReport.jsp" and encodes the URL reserved words such as "?" and "&". For example, the extracted original URL is "tryView.jsp?jrs.cmd=jrs.try\_vw&jrs.report=%2fSampleReports%2fShipment Status Report.wls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result\_type=8", the encoded URL that can be set as the value will be "tryView.jsp%3Fjrs.cmd%3Djrs.try\_vw%26jrs.report%3D%2FSampleReports%2FShipment Status Report.wls%26jrs.catalog%3D%2FSampleReports%2FSampleReports.cat%26jrs.result\_type%3D8".  
> >  "type":46/47 // The type of the report. Value: 46/47. 46 means it is a web report, 47 a page report.
>
> }
>
> ]

}

**Examples:**

* Open a dashboard and a report:

  `http://localhost:8888/dashboard/app/entry/run.jsp?jrd_resext={"active":1,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard 2.dsh","ver":-1},{"name":"/SampleReports/Shipment Status Report.wls","ver":-1,"type":44,"param_page":true,"dependence":{"catalog":{"name":"/SampleReports/SampleReports.cat","ver":-1}}}]}&jrs.authorization=YWRtaW46YWRtaW4%3D`
* Open a dashboard, a web report, and a page report:

  `http://localhost:8888/dashboard/app/entry/run.jsp?jrd_resext={"active":1,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard 2.dsh","ver":-1},{"name":"/SampleReports/Sales Detail Report.wls","ver":-1,"type":44,"dependence":{"catalog":{"name":"/SampleReports/SampleReports.cat","ver":-1}}},{"name":"/SampleReports/Payroll Report.cls","ver":-1,"type":45,"dependence":{"catalog":{"name":"/SampleReports/SampleReports.cat","ver":-1}}}]}&jrs.authorization=YWRtaW46YWRtaW4%3D`
* Open two dashboards and a report in the view mode of JDashboard:

  `http://localhost:8888/dashboard/app/entry/run.jsp?jrd_resext={"active":0,"reslst":[{"name":"%2fSampleReports%2fPayroll Report.cls","ver":-1,"real":false,"type":45},{"name":"/SampleReports/Dashboard - Medicare.dsh","ver":-1},{"name":"%2fSampleReports%2fCoffee%20Sales.wls","ver":-1,"real":false,"type":44}]}&jrd_dashboard_mode=view&jrs.authorization=YWRtaW46YWRtaW4%3D`
* Open a dashboard by specifying the name and path and two reports by specifying the URL:

  `http://localhost:8888/dashboard/app/entry/run.jsp?jrd_resext={"active":1,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard 2.dsh","ver":-1},{"name":"tryView.jsp%3Fjrs.cmd%3Djrs.try_vw%26jrs.report%3D%2FSampleReports%2FShipment Status Report.wls%26jrs.catalog%3D%2FSampleReports%2FSampleReports.cat%26jrs.result_type%3D8","type":46},{"name":"tryView.jsp%3Fjrs.cmd%3Djrs.try_vw%26jrs.report%3D%2fSampleReports%2fCorporate+Overview.cls%26jrs.catalog%3D%2fSampleReports%2fSampleReports.cat%26jrs.result_type=8","type":47}]}&jrs.authorization=YWRtaW46YWRtaW4%3D`

  `http://localhost:8888/dashboard/app/entry/run.jsp?jrd_resext={"active":1,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard 2.dsh","ver":-1},{"name":"runReport.jsp%3Fjrs.cmd%3Djrs.try_vw%26jrs.report%3D%2FSampleReports%2FShipment Status Report.wls%26jrs.catalog%3D%2FSampleReports%2FSampleReports.cat%26jrs.result_type%3D8","type":46},{"name":"runReport.jsp%3Fjrs.cmd%3Djrs.try_vw%26jrs.report%3D%2fSampleReports%2fCorporate+Overview.cls%26jrs.catalog%3D%2fSampleReports%2fSampleReports.cat%26jrs.result_type=8","type":47}]}&jrs.authorization=YWRtaW46YWRtaW4%3D`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750382-Working-with-Server-via-URL)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750402-Accessing-Visual-Analysis-via-URL)
