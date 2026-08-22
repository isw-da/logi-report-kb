---
title: "Dynamic Connection API"
id: 1500009686302
section: "Using the Server API"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009686302-Dynamic-Connection-API
updated_at: 2021-11-03T06:58:34Z
---

# Dynamic Connection API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686382-Using-NLS-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009686322-Dynamic-Security-API)

# Dynamic Connection API

Logi JReport Server manages [dynamic connections](https://devnet.logianalytics.com/hc/en-us/articles/1500009712421-Creating-and-Using-Dynamic-Connections) by DynamicConnectionManager. You can call *jet.server.api.admin.AdminService.getDynamicConnectionManager()* to get the DynamicConnectionManager object, and call its methods *addDynamicConnection()*, *updateDynamicConnection()* or *removeDynamicConnection()* to maintain dynamic connections for multi-tenancy clients by programs.

When running a report, Logi JReport Server calls the DynamicConnectionProvider (the built-in provider calls DynamicConnectionManager internally) to get dynamic connections for all used data sources at first and then passes the dynamic connection properties to Logi JReport Engine. Logi JReport Engine then merges the changed properties with the original catalog connection properties to setup the database connection.

You can implement jet.server.api.dynamiccon.DynamicConnectionProvider to get dynamic connections from your own system and then register a customized DynamicConnectionProvider into Logi JReport Server by adding the property server.custom.DynamicConnectionProvider in the server.properties file in `<install_root>\bin`.

For detailed usages about the Dynamic Connection API, refer to the jet.server.api.dynamiccon package in the Logi JReport Javadoc.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686382-Using-NLS-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009686322-Dynamic-Security-API)
