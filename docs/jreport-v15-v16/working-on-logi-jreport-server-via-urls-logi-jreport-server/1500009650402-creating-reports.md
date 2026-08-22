---
title: "Creating Reports"
id: 1500009650402
section: "Working on Logi JReport Server via URLs Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009650402-Creating-Reports
updated_at: 2021-07-24T20:53:32Z
---

# Creating Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650522-Scheduling-Reports)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009650382-Using-the-Authentication-Properties-)

# Creating Reports

You can use URL to create reports directly. When creating a web report via URL, you can choose whether to take the standard wizard way or quick start way of Web Report Studio (select [here](https://devnet.logianalytics.com/hc/en-us/articles/1500009675101-Web-Report-Studio#Way) for details about the differences between the two ways).

Below is a list of the sections covered in this topic:

* [Creating a Page Report](#Page)
* [Creating a Web Report via Standard Wizard Way](#Web)
* [Creating a Web Report via Quick Start Way](#Quickstart)

## Creating a Page Report

URL entry: /dhtmljsp/newreport.jsp

**Properties:**

* **jrs.catalog**  
   The catalog name with full path.
* **FromServer**  
   Optional. The value is true and it cannot be changed.
* [Authentication properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009650382-Using-the-Authentication-Properties-) (optional)
* **jrs.ds\_name**  
   Optional. The data source name in the specified catalog. If the data source is given (not null), only the business views in the data source will be shown.
* **jrs.query\_name**  
   Optional. The query name in the specified catalog. If the query name is given (not null), the step of selecting business views in the report wizard will be skipped and will not be shown as a step. The business view based on the query will be used, and the jrs.cube\_name property should be ignored.
* **jrs.cube\_name**  
   Optional. The business view name in the specified catalog, that is the Name property value of the business view in the Catalog Browser of Logi JReport Designer. If the business view name is given (not null), the step of selecting business views in the report wizard will be skipped and will not be shown as a step. If there are some business views with the same name, one of them will be used.
* [jrs.param$](https://devnet.logianalytics.com/hc/en-us/articles/1500009668881-Appendix-1-URL-Properties#jrsparam) (optional)
* [jrs.param\_page](https://devnet.logianalytics.com/hc/en-us/articles/1500009668881-Appendix-1-URL-Properties#jrsparam_page) (optional)

**Examples:**

* `http://localhost:8888/dhtmljsp/newreport.jsp?FromServer=true&jrs.catalog=/SampleReports/SampleReports.cat`
* `http://localhost:8888/dhtmljsp/newreport.jsp?FromServer=true&jrs.catalog=%2fSampleReports%2fSampleReports.cat`

You will then be directed to the New Page Report dialog which leads you to [create a page report](https://devnet.logianalytics.com/hc/en-us/articles/1500009673901-Creating-Page-Reports#Dialog) in the specified catalog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Creating a Web Report via Standard Wizard Way

URL entry: webos/app/webstudio/run.jsp?jrd\_wizard=1&

The properties are encapsulated as JSON (JavaScript Object Notation) objects:

* jrd\_catalog={  
  "name":"xxx", // The catalog name with full path.  
  "ver":"-1", // Optional. The catalog version. -1 means the latest version. Default value is "-1".  
  "real":"false", // Optional. If you use absolute resource path, you need to add the property "real":"true" for the path. Default value is "false".  
  "dsName":"xxx", // Optional. The data source name in the catalog. If the data source is given (not null), only the business views in this data source are shown in the report wizard.  
  "QueryName":"xxx", // Optional. The query name in the catalog. If the query name is given (not null), the selecting business view drop-down list in the report wizard will be disabled. The business view based on the query will be used, and the BVName property below should be ignored.  
  "BVName":"xxx", // Optional. The business view name in the catalog, that is the display name in the Catalog Browser of Logi JReport Designer. If the business view name is given (not null), the selecting business view drop-down list in the report wizard will be disabled. If there are some business views with the same name, one of them will be used.   
  "param\_page":"true" // Optional. Value: true/false. Default value: true. It controls whether to show the parameter dialog displayed during report running for specifying parameter values that are not provided by jrd.param$ in the URL. The Parameters panel in Web Report Studio is not affected by this property, because the dialog is to display all the parameters of the report. When it is true and the value of a middle level cascading parameter (including old style cascading parameter) is provided, the parameter dialog only shows the lower level parameters. When it is false, no parameter dialog will pop up and the given parameter values and the default values of the other parameters will be used to run the report.  
  }

* jrd\_param$={  
  "p1":"value1", // p1 is parameter name, and value1 is p1's value.  
  "p2":["value1","value2","value3"] // For multiple values.  
  }
* [Authentication properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009650382-Using-the-Authentication-Properties-): jrs.authorization, jrs.auth\_uid, and jrs.auth\_pwd // Optional.

**Examples:**

* `http://localhost:8888/webos/app/webstudio/run.jsp?jrd_wizard=1&jrd_catalog={"name":"/SampleReports/SampleReports.cat","ver":"-1"}`
* Real path example: `http://localhost:8888/webos/app/webstudio/run.jsp?jrd_wizard=1&jrd_catalog={"name":"E:\\Logi JReport\\Server\\Logi JReports\\SampleReports\\SampleReports.cat","real":"true"}`

You will then be directed to the Web Report Wizard which guides you through [creating a web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009675141-Standard-Way-of-Report-Creation-Using-Wizard#Wizard) in the specified catalog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Creating a Web Report via Quick Start Way

URL entry: webos/app/webstudio/run.jsp?

The properties are encapsulated as JSON (JavaScript Object Notation) objects:

* [jrd\_studio\_mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009650502-Specifying-the-Report-Studio-Mode) // Specifies which Web Report Studio mode is available.
* [jrd\_catalog](#jrd_catalog) // Optional. Specifies the catalog path or the catalog name with full path.

**Examples:**

* `http://localhost:8888/webos/app/webstudio/run.jsp?jrd_studio_mode=edit`
* `http://localhost:8888/webos/app/webstudio/run.jsp?jrd_studio_mode=edit&jrd_catalog={"name":"/"}`
* `http://localhost:8888/webos/app/webstudio/run.jsp?jrd_studio_mode=edit&jrd_catalog={"name":"/SampleReports/SampleReports.cat"}`

You will then be prompted to select data fields from a business view and a table report will be created based on the fields. However when Web Report Studio is in the standard way, a blank web report will be created instead.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650522-Scheduling-Reports)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009650382-Using-the-Authentication-Properties-)
