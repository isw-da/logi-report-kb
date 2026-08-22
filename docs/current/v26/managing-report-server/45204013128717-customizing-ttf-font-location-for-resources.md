---
title: "Customizing TTF Font Location for Resources"
id: 45204013128717
section: "Managing Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45204013128717-Customizing-TTF-Font-Location-for-Resources
updated_at: 2026-04-30T14:10:30Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Customizing TTF Font Location for Resources 

This topic describes how you can change the TTF font location for server resources.

The default font path in Report Server is <install_root>\font. You can set the font path to a different location in one of the following three ways, in an order from higher to lower priority:

- Use the property server.font.path in the server.properties file in <install_root>\bin to set a full path to it.

- Use the -D parameter to set the system property key jreport.server.font.path. Server does not save the value into the server.properties file.

- Use the API method HttpUtil.initEnv() to set the property key server.font.path. Server saves the value into the server.properties file.
