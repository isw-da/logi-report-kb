---
title: "Customizing TTF Font Location for Resources"
id: 1500009648842
section: "Managing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009648842-Customizing-TTF-Font-Location-for-Resources
updated_at: 2021-07-24T20:54:03Z
---

# Customizing TTF Font Location for Resources

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648902-Getting-and-Using-Resources-from-a-Real-Path)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648802-Working-with-Custom-Fields)

# Customizing TTF Font Location for Resources

The default font path in Logi JReport Server is `<install_root>\font`. You can set the font path to a different location by using the following three ways. These are in an order from higher to lower priority:

* Use the property server.font.path in the server.properties file saved in `<install_root>\bin` to set a full path to it.
* Use the *-D* parameter to set the system property key Logi JReport.server.font.path.
* Use the API HttpUtil.initEnv() to set the property key server.font.path.

**Note:** The value specified by the *-D* parameter is not stored into the server.properties file, while the value specified using API is stored into the file.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648902-Getting-and-Using-Resources-from-a-Real-Path)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648802-Working-with-Custom-Fields)
