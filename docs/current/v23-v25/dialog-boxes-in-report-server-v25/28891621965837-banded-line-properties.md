---
title: "Banded Line Properties"
id: 28891621965837
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891621965837-Banded-Line-Properties
updated_at: 2026-02-26T02:12:35Z
source_host: docs-report.zendesk.com
---
# 
Banded Line Properties

You can use the Banded Line Properties dialog box to update the properties of a line in a banded object. This topic describes the properties in the dialog box.

Server displays the dialog box when you right-click a line in a banded object and select Properties from the shortcut menu.

This topic contains the following sections:

- 
General Tab Properties 

- Line Property Tab Properties

- Export Tab Properties

- Excel Tab Properties

You see these elements on all the tabs:

OK

Select to apply any changes you made here and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help button

Select to view information about the dialog box.

Close button

Select to close the dialog box without saving any changes.

## 
General Tab Properties

Specify the general properties of the line.

Name

Specify the display name of the line.

Show NLS Value

Select to show the translated name for the display name of the object in the Name text box if you have enabled the NLS feature and translated it, and when you have not modified the display name of the object.

Position

Specify the position of the line.

- 
absolute
  Select if you want to use the X and Y property values to decide the line's position.

- 
static
    Select if you want to place the line at the default location in its container. Server will hide or disable the X, Y, and other position-related properties.

Top Attach Pos X

Specify the horizontal coordinate of the upper left point of the line in a banded panel. A line can cross panels, and the coordinate indicates the relative position in the involved panel. 

Web Report Studio only supports horizontal lines and vertical lines, so you need to ensure that the line you draw is horizontal or vertical.

Top Attach Pos Y

Specify the vertical coordinate of the upper left point of the line in a banded panel.

Bottom Attach Pos X

Specify the horizontal coordinate of the lower right point of the line in a banded panel.

Bottom Attach Pos Y

Specify the vertical coordinate of the lower right point of the line in a banded panel.

## 
Line Properties Tab Properties

Specify the line properties. 

Line Color

Specify the color of the line.

To change the color, select the color indicator. Server displays the color palette. Select a color, or select More Colors to access the Color Picker dialog box in which you can specify a color within a wider range. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff.

If you want to make the color transparent, type Transparent in the text box.

Line Thickness

Specify the thickness of the line.

Line Style

Select the style of the line.

Suppress When No Records

Select if you want to hide the line in the report when no record returns to its parent data component.

## 
Export Tab Properties

Configure the export settings.

Export to CSV

Select if you want to include the object in the Text output with Delimited Format.

Export to Excel

Select if you want to include the object in the Excel output.

Export to HTML 

Select if you want to include the object in the HTML output.

Export to PDF

Select if you want to include the object in the PDF output.

Export to PostScript

Select if you want to include the object in the PostScript output.

Export to Report Result 

Select if you want to include the object when opening the report in Web Report Result.

Export to RTF

Select if you want to include the object in the RTF output.

Export to Text

Select if you want to include the object in the Text output without Delimited Format.

Export to XML

Select if you want to include the object in the XML output.

## 
Excel Tab Properties

Configure the settings for the Excel output.

Bottom Attach Column

Specify the X coordinate of the lower-right corner of the line in the Excel output, measured in the number of cells.

Bottom Attach Row

Specify the Y coordinate of the lower-right corner of the line in the Excel output, measured in the number of cells.

Top Attach Column

Specify the X coordinate of the upper-left corner of the line in the Excel output, measured in the number of cells.

Top Attach Row

Specify the Y coordinate of the upper-left corner of the line in the Excel output, measured in the number of cells.
