---
title: "Changing the Runtime Database Connection"
id: 1500009644102
section: "Working With APIs Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009644102-Changing-the-Runtime-Database-Connection
updated_at: 2021-07-24T20:55:27Z
---

# Changing the Runtime Database Connection

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009668841-Working-With-Resource-Versions)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644142-Scheduling-a-Report-Task)

# Changing the Runtime Database Connection

Normally, after a report has been created, it is fixed to a specific catalog connection. Logi JReport allows you to set new connection information at runtime via the Server API.

The runtime configuration of connection includes the connection object and connection info (such as url, driver, and user/password), and the connection object has higher priority than the connection info.

There are two ways of changing the connection by API at runtime, one is set the connection info by specifying the data source name, which will only change the connection of the indicated data source; the other is set the connection info without a specific data source name, which is regarded as a default change and will change the connections that have not been changed by the previous way.

The following is an API example of setting database connection information:

|  |
| --- |
| ``` props.put(APIConst.TAG_JDBC_URL, "jdbc:mysql://192.0.0.1:3306"); props.put(APIConst.TAG_JDBC_DRIVER, "com.mysql.jdbc.Driver"); props.put(APIConst.TAG_DB_USER, "Logi JReport"); props.put(APIConst.TAG_DB_PSWD, "Logi JReport"); ``` |

There is an API sample of running a report which is APIDemoRunReport.java in  `<install_root>\help\samples\APIServer`, and you can add the above codes in it so as to change the connection when running the report.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009668841-Working-With-Resource-Versions)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644142-Scheduling-a-Report-Task)
