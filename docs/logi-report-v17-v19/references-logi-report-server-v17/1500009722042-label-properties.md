---
title: "Label Properties"
id: 1500009722042
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009722042-Label-Properties
updated_at: 2021-07-25T07:19:15Z
---

# Label Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009722022-KPI-Properties)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009749141-Mapping-Table)

# Label Properties

The Label Properties dialog box is used to specify the properties of a label. It appears when you right-click a label and select Properties from the shortcut menu.

There are the following tabs in this dialog box: [General](#General), [Font](#Font) and [Border](#Border).

**OK**

Applies the settings and closes this dialog box.

**Cancel**

Cancels the settings and closes this dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404936816535/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404942519575/btn_close.gif)

Ignores the setting and closes this dialog box.

## General

This tab shows some general information of the label.

![Label Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404942530455/lblprpty_gnrl.gif)

**Name**

Specifies the display name of the label.

**Show NLS Value**

Select this option to show the translated name for the display name of the object in the Name text box if you have enabled the NLS feature and translated it.

If selected, this option takes effect only when the display name of the object is not modified.

**Text**

Specifies the text of the label.

**Auto Map Field Name**

Enabled when the label is related to a field. It specifies whether to automatically map the label text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/1500009723082-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the field. If selected, the text specified in the Text text box will be ignored.

**Width**

Specifies the width of the label.

**Height**

Specifies the height of the label.

**Position**

Displays the position mode of the label. If the label is directly contained in the report body, a tabular cell, or a text box, its position mode can be modified.

* **Absolute**: The label's position will be decided by its X and Y property values.
* **Static**: The label will be positioned at the default location in its container. If selected, the X, Y and other position-related properties will be hidden or disabled.

**Top Padding**

Specifies the space between the text of the label and its top border.

**Bottom Padding**

Specifies the space between the text of the label and its bottom border.

**Left Padding**

Specifies the space between the text of the label and its left border.

**Right Padding**

Specifies the space between the text of the label and its right border.

**Background**

Specifies the background color of the label.

To change the color, select the color indicator to select a color from the color palette. You can select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009721402-Color-Picker-) dialog box in which you can select a color within a wider range. You can also type a color string in the format #RRGGBB directly in the text box. If you want to make the background transparent, type Transparent in the text box.

**Foreground**

Specifies the foreground color of the label.

To change the color, select the color indicator to select a color from the color palette. You can select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009721402-Color-Picker-) dialog box in which you can select a color within a wider range. You can also type a color string in the format #RRGGBB directly in the text box.

## Font

This tab shows the font-related information of the label.

![Label Properties dialog - Font tab](https://devnet.logianalytics.com/hc/article_attachments/4404942530711/lblprpty_font.gif)

**Font**

Specifies the font face of the label text.

**Size**

Specifies the font size of the label text.

**Horizontal Alignment**

Specifies the horizontal alignment mode of the text in the label.

**Vertical Alignment**

Specifies the vertical alignment mode of the text in the label.

**Bold**

Specifies whether to make the label text bold or not.

**Underline**

Specifies whether the label text will be underlined or not.

**Strikethrough**

Specifies whether or not to attach a strikeout line to the label text.

**Italic**

Specifies whether to make the label text italic or not.

**Autofit**

Specifies whether or not to automatically adjust the width of the label. If the label is in a table column, the property takes effect only when the optin Autofit on the shortcut menu of the column is also set to true.

**Word Wrap**

Specifies whether or not to wrap the text to the label width.

**Ignore HTML Tag**

If this option is unselected, Logi Report will parse HTML tag elements in the field value while the report is to be saved as an HTML file; or the field value will appear in the HTML file the same as that in Web Report Studio (HTML tag elements in the field value, if any, will not be parsed).

## Border

This tab shows information about borders of the label. You can modify all the border settings in this tab.

![Label Properties dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4404936833943/lblprpty_border.gif)

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

**Shadow**

Specifies whether the borders will have a shadow effect or not. This property cannot be rendered in Web Report Studio or JDashboard.

**Shadow Color**

Specifies the color of the border shadow. This property cannot be rendered in Web Report Studio or JDashboard.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009722022-KPI-Properties)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009749141-Mapping-Table)
