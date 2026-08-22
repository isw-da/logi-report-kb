---
title: "Filter Control Properties"
id: 4405690580759
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690580759-Filter-Control-Properties
updated_at: 2022-01-27T07:59:16Z
---

# Filter Control Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683816983-Fill-Effects-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683818007-Filter-Dialog-Box-Properties)

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

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4420447202071/btn_help.gif)

Select to view information about the Filter Control Properties dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420447202455/btn_close.gif)

Select to close the dialog box without saving any changes.

## General Tab Properties

This tab shows some general information of the filter control.

![Filter Control Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4420447250071/fltrctrlprpty_gnrl.gif)

**Name**

Specifies the name of the filter control.

**Show NLS Value**

Select to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it, and when you have not modified the display name of the object.

**Format**

Specifies the value format of the field added in the filter control.

**Auto Scale in Number**

Select **true** if you want to automatically scale the values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

The value **auto** means that the setting follows that of the parent data container. When you set the property to **true**, the specified format will apply to the integer part of the values after being scaled. If the specified format conflicts with the Number data type, Logi Report will ignore the **Auto Scale in Number** setting.

**Filter On**

Displays the fields that the filter control is based on. You can select the ellipsis button ![Select Fields](https://devnet.logianalytics.com/hc/article_attachments/4420453393175/btn_chsr2.gif) to open the [Edit Filter Control](https://devnet.logianalytics.com/hc/en-us/articles/4405683811095-Edit-Filter-Control-Dialog-Box-Properties) dialog box.

**Width**

Specifies the width of the filter control.

**Height**

Specifies the height of the filter control.

**Background**

Specifies the background color of the filter control.

To change the color, select the color indicator. Server displays the color palette. Select a color, or select **More Colors** to access the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683802391-Color-Picker-Dialog-Box-Properties) in which you can specify a color within a wider range. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff. If you want to make the background transparent, type **Transparent** in the text box.

**Foreground**

Specifies the foreground color of the filter control.

To change the color, select the color indicator. Server displays the color palette. Select a color, or select **More Colors** to access the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683802391-Color-Picker-Dialog-Box-Properties) in which you can specify a color within a wider range. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff.

**Show Title**

Specifies whether to show the title of the filter control.

## Font Tab Properties

Specify the font properties of the text in the filter control.

![Filter Control Properties dialog - Font tab](https://devnet.logianalytics.com/hc/article_attachments/4420447250327/fltrctrlprpty_font.gif)

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

![Filter Control Properties dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4420461651735/fltrctrlprpty_border.gif)

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

![Filter Control Properties dialog - Title tab](https://devnet.logianalytics.com/hc/article_attachments/4420447250583/fltrctrlprpty_title.gif)

**Text**

Specifies the text of the title.

* **Auto Map Field Name**  
   Specifies whether to automatically map the title text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/4405683929879-Managing-Dynamic-Display-Names-of-Business-View-Elements) of a field bound with the filter control.

**Background**

Specifies the background color of the title.

To change the color, select the color indicator. Server displays the color palette. Select a color, or select **More Colors** to access the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683802391-Color-Picker-Dialog-Box-Properties) in which you can specify a color within a wider range. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff. If you want to make the background transparent, type **Transparent** in the text box.

**Foreground**

Specifies the foreground color of the title.

To change the color, select the color indicator. Server displays the color palette. Select a color, or select **More Colors** to access the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683802391-Color-Picker-Dialog-Box-Properties) in which you can specify a color within a wider range. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff.

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683816983-Fill-Effects-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683818007-Filter-Dialog-Box-Properties)
