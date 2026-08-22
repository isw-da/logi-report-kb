---
title: "Format Activity Gauge Dialog Box Properties"
id: 45203918672781
section: "Dialog Boxes in Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203918672781-Format-Activity-Gauge-Dialog-Box-Properties
updated_at: 2026-04-30T14:08:21Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Format Activity Gauge Dialog Box Properties 

You can use the Format Activity Gauge dialog box to format an activity gauge chart. This topic describes the properties in the dialog box.

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

Help

Select to view information about the dialog box.

## 
Circular Graph Tab Properties

Specify the properties for circles in the activity gauge.

Circular

Specify the size of the circles.

- 
Hole Size
    Specify the relative size of a circle in a percentage of the total circle size.

- 
Circular Gap
    Specify the distance between the circles.

- 
Start Style
    Select the style for the start graph of the circles.

- 
End Style
    Select the style for the end graph of the circles.

- 
Start Mark
    Select the mark for the start graph of the circles.

- 
Stop Mark
    Select the mark for the stop graph of the circles.

Fill

Specify the fill color of the circles.

- 
Color
    Specify the color of the circles.

- 
Color List
    Select to open the Color List dialog box to specify the color of the circles.

- 
Transparency
    Specify the transparency for the color of the circles.

- 
Background
    Specify the background color of the circles.
    - 
Auto
          Select to use colors that are lighter than the circles automatically. You cannot specify the Background color when you select Auto.

- 
Use Range Color
    Select to use the color you defined for the ranges as the color of the circles. Then, Server disables the Color, Color List, and Transparency properties.

Value

Specify the values you want to display in the chart. 

- 
Minimum Value
    Specify the minimum value in the chart.

- 
Maximum Value
    Specify the maximum value in the chart.

## 
Pointer Tab Properties

Specify properties of the pointers in the activity gauge.

Show Pointer Value

  Select to show the pointer values. 

- 
Position
 Select the position relationship of the value and the pointers. If you select customized, the X and Y settings on the General tab of the Format Pointer Label dialog box will take effect.

## 
Target Tab Properties

Specify properties of the target in the activity gauge.

Use Target Value

Select to use the target value for the activity gauge.

- 
Target Value 
    Specify the value of the target. 

Target Value

Specify the properties of the target value.

- 
Show Target Value
    Select to show the target value on the activity gauge.
    - 
Position
          Select the position of the target value relative to the circle. If you select customized, the X and Y settings on the General tab of the Format Target Label dialog box will take effect.

## 
Frame Tab Properties

Specify the frame properties of the activity gauge chart.

Size

Specify the size properties of the frame.

- 
Frame Size 
    Specify the size of the frame.

Fill

Specify the color and transparency of the frame.

- 
Fill
    Specify the color to fill the frame.

- 
Transparency
    Specify the transparency of the color to fill the frame.

Border

Specify the properties for the border of the frame.

- 
Line Style

Select the line style of the border.

- 
Border Type

    Select the type of the border.

- 
Color

    Specify the color of the border. To change the color, select the color indicator to access the Select Color dialog box, and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff.

- 
Transparency

  Specify the transparency for the color of the border.

- 
Thickness

    Specify the thickness of the border, in inches.

Gauge Group Name 

Specify the properties for the gauge group name.

- 
Show Gauge Group Name 
    Select to show the names for the circles in the activity gauge, which are values of the field on the category axis. If the activity gauge contains no category field, the group name shows Report by default.
    - 
Position
          Select the position of the names relative to the circles. If you select customized, the X and Y settings on the General tab of the Format Gauge Label dialog box will take effect.

## 
Range Color Tab Properties

Specify different colors to fill the circles in the activity gauge in different ranges.

Add button

Select to add a new color range.

Remove button

Select to remove the selected color range.

Range table

- 
Minimum

Specify the minimum value of a range.

- 
Maximum

Specify the maximum value of a range.

- 
Color

Select the color cell to open the Select Color dialog box, and specify a new color.

- 
Name

Specify the name of a range.

Others

Specify the properties for values that do not fall into any of the ranges you define in the range table.

- 
Name

Specify the name for the values.

- 
Color

    Specify the color for the values. To change the color, select the color indicator to access the Select Color dialog box, and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff.

## 
Hint Tab Properties

Specify the properties of the data marker hint.

Show Category and Series

Select to include the category and series values in the data marker hint.

Auto Scale in Number

When you select Auto fit, Outside Top Inside, Top or Inside Bottom as static data labels' position, you can customize the spacing between the data label and the bar.

The default value auto means that the setting follows that of the chart platform.
