---
title: "Special Field Properties"
id: 1500009773081
section: "Page Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009773081-Special-Field-Properties
updated_at: 2021-07-24T00:49:03Z
---

# Special Field Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009773061-Sort-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745102-Split-Dialog-Box-Properties)

# Special Field Properties

You can use the Special Field Properties dialog box to edit the properties of a special field. This topic describes the options in the dialog box.

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

This tab shows some general information of the special field.

![Special Field Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404880481047/spcprpty_gnrl.gif)

**Name**

Specifies the display name of the special field.

**Show NLS Value**

Select this option to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it.

If you select this option, it takes effect only when you have not modified the display name of the object.

**Type**

Specifies the type of the special field. Select a new one from the drop-down list if you want to change the type.

**Position**

Displays the position mode of the component. If the component is directly contained in the report body, a tabular cell, or a text box, you can modify its position mode.

* **Absolute**  
  Logi Report will decide the component's position by its X and Y property values.
* **Static**  
  Logi Report will position the component at the default location in its container. It will also hide or disable the X, Y, and other position-related properties.

**X**

Specifies the X coordinate of the special field.

**Y**

Specifies the Y coordinate of the special field.

**Width**

Specifies the width of the special field.

**Height**

Specifies the height of the special field.

**Background**

Specifies the background color of the special field.

To change the color, select the color indicator to bring out the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009745022-Select-Color-Dialog-Box-Properties) dialog box and then specify a new color, or type a color string in the format #RRGGBB. If you want to make the background transparent, type Transparent in the text box.

**Foreground**

Specifies the foreground color of the special field.

To change the color, select the color indicator to bring out the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009745022-Select-Color-Dialog-Box-Properties) dialog box and then specify a new color, or type a color string in the text box.

## Font Tab Properties

This tab shows the font-related information of the special field. You can modify all the font settings in this tab.

![Special Field Properties dialog - Font tab](https://devnet.logianalytics.com/hc/article_attachments/4404880481559/spcprpty_font.gif)

**Font**

Specifies the font face of the field text.

**Size**

Specifies the font size of the field text.

**Horizontal Alignment**

Specifies the horizontal alignment mode of the text in the special field.

**Vertical Alignment**

Specifies the vertical alignment mode of the text in the special field.

**Bold**

Specifies whether to make the object text bold or not.

**Underline**

Specifies whether the field text will be underlined or not.

**Strikethrough**

Specifies whether to attach a strikeout line to the field text.

**Italic**

Specifies whether to make the field text italic or not.

**Autofit**

Specifies whether to automatically adjust the width of the special field.

**Word Wrap**

Specifies whether to wrap the text to the special field width.

**Ignore HTML Tag**

By default, Logi Report Engine ignores the HTML tag elements that are included in the values of the special field so they display exactly as what they are in the report. Set the option to false if you want Logi Report Engine to transfer the HTML tag elements to the web browser so they are translated into HTML by the web browser. The setting also applies in the HTML output of the report.

**Repeat**

Specifies whether to repeat the group name in the report result. Only available for table and it takes effect only when the group-by field is placed in the detail row.

## Border Tab Properties

This tab shows information about borders of the special field. You can modify all the border settings in this tab.

![Special Field Properties dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4404880481815/spcprpty_border.gif)

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

![Special Field Properties dialog - Others tab](https://devnet.logianalytics.com/hc/article_attachments/4404885549207/spcprpty_other.gif)

**TOC Anchor**

Specifies whether to add the node that represents the special field to the TOC tree in the TOC Browser.

**Suppress When No Records**

Specifies whether to display the special field in the report result when no record is returned to its parent data component.

**Export to XLS**

If true, Server will export the component when you save the report result as an XLS file (make sure to check **Data Format** in the Export dialog box).

**Export to CSV**

If true, Server will export the component when you save the report result as a TXT file with Delimited Format selected.

**Logic Column**

Specifies whether to show the special field in the next visible table cell in the same row when you have hidden the column that holds the field.

**Data Evaluation Setting**

Specifies the group information for the object. Available only for the group-by fields in table.

* **current column**  
   The object will take value of the group-by field in the current column.
* **current row**  
   The object will take value of the group-by field in the current row.

## Display Tab Properties

You can use this tab to modify the render type of the special field. For more information, see [Data Field Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009744242-Data-Field-Properties#Render).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009773061-Sort-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745102-Split-Dialog-Box-Properties)
