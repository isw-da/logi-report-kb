---
title: "KPI Chart Wizard Dialog Box"
id: 45190544894221
section: "References - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190544894221-KPI-Chart-Wizard-Dialog-Box
updated_at: 2026-04-30T15:13:52Z
source_host: logi-report-v26.insightsoftware.com
---
# 
KPI Chart Wizard Dialog Box

You can use the KPI Chart Wizard dialog box to modify the KPI chart in a KPI. This topic describes the options in the dialog box.
    

Designer displays the KPI Chart Wizard dialog box when you right-click a KPI chart in a KPI and select KPI Chart Wizard from the shortcut menu.

 The dialog box contains the following screens:

- Data Screen

- Type Screen

- Display Screen

- Layout Screen

- Style Screen

Designer displays these buttons in all the screens:

Back

Select to go back to the previous screen.

Next

Select to go to the next screen.

Finish

Select to finish your work and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.

## 
Data Screen

This screen shows that the KPI chart inherits the dataset bound with the KPI. You cannot change the dataset.

 

## 
Type Screen

Use this screen to specify the type of the KPI chart. You can create a KPI chart in any of the following 2-D types: Bar, Bench, Line, Area, Pie, and Bullet. See Chart Types for the more information about the chart types.

Single chart

Select to create a single chart.

- Chart Type
This box lists all the chart types that you can use to create a single chart. Select the type you want.

- 
Subtype

This box lists all the subtypes of the selected chart type. Select the subtype for the chart. You can point to a subtype icon to get its name.

Combo chart

Select to create more than one type using the primary or secondary axis. The types should be featured as a combination chart.

- 
Chart Type

This box lists all the chart types that you can use in a combo chart. Select the type you want.

- 
Subtype

This box lists all the subtypes of the selected chart type. Select the subtype for the combo chart. You can point to a subtype icon to get its name.

- 
Chart Type Groups

This box lists the chart types that you select to use in the combo chart.

- 
Primary Axis

- 
<Add Combo Type>

Select to add a chart type to the primary axis.

- 
Secondary Axis

- 
<Add Combo Type>

Select  to add a chart type to the secondary axis.

- 
Remove button
Select to delete the specified chart type from the Chart Type Groups box.

 

## 
Display Screen

Use this screen to specify the data to display in the KPI chart.

Title

Specify the title of the KPI chart.

Resources

This box lists the available data fields that you can use for the KPI chart. You can also create dynamic resources to use in the KPI chart. 

Add button

Select to add the specified field in the Resources box to the chart axis.

Remove button

Select to remove the specified field from the KPI chart.

Replace button

Select to replace the field on an axis with the specified field in the Resources box.

Category/Series

This box lists the field that you add to display on the category/series axis of the KPI chart.

For a real time chart, if you do not specify the category field, Designer displays the text "Use System Refresh Time" in the Category box by default, meaning Designer uses the time at which the chart refreshes itself  as the category value. Designer disables the Series box in this case.

- 
Special Group
Select to open the User Defined Group dialog box to define how to group information.

- 
Order/Select N 
Select to open the Category Options dialog box or Series Options dialog box to specify the sort order of the category or series values and define the number of the category or series values to show in the chart.

Show Values

This box lists the values that you add to show in the KPI chart.

- 
Edit button
Designer enables this button when you select a constant value or an average value in the Show Values box. Select it to open the Edit Additional Value dialog box to edit the value. 

- 
Move Up button
Select to move the specified value higher in the display order.

- 
Move Down button
Select to move the specified value lower in the display order.

Motion Bar for Playable Chart

Designer enables this option only when the KPI chart is of the single bar or bench type. Select it and then add a  field as the motion field to make the chart a motion chart. A motion field can only be of the Integer, Date, or Time data type. 

- 
Special Function
Designer enables this button when the motion field is Date data type. Select it to open the Special Function dialog box to define special function to the motion field. 

Real Time

 Designer enables this option only when the KPI chart is of the single bar, bench, line, or area type. Select it to run the chart in real time mode.

- 
Use System Time for Category
Select to use the time at which the chart refreshes itself as the category value.

- 
Refresh Interval
Specify the time interval at which the chart gets data and refreshes itself automatically.

- 
Show Most Recent N Points
Specify the number of points to keep for the real time data in the chart.

- 
Incremental Fetch
Select to open the Unique Key dialog box to configure a unique key for the real time chart.

 

## 
Layout Screen

Use this screen to specify the layout of the chart elements. Designer does not display some options  for certain chart types. For more information about the options, select here.

 

## 
Style Screen

Use this screen to specify the style of the KPI chart.

Style

This box lists the styles you can apply. Select the style for the KPI hart.

Preview

This box displays a diagram illustrating the effect of the selected style on the KPI chart.

Inherit Style

Select to apply the style of the parent KPI to the KPI chart.
