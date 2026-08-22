---
title: "Parameter Control Properties"
id: 5741425258519
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741425258519-Parameter-Control-Properties
updated_at: 2022-10-31T17:16:30Z
---

# Parameter Control Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741440252183-Page-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741418543127-Parameter-Field-Properties)

# Parameter Control Properties

You can use the Parameter Control Properties dialog box to edit the properties of a parameter control. This topic describes the properties in the dialog box.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Font Tab Properties](#Font)
* [Border Tab Properties](#Border)

You see these elements on all the tabs:

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## General Tab Properties

Specify the general properties of the parameter control.

![Parameter Control Properties dialog box - General tab](https://devnet.logianalytics.com/hc/article_attachments/9905762582679/prmctrlprpty_gnrl.gif)

**Name**

Specify the name of the parameter control.

**Show NLS Value**

Select to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it, and when you have not modified the display name of the object.

**Format**

Specify the display format of the parameter values.

**Position**

Select the position mode of the object when it is directly contained in the report body, a tabular cell, or a text box.

* **Absolute**  
  Select if you want to use the X and Y property values to decide the object's position.
* **Static**  
  Select if you want to place the object at the default location in its container. Server will hide or disable the X, Y, and other position-related properties.

**Parameter**

The name of the parameter.

**X**

Specify the X coordinate of the parameter control.

**Y**

Specify the Y coordinate of the parameter control.

**Width**

Specify the width of the parameter control.

**Height**

Specify the height of the parameter control.

**Top Padding**

Specify the space between the text of the object and its top border.

**Bottom Padding**

Specify the space between the text of the object and its bottom border.

**Left Padding**

Specify the space between the text of the object and its left border.

**Right Padding**

Specify the space between the text of the object and its right border.

**Background**

Specify the background color of the parameter control.

To change the color, select the color indicator to access the [Select Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741389405847-Select-Color-Dialog-Box-Properties), and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff. If you want to make the background transparent, type **Transparent** in the text box.

**Foreground**

Specify the foreground color of the parameter control.

To change the color, select the color indicator to access the [Select Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741389405847-Select-Color-Dialog-Box-Properties), and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff.

**Export as Text**

Enable this property if you want to export the parameter control as text. Otherwise, Logi Report will export the parameter control as an image.

When you enable this property, depending on the properties of the parameter in the parameter control, Logi Report will export the parameter control as follows:

* Logi Report will export the selected values or text of the parameter as text while it will not export the icon or button for specifying the parameter value.
* If the parameter in the parameter control is of Boolean type, Logi Report displays it as a checkbox in the parameter control. Then when you select the checkbox, Logi Report will export it as ![Checkmark](https://devnet.logianalytics.com/hc/article_attachments/9905635142039/chkmrk.gif), or as ![Checkbox](https://devnet.logianalytics.com/hc/article_attachments/9905635178903/chkbox.gif) if you clear the checkbox.

## Font Tab Properties

Specify the font properties of the text in the parameter control.

![Parameter Control Properties dialog box - Font tab](https://devnet.logianalytics.com/hc/article_attachments/9905762603287/prmctrlprpty_font.gif)

**Font**

Select the font face of the text.

**Size**

Specify the font size of the text.

**Horizontal Alignment**

Select the horizontal alignment mode of the text.

**Vertical Alignment**

Select the vertical alignment mode of the text.

**Bold**

Select **true** to make the text bold.

**Underline**

Select **true** to underline the text.

**Italic**

Select **true** to make the text italic.

## Border Tab Properties

Specify the border properties of the parameter control.

![Parameter Control Properties dialog box - Border tab](https://devnet.logianalytics.com/hc/article_attachments/9905774310679/prmctrlprpty_border.gif)

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741440252183-Page-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741418543127-Parameter-Field-Properties)
