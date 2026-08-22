---
title: "Export Page Setting Object Properties"
id: 1500009749362
section: "Page Panel Properties"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009749362-Export-Page-Setting-Object-Properties
updated_at: 2021-07-24T00:47:43Z
---

# Export Page Setting Object Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749322-Page-Footer-Panel-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009778181-Parameter-Control-Properties)

# Export Page Setting Object Properties

This topic describes the properties of an export page setting object. By defining the properties, you can customize the page properties for the exported result of the corresponding export format.

When you clear the **Auto** option for an export format and select **OK** in the [Export](https://devnet.logianalytics.com/hc/en-us/articles/1500009747842-Page-Setup-Dialog-Box-Properties#Export) tab of the **Page Setup** dialog box, Server adds an export page setting object in the Inspector tree for this specific export format. The page properties that you specified for any export format also apply when you advanced run and schedule to run the report in this format on Logi Report Server.

| Property Name | Description |
| --- | --- |
| Paper | |
| Height | Specifies the height of the page in inches or centimeters. The Width and Height values change when Orientation changes. The Page Type setting determines the Width and Height values, but you can change the latter as desired. Type a numeric value to change the height. Data type: Float |
| Height Auto Fit | Specifies whether to dynamically calculate the page height according to the height of the contents within the page. Data type: Boolean |
| Orientation | Specifies how to position the report page. The Orientation setting affects the Width and Height values. Choose an option from the drop-down list.  * **Portrait** - The page is positioned vertically. * **Landscape** - The page is positioned horizontally.   Data type: Enumeration |
| Page Type | Specifies the report page dimensions. Choose a size from the drop-down list. Data type: Enumeration |
| Width | Specifies the width of the page in inches or centimeters. The Width and Height values change when Orientation changes. The Page Type setting determines the Width and Height values, but you can change the latter as desired. Type a numeric value to change the width. Data type: Float |
| Width Auto Fit | Specifies whether to dynamically calculate the page width according to the width of the contents within the page. Data type: Boolean |
| Margin | |
| Bottom Margin | Specifies the distance in inches or centimeters between the bottom page edge and the data area. Type a numeric value to change the margin. Data type: Float |
| Left Margin | Specifies the distance in inches or centimeters between the left page edge and the data area. Type a numeric value to change the margin. Data type: Float |
| Right Margin | Specifies the distance in inches or centimeters between the right page edge and the data area. Type a numeric value to change the margin. Data type: Float |
| Top Margin | Specifies the distance in inches or centimeters between the top page edge and the data area. Type a numeric value to change the thickness. Data type: Float |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749322-Page-Footer-Panel-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009778181-Parameter-Control-Properties)
