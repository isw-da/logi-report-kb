---
title: "Changing the Runtime Database Connection"
id: 1500009712161
section: "Using the Server API"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009712161-Changing-the-Runtime-Database-Connection
updated_at: 2021-11-03T06:58:33Z
---

# Changing the Runtime Database Connection

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686442-Working-with-Resource-Versions)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009686402-Scheduling-a-Report-Task)

# Changing the Runtime Database Connection

Normally, after a report has been created, it is fixed to a specific catalog connection. Logi JReport allows you to set new connection information at runtime via the Server API.

The runtime configuration of connection includes the connection object and connection info (such as url, driver, and user/password), and the connection object has higher priority than the connection info.

There are two ways of changing the connection by API at runtime, one is set the connection info by specifying the data source name, which will only change the connection of the indicated data source; the other is set the connection info without a specific data source name, which is regarded as a default change and will change the connections that have not been changed by the previous way.

The following is an API example of setting database connection information:

```
props.put(APIConst.TAG_JDBC_URL, "jdbc:mysql://192.0.0.1:3306");  

props.put(APIConst.TAG_JDBC_DRIVER, "com.mysql.jdbc.Driver");  

props.put(APIConst.TAG_DB_USER, "jreport");  

props.put(APIConst.TAG_DB_PSWD, "jreport");
```

There is an API sample of running a report which is APIDemoRunReport.java in  `<install_root>\help\samples\APIServer`, and you can add the above codes in it so as to change the connection when running the report.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686442-Working-with-Resource-Versions)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009686402-Scheduling-a-Report-Task)
