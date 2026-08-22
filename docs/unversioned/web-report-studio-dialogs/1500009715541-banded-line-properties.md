---
title: "Banded Line Properties"
id: 1500009715541
section: "Web Report Studio Dialogs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009715541-Banded-Line-Properties
updated_at: 2021-11-03T06:57:30Z
---

# Banded Line Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009715461-Aggregate-On)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009715581-Banded-Object-Properties)

# Banded Line Properties

The Banded Line Properties dialog helps you to specify the properties of the line and contains the following tabs: [General](#General), [Line Property](#Property), [Export](#Export) and [Excel](#Excel). This dialog appears when you right-click a line in a banded object and select Properties from the shortcut menu.

**OK**

Applies the line properties and closes this dialog.

**Cancel**

Cancels the changes and closes this dialog.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4412139537431/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4412112572951/btn_close.gif)

Ignores the setting and closes this dialog.

## General

This tab shows some general information of the line.

![Banded Line Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4412139562647/bdlineprpty_gnrl.gif)

**Name**

Specifies the display name of the line.

**Show NLS Value**

Specifies to show the translated name for the display name of the line in the Name text box if you have enabled the NLS feature and translated it.

If checked, this option takes effect only when the display name of the line is not modified.

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

![Banded Line Properties dialog - Line Properties tab](https://devnet.logianalytics.com/hc/article_attachments/4412131457047/bdlineprpty_prpty.gif)

**Line Color**

Specifies the color of the line.

To change the color, select the color indicator to select a color from the color palette. You can select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009715801-Color-Picker-) dialog in which you can select a color within a wider range. You can also input a color string in the format #RRGGBB directly in the text box. If you want to make the color transparent, input Transparent in the text box.

**Line Thickness**

Specifies the thickness of the line.

**Line Style**

Specifies the style of the line.

**Suppress When No Records**

Specifies whether to display the line in the report result when no record is returned to its parent data component.

## Export

You can use this tab to configure the export settings.

![Banded Line Properties dialog - Export tab](https://devnet.logianalytics.com/hc/article_attachments/4412139562903/bdlineprpty_expt.gif)

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

![Banded Line Properties dialog - Excel tab](https://devnet.logianalytics.com/hc/article_attachments/4412112604439/bdlineprpty_excl.gif)

[**Bottom Attach Column**](https://devnet.logianalytics.com/hc/en-us/articles/1500009692142-Line#Attach)

Specifies the X coordinate of the lower right corner of the line in the exported Excel file, measured in cells.

[**Bottom Attach Row**](https://devnet.logianalytics.com/hc/en-us/articles/1500009692142-Line#Attach)

Specifies the Y coordinate of the lower right corner of the line in the exported Excel file, measured in cells.

[**Top Attach Column**](https://devnet.logianalytics.com/hc/en-us/articles/1500009692142-Line#Attach)

Specifies the X coordinate of the upper left corner of the line in the exported Excel file, measured in cells.

[**Top Attach Row**](https://devnet.logianalytics.com/hc/en-us/articles/1500009692142-Line#Attach)

Specifies the Y coordinate of the upper left corner of the line in the exported Excel file, measured in cells.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009715461-Aggregate-On)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009715581-Banded-Object-Properties)
