---
title: "Opening Web Reports in Web Report Studio via JSON"
id: 1500009675501
section: "Working on Logi JReport Server via URLs Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009675501-Opening-Web-Reports-in-Web-Report-Studio-via-JSON
updated_at: 2021-07-24T20:53:30Z
---

# Opening Web Reports in Web Report Studio via JSON

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675441-Refreshing-Page-Report-Data-Automatically)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009650502-Specifying-the-Report-Studio-Mode)

# Opening Web Reports in Web Report Studio via JSON

Logi JReport provides properties for developer users to run web reports in Web Report Studio via JSON (JavaScript Object Notation).

The following lists the properties that are encapsulated as JSON objects. It will help if you obtain some knowledge on JSON to understand the syntax more clearly.

* jrd\_report={  
   "name":"xxx", // The full path of the web report.  
   "ver":"-1", // Optional. The report version. -1 means the latest version.  
   }
* jrd\_catalog={  
   "name":"xxx", // The full path of the catalog that the web report uses.  
   "ver":"-1", // Optional. The catalog version. -1 means the latest version.   
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
* jrd\_security\_file\_name={  
   "name":"xxx", // The name of a [security file](https://devnet.logianalytics.com/hc/en-us/articles/1500009674921-Dynamic-Security). When a security file is given, the security definitions in the specified catalog will be replaced by that defined in the security file.  
   // Optional.   
   }
* jrd\_datasources=[  
   // Optional.  
   // The following types of external data sources are supported:  
   // 0 - JDBC data source, 1 - JNDI data source, 2 - Java DataSource object, 3 - Connection object, 4 - ResultSet object.  
   // One or multiple data sources can be included at a time.

  ```
  {   
          // JDBC data source.  
          "ds":"Data Source 1", // Data source name.  
          "uid":"xxx", // DB user name.  
          "pwd":"xxx", // DB user password.  
          "type":"0", // Indicates it is JDBC data source.  
          "url":"xxx", // JDBC URL. For example, "url":"jdbc:oracle:thin:@127.0.0.1:1521:ora8i".  
          "driver":"xxx" // JDBC driver. For example, "driver":"oracle.jdbc.driver.OracleDriver".  
    
          // When connecting to a different database with different database metadata or data metadata, you need to also specify the following commands to set the target database metadata information if there are differences:  
          "refresh_support_info":"True", // Optional. Value: True/False. If it is true, Logi JReport will get support information including reverse words, quote characters, and so on from the driver each time fetching data from the database. It is recommended that you set this property to true when connecting to a different database.  
          "quote_character":"xxx", // Optional. The quote characters.  
          "extra_characters":"xxx", // Optional. The extra characters.  
          "date_format":"xxx", // Optional. The date format.  
          "datetime_format":"xxx", // Optional. The datetime format.  
          "time_format":"xxx", // Optional. The time format.  
          "transaction_readonly":"xxx", // Optional. The transaction "read only" property. Possible value: default, Read only, or Read&Write. Ignore other values.  
          "transaction_mode":"xxx", // Optional. The transaction mode. Possible value: default, None, Read Uncommitted, Read Committed, Repeatable Read, or Serializable. Ignore other values.   
          "char_to_be_replaced":"xxx", // Optional. The characters that are to be replaced.   
          "char_replaced_by":"xxx" // Optional. The characters used to replace the characters specified by char_to_be_replaced.  
          },  
    
          {   
          // JNDI data source. Currently Logi JReport only supports local JNDI with anonymous lookup which means that the JNDI data source and the report server are in one JVM and the JNDI needs no authentication.  
          "ds":"Data Source 2", // Data source name.  
          "uid":"xxx", // DB user name.  
          "pwd":"xxx", // DB user password.  
          "type":"1", // Indicates it is JNDI data source.  
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
          "type":"2/3/4", // Indicates the data source type.  
          "key":"xxx" // Request attribute object name, included in request or session.  
          }
  ```

  `]`
* [jrd\_studio\_mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009650502-Specifying-the-Report-Studio-Mode) // Specifies which Web Report Studio mode is available.

When composing the URL, you need to use URL encoding to avoid errors.

Here is an example of the complete URL without URL encoding to make it easier to read:

`http://localhost:8888/webreport/studio/entry/run.jsp?jrd_report={"name":"/SampleReports/report.wls","ver":"-1"}&jrd_catalog={"name":"/SampleReports/SampleReports.cat","ver":"-1"}&jrd_param$={"P_Coutry":"USA"}&jrd_security_file_name={"name":"SampleReports.security.xml"}&jrd_datasources=[{"ds":"Data Source 1","uid":"xxx","pwd":"xxx","type":"0","url":"xxx","driver":"xxx"},{"ds":"Data Source 2","type":"2","key":"xxx"}]`

If you use absolute resource path, you need to add the property "real":"true" for the path. For example,

`jrd_report={"name":"C:\\Logi JReport\\Server\\Logi JReports\\SampleReports\\Products.wls","real":"true"}&jrd_catalog={"name":"C:\\Logi JReport\\Server\\Logi JReports\\SampleReports\\SampleReports.cat","real":"true"}`

Run Products.wls in the Public Reports > SampleReports folder:

`http://localhost:8888/webreport/studio/entry/run.jsp?jrd_report={"name":"/SampleReports/Products.wls"}&jrd_catalog={"name":"/SampleReports/SampleReports.cat"}`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675441-Refreshing-Page-Report-Data-Automatically)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009650502-Specifying-the-Report-Studio-Mode)
