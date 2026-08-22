---
title: "Parameter Control Properties"
id: 1500009746161
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009746161-Parameter-Control-Properties
updated_at: 2021-07-25T07:19:58Z
---

# Parameter Control Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746141-Page-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009719822-Parameter-Field-Properties)

# Parameter Control Properties

The Parameter Control Properties dialog box is used to edit the properties of a parameter control.

There are the following tabs in this dialog box: [General](#General), [Font](#Font) and [Border](#Border).

**OK**

Applies the settings and closes this dialog box.

**Cancel**

Cancels the settings and closes this dialog box.

**Help**

Displays the help document about this feature.

## General

This tab shows some general information of the parameter control.

![Parameter Control Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404936916119/prmctrlprpty_gnrl.gif)

**Name**

Specifies the name of the parameter control.

**Show NLS Value**

Select this option to show the translated name for the display name of the object in the Name text box if you have enabled the NLS feature and translated it.

If selected, this option takes effect only when the display name of the object is not modified.

**Format**

Specifies the display format of the parameter value.

**Position**

Displays the position mode of the parameter control. If the parameter control is directly contained in the report body, a tabular cell, or a text box, its position mode can be modified.

* **Absolute**: The parameter control's position will be decided by its X and Y property values.
* **Static**: The parameter control will be positioned at the default location in its container. If selected, the X, Y and other position-related properties will be hidden or disabled.

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

To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009746261-Select-Color) dialog box and then specify a new color, or type a color string in the format #RRGGBB. If you want to make the background transparent, type Transparent in the text box.

**Foreground**

Specifies the foreground color of the parameter control.

To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009746261-Select-Color) dialog box and then specify a new color, or type a color string in the format #RRGGBB.

**Export as Text**

Specifies whether to export the parameter control as text. If this option is unselected, the parameter control will be exported as an image.

When Export as Text is selected, depending on the properties of the parameter bound in the parameter control, Logi Report will export the parameter control as follows:

* The selected values or text of the parameter will be exported as text while the icon or button for specifying the parameter value not exported.
* If the parameter in the parameter control is of Boolean type, Logi Report displays it as a check box in the parameter control. Then when the check box is selected, it will be exported as ![Checkmark](https://devnet.logianalytics.com/hc/article_attachments/4404942485783/chkmrk.gif) and if unselected as ![Checkbox](https://devnet.logianalytics.com/hc/article_attachments/4404942486039/chkbox.gif).

## Font

This tab shows the font-related information of the text in the parameter control.

![Parameter Control Properties dialog - Font tab](https://devnet.logianalytics.com/hc/article_attachments/4404936916375/prmctrlprpty_font.gif)

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

## Border

This tab shows information about borders of the parameter control.

![Parameter Control Properties dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4404942584215/prmctrlprpty_border.gif)

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746141-Page-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009719822-Parameter-Field-Properties)
