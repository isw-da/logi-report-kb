---
title: "Format Platform Dialog Box Properties"
id: 1500009772421
section: "Page Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009772421-Format-Platform-Dialog-Box-Properties
updated_at: 2021-07-24T00:49:13Z
---

# Format Platform Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744502-Format-Pie-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744522-Format-Pointer-Label-Dialog-Box-Properties)

# Format Platform Dialog Box Properties

You can use the Format Platform dialog box to format the platform of a chart. This topic describes the options in the dialog box.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Border Tab Properties](#Border)
* [Data Tab Properties](#Data)
* [Others Tab Properties](#Others)

**OK**

Applies the settings and closes this dialog box.

**Cancel**

Cancels the settings and closes this dialog box.

**Help**

Displays the help document about this feature.

## General Tab Properties

This tab shows some general information of the chart platform.

![Format Platform dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404885573911/fmtpltfrm_gnrl.gif)

**Name**

Specifies the display name of the platform.

**Show NLS Value**

Select this option to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it.

If you select this option, it takes effect only when you have not modified the display name of the object.

**Position**

Displays the position mode of the component. If the component is directly contained in the report body, a tabular cell, or a text box, you can modify its position mode.

* **Absolute**  
  Logi Report will decide the component's position by its X and Y property values.
* **Static**  
  Logi Report will position the component at the default location in its container. It will also hide or disable the X, Y, and other position-related properties.

**X**

Specifies the X coordinate of the platform.

**Y**

Specifies the Y coordinate of the platform.

**Width**

Specifies the width of the platform.

**Height**

Specifies the height of the platform.

**Fill Type**

Specifies a type for filling the platform.

**Color**

Indicates the background color of the platform.

To change the color, select the color indicator to bring out the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009745022-Select-Color-Dialog-Box-Properties) dialog box, and then specify a new color, or type a color string in the format #RRGGBB. If you want to make the background transparent, type Transparent in the text box.

**Transparency**

Specifies the transparency of the chart background color.

**Show Legend**

Specifies whether to show the legend.

## Border Tab Properties

This tab shows information about borders of the chart platform.

![Format Platform dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4404880514327/fmtpltfrm_border.gif)

**Line Style**

Specifies the line style of the platform borders.

**Border Type**

Specifies the type of the platform borders.

**Color**

Specifies the color of the platform borders.

**Transparency**

Specifies the color transparency of the platform borders.

**Thickness**

Specifies the thickness of the platform borders.

## Data Tab Properties

You can use this tab to view and configure properties of the chart data.

![Format Platform dialog - Data tab](https://devnet.logianalytics.com/hc/article_attachments/4404885574679/fmtpltfrm_data.gif)

**Sort Category**

Specifies the sorting order for the category field values.

**Sort Series**

Specifies the sorting order for the series field values.

**Reverse Category**

Specifies whether to reverse the category field value sequence.

**Reverse Series**

Specifies whether to reverse the series field value sequence.

**Category Start Offset**

Specifies the starting offset of the categories.

**Category End Offset**

Specifies the ending offset of the categories.

**Series Start Offset**

Specifies the starting offset of the series.

**Series End Offset**

Specifies the ending offset of the series.

**Category Value Encoding**

Specifies the encoding format for values on the category axis. Formats here usually refer to the following: BIG5, EUCJIS, GBK, UTF8, and XXXXX....

**Series Value Encoding**

Specifies the encoding format for values on the series axis. Formats here usually refer to the following: BIG5, EUCJIS, GBK, UTF8, and XXXXX....

**Swap Data Group**

Specifies to display values from different data fields by switching data between the category and series axes, the category and values axes.

## Others Tab Properties

You can use this tab to view and configure some miscellaneous settings.

![Format Platform dialog - Others tab](https://devnet.logianalytics.com/hc/article_attachments/4404880515991/fmtpltfrm_other.gif)

**Auto Scale in Number**

Specifies whether to
automatically scale the values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

**TOC Anchor**

Specifies whether to add the node that represents the platform to the TOC tree in the TOC Browser.

**Suppress When No Records**

Specifies whether to display the platform in the report result when no record is returned to its parent data component.

**Export to XLS**

If true, Server will export the component when you save the report result as an XLS file (make sure to check **Data Format** in the Export dialog box).

**Export to CSV**

If true, Server will export the component when you save the report result as a TXT file with Delimited Format selected.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744502-Format-Pie-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744522-Format-Pointer-Label-Dialog-Box-Properties)
