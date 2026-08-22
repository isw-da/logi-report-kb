---
title: "Filter Control Properties"
id: 1500009744322
section: "Page Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009744322-Filter-Control-Properties
updated_at: 2021-07-24T00:49:17Z
---

# Filter Control Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744302-Filter-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744342-Format-Activity-Gauge-Dialog-Box-Properties)

# Filter Control Properties

You can use the Filter Control Properties dialog box to edit the properties of a filter control. This topic describes the options in the dialog box.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Font Tab Properties](#Font)
* [Border Tab Properties](#Border)
* [Title Tab Properties](#Title)

**OK**

Applies the settings and closes this dialog box.

**Cancel**

Cancels the settings and closes this dialog box.

**Help**

Displays the help document about this feature.

## General Tab Properties

This tab shows general information of the filter control.

![Filter Control Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404880538519/fltrctrlprpty_gnrl.gif)

**Name**

Specifies the name of the filter control.

**Show NLS Value**

Select this option to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it.

If you select this option, it takes effect only when you have not modified the display name of the object.

**Format**

Specifies the field value format in the filter control.

**Auto Scale in Number**

Specifies whether to
automatically scale the values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

The value **auto** means that the setting follows that of the parent data container. When you set the property to **true**, the specified format will apply to the integer part of the values after being scaled; but if the specified format conflicts with the Number data type, Logi Report will ignore the Auto Scale in Number setting.

**Position**

Displays the position mode of the component. If the component is directly contained in the report body, a tabular cell, or a text box, you can modify its position mode.

* **Absolute**  
  Logi Report will decide the component's position by its X and Y property values.
* **Static**  
  Logi Report will position the component at the default location in its container. It will also hide or disable the X, Y, and other position-related properties.

**Filter On**

Displays the fields that the filter control is based on. You can select the button ![Edit Filter Control](https://devnet.logianalytics.com/hc/article_attachments/4404880145687/btn_chsr2.gif) to open the [Edit Filter Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009744262-Edit-Filter-Control-Dialog-Box-Properties) dialog box.

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

To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009745022-Select-Color-Dialog-Box-Properties) dialog box and then specify a new color, or type a color string in the format #RRGGBB. If you want to make the background transparent, type Transparent in the text box.

**Foreground**

Specifies the foreground color of the filter control.

To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009745022-Select-Color-Dialog-Box-Properties) dialog box and then specify a new color, or type a color string in the format #RRGGBB.

**Show Title**

Specifies whether to show the title of the filter control.

## Font Tab Properties

This tab shows the font-related information of the text in the filter control.

![Filter Control Properties dialog - Font tab](https://devnet.logianalytics.com/hc/article_attachments/4404880539031/fltrctrlprpty_font.gif)

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

## Border Tab Properties

This tab shows information about borders of the filter control.

![Filter Control Properties dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4404880539415/fltrctrlprpty_border.gif)

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

## Title Tab Properties

This tab shows information about the title of the filter control. It is available when the Show Title option is selected in the General tab of the same dialog box.

![Filter Control Properties dialog - Title tab](https://devnet.logianalytics.com/hc/article_attachments/4404880539671/fltrctrlprpty_title.gif)

**Text**

Specifies the text of the title.

* **Auto Map Field Name**  
   Specifies whether to automatically map the title text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/1500009777181-Managing-Dynamic-Display-Names-of-Business-View-Elements) of a field bound with the filter control.

**Background**

Specifies the background color of the title.

To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009745022-Select-Color-Dialog-Box-Properties) dialog box and then specify a new color, or type a color string in the format #RRGGBB. If you want to make the background transparent, type Transparent in the text box.

**Foreground**

Specifies the foreground color of the title.

To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009745022-Select-Color-Dialog-Box-Properties) dialog box and then specify a new color, or type a color string in the format #RRGGBB.

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744302-Filter-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744342-Format-Activity-Gauge-Dialog-Box-Properties)
