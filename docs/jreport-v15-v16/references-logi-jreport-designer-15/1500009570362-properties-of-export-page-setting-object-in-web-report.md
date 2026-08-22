---
title: "Properties of Export Page Setting Object in Web Report"
id: 1500009570362
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009570362-Properties-of-Export-Page-Setting-Object-in-Web-Report
updated_at: 2021-07-24T05:53:58Z
---

# Properties of Export Page Setting Object in Web Report

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592241-Properties-of-Page-Footer-Panel-in-Web-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592281-Properties-of-Parameter-Control-in-Web-Report)

# Properties of Export Page Setting Object in Web Report

When you uncheck the Auto option for an export format and select OK in the [Export](https://devnet.logianalytics.com/hc/en-us/articles/1500009588121-Page-Setup-Dialog) tab [of the Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009588121-Page-Setup-Dialog) dialog, an export page setting object is added in the Report Inspector tree for this specific export format. By defining the properties of an export page setting object, you can customize the page properties for the exported result of the corresponding export format. The page properties specified for any export format will also be applied when advanced running and scheduling to run the report in this format on Logi JReport Server.

The properties for an export page setting object in a web report are as follows:

| Property Name | Description |
| --- | --- |
| Paper | |
| Height | Specifies the height of the page. The Width and Height values change when Orientation changes. The Page Type setting determines the Width and Height values but you can change the latter as desired. Enter a numeric value to change the height. Data type: Float |
| Height Auto Fit | Specifies whether to dynamically calculate the page height according to the height of the contents within the page. Data type: Boolean |
| Orientation | Specifies how to position the report page. The Orientation setting affects the Width and Height values. Choose an option from the drop-down list.  * **portrait** - The page is positioned vertically. * **landscape** - The page is positioned horizontally.   Data type: Enumeration |
| Page Type | Specifies the report page dimensions. Choose a size from the drop-down list. Data type: Enumeration |
| Width | Specifies the width of the page. The Width and Height values change when Orientation changes. The Page Type setting determines the Width and Height values but you can change the latter as desired. Enter a numeric value to change the width. Data type: Float |
| Width Auto Fit | Specifies whether to dynamically calculate the page width according to the width of the contents within the page. Data type: Boolean |
| Margin | |
| Bottom Margin | Specifies the distance between the bottom page edge and the data area. Enter a numeric value to change the margin. Data type: Float |
| Left Margin | Specifies the distance between the left page edge and the data area. Enter a numeric value to change the margin. Data type: Float |
| Right Margin | Specifies the distance between the right page edge and the data area. Enter a numeric value to change the margin. Data type: Float |
| Top Margin | Specifies the distance between the top page edge and the data area. Enter a numeric value to change the thickness. Data type: Float |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592241-Properties-of-Page-Footer-Panel-in-Web-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592281-Properties-of-Parameter-Control-in-Web-Report)
