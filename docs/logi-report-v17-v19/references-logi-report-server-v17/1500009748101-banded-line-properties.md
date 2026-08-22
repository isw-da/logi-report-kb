---
title: "Banded Line Properties"
id: 1500009748101
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009748101-Banded-Line-Properties
updated_at: 2021-07-25T07:19:31Z
---

# Banded Line Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748081-Aggregate-On)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009721242-Banded-Object-Properties)

# Banded Line Properties

The Banded Line Properties dialog box is used to specify the properties of a line in a banded object. It appears when you right-click a line in a banded object and select Properties from the shortcut menu.

There are the following tabs in this dialog box: [General](#General), [Line Property](#Property), [Export](#Export) and [Excel](#Excel).

**OK**

Applies the line properties and closes this dialog box.

**Cancel**

Cancels the changes and closes this dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404936816535/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404942519575/btn_close.gif)

Ignores the setting and closes this dialog box.

## General

This tab shows some general information of the line.

![Banded Line Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404936873623/bdlineprpty_gnrl.gif)

**Name**

Specifies the display name of the line.

**Show NLS Value**

Select this option to show the translated name for the display name of the object in the Name text box if you have enabled the NLS feature and translated it.

If selected, this option takes effect only when the display name of the object is not modified.

**Position**

Specifies the position of the object.

* **absolute**  
   The object's position will be decided by its X and Y property values.
* **static**  
   The object will be positioned at the default location in its container. If selected, the X, Y and other position-related properties will be hidden or disabled.

**Top Attach Pos X**

Specifies the horizontal coordinate of the top left point of the line in a banded panel. A line can cross panels and the coordinate indicates the relative position in the involved panel. Only horizontal lines and vertical lines are supported in Web Report Studio, so you need to ensure that the line you draw is horizontal or vertical.

**Top Attach Pos Y**

Specifies the vertical coordinate of the top left point of the line in a banded panel. A line can cross panels and the coordinate indicates the relative position in the involved panel. Only horizontal lines and vertical lines are supported in Web Report Studio, so you need to ensure that the line you draw is horizontal or vertical.

**Bottom Attach Pos X**

Specifies the horizontal coordinate of the bottom right point of the line in a banded panel. A line can cross panels and the coordinate indicates the relative position in the involved panel. Only horizontal lines and vertical lines are supported in Web Report Studio, so you need to ensure that the line you draw is horizontal or vertical.

**Bottom Attach Pos Y**

Specifies the vertical coordinate of the bottom right point of the line in a banded panel. A line can cross panels and the coordinate indicates the relative position in the involved panel. Only horizontal lines and vertical lines are supported in Web Report Studio, so you need to ensure that the line you draw is horizontal or vertical.

## Line Properties

Specifies the properties for the lines.

![Banded Line Properties dialog - Line Properties tab](https://devnet.logianalytics.com/hc/article_attachments/4404936873879/bdlineprpty_prpty.gif)

**Line Color**

Specifies the color of the line.

To change the color, select the color indicator to select a color from the color palette. You can select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009721402-Color-Picker-) dialog box in which you can select a color within a wider range. You can also type a color string in the format #RRGGBB directly in the text box. If you want to make the color transparent, type Transparent in the text box.

**Line Thickness**

Specifies the thickness of the line.

**Line Style**

Specifies the style of the line.

**Suppress When No Records**

Specifies whether to display the line in the report result when no record is returned to its parent data component.

## Export

You can use this tab to configure the export settings.

![Banded Line Properties dialog - Export tab](https://devnet.logianalytics.com/hc/article_attachments/4404942558103/bdlineprpty_expt.gif)

**Export to CSV**

Specifies whether to include the line when you save the report result as a TXT file with Delimited Format selected.

**Export to Excel**

Specifies whether to include the line when exporting the report to Excel.

**Export to HTML**

Specifies whether to include the line when exporting the report to HTML.

**Export to PDF**

Specifies whether to include the line when exporting the report to PDF.

**Export to PostScript**

Specifies whether to include the line when exporting the report to PostScript.

**Export to Report Result**

Specifies whether to include the line in Web Report Studio or when the report is opened in Web Report Result.

**Export to RTF**

Specifies whether to include the line when exporting the report to RTF.

**Export to Text**

Specifies whether to include the line when exporting the report to Text with Delimited Format unselected.

**Export to XML**

Specifies whether to include the line when exporting the report to XML.

## Excel

You can use this tab to configure the settings when the line is exported to an Excel file.

![Banded Line Properties dialog - Excel tab](https://devnet.logianalytics.com/hc/article_attachments/4404936874135/bdlineprpty_excl.gif)

[**Bottom Attach Column**](https://devnet.logianalytics.com/hc/en-us/articles/1500009723962-Line#Attach)

Specifies the X coordinate of the lower right corner of the line in the exported Excel file, measured in cells.

[**Bottom Attach Row**](https://devnet.logianalytics.com/hc/en-us/articles/1500009723962-Line#Attach)

Specifies the Y coordinate of the lower right corner of the line in the exported Excel file, measured in cells.

[**Top Attach Column**](https://devnet.logianalytics.com/hc/en-us/articles/1500009723962-Line#Attach)

Specifies the X coordinate of the upper left corner of the line in the exported Excel file, measured in cells.

[**Top Attach Row**](https://devnet.logianalytics.com/hc/en-us/articles/1500009723962-Line#Attach)

Specifies the Y coordinate of the upper left corner of the line in the exported Excel file, measured in cells.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748081-Aggregate-On)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009721242-Banded-Object-Properties)
