---
title: "Customizing TTF Font Location for Resources"
id: 1500009723102
section: "Manage Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009723102-Customizing-TTF-Font-Location-for-Resources
updated_at: 2021-07-25T07:18:58Z
---

# Customizing TTF Font Location for Resources

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750141-Getting-and-Using-Resources-from-a-Real-Path)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009723042-Working-with-Custom-Fields)

# Customizing TTF Font Location for Resources

The default font path in Logi Report Server is `<install_root>\font`. You can set the font path to a different location in one of the following three ways. These are in an order from higher to lower priority:

* Use the property server.font.path in the server.properties file saved in `<install_root>\bin` to set a full path to it.
* Use the "-D" parameter to set the system property key jreport.server.font.path.
* Use the API method *HttpUtil.initEnv()* to set the property key server.font.path.

**Note:** The value specified by the "-D" parameter is not stored into the server.properties file, while the value specified using API is stored into the file.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750141-Getting-and-Using-Resources-from-a-Real-Path)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009723042-Working-with-Custom-Fields)
