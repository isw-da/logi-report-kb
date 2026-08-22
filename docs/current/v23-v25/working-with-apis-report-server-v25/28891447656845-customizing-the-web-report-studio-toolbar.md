---
title: "Customizing the Web Report Studio Toolbar"
id: 28891447656845
section: "Working with APIs Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891447656845-Customizing-the-Web-Report-Studio-Toolbar
updated_at: 2026-02-26T02:11:10Z
source_host: docs-report.zendesk.com
---
# 
Customizing the Web Report Studio Toolbar 

You can customize whether to show the toolbar and the buttons on the toolbar in Web Report Studio via API. The API includes WebUIConfig.java and WebUIConfigConstant.java in the com.jinfonet.web.ui.config package, and uses the two files JRStructuredClient.jar and JRStructuredEngine.jar in <install_root>\lib. This topic describes the API functions. 

- WebUIConfig config = WebUIConfig.getDefaultWebUIConfig();
                
Gets the default toolbar configuration.

- setToolbarVisible()
                
Shows/hides the toolbar for View Mode and Edit Mode.

- config.setToolbarButtonVisible()
                
Shows/hides toolbar buttons for View Mode and Edit Mode.

- WebUIConfigPreserver writer = new WebUIConfigPreserver();
writer.saveTo(config, "d:\\temp\\demo.config");
WebUIConfigLoader loader = new WebUIConfigLoader("d:\\temp\\demo.config");
                
Stores the state of writer and loader that is in user implemented API.
