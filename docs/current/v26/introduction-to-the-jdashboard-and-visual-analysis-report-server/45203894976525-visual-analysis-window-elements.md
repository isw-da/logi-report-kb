---
title: "Visual Analysis Window Elements"
id: 45203894976525
section: "Introduction to the JDashboard and Visual Analysis Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203894976525-Visual-Analysis-Window-Elements
updated_at: 2026-04-30T14:07:40Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Visual Analysis Window Elements 

The Visual Analysis window has a toolbar at the top, the Resources panel and Filters panel on the left, the presentation area in the middle, and a legend on the right. This topic describes the elements on the Visual Analysis window.

This topic contains the following sections:

- Toolbar

- Resources panel

- Filters panel

- Presentation Area

- Display Type

- Legend

## 
Toolbar

 Menu

Select to open a drop-down menu which contains the following options.

- 
New
 Select to start a new visual analysis in a new Visual Analysis window. 

- 
Open
    Select to open an existing analysis template in a new Visual Analysis window using the Open dialog box. 

- 
Save
 Select to save the changes you made to the current analysis template.

- 
Save As
    Select to save the current analysis template with a different name or location or as a new version using the Save As dialog box. 

- 
Undo
 Select to undo the last operation.

- 
Redo
    Select to reverse the operation of Undo.

- 
Clear Filters
    Select to clear the filters in the Filters panel.

- 
Swap
    Select to exchange the row headers and the column headers.

- 
View
    Select to choose the view mode: 
    
- 
Normal View
      The Report smart layout. A scroll bar appears horizontally or vertically if the available space cannot hold all the data.

- 
Fit Height
 Select to display     all data according to the available height. 

- 
Fit Width
      Select to display     all data according to the available width.

- 
Fit Visible
      Select to use the combination of Fit Width and Fit Height. Server displays all data according to the available space horizontally and vertically.

In the Fit XXX mode, the column header height, row header width, and the header font size is the same as that in Normal View. Server displays a part of the text in the header if there is not enough space for the text.

- 
Help
Select to display the Visual Analysis user documentation.

- 
Exit
Select to exit the Visual Analysis window.

Undo

Select to undo the last operation.

Redo 

Select to reverse the operation of Undo.

Refresh 

Select to refresh the current data. 

 Open

Select to open an existing analysis template in a new Visual Analysis window using the Open dialog box. 

 Save 

Select to save the changes you made during the visual analysis.

Save As

Select to save the current analysis template with a different name or location or as a new version using the Save As dialog box. 

Swap

Select to exchange the columns and rows in the data presentation area.

 View mode

Select the view mode from the drop-down list.

## 
Resources panel

This panel lists all the fields in the current business view. You can drag data resources from the Resources panel to the Filters panel, the presentation area, and the legend section.

## 
Filters panel

This panel lists the filters in use. You can add new filters by dragging group fields from the Resources panel into the Filters panel. The newly added filters use all data by default. 

## 
Presentation Area

This is where you perform visual analysis operations. Follow the instructions in this area to drag data fields from the Resources panel to the positions you want in the presentation area. As you start to drag a field, Server highlights the possible places where you can drop it, with an orange border. When you add a group as a row or column, the crosstab expands to include the new group and recalculates all the aggregations.

You can only add group and aggregation fields into the data presentation area.

The following describes the Column and Row control boxes:

- 

  You can add group fields to this control box to become column headers.

- 

 You can add aggregation fields to this control box to become column headers. Server uses the fields to draw axes horizontally at the bottom.

- 

    You can add group fields to this control box to become row headers. 

- 

    You can add aggregation fields to this control box to become row headers. Server uses the fields to draw axes vertically on the left.

## 
Display Type

Server displays the Display Type button at the upper left of the presentation area. It controls the display type of the data values in the data presentation area. You can select from the following display types: 

- 
Text
  Select to display the data values as text. You should add a data field to the label legend  in the legend section.

- 
Bar
  Select to display the data values in bar chart. 

- 
Line
  Select to display the data values in line chart. 

- 
Pie
  Select to display the data values in pie chart. 

- 
Shape
  Select to display the data values as shape diagrams. 

## 
Legend

Server displays the legend section on the right of the presentation area. The following introduces all available legend types. Some legend types are specific to certain display types. 

- 
 Color
    You can use the color legend to identify the members of a data field by colors.
    You can only bind either of the following data fields with the color legend: 

- One or more group fields.

- One aggregation field. 

For a single field, Server marks each field member by a distinct color. For multiple group fields, Server marks each combination of the members of the fields by a distinct color.

- 
 Label
    You can bind the label legend with multiple data fields to provide label text to the members of the data fields.

- 
 Size
    You can bind the size legend with at most one data field to identify the members of the data field by sizes.

- 
 Slice
    You can bind the slice legend with at most one aggregation field to identify the members of the aggregation field by pie slices. It is available to the Pie display type only. 

- 
 Shape
    You can bind the shape legend with at most one data field to identify the members of the data field by shapes. It is available to the Shape display type only.
