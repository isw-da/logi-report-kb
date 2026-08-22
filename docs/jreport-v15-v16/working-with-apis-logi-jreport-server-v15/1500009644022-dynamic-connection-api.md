---
title: "Dynamic Connection API"
id: 1500009644022
section: "Working With APIs Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009644022-Dynamic-Connection-API
updated_at: 2021-07-24T20:55:30Z
---

# Dynamic Connection API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644082-Using-NLS-API)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009668621-Dynamic-Security-API)

# Dynamic Connection API

Logi JReport Server manages [dynamic connections](https://devnet.logianalytics.com/hc/en-us/articles/1500009669041-Configuring-Dynamic-Connections) by the DynamicConnectionManager. Users can call jet.server.api.admin.AdminService.getDynamicConnectionManager() to get the DynamicConnectionManager object, and call its methods addDynamicConnection(...), updateDynamicConnection(...) or removeDynamicConnection(...) to maintain dynamic connections for multiple tenancy clients by programs.

When running a report, the server calls the DynamicConnectionProvider (the built-in provider calls DynamicConnectionManager internally) to get dynamic connections for all used data sources at first and then passes the dynamic connection properties into the engine. The engine will merge the changed properties with the original catalog connection properties to setup the database connection.

Users can implement jet.server.api.dynamiccon.DynamicConnectionProvider to get dynamic connections from their own systems and then register a customized DynamicConnectionProvider into Logi JReport Server by adding the property server.custom.DynamicConnectionProvider in the server.properties file in `<install_root>\bin`.

For detailed usages about the Dynamic Connection API, see Logi JReport Javadoc jet.server.api.dynamiccon package in `<install_root>\help\api`.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644082-Using-NLS-API)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009668621-Dynamic-Security-API)
