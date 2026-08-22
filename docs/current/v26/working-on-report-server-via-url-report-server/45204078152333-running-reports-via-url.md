---
title: "Running Reports via URL"
id: 45204078152333
section: "Working on Report Server via URL Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45204078152333-Running-Reports-via-URL
updated_at: 2026-04-30T14:11:06Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Running Reports via URL

This topic describes how you can use the three JSPs to run reports via URL: tryView.jsp, runReport.jsp, and run.jsp.

However, Page Report Studio and Web Report Studio have permission control. To run reports in them, you should have the Execute and/or Edit permissions on the reports.

The image illustrates the relationship between the JSPs:

Note: The customer can specify only the report and report version (without specifying the catalog) in the URL, provided that the report and version are associated with a report-catalog relation, which can be retrieved via the web API endpoint GET /node/rptcatrelation.

tryView.jsp

This is the normal method of accessing reports using URL. You can use tryView.jsp to run page reports and web reports to any formats that Server supports.

If the report has parameters and you do not set any parameters in the URL or the parameters in the URL fail to include all necessary parameters, Server displays the parameter dialog box for specifying parameter values.

See the examples: 

- Run a page report in Page Report Studio:
http://localhost:8888/jinfonet/tryView.jsp?jrs.report=%2fSampleReports%2fEmployee Information List.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=8

- Run a page report in PDF:
http://localhost:8888/jinfonet/tryView.jsp?jrs.report=%2fSampleReports%2fEmployee Information List.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=2

- Run a web report in Web Report Studio: 
http://localhost:8888/jinfonet/tryView.jsp?&jrs.report=%2fSampleReports%2fSales Detail Report.wls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=8

- Run a web report in HTML: 
http://localhost:8888/jinfonet/tryView.jsp?&jrs.report=%2fSampleReports%2fSales Detail Report.wls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=1

runReport.jsp

This JSP functions the same as tryView.jsp when the report has no parameters. When it has parameters, Server runs the report with the default parameter values if you specify no parameter values, or else it runs with the parameter values you specified in the URL.

You can use runReport.jsp to run page reports and web reports to any formats that Server supports.

See the examples:

- Run a page report in HTML: 
http://localhost:8888/jinfonet/runReport.jsp?jrs.report=%2fSampleReports%2fABC.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=1&&jrs.param$P_StartDate=2016-01-01&jrs.param$p_EndDate=2017-12-31

- Run a web report in Web Report Studio:
http://localhost:8888/jinfonet/runReport.jsp?jrs.report=%2fSampleReports%2fSales Detail Report.wls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=8

run.jsp

You can use run.jsp to run page reports in Page Report Studio and web reports in Web Report Studio. When a report has parameters, Server runs the report with the default parameter values if you specify no parameter values, or else it runs with the parameter values you specified in the URL.

- The URL entry for running web reports in Web Report Studio is: webreport/studio/entry/run.jsp. For more information, see Opening Web Reports in Web Report Studio Via JSON.

- The URL entry for running page reports and page report result files in Page Report Studio is: webos/app/pagestudio/run.jsp. For example: 
http://localhost:8888/webos/app/pagestudio/run.jsp?jrs.report=%2fSampleReports%2fEmployee Information List.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat

You can use run.jsp in the following scenarios:

- 
Working with Dashboards via URL. The URL entry is: dashboard/app/entry/run.jsp.

- 
Accessing Visual Analysis via URL. The URL entry is: webos/app/designer/run.jsp.

- 
Creating a Web Report in the Traditional Wizard Way via URL. The URL entry is: webos/app/webstudio/run.jsp?jrd_wizard=1&.

- 
Creating a Web Report Using the Quick Start Method via URL. The URL entry is: webos/app/webstudio/run.jsp.

- 
Viewing page report result files  in Page Report Studio.

In addition to the preceding JSPs, you can call the server servlet jrserver to run reports to any allowed format. However, when you use servlet to run a report, Report redirects the request to an appropriate JSP, so you should use JSP to run the report directly. See the two examples: 

- Run a page report in Page Report Studio:
http://localhost:8888/jrserver/SampleReports/SampleReports.cat/Employee Information List.cls?jrs.cmd=jrs.web_vw&jrs.result_type=8

- Run a web report to HTML:
http://localhost:8888/jrserver/SampleReports/SampleReports.cat/Sales Detail Report.wls?jrs.cmd=jrs.web_vw&jrs.result_type=1

 For more information, see URL Properties for Running, Scheduling, and Viewing Reports via URL.

