---
title: "Format Indicator Dialog Box"
id: 28898058293261
section: "References - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28898058293261-Format-Indicator-Dialog-Box
updated_at: 2024-11-19T18:42:35Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Format Indicator Dialog Box

You can use the Format Indicator dialog box to format the indicators in an indicator chart. This topic describes the options in the dialog box.
    

Designer displays the Format Indicator dialog box when you right-click an indicator in an indicator chart and select Format Indicator from the shortcut menu, or double-click any indicator in an indicator chart.

The dialog box contains the following tabs (Designer displays the Behaviors tab only when the chart is in a library component):

- General Tab

- Frame Tab

- Range Color Tab

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

Use this tab to specify the general properties of the indicators.

Style

You can specify the style of the indicators in this box.

- 
Single
Select to use an indicator to show each value.

- 
Multiple
Select to use multiple indicators to show each value.

Option

You can specify the indicator options in this box.

- 
Left Margin
Specify the gap between the left labels and the left indicators, in pixels.

- 
Top Margin
Specify  the gap between the top labels and the top indicators, in pixels.

- 
Range Radius
Specify the relative size of an indicator in a percentage of the total indicator size.

- 
Style
Select the shape of the indicator graph.

- 
Fill Type
Designer enables this option when the indicator chart displays numeric values. You can use it to specify how you want to fill the indicators.
- 
all
Select to fill the whole indicator.

- 
base on max value
Select to fill the portion of the indicators calculated based on the maximum value of the chart.

Border

You can specify properties for the border of the indicators in this box.

- 
Show Border
Select to show the border of the indicators. Designer enables the other border properties in this box after you select this option.
            

- 

- 
Color
Specify the color of the border. To edit the color, select the color indicator and select a color from the color palette, or type the hexadecimal RGB value of a color  (for example, 0xff0000) in the text box.

- 
Line Style
Select the line style of the border.

- 
Transparency
Specify the transparency of the border.

- 
Thickness
Specify the width of the border, in pixels.

Value

Designer enables this box when the indicator chart displays numeric values. You can use the options in this box to specify the minimum and maximum values to display in the chart.

- 
Minimum
Specify the minimum value to display in the chart.

- 
Maximum
Specify the maximum value to display in the chart.

Value Label

You can specify options for the value labels of the indicators in this box.

- 
Show Value
Select to show the value labels for the indicators.

- 
Position
Select the position  of the value labels relative to the indicators: top, bottom, or center.

- 
Auto Scale in Number
Specify whether to automatically scale the Number values in the labels that fall into the two ranges:
- When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).

- When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.

By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property on the chart in the Report Inspector for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.

Sample

This box displays a preview sample based on your selections.

## 
Frame Tab

Use this tab to specify properties for the frame of the indicator chart.

Size

You can specify the frame size  in this box.

- 
Frame Size
Specify the size of the frame.

Fill

You can specify the fill pattern of the frame in this box.

- 
Fill
Specify the fill pattern of the frame. To edit the fill pattern, select the color indicator and specify a color or effect using the color palette. You can also type the hexadecimal RGB value of a color  (for example, 0xff0000) in the text box.

- 
Transparency
Specify the transparency of the fill pattern.

Border

You can specify properties for the border of the frame in this box.

- 
Border Type
Select the type of the border.
            
- 
none
Select if you do not want to show the border.

- 
raised
Select to show 3-D border that appears as if it is raised off the page.

- 
recess
Select to show 3-D border that appears as if it is pressed into the page.

- 
shadow
Select to show two shadowed borders, beneath and to the right of the object.

- 
solid
Select to use single-line border.

- 
Color
Specify the color of the border. To edit the color, select the color indicator and select a color from the color palette, or type the hexadecimal RGB value of a color  (for example, 0xff0000) in the text box.

- 
Line Style
Select the line style of the border.

- 
Transparency
Specify the transparency of the border.

- 
Thickness
Specify the width of the border, in pixels.

- 
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

- 
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

- 
Path
Specify the fill pattern of the border.
                
- 
Outline Path
Select to use outline path for the border.

- 
Fill Path
Select to use whole path for the border.

- 
Dash
Specify the dash size of the border if you select a dash line style for the border.
    
- 
Auto Adjust Dash
Select to adjust the dash size automatically.

- 
Fixed Dash Size
Select to use fixed dash size.

Category Label

You can specify options for the category labels of the indicators in this box.

- 
Show Category Label
Select to show the category labels for the indicators, which display the category value each indicator represents.

- 
Position
Select the position of the category labels relative to the indicators: top, bottom, or center.

Sample

This box displays a preview sample based on your selections.

## 
Range Color Tab

Use this tab to specify different colors or images to fill the indicators. Designer displays different options in the tab based on the different data types of the values in the indicator chart: Boolean and Numeric/String.

### 
For Boolean Values

Show Image

Select to use images instead of colors to represent the two values in the indicator chart. When you select this option, Designer ignores the colors that you specify in the Color column for the ranges.

Value

This column shows the two values  of the indicator chart, True and False. You cannot change the values.

Color

This column shows the colors that you specify for the two values in the indicator chart. Select the cell to customize the color in the color palette.

Image

This column shows the images that you specify to represent the two values of the indicator chart. Select the ellipsis  in each cell to select the image for a range.

Name

This column shows the names that you specify to display for the two values of the indicator chart.

### 
For Numeric/String Values

Show Image

Select to use images instead of colors to represent the values in different ranges. When you select this option, Designer ignores the colors that you specify in the Color column for the ranges.

Add button

Select to add a new value range.

Remove button

Select to delete the specified value range.

Minimum

This column shows the minimum values that you specify for the ranges.

Maximum

This column shows the maximum values that you specify for the ranges.

Color

This column shows the colors that you specify for the ranges. Select the color cell to customize the color in the color palette.

Image

This column shows the images that you specify to represent the values in the ranges. Select the ellipsis  in each cell to select the image for a range.

Name

This column shows the names that you specify for the ranges.

Others

You can specify the properties for values that do not fall into any of the ranges you define in this box.

- 
Name
Specify the name for the values.

- 
Color
Specify the color for the values. To edit the color, select the color indicator and select a color from the color palette, or type the hexadecimal RGB value of a color  (for example, 0xff0000) in the text box.

- 
Image
Specify the image to represent the values. Select the ellipsis  to select the image.

## 
Hint Tab

Use this tab to specify properties for the hint of the indicators. 

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

Designer displays the Behaviors tab only when the indicator chart is in a library component. You can use it to specify web behaviors to the indicators. 

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
            

Previous Topic  Next Topic
