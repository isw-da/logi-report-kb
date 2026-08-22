---
title: "Configuring Connection Pool"
id: 1500009644562
section: "Configuring Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009644562-Configuring-Connection-Pool
updated_at: 2021-07-24T20:55:18Z
---

# Configuring Connection Pool

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009669061-Configuring-the-datasource-xml-File)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644542-Configuring-Logs)

# Configuring Connection Pool

If you have used SQL or other similar tools to connect to a database and act on data, you probably know that getting the connection and logging in is the part that takes the most time. A program can spend several seconds every time it needs to establish a connection. To improve performance, Logi JReport Server supports caching a connection, so that it can be used each time the same user accesses the same table. Cached connections are kept in the connection pool and can be used and re-used as required. Therefore Logi JReport Server is freed from having to create the connection to the database, leading to a considerable saving of time.

If you want to improve the performance of Logi JReport Server, you can configure a connection pool using the ConnectionPoolConfig.properties file in the directory `<install_root>\bin`. The following is an example of the ConnectionPoolConfig.properties file and detailed description of each property in the file:

|  |
| --- |
| ``` # jdbcpool configure information URL1=jdbc:hsqldb:JRDemo1400 Expire_URL1=0 IdleExpire_URL1=1 MaxCount_URL1=15 MaxShare_URL1=1 Attempt_URL1=100 Interval_URL1=1000 ``` |

* **URL1**  
   JDBC URL that can establish a connection to your database. The URL contents are case sensitive.

  This property is required to enable using the connection pool. You should give a value that matches exactly to the URL used in Designer to establish a connection to the database. The other six properties are optional. If no values are set to them, the default values will be used.

  "URL1" is an example of naming the URL. The name should start with the uppercase "URL". If you change the name "URL1" to "URLxY", the "URL1" in the other property names should also be updated to "URLxY", for example, "Expire\_URL1" should be changed to "Expire\_URLxY".
* **Expire\_URL1**  
   You can define how long in seconds it takes for an active connection to expire. The value for this property by default is "0", which means that the active connection will not expire.
* **IdleExpire\_URL1**  
   You can define how long a free connection can be idle before it is closed. The connection will not be released until the defined time has reached its limit. The value for this property by default is "1", which means that the connection will be released after 1 second. If the value is "0", the connection will be closed right after it starts idling.
* **MaxCount\_URL1**  
   The maximum number of connections based on the URL. The value for this property by default is "50". Once the number of the connections reaches the maximum, a new connection will be blocked until a free connection becomes available. Generally speaking, the fewer the connections, the better the performance of Logi JReport Server. If the value is set to "0", it means that there will be no limit on the number of the connections.
* **MaxShare\_URL1**  
   The maximum number of requests in one connection that can be executed simultaneously. Once the number of the requests reaches the maximum, a new connection will be created to connect to the database. The value for this property by default is "1", which means that one request in one connection can be executed simultaneously. The smaller the number of requests, the better the performance of Logi JReport Server. If the value is set to "0", it means that there will be no limit to the maximum number of requests sharing one connection and that all the requests in one connection can be executed simultaneously.

  Since the property MaxShare\_URL1 and MaxCount\_URL1 are incompatible, you should make a balance between these two properties to achieve the best performance of Logi JReport Server.
* **Attempt\_URL1**  
   This property has a close relation to the property MaxCount\_URL1. Once the number of the connections reaches the maximum, a new connection will be blocked until a free connection becomes available. To make the maximum use of the available connections in the pool, the property Attempt\_URL1 allows you to set how many times the engine will try to establish a new connection. The default value for this property is "1", which means that the engine will only try once to create a new connection. A good value for this is 100 which means it will try 100 times based on the interval set below.
* **Interval\_URL1**  
   The interval the engine will wait for between attempts to create a new connection if a previous try has failed. The default value for this property is "0", which means that the engine will start the next attempt immediately. The unit of the property value is milliseconds. However, if the Attempt\_URL1 is set to 1 then this property is ignored as there will not be a second attempt. A good value for this is 1000 which is one second.

Administrators can log onto the Logi JReport Administration page to view the cached connections.

1. On the Logi JReport Administration page, select **Configuration** on the system toolbar and select **Connection Pool** from the drop-down menu.
2. The Configuration - Connection Pool page appears. All the cached connections are displayed in the connection table with the following information.  

   |  |  |
   | --- | --- |
   | **Column Name** | **Description** |
   | Disconnect | Cancels the selected connection from working. |
   | User | The user who triggered the connection. |
   | URL - URL1 | JDBC URL that can establish a connection to your database. The URL contents are case sensitive. |
   | Expiration Time | The period of time in seconds it takes for an active connection to expire. "0" means that the active connection will not expire. |
   | Idle Expiration Time | The period of time for when a free connection can be idle before it is closed. The connection will not be released until the defined time has reached its limit. "1" means that the connection will be released after 1 second. "0" means the connection will be closed right after it starts idling. |
   | Maximum Connection Count | The maximum number of connections based on the URL. Once the number of the connections reaches the maximum, a new connection will be blocked until a free connection becomes available. Generally speaking, the fewer the connections, the better the performance of Logi JReport Server. "0" means that there will be no limit on the number of the connections. |
   | Maximum Share Count | The maximum number of requests in one connection that can be executed simultaneously. Once the number of the requests reaches the maximum, a new connection will be created to connect to the database. "1" means that one request in one connection can be executed simultaneously. "0" means that there will be no limit to the maximum number of requests sharing one connection and that all the requests in one connection can be executed simultaneously. The smaller the number of requests, the better the performance of Logi JReport Server. |
   | Attempts | The number of times the engine will try to establish a new connection. "1" means that the engine will only try once to create a new connection. This property has a close relation to the property Maximum Connection Count. Once the number of the connections reaches the maximum, a new connection will be blocked until a free connection becomes available. |
   | Interval | The interval the engine will wait for between attempts to create a new connection if a previous try has failed. "0" means that the engine will start the next attempt immediately. The unit of the property value is milliseconds. |
   | Last User Connection Time | The time when the user connection was last established. |
   | Current Idle Time | The time for when the free connection has been idle. |
   | Current Share Count | The number of requests in the connections that are being executed concurrently. |
3. To cancel a connection from working, check the checkbox ahead of the connection in the table and select **Disconnect**.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009669061-Configuring-the-datasource-xml-File)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644542-Configuring-Logs)
