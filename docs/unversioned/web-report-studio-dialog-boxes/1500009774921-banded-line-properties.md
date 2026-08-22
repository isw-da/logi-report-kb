---
title: "Banded Line Properties"
id: 1500009774921
section: "Web Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009774921-Banded-Line-Properties
updated_at: 2021-07-24T00:48:34Z
---

# Banded Line Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009774881-Aggregate-On-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009746722-Banded-Object-Properties)

# Banded Line Properties

This topic describes how you can use the Banded Line Properties dialog box to update the properties of a line in a banded object. Server displays the dialog box when you right-click a line in a banded object and select **Properties** from the shortcut menu.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Line Property Tab Properties](#Property)
* [Export Tab Properties](#Export)
* [Excel Tab Properties](#Excel)

You see these elements on all the tabs:

**OK**

Select **OK** to apply any changes you made here.

**Cancel**

Select **Cancel** to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Select to view information about the Banded Line Properties dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Select to close the dialog box without saving any changes.

## General Tab Properties

This tab shows some general information of the line.

![Banded Line Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404880406423/bdlineprpty_gnrl.gif)

**Name**

Specifies the display name of the line.

**Show NLS Value**

Select this option to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it.

If you select this option, it takes effect only when you have not modified the display name of the object.

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

## Line Properties Tab Properties

Specifies the properties for the lines.

![Banded Line Properties dialog - Line Properties tab](https://devnet.logianalytics.com/hc/article_attachments/4404880406935/bdlineprpty_prpty.gif)

**Line Color**

Specifies the color of the line.

To change the color, select the color indicator to select a color from the color palette. You can select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009746842-Color-Picker-Dialog-Box-Properties) dialog box in which you can select a color within a wider range. You can also type a color string in the format #RRGGBB directly in the text box. If you want to make the color transparent, type Transparent in the text box.

**Line Thickness**

Specifies the thickness of the line.

**Line Style**

Specifies the style of the line.

**Suppress When No Records**

Specifies whether to display the line in the report result when no record is returned to its parent data component.

## Export Tab Properties

You can use this tab to configure the export settings.

![Banded Line Properties dialog - Export tab](https://devnet.logianalytics.com/hc/article_attachments/4404885497623/bdlineprpty_expt.gif)

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

## Excel Tab Properties

You can use this tab to configure the settings when the line is exported to an Excel file.

![Banded Line Properties dialog - Excel tab](https://devnet.logianalytics.com/hc/article_attachments/4404880407703/bdlineprpty_excl.gif)

[**Bottom Attach Column**](https://devnet.logianalytics.com/hc/en-us/articles/1500009749282-Line-Properties#Attach)

Specifies the X coordinate of the lower right corner of the line in the exported Excel file, measured in cells.

[**Bottom Attach Row**](https://devnet.logianalytics.com/hc/en-us/articles/1500009749282-Line-Properties#Attach)

Specifies the Y coordinate of the lower right corner of the line in the exported Excel file, measured in cells.

[**Top Attach Column**](https://devnet.logianalytics.com/hc/en-us/articles/1500009749282-Line-Properties#Attach)

Specifies the X coordinate of the upper left corner of the line in the exported Excel file, measured in cells.

[**Top Attach Row**](https://devnet.logianalytics.com/hc/en-us/articles/1500009749282-Line-Properties#Attach)

Specifies the Y coordinate of the upper left corner of the line in the exported Excel file, measured in cells.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009774881-Aggregate-On-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009746722-Banded-Object-Properties)
