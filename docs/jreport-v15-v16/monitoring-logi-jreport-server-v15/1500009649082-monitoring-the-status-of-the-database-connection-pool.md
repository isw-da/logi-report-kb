---
title: "Monitoring the Status of the Database Connection Pool"
id: 1500009649082
section: "Monitoring Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009649082-Monitoring-the-Status-of-the-Database-Connection-Pool
updated_at: 2021-07-24T20:53:58Z
---

# Monitoring the Status of the Database Connection Pool

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009649122-Monitoring-the-Status-of-Online-Users)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009649022-Monitoring-the-Server-Performance)

# Monitoring the Status of the Database Connection Pool

To see the status of the database connection pool, expand any server node in the left panel of the Logi JReport Server Monitor home page, and then select **Databases**. You can also select and remove specific connections.

The status table of the connection pool includes:

| # | Column Heading | Value | Description |
| --- | --- | --- | --- |
| 1 | User | String | The user who is currently using the connection. |
| 2 | URL | A URL connecting to a database. | It specifies the connections that are based on a URL which will be caught in the pool. |
| 3 | Expiring Time(s) | 0 (default) or expiring time. The unit is second. If the value is zero then the connection will never expire. | Shows the time during which a connection can be alive. If a connection has expired, the connection pool will close it. |
| 4 | Idle Expiring Time(s) | 1 (default) or expiring time. The unit is second. Its value must be larger than or equals to 1. | Shows the time during which a connection is kept after it starts idling. If a connection is not used, it will stay open until the idle expiry time has been reached. |
| 5 | Maximal Connection Count | 0 (default) or a positive integer. | Shows the pool size, which limits the number of connections under a single URL |
| 6 | Maximal Share Count | 0 (default) or a positive integer. | Shows the number of users who can share a connection simultaneously. |
| 7 | Attempt | A positive integer, the default value is 1. | Shows whether to re-create a connection when the connection pool has failed to create one and the number of attempts for creating the connection. If the user sets this value to a non-positive integer, the default value (1) will be used. |
| 8 | Interval(ms) | 0 (default) or a positive integer. The unit is millisecond (ms). | If property ‘Attempt' is larger than 1, then before the connection pool retries to create a connection it will wait for an interval time. This property defines the interval time. |
| 9 | Last User Connecting Time(s) | 0 (default) or a positive integer. The unit is second. | It shows the time elapsed since the last user has taken this connection. |
| 10 | Current Idle Time(s) | 0 (default) or a positive integer.The unit is second. | Shows the time elapsed since the connection started to idle. |
| 11 | Current Share Count | 0 (default) or a positive integer. | Shows the number of users who are currently sharing this connection. |

**Note:** The properties numbered 2 to 8 can be set in the ConnectionPoolConfig.properties file in `<server_install_root>\bin` and the last three properties will be shown according to the real time status.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009649122-Monitoring-the-Status-of-Online-Users)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009649022-Monitoring-the-Server-Performance)
