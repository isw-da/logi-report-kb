---
title: "Customizing the Web Report Studio Toolbar"
id: 45203871291533
section: "Working with APIs Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203871291533-Customizing-the-Web-Report-Studio-Toolbar
updated_at: 2026-04-30T14:07:52Z
source_host: logi-report-v26.insightsoftware.com
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