This topic contains the following sections:

- Running a Report Tab in a Page Report via URL
                

- Refreshing Page Report Data Automatically via URL                

- Opening Web Reports in Web Report Studio via JSON
                

- Specifying the Web Report Studio Mode via URL
                

- Specifying the Page Report Studio View via URL
                

- Specifying a Time Duration for a Task and Notifying Someone by Email via URL
                

- Switching the Report Database Connection via URL
                

## 
Running a Report Tab in a Page Report via URL

If you want to run a specific page report tab, use jrs.report_sheet$RPT_TAB_NAME=true to specify a report tab in the current page report, where RPT_TAB_NAME is the report name of the specific report tab, not the display name. For example, jrs.report_sheet$Report2=true. 

To get the report name and display name of a page report tab, you can open the page report in Report Designer and look at the Instance Name property in the Report Inspector, or you can make use of the API methods getName() and getDisplayName() in the jet.server.api.ReportSheetInfo  interface (for more information, see the Report Javadoc). 

The URL for running the report tab Financial report in Page Report Studio within the report Detail Report Corporate Overview.cls is: 

http://localhost:8888/jinfonet/tryView.jsp?jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.report=%2fSampleReports%2fDetail Report Corporate Overview.cls&jrs.result_type=8&jrs.report_sheet$report2=true

## 
Refreshing Page Report Data Automatically via URL

When running a page report in Page Report Studio, you can ask Report to automatically refresh the report data at certain intervals. To achieve this, you need to run the report with run.jsp and add the two properties in the URL:

- 
jrs.auto_refresh_data=true
    Server automatically refreshes the report data. 

- 
jrs.auto_refresh_data_time=[a number in seconds]
    The time interval after which Server refreshes the report data.

See the URL example: 

http://localhost:8888/webos/app/pagestudio/run.jsp?jrs.report=%2fSampleReports%2fEmployee Information List.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.auto_refresh_data=true&jrs.auto_refresh_data_time=10

## 
Opening Web Reports in Web Report Studio via JSON

Report provides properties for developer users to run web reports in Web Report Studio via JavaScript Object Notation (JSON).

This section lists the properties that Server encapsulates as JSON objects. It will help if you obtain the knowledge on JSON to understand the syntax more clearly.

- jrd_report={
    "name":"xxx", // The full path of a web report.
    "ver":-1, // Optional. The report version. -1 means the latest version.
    }

- jrd_catalog={
    "name":"xxx", // The full path of the catalog that the web report uses.
    "ver":-1, // Optional. The catalog version. -1 means the latest version. 
    }

- jrd_param$={
    "p1":"value1", // p1 is a parameter name, and value1 is p1's value.
    "p2":["value1","value2","value3"] // For multiple values.
    }

- jrd_userinfo={ // Optional.
    "user":"xxx", // Username.
    "country":"us", // The locale representing the region part for running reports, following the locale naming specification.
    "language":"en", // The locale representing the language part for running reports, following the locale naming specification.
    "encoding":"UTF-8", // The encoding for running reports.
    "resolution":"96" // The resolution for displaying reports.
"prefer":{
  "rpt_timezone":"CST", // The time zone for displaying date and time in reports.
"bookmark":"xxx" // Specify the name of a bookmark that you saved for the web report to run the bookmark.
  }
    }

-  jrd_security_file_name={ // Optional. 
    "name":"xxx", // The name of a security file. When you provide a security file, the security definition you defined in the security file will replace that in the specified catalog.
    } 

