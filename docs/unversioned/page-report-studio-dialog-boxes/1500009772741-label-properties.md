---
title: "Label Properties"
id: 1500009772741
section: "Page Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009772741-Label-Properties
updated_at: 2021-07-24T00:49:08Z
---

# Label Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744782-Insert-Summary-Column-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744802-Multivalue-Container-Properties)

# Label Properties

You can use the Label Properties dialog box to edit the properties of a label. This topic describes the options in the dialog box.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Font Tab Properties](#Font)
* [Border Tab Properties](#Border)
* [Others Tab Properties](#Others)
* [Display Tab Properties](#Render)

**OK**

Applies the settings and closes this dialog box.

**Cancel**

Cancels the settings and closes this dialog box.

**Help**

Displays the help document about this feature.

## General Tab Properties

This tab shows some general information of the label.

![Label Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404885558935/lblprpty_gnrl.gif)

**Name**

Specifies the display name of the label.

**Show NLS Value**

Select this option to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it.

If you select this option, it takes effect only when you have not modified the display name of the object.

**Text**

Specifies the text of the label.

**Auto Map Field Name**

Enabled when the label is related to a field. It specifies whether to automatically map the label text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/1500009777181-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the field. If selected, the text specified in the Text text box will be ignored.

**Position**

Displays the position mode of the component. If the component is directly contained in the report body, a tabular cell, or a text box, you can modify its position mode.

* **Absolute**  
  Logi Report will decide the component's position by its X and Y property values.
* **Static**  
  Logi Report will position the component at the default location in its container. It will also hide or disable the X, Y, and other position-related properties.

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

To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009745022-Select-Color-Dialog-Box-Properties) dialog box and then specify a new color, or type a color string in the format #RRGGBB. If you want to make the background transparent, type Transparent in the text box.

**Foreground**

Specifies the foreground color of the label.

To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009745022-Select-Color-Dialog-Box-Properties) dialog box and then specify a new color, or type a color string in the format #RRGGBB.

## Font Tab Properties

This tab shows the font-related information of the label.

![Label Properties dialog - Font tab](https://devnet.logianalytics.com/hc/article_attachments/4404880495383/lblprpty_font.gif)

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

Specifies whether to automatically adjust the width of the label.

**Word Wrap**

Specifies whether to wrap the text to the label width.

**Ignore HTML Tag**

By default, Logi Report Engine ignores the HTML tag elements that are included in the label text so they display exactly as what they are in the report. Set the option to false if you want Logi Report Engine to transfer the HTML tag elements to the web browser so they are translated into HTML by the web browser. The setting also applies in the HTML output of the report.

## Border Tab Properties

This tab shows information about borders of the label. You can modify all the border settings in this tab.

![Label Properties dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4404880495767/lblprpty_border.gif)

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

## Others Tab Properties

You can use this tab to view and configure some miscellaneous settings.

![Label Properties dialog - Others tab](https://devnet.logianalytics.com/hc/article_attachments/4404885559703/lblprpty_other.gif)

**TOC Anchor**

Specifies whether to add the node that represents the label to the TOC tree in the TOC Browser.

**Suppress When No Records**

Specifies whether to display the label in the report result when no record is returned to its parent data component.

**Export to XLS**

If true, Server will export the component when you save the report result as an XLS file (make sure to check **Data Format** in the Export dialog box).

**Export to CSV**

If true, Server will export the component when you save the report result as a TXT file with Delimited Format selected.

**Logic Column**

Specifies whether to show the label in the next visible table cell in the same row when the column which holds the label is hidden.

## Display Tab Properties

You can use this tab to modify the display type of the label. For more information, see [Data Field Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009744242-Data-Field-Properties#Render).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744782-Insert-Summary-Column-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744802-Multivalue-Container-Properties)
