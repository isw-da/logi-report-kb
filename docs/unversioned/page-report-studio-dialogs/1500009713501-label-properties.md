---
title: "Label Properties"
id: 1500009713501
section: "Page Report Studio Dialogs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009713501-Label-Properties
updated_at: 2021-11-03T06:58:05Z
---

# Label Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009687642-Insert-Summary-Column)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009687662-Multivalue-Container-Properties)

# Label Properties

The Label Properties dialog helps you to edit the properties of a label. It contains the following tabs: [General](#General), [Font](#Font), [Border](#Border), [Others](#Others) and [Display](#Render).

**OK**

Applies the settings and closes this dialog.

**Cancel**

Cancels the settings and closes this dialog.

**Help**

Displays the help document about this feature.

## General

This tab shows some general information of the label.

![Label Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4412131495319/lblprpty_gnrl.gif)

**Name**

Specifies the display name of the label.

**Show NLS Value**

Specifies to show the translated name for the display name of the label in the Name text box if you have enabled the NLS feature and translated it.

If checked, this option takes effect only when the display name of the label is not modified.

**Text**

Specifies the text of the label.

**Auto Map Field Name**

Enabled when the label is related to a field. It specifies whether to automatically map the label text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/1500009717801-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the field. If selected, the text specified in the Text text box will be ignored.

**Position**

Displays the position mode of the label. If the label is directly contained in the report body, a tabular cell, or a text box, its position mode can be modified.

* **Absolute**: The label's position will be decided by its X and Y property values.
* **Static**: The label will be positioned at the default location in its container. If selected, the X, Y and other position-related properties will be hidden or disabled.

**X**

Specifies the X coordinate of the label.

**Y**

Specifies the Y coordinate of the label.

**Width**

Specifies the width of the label.

**Height**

Specifies the height of the label.

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

To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009713741-Select-Color) dialog and then specify a new color, or input a color string in the format #RRGGBB. If you want to make the background transparent, input Transparent in the text box.

**Foreground**

Specifies the foreground color of the label.

To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009713741-Select-Color) dialog and then specify a new color, or input a color string in the format #RRGGBB.

## Font

This tab shows the font-related information of the label.

![Label Properties dialog - Font tab](https://devnet.logianalytics.com/hc/article_attachments/4412131495575/lblprpty_font.gif)

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

Specifies whether or not to automatically adjust the width of the label.

**Word Wrap**

Specifies whether or not to wrap the text to the label width.

**Ignore HTML Tag**

If this option is unchecked, Logi JReport will parse HTML tag elements in the field value while the report is to be saved as an HTML file; or the field value will appear in the HTML file the same as that in Page Report Studio (HTML tag elements in the field value, if any, will not be parsed).

## Border

This tab shows information about borders of the label. You can modify all the border settings in this tab.

![Label Properties dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4412131495831/lblprpty_border.gif)

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

Specifies whether the borders will have a shadow effect or not.

**Shadow Color**

Specifies the color of the border shadow.

## Others

You can use this tab to view and configure some miscellaneous settings.

![Label Properties dialog - Others tab](https://devnet.logianalytics.com/hc/article_attachments/4412139580823/lblprpty_other.gif)

**TOC Anchor**

Specifies whether or not to add the node that represents the label to the TOC tree that is displayed in the TOC Browser.

**Suppress When No Records**

Specifies whether to display the label in the report result when no record is returned to its parent data component.

**Export to XLS**

If true, the label will be exported when you save the report result as an XLS file (make sure to check Data Format in the Export dialog).

**Export to CSV**

If true, the label will be exported when you save the report result as a TXT file with Delimited Format selected.

**Logic Column**

Specifies whether to show the label in the next visible table cell in the same row when the column which holds the label is hidden.

## Display

You can use this tab to modify the display type of the label. For details about the display types, see [Data Field Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009687162-Data-Field-Properties#Render).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009687642-Insert-Summary-Column)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009687662-Multivalue-Container-Properties)
