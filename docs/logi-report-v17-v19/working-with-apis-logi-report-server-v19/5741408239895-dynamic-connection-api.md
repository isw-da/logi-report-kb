---
title: "Dynamic Connection API"
id: 5741408239895
section: "Working with APIs Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741408239895-Dynamic-Connection-API
updated_at: 2022-10-31T17:15:49Z
---

# Dynamic Connection API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741408431895-Using-the-NLS-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741415142807-Dynamic-Security-API)

# Dynamic Connection API

Logi Report Server manages [dynamic connections](https://devnet.logianalytics.com/hc/en-us/articles/5741395796375-Creating-and-Using-Dynamic-Connections) by **DynamicConnectionManager**. This topic describes how Logi Report Server applies dynamic connections and how you can register dynamic connections in the server via API.

You can call *jet.server.api.admin.AdminService.getDynamicConnectionManager()* to get the DynamicConnectionManager object, and call its methods *addDynamicConnection()*, *updateDynamicConnection()*, or *removeDynamicConnection()* to maintain dynamic connections for multitenancy clients by programs.

When running a report, Logi Report Server calls the DynamicConnectionProvider (the built-in provider calls DynamicConnectionManager internally) to get dynamic connections for all used data sources at first and then passes the dynamic connection properties to Logi Report Engine. Logi Report Engine then merges the changed properties with the original catalog connection properties to set up the database connection.

You can implement jet.server.api.dynamiccon.DynamicConnectionProvider to get dynamic connections from your own system and then register a customized DynamicConnectionProvider into Logi Report Server by adding the property **server.custom.DynamicConnectionProvider** in the server.properties file in `<install_root>\bin`.

For more information, see the **jet.server.api.dynamiccon** package in the Logi Report Javadoc.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741408431895-Using-the-NLS-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741415142807-Dynamic-Security-API)
