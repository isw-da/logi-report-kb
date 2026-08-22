---
title: "Special Field Properties"
id: 1500009645762
section: "References Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009645762-Special-Field-Properties
updated_at: 2021-07-24T20:55:01Z
---

# Special Field Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009645742-Sort)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009645782-Split)

# Special Field Properties

The Special Field Properties dialog helps you to edit the properties of a special field. It contains the following tabs:

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

This tab shows some general information of the special field. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404926763031/spcprpty_gnrl.gif)

**Name**

Specifies the display name of the special field, which will be shown on the shortcut menu of the special field.

**Show NLS Value**

Specifies to show the translated name of the display name of the special field in the Name text box if you have enabled the NLS feature and translated it.

If checked, this option takes effect only when the display name of the special field is not modified.

**Type**

Specifies the type of the special field. Select a new one from the drop-down list if you want to change the type. The following types are available:

* **Fetch Date**  
   Prints the date when the data is retrieved from the database.
* **Fetch Time**  
   Prints the time when the data is retrieved from the database.
* **Global Page N of M**  
  Prints a specific global page number out of the global total page number. You can specify the format of this special field in the Report Inspector. The operation is the same as Page N of M.
* **Global Page Number**  
  Prints the global page number of the whole report wherever it is placed.
* **Global Total Page Number**  
  Prints the global total page number of the whole report wherever the field is placed.
* **Group Name**  
   Prints the group name, which usually placed in the Group Header/Footer panel.
* **Group Number**  
   Prints the group number, which is usually placed in the Group Header/Footer panel.
* **Modified Date**  
   Prints the last modified date for the catalog.
* **Modified Time**  
   Prints the last modified time for the catalog.
* **Page N of M**  
  Prints the page number of the total page number.
* **Page Number**  
  Prints the page number for each page.
* **Print Date**  
   Prints today's date (or the date designated on your computer).
* **Print Time**  
   Prints the current time on your computer.
* **Record Number**  
  Prints the record number, which is usually placed in the Details panel.
* **SQL Statement**  
  Prints the SQL statements used to execute the query.
* **Task ID**  
  Prints the internal task ID, which is a unique time stamp.
* **Total Fetched Records**  
   Prints the total number of records which take part in grouping calculation. The possible result of the special field is as follows:
  + If you don't set any filter condition in the Filter dialog, print the very number of the record obtained after setting the property Maximum Records.
  + If you set filter conditions in the Filter dialog, print the number of records obtained after performing the filters, even though you have set the property Maximum Records before setting the filters.
* **Total Group Number**  
   Prints the total group number, which is usually placed in the group Header/Footer panel.
* **Total Page Number**  
   Prints the total number of pages in the report.
* **Total Records**  
   Prints the total number of records after all the filter conditions are performed, except the ones created in the Filter dialog of Page Report Studio, and the Group Filter dialog and top N or bottom N condition in Logi JReport Designer.
* **User Name**  
   Prints the User name with which you log onto Logi JReport Server.

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

To change the color, select the color indicator to bring out the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009645662-Select-Color) dialog and then specify a new color, or input a color string in the format #RRGGBB. If you want to make the background transparent, input Transparent in the text box.

**Foreground**

Specifies the foreground color of the special field.

To change the color, select the color indicator to bring out the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009645662-Select-Color) dialog and then specify a new color, or input a color string in the text box.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Font

This tab shows the font-related information of the special field. You can modify all the font settings in this tab. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920612503/spcprpty_font.gif)

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

If this option is unchecked, Logi JReport will parse HTML tag elements in the field value while the report is to be saved as an HTML file; or the field value will appear in the HTML file the same as that in Page Report Studio (HTML tag elements in the field value, if any, will not be parsed).

**Repeat**

Specifies whether to repeat the group name in the report result. Only available for table and it takes effect only when the group by field is placed in the detail row.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Border

This tab shows information about borders of the special field. You can modify all the border settings in this tab. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404926763415/spcprpty_border.gif)

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

![](https://devnet.logianalytics.com/hc/article_attachments/4404926763671/spcprpty_other.gif)

**TOC Anchor**

Specifies whether or not to add the node that represents the special field to the TOC tree that is displayed in the TOC Browser.

**Suppress When No Records**

If true and no records are returned by the report, the special field will not be displayed.

**Export to XLS**

If true, the special field will be exported when you save the report result as an XLS file (make sure to check Data Format in the Export dialog).

**Export to CSV**

If true, the special field will be exported when you save the report result as a TXT file with Delimited Format selected.

**Logic Column**

Specifies whether to show the special field in the next visible table cell in the same row when the column which holds the field is hidden.

**Data Evaluation Setting**

Specifies the group information for the object. Available only for the group by fields in table.

* **current column**  
   The object will take value of the group by field in the current column.
* **current row**  
   The object will take value of the group by field in the current row.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Display

You can use this tab to modify the render type of the special field. For details about the display types, see [Data Field Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009645022-Data-Field-Properties#Render).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009645742-Sort)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009645782-Split)