- 
jrd_datasources=[
    // Optional.
    // Server supports these types of external data sources:
    // 0 - JDBC data source, 1 - JNDI data source, 2 - Java DataSource object, 3 - Connection object, 4 - ResultSet object, and 9 - MongoDB data source.
    // You can include one or multiple data sources at a time.
    { 
        // JDBC data source.
        "ds":"Data Source 1", // Data source name.
        "uid":"xxx", // DB username.
        "pwd":"xxx", // DB user password.
        "type":0, // 0 means JDBC data source.
        "url":"xxx", // JDBC URL. For example, "url":"jdbc:oracle:thin:@127.0.0.1:1521:ora8i".
        "driver":"xxx" // JDBC driver. For example, "driver":"oracle.jdbc.driver.OracleDriver".

        // When connecting to a different database with different database metadata or data metadata, you need to also specify the following commands to set the target database metadata information if there are differences:
       "refresh_support_info":True, // Optional. Value: True/False. If it is True, Report will get support information such as reverse words and quote characters from the driver each time fetching data from the database. You should set this property to True when connecting to a different database.
        "quote_character":"xxx", // Optional. The quote characters.
        "extra_characters":"xxx", // Optional. The extra characters.
        "date_format":"xxx", // Optional. The date format.
        "datetime_format":"xxx", // Optional. The datetime format.
        "time_format":"xxx", // Optional. The time format.
        "transaction_readonly":"xxx", // Optional. The transaction "read only" property. Possible value: default, read only, or read & write. Server ignores other values.
        "transaction_mode":"xxx", // Optional. The transaction mode. Possible value: default, none, read uncommitted, read committed, repeatable read, or serializable. Server ignores other values. 
        "char_to_be_replaced":"xxx", // Optional. The characters that you want to replace. 
        "char_replaced_by":"xxx" // Optional. The characters that you use to replace the characters specified by char_to_be_replaced.
        },

        { 
        // JNDI data source. Currently Report only supports local JNDI with anonymous lookup, which means that the JNDI data source and the report server are in one JVM and the JNDI needs no authentication.
        "ds":"Data Source 2", // Data source name.
        "uid":"xxx", // DB username.
        "pwd":"xxx", // DB user password.
        "type":1, // 1 means JNDI data source.
        "url":"xxx", // JNDI name. For example, "url":"jndi/testDB". 
        },

{
// MongoDB data source.
        "ds":"Data Source 3", // Data source name.
 "connection":"xxxx", // Connection Name.
        "uid":"xxx", // DB username.
        "pwd":"xxx", // DB user password.
        "type":9, // 9 means MongoDB data source.
        "url":"xxx", // MongoDB URL. For example,        "url":"mongodb://192.127.000.1:27017".
"driver":"xxx", // MongoDB driver. For example, "driver":"toolkit.db.mongo.MongoDriver".
"mongodb_databases":[
// The database list in the MongoDB connection, which is an array.
 {
    "mongodb_catdb":"xxx", // The database name you defined in the catalog for MongoDB.
    "mongodb_dbname":"xx", // The new database name you want to use at runtime to replace the original database name you defined in MongoDB APE.
    "mongodb_collections":[
    // The collection list in a MongoDB database, which is an array.
    {
        "mongodb_catcollection":"xxx", // The collection name you defined in the catalog for MongoDB.
        "mongodb_collection":"xxx" // The new collection name you want to use at runtime to replace the original collection name you defined in MongoDB APE.
    }
    ]
}
]
},

        { 
        // Java DataSource object/Connection object/ResultSet object.
        // You should define the request or session attribute, then the attribute key is the one you defined in the request.
        // For example, write user.jsp as:
        // String key = "Rst";
        // java.sql.ResultSet rst = null;
        // rst = // Gets result set object from your business logic.
        // request.setAttribute("Rst", rst); 
        // Then the key would be: "key":"Rst".
        // The preceding example is based on the ResultSet object. It also applies to the other two types.
        "ds":"Data Source 4", // Data source name.
        "type":2/3/4, // 2 means Java DataSource object, 3 Connection object, and 4 ResultSet object.
        "key":"xxx" // Request attribute object name, included in the request or session.
    }    

]

- 
jrd_studio_mode // The Web Report Studio mode.

- jrd_responsive
// Optional. Set this property to false if you want to turn off  Responsive View in the View Mode of Web Report Studio on computers.

- 
jrd_filters={
    "osf":[
        // Values of the on-screen filters in the report. There are two ways to designate an on-screen filter. One is by the instance name of the filter and the other by the field that is bound with the filter. 
      

{
// An on-screen filter and its values. 

	       "name":"fc1", // The instance name of an on-screen filter.
         "reverse":false, // Optional. If true, the values of the on-screen filter are those you do not specify in the "values" property.
         "selectAll":false, // Optional. If true, it means to apply all the values at runtime and ignore the "values" property.
      "values":["USA","China"] // The values of the on-screen filter. 
}, 

{
  "field":{         
          
         // A field that is bound with an on-screen filter and the values of the field.      

"type":2, // The data resource type. 0 means it is a query and 2 means business view.
	       "ds":"DataSource 1", // The data source name.
	       "query":"Query 1", // Optional. The query name. You should specify the property when the data resource type is query.
	       "bv":"BV 1", // Optional. The business view name. You should specify the property when the data resource type is business view. 
         "name":"Customers.Country" // The mapping name of the field if the data resource type is query, or the qualified display name of	the field if the data resource type is business view.		 

},      
	       "reverse":false, // Optional. If true, the values of the field are those you do not specify in the "values" property.
"selectAll":false, // Optional. If true, it means to apply all the values at runtime and ignore the "values" property. 
	       "values":["USA","China"] // The values of the field.
	       }

] 

}

