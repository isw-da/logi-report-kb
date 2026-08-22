---
title: "Banded Object Properties"
id: 4405683609111
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683609111-Banded-Object-Properties
updated_at: 2022-01-27T07:58:34Z
---

# Banded Object Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683608087-Apply-Style-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683610135-Banded-Panel-Properties)

# Banded Object Properties

You can use the Banded Object Properties dialog box to edit the properties of a banded object. This topic describes the properties in the dialog box.

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

Use this tab to update general information of the banded object.

![Banded Object Properties dialog box - General tab](https://devnet.logianalytics.com/hc/article_attachments/4420447346711/bdobjprpty_gnrl.gif)

**Name**

Specify the display name of the banded object.

**Show NLS Value**

Select to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it, and when you have not modified the display name of the object.

**Position**

Select the position mode of the object when it is directly contained in the report body, a tabular cell, or a text box.

* **Absolute**  
  Select if you want to use the X and Y property values to decide the object's position.
* **Static**  
  Select if you want to place the object at the default location in its container. Server will hide or disable the X, Y, and other position-related properties.

**X**

Specify the X coordinate of the banded object, in inches.

**Y**

Specify the Y coordinate of the banded object, in inches.

**Width**

Specify the width of the banded object, in inches.

**Height**

Specify the height of the banded object, in inches.

**Auto Fit**

Select if you want to automatically adjust the width of a vertical banded object or the height of a horizontal banded object according to the contents.

**Background**

Specify the background color of the banded object.

To change the color, select the color indicator to access the [Select Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683679639-Select-Color-Dialog-Box-Properties), and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff.

If you want to make the background transparent, type **Transparent** in the text box.

## Border Tab Properties

Use this tab to specify border information of the banded object.

![Banded Object Properties dialog box - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4420453665303/bdobjprpty_border.gif)

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

![Banded Object Properties dialog box - Others tab](https://devnet.logianalytics.com/hc/article_attachments/4420453666071/bdobjprpty_other.gif)

**Auto Scale in Number**

Select **true** if you want to automatically scale the values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

**TOC Anchor**

Select **true** if you want to add the object to the TOC tree in the TOC Browser.

**Suppress When No Records**

Select **true** if you want to hide the object in the report when no record returns to its parent data component.

**Export to XLS**

Select **true** if you want to export the object when you save the report as an XLS file (make sure to check **Data Format** in the Export dialog box).

**Export to CSV**

Select **true** if you want to export the object when you save the report as a TXT file with Delimited Format.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683608087-Apply-Style-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683610135-Banded-Panel-Properties)
