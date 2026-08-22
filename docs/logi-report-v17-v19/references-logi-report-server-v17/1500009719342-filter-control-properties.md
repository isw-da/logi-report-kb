---
title: "Filter Control Properties"
id: 1500009719342
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009719342-Filter-Control-Properties
updated_at: 2021-07-25T07:20:06Z
---

# Filter Control Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009719322-Filter)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745501-Format-Activity-Gauge)

# Filter Control Properties

The Filter Control Properties dialog box is used to edit the properties of a filter control.

There are the following tabs in this dialog box: [General](#General), [Font](#Font), [Border](#Border) and [Title](#Title).

**OK**

Applies the settings and closes this dialog box.

**Cancel**

Cancels the settings and closes this dialog box.

**Help**

Displays the help document about this feature.

## General

This tab shows some general information of the filter control.

![Filter Control Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404936944663/fltrctrlprpty_gnrl.gif)

**Name**

Specifies the name of the filter control.

**Show NLS Value**

Select this option to show the translated name for the display name of the object in the Name text box if you have enabled the NLS feature and translated it.

If selected, this option takes effect only when the display name of the object is not modified.

**Format**

Specifies the field value format in the filter control.

**Auto Scale in Number**

Specifies whether to
automatically scale the values of the field added in the filter control that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

By default it is set to auto which means that the setting follows that of the filter control's parent data container. When it is true, the specified format applies to the integer part of the values after scaled, but if the specified format conflicts with Auto Scale in Number, for example, the values are displayed in percentage, then the Auto Scale in Number setting is ignored.

**Position**

Displays the position mode of the filter control. If the filter control is directly contained in the report body, a tabular cell, or a text box, its position mode can be modified.

* **Absolute**: The filter control's position will be decided by its X and Y property values.
* **Static**: The filter control will be positioned at the default location in its container. If selected, the X, Y and other position-related properties will be hidden or disabled.

**Filter On**

Displays the fields that the filter control is based on. You can select the button ![Edit Filter Control](https://devnet.logianalytics.com/hc/article_attachments/4404942451479/btn_chsr2.gif) to open the [Edit Filter Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009719262-Edit-Filter-Control) dialog box.

**X**

Specifies the X coordinate of the filter control.

**Y**

Specifies the Y coordinate of the filter control.

**Width**

Specifies the width of the filter control.

**Height**

Specifies the height of the filter control.

**Background**

Specifies the background color of the filter control.

To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009746261-Select-Color) dialog box and then specify a new color, or type a color string in the format #RRGGBB. If you want to make the background transparent, type Transparent in the text box.

**Foreground**

Specifies the foreground color of the filter control.

To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009746261-Select-Color) dialog box and then specify a new color, or type a color string in the format #RRGGBB.

**Show Title**

Specifies whether to show the title of the filter control.

## Font

This tab shows the font-related information of the text in the filter control.

![Filter Control Properties dialog - Font tab](https://devnet.logianalytics.com/hc/article_attachments/4404936944919/fltrctrlprpty_font.gif)

**Font**

Specifies the font face of the text.

**Size**

Specifies the font size of the text.

**Bold**

Specifies whether to make the text bold or not.

**Underline**

Specifies whether the text will be underlined or not.

**Italic**

Specifies whether to make the text italic or not.

## Border

This tab shows information about borders of the filter control.

![Filter Control Properties dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4404936945175/fltrctrlprpty_border.gif)

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

## Title

This tab shows information about the title of the filter control. It is available when the Show Title option is selected in the General tab of the same dialog box.

![Filter Control Properties dialog - Title tab](https://devnet.logianalytics.com/hc/article_attachments/4404942598551/fltrctrlprpty_title.gif)

**Text**

Specifies the text of the title.

* **Auto Map Field Name**  
   Specifies whether to automatically map the title text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/1500009723082-Managing-Dynamic-Display-Names-of-Business-View-Elements) of a field bound with the filter control.

**Background**

Specifies the background color of the title.

To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009746261-Select-Color) dialog box and then specify a new color, or type a color string in the format #RRGGBB. If you want to make the background transparent, type Transparent in the text box.

**Foreground**

Specifies the foreground color of the title.

To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009746261-Select-Color) dialog box and then specify a new color, or type a color string in the format #RRGGBB.

**Font**

Specifies the font face of the text.

**Size**

Specifies the font size of the text.

**Horizontal Alignment**

Specifies the horizontal alignment mode of the text.

**Bold**

Specifies whether to make the text bold or not.

**Underline**

Specifies whether the text will be underlined or not.

**Italic**

Specifies whether to make the text italic or not.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009719322-Filter)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745501-Format-Activity-Gauge)
