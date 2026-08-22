---
title: "Filter Control Properties"
id: 5741402536087
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741402536087-Filter-Control-Properties
updated_at: 2022-10-31T17:16:15Z
---

# Filter Control Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741402520855-Filter-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741424370455-Format-Activity-Gauge-Dialog-Box-Properties)

# Filter Control Properties

You can use the Filter Control Properties dialog box to edit the properties of a filter control. This topic describes the properties in the dialog box.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Font Tab Properties](#Font)
* [Border Tab Properties](#Border)
* [Title Tab Properties](#Title)

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## General Tab Properties

You can specify the general information of the filter control.

![Filter Control Properties dialog box - General tab](https://devnet.logianalytics.com/hc/article_attachments/9905816142615/fltrctrlprpty_gnrl.gif)

**Name**

Specify the name of the filter control.

**Show NLS Value**

Select to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it, and when you have not modified the display name of the object.

**Format**

Specify the field value format in the filter control.

**Auto Scale in Number**

Select **true** if you want to automatically scale the values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

The value **auto** means that the setting follows that of the parent data container. When you set the property to **true**, the specified format will apply to the integer part of the values after being scaled. If the specified format conflicts with the Number data type, Logi Report will ignore the **Auto Scale in Number** setting.

**Position**

Select the position mode of the object when it is directly contained in the report body, a tabular cell, or a text box.

* **Absolute**  
  Select if you want to use the X and Y property values to decide the object's position.
* **Static**  
  Select if you want to place the object at the default location in its container. Server will hide or disable the X, Y, and other position-related properties.

**Filter On**

Server displays the fields that the filter control is based on. You can select the ellipsis button ![Edit Filter Control](https://devnet.logianalytics.com/hc/article_attachments/9905577763991/btn_chsr2.gif) to open the [Edit Filter Control dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741410351255-Edit-Filter-Control-Dialog-Box-Properties).

**X**

Specify the X coordinate of the filter control.

**Y**

Specify the Y coordinate of the filter control.

**Width**

Specify the width of the filter control, in inches.

**Height**

Specify the height of the filter control, in inches.

**Background**

Specify the background color of the filter control.

To change the color, select the color indicator to access the [Select Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741389405847-Select-Color-Dialog-Box-Properties), and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff. If you want to make the background transparent, type **Transparent** in the text box.

**Foreground**

Specify the foreground color of the filter control.

To change the color, select the color indicator to access the [Select Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741389405847-Select-Color-Dialog-Box-Properties), and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff.

**Show Title**

Select to show the title of the filter control.

## Font Tab Properties

Specify the font properties of the text in the filter control.

![Filter Control Properties dialog box - Font tab](https://devnet.logianalytics.com/hc/article_attachments/9905777411479/fltrctrlprpty_font.gif)

**Font**

Select the font face of the text.

**Size**

Specify the font size of the text.

**Bold**

Select **true** to make the text bold.

**Underline**

Select **true** to underline the text.

**Italic**

Select **true** to make the text italic.

## Border Tab Properties

You can specify the border properties of the filter control.

![Filter Control Properties dialog box - Border tab](https://devnet.logianalytics.com/hc/article_attachments/9905816193687/fltrctrlprpty_border.gif)

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

You can specify the title properties of the filter control. This tab is available when you selected **Show Title** on the **General** tab of the dialog box.

![Filter Control Properties dialog box - Title tab](https://devnet.logianalytics.com/hc/article_attachments/9905777469975/fltrctrlprpty_title.gif)

**Text**

Server enables this property when you disable **Auto Map Field Name**. Type the text you want to display as the title.

When you add only one DBField to the text list filter control and insert the On-screen Filter special field in a data container that uses the same data resource as the DBField, Logi Report also applies the text in the filter expression of the special field.

* **Auto Map Field Name**  
   Select to automatically map the title text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/5741468400151-Managing-Dynamic-Display-Names-of-Business-View-Elements) of a field bound with the filter control.

**Background**

Specify the background color of the title.

To change the color, select the color indicator to access the [Select Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741389405847-Select-Color-Dialog-Box-Properties), and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff. If you want to make the background transparent, type **Transparent** in the text box.

**Foreground**

Specify the foreground color of the title.

To change the color, select the color indicator to access the [Select Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741389405847-Select-Color-Dialog-Box-Properties), and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff.

**Font**

Select the font face of the text.

**Size**

Specify the font size of the text.

**Horizontal Alignment**

Select the horizontal alignment mode of the text.

**Title Height**

Specify the height of the title, to ensure larger font sizes display without being cut off. Type a numeric value to change the height.

**Bold**

Select **true** to make the text bold.

**Underline**

Select **true** to underline the text.

**Italic**

Select **true** to make the text italic.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741402520855-Filter-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741424370455-Format-Activity-Gauge-Dialog-Box-Properties)
