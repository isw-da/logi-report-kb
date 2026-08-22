---
title: "Table Cell Properties"
id: 4405690527255
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690527255-Table-Cell-Properties
updated_at: 2022-01-27T07:58:50Z
---

# Table Cell Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690525463-Style-List-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683687703-Table-Properties)

# Table Cell Properties

You can use the Table Cell Properties dialog box to edit the properties of a table cell. This topic describes the properties in the dialog box.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Border Tab Properties](#Border)
* [Others Tab Properties](#Others)

You see these elements on all the tabs:

**OK**

Select to apply any changes you made here and exit the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## General Tab Properties

Specify the general properties of the table cell.

![Table Cell Properties dialog box - General tab](https://devnet.logianalytics.com/hc/article_attachments/4420447303959/tablecelprpty_gnrl.gif)

**Name**

Specify the display name of the table cell.

**Show NLS Value**

Select to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it, and when you have not modified the display name of the object.

**Background**

Specify the background color of the table cell.

To change the color, select the color indicator to access the [Select Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683679639-Select-Color-Dialog-Box-Properties), and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff. If you want to make the background transparent, type **Transparent** in the text box.

## Border Tab Properties

Specify the border properties of the table cell.

![Table Cell Properties dialog box - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4420461694999/tablecelprpty_border.gif)

**Color**

Specify the border color.

**Width**

Specify the border width in inches.

**Top Line**

Select the style of the top border line.

**Bottom Line**

Select the style of the bottom border line.

**Left Line**

Select the style of the left border line.

**Right Line**

Select the style of the right border line.

## Others Tab Properties

Configure some miscellaneous settings.

![Table Cell Properties dialog box - Others tab](https://devnet.logianalytics.com/hc/article_attachments/4420453624599/tablecelprpty_other.gif)

**Export to XLS**

Select **true** if you want to export the object when you save the report as an XLS file (make sure to check **Data Format** in the Export dialog box).

**Export to CSV**

Select **true** if you want to export the object when you save the report as a TXT file with Delimited Format.

**Horizontal Alignment**

Specify the horizontal alignment mode of the contents in the table cell. When the Position property for the object in the cell is absolute, this property does not take effect.

**Vertical Alignment**

Specify the vertical alignment mode of the contents in the table cell. When the Position property for the object in the cell is absolute, this property does not take effect.

**Scope**

A representation of the standard HTML attribute *[scope](http://www.w3.org/TR/html401/struct/tables.html#adef-scope)*. Specify the set of data cells for which the current header cell provides header information.

* **row**  
  Select if you want the current cell to provide header information for the rest of the row that contains it.
* **column**  
  Select if you want the current cell to provide header information for the rest of the column that contains it.
* **none**Select if you don't want to generate the scope attribute when exporting to HTML.

**Joining Merge**

Select **true** to make all the sequential rows in the cell vertically merged in the report. It is meaningful to set the property only when the cell merges with other cells in the same column.

**Repeat**

Select **true** to repeat the contents of the cell in every page of the report when the cell splits into pages.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690525463-Style-List-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683687703-Table-Properties)
