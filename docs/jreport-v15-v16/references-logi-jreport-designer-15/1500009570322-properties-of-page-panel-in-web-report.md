---
title: "Properties of Page Panel in Web Report"
id: 1500009570322
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009570322-Properties-of-Page-Panel-in-Web-Report
updated_at: 2021-07-24T05:53:58Z
---

# Properties of Page Panel in Web Report

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009570302-Properties-of-OLE-Object-Multimedia-Object-in-Web-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009570342-Properties-of-Page-Header-Panel-in-Web-Report)

# Properties of Page Panel in Web Report

A page panel can have the following child objects: [Page Header Panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009570342-Properties-of-Page-Header-Panel-in-Web-Report), [Page Footer Panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009592241-Properties-of-Page-Footer-Panel-in-Web-Report) and [Export Page Setting Object](https://devnet.logianalytics.com/hc/en-us/articles/1500009570362-Properties-of-Export-Page-Setting-Object-in-Web-Report).

The properties of a page panel object in a web report are as follows:

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

You can also define the properties via the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009588121-Page-Setup-Dialog#General) dialog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009570302-Properties-of-OLE-Object-Multimedia-Object-in-Web-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009570342-Properties-of-Page-Header-Panel-in-Web-Report)
