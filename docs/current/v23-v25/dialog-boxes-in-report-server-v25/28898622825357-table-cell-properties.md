---
title: "Table Cell Properties"
id: 28898622825357
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28898622825357-Table-Cell-Properties
updated_at: 2026-02-26T02:11:53Z
source_host: docs-report.zendesk.com
---
# 
Table Cell Properties 

You can use the Table Cell Properties dialog box to edit the properties of a table cell. This topic describes the properties in the dialog box.

This topic contains the following sections:

- General Tab Properties

- Border Tab Properties

- Others Tab Properties

You see these elements on all the tabs:

OK

Select to apply any changes you made here and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.

## 
General Tab Properties

Specify the general properties of the table cell.

Name

Specify the display name of the table cell.

Show NLS Value

Select to show the translated name for the display name of the object in the Name text box if you have enabled the NLS feature and translated it, and when you have not modified the display name of the object.

Background

Specify the background color of the table cell. 

To change the color, select the color indicator to access the Select Color dialog box, and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff. If you want to make the background transparent, type Transparent in the text box.

## 
Border Tab Properties

Specify the border properties of the table cell.

Color

Specify the border color.

Width

Specify the border width in inches.

Top Line

Select the style of the top border line.

Bottom Line

Select the style of the bottom border line.

Left Line

Select the style of the left border line.

Right Line

Select the style of the right border line.

## 
Others Tab Properties

Configure some miscellaneous settings.

Export to XLS

Select true if you want to export the object when you save the report as an XLS file (make sure to check Data Format in the Export dialog box).

Export to CSV

Select true if you want to export the object when you save the report as a TXT file with Delimited Format.

Horizontal Alignment

Specify the horizontal alignment mode of the contents in the table cell. When the Position property for the object in the cell is absolute, this property does not take effect.

Vertical Alignment

Specify the vertical alignment mode of the contents in the table cell. When the Position property for the object in the cell is absolute, this property does not take effect.

Scope

A representation of the standard HTML attribute scope. Specify the set of data cells for which the current header cell provides header information.

- 
row
Select if you want the current cell to provide header information for the rest of the row that contains it.
  

- 
column
Select if you want the current cell to provide header information for the rest of the column that contains it.
  

- 
none
Select if you don't want to generate the scope attribute when exporting to HTML.

Joining Merge

Select true to make all the sequential rows in the cell vertically merged in the report. It is meaningful to set the property only when the cell merges with other cells in the same column.

Repeat

Select true to repeat the contents of the cell in every page of the report when the cell splits into pages.
