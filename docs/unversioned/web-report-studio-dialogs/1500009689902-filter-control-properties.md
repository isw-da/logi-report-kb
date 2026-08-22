---
title: "Filter Control Properties"
id: 1500009689902
section: "Web Report Studio Dialogs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009689902-Filter-Control-Properties
updated_at: 2021-11-03T06:57:23Z
---

# Filter Control Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009716141-Fill-Effects)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009689882-Filter)

# Filter Control Properties

The Filter Control Properties dialog helps you to edit the properties of the filter control and contains the following tabs: [General](#General), [Font](#Font), [Border](#Border) and [Title](#Title). This dialog appears when you right-click a filter control and select Properties from the shortcut menu.

**OK**

Applies the settings and closes this dialog.

**Cancel**

Cancels the settings and closes this dialog.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4412139537431/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4412112572951/btn_close.gif)

Ignores the setting and closes this dialog.

## General

This tab shows some general information of the filter control.

![Filter Control Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4412139556503/fltrctrlprpty_gnrl.gif)

**Name**

Specifies the name of the filter control.

**Show NLS Value**

Specifies to show the translated name for the display name of the filter control in the Name text box if you have enabled the NLS feature and translated it.

If checked, this option takes effect only when the display name of the filter control is not modified.

**Format**

Specifies the value format of the field added in the filter control.

**Auto Scale in Number**

Specifies whether to
automatically scale the values of the field added in the filter control that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

By default it is set to auto which means that the setting follows that of the filter control's parent data container. When it is true, the specified format applies to the integer part of the values after scaled, but if the specified format conflicts with Auto Scale in Number, for example, the values are displayed in percentage, then the Auto Scale in Number setting is ignored.

**Filter On**

Displays the fields that the filter control is based on. You can select the button ![Select Fields](https://devnet.logianalytics.com/hc/article_attachments/4412139488919/btn_chsr2.gif) to open the [Edit Filter Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009715981-Edit-Filter-Control) dialog.

**Width**

Specifies the width of the filter control.

**Height**

Specifies the height of the filter control.

**Background**

Specifies the background color of the filter control.

To change the color, select the color indicator to select a color from the color palette. You can select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009715801-Color-Picker-) dialog in which you can select a color within a wider range. You can also input a color string in the format #RRGGBB directly in the text box. If you want to make the background transparent, input Transparent in the text box.

**Foreground**

Specifies the foreground color of the filter control.

To change the color, select the color indicator to select a color from the color palette. You can select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009715801-Color-Picker-) dialog in which you can select a color within a wider range. You can also input a color string in the format #RRGGBB directly in the text box.

**Show Title**

Specifies whether to show the title of the filter control.

## Font

This tab shows the font-related information of the text in the filter control.

![Filter Control Properties dialog - Font tab](https://devnet.logianalytics.com/hc/article_attachments/4412131452183/fltrctrlprpty_font.gif)

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

![Filter Control Properties dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4412139556887/fltrctrlprpty_border.gif)

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

This tab shows information about the title of the filter control. It is available when the Show Title option is selected in the General tab of the same dialog.

![Filter Control Properties dialog - Title tab](https://devnet.logianalytics.com/hc/article_attachments/4412139557143/fltrctrlprpty_title.gif)

**Text**

Specifies the text of the title.

* **Auto Map Field Name**  
   Specifies whether to automatically map the title text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/1500009717801-Managing-Dynamic-Display-Names-of-Business-View-Elements) of a field bound with the filter control.

**Background**

Specifies the background color of the title.

To change the color, select the color indicator to select a color from the color palette. You can select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009715801-Color-Picker-) dialog in which you can select a color within a wider range. You can also input a color string in the format #RRGGBB directly in the text box. If you want to make the background transparent, input Transparent in the text box.

**Foreground**

Specifies the foreground color of the title.

To change the color, select the color indicator to select a color from the color palette. You can select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009715801-Color-Picker-) dialog in which you can select a color within a wider range. You can also input a color string in the format #RRGGBB directly in the text box.

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009716141-Fill-Effects)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009689882-Filter)
