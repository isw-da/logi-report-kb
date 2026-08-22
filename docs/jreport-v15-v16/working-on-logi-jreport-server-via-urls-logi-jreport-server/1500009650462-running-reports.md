---
title: "Running Reports"
id: 1500009650462
section: "Working on Logi JReport Server via URLs Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009650462-Running-Reports
updated_at: 2021-07-24T20:53:32Z
---

# Running Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675421-Working-on-Logi-JReport-Server-Guide-v15-Server-via-URLs)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675481-Running-a-Report-Tab-in-a-Page-Report)

# Running Reports

You can use the following JSP's to run reports via URL: [tryView.jsp](#tryView), [runReport.jsp](#runReport), and [run.jsp.](#run) However Page Report Studio and Web Report Studio have permission control, so in order to run reports in report studio you are required to have the [Execute and/or Edit permissions](https://devnet.logianalytics.com/hc/en-us/articles/1500009674981-Managing-Permissions) on the reports.

The image illustrates the relationship between the JSPs:

![JSP Relationship](https://devnet.logianalytics.com/hc/article_attachments/4404920354839/url_run.gif)

**tryView.jsp**

This is the normal method of accessing reports using URLs. tryView.jsp can be used to run page reports and web reports to any allowed formats.

If the report has parameters and no parameter specified in the URL or the parameters provided in the URL fail to include all necessary parameters, the server then displays the parameter dialog for entering parameter values.

Below are some examples:

* Run a page report in Page Report Studio:  
  `http://localhost:8888/jinfonet/tryView.jsp?jrs.report=%2fSampleReports%2fCustomerAnalysis.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=8`
* Run a page report in PDF format:  
  `http://localhost:8888/jinfonet/tryView.jsp?jrs.report=%2fSampleReports%2fCustomerAnalysis.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=2`
* Run a web report in Web Report Studio:   
  `http://localhost:8888/jinfonet/tryView.jsp?&jrs.report=%2fSampleReports%2fLink.wls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=8`
* Run a web report in HTML format:   
  `http://localhost:8888/jinfonet/tryView.jsp?&jrs.report=%2fSampleReports%2fLink.wls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=1`

**runReport.jsp**

This JSP functions the same as tryView.jsp when the report has no parameters. When it has parameters, the report runs with the default parameters if no parameter values are specified, or else it runs with the parameters specified in the URL.

runReport.jsp can be used to run page reports and web reports to any allowed formats.

Below are some examples:

* Run a page report in HTMl format:   
  `http://localhost:8888/jinfonet/runReport.jsp?jrs.report=%2fSampleReports%2fCustomerAnalysis.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=1`&`&jrs.param$P_StartDate=2006-01-01&jrs.param$p_EndDate=2007-12-31`
* Run a web report in Web Report Studio:  
  `http://localhost:8888/jinfonet/runReport.jsp?jrs.report=%2fSampleReports%2fProducts.wls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=8`

**run.jsp**

run.jsp can be used to run page reports in Page Report Studio and web reports in Web Report Studio. When it has parameters, the report runs with the default parameters if no parameter values are specified, or else it runs with the parameters specified in the URL.

* The URL entry for running web reports in Web Report Studio is: webreport/studio/entry/run.jsp. For more information, see [Opening Web Reports in Web Report Studio via JSON](https://devnet.logianalytics.com/hc/en-us/articles/1500009675501-Opening-Web-Reports-in-Web-Report-Studio-via-JSON).
* The URL entry for running page reports and page report result files in Page Report Studio is: webos/app/pagestudio/run.jsp. See the following examples: `http://localhost:8888/webos/app/pagestudio/run.jsp?jrs.report=%2fSampleReports%2fCustomerAnalysis.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat`

run.jsp can also be used in the following scenarios:

* [Running dashboards](https://devnet.logianalytics.com/hc/en-us/articles/1500009650422-Working-With-Dashboards). The URL entry is: dashboard/app/entry/run.jsp.
* [Accessing Visual Analysis](https://devnet.logianalytics.com/hc/en-us/articles/1500009650562-Accessing-Visual-Analysis). The URL entry is: webos/app/designer/run.jsp.
* [Creating a web report via standard wizard way](https://devnet.logianalytics.com/hc/en-us/articles/1500009650402-Creating-Reports#Web). The URL entry is: webos/app/webstudio/run.jsp?jrd\_wizard=1&.
* [Creating a web report via quick start way](https://devnet.logianalytics.com/hc/en-us/articles/1500009650402-Creating-Reports#Quickstart). The URL entry is: webos/app/webstudio/run.jsp.
* [Viewing Page Report Result files](https://devnet.logianalytics.com/hc/en-us/articles/1500009650542-Working-with-Logi-JReport-Server-Guide-v15-Server#ViewResult) in Page Report Studio.

In addition to the above JSPs, you can call the server servlet *jrserver* to run reports to any allowed format. However when you use servlet to run a report, Logi JReport redirects the request to an appropriate JSP so it is recommended to use JSP to run the report directly. The following are two examples:

* Run a page report in Page Report Studio:  
  `http://localhost:8888/jrserver/SampleReports/SampleReports.cat/CustomerAnalysis.cls?jrs.cmd=jrs.web_vw&jrs.result_type=8`
* Run a web report to HTML:  
  `http://localhost:8888/jrserver/SampleReports/SampleReports.cat/Link.wls?jrs.cmd=jrs.web_vw&jrs.result_type=1`

For detailed information about the properties that are included in the URLs, see [Appendix 1: URL Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009668881-Appendix-1-URL-Properties).

Below are some more specific examples about running reports via URL:

* [Running a Report Tab in a Page Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009675481-Running-a-Report-Tab-in-a-Page-Report)
* [Refreshing Page Report Data Automatically](https://devnet.logianalytics.com/hc/en-us/articles/1500009675441-Refreshing-Page-Report-Data-Automatically)
* [Opening Web Reports in Web Report Studio via JSON](https://devnet.logianalytics.com/hc/en-us/articles/1500009675501-Opening-Web-Reports-in-Web-Report-Studio-via-JSON)
* [Specifying the Report Studio Mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009650502-Specifying-the-Report-Studio-Mode)
* [Specifying a Time Duration for a Task and Notifying Someone by E-Mail](https://devnet.logianalytics.com/hc/en-us/articles/1500009650482-Specifying-a-Time-Duration-for-a-Task-and-Notifying-Someone-by-E-mail)
* [Switching the Report Database Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009675461-Switching-the-Report-Database-Connection)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675421-Working-on-Logi-JReport-Server-Guide-v15-Server-via-URLs)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675481-Running-a-Report-Tab-in-a-Page-Report)
