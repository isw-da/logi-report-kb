---
title: "Customizing the Web Report Studio Toolbar"
id: 1500009686422
section: "Using the Server API"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009686422-Customizing-the-Web-Report-Studio-Toolbar
updated_at: 2021-11-03T06:58:31Z
---

# Customizing the Web Report Studio Toolbar

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009711981-Configuring-the-Security-Cache-System)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009712201-Customized-Implementation-of-the-Security-API)

# Customizing the Web Report Studio Toolbar

You can customize whether to show the toolbar and the buttons on the toolbar in Web Report Studio via API. The API includes WebUIConfig.java and WebUIConfigConstant.java in the com.jinfonet.web.ui.config package, and uses the two files JRStructuredClient.jar or JRStructuredEngine.jar in `<install_root>\lib`.

The following lists the API functions:

* WebUIConfig config = WebUIConfig.getDefaultWebUIConfig();
    
  Gets the default toolbar configuration.
* setToolbarVisible()
    
  Shows/hides the toolbar for View Mode and Edit Mode.
* config.setToolbarButtonVisible()
    
  Shows/hides toolbar buttons for View Mode and Edit Mode.
* WebUIConfigPreserver writer = new WebUIConfigPreserver();  
  writer.saveTo(config, "d:\\temp\\demo.config");  
  WebUIConfigLoader loader = new WebUIConfigLoader("d:\\temp\\demo.config");
    
  Stores the state of writer and loader that is in user implemented API.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009711981-Configuring-the-Security-Cache-System)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009712201-Customized-Implementation-of-the-Security-API)