- jrd_root_folder
// Optional. Specify a folder in the Public Reports folder to replace the default Public Reports folder in the Save As and Open dialog boxes.
            

- jrd_show_myfolder
// Optional. Set the property to false if you don't want to show the My Reports folder in the Save As and Open dialog boxes.
            

When composing the URL, you need to use URL encoding to avoid errors.

Here is an example of the complete URL without URL encoding to make it easier to read:

http://localhost:8888/webreport/studio/entry/run.jsp?jrd_report={"name":"/SampleReports/report.wls","ver":-1}&jrd_catalog={"name":"/SampleReports/SampleReports.cat","ver":-1}&jrd_param$={"P_Coutry":"USA"}&jrd_filters={"osf":[{"name":"FilterControl","values":["USA","China"]}]}&jrd_security_file_name={"name":"SampleReports.security.xml"}&jrd_datasources=[{"ds":"Data Source 1","uid":"xxx","pwd":"xxx","type":0,"url":"xxx","driver":"xxx"},{"ds":"Data Source 2","type":2,"key":"xxx"}]

If you use absolute resource path, you need to add the property "real":true for the path. For example,

jrd_report={"name":"C:\\LogiReport\\Server\\jreports\\SampleReports\\Sales Detail Report.wls","real":true}&jrd_catalog={"name":"C:\\LogiReport\\Server\\jreports\\SampleReports\\SampleReports.cat","real":true}

Run Sales Detail Report.wls in the Public Reports > SampleReports folder:

http://localhost:8888/webreport/studio/entry/run.jsp?jrd_report={"name":"/SampleReports/Sales Detail Report.wls"}&jrd_catalog={"name":"/SampleReports/SampleReports.cat"}

## 
Specifying the Web Report Studio Mode via URL

Web Report Studio has two modes: View Mode and Edit Mode. When opening web reports in Web Report Studio by URL, you can use the property jrd_studio_mode to specify the mode. If you do not provide this property in the URL, the default mode you set in the server profile applies.

See the values of the property:

- 
view - Web Report Studio opens in the View Mode by default. You can switch to the Edit Mode.

- 
view_only - Web Report Studio opens in the View Mode only.

- 
edit - Web Report Studio opens in the Edit Mode by default. You can switch to the View Mode.

However, for web reports in public folders in the server resource tree, Web Report Studio adopts a permission control to restrict user access, so whether you can access the specified mode depends on whether you have the Execute and/or Edit permissions on the web reports: Execute for View Mode and Edit for Edit Mode. If you do not have the required permission on the public web report you are going to run:

- When you have neither Execute nor Edit permissions, you cannot access Web Report Studio.

-  When you have the Execute permissions but not Edit:
    
-  view - Web Report Studio opens in the View Mode, same as view_only.

-  edit - You cannot access Web Report Studio.

- When you have the Edit permissions but not Execute:
    
- view and view_only - You cannot access Web Report Studio.

-  edit - Web Report Studio opens in the Edit Mode.

Example：

http://localhost:8888/webreport/studio/entry/run.jsp?jrd_report={"name":"/SampleReports/Sales Detail Report.wls"}&jrd_catalog={"name":"/SampleReports/SampleReports.cat"}&jrd_studio_mode=view

## 
Specifying the Page Report Studio View via URL

Page Report Studio has two views: Basic View and Interactive View. When opening page reports or page report results in Page Report Studio by URL, you can use the jrd_studio_mode property to specify the view. If you do not provide this property in the URL, the default view you set in the server profile applies.

See the values of the property:

- 
basic - Page Report Studio opens in the Basic View by default. You can switch to the Interactive View.

- 
basic_only - Page Report Studio opens in the Basic View only.

- 
interactive - Page Report Studio opens in the Interactive View by default. You can switch to the Basic View.

