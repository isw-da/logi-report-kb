---
title: "Embedding Logi Report Server Console and Reports in Your Applications via JavaScript APIs"
id: 1500009770701
section: "Working with APIs Logi Report Server v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009770701-Embedding-Logi-Report-Server-Console-and-Reports-in-Your-Applications-via-JavaScript-APIs
updated_at: 2021-07-24T00:49:39Z
---

# Embedding Logi Report Server Console and Reports in Your Applications via JavaScript APIs

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009742982-Working-with-APIs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009770821-Using-Server-API-to-Work-with-Logi-Report-Server)

# Embedding Logi Report Server Console and Reports in Your Applications via JavaScript APIs

This topic describes how you can embed the Logi Report Server Console, page reports, web reports, and dashboards into your applications and then perform actions outside the report template, using Logi Report's JavaScript APIs.

This topic contains the following sections:

* [Embedding the Server Console in Your Application](#Console)
* [Embedding Logi Report Reports and Dashboards in Your Application](#Report)

+ [Integrating JavaScript APIs Into Your Environment](#Integ)
+ [Running the JavaScript API Demos](#Demo)
+ [Specifying Parameter Values](#Param)
+ [Using Single Sign On](#SSO)

## Embedding the Server Console in Your Application

Logi Report provides modularized RESTful Web APIs for the Logi Report Server Console so that you can call these APIs to set up a similar server console as the Logi Report Server Console in your applications on any platform such as JavaScript, Java, .NET, C++, etc. RESTful Web APIs are popular and typically based on HTTP methods to access resources via URL-encoded parameters and the use of JSON or XML to transmit data. Logi Report Web API definition is developed using [openAPI](https://www.openapis.org/) as the specification, and the Web API documents are accessible via the URL <http://localhost:8888/servlet/sendfile/help/webapi/webapi-docs/index.html> if you have a local Logi Report Server started. You can easily generate client side APIs according to the Web API definition file **logireportserver.yaml** located in the `<install_root>\help\webapi` directory. Client APIs finally call the Web APIs to a Logi Report Server.

![JavaScript API](https://devnet.logianalytics.com/hc/article_attachments/4404880583447/jsapi.gif)

Logi Report Web APIs cover the following server functions:

* **Logging in and out**  
  You can log in and out Logi Report Server, get user session information such as login user name and session ID, and set session timeout time.
* **Managing resources**  
   You can perform the following resource management tasks using the Web APIs: Listing all resources including folders, reports, library components, dashboards, and versions.

  + Creating folders in the server resource tree and publishing resources to them.
  + Getting and setting resource properties.
  + Setting and deleting resource permissions.
  + Getting, setting, and deleting catalog level, report level, and global NLS.
  + Getting all resources in the server resource tree with their properties using a single call, and obtaining parameter information of the resources.
* **Managing business view resources**  
  You can list all the business views in a catalog, including the categories, group objects, aggregation objects, and detail objects in the business views, and get, set, and delete permissions of group objects and business views.
* **Managing users, groups, and groups in the server security system**  
  You can add, remove, get, and edit users, groups, and roles, and add/remove members to/from them.
* **Scheduling report tasks and advanced running reports**  
  You can schedule tasks to run reports and send report results to various locations such as to the versioning system, to disk, to e-mail addresses, to printer, to fax, and to FTP sites, and view, enable, disable, copy, get, run, import, export, and delete the report tasks. Schedule Run and Advanced Run support all the formats including Page Report Result, Web Report Result, HTML, PDF, Excel, Text, RTF, XML, and PostScript.
* **Configuring user preferences**  
  You can get and set server preferences, and get, add, edit, and delete the profiles of Page Report Studio, Web Report Studio, and JDashboard.
* **Dynamic settings for catalogs**  
  You can get, set, create, and delete dynamic connections, dynamic security, and dynamic display names for business view elements.

The client-side JavaScript APIs are already generated in Logi Report Server for your direct use and you can find the file **javascript-client-generated.zip** in the `<install_root>\help\webapi\client-js` directory. Extract the zip file and you will get the **javascript-client** folder which contains the following: JavaScript API codes are in the **src** subfolder; for the files in the **docs** subfolder and the README file, you need to use Markdown Viewer to view them. To access the JavaScript API documents, open the file **index.html** in the `<install_root>\help\webapi\client-js\js-docs` directory.

However, for other client side APIs like Java, .NET, C++, etc., you need to generate them by yourself using the Web API definition file **logireportserver.yaml**.

You can refer to the following sample code for an example if you have a local Logi Report Server started: <http://localhost:8888/servlet/sendfile/help/webapi/client-js/sample/index.html>. You can find the complete sample materials in the `<install_root>\help\webapi\client-js\sample` directory. For the code details, view **index.js** in the **src** subfolder.

The following is a fragment of the sample code for your information:

```
    /* Get the nodes in the folder "/SampleReports". */  
  getNodesInFolder : function() {  
    var folder = "/SampleReports";  
    var callback = function(error, data, response) {  
      var $msg = $('#div_result').html("<div>test ResourceTreeApi.getNodesInFolder, folder: " + folder + "...</div>");  
      if (error) {  
        $msg.append($("<span style='color: red;'>" + error + "</span>"));  
      } else {  
        $msg.append('<div>path:/SampleReports</div>');  
        $msg.append("Done! return node size: " + data.length);  
        }  
        };  
        var opts = {  
        path: folder, // String | The server resource path, like "/SampleReports".  
        types: ["folder", "report", "catalog"] // [String] | The types of the nodes to return. Return all if there is not this parameter.  
        };  
        this.api.getNodesInFolder(opts, callback);  
        },  
  
  
						
  /* Submit a new daily schedule task named "2 - task from js api". The catalog is "/SampleReports/SampleReports.cat" and  
report is "/SampleReports/Shipment Status Report.wls". */  
  submitScheduledTask : function() {  
    var opts = {  
      'name': "2 - task from js api",  
      'timeCondition': {  
        'type': "Periodically",  
        'periodically': {  
          'date' : {  
            'type' : "Daily"  
          },  
          'time' :{  
            'type' : "At",  
            'timeAt' : {  
              'hour' : 5,  
              'minute' : 0,  
              'meridiem' : "PM"  
            }  
          }  
        },  
        'runMissedTaskUponServerRestart' : true  
      },  
      'reportInfo': {  
        'report': "/SampleReports/Shipment Status Report.wls",  
        'catalog': "/SampleReports/SampleReports.cat",  
        'reportParameters' : [  
        {  
          'name': "P_StartDate",  
          'value': "2015-12-30"  
        },  
        {  
          'name': "p_EndDate",  
          'value': "2018-6-7"  
        },  
        {  
          'name': "P_ShipperTerritory-Shipper Territory",  
          'multipleValues' : [  
            "Central, USA", "West, USA"  
          ],  
          'isAll': false  
        },  
        {  
          'name': "P_ShipperTerritory-Shipper Name",  
          'multipleValues' : [  
            "MW Shipping"  
          ],  
          'isAll': false  
        }  
        ]  
      },  
      'publish': {  
        'toVersion': {  
          'formats': {  
            'html': {}  
          }  
        }  
      }  
    };  
    var callback = function(error, data, response) {  
      var $msg = $('#div_result').html("<div>test TaskApi.submitScheduledTask...</div>");  
      if (error) {  
        $msg.append($("<span style='color: red;'>" + error + "</span>"));  
      } else {  
        $msg.append("<div>catalog:/SampleReports/SampleReports.cat</div>");  
        $msg.append("<div>report:/SampleReports/Shipment Status Report.wls</div>");  
        $msg.append("Done! task id="+data);  
      }  
    };  
    $('#div_result').html("<div>Waiting for response...</div>");  
    this.api.submitScheduledTask(opts, callback);  
  },  
  
  
  /* Get the parameter information such as parameter names, their default values, the value lists, etc. of the report "/SampleReports/Invoice Report.wls".  
The catalog is "/SampleReports/SampleReports.cat". */  
  getReportParameterInfoList : function(changingParameter) {  
    var opts = {  
      'report': "/SampleReports/Invoice Report.wls",  
      'catalog': "/SampleReports/SampleReports.cat",  
      'reportParameters': [{},{}]  
      };  
  
					
    var pCountry = changingParameter >= 1 ? $("#p_Cascading-Country").children(":selected").val() : null;  
    var pState = changingParameter >= 2 ? $("#p_Cascading-State").children(":selected").val() : null;  
  
    if (changingParameter >= 1 && pCountry != null) {  
      opts.reportParameters[0].name = "p_Cascading-Country";  
      opts.reportParameters[0].value = pCountry;  
      if (changingParameter >= 2 && pState != null) {  
      opts.reportParameters[1].name = "p_Cascading-State";  
      opts.reportParameters[1].value = pState;  
      }  
      }  
  
					
    if (changingParameter >= 1 && parameterEngineId != null) {  
      opts.parameterEngineId = parameterEngineId;  
      }  
  
					
    var callback = function(error, data, response) {  
      var $msg = $('#div_result').html("<div>test TaskApi.getReportParameterInfoList...</div>");  
      if (error) {  
      $msg.append($("<span style='color: red;'>" + error + "</span>"));  
      } else {  
      parameterEngineId = data.parameterEngineId;  
      $msg.append("<div>catalog: /SampleReports/SampleReports.cat</div>");  
      $msg.append("<div>report: /SampleReports/Invoice Report.wls</div>");  
      if (changingParameter >= 1 && pCountry != null) {  
      $msg.append("<div>parameter: p_Cascading-Country = " + pCountry + "</div>");  
      }  
      if (changingParameter >= 2 && pState != null) {  
      $msg.append("<div>parameter: p_Cascading-State = " + pState + "</div>");  
      }  
      $msg.append("<div> </div><div>return ReportParameterInfoPack:</div>");  
      $msg.append(JSON.stringify(data));  
  
					
      $("#div_parameters").contents().filter(function(){  
      return this.nodeType == 3;  
      }).remove();  
      $("#p_Cascading-Country").empty();  
      $("#p_Cascading-State").empty();  
      $("#p_Cascading-City").empty();  
		
      var selectValue = data.parameterInfos[0].defaultValue;  
      $("#p_Cascading-Country").before(data.parameterInfos[0].prompt);  
      for (var i in data.parameterInfos[0].valueList) {  
      if (data.parameterInfos[0].valueList[i].value.match(selectValue)) {  
      $("#p_Cascading-Country").append("<option selected=\"selected\" value=\"" +  
      data.parameterInfos[0].valueList[i].value + "\"> " +  
      data.parameterInfos[0].valueList[i].displayValue + "</option>");  
      } else {  
      $("#p_Cascading-Country").append("<option value=\"" +  
      data.parameterInfos[0].valueList[i].value + "\"> " +  
      data.parameterInfos[0].valueList[i].displayValue + "</option>");  
      }  
      }  
  
      selectValue = data.parameterInfos[1].defaultValue;  
      $("#p_Cascading-State").before(data.parameterInfos[1].prompt);  
      for (var i in data.parameterInfos[1].valueList) {  
      if (data.parameterInfos[1].valueList[i].value.match(selectValue)) {  
      $("#p_Cascading-State").append("<option selected=\"selected\" value=\"" +  
      data.parameterInfos[1].valueList[i].value + "\"> " +  
      data.parameterInfos[1].valueList[i].displayValue + "</option>");  
      } else {  
      $("#p_Cascading-State").append("<option value=\"" +  
      data.parameterInfos[1].valueList[i].value + "\"> " +  
      data.parameterInfos[1].valueList[i].displayValue + "</option>");  
      }  
      }  
  
      $("#p_Cascading-City").before(data.parameterInfos[2].prompt);  
      for (var i in data.parameterInfos[2].valueList) {  
      $("#p_Cascading-City").append("<option value=\"" +  
      data.parameterInfos[2].valueList[i].value + "\"> " +  
      data.parameterInfos[2].valueList[i].displayValue + "</option>");  
      }  
      }  
      };  
  
					
    ('#div_result').html("<div>Waiting for response...</div>");  
      this.api.getReportParameterInfoList(opts, callback);  
      }
```

## Embedding Logi Report Reports and Dashboards in Your Application

With the JavaScript APIs Logi Report provides, you can embed page reports, web reports, and dashboards into your own application and perform actions outside the report template without using [Page Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/1500009777501-Page-Report-Studio), [Web Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/1500009778701-Web-Report-Studio), or [JDashboard](https://devnet.logianalytics.com/hc/en-us/articles/1500009771721-Introduction-to-the-Logi-Report-JDashboard).

You can implement JavaScript APIs in an external application and perform the following actions on the embedded reports and dashboards:

* Open
* Close
* Export
* Print
* Specify Parameter Values
* Refresh Data
* Save
* Save As
* Navigate Pages in Page Reports

For more information about the JavaScript APIs, refer to the API documentation in the `<install_root>\help\javascriptapi` directory.

### Integrating JavaScript APIs Into Your Environment

The JavaScript APIs that Logi Report provides is a single JavaScript file jreportapi.js. It is created in the `<install_root>\public_html\webos\jsvm\lib` directory by the JavaScript making tool. There are two ways to use the JavaScript APIs in customer's application.

* **Deploying jreportapi.js to customer's application**
  1. Copy jreportapi.js from `<install_root>\public_html\webos\jsvm\lib` to a folder `C:\API` in the customer's application.
  2. Load jreportapi.js in customer's html page as follows:

     `<script id="j$vm" type="text/javascript" src="C:\API\jreportapi.js"></script>`
* **Loading jreportapi.js from a remote Logi Report Server**

  Assume that Logi Report Server is running on 192.168.0.1:8888. Then you can load jreportapi.js by setting the URL `http://192.168.0.1:8888/webos/jsvm/lib/jreportapi.js` in the customer's html page as follows:

  `<script id="j$vm" type="text/javascript" src="http://192.168.0.1:8888/webos/jsvm/lib/jreportapi.js"></script>`

### Running the JavaScript API Demos

Logi Report Server provides two demos in the `<install_root>\public_html\webos\app\demo` directory:

* jreportapi-demo-rpt.html for embedding a page/web report. The demo file uses an outside JavaScript file demo-rpt.js located in the same folder which shows how to use Logi Report JavaScript APIs.
* jreportapi-demo-dsb.html for embedding dashboards. The demo file uses an outside JavaScript file demo-dsb.js located in the same folder which shows how to use Logi Report JavaScript APIs.

**To run the demos:**

1. Start your Logi Report Server and then open a demo file using URL like the following:

   `http://localhost:8888/webos/app/demo/jreportapi-demo-rpt.html  
    http://localhost:8888/webos/app/demo/jreportapi-demo-dsb.html`
2. In the displayed web page, select the **Open xxx** option on the left menu to load the specified report or dashboards as customized in the API.

   For the dashboard demo, two dashboards are opened, and their names are shown above the dashboard body. You can select the names to switch between the two dashboards.
3. Use the left menu to perform actions on the report or dashboards.
4. If the report or dashboards has defined web controls such as filter control and custom control, they can also work.
5. If there are links in the report or dashboards, after you select a link, Server displays a link path above the report body or dashboard body. You can then use the link path to go back to the previous step.

### Specifying Parameter Values

When the reports or dashboards embedded in an application contain parameters, you need to specify parameters when running them. See the following example for a page report:

```
thi$.openPageReport = function(entryId){  
  
var  params1 = {  
"p_Cascading-Country":"USA",  
"p_Cascading-City":["New York","Los Angeles","Chicago"],  
};  
  
var app = Factory.runReport(  
server, prptRes, catRes, params1, entryId);  
};
```

After the reports or dashboards are opened, you can take the following API functions to get and change their parameter values.

* **getParameterInfo(callback)**   
  Gets the paramters of the current report or dashboard and returns array of parameter name and default value pair.
* **changeParameters(parameterInfo)**   
  Sets user specified report parameter values using the parameter parameterInfo to re-run the current report or dashboard.

  ```
  @param parameterInfo Array.  
   [  
   {
  pname: String. The parameter name.
  pvalue: Array. The parameter value. For most parameter types pvalue has only one element, but a multi-value parameter may have several elements.  
  ownerID: Array. The report ID or library component ID which uses the current parameter. ownerID is not necessary for reports, but must be provided for dashboards.   
  }  
  ...  
  ]
  ```

You can find the detailed usage in the two files Dashboard.js and ReportSet.js in the `<install_root>\public_html\webos\jsvm\src\com\jinfonet\api` directory.

### Using Single Sign On

When the reports or dashboards are embedded in a [Single Sign On](https://devnet.logianalytics.com/hc/en-us/articles/1500009749962-Security-for-Accessing-Web-Pages#SSO) environment, you should specify the authorized user in your code. The following shows how to specify a user for single sign on as compared to normal login.

For common login, user name and password are set as:

`user: "admin",  
pass: "admin",`

See the following example:

```
        var server = {  
          url: "http://localhost:8888/jinfonet/tryView.jsp"  
    user: "admin",  
       pass: "admin",  
          jrd_prefer:{  
              // For page report  
              pagereport:{  
                  feature_UserInfoBar:false,  
                  feature_ToolBar: false,  
                  feature_Toolbox: false,  
                  feature_DSOTree: false,  
                  feature_TOCTree: false,  
                  feature_PopupMenu: false,  
                  feature_ADHOC: false  
              },  
                
              // For web report  
              webreport:{  
                  viewMode:{  
                      hasToolbar: false,  
                      hasSideArea: false  
                  }  
              }  
          },  
          jrd_studio_mode: "view",  
          "jrs.param_page": true  
      },
```

For single sign on, use authorized\_user:"user\_name" to specify the authorized user as follows:

```
        var server = {  
        url: "http://localhost:8888/jinfonet/tryView.jsp",  
        authorized_user:"admin",  
        jrd_prefer:{  
            // For page report  
            pagereport:{  
                feature_UserInfoBar:false,  
                feature_ToolBar: false,  
                feature_Toolbox: false,  
                feature_DSOTree: false,  
                feature_TOCTree: false,  
                feature_PopupMenu: false,  
                feature_ADHOC: false  
            },  
              
            // For web report  
            webreport:{  
                viewMode:{  
                    hasToolbar: false,  
                    hasSideArea: false  
                }  
            }  
        },  
        jrd_studio_mode: "view",  
        "jrs.param_page": true  
    },
```

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009742982-Working-with-APIs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009770821-Using-Server-API-to-Work-with-Logi-Report-Server)
