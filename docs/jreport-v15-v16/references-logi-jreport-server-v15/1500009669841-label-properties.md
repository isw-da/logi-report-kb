---
title: "Label Properties"
id: 1500009669841
section: "References Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009669841-Label-Properties
updated_at: 2021-07-24T20:55:07Z
---

# Label Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009645382-Insert-Summary-Column)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009645402-Multivalue-Container-Properties)

# Label Properties

The Label Properties dialog helps you to edit the properties of a label. It contains the following tabs:

* [General](#General)
* [Font](#Font)
* [Border](#Border)
* [Others](#Others)
* [Display](#Render)

**OK**

Applies the settings and closes this dialog.

**Cancel**

Cancels the settings and closes this dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## General

This tab shows some general information of the label. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920622359/lblprpty_gnrl.gif)

**Name**

Specifies the display name of the label, which will be shown on the shortcut menu of the label.

**Show NLS Value**

Specifies to show the translated name of the display name of the label in the Name text box if you have enabled the NLS feature and translated it.

If checked, this option takes effect only when the display name of the label is not modified.

**Text**

Specifies the text of the label.

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

To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009645662-Select-Color) dialog and then specify a new color, or input a color string in the format #RRGGBB. If you want to make the background transparent, input Transparent in the text box.

**Foreground**

Specifies the foreground color of the label.

To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009645662-Select-Color) dialog and then specify a new color, or input a color string in the format #RRGGBB.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Font

This tab shows the font-related information of the label. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920622615/lblprpty_font.gif)

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

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Border

This tab shows information about borders of the label. You can modify all the border settings in this tab. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920622871/lblprpty_border.gif)

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

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Others

You can use this tab to view and configure some miscellaneous settings. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920623127/lblprpty_other.gif)

**TOC Anchor**

Specifies whether or not to add the node that represents the label to the TOC tree that is displayed in the TOC Browser.

**Suppress When No Records**

If true and no records are returned by the report, the label will not be displayed.

**Export to XLS**

If true, the label will be exported when you save the report result as an XLS file (make sure to check Data Format in the Export dialog).

**Export to CSV**

If true, the label will be exported when you save the report result as a TXT file with Delimited Format selected.

**Logic Column**

Specifies whether to show the label in the next visible table cell in the same row when the column which holds the label is hidden.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Display

You can use this tab to modify the display type of the label. For details about the display types, see [Data Field Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009645022-Data-Field-Properties#Render).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009645382-Insert-Summary-Column)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009645402-Multivalue-Container-Properties)
