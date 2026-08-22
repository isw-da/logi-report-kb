---
title: "Format Activity Gauge Dialog Box Properties"
id: 28891524033677
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891524033677-Format-Activity-Gauge-Dialog-Box-Properties
updated_at: 2026-02-26T02:12:47Z
source_host: docs-report.zendesk.com
---
# 
Format Activity Gauge Dialog Box Properties

This topic describes how you can use the Format Activity Gauge dialog box to format an activity gauge chart. Server displays the dialog box when you right-click on an activity gauge chart and select Format Graph from the shortcut menu.

This topic contains the following sections:

- Circular Graph Tab Properties

- Pointer Tab Properties

- Target Tab Properties

- Frame Tab Properties

- Range Color Tab Properties

- Hint Tab Properties

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
Circular Graph Tab Properties

Specify the properties for circles in the activity gauge.

Circular

Specify the size of the circles.

- 
Hole Size
    Specify the relative size of a circle in a percentage of total circle size.

- 
Circular Gap
    Specify the distance between the circles.

- 
Start Style
    Specify the style for the start graph of the circles.

- 
End Style
    Specify the style for the end graph of the circles.

- 
Start Mark
    Specify the mark for the start graph of the circles.

- 
Stop Mark
    Specify the mark for the stop graph of the circles.

Fill

Specify the color of the circles.

- 
Color
    Specify the color of the circles.

- 
Color List
    Select to open the Color List dialog box, and then specify the color of the circles.

- 
Transparency
    Specify the transparency for color of the circles.

- 
Background
    Specify the background color of the circles.
    - 
Auto
          Select if you want to use colors that are lighter than the circles automatically. Server disables the Background property when Auto is selected.

- 
Use Range Color
    Select if you want to use the color you defined for the ranges as the color of the circles. Then, Server disables the Color, Color List, and Transparency properties in the tab.

Value

Specify the values you want to display in the chart. 

- 
Minimum Value
    Specify the minimum value in the chart. You can also use a formula to control the property.

- 
Maximum Value
    Specify the maximum value in the chart. You can also use a formula to control the property.

## 
Pointer Tab Properties

Specify properties of the pointers in the activity gauge.

Show Pointer Value

     Select if you want to show the pointer values. 

- 
Position
    Select the position relationship of the value and the pointers. If you select customized, the X and Y settings in the General tab of the Format Pointer Label dialog box will take effect.

## 
Target Tab Properties

Specify properties of the target in the activity gauge.

Use Target Value

Select if you want to use the target value for the activity gauge.

- 
Target Value 
    Specify the value of the target. You can also use a formula to control the value.

Target Value

Specify properties of the target value.

- 
Show Target Value
 Select if you want to show the target value on the activity gauge.
    - 
Position
 Select the position of the target value relative to the circle. If you select customized, the X and Y settings in the General tab of the Format Target Label dialog box will take effect.

## 
Frame Tab Properties

Specify properties for the frame of the activity gauge chart.

Size

Specify the size properties of the frame.

- 
Frame Size 
    Specify the size of the frame.

Fill

Specify the color and transparency of the frame.

- 
Fill
    Specify the color you want to fill the frame.

- 
Transparency
    Specify the transparency of the color you want to fill the frame.

Border

Specify the properties for the border of the frame.

- 
Line Style

Specify the line style you want to apply to the border.

- 
Border Type

    Specify the type of the border.

- 
Color

    Specify the color of the border. To change the color, select the color indicator. Server displays the color palette. Select a color, or select More Colors to access the Color Picker dialog box in which you can specify a color within a wider range.

- 
Transparency

  Specify the transparency for color of the border.

- 
Thickness

    Specify the thickness of the border, in inches.

Gauge Group Name

Specify the properties for the gauge group name.

- 
Show Gauge Group Name
    Select if you want to show names for the circles in the activity gauge which are values of the field on its category axis. If the activity gauge contains no category field, the group name shows Report by default.
    - 
Position
 Select the position of the names relative to the circles. If you select customized, the X and Y settings in the General tab of the Format Gauge Label dialog box will take effect.

## 
Range Color Tab Properties

Specify different colors to fill the circles in the activity gauge in different ranges.

Add buttonSelect to add a new color range.

Remove button

Select to remove the selected color range.

Minimum

Specify the minimum value of the range.

Maximum

Specify the maximum value of the range.

Color

Specify the color schema of the range. 

Select in the color cell. Server displays the color palette. Select a color, or select More Colors to access the Color Picker dialog box in which you can specify a color within a wider range.

Name

Specify the name of a range.

Others

Specify the properties for values that do not fall into any of the ranges you define.

- 
Name

Specify the name for the values.

- 
Color

    Specify the color for the values. To change the color, select the color indicator. Server displays the color palette. Select a color, or select More Colors to access the Color Picker dialog box in which you can specify a color within a wider range.

## 
Hint Tab Properties

Specify properties of the data marker hint.

Show Category and Series

Select to include the category and series values in the data marker hint.

Auto Scale in Number

When you select Auto fit, Outside Top Inside, Top or Inside Bottom as static data labels' position, you can customize the spacing between the data label and the bar.

The default value auto means that the setting follows that of the chart.
