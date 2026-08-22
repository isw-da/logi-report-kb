---
title: "Parameter Field Properties"
id: 1500009744962
section: "Page Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009744962-Parameter-Field-Properties
updated_at: 2021-07-24T00:49:05Z
---

# Parameter Field Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744942-Parameter-Control-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009772901-Parameter-Form-Control-Properties)

# Parameter Field Properties

You can use the Parameter Field Properties dialog box to edit the properties of a parameter field. This topic describes the options in the dialog box.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Font Tab Properties](#Font)
* [Border Tab Properties](#Border)
* [Others Tab Properties](#Others)
* [Display Tab Properties](#Render)

**OK**

Applies the settings and closes this dialog box.

**Cancel**

Cancels the settings and closes this dialog box.

**Help**

Displays the help document about this feature.

## General Tab Properties

This tab shows some general information of the parameter field.

![Parameter Field Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404880486423/prmtrprpty_gnrl.gif)

**Name**

Specifies the display name of the parameter field.

**Show NLS Value**

Select this option to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it.

If you select this option, it takes effect only when you have not modified the display name of the object.

**Format**

Specifies the data format of the parameter field.

**Position**

Displays the position mode of the component. If the component is directly contained in the report body, a tabular cell, or a text box, you can modify its position mode.

* **Absolute**  
  Logi Report will decide the component's position by its X and Y property values.
* **Static**  
  Logi Report will position the component at the default location in its container. It will also hide or disable the X, Y, and other position-related properties.

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

To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009745022-Select-Color-Dialog-Box-Properties) dialog box and then specify a new color, or type a color string in the format #RRGGBB. If you want to make the background transparent, type Transparent in the text box.

**Foreground**

Specifies the foreground color of the parameter field.

To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009745022-Select-Color-Dialog-Box-Properties) dialog box and then specify a new color, or type a color string in the text box.

## Font Tab Properties

This tab shows the font-related information of the parameter field.

![Parameter Field Properties dialog - Font tab](https://devnet.logianalytics.com/hc/article_attachments/4404885552791/prmtrprpty_font.gif)

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

Specifies whether to attach a strikeout line to the field text.

**Italic**

Specifies whether to make the field text italic or not.

**Autofit**

Specifies whether to automatically adjust the width of the parameter field.

**Word Wrap**

Specifies whether to wrap the text to the parameter field width.

**Ignore HTML Tag**

By default, Logi Report Engine ignores the HTML tag elements that are included in the values of the parameter field so they display exactly as what they are in the report. Set the option to false if you want Logi Report Engine to transfer the HTML tag elements to the web browser so they are translated into HTML by the web browser. The setting also applies in the HTML output of the report.

## Border Tab Properties

This tab shows information about borders of the parameter field.

![Parameter Field Properties dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4404880487191/prmtrprpty_border.gif)

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

## Others Tab Properties

You can use this tab to view and configure some miscellaneous settings.

![Parameter Field Properties dialog - Others tab](https://devnet.logianalytics.com/hc/article_attachments/4404880487959/prmtrprpty_other.gif)

**TOC Anchor**

Specifies whether to add the node that represents the parameter field to the TOC tree in the TOC Browser.

**Suppress When No Records**

Specifies whether to display the parameter field in the report result when no record is returned to its parent data component.

**Export to XLS**

If true, Server will export the component when you save the report result as an XLS file (make sure to check **Data Format** in the Export dialog box).

**Export to CSV**

If true, Server will export the component when you save the report result as a TXT file with Delimited Format selected.

## Display Tab Properties

For a parameter field, you can change its display type to one of the following: Text, Rank, Image, Barcode, Text Field, Hidden Field, Text Area, Checkbox, Radio Button, List, Drop-down List, Image Button, Button, Submit, Reset and Hidden.

### List

Specifies to display the parameter field as list.

![Parameter Field Properties dialog - List Display Type](https://devnet.logianalytics.com/hc/article_attachments/4404885553943/prmtrprpty_rndrlst.gif)

**Name**

Specifies the name of the list.

**Title**

Specifies the title of the list.

**Selected**

Specifies the item to be selected.

**Allow Multiple**

Specifies whether to allow multiple items to be selected.

**Disabled**

Specifies whether to make the list disabled.

### Drop-Down List

Specifies to display the parameter field as drop-down list.

![Parameter Field Properties dialog - Drop-down List Display Type](https://devnet.logianalytics.com/hc/article_attachments/4404885554199/prmtrprpty_rndrdrpdwn.gif)

**Name**

Specifies the name of the drop-down list.

**Title**

Specifies the title of the drop-down list.

**Selected**

Specifies the item to be selected.

**Disabled**

Specifies whether to make the drop-down list disabled.

**Reference:** For the rest display types, see [Data Field Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009744242-Data-Field-Properties#Render).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744942-Parameter-Control-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009772901-Parameter-Form-Control-Properties)
