---
title: "Changing the Runtime Database Connection"
id: 5741400603543
section: "Working with APIs Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741400603543-Changing-the-Runtime-Database-Connection
updated_at: 2022-10-31T17:15:52Z
---

# Changing the Runtime Database Connection

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741386771735-Working-with-Resource-Versions)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741386712599-Scheduling-a-Report-Task)

# Changing the Runtime Database Connection

Normally a report is fixed to a specific catalog connection after being created. You can set new connection information at runtime via the Server API. This topic describes how you can configure the runtime connection.

The runtime configuration of connection includes the connection object and connection info (such as URL, driver, and user/password), and the connection object has higher priority than the connection info.

There are two ways of changing the connection by API at runtime, one is set the connection info by specifying the data source name, which will only change the connection of the indicated data source; the other is set the connection info without a specific data source name, which is regarded as a default change and will change the connections that have not been changed by the previous way.

The following is an API example of setting database connection information:

```
props.put(APIConst.TAG_JDBC_URL, "jdbc:mysql://192.0.0.1:3306");  
props.put(APIConst.TAG_JDBC_DRIVER, "com.mysql.jdbc.Driver");  
props.put(APIConst.TAG_DB_USER, "admin");  
props.put(APIConst.TAG_DB_PSWD, "admin");
```

An API sample of running a report is **APIDemoRunReport.java** in  `<install_root>\help\samples\APIServer`. You can add the preceding codes in it to change the connection when running the report.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741386771735-Working-with-Resource-Versions)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741386712599-Scheduling-a-Report-Task)
