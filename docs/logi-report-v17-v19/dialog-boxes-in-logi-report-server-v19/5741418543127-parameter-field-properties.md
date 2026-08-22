---
title: "Parameter Field Properties"
id: 5741418543127
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741418543127-Parameter-Field-Properties
updated_at: 2022-10-31T17:16:29Z
---

# Parameter Field Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741425258519-Parameter-Control-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741425275799-Parameter-Form-Control-Properties)

# Parameter Field Properties

You can use the Parameter Field Properties dialog box to edit the properties of a parameter field. This topic describes the properties in the dialog box.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Font Tab Properties](#Font)
* [Border Tab Properties](#Border)
* [Others Tab Properties](#Others)
* [Display Tab Properties](#Render)

You see these elements on all the tabs:

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## General Tab Properties

Specify the general properties of the parameter field.

![Parameter Field Properties dialog box - General tab](https://devnet.logianalytics.com/hc/article_attachments/9905774036375/prmtrprpty_genrl.gif)

**Name**

Specify the display name of the parameter field.

**Show NLS Value**

Select to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it, and when you have not modified the display name of the object.

**Format**

Specify the data format of the parameter field.

**Format Locale**

Specify the locale for displaying and formatting values of the object when its data type is locale sensitive, such as the date and time formats, and number and currency formats. Default is the locale of your JVM or the language of the NLS report. Choose an option from the drop-down list if you want to change the locale.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) When you use a formula to control the locale, the return value should be the two-letter language and country codes as defined by ISO-639 and ISO-3166 in the format *language\_country*, for example, de\_DE.

**Position**

Select the position mode of the object when it is directly contained in the report body, a tabular cell, or a text box.

* **Absolute**  
  Select if you want to use the X and Y property values to decide the object's position.
* **Static**  
  Select if you want to place the object at the default location in its container. Server will hide or disable the X, Y, and other position-related properties.

**X**

Specify the X coordinate of the parameter field.

**Y**

Specify the Y coordinate of the parameter field.

**Width**

Specify the width of the parameter field.

**Height**

Specify the height of the parameter field.

**Top Padding**

Specify the space between the text of the object and its top border.

**Bottom Padding**

Specify the space between the text of the object and its bottom border.

**Left Padding**

Specify the space between the text of the object and its left border.

**Right Padding**

Specify the space between the text of the object and its right border.

**Background**

Specify the background color of the parameter field.

To change the color, select the color indicator to access the [Select Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741389405847-Select-Color-Dialog-Box-Properties), and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff. If you want to make the background transparent, type **Transparent** in the text box.

**Foreground**

Specify the foreground color of the parameter field.

To change the color, select the color indicator to access the [Select Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741389405847-Select-Color-Dialog-Box-Properties), and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff.

## Font Tab Properties

Specify the font properties of the parameter field.

![Parameter Field Properties dialog box - Font tab](https://devnet.logianalytics.com/hc/article_attachments/9905762397975/prmtrprpty_font.gif)

**Font**

Select the font face of the text.

**Size**

Specify the font size of the text.

**Horizontal Alignment**

Select the horizontal alignment mode of the text in the object.

**Vertical Alignment**

Select the vertical alignment mode of the text in the object.

**Bold**

Enable this property if you want to make the text bold.

**Italic**

Enable this property if you want to make the text italic.

**Underline**

Enable this property if you want to underline the text.

**Strikethrough**

Enable this property if you want to attach a strikeout line to the text.

**Autofit**

Enable this property if you want to automatically expand the object width according to the maximum length of the contents.

**Reduce Width When Autofit**

Enable this property if you want to reduce the width of the object according to its content when you specify to automatically adjust its width (the object's Autofit being true) and the actual width of the content is smaller than that of the object.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) This property takes effect when you set Position of the object to absolute; but, it does not work if the Word Wrap property of the object is true.

**Word Wrap**

Enable this property if you want to wrap the text to the object width.

**Ignore HTML Tag**

Enable this property if you don't want Logi Report Engine to parse the HTML tag elements in the text, at runtime or in the HTML output, so they display exactly as what they are in the report.

Disable this property if you want Engine to transfer the HTML tag elements to the web browser so the web browser translates them into HTML.

## Border Tab Properties

Specify the border properties of the parameter field.

![Parameter Field Properties dialog box - Border tab](https://devnet.logianalytics.com/hc/article_attachments/9905774071831/prmtrprpty_border.gif)

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

**Shadow**

Select **true** if you want to add a shadow effect to the border.

**Shadow Color**

Specify the color of the border shadow. To change the color, select the color indicator to access the [Select Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741389405847-Select-Color-Dialog-Box-Properties), and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff.

## Others Tab Properties

Use this tab to view and configure some miscellaneous settings.

![Parameter Field Properties dialog box - Others tab](https://devnet.logianalytics.com/hc/article_attachments/9905774092567/prmtrprpty_other.gif)

**TOC Anchor**

Select **true** if you want to add the object to the TOC tree in the TOC Browser.

**Suppress When No Records**

Select **true** if you want to hide the object in the report when no record returns to its parent data component.

**Export to XLS**

Select **true** if you want to export the object when you save the report as an XLS file (make sure to check **Data Format** in the Export dialog box).

**Export to CSV**

Select **true** if you want to export the object when you save the report as a TXT file with Delimited Format.

## Display Tab Properties

For a parameter field, you can change its display type. This section describes two display types: **List** and **Drop-down List**. For information about the other display types, see [Data Field Properties](https://devnet.logianalytics.com/hc/en-us/articles/5741396989975-Data-Field-Properties#Render).

### List

Select to display the parameter field as a list.

![Parameter Field Properties dialog box - List Display Type](https://devnet.logianalytics.com/hc/article_attachments/9905774118039/prmtrprpty_rndrlst.gif)

**Name**

Specify the name of the list.

**Title**

Specify the title of the list.

**Selected**

Specify the item you want to select in the list.

**Allow Multiple**

Select **true** if you want to select multiple items in the list.

**Disabled**

Select **true** if you want to disable the list.

### Drop-Down List

Select to display the parameter field as a drop-down list.

![Parameter Field Properties dialog box - Drop-down List Display Type](https://devnet.logianalytics.com/hc/article_attachments/9905762484119/prmtrprpty_rndrdrpdwn.gif)

**Name**

Specify the name of the drop-down list.

**Title**

Specify the title of the drop-down list.

**Selected**

Specify the item you want to select in the drop-down list.

**Disabled**

Select **true** if you want to disable the drop-down list.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741425258519-Parameter-Control-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741425275799-Parameter-Form-Control-Properties)
