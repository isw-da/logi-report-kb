---
title: "Running Reports"
id: 1500009693002
section: "Working on Logi JReport Server via URLs Logi JReport Server v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009693002-Running-Reports
updated_at: 2021-11-03T06:56:25Z
---

# Running Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009692942-Working-on-Logi-JReport-Server-via-URLs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009693022-Scheduling-Reports)

# Running Reports

You can use the following JSPs to run reports via URL: [tryView.jsp](#tryView), [runReport.jsp](#runReport), and [run.jsp.](#run) However Page Report Studio and Web Report Studio have permission control, so in order to run reports in Web/Page Report Studio you are required to have the [Execute and/or Edit permissions](https://devnet.logianalytics.com/hc/en-us/articles/1500009718881-Managing-Permissions) on the reports.

The image illustrates the relationship between the JSPs:

![JSP Relationship](https://devnet.logianalytics.com/hc/article_attachments/4412131374615/url_run.gif)

**tryView.jsp**

This is the normal method of accessing reports using URLs. tryView.jsp can be used to run page reports and web reports to any allowed formats.

If the report has parameters and no parameter specified in the URL or the parameters provided in the URL fail to include all necessary parameters, the server then displays the parameter dialog for entering parameter values.

Below are some examples:

* Run a page report in Page Report Studio:  
  `http://localhost:8888/jinfonet/tryView.jsp?jrs.report=%2fSampleReports%2fEmployee Information List.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=8`
* Run a page report in PDF format:  
  `http://localhost:8888/jinfonet/tryView.jsp?jrs.report=%2fSampleReports%2fEmployee Information List.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=2`
* Run a web report in Web Report Studio:   
  `http://localhost:8888/jinfonet/tryView.jsp?&jrs.report=%2fSampleReports%2fSales Detail Report.wls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=8`
* Run a web report in HTML format:   
  `http://localhost:8888/jinfonet/tryView.jsp?&jrs.report=%2fSampleReports%2fSales Detail Report.wls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=1`

**runReport.jsp**

This JSP functions the same as tryView.jsp when the report has no parameters. When it has parameters, the report runs with the default parameters if no parameter values are specified, or else it runs with the parameters specified in the URL.

runReport.jsp can be used to run page reports and web reports to any allowed formats.

Below are some examples:

* Run a page report in HTMl format:   
  `http://localhost:8888/jinfonet/runReport.jsp?jrs.report=%2fSampleReports%2fABC.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=1`&`&jrs.param$P_StartDate=2016-01-01&jrs.param$p_EndDate=2017-12-31`
* Run a web report in Web Report Studio:  
  `http://localhost:8888/jinfonet/runReport.jsp?jrs.report=%2fSampleReports%2fSales Detail Report.wls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=8`

**run.jsp**

run.jsp can be used to run page reports in Page Report Studio and web reports in Web Report Studio. When it has parameters, the report runs with the default parameters if no parameter values are specified, or else it runs with the parameters specified in the URL.

* The URL entry for running web reports in Web Report Studio is: webreport/studio/entry/run.jsp. For more information, see [Opening Web Reports in Web Report Studio Via JSON](#JSON).
* The URL entry for running page reports and page report result files in Page Report Studio is: webos/app/pagestudio/run.jsp. For example:   
  `http://localhost:8888/webos/app/pagestudio/run.jsp?jrs.report=%2fSampleReports%2fEmployee Information List.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat`

run.jsp can also be used in the following scenarios:

* [Running dashboards](https://devnet.logianalytics.com/hc/en-us/articles/1500009692962-Working-with-Dashboards). The URL entry is: dashboard/app/entry/run.jsp.
* [Accessing Visual Analysis](https://devnet.logianalytics.com/hc/en-us/articles/1500009693042-Accessing-Visual-Analysis). The URL entry is: webos/app/designer/run.jsp.
* [Creating a web report in the traditional wizard way](https://devnet.logianalytics.com/hc/en-us/articles/1500009719361-Creating-Reports#Web). The URL entry is: webos/app/webstudio/run.jsp?jrd\_wizard=1&.
* [Creating a web report in the quick start way](https://devnet.logianalytics.com/hc/en-us/articles/1500009719361-Creating-Reports#Quickstart). The URL entry is: webos/app/webstudio/run.jsp.
* [Viewing page report result files](https://devnet.logianalytics.com/hc/en-us/articles/1500009719381-Working-with-Logi-Report-Server#ViewResult) in Page Report Studio.

In addition to the above JSPs, you can call the server servlet jrserver to run reports to any allowed format. However when you use servlet to run a report, Logi JReport redirects the request to an appropriate JSP so it is recommended to use JSP to run the report directly. The following are two examples:

* Run a page report in Page Report Studio:  
  `http://localhost:8888/jrserver/SampleReports/SampleReports.cat/Employee Information List.cls?jrs.cmd=jrs.web_vw&jrs.result_type=8`
* Run a web report to HTML:  
  `http://localhost:8888/jrserver/SampleReports/SampleReports.cat/Sales Detail Report.wls?jrs.cmd=jrs.web_vw&jrs.result_type=1`

For detailed information about the properties that are included in the URLs, see [Appendix 1: URL Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009686482-Appendix-1-URL-Properties).

Below are some more specific topics about running reports via URL:

* [Running a Report Tab in a Page Report](#Tab)
* [Refreshing Page Report Data Automatically](#Refresh)
* [Opening Web Reports in Web Report Studio via JSON](#JSON)
* [Specifying the Web Report Studio Mode](#WebMode)
* [Specifying the Page Report Studio View](#PageView)
* [Specifying a Time Duration for a Task and Notifying Someone by E-mail](#Task)
* [Switching the Report Database Connection](#Connection)

## Running a Report Tab in a Page Report

If you want to run a specific page report tab, use jrs.report\_sheet$RPT\_TAB\_NAME=true to specify a report tab in the current page report, where RPT\_TAB\_NAME is the report name of the specific report tab, not the display name. For example, `jrs.report_sheet$Report2=true`.

To get the report name and display name of a page report tab you can open the page report in Logi JReport Designer and look at the Instance Name property in the Report Inspector or you can make use of the API methods *getName()* and *getDisplayName()* in the interface jet.server.api.ReportSheetInfo. For the detailed usages, see the Logi JReport Javadoc located in `<install_root>\help\api`.

The URL for running the report tab Financial report in Page Report Studio within the report Detail Report Corporate Overview.cls is as follows:

`http://localhost:8888/jinfonet/tryView.jsp?jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.report=%2fSampleReports%2fDetail Report Corporate Overview.cls&jrs.result_type=8&jrs.report_sheet$report2=true`

## Refreshing Page Report Data Automatically

When running a page report in Page Report Studio, you can ask Logi JReport to automatically refresh the report data at certain interval. To achieve this, you need to run the report with run.jsp and add the following two properties in the URL:

* **jrs.auto\_refresh\_data=true**  
   Specifies to automatically refresh the report data.
* **jrs.auto\_refresh\_data\_time=[a number in seconds]**  
   Specifies the time interval at which to refresh the report data.

The following is a URL example:

`http://localhost:8888/webos/app/pagestudio/run.jsp?jrs.report=%2fSampleReports%2fEmployee Information List.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.auto_refresh_data=true&jrs.auto_refresh_data_time=10`

## Opening Web Reports in Web Report Studio via JSON

Logi JReport provides properties for developer users to run web reports in Web Report Studio via JSON (JavaScript Object Notation).

The following lists the properties that are encapsulated as JSON objects. It will help if you obtain some knowledge on JSON to understand the syntax more clearly.

* jrd\_report={  
   "name":"xxx", // The full path of the web report.  
   "ver":-1, // Optional. The report version. -1 means the latest version.  
   }
* jrd\_catalog={  
   "name":"xxx", // The full path of the catalog that the web report uses.  
   "ver":-1, // Optional. The catalog version. -1 means the latest version.   
   }
* jrd\_param$={  
   "p1":"value1", // p1 is parameter name, and value1 is p1's value.  
   "p2":["value1","value2","value3"] // For multiple values.  
   }
* jrd\_userinfo={ // Optional.  
   "user":"xxx", // User name.  
   "country":"us", // The locale representing the region part for running reports, following locale naming specification.  
   "language":"en", // The locale representing the language part for running reports, following locale naming specification.  
   "encoding":"UTF-8", // The encoding for running reports.  
   "resolution":"96" // The resolution for displaying reports.  
   }
* jrd\_security\_file\_name={ // Optional.   
   "name":"xxx", // The name of a [security file](https://devnet.logianalytics.com/hc/en-us/articles/1500009692602-Dynamic-Security). When a security file is given, the security definitions in the specified catalog will be replaced by that defined in the security file.  
   }
* jrd\_datasources=[  
   // Optional.  
   // The following types of external data sources are supported:  
   // 0 - JDBC data source, 1 - JNDI data source, 2 - Java DataSource object, 3 - Connection object, 4 - ResultSet object.  
   // One or multiple data sources can be included at a time.

  {   
   // JDBC data source.  
   "ds":"Data Source 1", // Data source name.  
   "uid":"xxx", // DB user name.  
   "pwd":"xxx", // DB user password.  
   "type":0, // Indicates it is JDBC data source.  
   "url":"xxx", // JDBC URL. For example, "url":"jdbc:oracle:thin:@127.0.0.1:1521:ora8i".  
   "driver":"xxx" // JDBC driver. For example, "driver":"oracle.jdbc.driver.OracleDriver".

  // When connecting to a different database with different database metadata or data metadata, you need to also specify the following commands to set the target database metadata information if there are differences:  
   "refresh\_support\_info":True, // Optional. Value: True/False. If it is True, Logi JReport will get support information including reverse words, quote characters, and so on from the driver each time fetching data from the database. It is recommended that you set this property to true when connecting to a different database.  
   "quote\_character":"xxx", // Optional. The quote characters.  
   "extra\_characters":"xxx", // Optional. The extra characters.  
   "date\_format":"xxx", // Optional. The date format.  
   "datetime\_format":"xxx", // Optional. The datetime format.  
   "time\_format":"xxx", // Optional. The time format.  
   "transaction\_readonly":"xxx", // Optional. The transaction "read only" property. Possible value: default, Read only, or Read&Write. Ignore other values.  
   "transaction\_mode":"xxx", // Optional. The transaction mode. Possible value: default, None, Read Uncommitted, Read Committed, Repeatable Read, or Serializable. Ignore other values.   
   "char\_to\_be\_replaced":"xxx", // Optional. The characters that are to be replaced.   
   "char\_replaced\_by":"xxx" // Optional. The characters used to replace the characters specified by *char\_to\_be\_replaced*.  
   },

  {   
   // JNDI data source. Currently Logi JReport only supports local JNDI with anonymous lookup which means that the JNDI data source and the report server are in one JVM and the JNDI needs no authentication.  
   "ds":"Data Source 2", // Data source name.  
   "uid":"xxx", // DB user name.  
   "pwd":"xxx", // DB user password.  
   "type":1, // Indicates it is JNDI data source.  
   "url":"xxx", // JNDI name. For example, "url":"jndi/testDB".   
   },

  {   
   // Java DataSource object/Connection object/ResultSet object.  
   // Users should define request or session attribute, then the attribute key is the one defined in the request.  
   // For example, write user.jsp as follows:  
   // String key = "Rst";  
   // java.sql.ResultSet rst = null;  
   // rst = // Gets result set object from user own business logic.  
   // request.setAttribute("Rst", rst);   
   // Then the key would be that "key":"Rst".  
   // The above example is based on ResultSet object. It also applies to the other two types.  
   "ds":"Data Source 3", // Data source name.  
   "type":2/3/4, // Indicates the data source type.  
   "key":"xxx" // Request attribute object name, included in request or session.  
   }

  ]
* [jrd\_studio\_mode](#WebMode) // Specifies which Web Report Studio mode is available.
* jrd\_filters={

  "osf":[  
   // Specifies values of the on-screen filters in the report. There are two ways to designate an on-screen filter. One is by the instance name of the filter and the other by the field that is bound with the filter.

  {  
  // Specifies an on-screen filter and its values.

  "name":"fc1", // The instance name of an on-screen filter.  
   "reverse":false, // Optional. If true, the values of the on-screen filter are those not specified in the "values" property below.  
   "selectAll":false, // Optional. If true, it means to apply all the values at runtime and ignore the "values" property below.  
   "values":["USA","China"] // The values of the on-screen filter.   
  },

  {  
   "field":{
    
   // Specifies a field that is bound with an on-screen filter and the values of the field.

  "type":2, // The data resource type. 0 means it is a query and 2 means business view.  
   "ds":"DataSource 1", // The data source name.  
   "query":"Query 1", // Optional. The query name. It should be specified when the data resource type is query.  
   "bv":"BV 1", // Optional. The business view name. It should be specified when the data resource type is business view.   
   "name":"Customers.Country" // The mapping name of the field if the data resource type is query or the qualified display name of the field if the data resource type is business view.

  },   
   "reverse":false, // Optional. If true, the values of the field are those not specified in the "values" property below.  
  "selectAll":false, // Optional. If true, it means to apply all the values at runtime and ignore the "values" property below.   
   "values":["USA","China"] // The values of the field.  
   }

  ]

  }

When composing the URL, you need to use URL encoding to avoid errors.

Here is an example of the complete URL without URL encoding to make it easier to read:

`http://localhost:8888/webreport/studio/entry/run.jsp?jrd_report={"name":"/SampleReports/report.wls","ver":-1}&jrd_catalog={"name":"/SampleReports/SampleReports.cat","ver":-1}&jrd_param$={"P_Coutry":"USA"}&jrd_filters={"osf":[{"name":"FilterControl","values":["USA","China"]}]}&jrd_security_file_name={"name":"SampleReports.security.xml"}&jrd_datasources=[{"ds":"Data Source 1","uid":"xxx","pwd":"xxx","type":0,"url":"xxx","driver":"xxx"},{"ds":"Data Source 2","type":2,"key":"xxx"}]`

If you use absolute resource path, you need to add the property "real":true for the path. For example,

`jrd_report={"name":"C:\\JReport\\Server\\jreports\\SampleReports\\Sales Detail Report.wls","real":true}&jrd_catalog={"name":"C:\\JReport\\Server\\jreports\\SampleReports\\SampleReports.cat","real":true}`

Run Sales Detail Report.wls in the Public Reports > SampleReports folder:

`http://localhost:8888/webreport/studio/entry/run.jsp?jrd_report={"name":"/SampleReports/Sales Detail Report.wls"}&jrd_catalog={"name":"/SampleReports/SampleReports.cat"}`

## Specifying the Web Report Studio Mode

Web Report Studio has two modes: View Mode and Edit Mode. When opening web reports in Web Report Studio by URL, you can use the property jrd\_studio\_mode to specify the mode. If this property is not provided in the URL, the [default mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009686822-Configuring-Server-Profile#WebMode) set in the server profile will be applied.

Below are the values of the property:

* view - Displays Web Report Studio in View Mode by default and allows for switching to Edit Mode.
* view\_only - Displays Web Report Studio in View Mode only.
* edit - Displays Web Report Studio in Edit Mode by default and allows for switching to View Mode.

However for web reports saved in public folders in the server resource tree, Web Report Studio adopts a [permission control](https://devnet.logianalytics.com/hc/en-us/articles/1500009718881-Managing-Permissions) to restrict user access, so whether the specified mode can be opened depends on if you have the Execute and/or Edit permissions on the web reports: Execute for View Mode and Edit for Edit Mode. If you do not have the required permission on the public web report you are going to run:

* When both Execute and Edit are disabled, you will be denied to access Web Report Studio.
* When Execute is enabled but Edit is not:
  + view - Displays Web Report Studio in View Mode, same as view\_only.
  + edit - Access to Web Report Studio is denied.
* When Edit is enabled but Execute is not:
  + view and view\_only - Access to Web Report Studio is denied.
  + edit - Displays Web Report Studio in Edit Mode.

**Example：**

`http://localhost:8888/webreport/studio/entry/run.jsp?jrd_report={"name":"/SampleReports/Sales Detail Report.wls"}&jrd_catalog={"name":"/SampleReports/SampleReports.cat"}&jrd_studio_mode=view`

## Specifying the Page Report Studio View

Page Report Studio has two views: Basic View and Interactive View. When opening page reports or page report results in Page Report Studio by URL, you can use the property jrd\_studio\_mode to specify the view. If this property is not provided in the URL, the [default view](https://devnet.logianalytics.com/hc/en-us/articles/1500009686822-Configuring-Server-Profile#PageMode)  set in the server profile will be applied.

Below are the values of the property:

* basic - Displays Page Report Studio in Basic View by default and allows for switching to Interactive View.
* basic\_only - Displays Page Report Studio in Basic View only.
* interactive - Displays Page Report Studio in Interactive View by default and allows for switching to Basic View.

However for page reports and page report results saved in public folders in the server resource tree, Page Report Studio adopts a [permission control](https://devnet.logianalytics.com/hc/en-us/articles/1500009718881-Managing-Permissions) to restrict user access, so whether the specified view can be opened depends on if you have the Execute and/or Edit permissions on the page reports or page report results: Execute for Basic View and Edit for Interactive View. If you do not have the required permission on the public page report or page report result you are going to run:

* When both Execute and Edit are disabled, you will be denied to access Page Report Studio.
* When Execute is enabled but Edit is not:
  + basic - Displays Page Report Studio in Basic View, same as basic\_only.
  + interactive - Access to Page Report Studio is denied.
* When Edit is enabled but Execute is not:
  + basic and basic\_only - Access to Page Report Studio is denied.
  + interactive - Displays Page Report Studio in Interactive View.

**Examples：**

* `http://localhost:8888/webos/app/pagestudio/run.jsp?jrs.report=%2fSampleReports%2fEmployee Information List.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrd_studio_mode=interactive`
* `http://localhost:8888/webos/app/pagestudio/run.jsp?jrs.resource_path=%2fUSERFOLDERPATH%2fadmin%2ftest&jrs.file=1980996366.rsd&jrd_studio_mode=basic_only`

## Specifying a Time Duration for a Task and Notifying Someone by E-mail

Take the following examples to specify a time duration for a report run task, and ask Logi JReport Server to notify someone of the task status via e-mail if the task has not yet finished running when the task duration is up:

* Use tryView.jsp to run a report without a parameter:

  `http://localhost:8888/jinfonet/tryView.jsp?&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.report=%2fSampleReports%2fEmployee Information List.cls&jrs.timeout_send_email=true&jrs.report_timeout=5&jrs.mailto=person@company.com&jrs.mailsubject=TaskForTimeoutSendEmail&jrs.result_type=1&jrs.mailcomments=IFTHEREPORTISFINISHEDTHERESULTWILLBESENT&jrs.mailfrom=person@company.com`
* Use runReport.jsp to run a report with parameters:

  `http://localhost:8888/jinfonet/runReport.jsp?jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.report=%2fSampleReports%2fABC.cls&jrs.param$P_StartDate=2016-1-1&jrs.param$p_EndDate=2017-12-31&jrs.timeout_send_email=true&jrs.report_timeout=1&jrs.mailto=person@company.com&jrs.mailsubject=AboutTaskForTimeout&jrs.result_type=1`

You can also set a message in the e-mail by setting the property *jrs.timeout\_sendmail\_message*.

For example, you want to display message as follows:

Running <report name> takes more than <Timeout> seconds.  
 The subject is <mail subject> and has been sent to <mailto> from <mailfrom>  
 It is a file whose type is <type>.

Then you can set the property in URL as follows:

`jrs.timeout_sendmail_message=Running {6} takes more than {0} seconds.<p>The subject is {2} and has been sent to {1} from {5}.<p>It is a file whose type is {3}.`

**Where**

{0} - The report timeout  
 {1} - mail to  
 {2} - mail subject  
 {3} - result type  
 {4} - mail comment  
 {5} - mail from  
 {6} - Catalog name/report  
 <p> - an Enter key

**Example**

`http://localhost:8888/jinfonet/tryView.jsp?jrs.report=%2fSampleReports%2fEmployee Information List.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.timeout_send_email=true&jrs.report_timeout=1&jrs.mailto=person@company.com&jrs.mailsubject=AboutTaskForTimeoutSendEmail&jrs.result_type=1&jrs.mailcomments=Employee Information List&jrs.mailfrom=person@company.com&jrs.timeout_sendmail_message=.This {6} is a large report whose runtime is over {0} seconds.<p>The report is sent to {1} from {5}.<p>The subject of the mail is {2}.<p>Its type is {3}.`

**Note:** You should type the single quote sign " ' " twice if you use it in the message.

## Switching the Report Database Connection

When accessing reports via URL, you can switch the connection in the same database or between different databases at runtime by setting the properties: [jrs.jdbc\_url, jrs.jdbc\_driver, jrs.db\_user and jrs.db\_pswd](https://devnet.logianalytics.com/hc/en-us/articles/1500009686482-Appendix-1-URL-Properties#DB). As a result, if the databases you want to switch between have the same structure, you will then be free from having to build another similar catalog. You can use the switch database commands to set the JDBC connection or to change the user name/password in order to connect to another database.

**See also:**

* [Opening Web Reports in Web Report Studio via JSON](#jrd_datasources) for switching connection for web reports via JSON
* [Running Dashboards via URL](https://devnet.logianalytics.com/hc/en-us/articles/1500009692962-Working-with-Dashboards#dsh_datasources) for switching connection for dashboards

**Switching the connection and user/password in the same database**

* Set the Oracle database named oracle815 connection when designing the report Report1.cls, and later switch the connection to the Oracle database named demo at runtime.

  The URL for switching the connection:

  `http://localhost:8888/jinfonet/tryView.jsp?jrs.report=%2fSampleReports%2fReport1.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=1&jrs.jdbc_url=jdbc:oracle:thin:@host:1521:demo`
* Set the SQL database named MBA2000 when designing the report Report1.cls, and later switch the connection to the SQL database named JTTest at runtime.

  The URL for switching the connection:

  `http://localhost:8888/jinfonet/tryView.jsp?jrs.report=%2fSampleReports%2fReport1.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=1&jrs.jdbc_url=jdbc:inetdae:host:1433?database=JTTest&sql7=true`
* Specify the user ID system/manager to ensure security when designing the web report Report2.wls, and then switch to the user ID Scott and the password tiger when running the report in Web Report Studio.

  The URL for switching the user ID and password:

  `http://localhost:8888/jinfonet/tryView.jsp?jrs.report=/SampleReports/Report2.wls&jrs.catalog=/SampleReports/SampleReports.cat&jrs.result_type=8&jrs.db_user=Scott&jrs.db_pswd=tiger`
* Set the Sybase 12 database named master when designing the web report Report2.wls, and later switch the connection to the Sybase 12 database named product at runtime.

  The URL for switching the connection:

  `http://localhost:8888/jinfonet/tryView.jsp?jrs.report=%2fSampleReports%2fReport2.wls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=1&jrs.jdbc_url=jdbc:sybase:Tds:host:5000/product`

**Switching the connection between different databases with the same database metadata**

* Set oracle815 connection when designing the report Report1.cls, and then switch the connection to Access database with the JDBC-ODBC driver named products at runtime.

  The URL for switching the connection:

  `http://localhost:8888/jinfonet/tryView.jsp?jrs.report=%2fSampleReports%2fReport1.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=1&jrs.jdbc_driver=sun.jdbc.odbc.JdbcOdbcDriver&jrs.jdbc_url=jdbc:odbc:products`
* Set oracle815 connection when designing the web report Report2.wls, and then switch the connection to SQL server database named products at runtime.

  The URL for switching the connection:

  `http://localhost:8888/jinfonet/tryView.jsp?jrs.report=%2fSampleReports%2fReport2.wls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=1&jrs.jdbc_driver=com.inet.tds.TdsDriver&jrs.jdbc_url=jdbc:inetdae:JT_P05:1433?database=products&sql7=true`

**Switching the connection between different databases with different database metadata**

When connecting to a different database with different database metadata or data metadata, you need to also specify the following properties to set the target database metadata information if there are differences:

* **jrs.db\_refresh\_support\_info**  
   Optional. If it is true, Logi JReport will get support information including reverse words, quote characters, and so on from the driver each time fetching data from the database. If it is not set, the property will be treated as false. It is recommended that you set this property to true when connecting to a different database.
* **jrs.db\_quote\_character**  
   Optional. Specifies the quote characters.
* **jrs.db\_extra\_characters**  
   Optional. Specifies the extra characters.
* **jrs.db\_date\_format**  
   Optional. Specifies the date format.
* **jrs.db\_datetime\_format**  
   Optional. Specifies the datetime format.
* **jrs.db\_time\_format**  
   Optional. Specifies the time format.
* **jrs.db\_transaction\_readonly**  
   Optional. Specifies the transaction "read only" property. Possible value: "default", "Read only", or "Read&Write". Ignore other values.
* **jrs.db\_transaction\_mode**  
   Optional. Specifies the transaction mode. Possible value: "default", "None", "Read Uncommitted", "Read Committed", "Repeatable Read", or "Serializable". Ignore other values.
* **jrs.db\_char\_to\_be\_replaced**  
   Optional. Specifies the characters that are to be replaced.
* **jrs.db\_char\_replaced\_by**  
   Optional. Specifies the characters used to replace the characters specified by jrs.db\_char\_to\_be\_replaced.

The URL for switching the database to Oracle when running the page report report1.cls:

`http://localhost:8080/remote/sub/jinfonet/tryView.jsp?jrs.catalog=/Test/Test.cat&jrs.report=/Test/report1.cls&jrs.cmd=jrs.try_vw&jrs.result_type=8&jrs.jdbc_driver=oracle.jdbc.driver.OracleDriver&jrs.jdbc_url=jdbc:oracle:thin:@192.168.0.1:1521:oracle9&jrs.db_user=test&jrs.db_pswd=1234&jrs.db_quote_character="&jrs.db_date_format=M/d/yyyy&jrs.db_datetime_format=d/M/yyyy h:mm:ss a&jrs.db_time_format=HH:mm:ss.SSS&jrs.db_transaction_readonly=Read Only&jrs.db_transaction_mode=Repeatable Read&jrs.db_char_to_be_replaced=}&jrs.db_char_replaced_by=}oracle91234`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009692942-Working-on-Logi-JReport-Server-via-URLs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009693022-Scheduling-Reports)
