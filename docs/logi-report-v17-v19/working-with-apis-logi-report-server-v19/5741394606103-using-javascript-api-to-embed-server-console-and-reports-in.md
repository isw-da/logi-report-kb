---
title: "Using JavaScript API to Embed Server Console and Reports in Your Applications "
id: 5741394606103
section: "Working with APIs Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741394606103-Using-JavaScript-API-to-Embed-Server-Console-and-Reports-in-Your-Applications
updated_at: 2022-10-31T17:15:44Z
---

# Using JavaScript API to Embed Server Console and Reports in Your Applications 

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741381172631-Working-with-APIs-Logi-Report-Server-v19)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741407944855-Using-Server-API-to-Work-with-Logi-Report-Server)

# Using JavaScript API to Embed Server Console and Reports in Your Applications

This topic describes how you can embed the Logi Report Server Console, page reports, web reports, and dashboards into your applications and then perform actions outside the report template, using Logi Report JavaScript APIs.

This topic contains the following sections:

* [Embedding the Server Console in Your Application](#Console)
* [Embedding Logi Report Reports and Dashboards in Your Application](#Report)
  + [Integrating JavaScript APIs Into Your Environment](#Integ)
  + [Running the JavaScript API Demos](#Demo)
  + [Specifying Parameter Values](#Param)
  + [Using Single Sign-on](#SSO)
* [Accessing Rest API via URL, Header, or SSO](#Rest)

## Embedding the Server Console in Your Application

Logi Report provides modularized RESTful Web APIs for the Server Console so that you can call these APIs to set up a similar server console as the Logi Report Server Console in your applications on any platforms such as JavaScript, Java, .NET, and C++. RESTful Web APIs are popular and typically based on HTTP methods to access resources via URL-encoded parameters and the use of JSON or XML to transmit data. Logi Report develops Web API definition using [openAPI](https://www.openapis.org/) as the specification. You can easily generate client side APIs according to the Web API definition file **logireportserver.yaml** in the `<install_root>\help\webapi` directory. Client APIs finally call the Web APIs to a Logi Report Server.

![JavaScript API](https://devnet.logianalytics.com/hc/article_attachments/9905819944855/jsapi.gif)

You can access the Web API documentation via the URL <http://localhost:8888/servlet/sendfile/help/webapi/webapi-docs/index.html> if you have started a local Logi Report Server.

Logi Report Web APIs cover these server functions:

* **Signing in and out**
  + Sign in and out of Logi Report Server.
  + Get user session information such as username and session ID.
  + Set session timeout time.
* **Managing resources**
  + List all resources including folders, reports, library components, dashboards, and versions.
  + Create folders in the server resource tree and publish resources to them.
  + Get and set resource properties.
  + Set and delete resource permissions.
  + Get, set, and delete catalog-level, report-level, and global NLS.
  + Get all resources in the server resource tree with their properties using a single call, and obtain parameter information of the resources.
* **Managing business views**
  + List all the business views in a catalog, including the categories, group objects, aggregation objects, and detail objects in the business views.
  + Get, set, and delete permissions of business views and group objects.
  + Manage business views available to a report
  + Get, set, and delete business view security in a catalog.
* **Managing server security**
  + Add, remove, get, and edit users, groups, and roles; add and remove their members.
  + Get, create, update, and delete organizations; get and update resource allocations of organizations.
* **Scheduling report tasks and advanced running reports**
  + Schedule report running and bursting tasks and send reports to various locations such as the versioning system, hard drive, email addresses, printer, fax, and FTP sites. Schedule and Advanced Run support all the formats including Page Report Result, Web Report Result, HTML, PDF, Excel, Text, RTF, XML, and PostScript.
  + View, enable, disable, copy, get, run, import, export, and delete report tasks.
* **Configuring user preferences**
  + Get and set server preferences.
  + Get, add, edit, and delete the profiles of Page Report Studio, Web Report Studio, and JDashboard.
* **![This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9905577570711/___newv19.2.png "New for version 19.2.")Using the LDAP server**
  + Get and modify the LDAP server settings.
  + Import users and groups from the LDAP server.
  + Get and set LDAP synchronization schedule settings.
  + Get, add, and modify LDAP role maps.
* **![This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9905577570711/___newv19.2.png "New for version 19.2.")Managing Triggers**  
  You can get, create, enable, disable, and fire triggers.
* **Dynamic settings for catalogs**  
  You can get, set, create, and delete dynamic connections, dynamic security, and dynamic display names for business view elements.

Logi Report Server has already generated the client JavaScript APIs for your direct use. You can find the **javascript-client-generated.zip** file in the `<install_root>\help\webapi\client-js` directory. Extract the zip file, and you will get the **javascript-client** folder which contains the following: JavaScript API codes are in the **src** subfolder; for the files in the **docs** subfolder and the README file, you need to use Markdown Viewer to view them. To access the JavaScript API documents, open the **index.html** file in the `<install_root>\help\webapi\client-js\js-docs` directory.

However, for other client side APIs like Java, .NET, and C++, you need to generate them by yourself using the Web API definition file **logireportserver.yaml**.

You can refer to the following sample code if you have started a local Logi Report Server: <http://localhost:8888/servlet/sendfile/help/webapi/client-js/sample/index.html>. You can find the complete sample materials in the `<install_root>\help\webapi\client-js\sample` directory. For the code details, view **index.js** in the **src** folder.

## Embedding Logi Report Reports and Dashboards in Your Application

With the JavaScript APIs Logi Report provides, you can embed page reports, web reports, and dashboards into your own application and perform actions outside the report template without using [Page Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/5741462429975-Page-Report-Studio-Server-v19), [Web Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/5741464180119-Web-Report-Studio-Server-v19), or [JDashboard](https://devnet.logianalytics.com/hc/en-us/articles/5741387513879-Introduction-to-the-Logi-Report-JDashboard-Logi-Report-Server-v19).

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

For more information about the JavaScript APIs, select the link: [JavaScript API documentation](https://reportkbase.logianalytics.com/v19.2/javascriptapi/index.html).

### Integrating JavaScript APIs Into Your Environment

The JavaScript APIs that Logi Report provides is a single JavaScript file **jreportapi.js**. Server created it in the `<install_root>\public_html\webos\jsvm\lib` directory by the JavaScript making tool. You can use the JavaScript APIs in your application in two ways.

* **Deploying jreportapi.js to your application**
  1. Copy **jreportapi.js** from `<install_root>\public_html\webos\jsvm\lib` to a folder `C:\API` in your application.
  2. Load **jreportapi.js** in your HTML page:

     `<script id="j$vm" type="text/javascript" src="C:\API\jreportapi.js"></script>`
* **Loading jreportapi.js from a remote Logi Report Server**

  Assume that Logi Report Server is running on 192.0.0.1:8888. Then you can load jreportapi.js by setting the URL `http://192.0.0.1:8888/webos/jsvm/lib/jreportapi.js` in your HTML page:

  `<script id="j$vm" type="text/javascript" src="http://192.0.0.1:8888/webos/jsvm/lib/jreportapi.js"></script>`

### Running the JavaScript API Demos

Logi Report Server provides two JavaScript API demos in the `<install_root>\public_html\webos\app\demo` directory:

* **jreportapi-demo-rpt.html** for embedding a page or web report. The demo file uses an outside JavaScript file **demo-rpt.js** in the same folder which shows how to use Logi Report JavaScript APIs.
* **jreportapi-demo-dsb.html** for embedding dashboards. The demo file uses an outside JavaScript file **demo-dsb.js** in the same folder which shows how to use Logi Report JavaScript APIs.

**To run the demos:**

1. Start your Logi Report Server.
2. Open a demo file using URL like this:

   `http://localhost:8888/webos/app/demo/jreportapi-demo-rpt.html  
    http://localhost:8888/webos/app/demo/jreportapi-demo-dsb.html`
3. Server displays a web page. Select the **Open xxx** option on the left menu to load the specified report or dashboards as customized in the API.

   For the dashboard demo, Server opens two dashboards and display their names above the dashboard body. You can select the names to switch between the two dashboards.
4. Use the left menu to perform actions on the report or dashboards.
5. If the report or dashboards has defined web controls such as filter control and custom control, they can also work.
6. If there are links in the report or dashboards, after you select a link, Server displays a link path above the report body or dashboard body. You can then use the link path to go back to the previous step.

### Specifying Parameter Values

When the reports or dashboards you embedded in an application use parameters, you need to specify the parameters values when running them. To apply all the values of a parameter, set the parameter value to **\x07**.

See the example for a page report:

```
thi$.openPageReport = function(entryId){  
  
var  params1 = {  
"p_Cascading-Country":"USA",  
"p_Cascading-City":["New York","Los Angeles","Chicago"],  
"p_Year": "\x07"  
};  
  
var app = Factory.runReport(  
server, prptRes, catRes, params1, entryId);  
};
```

After you open reports or dashboards, you can use the following API functions to get and change their parameter values.

* **getParameterInfo(callback)**   
  Get the parameters of the current report or dashboard and return an array of the parameter name and default value pair.
* **changeParameters(parameterInfo)**   
  Set parameter values using the parameter **parameterInfo** to rerun the current report or dashboard.

  ```
  @param parameterInfo Array.  
   [  
   {
  pname: String. The parameter name.
  pvalue: An array. The parameter value. For most parameter types pvalue has only one element, but a multi-valued parameter may have several elements.  
  ownerID: An array. The report ID or library component ID which uses the current parameter. ownerID is not necessary for reports, but you must provide it for dashboards.   
  }  
  ...  
  ]
  ```

For more information, see the **Dashboard.js** and **ReportSet.js** files in `<install_root>\public_html\webos\jsvm\src\com\jinfonet\api`.

### Using Single Sign-on

When you embed reports or dashboards in a [Single Sign-on](https://devnet.logianalytics.com/hc/en-us/articles/5741484187415-Security-for-Accessing-Web-Pages#SSO) (SSO) environment, you should specify the authorized user in your code. This section shows how to specify a user for SSO as compared to normally signing in.

For normally signing in, you set username and password as:

`user: "admin",  
pass: "admin",`

See the example:

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

For SSO, use **authorized\_user:"user\_name**" to specify the authorized user:

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

## Accessing Rest API via URL, Header, or SSO

The following example shows how you can access Logi Report Rest API to obtain reports in a folder, by setting username and password in URL or header or using SSO.

1. In the computer B with the domain name b.test.com, install Logi Report Server to `D:\LogiReport\Server`.
2. Compile the **WebAPIExternalAuthorized.java** file.

   ```
   javac -classpath D:\LogiReport\Server\lib\* D:\LogiReport\Server\help\webapi\sample\WebAPIExternalAuthorized.java
   ```
3. Add the compiled class to the **SSO.jar**.
4. Add the path of **SSO.jar** in **JRServer.bat** in `D:\LogiReport\Server\bin`.
5. Add -D parameters in **JRServer.bat**.

   ```
   -Djrs.httpExternalAuthorized=WebAPIExternalAuthorized -Djreport.server.csrf.whitelist=a.test.com
   ```
6. Start Logi Report Server.
7. In the computer A with the domain name a.test.com, start **Internet Information Services** (IIS).
8. Deploy **WebAPIDemo.html** from `D:\LogiReport\Server\help\webapi\sample` in the computer B.

   ![Add WebAPIDemo.html](https://devnet.logianalytics.com/hc/article_attachments/9905831712535/restapi1.gif)
9. Access `http://a.test.com/webapidemo.html` from any computer.

   ![Access WebAPIDemo.html](https://devnet.logianalytics.com/hc/article_attachments/9905831746839/restapi2.gif)

   You can then operate on the page to view the six scenarios of signing in Logi Report Server and getting nodes in a folder.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741381172631-Working-with-APIs-Logi-Report-Server-v19)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741407944855-Using-Server-API-to-Work-with-Logi-Report-Server)
