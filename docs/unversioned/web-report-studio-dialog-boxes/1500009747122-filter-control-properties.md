---
title: "Filter Control Properties"
id: 1500009747122
section: "Web Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009747122-Filter-Control-Properties
updated_at: 2021-07-24T00:48:27Z
---

# Filter Control Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009747082-Fill-Effects-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009775301-Filter-Dialog-Box-Properties)

# Filter Control Properties

This topic describes how you can use the Filter Control Properties dialog box to edit the properties of a filter control. Server displays the dialog box when you right-click a filter control and select **Properties** from the shortcut menu.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Font Tab Properties](#Font)
* [Border Tab Properties](#Border)
* [Title Tab Properties](#Title)

You see these elements on all the tabs:

**OK**

Select **OK** to apply any changes you made here.

**Cancel**

Select **Cancel** to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Select to view information about the Filter Control Properties dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Select to close the dialog box without saving any changes.

## General Tab Properties

This tab shows some general information of the filter control.

![Filter Control Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404880390935/fltrctrlprpty_gnrl.gif)

**Name**

Specifies the name of the filter control.

**Show NLS Value**

Select this option to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it.

If you select this option, it takes effect only when you have not modified the display name of the object.

**Format**

Specifies the value format of the field added in the filter control.

**Auto Scale in Number**

Specifies whether to
automatically scale the values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

The value **auto** means that the setting follows that of the parent data container. When you set the property to **true**, the specified format will apply to the integer part of the values after being scaled; but if the specified format conflicts with the Number data type, Logi Report will ignore the Auto Scale in Number setting.

**Filter On**

Displays the fields that the filter control is based on. You can select the button ![Select Fields](https://devnet.logianalytics.com/hc/article_attachments/4404880145687/btn_chsr2.gif) to open the [Edit Filter Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009775141-Edit-Filter-Control-Dialog-Box-Properties) dialog box.

**Width**

Specifies the width of the filter control.

**Height**

Specifies the height of the filter control.

**Background**

Specifies the background color of the filter control.

To change the color, select the color indicator to select a color from the color palette. You can select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009746842-Color-Picker-Dialog-Box-Properties) dialog box in which you can select a color within a wider range. You can also type a color string in the format #RRGGBB directly in the text box. If you want to make the background transparent, type Transparent in the text box.

**Foreground**

Specifies the foreground color of the filter control.

To change the color, select the color indicator to select a color from the color palette. You can select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009746842-Color-Picker-Dialog-Box-Properties) dialog box in which you can select a color within a wider range. You can also type a color string in the format #RRGGBB directly in the text box.

**Show Title**

Specifies whether to show the title of the filter control.

## Font Tab Properties

This tab shows the font-related information of the text in the filter control.

![Filter Control Properties dialog - Font tab](https://devnet.logianalytics.com/hc/article_attachments/4404880391191/fltrctrlprpty_font.gif)

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

![Filter Control Properties dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4404880391447/fltrctrlprpty_border.gif)

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

![Filter Control Properties dialog - Title tab](https://devnet.logianalytics.com/hc/article_attachments/4404880391703/fltrctrlprpty_title.gif)

**Text**

Specifies the text of the title.

* **Auto Map Field Name**  
   Specifies whether to automatically map the title text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/1500009777181-Managing-Dynamic-Display-Names-of-Business-View-Elements) of a field bound with the filter control.

**Background**

Specifies the background color of the title.

To change the color, select the color indicator to select a color from the color palette. You can select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009746842-Color-Picker-Dialog-Box-Properties) dialog box in which you can select a color within a wider range. You can also type a color string in the format #RRGGBB directly in the text box. If you want to make the background transparent, type Transparent in the text box.

**Foreground**

Specifies the foreground color of the title.

To change the color, select the color indicator to select a color from the color palette. You can select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009746842-Color-Picker-Dialog-Box-Properties) dialog box in which you can select a color within a wider range. You can also type a color string in the format #RRGGBB directly in the text box.

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009747082-Fill-Effects-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009775301-Filter-Dialog-Box-Properties)
