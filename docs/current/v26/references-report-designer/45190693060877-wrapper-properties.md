---
title: "Wrapper Properties"
id: 45190693060877
section: "References - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190693060877-Wrapper-Properties
updated_at: 2026-04-30T15:15:55Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Wrapper Properties

This topic describes the properties of the Wrapper object in a library component.

| Property Name | Description |
| --- | --- |
| General |  |
| Author | Specifies the author of the library component. Data type: String |
| Author Email | Specifies the author's email address. Data type: String |
| Description | Specifies the description of the library component. Data type: String |
| Title | Specifies the title of the library component. Data type: String |
| Refresh |  |
| Enable Auto Refresh | Specifies whether to automatically refresh the objects in the library component that are not bound with data at runtime based on a defined interval. Data type: Boolean |
| Interval | Designer enables this property when you set Enable Auto Refresh to "true". You can use it to specify the time interval between two auto refreshes, which can range from 0 to 86400 seconds. Type a numeric value to change the interval. Data type: Integer |
| CSS |  |
| Class | Shows the CSS class the title bar of the library component applies. Read only. The style of the title bar is controlled by JDashboard theme, which you can edit in the corresponding CSS file only. |
