---
title: "Dynamic Connection API"
id: 1500009744321
section: "Work With APIs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009744321-Dynamic-Connection-API
updated_at: 2021-07-25T07:20:23Z
---

# Dynamic Connection API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744401-Using-NLS-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744341-Dynamic-Security-API)

# Dynamic Connection API

Logi Report Server manages [dynamic connections](https://devnet.logianalytics.com/hc/en-us/articles/1500009718782-Creating-and-Using-Dynamic-Connections) by DynamicConnectionManager. You can call *jet.server.api.admin.AdminService.getDynamicConnectionManager()* to get the DynamicConnectionManager object, and call its methods *addDynamicConnection()*, *updateDynamicConnection()* or *removeDynamicConnection()* to maintain dynamic connections for multitenancy clients by programs.

When running a report, Logi Report Server calls the DynamicConnectionProvider (the built-in provider calls DynamicConnectionManager internally) to get dynamic connections for all used data sources at first and then passes the dynamic connection properties to Logi Report Engine. Logi Report Engine then merges the changed properties with the original catalog connection properties to setup the database connection.

You can implement jet.server.api.dynamiccon.DynamicConnectionProvider to get dynamic connections from your own system and then register a customized DynamicConnectionProvider into Logi Report Server by adding the property server.custom.DynamicConnectionProvider in the server.properties file in `<install_root>\bin`.

For detailed usages about the Dynamic Connection API, refer to the jet.server.api.dynamiccon package in the Logi Report Javadoc.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744401-Using-NLS-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744341-Dynamic-Security-API)
