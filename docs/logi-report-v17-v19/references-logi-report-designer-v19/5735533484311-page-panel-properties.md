---
title: "Page Panel Properties"
id: 5735533484311
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735533484311-Page-Panel-Properties
updated_at: 2022-11-02T08:18:44Z
---

# Page Panel Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735517412759-Oval-Shape-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735546494871-Page-Header-Panel-Properties)

# Page Panel Properties

This topic describes the properties of a [Page Panel object](https://devnet.logianalytics.com/hc/en-us/articles/5735569908631-Designing-the-Report-Pages#Panel). You can also specify the properties using the [Page Setup dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552285079-Page-Setup-Dialog-Box#General).

Designer provides some properties only when you use the object in certain [report types](https://devnet.logianalytics.com/hc/en-us/articles/5735584998167-Report-Object-Properties#ReportType). You can get details from the Available For column in the property table.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Shows the class type of the object. Read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. Read only. |
| TOC Page Panel | Page Report, Web Report | Shows whether the page panel is a TOC page panel. Read only. |
| Paper | | |
| Height | Page Report, Web Report, Library Component | Specifies the height of the page. Type a numeric value to change the height. Data type: Float |
| Height Auto Fit | Page Report, Web Report, Library Component | Specifies whether to dynamically calculate the page height according to the height of the content within the page. Data type: Boolean |
| Orientation | Page Report, Web Report, Library Component | Specifies how you want to position the report page, vertically (portrait) or horizontally (landscape). Choose an option from the drop-down list. Data type: Enumeration  Note icon Designer disables this property when you select a formula to control either the Width or Height property. |
| Page Type | Page Report, Web Report, Library Component | Specifies the report page dimensions. Choose a size from the drop-down list. Data type: Enumeration |
| Width | Page Report, Web Report, Library Component | Specifies the width of the page. Type a numeric value to change the width. Data type: Float |
| Width Auto Fit | Page Report, Web Report, Library Component | Specifies whether to dynamically calculate the page width according to the width of the content within the page. Data type: Boolean |
| Margin | | |
| Bottom Margin | Page Report, Web Report, Library Component | Specifies the distance between the report data and the bottom edge of the page. Type a numeric value to change the margin. Data type: Float |
| Left Margin | Page Report, Web Report, Library Component | Specifies the distance between the report data and the left edge of the page. Type a numeric value to change the margin. Data type: Float |
| Right Margin | Page Report, Web Report, Library Component | Specifies the distance between the report data and the right edge of the page. Type a numeric value to change the margin. Data type: Float |
| Top Margin | Page Report, Web Report, Library Component | Specifies the distance between the report data and the top edge of the page. Type a numeric value to change the margin. Data type: Float |
| Others | | |
| Invisible | Query Page Report | Specifies whether to hide the object in the design area and in the report. Logi Report Engine performs all calculations that involve the object regardless of whether the object is visible or not. Data type: Boolean |

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)

* Designer changes the values for the Height and Width properties automatically when you change Orientation or Page Type; after you select a paper type and edit either Height or Width, Designer changes the paper type to "custom size" automatically.
* You can [use constant level formulas to control](https://devnet.logianalytics.com/hc/en-us/articles/5735545031703-Using-Formulas-to-Control-Object-Properties) some page properties for a page report tab, if you have [bound a data resource to its report body](https://devnet.logianalytics.com/hc/en-us/articles/5735586128791-Applying-Datasets-in-a-Report#BindData).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735517412759-Oval-Shape-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735546494871-Page-Header-Panel-Properties)
