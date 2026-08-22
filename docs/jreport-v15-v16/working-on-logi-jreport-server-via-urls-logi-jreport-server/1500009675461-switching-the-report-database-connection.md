---
title: "Switching the Report Database Connection"
id: 1500009675461
section: "Working on Logi JReport Server via URLs Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009675461-Switching-the-Report-Database-Connection
updated_at: 2021-07-24T20:53:31Z
---

# Switching the Report Database Connection

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650482-Specifying-a-Time-Duration-for-a-Task-and-Notifying-Someone-by-E-mail)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009650522-Scheduling-Reports)

# Switching the Report Database Connection

When accessing reports via URL, you can switch the connection in the same database or between different databases at runtime by setting the properties: [jrs.jdbc\_url, jrs.jdbc\_driver, jrs.db\_user and jrs.db\_pswd](https://devnet.logianalytics.com/hc/en-us/articles/1500009668881-Appendix-1-URL-Properties#DB). As a result, if the databases you want to switch between have the same structure, you will then be free from having to build another similar catalog. You can use the switch database commands to set the JDBC connection or to change the user name/password in order to connect to another database.

**See also:**

* [Opening Web Reports in Web Report Studio via JSON](https://devnet.logianalytics.com/hc/en-us/articles/1500009675501-Opening-Web-Reports-in-Web-Report-Studio-via-JSON#jrd_datasources) for switching connection for web reports via JSON
* [Running Dashboards via URL](https://devnet.logianalytics.com/hc/en-us/articles/1500009650422-Working-With-Dashboards#dsh_datasources) for switching connection for dashboards

Below is a list of the sections covered in this topic:

* [Switching the Connection and User/Password in the Same Database](#Same)
* [Switching the Connection Between Different Databases With the Same Database Metadata](#Meta)
* [Switching the Connection Between Different Databases With Different Database Metadata](#Dif)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Switching the Connection and User/Password in the Same Database

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

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Switching the Connection Between Different Databases With the Same Database Metadata

* Set oracle815 connection when designing the report Report1.cls, and then switch the connection to Access database with the JDBC-ODBC driver named products at runtime.

  The URL for switching the connection:

  `http://localhost:8888/jinfonet/tryView.jsp?jrs.report=%2fSampleReports%2fReport1.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=1&jrs.jdbc_driver=sun.jdbc.odbc.JdbcOdbcDriver&jrs.jdbc_url=jdbc:odbc:products`
* Set oracle815 connection when designing the web report Report2.wls, and then switch the connection to SQL server database named products at runtime.

  The URL for switching the connection:

  `http://localhost:8888/jinfonet/tryView.jsp?jrs.report=%2fSampleReports%2fReport2.wls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=1&jrs.jdbc_driver=com.inet.tds.TdsDriver&jrs.jdbc_url=jdbc:inetdae:JT_P05:1433?database=products&sql7=true`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Switching the Connection Between Different Databases With Different Database Metadata

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
   Optional. Specifies the characters used to replace the characters specified by *jrs.db\_char\_to\_be\_replaced*.

The URL for switching the database to Oracle when running the page report report1.cls:

`http://localhost:8080/remote/sub/jinfonet/tryView.jsp?jrs.catalog=/Test/Test.cat&jrs.report=/Test/report1.cls&jrs.cmd=jrs.try_vw&jrs.result_type=8&jrs.jdbc_driver=oracle.jdbc.driver.OracleDriver&jrs.jdbc_url=jdbc:oracle:thin:@192.168.0.1:1521:oracle9&jrs.db_user=test&jrs.db_pswd=1234&jrs.db_quote_character="&jrs.db_date_format=M/d/yyyy&jrs.db_datetime_format=d/M/yyyy h:mm:ss a&jrs.db_time_format=HH:mm:ss.SSS&jrs.db_transaction_readonly=Read Only&jrs.db_transaction_mode=Repeatable Read&jrs.db_char_to_be_replaced=}&jrs.db_char_replaced_by=}oracle91234`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650482-Specifying-a-Time-Duration-for-a-Task-and-Notifying-Someone-by-E-mail)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009650522-Scheduling-Reports)
