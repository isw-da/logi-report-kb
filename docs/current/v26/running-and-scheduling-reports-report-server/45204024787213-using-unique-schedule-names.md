---
title: "Using Unique Schedule Names"
id: 45204024787213
section: "Running and Scheduling Reports Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45204024787213-Using-Unique-Schedule-Names
updated_at: 2026-04-30T14:10:47Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Using Unique Schedule Names

This topic describes how you can manage unique scheduling names on Server. Administrators can toggle unique scheduling names on or off, by setting the Unique Schedule Names option on the Server Console > Administration > Configuration > Advanced tab. The default value is set to false.

When unique scheduling names are enabled, Server ensures that each schedule name is distinct. In case a newly created schedule name conflicts with any existing schedules, an error message will be promptly displayed to alert the user.

This configuration can also be accessed and modified in the server.properties file, using the property name "server.enable.unique_schedule_names". Adjusting this property in the server.properties file provides an alternative method for administrators to control the unique scheduling names feature.
