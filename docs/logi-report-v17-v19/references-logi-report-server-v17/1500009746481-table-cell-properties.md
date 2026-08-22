---
title: "Table Cell Properties"
id: 1500009746481
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009746481-Table-Cell-Properties
updated_at: 2021-07-25T07:19:54Z
---

# Table Cell Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746421-Style-List)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009746501-Table-Properties)

# Table Cell Properties

The Table Cell Properties dialog box is used to edit the properties of a table cell.

There are the following tabs in this dialog box: [General](#General), [Border](#Border) and [Others](#Others).

**OK**

Applies the settings and closes this dialog box.

**Cancel**

Cancels the settings and closes this dialog box.

**Help**

Displays the help document about this feature.

## General

This tab shows some general information of the table cell.

![Table Cell Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404936907287/tablecelprpty_gnrl.gif)

**Name**

Specifies the display name of the table cell.

**Show NLS Value**

Select this option to show the translated name for the display name of the object in the Name text box if you have enabled the NLS feature and translated it.

If selected, this option takes effect only when the display name of the object is not modified.

**Background**

Specifies the background color of the table cell.

To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009746261-Select-Color) dialog box and then specify a new color, or type a color string in the format #RRGGBB. If you want to make the background transparent, type Transparent in the text box.

## Border

This tab shows information about borders of the table cell. You can modify all the border settings in this tab.

![Table Cell Properties dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4404942581271/tablecelprpty_border.gif)

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

![Table Cell Properties dialog - Others tab](https://devnet.logianalytics.com/hc/article_attachments/4404942581527/tablecelprpty_other.gif)

**Export to XLS**

If true, the table cell will be exported when you save the report result as an XLS file (make sure to check Data Format in the Export dialog box).

**Export to CSV**

If true, the table cell will be exported when you save the report result as a TXT file with Delimited Format selected.

**Horizontal Alignment**

Specifies the horizontal alignment mode of the content in the table cell. When the Position property for the object in the cell is set to absolute, this property does not take effect.

**Vertical Alignment**

Specifies the vertical alignment mode of the content in the table cell. When the Position property for the object in the cell is set to absolute, this property does note take effect.

**Scope**

A representation of the standard HTML attribute *[scope](http://www.w3.org/TR/html401/struct/tables.html#adef-scope)*. This attribute specifies the set of data cells for which the current header cell provides header information.

* **Row** - The current cell provides header information for the rest of the row that contains it.
* **Column** - The current cell provides header information for the rest of the column that contains it.
* **None** - The scope attribute will not be generated when exporting to HTML.

**Joining Merge**

Specifies whether to make all the sequential rows included in the cell vertically merged in the report result. It is meaningful to set the property only when the cell is merged with other cells in the same column.

**Repeat**

Specifies whether to repeat the content of the cell in every page of the report result when the cell is split into pages.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746421-Style-List)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009746501-Table-Properties)
