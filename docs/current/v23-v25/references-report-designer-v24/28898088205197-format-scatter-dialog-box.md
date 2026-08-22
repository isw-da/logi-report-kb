---
title: "Format Scatter Dialog Box"
id: 28898088205197
section: "References - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28898088205197-Format-Scatter-Dialog-Box
updated_at: 2024-09-30T09:09:31Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Format Scatter Dialog Box

You can use the Format Scatter dialog box to format the scatter in a scatter chart. This topic describes the options in the dialog box.
    

Designer display the Format Scatter dialog box when you right-click a marker in a scatter chart and select Format Scatter from the shortcut menu, or double-click a marker in a scatter chart. 

This dialog box contains the following tabs:

- General Tab

- Fill Tab

- Data Label Tab

- Hint Tab

Designer displays these buttons in all the tabs:

OK

Select to apply your settings and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Apply

Select to apply all changes and leave the dialog box open.

Help

Select to view information about the dialog box.

## 
General Tab

Use this tab to specify general properties of the scatter chart.

Layout

You can specify the layout of the scatter in this box.

- 
No line
Select if you do not want to use lines  to connect the markers in the scatter chart.

- 
Straight Line
Select to use straight lines to connect the markers in the scatter chart.

- 
Curved Line
Select to use curved lines to connect the markers in the scatter chart.

Line

You can specify the property of the lines that connect the markers in the scatter chart in this box.

- 
Thickness
    Specify the thickness of the lines, in pixels.

Node

You can specify properties of the markers in the scatter chart in this box.

- 
Style
Select the style of the markers.

- 
Width
Specify the width of the markers, in pixels.

- 
Height
Specify the height of the markers, in pixels.

## 
Fill Tab

Use this tab to specify the fill pattern of the scatter markers.

Color

Specify the color of the selected scatter markers in the same data series. To edit the color, select the color indicator and select a color from the color palette, or type the hexadecimal RGB value of a color  (for example, 0xff0000) in the text box.

Transparency

Specify the transparency of the color.

Self Settings

Select to apply the color pattern to the scatter markers themselves only. When this option is cleared, Designer synchronizes the color pattern that you specify here with the Pattern List property of the chart in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart.

Color List

Select to open the Color List dialog box to modify the color pattern for scatter markers in the same data series respectively.

Sample

This box displays a preview sample based on your selections.

## 
Data Label Tab

Designer does not support displaying data labels in scatter charts, so you can skip this tab.

## 
Hint Tab

Use this tab to specify properties for the hint of the scatter markers.

Show Category and Series

Select to include the category and series values in the hint. 

Auto Scale in Number

Specify whether to automatically scale the Number values in the hint that fall into the two ranges:

- When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).

- When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.

By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property on the chart in the Report Inspector for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.

Customize Chart Value Names

Select to customize the names of the fields on the value axis which you want to display in the hint. By default, Designer applies the display names of the fields in the hint to label the values which may be not intuitive to users. You can select the option and select the ellipsis  to customize the names in the Customize Chart Value Names dialog box to help users better understand the values.

Previous Topic  Next Topic
