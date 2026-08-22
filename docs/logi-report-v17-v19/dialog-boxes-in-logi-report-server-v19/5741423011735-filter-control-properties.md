---
title: "Filter Control Properties"
id: 5741423011735
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741423011735-Filter-Control-Properties
updated_at: 2022-10-31T17:17:21Z
---

# Filter Control Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741444679959-Fill-Effects-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741449994391-Filter-Dialog-Box-Properties)

# Filter Control Properties

This topic describes how you can use the Filter Control Properties dialog box to edit the properties of a filter control. Server displays the dialog box when you right-click a filter control and select **Properties** from the shortcut menu.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Font Tab Properties](#Font)
* [Border Tab Properties](#Border)
* [Title Tab Properties](#Title)

You see these elements on all the tabs:

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

## General Tab Properties

Specify the general properties of the filter control.

![Filter Control Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/9905733467287/fltrctrlprpty_gnrl.gif)

**Name**

Specify the name of the filter control.

**Show NLS Value**

Select to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it, and when you have not modified the display name of the object.

**Format**

Specify the value format of the field that you added in the filter control.

**Auto Scale in Number**

Select **true** if you want to automatically scale the values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

The value **auto** means that the setting follows that of the parent data container. When you set the property to **true**, the specified format will apply to the integer part of the values after being scaled. If the specified format conflicts with the Number data type, Logi Report will ignore the **Auto Scale in Number** setting.

**Filter On**

Server displays the fields that the filter control is based on. You can select the ellipsis button ![Select Fields](https://devnet.logianalytics.com/hc/article_attachments/9905577763991/btn_chsr2.gif) to open the [Edit Filter Control dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741444498967-Edit-Filter-Control-Dialog-Box-Properties).

**Width**

Specify the width of the filter control.

**Height**

Specify the height of the filter control.

**Background**

Specify the background color of the filter control.

To change the color, select the color indicator. Server displays the color palette. Select a color, or select **More Colors** to access the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428592023-Color-Picker-Dialog-Box-Properties) in which you can specify a color within a wider range. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff. If you want to make the background transparent, type **Transparent** in the text box.

**Foreground**

Specify the foreground color of the filter control.

**Show Title**

Clear if you want to hide the title of the filter control.

## Font Tab Properties

Specify the font properties of the text in the filter control.

![Filter Control Properties dialog - Font tab](https://devnet.logianalytics.com/hc/article_attachments/9905755292823/fltrctrlprpty_font.gif)

**Font**

Specify the font face of the text.

**Size**

Specify the font size of the text.

**Bold**

Select if you want to make the text bold.

**Underline**

Select if you want to underline the text.

**Italic**

Select if you want to make the text italic.

## Border Tab Properties

Specify the border properties of the filter control.

![Filter Control Properties dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/9905733521815/fltrctrlprpty_border.gif)

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

## Title Tab Properties

Specify the title properties of the filter control. This tab is available when **Show Title** is selected in the General tab of the dialog box.

![Filter Control Properties dialog - Title tab](https://devnet.logianalytics.com/hc/article_attachments/9905755352599/fltrctrlprpty_title.gif)

**Text**

Server enables this property when you clear **Auto Map Field Name**. Type the text you want to display as the title.

When you add only one DBField to the text list filter control and insert the On-screen Filter special field in a data container that uses the same data resource as the DBField, Logi Report also applies the text in the filter expression of the special field.

* **Auto Map Field Name**  
   Select if you want to automatically map the title text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/5741468400151-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the field bound with the filter control.

**Background**

Specify the background color of the title.

To change the color, select the color indicator. Server displays the color palette. Select a color, or select **More Colors** to access the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428592023-Color-Picker-Dialog-Box-Properties) in which you can specify a color within a wider range. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff. If you want to make the background transparent, type **Transparent** in the text box.

**Foreground**

Specify the foreground color of the title.

**Font**

Specify the font face of the text.

**Size**

Specify the font size of the text.

**Horizontal Alignment**

Specify the horizontal alignment mode of the text.

**Title Height**

Specify the height of the title, to ensure larger font sizes display without being cut off. Type a numeric value to change the height.

**Bold**

Select if you want to make the text bold.

**Underline**

Select if you want to underline the text.

**Italic**

Select if you want to make the text italic.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741444679959-Fill-Effects-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741449994391-Filter-Dialog-Box-Properties)
