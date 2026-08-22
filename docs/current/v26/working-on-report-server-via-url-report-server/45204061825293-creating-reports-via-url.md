---
title: "Creating Reports via URL"
id: 45204061825293
section: "Working on Report Server via URL Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45204061825293-Creating-Reports-via-URL
updated_at: 2026-04-30T14:11:05Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Creating Reports via URL

You can use URL to create reports directly. This topic describes how you can create a web report via URL, using either the traditional wizard method or the quick start method.

See Web Report Studio for more information about the differences between the two ways. 

This topic contains the following sections:

- Creating a Page Report via URL
                

- Creating a Web Report Using the Traditional Wizard Method via URL
                

- Creating a Web Report Using the Quick Start Method via URL
                

## 
Creating a Page Report via URL

URL entry: /dhtmljsp/newreport.jsp

Properties:

- 
jrs.catalog
  The catalog name with full path.

- 
FromServer
    Optional. The value is true, and you cannot change it.   

- 
Authentication properties (optional)

- 
jrs.ds_name
    Optional. The data source name in the specified catalog. If the data source is given (not null), only the business views in the data source will be shown. 

- 
jrs.query_name
  Optional. The query name in the specified catalog. If the query name is given (not null), the step of selecting business views in the report wizard will be skipped and will not be shown as a step. The business view based on the query will be used, and the jrs.cube_name property should be ignored. 

- 
jrs.cube_name
  Optional. The business view name in the specified catalog, that is the Name property value of the business view in the Catalog Manager of Report Designer. If the business view name is given (not null), the step of selecting business views in the report wizard will be skipped and will not be shown as a step. If there are some business views with the same name, one of them will be used. 

- 
jrs.param$ (optional)

- 
jrs.param_page (optional)

 Examples:

- http://localhost:8888/dhtmljsp/newreport.jsp?FromServer=true&jrs.catalog=/SampleReports/SampleReports.cat

- http://localhost:8888/dhtmljsp/newreport.jsp?FromServer=true&jrs.catalog=%2fSampleReports%2fSampleReports.cat

Server directs you to the New Page Report dialog box which leads you to create a page report in the specified catalog.

## 
Creating a Web Report Using the Traditional Wizard Method via URL

URL entry: webos/app/webstudio/run.jsp?jrd_wizard=1&

The properties are encapsulated as JSON (JavaScript Object Notation) objects:

- 
jrd_catalog={
"name":"xxx", // The catalog name with full path.
"ver":-1, // Optional. The catalog version. -1 means the latest version. Default value is "-1".
"real":false, // Optional. If you use absolute resource path, you need to add the property "real":true for the path. Default value is "false".
"dsName":"xxx", // Optional. The data source name in the catalog. If the data source is given (not null), only the business views in this data source are shown in the report wizard.
"QueryName":"xxx", // Optional. The query name in the catalog. If the query name is given (not null), the selecting business view drop-down list in the report wizard will be disabled. The business view based on the query will be used, and the BVName property should be ignored.
"BVName":"xxx", // Optional. The business view name in the catalog, that is the display name in the Catalog Browser of Report Designer. If the business view name is given (not null), the selecting business view drop-down list in the report wizard will be disabled. If there are some business views with the same name, one of them will be used. 
"param_page":true // Optional. Value: true/false. Default value: true. It controls whether to show the parameter dialog box displayed during report running for specifying parameter values that are not provided by jrd.param$ in the URL. The Parameters panel in Web Report Studio is not affected by this property, because the dialog box is to display all the parameters of the report. When it is true and the value of a middle level cascading parameter (including old style cascading parameter) is provided, the parameter dialog box only shows the lower level parameters. When it is false, no parameter dialog box will pop up and the given parameter values and the default values of the other parameters will be used to run the report.
} 

- jrd_param$={
"p1":"value1", // p1 is parameter name, and value1 is p1's value.
"p2":["value1","value2","value3"] // For multiple values.
}

- 
Authentication properties: jrs.authorization, jrs.auth_uid, and jrs.auth_pwd // Optional.

Examples:

- http://localhost:8888/webos/app/webstudio/run.jsp?jrd_wizard=1&jrd_catalog={"name":"/SampleReports/SampleReports.cat","ver":-1}

- Real path example: http://localhost:8888/webos/app/webstudio/run.jsp?jrd_wizard=1&jrd_catalog={"name":"E:\\LogiReport\\Server\\jreports\\SampleReports\\SampleReports.cat","real":true}

Server directs you to the Web Report Wizard which guides you through creating a web report in the specified catalog.

## 
Creating a Web Report Using the Quick Start Method via URL

URL entry: webos/app/webstudio/run.jsp?

The properties are encapsulated as JSON (JavaScript Object Notation) objects:

- 
jrd_studio_mode // The Web Report Studio mode.

- 
jrd_catalog // Optional. The catalog path or the catalog name with full path. 

Examples:

- http://localhost:8888/webos/app/webstudio/run.jsp?jrd_studio_mode=edit

- http://localhost:8888/webos/app/webstudio/run.jsp?jrd_studio_mode=edit&jrd_catalog={"name":"/"}

- http://localhost:8888/webos/app/webstudio/run.jsp?jrd_studio_mode=edit&jrd_catalog={"name":"/SampleReports/SampleReports.cat"}

Server prompts you to select data fields from a business view and then creates a table report based on the fields. However, when you turn on the traditional method, Server creates a blank web report instead.
