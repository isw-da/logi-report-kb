---
title: "Parameter Field Properties"
id: 1500009713681
section: "Page Report Studio Dialogs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009713681-Parameter-Field-Properties
updated_at: 2021-11-03T06:58:03Z
---

# Parameter Field Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009713641-Parameter-Control-Properties)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009713661-Parameter-Form-Control-Properties)

# Parameter Field Properties

The Parameter Field Properties dialog helps you to edit the properties of a parameter field. It contains the following tabs: [General](#General), [Font](#Font), [Border](#Border), [Others](#Others) and [Display](#Render).

**OK**

Applies the settings and closes this dialog.

**Cancel**

Cancels the settings and closes this dialog.

**Help**

Displays the help document about this feature.

## General

This tab shows some general information of the parameter field.

![Parameter Field Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4412131492247/prmtrprpty_gnrl.gif)

**Name**

Specifies the display name of the parameter field.

**Show NLS Value**

Specifies to show the translated name for the display name of the parameter field in the Name text box if you have enabled the NLS feature and translated it.

If checked, this option takes effect only when the display name of the parameter field is not modified.

**Format**

Specifies the data format of the parameter field.

**Position**

Specifies the position mode of the parameter field. If the parameter field is directly contained in the report body, a tabular cell, or a text box, its position mode can be modified.

* **Absolute**: The parameter field's position will be decided by its X and Y property values.
* **Static**: The parameter field will be positioned at the default location in its container. If selected, the X, Y and other position-related properties will be hidden or disabled.

**X**

Specifies the X coordinate of the parameter field.

**Y**

Specifies the Y coordinate of the parameter field.

**Width**

Specifies the width of the parameter field.

**Height**

Specifies the height of the parameter field.

**Top Padding**

Specifies the space between the text of the parameter field and its top border.

**Bottom Padding**

Specifies the space between the text of the parameter field and its bottom border.

**Left Padding**

Specifies the space between the text of the parameter field and its left border.

**Right Padding**

Specifies the space between the text of the parameter field and its right border.

**Background**

Specifies the background color of the parameter field.

To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009713741-Select-Color) dialog and then specify a new color, or input a color string in the format #RRGGBB. If you want to make the background transparent, input Transparent in the text box.

**Foreground**

Specifies the foreground color of the parameter field.

To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009713741-Select-Color) dialog and then specify a new color, or input a color string in the text box.

## Font

This tab shows the font-related information of the parameter field.

![Parameter Field Properties dialog - Font tab](https://devnet.logianalytics.com/hc/article_attachments/4412112617495/prmtrprpty_font.gif)

**Font**

Specifies the font face of the field text.

**Size**

Specifies the font size of the field text.

**Horizontal Alignment**

Specifies the horizontal alignment mode of the text in the parameter field.

**Vertical Alignment**

Specifies the vertical alignment mode of the text in the parameter field.

**Bold**

Specifies whether to make the field text bold or not.

**Underline**

Specifies whether the field text will be underlined or not.

**Strikethrough**

Specifies whether or not to attach a strikeout line to the field text.

**Italic**

Specifies whether to make the field text italic or not.

**Autofit**

Specifies whether or not to automatically adjust the width of the parameter field.

**Word Wrap**

Specifies whether or not to wrap the text to the parameter field width.

**Ignore HTML Tag**

If this option is unchecked, Logi JReport will parse HTML tag elements in the field value while the report is to be saved as an HTML file; or the field value will appear in the HTML file the same as that in Page Report Studio (HTML tag elements in the field value, if any, will not be parsed).

## Border

This tab shows information about borders of the parameter field.

![Parameter Field Properties dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4412131492503/prmtrprpty_border.gif)

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

**Shadow**

Specifies whether the borders will have a shadow effect or not.

**Shadow Color**

Specifies the color of the border shadow.

## Others

You can use this tab to view and configure some miscellaneous settings.

![Parameter Field Properties dialog - Others tab](https://devnet.logianalytics.com/hc/article_attachments/4412131492759/prmtrprpty_other.gif)

**TOC Anchor**

Specifies whether or not to add the node that represents the parameter field to the TOC tree that is displayed in the TOC Browser.

**Suppress When No Records**

Specifies whether to display the parameter field in the report result when no record is returned to its parent data component.

**Export to XLS**

If true, the parameter field will be exported when you save the report result as an XLS file (make sure to check Data Format in the Export dialog).

**Export to CSV**

If true, the parameter field will be exported when you save the report result as a TXT file with Delimited Format selected.

## Display

For a parameter field, you can change its display type to one of the following: Text, Rank, Image, Barcode, Text Field, Hidden Field, Text Area, Checkbox, Radio Button, List, Drop-down List, Image Button, Button, Submit, Reset and Hidden.

### List

Specifies to display the parameter field as list.

![Parameter Field Properties dialog - List Display Type](https://devnet.logianalytics.com/hc/article_attachments/4412131493015/prmtrprpty_rndrlst.gif)

**Name**

Specifies the name of the list.

**Title**

Specifies the title of the list.

**Selected**

Specifies the item to be selected.

**Allow Multiple**

Specifies whether or not to allow multiple items to be selected.

**Disabled**

Specifies whether or not to make the list disabled.

### Drop-Down List

Specifies to display the parameter field as drop-down list.

![Parameter Field Properties dialog - Drop-down List Display Type](https://devnet.logianalytics.com/hc/article_attachments/4412131493527/prmtrprpty_rndrdrpdwn.gif)

**Name**

Specifies the name of the drop-down list.

**Title**

Specifies the title of the drop-down list.

**Selected**

Specifies the item to be selected.

**Disabled**

Specifies whether or not to make the drop-down list disabled.

**Reference:** For the rest display types, see [Data Field Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009687162-Data-Field-Properties#Render).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009713641-Parameter-Control-Properties)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009713661-Parameter-Form-Control-Properties)
