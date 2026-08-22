---
title: "Format Bullet Dialog Box"
id: 45190525144973
section: "References - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190525144973-Format-Bullet-Dialog-Box
updated_at: 2026-04-30T15:13:29Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Format Bullet Dialog Box

You can use the Format Bullet dialog box to format the bullets in a bullet chart. This topic describes the options in the dialog box.
    

Designer displays the Format Bullet dialog box when you right-click a bullet of a bullet chart and select Format Bullet from the shortcut menu, or double-click any bullet in the bullet chart.

The dialog box contains the following tabs (Designer displays the Behaviors tab only when the chart is in a library component):

- General Tab

- Fill Tab

- Border Tab

- Data Label Tab

- Hint Tab

- Behaviors Tab

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

Use this tab to specify the general options of the bullet chart.

Size

You can specify the size of the bullets in this box.

- 
Featured Measure Width
Specify the featured measure width as a percentage of the unit width.

- 
Comparative Measure Width
Specify the comparative measure width as a percentage of the unit width.

- 
Qualitative Ranges Width
Specify the qualitative ranges width as a percentage of the unit width.

 

## 
Fill Tab

Use this tab to specify the fill pattern of the bullets.

Featured Measure Color List

You can specify the color pattern of the featured measures in this box. 

- 
Color
Specify the color of the featured measures. To edit the color, select the color indicator and select a color from the color palette, or type the hexadecimal RGB value of a color  (for example, 0xff0000) in the text box.

- 
Transparency
Specify the transparency of the color.

- 
Self Settings
Select to apply the color pattern to the featured measures themselves. When this option is cleared, Designer synchronizes the color pattern that you specify here with the Pattern List property of the chart in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart.

- 
Vary Colors by Color List
Select to apply different colors to the  featured measures.- 
Color List
Select to open the Color List dialog box to modify the color pattern for each featured measure respectively.

Comparative Measure Color List

You can specify the color pattern of the comparative measures in this box.

- 
Color
Specify the color of the selected comparative measures in the same data series. To edit the color, select the color indicator and select a color from the color palette, or type the hexadecimal RGB value of a color  (for example, 0xff0000) in the text box.

- 
Transparency
Specify the transparency of the color.

- 
Color List
Select to open the Color List dialog box to modify the color pattern for comparative measures in the same data series respectively. 

Qualitative Ranges Color List

You can specify the color pattern of the qualitative ranges in this box.

- 
Color
Specify the color of the selected qualitative ranges in the same data series. To edit the color, select the color indicator and select a color from the color palette, or type the hexadecimal RGB value of a color  (for example, 0xff0000) in the text box.

- 
Transparency
Specify the transparency of the color.

- 
Color List
Select to open the Color List dialog box to modify the color pattern for qualitative ranges in the same data series respectively.

Sample

This box displays a preview sample based on your selections.

 

## 
Border Tab

Use this tab to specify properties for the border of the bullets.

Show Border

Select to show the border of the bullets. Designer enables the other border properties in this tab after you select this option.

Color

Specify the color of the border. To edit the color, select the color indicator and select a color from the color palette, or type the hexadecimal RGB value of a color  (for example, 0xff0000) in the text box.

Transparency

Specify the transparency of the border.

Line Style

Select the line style of the border.

Thickness

Specify the width of the border, in pixels.

End Caps

Select the ending style of the border.

- 
butt

Select to end unclosed subpaths and dash segments with no added decoration.

- 
round

Select to end unclosed subpaths and dash segments with a round decoration that has a radius equal to half of the line width.

- 
square

Select to end unclosed subpaths and dash segments with a square projection that extends beyond the end of the segment to a distance equal to half of the line width.

Line Joint

Select the joint style of the border.

- 
miter

Select to join path segments by extending their outside edges until they meet.

- 
round

Select to join path segments by rounding off the corner at a radius of half the line width.

- 
bevel

Select to join path segments by connecting the outer corners of their wide outlines with a straight segment.

Sample

This box displays a preview sample based on your selections.

Path

You can specify the fill pattern of the border in this box.

- 
Outline Path

Select to use outline path for the border.

- Fill Path

- Select  to use whole path for the border.

Dash

You can specify the dash size of the border
in this box if you select a dash line style for the border.

- 
Auto Adjust Dash

Select to adjust the dash size automatically.

- 
Fixed Dash Size

Select to use fixed dash size.

 

## 
Data Label Tab

Designer does not support displaying data labels in bullet charts, so you can skip this tab.

 

## 
Hint Tab

Use this tab to specify properties for the hint of the bullets.

Show Category and Series

Select to include the category and series values in the hint. 

Auto Scale in Number

Specify whether to automatically scale the Number values in the hint that fall into the two ranges:

- When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).

- When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.

By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property on the chart in the Report Inspector for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.

Customize Chart Value Names

Select to customize the names of the fields on the value axis which you want to display in the hint. By default, Designer applies the display names of the fields in the hint to label the values which may be not intuitive to users. You can select the option and select the ellipsis  to customize the names in the Customize Chart Value Names dialog box to help users better understand the values.

 

## 
Behaviors Tab

Designer displays the Behaviors tab only when the bullet chart is in a library component. You can use it to specify web behaviors to the bullets.

Add button

Select to add a new web behavior line.

Remove button

Select to delete the specified web behavior.

Move Up button

Select to move the specified web behavior higher in the list. At runtime, when an event bound with more than one action happens, JDashboard triggers the upper action first.

Move Down button

Select to move the specified web behavior lower in the list.

Events

This column shows the events that you select to trigger the web actions.

Actions

This column shows the web actions that you specify for the events to trigger. Select the ellipsis  in each cell to bind the web action using the Web Action List dialog box.
