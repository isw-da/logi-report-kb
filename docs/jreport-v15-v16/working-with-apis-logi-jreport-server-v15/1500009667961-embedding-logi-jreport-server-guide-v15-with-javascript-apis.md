---
title: "Embedding Logi JReport Server Guide v15 With JavaScript APIs"
id: 1500009667961
section: "Working With APIs Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009667961-Embedding-Logi-JReport-Server-Guide-v15-With-JavaScript-APIs
updated_at: 2021-07-24T20:55:33Z
---

# Embedding Logi JReport Server Guide v15 With JavaScript APIs

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650562-Accessing-Visual-Analysis)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009643402-Working-With-APIs)

# Embedding Logi JReport With JavaScript APIs

With the JavaScript APIs provided by Logi JReport, you can successfully embed page reports, web reports and dashboards into your own application and then perform actions outside the report template without using [Page Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/1500009649242-Page-Report-Studio), [Web Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/1500009675101-Web-Report-Studio), or [JDashboard](https://devnet.logianalytics.com/hc/en-us/articles/1500009644602-JDashboard).

The implemented JavaScript APIs in an external application can be applied to perform the following actions:

**For page report and web report**

* Open a report
* Close the report
* Export the report
* Print the report
* Refresh data
* Save the report
* Page navigation (available to page report only)

**For dashboards**

* Open multiple dashboards and switch among them
* Close dashboards
* Export a dashboard using the JDashboard Export dialog
* Print a dashboard using the JDashboard Print dialog
* Refresh data
* Save the current active dashboard

Below is a list of the sections coverd in this topic:

* [Integrating JavaScript APIs Into Your Environment](#Integ)
* [Running the JavaScript API Demos](#Demo)
* [Specifying Parameter Values](#Param)
* [Using Single Sign-On](#SSO)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Integrating JavaScript APIs Into Your Environment

The JavaScript APIs that Logi JReport provides is a single JavaScript file Logi JReportapi.js. It is created in the `<Logi JReportServer_install_root>\public_html\webos\jsvm\lib` folder by the JavaScript making tool. There are two ways to use the JavaScript APIs in customer's application.

* **Deploying Logi JReportapi.js to customer's application**
  1. Copy the Logi JReportapi.js file from `<Logi JReportServer_install_root>\public_html\webos\jsvm\lib` to a folder `C:\API` in the customer's application.
  2. Load the Logi JReportapi.js file in customer's html page as follows:

     `<script id="j$vm" type="text/javascript" src="C:\API\Logi JReportapi.js"></script>`
* **Loading Logi JReportapi.js from a remote Logi JReport Server**

  Assume that Logi JReport Server is running on 192.168.0.1:8888. Then you can load Logi JReportapi.js by setting the URL `http://192.168.0.1:8888/webos/jsvm/lib/Logi JReportapi.js` in the customer's html page as follows:

  `<script id="j$vm" type="text/javascript" src="http://192.168.0.1:8888/webos/jsvm/lib/Logi JReportapi.js"></script>`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Running the JavaScript API Demos

Logi JReport Server provides two demos in the `<Logi JReportServer_install_root>\public_html\webos\app\demo` folder:

* Logi JReportapi-demo-rpt.html for embedding a page/web report. The demo file uses an outside JavaScript file demo-rpt.js located in the same folder which shows how to use Logi JReport JavaScript APIs.
* Logi JReportapi-demo-dsb.html for embedding dashboards. The demo file uses an outside JavaScript file demo-dsb.js located in the same folder which shows how to use Logi JReport JavaScript APIs.

**To run the demos:**

1. Start your Logi JReport Server and then open a demo file using URL like the following:

   `http://localhost:8888/webos/app/demo/Logi JReportapi-demo-rpt.html  
    http://localhost:8888/webos/app/demo/Logi JReportapi-demo-dsb.html`
2. In the displayed web page, select the **Open xxx** option on the left menu to load the specified report or dashboards as customized in the API.

   For the dashboard demo, two dashboards are opened and their names are shown above the dashboard body. You can select the names to switch between the two dashboards.
3. Use the left menu to perform actions on the report or dashboards.
4. If the report or dashboards has defined web controls such as filter control and custom control, they can also work.
5. If there are links in the report or dashboards, after you select a link, a link path is displayed above the report body or dashboard body. You can then use the link path to go back to the previous step.

As for the detailed JavaScript APIs and methods of each API that Logi JReport provides, refer to the API documentation in the `<Logi JReportServerinstall_root>\help\javascriptapi` folder.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Specifying Parameter Values

When the reports or dashboards embedded in an application contain parameters, you need to specify parameters when running them. See the following example for a page report:

|  |
| --- |
| ``` thi$.openPageReport = function(entryId){ var  params1 = { "p_Cascading-Country":"USA", "p_Cascading-City":["New York","Los Angeles","Chicago"], }; var app = Factory.runReport( server, prptRes, catRes, params1, entryId); }; ``` |

After the reports or dashboards are opened, you can take the following API functions to get and change their parameter values.

* **getParameterInfo(callback)**

  Gets the parameters of the current report or dashboard and returns array of parameter name and default value pair.
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

You can find the detailed usage in the two files Dashboard.js and ReportSet.js in the `<server_install_root>\public_html\webos\jsvm\src\com\jinfonet\api` directory.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Using Single Sign-On

When the reports or dashboards are embedded in a [single sign-on](https://devnet.logianalytics.com/hc/en-us/articles/1500009650182-Security-for-Accessing-Web-Pages#SSO) environment, you should specify the authorized user in your code. The following shows how to specify a user for single sign-on as compared to normal login.

For common login, user name and password are set as:

*user: "admin",  
pass: "admin",*

See the following example:

`var server = {  
         url: "http://localhost:8888/jinfonet/tryView.jsp",  
        user: "admin",  
        pass: "admin",  
         jrd_prefer:{  
             // For page report  
             pagestudio:{  
                 feature_UserInfoBar:false,  
                 feature_ToolBar: false,  
                 feature_Toolbox: false,  
                 feature_DSOTree: false,  
                 feature_TOCTree: false,  
                 feature_PopupMenu: false,  
                 feature_ADHOC: false  
             },  
               
             // For web report  
             wrptstudio:{  
                 viewMode:{  
                     hasToolbar: false,  
                     hasSideArea: false  
                 }  
             }  
         },  
         jrd_studio_mode: "view",  
         "jrs.param_page": true  
     },`

For single sign-on, use *authorized\_user:"user\_name"* to specify the authorized user as follows:

`var server = {  
        url: "http://localhost:8888/jinfonet/tryView.jsp",  
        authorized_user:"admin",  
        jrd_prefer:{  
            // For page report  
            pagestudio:{  
                feature_UserInfoBar:false,  
                feature_ToolBar: false,  
                feature_Toolbox: false,  
                feature_DSOTree: false,  
                feature_TOCTree: false,  
                feature_PopupMenu: false,  
                feature_ADHOC: false  
            },  
              
            // For web report  
            wrptstudio:{  
                viewMode:{  
                    hasToolbar: false,  
                    hasSideArea: false  
                }  
            }  
        },  
        jrd_studio_mode: "view",  
        "jrs.param_page": true  
    },`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650562-Accessing-Visual-Analysis)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009643402-Working-With-APIs)
