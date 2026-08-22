---
title: "Special Field Properties"
id: 1500009746381
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009746381-Special-Field-Properties
updated_at: 2021-07-25T07:19:55Z
---

# Special Field Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746361-Sort)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009746401-Split)

# Special Field Properties

The Special Field Properties dialog box is used to edit the properties of a special field.

There are the following tabs in this dialog box: [General](#General), [Font](#Font), [Border](#Border), [Others](#Others) and [Display](#Render).

**OK**

Applies the settings and closes this dialog box.

**Cancel**

Cancels the settings and closes this dialog box.

**Help**

Displays the help document about this feature.

## General

This tab shows some general information of the special field.

![Special Field Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404936908183/spcprpty_gnrl.gif)

**Name**

Specifies the display name of the special field.

**Show NLS Value**

Select this option to show the translated name for the display name of the object in the Name text box if you have enabled the NLS feature and translated it.

If selected, this option takes effect only when the display name of the object is not modified.

**Type**

Specifies the type of the special field. Select a new one from the drop-down list if you want to change the type.

**Position**

Specifies the position mode of the special field. If the special field is directly contained in the report body, a tabular cell, or a text box, its position mode can be modified.

* **Absolute**: The special field's position will be decided by its X and Y property values.
* **Static**: The special field will be positioned at the default location in its container. If selected, the X, Y and other position-related properties will be hidden or disabled.

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

To change the color, select the color indicator to bring out the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009746261-Select-Color) dialog box and then specify a new color, or type a color string in the format #RRGGBB. If you want to make the background transparent, type Transparent in the text box.

**Foreground**

Specifies the foreground color of the special field.

To change the color, select the color indicator to bring out the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009746261-Select-Color) dialog box and then specify a new color, or type a color string in the text box.

## Font

This tab shows the font-related information of the special field. You can modify all the font settings in this tab.

![Special Field Properties dialog - Font tab](https://devnet.logianalytics.com/hc/article_attachments/4404942581783/spcprpty_font.gif)

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

Specifies whether or not to attach a strikeout line to the field text.

**Italic**

Specifies whether to make the field text italic or not.

**Autofit**

Specifies whether or not to automatically adjust the width of the special field.

**Word Wrap**

Specifies whether or not to wrap the text to the special field width.

**Ignore HTML Tag**

If this option is unselected, Logi Report will parse HTML tag elements in the field value while the report is to be saved as an HTML file; or the field value will appear in the HTML file the same as that in Page Report Studio (HTML tag elements in the field value, if any, will not be parsed).

**Repeat**

Specifies whether to repeat the group name in the report result. Only available for table and it takes effect only when the group-by field is placed in the detail row.

## Border

This tab shows information about borders of the special field. You can modify all the border settings in this tab.

![Special Field Properties dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4404936908439/spcprpty_border.gif)

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

![Special Field Properties dialog - Others tab](https://devnet.logianalytics.com/hc/article_attachments/4404936908695/spcprpty_other.gif)

**TOC Anchor**

Specifies whether or not to add the node that represents the special field to the TOC tree in the TOC Browser.

**Suppress When No Records**

Specifies whether to display the special field in the report result when no record is returned to its parent data component.

**Export to XLS**

If true, the special field will be exported when you save the report result as an XLS file (make sure to check Data Format in the Export dialog box).

**Export to CSV**

If true, the special field will be exported when you save the report result as a TXT file with Delimited Format selected.

**Logic Column**

Specifies whether to show the special field in the next visible table cell in the same row when the column which holds the field is hidden.

**Data Evaluation Setting**

Specifies the group information for the object. Available only for the group-by fields in table.

* **current column**  
   The object will take value of the group-by field in the current column.
* **current row**  
   The object will take value of the group-by field in the current row.

## Display

You can use this tab to modify the render type of the special field. For details about the display types, see [Data Field Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009745381-Data-Field-Properties#Render).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746361-Sort)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009746401-Split)
