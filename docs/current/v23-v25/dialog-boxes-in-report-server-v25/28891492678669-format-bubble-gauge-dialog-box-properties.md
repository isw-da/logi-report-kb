---
title: "Format Bubble Gauge Dialog Box Properties"
id: 28891492678669
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891492678669-Format-Bubble-Gauge-Dialog-Box-Properties
updated_at: 2026-02-26T02:12:49Z
source_host: docs-report.zendesk.com
---
# 
Format Bubble Gauge Dialog Box Properties

This topic describes how you can use the Format Bubble Gauge dialog box to format the bubble gauges in a bubble gauge chart. Server displays the dialog box when you right-click on a bubble gauge chart and select Format Graph from the shortcut menu. 

This topic contains the following sections:

- Staff Graph Tab Properties

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
Staff Graph Tab Properties

Specify the properties for bubbles in the bubble gauge.

Bubbles

Specify the properties of the bubbles.

- 
Left Margin
    Specify the gap between the left labels and left bubbles, in inches.

- 
Top Margin
    Specify the gap between top labels and top bubbles, in inches.

- 
Range Radius
    Specify the relative size of a bubble in a percentage of total bubble size.

- 
Draw Category (X) Grid
    Select if you want to draw category grid.

- 
Draw Series (Z) Grid
    Select if you want to draw series grid.

Border

Specify the properties for the border of the bubbles.

- 
Show Border
Select if you want to show the border of the bubbles. Then, Server enables the following border properties.

- 
Line Style
        Specify the line style you want to apply to the border.

- 
Color
        Specify the color of the border.

- 
Transparency
Specify the transparency for color of the border.

- 
Thickness
        Specify the thickness of the border, in inches.

Value

Specify the minimum and maximum values for the color range. Server divides the values equally into three ranges, each of which uses the color you specify in the Range Color tab automatically. This setting works only when you do not specify ranges for the values in the Range Color tab. 

- 
Minimum Value
    Specify the minimum value you want to display in the chart. You can also use a formula to control the property.

- 
Maximum Value
    Specify the maximum value you want to display in the chart. You can also use a formula to control the property.

## 
Frame Tab Properties

Specify the properties for the frame of the bubble gauge chart.

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
    Select if you want to show names for the bubbles in the bubble gauge which are values of the field on its category axis. If the bubble gauge contains no category field, the group name shows Report by default.
    - 
Position
        Select the position of the names relative to the bubbles. If you select customized, the X and Y settings in the General tab of the Format Gauge Label dialog box will take effect.

## 
Range Color Tab Properties

Specify different colors to fill the bubbles in bubble gauge in different ranges.

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

Specify the properties of the data marker hint.

Show Category and Series

Select to include the category and series values in the data marker hint.

Auto Scale in Number

When you select Auto fit, Outside Top Inside, Top or Inside Bottom as static data labels' position, you can customize the spacing between the data label and the bar.

The default value auto means that the setting follows that of the chart.
