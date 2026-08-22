---
title: "Configuring Connection Pool"
id: 4405690490903
section: "Configuring Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690490903-Configuring-Connection-Pool
updated_at: 2022-01-27T07:58:31Z
---

# Configuring Connection Pool

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683581207-Specifying-Connections-in-datasource-xml)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690489111-Configuring-Logi-Report-Logging-System)

# Configuring the Connection Pool

This topic describes how you can configure a connection pool using the **ConnectionPoolConfig.properties** file and view cached connections on the Server Console.

If you have used SQL statements or other similar tools to connect to a database and act on data, you probably know that getting the connection and signing in is the part that takes the most time. It takes several seconds every time a program needs to establish a connection. To improve performance, you can cache connections in the connection pool. Logi Report Server can then use a cached connection each time the same user accesses the same database table, free from having to create the connection to the database, which saves much time.

You can configure a connection pool using the **ConnectionPoolConfig.properties** file in the `<install_root>\bin` directory. The following example shows the contents in the file and describes the properties in the file:

```
# jdbcpool configure information  
URL1=jdbc:hsqldb:JRDemo1400  
Expire_URL1=0  
IdleExpire_URL1=1  
MaxCount_URL1=15  
MaxShare_URL1=1  
Attempt_URL1=100  
Interval_URL1=1000
```

* **URL1**  
   JDBC URL that can establish a connection to your database. The URL contents are case sensitive.

  You need this property to enable the connection pool. You should give a value that matches exactly with the URL used in Logi Report Designer to establish a connection to the database. The other six properties are optional. If you do not set values to them, Server uses the default values.

  "URL1" is an example of naming the URL. The name should start with the uppercase "URL". If you change the name "URL1" to "URLxY", you should also update the "URL1" in the other property names to "URLxY", for example, change "Expire\_URL1" to "Expire\_URLxY".
* **Expire\_URL1**  
   You can define how long in seconds it takes for an active connection to expire. The value for this property by default is 0, which means that the active connection will not expire.
* **IdleExpire\_URL1**  
   You can define how long a free connection can be idle before Server closes it. Server does not release the connection until the defined time is up. The value for this property by default is 1, which means that Server releases the connection after it is idle for one second. If the value is 0, Server closes the connection right after it starts idling.
* **MaxCount\_URL1**  
   The maximum number of connections based on the URL. The value for this property by default is 50. Once the number of the connections reaches the maximum, Server blocks any new connections until a free connection becomes available. The fewer the connections, the better the performance of Logi Report Server. If you set the value to 0, Server does not limit the number of the connections.
* **MaxShare\_URL1**  
   The maximum number of requests in one connection that Server can execute simultaneously. Once the number of the requests reaches the maximum, Server creates a new connection to connect to the database. The value for this property by default is 1, which means that Server can execute at most one request in one connection simultaneously. The smaller the number of requests, the better the performance of Logi Report Server. If you set the value to 0, Server does not limit the number of requests sharing one connection and executes all the requests in one connection simultaneously.

  Since the properties **MaxShare\_URL1** and **MaxCount\_URL1** are incompatible, you should make a balance between them to achieve the best performance of Logi Report Server.
* **Attempt\_URL1**  
   This property has a close relation to the property **MaxCount\_URL1**. Once the number of the connections reaches the maximum, Server blocks any new connections until a free connection becomes available. To make the most use of the available connections in the pool, you can use this property to set how many times the engine tries to establish a new connection. The default value for this property is 1, which means that the engine only tries once to create a new connection. A good value for this is 100, and the engine will try 100 times based on the interval you set to the Interval\_URL1 property.
* **Interval\_URL1**  
   The interval in milliseconds that the engine waits for between attempts to create a new connection if a previous try failed. The default value for this property is 0, which means that the engine starts the next attempt immediately. However, if you set **Attempt\_URL1** to 1, Server ignores this property is ignored because there will not be a second attempt. A good value for this is 1000 which is one second.

Administrators can view the cached connections: on the system toolbar of the Server Console, navigate to **Administration** > **Connection** > **Connection Pool**. Server displays the Connection Pool page and the cached connections in the connection table with the following information. To cancel a connection from working, it and then select **Disconnect**.

| **Column Name** | **Description** |
| --- | --- |
| Disconnect | Select to cancel the selected connection from working. |
| User | The user who triggered the connection. |
| URL | The JDBC URL that can establish a connection to your database. The URL contents are case sensitive. |
| Expiration Time | The period of time in seconds it takes for an active connection to expire. 0 means that the active connection will not expire. |
| Idle Expiration Time | The period of time for when a free connection can be idle before Server closes it. Server does not release the connection until the defined time is up. 1 means that Server releases the connection after it is idle for one second. 0 means Server closes the connection right after it starts idling. |
| Maximum Connection Count | The maximum number of connections based on the URL. Once the number of the connections reaches the maximum, Server blocks any new connections until a free connection becomes available. The fewer the connections, the better the performance of Logi Report Server. 0 means Server does not limit the number of the connections. |
| Maximum Share Count | The maximum number of requests in one connection that Server can execute simultaneously. Once the number of the requests reaches the maximum, Server creates a new connection to connect to the database. 1 means that Server executes at most one request in one connection simultaneously. 0 means that Server does not limit the number of requests sharing one connection and executes all the requests in one connection simultaneously. The smaller the number of requests, the better the performance of Logi Report Server. |
| Attempts | The number of times the engine will try to establish a new connection. 1 means that the engine only tries once to create a new connection. This property has a close relation to the property **Maximum Connection Count**. Once the number of the connections reaches the maximum, Server blocks any new connections until a free connection becomes available. |
| Interval | The interval in milliseconds the engine waits for between attempts to create a new connection if a previous try failed. 0 means that the engine starts the next attempt immediately. |
| Last User Connection Time | The time when the user connection was last established. |
| Current Idle Time | The time for when the free connection has been idle. |
| Current Share Count | The number of requests in the connections that are executing concurrently. |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683581207-Specifying-Connections-in-datasource-xml)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690489111-Configuring-Logi-Report-Logging-System)
