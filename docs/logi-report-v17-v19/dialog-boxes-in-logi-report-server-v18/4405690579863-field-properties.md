---
title: "Field Properties"
id: 4405690579863
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690579863-Field-Properties
updated_at: 2022-01-27T07:59:16Z
---

# Field Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690589847-Fetch-Data-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683816983-Fill-Effects-Dialog-Box-Properties)

# Field Properties

This topic describes how you can use the Field Properties dialog box to update the properties of a field. Server displays the dialog box when you right-click a field and select **Properties** from the shortcut menu.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Font Tab Properties](#Font)
* [Border Tab Properties](#Border)

You see these elements on all the tabs:

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4420447202071/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420447202455/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

## General Tab Properties

Specify the general properties of the field.

![Field Properties dialog box - General tab](https://devnet.logianalytics.com/hc/article_attachments/4420461653655/dbprpty_gnrl.gif)

**Name**

Specify the display name of the field.

**Show NLS Value**

Select to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it, and when you have not modified the display name of the object.

**Format**

Specify the format of the field.

**Auto Scale in Number**

Select **true** if you want to automatically scale the values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

The value **auto** means that the setting follows that of the parent data container. When you set the property to **true**, the specified format will apply to the integer part of the values after being scaled. If the specified format conflicts with the Number data type, Logi Report will ignore the **Auto Scale in Number** setting.

**Width**

Specify the width of the object.

**Height**

Specify the height of the object.

**Position**

Select the position mode of the object when it is directly contained in the report body, a tabular cell, or a text box.

* **Absolute**  
  Select if you want to use the X and Y property values to decide the object's position.
* **Static**  
  Select if you want to place the object at the default location in its container. Server will hide or disable the X, Y, and other position-related properties.

**Top Padding**

Specify the space between the text of the object and its top border.

**Bottom Padding**

Specify the space between the text of the object and its bottom border.

**Left Padding**

Specify the space between the text of the object and its left border.

**Right Padding**

Specify the space between the text of the object and its right border.

**Background**

Specify the background color of the object.

To change the color, select the color indicator. Server displays the color palette. Select a color, or select **More Colors** to access the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683802391-Color-Picker-Dialog-Box-Properties) in which you can specify a color within a wider range. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff. If you want to make the background transparent, type **Transparent** in the text box.

**Foreground**

Specify the foreground color of the object.

To change the color, select the color indicator. Server displays the color palette. Select a color, or select **More Colors** to access the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683802391-Color-Picker-Dialog-Box-Properties) in which you can specify a color within a wider range. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff.

The following four options are available when the field contains image data, for example, a DBField with image as the data, or a formula field with the expression `openBinFile()` or `openBinURL()`. You can choose to use the original size of the image or customize the size by yourself.

**Original Size**

Server adopts the original size of the image by default. Clear this property if you want to scale the image, then specify the scaling mode.

**Scaling Mode**

Server enables this property when you clear **Original Size**.

* **actual size**  
  Select to show the image in its actual size. If the display area is smaller than the image, Server hides part of the image.
* **fit image**Select if you want the image to fill the display area and keep the original perspective ratio under the limitation of Max Ratio.
* **fit width**Select if you want the image to fit the display area width under the limitation of Max Ratio.
* **fit height**Select if you want the image to fit the display area height, under the limitation of Max Ratio.
* **customize**Select if you want to specify the width and height of the image in the size fields.

**Image Height**

Specify the height of the area for displaying the image. This property is available when you clear **Original Size**.

**Image Width**

Specify the width of the area for displaying the image. This property is available when you clear **Original Size**.

## Font Tab Properties

Specify the font properties of the field.

![Field Properties dialog box - Font tab](https://devnet.logianalytics.com/hc/article_attachments/4420461653911/dbprpty_font.gif)

**Font**

Select the font face of the text.

**Size**

Specify the font size of the text.

**Horizontal Alignment**

Select the horizontal alignment mode of the text in the object.

**Vertical Alignment**

Select the vertical alignment mode of the text in the object.

**Bold**

Enable this property if you want to make the text bold.

**Italic**

Enable this property if you want to make the text italic.

**Underline**

Enable this property if you want to underline the text.

**Strikethrough**

Enable this property if you want to attach a strikeout line to the text.

**Autofit**

Enable this property if you want to automatically expand the object width according to the maximum length of the contents.

**Reduce Width When Autofit**

Enable this property if you want to reduce the width of the object according to its content when you specify to automatically adjust its width (the object's Autofit being true) and the actual width of the content is smaller than that of the object.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg) This property takes effect when you set Position of the object to absolute; but, it does not work if the Word Wrap property of the object is true.

**Word Wrap**

Enable this property if you want to wrap the text to the object width.

**Ignore HTML Tag**

Enable this property if you don't want Logi Report Engine to parse the HTML tag elements in the text, at runtime or in the HTML output, so they display exactly as what they are in the report.

Disable this property if you want Engine to transfer the HTML tag elements to the web browser so the web browser translates them into HTML.

## Border Tab Properties

Specify the border properties of the field.

![Field Properties dialog box - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4420453584407/dbprpty_border.gif)

**Color**

Specify the border color.

**Width**

Specify the border width.

**Top Line**

Select the style of the top border line.

**Bottom Line**

Select the style of the bottom border line.

**Left Line**

Select the style of the left border line.

**Right Line**

Select the style of the right border line.

**Shadow**

Select if you want to add a shadow effect to the border. Web Report Studio and JDashboard cannot render the shadow effect.

**Shadow Color**

Specify the color of the border shadow.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690589847-Fetch-Data-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683816983-Fill-Effects-Dialog-Box-Properties)
