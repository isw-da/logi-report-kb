---
title: "Customizing TTF Font Location for Resources"
id: 4405683930903
section: "Managing Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683930903-Customizing-TTF-Font-Location-for-Resources
updated_at: 2022-01-27T07:59:39Z
---

# Customizing TTF Font Location for Resources

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690643479-Getting-and-Using-Resources-From-a-Real-Path)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683927831-Working-with-Custom-Fields)

# Customizing TTF Font Location for Resources

This topic describes how you can change the TTF font location for server resources.

The default font path in Logi Report Server is `<install_root>\font`. You can set the font path to a different location in one of the following three ways, in an order from higher to lower priority:

* Use the property **server.font.path** in the **server.properties** file in `<install_root>\bin` to set a full path to it.
* Use the **-D** parameter to set the system property key **jreport.server.font.path**. Server does not save the value into the server.properties file.
* Use the API method *HttpUtil.initEnv()* to set the property key **server.font.path**. Server saves the value into the server.properties file.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690643479-Getting-and-Using-Resources-From-a-Real-Path)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683927831-Working-with-Custom-Fields)
