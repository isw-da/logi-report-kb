---
title: "Configuration Properties"
id: 45190660405005
section: "References - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190660405005-Configuration-Properties
updated_at: 2026-04-30T15:15:42Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Configuration Properties

This topic describes the properties of the Configuration object (that is, the Configuration Panel) in a library component.

| Property Name | Description |
| --- | --- |
| General |  |
| Class Type | Shows the class type of the object. Read only. |
| Data Inherit | Shows whether the object inherits dataset from another object. Read only. |
| Dataset | Shows the dataset the object applies. Read only. |
| Instance Name | Shows the instance name of the object. Read only. |
| Geometry |  |
| Height | Specifies the height of the object. Type a numeric value to change the height. Data type: Float |
| CSS |  |
| Class | Specifies the name of the Class Selector to apply to the object, which you define in the CSS file of the style the report applies. For example, if you define the CSS file as follows: @charset "GBK"; TextField {Background: #ff0000} /*Style=LabelX*/ TextField[Style="LabelX"]{Background: #0000FF} /*ID=W*/ TextField#W{Background: #FFFF00} /*class=C*/ TextField.C{Background: #00FFFF} To apply the Class Selector in the file to the object, type C in the value cell. Data type: String |
| Others |  |
| Default Show | Specifies whether to show the configuration panel by default when users insert the library component into a dashboard in JDashboard. Data type: Boolean |