However, for page reports and page report results in public folders in the server resource tree, Page Report Studio adopts a permission control to restrict user access, so whether you can access the specified view depends on whether you have the Execute and/or Edit permissions on the page reports or page report results: Execute for Basic View and Edit for Interactive View. If you do not have the required permission on the public page report or page report result you are going to run:

- When you have neither Execute nor Edit permissions, you cannot access Page Report Studio.

-  When you have the Execute permission but not Edit:
    
-  basic - Page Report Studio opens in the Basic View, same as basic_only.

-  interactive - You cannot access Page Report Studio.

- When you have the Edit permission but not Execute:
    
-  basic and basic_only - You cannot access Page Report Studio.

-  interactive - Page Report Studio opens in Interactive View.

Examples：

- http://localhost:8888/webos/app/pagestudio/run.jsp?jrs.report=%2fSampleReports%2fEmployee Information List.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrd_studio_mode=interactive

- http://localhost:8888/webos/app/pagestudio/run.jsp?jrs.resource_path=%2fUSERFOLDERPATH%2fadmin%2ftest&jrs.file=1980996366.rsd&jrd_studio_mode=basic_only

## 
Specifying a Time Duration for a Task and Notifying Someone by Email via URL

Take the following examples to specify a time duration for a report run task, and ask Server to notify someone of the task status via email if the task has not yet finished running when the task duration is up:

- 
Use tryView.jsp to run a report without a parameter:

http://localhost:8888/jinfonet/tryView.jsp?&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.report=%2fSampleReports%2fEmployee Information List.cls&jrs.timeout_send_email=true&jrs.report_timeout=5&jrs.mailto=person@company.com&jrs.mailsubject=TaskForTimeoutSendEmail&jrs.result_type=1&jrs.mailcomments=IFTHEREPORTISFINISHEDTHERESULTWILLBESENT&jrs.mailfrom=person@company.com

- 
Use runReport.jsp to run a report with parameters:

http://localhost:8888/jinfonet/runReport.jsp?jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.report=%2fSampleReports%2fABC.cls&jrs.param$P_StartDate=2016-1-1&jrs.param$p_EndDate=2017-12-31&jrs.timeout_send_email=true&jrs.report_timeout=1&jrs.mailto=person@company.com&jrs.mailsubject=AboutTaskForTimeout&jrs.result_type=1

You can also set a message in the email by setting the property jrs.timeout_sendmail_message.

For example, you want to display message as follows:

Running <report name> takes more than <Timeout> seconds.
  The subject is <mail subject> and has been sent to <mailto> from <mailfrom>
  It is a file whose type is <type>.

Then you can set the property in URL:

jrs.timeout_sendmail_message=Running {6} takes more than {0} seconds.<p>The subject is {2} and has been sent to {1} from {5}.<p>It is a file whose type is {3}.

Where

{0} - The report timeout
{1} - mail to
{2} - mail subject
{3} - result type
{4} - mail comment
{5} - mail from
{6} - Catalog_name/report
 <p> - an Enter key

Example

http://localhost:8888/jinfonet/tryView.jsp?jrs.report=%2fSampleReports%2fEmployee Information List.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.timeout_send_email=true&jrs.report_timeout=1&jrs.mailto=person@company.com&jrs.mailsubject=AboutTaskForTimeoutSendEmail&jrs.result_type=1&jrs.mailcomments=Employee Information List&jrs.mailfrom=person@company.com&jrs.timeout_sendmail_message=.This {6} is a large report whose runtime is over {0} seconds.<p>The report is sent to {1} from {5}.<p>The subject of the mail is {2}.<p>Its type is {3}.

