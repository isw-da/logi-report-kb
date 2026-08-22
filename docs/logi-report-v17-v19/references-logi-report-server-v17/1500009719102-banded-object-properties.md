---
title: "Banded Object Properties"
id: 1500009719102
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009719102-Banded-Object-Properties
updated_at: 2021-07-25T07:20:11Z
---

# Banded Object Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009745201-Apply-Style)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745221-Banded-Panel-Properties)

# Banded Object Properties

The Banded Object Properties dialog box is used to edit the properties of a banded object.

There are the following tabs in this dialog box: [General](#General), [Border](#Border) and [Others](#Others).

**OK**

Applies the settings and closes this dialog box.

**Cancel**

Cancels the settings and closes this dialog box.

**Help**

Displays the help document about this feature.

## General

This tab shows some general information of the banded object.

![Banded Object Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404936952855/bdobjprpty_gnrl.gif)

**Name**

Specifies the display name of the banded object.

**Show NLS Value**

Select this option to show the translated name for the display name of the object in the Name text box if you have enabled the NLS feature and translated it.

If selected, this option takes effect only when the display name of the object is not modified.

**Position**

Displays the position mode of the banded object. If the banded object is directly contained in the report body, a tabular cell, or a text box, its position mode can be modified.

* **Absolute**: The banded object's position will be decided by its X and Y property values.
* **Static**: The banded object will be positioned at the default location in its container. If selected, the X, Y and other position-related properties will be hidden or disabled.

**X**

Specifies the X coordinate of the banded object, in inches.

**Y**

Specifies the Y coordinate of the banded object, in inches.

**Width**

Specifies the width of the banded object, in inches.

**Height**

Specifies the height of the banded object, in inches.

**Background**

Specifies the background color of the banded object.

To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009746261-Select-Color) dialog box and then specify a new color, or type a color string in the format #RRGGBB. If you want to make the background transparent, type Transparent in the text box.

## Border

This tab shows information about borders of the banded object.

![Banded Object Properties dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4404936953111/bdobjprpty_border.gif)

**Color**

Specifies the border color. To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009746261-Select-Color) dialog box and then specify a new color, or type a color string in the format #RRGGBB.

**Width**

Specifies the border width in inches.

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

![Banded Object Properties dialog - Others tab](https://devnet.logianalytics.com/hc/article_attachments/4404936953367/bdobjprpty_other.gif)

**Auto Scale in Number**

Specifies whether to
automatically scale the values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

**TOC Anchor**

Specifies whether to add the node that represents the banded object to the TOC tree in the TOC Browser.

**Suppress When No Records**

Specifies whether to display the banded object in the report result when no record is returned to its parent data component.

**Export to XLS**

If true, the banded object will be exported when you save the report result as an XLS file (make sure to check Data Format in the Export dialog box).

**Export to CSV**

If true, the banded object will be exported when you save the report result as a TXT file with Delimited Format selected.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009745201-Apply-Style)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745221-Banded-Panel-Properties)
