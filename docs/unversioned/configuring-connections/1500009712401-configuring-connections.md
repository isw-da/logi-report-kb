---
title: "Configuring Connections"
id: 1500009712401
section: "Configuring Connections"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009712401-Configuring-Connections
updated_at: 2021-11-03T06:58:28Z
---

# Configuring Connections

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686842-Configuring-the-Server-Service)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009712421-Creating-and-Using-Dynamic-Connections)

# Configuring Connections

Normally, after a report has been created, it is fixed to a specific catalog connection. Logi JReport allows you to change the connection by applying a dynamic connection, editing the configuration file datasource.xml to connect to another JDBC or JNDI data source, or by setting a runtime connection via the Server API/URL.

The connection priority is as follows:

Runtime configuration of connection > dynamic connection > datasource.xml > catalog connection

This means that if the approach with higher priority fails to get the connection, the one with the next lower priority will be used.

Assuming that the catalog has two databases named as data source 1 and data source 2, here are some examples:

* A user does not set datasource.xml, but sets the connection by API without specifying a data source name. Both
  data source 1 and data source 2 will use the new setting.
* A user does not set datasource.xml, but sets a new connection A by specifying the data source name "data source 2". The result is:
  data source 1 has no change and data source 2 will use the connection A.
* A user does not set datasource.xml, but sets two connections by API, a new connection A by specifying the data source name "data source 2" and a new connection B without specifying a data source name. The result is: data source 1 will use the connection B and data source 2 the connection A.
* A user sets "data source 2" connection in  datasource.xml and a new connection A by API by specifying the data source name "data source 2". The result is: data source 1 has no change and data source 2 will use connection A ignoring the setting in datasource.xml.
* A user sets "data source 2" connection B in datasource.xml and a new connection A by API without specifying the data source name. The result is: data source 1 will use the connection A and data source 2 the connection B.
* A user sets "data source 2" connection in datasource.xml and a dynamic connection for data source 2. The result is: data source 1 has no change and data source 2 will use the dynamic connection.

The following topics provide more information on connections:

* [Creating and Using Dynamic Connections](https://devnet.logianalytics.com/hc/en-us/articles/1500009712421-Creating-and-Using-Dynamic-Connections)
* [Specifying Connections in datasource.xml](https://devnet.logianalytics.com/hc/en-us/articles/1500009712441-Specifying-Connections-in-datasource-xml)

For details about configuring runtime connection via API or URL, refer to [Changing the Runtime Database Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009712161-Changing-the-Runtime-Database-Connection) and [Switching the Report Database Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009693002-Running-Reports#Connection).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686842-Configuring-the-Server-Service)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009712421-Creating-and-Using-Dynamic-Connections)
