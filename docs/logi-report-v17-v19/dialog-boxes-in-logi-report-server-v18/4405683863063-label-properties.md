---
title: "Label Properties"
id: 4405683863063
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683863063-Label-Properties
updated_at: 2022-01-27T07:59:23Z
---

# Label Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690596631-KPI-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690597527-Mapping-Table-Dialog-Box-Properties)

# Label Properties

This topic describes how you can use the Label Properties dialog box to update the properties of a label. Server displays the dialog box when you right-click a label and select **Properties** from the shortcut menu.

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

Specify the general properties of the label.

![Label Properties dialog box - General tab](https://devnet.logianalytics.com/hc/article_attachments/4420447213207/lblprpty_gnrl.gif)

**Name**

Specify the display name of the label.

**Show NLS Value**

Select to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it, and when you have not modified the display name of the object.

**Text**

Specify the text of the label.

**Auto Map Field Name**

Available when the label is related to a field. By default, this property is selected. Server automatically maps the label text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/4405683929879-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the field and ignores the text you specified in the Text box.

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

## Font Tab Properties

Specify the font properties of the label.

![Label Properties dialog - Font tab](https://devnet.logianalytics.com/hc/article_attachments/4420461631511/lblprpty_font.gif)

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

Specify the border properties of the label.

![Label Properties dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4420461631895/lblprpty_border.gif)

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690596631-KPI-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690597527-Mapping-Table-Dialog-Box-Properties)
