---
title: "Banded Page Panel Properties"
id: 45190628704269
section: "References - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190628704269-Banded-Page-Panel-Properties
updated_at: 2026-04-30T15:15:38Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Banded Page Panel Properties

This topic describes the properties of a Banded Page Panel object.

Designer provides some properties only when you use the object in certain report types. You can get details from the Available For column in the property table.

| Property Name | Available For | Description |
| --- | --- | --- |
| General |  |  |
| Class Type | Query Page Report | Shows the class type of the object. Read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. Read only. |
| Paper |  |  |
| Height | Page Report, Web Report | Specifies the height of the page. Type a numeric value to change the height. Data type: Float |
| Height Auto Fit | Page Report, Web Report | Specifies whether to dynamically calculate the page height according to the height of the content within the page. Data type: Boolean |
| Orientation | Page Report, Web Report | Specifies how you want to position the report page, vertically (portrait) or horizontally (landscape). Choose an option from the drop-down list.Data type: Enumeration Designer disables this property if you select a formula to control either the Width or Height property. |
| Page Type | Page Report, Web Report | Specifies the report page dimensions. Choose a size from the drop-down list. Data type: Enumeration |
| Width | Page Report, Web Report | Specifies the width of the page. Type a numeric value to change the width. Data type: Float |
| Width Auto Fit | Page Report, Web Report | Specifies whether to dynamically calculate the page width according to the width of the content within the page. Data type: Boolean |
| Margin |  |  |
| Bottom Margin | Page Report, Web Report | Specifies the distance between the report data and the bottom edge of the page. Type a numeric value to change the margin. Data type: Float |
| Left Margin | Page Report, Web Report | Specifies the distance between the report data and the left edge of the page. Type a numeric value to change the margin. Data type: Float |
| Right Margin | Page Report, Web Report | Specifies the distance between the report data and the right edge of the page. Type a numeric value to change the margin. Data type: Float |
| Top Margin | Page Report, Web Report | Specifies the distance between the report data and the top edge of the page. Type a numeric value to change the margin. Data type: Float |

 Designer changes the values for the Height and Width properties automatically when you change Orientation or Page Type; after you select a paper type and edit either Height or Width, Designer changes the paper type to "custom size" automatically.
