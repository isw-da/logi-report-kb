---
title: "Banded Page Panel Properties"
id: 5735554261399
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735554261399-Banded-Page-Panel-Properties
updated_at: 2022-11-02T08:15:49Z
---

# Banded Page Panel Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/9898540313495-Banded-Group-Footer-Panel-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/9898557749271-Banded-Page-Header-Properties)

# Banded Page Panel Properties

This topic describes the properties of a Banded Page Panel object.

Designer provides some properties only when you use the object in certain [report types](https://devnet.logianalytics.com/hc/en-us/articles/5735584998167-Report-Object-Properties#ReportType). You can get details from the Available For column in the property table.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Shows the class type of the object. Read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. Read only. |
| Paper | | |
| Height | Page Report, Web Report | Specifies the height of the page. Type a numeric value to change the height. Data type: Float |
| Height Auto Fit | Page Report, Web Report | Specifies whether to dynamically calculate the page height according to the height of the content within the page. Data type: Boolean |
| Orientation | Page Report, Web Report | Specifies how you want to position the report page, vertically (portrait) or horizontally (landscape). Choose an option from the drop-down list. Data type: Enumeration  Note icon Designer disables this property if you select a formula to control either the Width or Height property. |
| Page Type | Page Report, Web Report | Specifies the report page dimensions. Choose a size from the drop-down list. Data type: Enumeration |
| Width | Page Report, Web Report | Specifies the width of the page. Type a numeric value to change the width. Data type: Float |
| Width Auto Fit | Page Report, Web Report | Specifies whether to dynamically calculate the page width according to the width of the content within the page. Data type: Boolean |
| Margin | | |
| Bottom Margin | Page Report, Web Report | Specifies the distance between the report data and the bottom edge of the page. Type a numeric value to change the margin. Data type: Float |
| Left Margin | Page Report, Web Report | Specifies the distance between the report data and the left edge of the page. Type a numeric value to change the margin. Data type: Float |
| Right Margin | Page Report, Web Report | Specifies the distance between the report data and the right edge of the page. Type a numeric value to change the margin. Data type: Float |
| Top Margin | Page Report, Web Report | Specifies the distance between the report data and the top edge of the page. Type a numeric value to change the margin. Data type: Float |

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) Designer changes the values for the Height and Width properties automatically when you change Orientation or Page Type; after you select a paper type and edit either Height or Width, Designer changes the paper type to "custom size" automatically.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/9898540313495-Banded-Group-Footer-Panel-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/9898557749271-Banded-Page-Header-Properties)
