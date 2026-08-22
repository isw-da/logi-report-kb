---
title: "Customizing the Web Report Studio Toolbar"
id: 1500009644162
section: "Working With APIs Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009644162-Customizing-the-Web-Report-Studio-Toolbar
updated_at: 2021-07-24T20:55:26Z
---

# Customizing the Web Report Studio Toolbar

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009643802-Configuring-the-Security-Cache-System)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009668781-Customized-Implementation-of-the-Security-API)

# Customizing the Web Report Studio Toolbar

Using API, you can customize whether to show the toolbar and the buttons on the toolbar in Web Report Studio. The API includes WebUIConfig.java and WebUIConfigConstant.java in the com.jinfonet.web.ui.config package, and uses the two files JRStructuredClient.jar or JRStructuredEngine.jar in `<install_root>\lib`. For details, see Logi JReport Javadoc in `<install_root>\help\api`.

The following lists the API functions:

* **WebUIConfig config = WebUIConfig.getDefaultWebUIConfig();**  
   Gets the default toolbar configuration.
* **setToolbarVisible()**  
   Shows/hides the toolbar for View Mode and Edit Mode.
* **config.setToolbarButtonVisible()**  
   Shows/hides toolbar buttons for View Mode and Edit Mode.
* **WebUIConfigPreserver writer = new WebUIConfigPreserver();  
   writer.saveTo(config, "d:\\temp\\demo.config");  
   WebUIConfigLoader loader = new WebUIConfigLoader("d:\\temp\\demo.config");**  
   Stores the state of writer and loader that is in user implemented API.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009643802-Configuring-the-Security-Cache-System)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009668781-Customized-Implementation-of-the-Security-API)
