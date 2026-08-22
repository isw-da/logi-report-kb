---
title: "Parameter Control Properties"
id: 1500009744942
section: "Page Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009744942-Parameter-Control-Properties
updated_at: 2021-07-24T00:49:06Z
---

# Parameter Control Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009772861-Page-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744962-Parameter-Field-Properties)

# Parameter Control Properties

You can use the Parameter Control Properties dialog box to edit the properties of a parameter control. This topic describes the options in the dialog box.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Font Tab Properties](#Font)
* [Border Tab Properties](#Border)

**OK**

Applies the settings and closes this dialog box.

**Cancel**

Cancels the settings and closes this dialog box.

**Help**

Displays the help document about this feature.

## General Tab Properties

This tab shows some general information of the parameter control.

![Parameter Control Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404880489751/prmctrlprpty_gnrl.gif)

**Name**

Specifies the name of the parameter control.

**Show NLS Value**

Select this option to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it.

If you select this option, it takes effect only when you have not modified the display name of the object.

**Format**

Specifies the display format of the parameter value.

**Position**

Displays the position mode of the component. If the component is directly contained in the report body, a tabular cell, or a text box, you can modify its position mode.

* **Absolute**  
  Logi Report will decide the component's position by its X and Y property values.
* **Static**  
  Logi Report will position the component at the default location in its container. It will also hide or disable the X, Y, and other position-related properties.

**Parameter**

Displays the name of the parameter.

**X**

Specifies the X coordinate of the parameter control.

**Y**

Specifies the Y coordinate of the parameter control.

**Width**

Specifies the width of the parameter control.

**Height**

Specifies the height of the parameter control.

**Top Padding**

Specifies the space between the text of the parameter control and its top border.

**Bottom Padding**

Specifies the space between the text of the parameter control and its bottom border.

**Left Padding**

Specifies the space between the text of the parameter control and its left border.

**Right Padding**

Specifies the space between the text of the parameter control and its right border.

**Background**

Specifies the background color of the parameter control.

To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009745022-Select-Color-Dialog-Box-Properties) dialog box and then specify a new color, or type a color string in the format #RRGGBB. If you want to make the background transparent, type Transparent in the text box.

**Foreground**

Specifies the foreground color of the parameter control.

To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009745022-Select-Color-Dialog-Box-Properties) dialog box and then specify a new color, or type a color string in the format #RRGGBB.

**Export as Text**

Specifies whether to export the parameter control as text. If you do not enable this option, Logi Report will export the parameter control as an image.

When you enable this option, depending on the properties of the parameter bound in the parameter control, Logi Report will export the parameter control as follows:

* Logi Report will export the selected values or text of the parameter as text while it will not export the icon or button for specifying the parameter value.
* If the parameter in the parameter control is of Boolean type, Logi Report displays it as a check box in the parameter control. Then when you select the check box, Logi Report will export it as ![Checkmark](https://devnet.logianalytics.com/hc/article_attachments/4404885377047/chkmrk.gif), or as ![Checkbox](https://devnet.logianalytics.com/hc/article_attachments/4404880239639/chkbox.gif) if you do not select the check box.

## Font Tab Properties

This tab shows the font-related information of the text in the parameter control.

![Parameter Control Properties dialog - Font tab](https://devnet.logianalytics.com/hc/article_attachments/4404880490007/prmctrlprpty_font.gif)

**Font**

Specifies the font face of the text.

**Size**

Specifies the font size of the text.

**Horizontal Alignment**

Specifies the horizontal alignment mode of the text.

**Vertical Alignment**

Specifies the vertical alignment mode of the text.

**Bold**

Specifies whether to make the text bold or not.

**Underline**

Specifies whether the text will be underlined or not.

**Italic**

Specifies whether to make the text italic or not.

## Border Tab Properties

This tab shows information about borders of the parameter control.

![Parameter Control Properties dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4404880490391/prmctrlprpty_border.gif)

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009772861-Page-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744962-Parameter-Field-Properties)
