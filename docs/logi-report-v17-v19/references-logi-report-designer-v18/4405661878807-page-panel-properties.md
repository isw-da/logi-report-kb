---
title: "Page Panel Properties"
id: 4405661878807
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661878807-Page-Panel-Properties
updated_at: 2022-01-27T20:38:16Z
---

# Page Panel Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661877783-Oval-Shape-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664667799-Export-Page-Setting-Object-Properties)

# Page Panel Properties

This topic describes the properties of a [Page Panel object](https://devnet.logianalytics.com/hc/en-us/articles/4405664695447-Designing-the-Report-Pages#Panel). You can also specify the properties using the [Page Setup dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664543511-Page-Setup-Dialog-Box#General).

Designer provides some properties only when you use the object in certain [report types](https://devnet.logianalytics.com/hc/en-us/articles/4405661831319-Report-Object-Properties#ReportType). You can get details from the Available For column in the property table.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Shows the class type of the object. This property is read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. This property is read only. |
| This image notes any new content for version 18.3 of the product. For more information please see the Release Notes or Enhancements topics.TOC Page Panel | Page Report, Web Report | Shows whether the page panel is a TOC page panel. This property is read only. |
| Paper | | |
| Height | Page Report, Web Report, Library Component | Specifies the height of the page. Type a numeric value to change the height. Data type: Float |
| Height Auto Fit | Page Report, Web Report, Library Component | Specifies whether to dynamically calculate the page height according to the height of the contents within the page. Data type: Boolean |
| Orientation | Page Report, Web Report, Library Component | Specifies how to position the report page. Choose an option from the drop-down list. Designer disables this property when you select a formula to control either the Width or Height property.  * **portrait** - Select to position the page vertically. * **landscape** - Select to position the page horizontally.   Data type: Enumeration |
| Page Type | Page Report, Web Report, Library Component | Specifies the report page dimensions. Choose a size from the drop-down list. Data type: Enumeration |
| Width | Page Report, Web Report, Library Component | Specifies the width of the page. Type a numeric value to change the width. Data type: Float |
| Width Auto Fit | Page Report, Web Report, Library Component | Specifies whether to dynamically calculate the page width according to the width of the contents within the page. Data type: Boolean |
| Margin | | |
| Bottom Margin | Page Report, Web Report, Library Component | Specifies the distance between the report data and the bottom edge of the page. Type a numeric value to change the margin. Data type: Float |
| Left Margin | Page Report, Web Report, Library Component | Specifies the distance between the report data and the left edge of the page. Type a numeric value to change the margin. Data type: Float |
| Right Margin | Page Report, Web Report, Library Component | Specifies the distance between the report data and the right edge of the page. Type a numeric value to change the margin. Data type: Float |
| Top Margin | Page Report, Web Report, Library Component | Specifies the distance between the report data and the top edge of the page. Type a numeric value to change the margin. Data type: Float |
| Others | | |
| This image notes any new content for version 18.3 of the product. For more information please see the Release Notes or Enhancements topics.Invisible | Query Page Report | Specifies whether to hide the object in the design area and in the report. Logi Report Engine performs all calculations that involve the object regardless of whether the object is visible or not. Data type: Boolean |

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg)

* Designer changes the values for the Height and Width properties automatically when you change Orientation or Page Type; after you select a paper type and edit either Height or Width, Designer changes the paper type to "custom size" automatically.
* You can [use constant level formulas to control](https://devnet.logianalytics.com/hc/en-us/articles/4405664601367-Using-Formulas-to-Control-Object-Properties) some page properties for a page report tab, if you have [bound a data resource to its report body](https://devnet.logianalytics.com/hc/en-us/articles/4405661926423-Creating-Reports#BindData).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661877783-Oval-Shape-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664667799-Export-Page-Setting-Object-Properties)
