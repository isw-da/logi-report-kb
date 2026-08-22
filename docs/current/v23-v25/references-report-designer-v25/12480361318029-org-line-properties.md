---
title: "Org Line Properties"
id: 12480361318029
section: "References - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480361318029-Org-Line-Properties
updated_at: 2026-02-25T23:48:01Z
source_host: docs-report.zendesk.com
---
# 
Org Line Properties

This topic describes the properties of the Line object in an organization chart.

Designer provides some properties only when you use the object in certain report types. You can get details from the Available For column in the property table.

| Property Name | Available For | Description |
| --- | --- | --- |
| General |  |  |
| Class Type | Query Page Report | Shows the class type of the object. Read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. Read only. |
| CSS |  |  |
| Class | Page Report | Specifies the name of the Class Selector to apply to the object, which you define in the CSS file of the style the report applies. For example, if you define the CSS file as follows: @charset "GBK"; TextField {Background: #ff0000} /*Style=LabelX*/ TextField[Style="LabelX"]{Background: #0000FF} /*ID=W*/ TextField#W{Background: #FFFF00} /*class=C*/ TextField.C{Background: #00FFFF} To apply the Class Selector in the file to the object, type C in the value cell. Data type: String |
| Style | Page Report | Specifies the style you want to apply to the object. You can specify the style in two ways: Type the style which should be an Attribute Selector whose attribute is "style" in the CSS file of the style the report applies. For example, to apply the style in the preceding sample CSS file to the object, type LabelX in the value cell. Choose a style from the drop-down list when you have specified the Style Group property for the page report tab and there are styles in the style group that are applicable to the object. Data type: String |
| Line Property |  |  |
| Line Color | Page Report, Web Report, Library Component | Specifies the color of the line. Choose a color from the drop-down list, or select Custom to customize a color in the Pick a Color dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Line Style | Page Report, Web Report, Library Component | Specifies the style of the line. Choose an option from the drop-down list. Data type: Enumeration |
| Line Thickness | Page Report, Web Report, Library Component | Specifies the width of the line. Type a numeric value to change the thickness. Data type: Float |
