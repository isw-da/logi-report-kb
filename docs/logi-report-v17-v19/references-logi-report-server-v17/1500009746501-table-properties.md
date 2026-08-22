---
title: "Table Properties"
id: 1500009746501
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009746501-Table-Properties
updated_at: 2021-07-25T07:19:54Z
---

# Table Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746481-Table-Cell-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009719942-Table-Row-Properties)

# Table Properties

The Table Properties dialog box is used to edit the properties of a table.

There are the following tabs in this dialog box: [General](#General), [Border](#Border) and [Others](#Others).

**OK**

Applies the settings and closes this dialog box.

**Cancel**

Cancels the settings and closes this dialog box.

**Help**

Displays the help document about this feature.

## General

This tab shows some general information of the table.

![Table Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404936907031/tableprpty_gnrl.gif)

**Name**

Specifies the display name of the table.

**Show NLS Value**

Select this option to show the translated name for the display name of the object in the Name text box if you have enabled the NLS feature and translated it.

If selected, this option takes effect only when the display name of the object is not modified.

**Position**

Specifies the position mode of the table. If the table is directly contained in the report body, a tabular cell, or a text box, its position mode can be modified.

* **Absolute**: The table's position will be decided by its X and Y property values.
* **Static**: The table will be positioned at the default location in its container. If selected, the X, Y and other position-related properties will be hidden or disabled.

**X**

Specifies the X coordinate of the table.

**Y**

Specifies the Y coordinate of the table.

**Width**

Specifies the width of the table.

**Height**

Specifies the height of the table.

**Background**

Specifies the background color of the table.

To change the color, select the color indicator to bring out the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009746261-Select-Color) dialog box and then specify a new color, or type a color string in the format #RRGGBB. If you want to make the background transparent, type Transparent in the text box.

## Border

This tab shows information about borders of the table.

![Table Properties dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4404942580759/tableprpty_border.gif)

**Color**

Specifies the border color.

**Width**

Specifies the border width.

**Top Line**

Specifies the style of the top border line.

**Bottom Line**

Specifies the style of the bottom border line.

**Left Line**

Specifies the style of the left border line.

**Right Line**

Specifies the style of the right border line.

## Others

You can use this tab to view and configure some miscellaneous settings.

![Table Properties dialog - Others tab](https://devnet.logianalytics.com/hc/article_attachments/4404942581015/tableprpty_other.gif)

**Auto Scale in Number**

Specifies whether to automatically scale the values that are of the Number data type in the table when the values fall into the two ranges:

* When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

**TOC Anchor**

Specifies whether or not to add the node that represents the table to the TOC tree in the TOC Browser.

**Suppress When No Records**

Specifies whether to display the table in the report result when no record is returned to its parent data component.

**Export to XLS**

If true, the table will be exported when you save the report result as an XLS file (make sure to check Data Format in the Export dialog box).

**Export to CSV**

If true, the table will be exported when you save the report result as a TXT file with Delimited Format selected.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746481-Table-Cell-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009719942-Table-Row-Properties)
