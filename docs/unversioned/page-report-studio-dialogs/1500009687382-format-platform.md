---
title: "Format Platform"
id: 1500009687382
section: "Page Report Studio Dialogs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009687382-Format-Platform
updated_at: 2021-11-03T06:58:11Z
---

# Format Platform

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009713301-Format-Pie)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009687402-Format-Pointer-Label)

# Format Platform

The Format Platform dialog helps you to format the platform of a chart. It contains the following tabs: [General](#General), [Border](#Border), [Data](#Data) and [Others](#Others).

**OK**

Applies the settings and closes this dialog.

**Cancel**

Cancels the settings and closes this dialog.

**Help**

Displays the help document about this feature.

## General

This tab shows some general information of the chart platform.

![Format Platform dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4412112621975/fmtpltfrm_gnrl.gif)

**Name**

Specifies the display name of the platform.

**Show NLS Value**

Specifies to show the translated name for the display name of the platform in the Name text box if you have enabled the NLS feature and translated it.

If checked, this option takes effect only when the display name of the platform is not modified.

**Position**

Displays the position mode of the platform. If the platform is directly contained in the report body, a tabular cell, or a text box, its position mode can be modified.

* **Absolute**: The platform's position will be decided by its X and Y property values.
* **Static**: The platform will be positioned at the default location in its container. If selected, the X, Y and other position-related properties will be hidden or disabled.

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

To change the color, select the color indicator to bring out the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009713741-Select-Color) dialog, and then specify a new color, or input a color string in the format #RRGGBB. If you want to make the background transparent, input Transparent in the text box.

**Transparency**

Specifies the transparency of the chart background color.

**Show Legend**

Specifies whether or not to show the legend.

## Border

This tab shows information about borders of the chart platform.

![Format Platform dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4412112622231/fmtpltfrm_border.gif)

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

## Data

You can use this tab to view and configure properties of the chart data.

![Format Platform dialog - Data tab](https://devnet.logianalytics.com/hc/article_attachments/4412131499799/fmtpltfrm_data.gif)

**Sort Category**

Specifies the sorting order for the category field values.

**Sort Series**

Specifies the sorting order for the series field values.

**Reverse Category**

Specifies whether or not to reverse the category field value sequence.

**Reverse Series**

Specifies whether or not to reverse the series field value sequence.

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

## Others

You can use this tab to view and configure some miscellaneous settings.

![Format Platform dialog - Others tab](https://devnet.logianalytics.com/hc/article_attachments/4412139587095/fmtpltfrm_other.gif)

**Auto Scale in Number**

Specifies whether to
automatically scale the values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

**TOC Anchor**

Specifies whether or not to add the node that represents the platform to the TOC tree that is displayed in the TOC Browser.

**Suppress When No Records**

Specifies whether to display the platform in the report result when no record is returned to its parent data component.

**Export to XLS**

If true, the platform will be exported when you save the report result as an XLS file (make sure to check Data Format in the Export dialog).

**Export to CSV**

If true, the platform will be exported when you save the report result as a TXT file with Delimited Format selected.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009713301-Format-Pie)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009687402-Format-Pointer-Label)