You should type the single quote sign (') twice if you use it in the message.

## 
Switching the Report Database Connection via URL

When accessing reports via URL, you can switch the connection in the same database or between different databases at runtime by setting the properties: jrs.jdbc_url, jrs.jdbc_driver, jrs.db_user, and jrs.db_pswd. As a result, if the databases you want to switch between have the same structure, you will then be free from having to build another similar catalog. You can use the switch database commands to set the JDBC connection or to change the username/password to connect to another database.

See also:

- 
Opening Web Reports in Web Report Studio via JSON for switching connections for web reports via JSON

- 
Running Dashboards via URL for switching connections for dashboards

Switching the connection and user/password in the same database 

- Set the Oracle database named oracle815 connection when designing the report Report1.cls, and later switch the connection to the Oracle database named demo at runtime.
    The URL for switching the connection:

http://localhost:8888/jinfonet/tryView.jsp?jrs.report=%2fSampleReports%2fReport1.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=1&jrs.jdbc_url=jdbc:oracle:thin:@host:1521:demo

- Set the SQL database named MBA2000 when designing the report Report1.cls, and later switch the connection to the SQL database named JTTest at runtime.
    The URL for switching the connection:

http://localhost:8888/jinfonet/tryView.jsp?jrs.report=%2fSampleReports%2fReport1.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=1&jrs.jdbc_url=jdbc:inetdae:host:1433?database=JTTest&sql7=true

- Specify the user ID system/manager to ensure security when designing the web report Report2.wls, and then switch to the user ID Scott and the password tiger when running the report in Web Report Studio.
    The URL for switching the user ID and password:

http://localhost:8888/jinfonet/tryView.jsp?jrs.report=/SampleReports/Report2.wls&jrs.catalog=/SampleReports/SampleReports.cat&jrs.result_type=8&jrs.db_user=Scott&jrs.db_pswd=tiger

- Set the Sybase 12 database named master when designing the web report Report2.wls, and later switch the connection to the Sybase 12 database named product at runtime.
    The URL for switching the connection:

http://localhost:8888/jinfonet/tryView.jsp?jrs.report=%2fSampleReports%2fReport2.wls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=1&jrs.jdbc_url=jdbc:sybase:Tds:host:5000/product

Switching the connection between different databases with the same database metadata

- Set oracle815 connection when designing the report Report1.cls, and then switch the connection to Access database with the JDBC-ODBC driver named products at runtime.
    The URL for switching the connection:

http://localhost:8888/jinfonet/tryView.jsp?jrs.report=%2fSampleReports%2fReport1.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=1&jrs.jdbc_driver=sun.jdbc.odbc.JdbcOdbcDriver&jrs.jdbc_url=jdbc:odbc:products

- Set oracle815 connection when designing the web report Report2.wls, and then switch the connection to SQL server database named products at runtime.
    The URL for switching the connection:

http://localhost:8888/jinfonet/tryView.jsp?jrs.report=%2fSampleReports%2fReport2.wls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=1&jrs.jdbc_driver=com.inet.tds.TdsDriver&jrs.jdbc_url=jdbc:inetdae:JT_P05:1433?database=products&sql7=true

Switching the connection between different databases with different database metadata

When connecting to a different database with different database metadata or data metadata, you need to also specify the following properties to set the target database metadata information if there are differences:

| Property | Description |
| --- | --- |
| jrs.db_refresh_support_info | Optional. If it is true, Report gets support information such as reverse words and quote characters from the driver each time fetching data from the database. If you do not set it, Server treats the property as false. You should set this property to true when connecting to a different database. |
| jrs.db_quote_character | Optional. The quote characters. |
| jrs.db_extra_characters | Optional. The extra characters. |
| jrs.db_date_format | Optional. The date format. |
| jrs.db_datetime_format | Optional. The datetime format. |
| jrs.db_time_format | Optional. The time format. |
| jrs.db_transaction_readonly | Optional. The transaction "read only" property. Possible value: "default", "read only", or "read & write". Server ignores other values. |
| jrs.db_transaction_mode | Optional. The transaction mode. Possible value: "default", "none", "read uncommitted", "read committed", "repeatable read", or "serializable". Server ignores other values. |
| jrs.db_char_to_be_replaced | Optional. The characters that you want to replace. |
| jrs.db_char_replaced_by | Optional. The characters you use to replace the characters specified by jrs.db_char_to_be_replaced. |

The URL for switching the database to Oracle when running the page report report1.cls:

http://localhost:8080/remote/sub/jinfonet/tryView.jsp?jrs.catalog=/Test/Test.cat&jrs.report=/Test/report1.cls&jrs.cmd=jrs.try_vw&jrs.result_type=8&jrs.jdbc_driver=oracle.jdbc.driver.OracleDriver&jrs.jdbc_url=jdbc:oracle:thin:@192.168.0.1:1521:oracle9&jrs.db_user=test&jrs.db_pswd=1234&jrs.db_quote_character="&jrs.db_date_format=M/d/yyyy&jrs.db_datetime_format=d/M/yyyy h:mm:ss a&jrs.db_time_format=HH:mm:ss.SSS&jrs.db_transaction_readonly=Read Only&jrs.db_transaction_mode=Repeatable Read&jrs.db_char_to_be_replaced=}&jrs.db_char_replaced_by=}oracle91234
