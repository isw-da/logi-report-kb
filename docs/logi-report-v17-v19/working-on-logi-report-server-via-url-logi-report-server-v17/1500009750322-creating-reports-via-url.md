---
title: "Creating Reports via URL"
id: 1500009750322
section: "Working on Logi Report Server via URL Logi Report Server v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009750322-Creating-Reports-via-URL
updated_at: 2021-07-24T00:47:27Z
---

# Creating Reports via URL

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009778901-Scheduling-Reports-via-URL)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750302-Using-the-Authentication-Properties-in-URL)

# Creating Reports via URL

You can use URL to create reports directly. This topic describes how you can create a web report via URL, using either the traditional wizard way or the quick start way of Web Report Studio.

See [Web Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/1500009778701-Web-Report-Studio) for more information about the differences between the two ways.

This topic contains the following sections:

* [Creating a Page Report via URL](#Page)
* [Creating a Web Report in the Traditional Wizard Way via URL](#Web)
* [Creating a Web Report in the Quick Start Way via URL](#Quickstart)

## Creating a Page Report via URL

URL entry: /dhtmljsp/newreport.jsp

**Properties:**

* **jrs.catalog**  
   The catalog name with full path.
* **FromServer**  
   Optional. The value is true, and you cannot change it.
* [Authentication properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009750302-Using-the-Authentication-Properties-in-URL) (optional)
* **jrs.ds\_name**  
   Optional. The data source name in the specified catalog. If the data source is given (not null), only the business views in the data source will be shown.
* **jrs.query\_name**  
   Optional. The query name in the specified catalog. If the query name is given (not null), the step of selecting business views in the report wizard will be skipped and will not be shown as a step. The business view based on the query will be used, and the jrs.cube\_name property should be ignored.
* **jrs.cube\_name**  
   Optional. The business view name in the specified catalog, that is the Name property value of the business view in the Catalog Manager of Logi Report Designer. If the business view name is given (not null), the step of selecting business views in the report wizard will be skipped and will not be shown as a step. If there are some business views with the same name, one of them will be used.
* [jrs.param$](https://devnet.logianalytics.com/hc/en-us/articles/1500009743382-Appendix-1-URL-Properties-for-Running-Scheduling-and-Viewing-Reports-via-URL#jrsparam) (optional)
* [jrs.param\_page](https://devnet.logianalytics.com/hc/en-us/articles/1500009743382-Appendix-1-URL-Properties-for-Running-Scheduling-and-Viewing-Reports-via-URL#jrsparam_page) (optional)

**Examples:**

* `http://localhost:8888/dhtmljsp/newreport.jsp?FromServer=true&jrs.catalog=/SampleReports/SampleReports.cat`
* `http://localhost:8888/dhtmljsp/newreport.jsp?FromServer=true&jrs.catalog=%2fSampleReports%2fSampleReports.cat`

Server directs you to the New Page Report dialog box which leads you to [create a page report](https://devnet.logianalytics.com/hc/en-us/articles/1500009748862-Creating-Page-Reports#Dialog) in the specified catalog.

## Creating a Web Report in the Traditional Wizard Way via URL

URL entry: webos/app/webstudio/run.jsp?jrd\_wizard=1&

The properties are encapsulated as JSON (JavaScript Object Notation) objects:

* jrd\_catalog={  
  "name":"xxx", // The catalog name with full path.  
  "ver":-1, // Optional. The catalog version. -1 means the latest version. Default value is "-1".  
  "real":false, // Optional. If you use absolute resource path, you need to add the property *"real":true* for the path. Default value is "false".  
  "dsName":"xxx", // Optional. The data source name in the catalog. If the data source is given (not null), only the business views in this data source are shown in the report wizard.  
  "QueryName":"xxx", // Optional. The query name in the catalog. If the query name is given (not null), the selecting business view drop-down list in the report wizard will be disabled. The business view based on the query will be used, and the BVName property below should be ignored.  
  "BVName":"xxx", // Optional. The business view name in the catalog, that is the display name in the Catalog Browser of Logi Report Designer. If the business view name is given (not null), the selecting business view drop-down list in the report wizard will be disabled. If there are some business views with the same name, one of them will be used.   
  "param\_page":true // Optional. Value: true/false. Default value: true. It controls whether to show the parameter dialog box displayed during report running for specifying parameter values that are not provided by jrd.param$ in the URL. The Parameters panel in Web Report Studio is not affected by this property, because the dialog box is to display all the parameters of the report. When it is true and the value of a middle level cascading parameter (including old style cascading parameter) is provided, the parameter dialog box only shows the lower level parameters. When it is false, no parameter dialog box will pop up and the given parameter values and the default values of the other parameters will be used to run the report.  
  }

* jrd\_param$={  
  "p1":"value1", // p1 is parameter name, and value1 is p1's value.  
  "p2":["value1","value2","value3"] // For multiple values.  
  }
* [Authentication properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009750302-Using-the-Authentication-Properties-in-URL): jrs.authorization, jrs.auth\_uid, and jrs.auth\_pwd // Optional.

**Examples:**

* `http://localhost:8888/webos/app/webstudio/run.jsp?jrd_wizard=1&jrd_catalog={"name":"/SampleReports/SampleReports.cat","ver":-1}`
* Real path example: `http://localhost:8888/webos/app/webstudio/run.jsp?jrd_wizard=1&jrd_catalog={"name":"E:\\LogiReport\\Server\\jreports\\SampleReports\\SampleReports.cat","real":true}`

Server directs you to the Web Report Wizard which guides you through [creating a web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009750022-Creating-Web-Reports-Using-the-Wizard#Wizard) in the specified catalog.

## Creating a Web Report in the Quick Start Way via URL

URL entry: webos/app/webstudio/run.jsp?

The properties are encapsulated as JSON (JavaScript Object Notation) objects:

* [jrd\_studio\_mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009750362-Running-Reports-via-URL#WebMode) // The Web Report Studio mode.
* [jrd\_catalog](#jrd_catalog) // Optional. The catalog path or the catalog name with full path.

**Examples:**

* `http://localhost:8888/webos/app/webstudio/run.jsp?jrd_studio_mode=edit`
* `http://localhost:8888/webos/app/webstudio/run.jsp?jrd_studio_mode=edit&jrd_catalog={"name":"/"}`
* `http://localhost:8888/webos/app/webstudio/run.jsp?jrd_studio_mode=edit&jrd_catalog={"name":"/SampleReports/SampleReports.cat"}`

Server prompts you to select data fields from a business view and then creates a table report based on the fields. However, when Web Report Studio is in the traditional way, Server creates a blank web report instead.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009778901-Scheduling-Reports-via-URL)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750302-Using-the-Authentication-Properties-in-URL)
