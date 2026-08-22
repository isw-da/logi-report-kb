---
title: "Customizing TTF Font Location for Resources"
id: 28891673910029
section: "Managing Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891673910029-Customizing-TTF-Font-Location-for-Resources
updated_at: 2026-02-26T02:13:30Z
source_host: docs-report.zendesk.com
---
# 
Customizing TTF Font Location for Resources 

This topic describes how you can change the TTF font location for server resources.

The default font path in Report Server is <install_root>\font. You can set the font path to a different location in one of the following three ways, in an order from higher to lower priority:

- Use the property server.font.path in the server.properties file in <install_root>\bin to set a full path to it.

- Use the -D parameter to set the system property key jreport.server.font.path. Server does not save the value into the server.properties file.

- Use the API method HttpUtil.initEnv() to set the property key server.font.path. Server saves the value into the server.properties file.
