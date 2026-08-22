---
title: "Configuring Connections"
id: 5741395778583
section: "Configuring Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741395778583-Configuring-Connections
updated_at: 2022-10-31T17:15:59Z
---

# Configuring Connections

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741409467031-Configuring-the-Server-Service)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741395796375-Creating-and-Using-Dynamic-Connections)

# Configuring Connections

This topic describes the priority among the different ways of setting catalog connections and how they work using examples.

Normally, a report is fixed to a specific catalog connection after you create the report. You can change the connection by applying a dynamic connection, by editing the configuration file datasource.xml to connect to another JDBC or JNDI data source, or by setting a runtime connection via the Server API/URL.

The connection priority is:

Runtime configuration of connection > dynamic connection > datasource.xml > catalog connection

If the approach with higher priority fails to get the connection, the one with the next lower priority will be used.

Assuming that a catalog has two databases named as **data source 1** and **data source 2**. See the following examples:

* You set the connection by API without specifying a data source name. Both
  data source 1 and data source 2 will use the new setting.
* You set a new connection A by specifying the data source name "data source 2". The result is:
  data source 1 has no change and data source 2 will use the connection A.
* You set two connections by API, a new connection A by specifying the data source name "data source 2" and a new connection B without specifying a data source name. The result is: data source 1 will use the connection B and data source 2 the connection A.
* You set "data source 2" connection in datasource.xml and a new connection A by API by specifying the data source name "data source 2". The result is: data source 1 has no change and data source 2 will use connection A ignoring the setting in datasource.xml.
* You set "data source 2" connection B in datasource.xml and a new connection A by API without specifying the data source name. The result is: data source 1 will use the connection A and data source 2 the connection B.
* You set "data source 2" connection in datasource.xml and a dynamic connection for data source 2. The result is: data source 1 has no change and data source 2 will use the dynamic connection.

Select the following links to view the topics:

* [Creating and Using Dynamic Connections](https://devnet.logianalytics.com/hc/en-us/articles/5741395796375-Creating-and-Using-Dynamic-Connections)
* [Specifying Connections in datasource.xml](https://devnet.logianalytics.com/hc/en-us/articles/5741415923607-Specifying-Connections-in-datasource-xml)

For more information about configuring runtime connection via API or URL, see [Changing the Runtime Database Connection](https://devnet.logianalytics.com/hc/en-us/articles/5741400603543-Changing-the-Runtime-Database-Connection) and [Switching the Report Database Connection via URL](https://devnet.logianalytics.com/hc/en-us/articles/5741456438167-Running-Reports-via-URL#Connection).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741409467031-Configuring-the-Server-Service)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741395796375-Creating-and-Using-Dynamic-Connections)
