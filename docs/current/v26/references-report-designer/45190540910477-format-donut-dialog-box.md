---
title: "Format Donut Dialog Box"
id: 45190540910477
section: "References - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190540910477-Format-Donut-Dialog-Box
updated_at: 2026-04-30T15:13:32Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Format Donut Dialog Box

You can use the Format Donut dialog box to format the donuts of a donut chart. This topic describes the options in the dialog box.
    

Designer displays the Format Donut dialog box when you right-click a donut in a donut chart and select Format Donut from the shortcut menu, or double-click any section in a donut of a donut chart.

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

Use this tab to specify the general properties of the donuts.

Option

You can specify options of the donuts in this box.

- 
Gap Amount
Specify the gap between two donuts.

- 
Explode Amount
Specify the gap between every section and the central point of a donut.

- 
Donut Hole
Specifythe radius percentage of the donut hole to the total donut circle.

- 
Show Donut Name
Select to show the names of the donuts.

KPI Value

Designer enables this box when you do not set the chart property Swap Groups to "true".

- 
Show KPI Value
Select to show the KPI value for each donut.
    

- 
KPI Value
Specify the KPI value to display on each donut. Type the value in the text box or select  and select a formula or summary from the drop-down list to use its value as the KPI value.- 
Auto
Select to use the total value of each donut as the KPI value.

- 
Position
Select the position of the KPI value relative to the donuts: top, bottom, center, or customized. When you select "customized", you can specify the position by dragging any KPI value in the donut chart in the design area.

Angle

You can specify the rotation angle of the donuts in this box.

- 
Angle X
Specify the rotation angle of the donuts around the X axis.

- 
Angle Y
Specify the rotation angle of the donuts around the Y axis.

 

## 
Fill Tab

Use this tab to specify the fill pattern of the donut sections.

Use Single Color

Select to apply single color pattern to fill the donut sections.

- 
Self Settings
Select  to apply the color pattern to the donuts themselves only. When this option is cleared, Designer synchronizes the color pattern that you specify here with the Pattern List property of the chart in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart.

- 
Color
Specify the color of the selected donut section if the chart has no series field, or the color of the donut sections in the current data series if the chart has series field. To edit the color, select the color indicator and select a color from the color palette, or type the hexadecimal RGB value of a color  (for example, 0xff0000) in the text box.

- 
Transparency
Specify the transparency of the color.

- 
Color List
Select to open the Color List dialog box to modify the color pattern for donut sections in the same data series respectively.

Use Single Color with Condition

Select to apply different color patterns to the donut sections based on different conditions. You can select Advanced or Normal to switch between the two editing modes to edit the conditions.

- 
Normal
- 
Select Field
This drop-down list contains all the available fields to which you can apply the conditional fill. Select the field on which you want to define the conditions.

- 
Add button
Select to add a new condition.

- 
Remove button
Select to delete the specified user-defined condition.

- 
Value
Designer displays the column when you select the category or series field of the chart, or a field the values of which are not numbers from the Select Field drop-down list. It shows the values that you specify for each condition.

- 
Start Value
Designer displays the column when you select a value field of the chart, or a field containing numeric values from the Select Field drop-down list. It shows the start values that you specify for each condition.

- 
End Value
Designer displays the column when you select a value field of the chart, or a field containing numeric values from the Select Field drop-down list. It shows the end values that you specify for each condition.

- 
Color
This column shows the colors you specify to apply to values that meet the conditions. To edit the color, select the color indicator and select a color from the color palette, or type the hexadecimal RGB value of a color  (for example, 0xff0000) in the text box.

- 
Transparency
This column shows the transparency of the colors you specify for the conditions.

- 
Label
Select to modify the legend entry label for values of the specified condition.

- 
Value
Designer displays this option after you select a value field of the chart, or a field containing numeric values from the Select Field drop-down list. Select it if you want to display data in the condition expression as value. 

- 
Percent
Designer displays this option after you select a value field of the chart, or a field containing numeric values from the Select Field drop-down list. Select it if you want to display data in the condition expression in percent.

- 
Advanced
- 
Edit button
Select to open the Edit Conditions and Label dialog box to specify the condition, and customize the color pattern and legend entry label for values that meet the condition.

- 
Condition
This column shows the default condition Other and the expression of the condition you add.

- 
Color
This column shows the colors you specify to apply to values that meet the conditions. To edit the color of the default Other condition, select the color indicator and select a color from the color palette, or type the hexadecimal RGB value  of a color (for example, 0xff0000) in the text box.

