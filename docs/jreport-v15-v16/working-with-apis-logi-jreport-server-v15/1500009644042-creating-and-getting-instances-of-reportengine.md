---
title: "Creating and Getting Instances of ReportEngine"
id: 1500009644042
section: "Working With APIs Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009644042-Creating-and-Getting-Instances-of-ReportEngine
updated_at: 2021-07-24T20:55:29Z
---

# Creating and Getting Instances of ReportEngine

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009643782-Using-the-Server-API)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009668801-Creating-and-Getting-Instances-of-RptServer-or-HttpRptServer)

# Creating and Getting Instances of ReportEngine

To get an instance of the ReportEngine, you can use the method getInstance() or getInstance(boolean setDebugLevel) in the jet.server.api.engine.ReportEngineFactory.

For example,

`bean = ReportEngineFactory.getInstance();`

or,

`bean = ReportEngineFactory.getInstance(true);`

**Reference:** See Logi JReport Javadoc in  `<install_root>\help\api` for usage of the ReportEngine methods.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009643782-Using-the-Server-API)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009668801-Creating-and-Getting-Instances-of-RptServer-or-HttpRptServer)
