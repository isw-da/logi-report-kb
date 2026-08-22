---
title: "Label Properties"
id: 1500009747702
section: "Web Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009747702-Label-Properties
updated_at: 2021-07-24T00:48:17Z
---

# Label Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009776061-KPI-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009776081-Mapping-Table-Dialog-Box-Properties)

# Label Properties

This topic describes how you can use the Label Properties dialog box to update the properties of a label. Server displays the dialog box when you right-click a label and select **Properties** from the shortcut menu.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Font Tab Properties](#Font)
* [Border Tab Properties](#Border)

You see these elements on all the tabs:

**OK**

Select **OK** to apply any changes you made here.

**Cancel**

Select **Cancel** to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Select to view information about the Label Properties dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Select to close the dialog box without saving any changes.

## General Tab Properties

This tab shows some general information of the label.

![Label Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404885453207/lblprpty_gnrl.gif)

**Name**

Specifies the display name of the label.

**Show NLS Value**

Select this option to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it.

If you select this option, it takes effect only when you have not modified the display name of the object.

**Text**

Specifies the text of the label.

**Auto Map Field Name**

Enabled when the label is related to a field. It specifies whether to automatically map the label text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/1500009777181-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the field. If selected, the text specified in the Text text box will be ignored.

**Width**

Specifies the width of the label.

**Height**

Specifies the height of the label.

**Position**

Displays the position mode of the component. If the component is directly contained in the report body, a tabular cell, or a text box, you can modify its position mode.

* **Absolute**  
  Logi Report will decide the component's position by its X and Y property values.
* **Static**  
  Logi Report will position the component at the default location in its container. It will also hide or disable the X, Y, and other position-related properties.

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

To change the color, select the color indicator to select a color from the color palette. You can select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009746842-Color-Picker-Dialog-Box-Properties) dialog box in which you can select a color within a wider range. You can also type a color string in the format #RRGGBB directly in the text box. If you want to make the background transparent, type Transparent in the text box.

**Foreground**

Specifies the foreground color of the label.

To change the color, select the color indicator to select a color from the color palette. You can select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009746842-Color-Picker-Dialog-Box-Properties) dialog box in which you can select a color within a wider range. You can also type a color string in the format #RRGGBB directly in the text box.

## Font Tab Properties

This tab shows the font-related information of the label.

![Label Properties dialog - Font tab](https://devnet.logianalytics.com/hc/article_attachments/4404880352151/lblprpty_font.gif)

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

Specifies whether to attach a strikeout line to the label text.

**Italic**

Specifies whether to make the label text italic or not.

**Autofit**

Specifies whether to automatically adjust the width of the label. If the label is in a table column, the property takes effect only when the option Autofit on the shortcut menu of the column is also set to true.

**Word Wrap**

Specifies whether to wrap the text to the label width.

**Ignore HTML Tag**

By default, Logi Report Engine ignores the HTML tag elements that are included in the label text so they display exactly as what they are in the report. Clear the option if you want Logi Report Engine to transfer the HTML tag elements to the web browser so they are translated into HTML by the web browser. The setting also applies in the HTML output of the report.

## Border Tab Properties

This tab shows information about borders of the label. You can modify all the border settings in this tab.

![Label Properties dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4404885453847/lblprpty_border.gif)

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009776061-KPI-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009776081-Mapping-Table-Dialog-Box-Properties)