- 
Transparency
This column shows the transparency of the colors you specify for the conditions. To edit the transparency of the default Other condition, select in the text box and specify the transparency.

- 
Label
Specify the legend entry label for values of the specified condition. You can edit the label in the text box, or select Customized and then select Edit to customize the label in the Label Editor dialog box.

- 
Value
This option indicates that Designer displays data in the condition expression as value. You cannot change it.

- 
Percent
Designer does not support this option when you edit conditions in the advanced mode.

Use Multiple Colors with Condition

Designer does not support this fill type for donut charts.

Sample

This box displays a preview sample based on your selections.

 

## 
Border Tab

Use this tab to specify properties for the border of the donut sections.

Show Border

Select to show the border of the donut sections. Designer enables the other border properties in this tab after you select this option.

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

Use this tab to specify properties of the data labels on the donuts.

Static Data Label

You can specify properties of the static data labels on the donuts in this box.

- 
Show Static Data Label
Select to show the static data labels. Designer enables the other static data label properties after you select this option.

- 
Position
Select the position of the static data labels on the donuts.
    
- 
auto fit
Select to display the static data labels automatically.

- 
sticker
Select to display the static data labels beside the donut sections.

- 
slim leg
Select to display the static data labels beside the donut sections and pointed by thin lines.

- 
best fit
Select to display the static data labels at the best fit position automatically.

- 
on slices
Select to display the static data labels on the donut sections (slices).

- 
Data Label Type
Select in which way to display the values in the static data labels.
    
- 
value
Select to show the value for each donut section.

- 
category name
Select to show the category name for each donut section.

- 
percent
Select to show the percentage of each donut section to the total.

- 
value and percent
Select to show the value and the percentage for each donut section.

- 
category name, value
Select to show the category name and value for each donut section.

- 
category name, percent
Select to show the category name and percentage for each donut section.

- 
category name, value, percent
Select to show the category name, value, and percentage for each donut section.

- 
Auto Scale in Number
Specify whether to automatically scale the Number values in the static data labels that fall into the two ranges:
- When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).

- When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.

By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property on the chart in the Report Inspector for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.

- 
Line Color
Specify the color of the thin lines that point to the static data labels. To edit the color, select the color indicator and select a color from the color palette, or type the hexadecimal RGB value of a color  (for example, 0xff0000) in the text box.

- 
Suppress Label When 0

Select if you do not want to display the static data label when its value is 0.

- 
Show Truncated Label
Select  to truncate the static data labels that go beyond the boundaries of the chart paper instead of them being hidden altogether.

Font

You can specify the font style of the text in the static data labels in this box.

- Font list This drop-down list contains all the font faces you can select to apply to the text.

- Font Size Specify the font size of the text.

- Font Color Specify the font color of the text. To edit the color, select the color indicator and select a color from the color palette, or type the hexadecimal RGB value of a color  (for example, 0xff0000) in the text box.

- Transparency Specify the transparency of the text.

- Rotation Specify the rotation angle of the text around its center, in degrees. The default value is 0.

- Shearing Specify the gradient of the text.

Effects

You can specify the special effects for the text in the static data labels in this box.

- Style Select the font style of the text. It can be one of the following: plain, bold, italic, and bold italic.

- Strikethrough Select the style of the horizontal line using which to strikethrough the text. It can be one of the following: none, thin line, bold line, and double lines.

- Underline Select the style of the horizontal line under the text. It can be one of the following: none, single, single lower, bold line, bold lower, double lines, bold double, patterned line, and bold patterned. When you select "patterned line" or "bold patterned", Designer draws a line or bold line in the pattern of the text.
			

 Web Report Studio and JDashboard do not support underlining chart text, therefore, this property is ignored when the chart runs in Web Report Studio or is used in a dashboard.

- Superscript Select to raise the text above the baseline and change the text to a smaller font size, if a smaller size is available.

- Subscript Select to lower the text below the baseline and change the text to a smaller font size, if a smaller size is available.

- Embossed Select to make the text appear to be raised off the page in relief.

- Engraved Select to make the text appear to be imprinted or pressed into the page.

- Outlined Select to display the exterior border around each character of the text.

- Shadowed Select to add a shadow beneath and to the right of the text.

 

## 
Hint Tab

Use this tab to specify properties for the hint of the donut sections. 

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

Designer displays the Behaviors tab only when the donut chart is in a library component. You can use it to specify web behaviors to the donuts.

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
