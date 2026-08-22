---
title: "Customizing the Web Report Studio Toolbar"
id: 4405683567895
section: "Working with APIs Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683567895-Customizing-the-Web-Report-Studio-Toolbar
updated_at: 2022-01-27T08:00:01Z
---

# Customizing the Web Report Studio Toolbar

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683549335-Configuring-the-Security-Cache-System)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690478871-Customized-Implementation-of-the-Security-API)

# Customizing the Web Report Studio Toolbar

You can customize whether to show the toolbar and the buttons on the toolbar in Web Report Studio via API. The API includes WebUIConfig.java and WebUIConfigConstant.java in the com.jinfonet.web.ui.config package, and uses the two files JRStructuredClient.jar and JRStructuredEngine.jar in `<install_root>\lib`. This topic describes the API functions.

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683549335-Configuring-the-Security-Cache-System)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690478871-Customized-Implementation-of-the-Security-API)
