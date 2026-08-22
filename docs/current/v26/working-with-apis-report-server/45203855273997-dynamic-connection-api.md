---
title: "Dynamic Connection API"
id: 45203855273997
section: "Working with APIs Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203855273997-Dynamic-Connection-API
updated_at: 2026-04-30T14:07:47Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Dynamic Connection API 

Report Server manages dynamic connections by DynamicConnectionManager. This topic describes how Report Server applies dynamic connections and how you can register dynamic connections in the server via API.

You can call jet.server.api.admin.AdminService.getDynamicConnectionManager() to get the DynamicConnectionManager object, and call its methods addDynamicConnection(), updateDynamicConnection(), or removeDynamicConnection() to maintain dynamic connections for multitenancy clients by programs. 

When running a report, Report Server calls the DynamicConnectionProvider (the built-in provider calls DynamicConnectionManager internally) to get dynamic connections for all used data sources at first and then passes the dynamic connection properties to Report Engine. Report Engine then merges the changed properties with the original catalog connection properties to set up the database connection.

You can implement jet.server.api.dynamiccon.DynamicConnectionProvider to get dynamic connections from your own system and then register a customized DynamicConnectionProvider into Report Server by adding the property server.custom.DynamicConnectionProvider in the server.properties file in <install_root>\bin.

For more information, see the jet.server.api.dynamiccon package in the Report Javadoc.
