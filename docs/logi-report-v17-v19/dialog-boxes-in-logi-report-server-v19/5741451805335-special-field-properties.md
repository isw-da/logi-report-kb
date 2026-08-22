---
title: "Special Field Properties"
id: 5741451805335
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741451805335-Special-Field-Properties
updated_at: 2022-10-31T17:17:46Z
---

# Special Field Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9305227644055/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741446516119-Share-Report-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9305200977175/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741436725911-Split-Cell-Dialog-Box-Properties)

# Special Field Properties

This topic describes how you can use the Special Field Properties dialog box to update the properties of a special field. Server displays the dialog box when you right-click a special field and select **Properties** from the shortcut menu.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Font Tab Properties](#Font)
* [Border Tab Properties](#Border)

You see these elements on all the tabs:

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9305243196567/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9305213813271/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

## General Tab Properties

Specify the general properties of the special field.

![Special Field Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/9305429842839/spcprpty_gnrl.gif)

**Name**

Specify the display name of the object.

**Show NLS Value**

Select to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it, and when you have not modified the display name of the object.

**Width**

Specify the width of the object.

**Height**

Specify the height of the object.

**Type**

Specify the [type](https://devnet.logianalytics.com/hc/en-us/articles/5741484470039-Components-Supported-in-Web-Reports#SpecialField) of the special field. Select a new one from the drop-down list if you want to change the type.

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

To change the color, select the color indicator. Server displays the color palette. Select a color, or select **More Colors** to access the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428592023-Color-Picker-Dialog-Box-Properties) in which you can specify a color within a wider range.

**Foreground**

Specify the foreground color of the object.

To change the color, select the color indicator. Server displays the color palette. Select a color, or select **More Colors** to access the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428592023-Color-Picker-Dialog-Box-Properties) in which you can specify a color within a wider range.

## Font Tab Properties

Specify the font properties of the special field.

![Special Field Properties dialog - Font tab](https://devnet.logianalytics.com/hc/article_attachments/9305419485335/spcprpty_font.gif)

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

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9305196643607/noteicon.jpg) This property takes effect when you set Position of the object to absolute; but, it does not work if the Word Wrap property of the object is true.

**Word Wrap**

Enable this property if you want to wrap the text to the object width.

**Ignore HTML Tag**

Enable this property if you don't want Logi Report Engine to parse the HTML tag elements in the text, at runtime or in the HTML output, so they display exactly as what they are in the report.

Disable this property if you want Engine to transfer the HTML tag elements to the web browser so the web browser translates them into HTML.

## Border Tab Properties

Specify the border properties of the special field.

![Special Field Properties dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/9305446061719/spcprpty_border.gif)

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

**Shadow**

Select if you want to add a shadow effect to the border. Web Report Studio and JDashboard cannot render the shadow effect.

**Shadow Color**

Specify the color of the border shadow.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9305227644055/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741446516119-Share-Report-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9305200977175/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741436725911-Split-Cell-Dialog-Box-Properties)
