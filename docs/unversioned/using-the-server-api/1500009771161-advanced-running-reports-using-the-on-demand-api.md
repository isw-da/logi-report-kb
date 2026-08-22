---
title: "Advanced Running Reports Using the On-Demand API"
id: 1500009771161
section: "Using the Server API"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009771161-Advanced-Running-Reports-Using-the-On-Demand-API
updated_at: 2021-07-24T00:49:34Z
---

# Advanced Running Reports Using the On-Demand API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009771221-Customized-Implementation-of-the-Security-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009771021-Applying-the-Implementations-of-the-Dashboard-Listener-API)

# Advanced Running Reports Using the On-Demand API

You can specify report information, result format information, and the path for the report result file, when you run a report in Advanced mode using the on-demand report execution API. This topic describes the demo codes for running a report in the PDF format and for exporting the RST file to HTML.

## Demo Code of Running a Report in the PDF Format Directly

```
//Set report properties  
Properties props = new Properties();  
  
//Set result type as .pdf format.  
props.put(APIConst.TAG_RESULT_TYPE, String.valueOf(APIConst.PDF));   
  
//Set result file location. The value of TAG_LOCATION_TO_SERVER_RESOURCE_PATH is 0,   
//and the value of TAG_LOCATION_TO_SERVER_DISK_REAL_PATH is 1.  
 
//The default value of TAG_RESULT_LOCATION_TYPE is 1.   
  
//props.put(APIConst.TAG_RESULT_LOCATION_TYPE, String.valueOf(APIConst.TAG_LOCATION_TO_SERVER_RESOURCE_PATH));   
//props.put(APIConst.TAG_RESULT_LOCATION, "/"); //props.put(APIConst.TAG_RESULT_LOCATION, "/");   
  
props.put(APIConst.TAG_RESULT_LOCATION_TYPE, String.valueOf(APIConst.TAG_LOCATION_TO_SERVER_DISK_REAL_PATH));  
props.put(APIConst.TAG_RESULT_LOCATION, "C:\\");   
System.out.println("========to pdf=" + props);  
tempResult = rptServer.runReport(user, catalog, rptName, props);
```

## Demo Code of Exporting the RST File to HTML

```
//Set task properties  
Properties props = new Properties();  
props.put(APIConst.TAG_RESULT_TYPE, String.valueOf(APIConst.RST));  
 
//Set result file location.  
props.put(APIConst.TAG_RESULT_LOCATION_TYPE, "0");   
props.put(APIConst.TAG_RESULT_LOCATION, "/");  
System.out.println("========to pdf=" + props);   
  
String tempResult = server.runReport("admin", catalog, rptName, props);  
System.out.println("========tempResult="+tempResult);   
  
//Export to HTML  
props.put(APIConst.TAG_HTML, "Crosstab");  
 
props.put(APIConst.TAG_HTML_DIR, "/");  
props.put(APIConst.TAG_HTML_DIR_TYPE, String.valueOf(APIConst.TAG_LOCATION_TO_SERVER_RESOURCE_PATH));  
 
System.out.println("\n========exportResult="+props);  
ExportedFileList fileList = server.exportResult("admin", tempResult, props);  
System.out.println("\n========fileList.getHTMLFilenameList()="+fileList.getHTMLFilenameList());
```

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009771221-Customized-Implementation-of-the-Security-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009771021-Applying-the-Implementations-of-the-Dashboard-Listener-API)
