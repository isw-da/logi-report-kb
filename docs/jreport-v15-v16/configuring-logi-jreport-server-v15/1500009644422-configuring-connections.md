---
title: "Configuring Connections"
id: 1500009644422
section: "Configuring Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009644422-Configuring-Connections
updated_at: 2021-07-24T20:55:22Z
---

# Configuring Connections

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009669221-Configuring-the-Server-Service)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009669041-Configuring-Dynamic-Connections)

# Configuring Connections

Normally, after a report has been created, it is fixed to a specific catalog connection. Logi JReport allows you to change the connection by applying a dynamic connection, configuring the datasource.xml file to connect to another JDBC or JNDI data source, or by setting a runtime connection via the Server API/URL.

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

This section introduces [Configuring Dynamic Connections](https://devnet.logianalytics.com/hc/en-us/articles/1500009669041-Configuring-Dynamic-Connections) and [Configuring the datasource.xml File](https://devnet.logianalytics.com/hc/en-us/articles/1500009669061-Configuring-the-datasource-xml-File) respectively.

For details about configuring runtime connection via API or URL, refer to the following topics:

* [Changing the Runtime Database Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009644102-Changing-the-Runtime-Database-Connection)
* [Switching the Report Database Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009675461-Switching-the-Report-Database-Connection)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009669221-Configuring-the-Server-Service)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009669041-Configuring-Dynamic-Connections)
