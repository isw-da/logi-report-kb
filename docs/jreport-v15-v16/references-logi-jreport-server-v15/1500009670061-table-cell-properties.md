---
title: "Table Cell Properties"
id: 1500009670061
section: "References Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009670061-Table-Cell-Properties
updated_at: 2021-07-24T20:55:00Z
---

# Table Cell Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009645782-Split)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009645802-Table-Properties)

# Table Cell Properties

The Table Cell Properties dialog helps you to edit the properties of a table cell. It contains the following tabs:

* [General](#General)
* [Border](#Border)
* [Others](#Others)

**OK**

Applies the settings and closes this dialog.

**Cancel**

Cancels the settings and closes this dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## General

This tab shows some general information of the table cell. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920608407/tablecelprpty_gnrl.gif)

**Name**

Specifies the display name of the table cell, which will be shown on the shortcut menu of the table cell.

**Show NLS Value**

Specifies to show the translated name of the display name of the table cell in the Name text box if you have enabled the NLS feature and translated it.

If checked, this option takes effect only when the display name of the table cell is not modified.

**Background**

Specifies the background color of the table cell.

To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009645662-Select-Color) dialog and then specify a new color, or input a color string in the format #RRGGBB. If you want to make the background transparent, input Transparent in the text box.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Border

This tab shows information about borders of the table cell. You can modify all the border settings in this tab. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920609175/tablecelprpty_border.gif)

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

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Others

You can use this tab to view and configure some miscellaneous settings. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920610327/tablecelprpty_other.gif)

**Export to XLS**

If true, the table cell will be exported when you save the report result as an XLS file (make sure to check Data Format in the Export dialog).

**Export to CSV**

If true, the table cell will be exported when you save the report result as a TXT file with Delimited Format selected.

**Horizontal Alignment**

Specifies the horizontal alignment mode of the content in the table cell. When the Position property for the object in the cell is set to absolute, this property does not take effect.

**Vertical Alignment**

Specifies the vertical alignment mode of the content in the table cell. When the Position property for the object in the cell is set to absolute, this property does not take effect.

**Scope**

A representation of the standard HTML attribute *[scope](http://www.w3.org/TR/html401/struct/tables.html#adef-scope)*. This attribute specifies the set of data cells for which the current header cell provides header information.

* **Row** - The current cell provides header information for the rest of the row that contains it.
* **Column** - The current cell provides header information for the rest of the column that contains it.
* **None** - The scope attribute will not be generated when exporting to HTML.

**Joining Merge**

Specifies whether to make all the sequential rows included in the cell vertically merged in the report result. It is meaningful to set the property only when the cell is merged with other cells in the same column.

**Repeat**

Specifies whether to repeat the content of the cell in every page of the report result when the cell is split into pages.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009645782-Split)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009645802-Table-Properties)
