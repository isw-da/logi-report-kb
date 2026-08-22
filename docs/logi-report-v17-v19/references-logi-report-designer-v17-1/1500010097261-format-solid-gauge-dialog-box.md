---
title: "Format Solid Gauge Dialog Box"
id: 1500010097261
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010097261-Format-Solid-Gauge-Dialog-Box
updated_at: 2021-07-23T19:15:32Z
---

# Format Solid Gauge Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010097241-Format-Series-Z-Gridline-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010097281-Format-Stock-Dialog-Box)

# Format Solid Gauge Dialog Box

You can use the Format Solid Gauge dialog box to [format a solid gauge chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010056922-Formatting-the-Gauge-in-a-Gauge-Chart#Solid). This topic describes the options in the dialog box.

Designer displays the Format Solid Gauge dialog box when you right-click any range in an arc in a solid gauge chart and select Format Solid Gauge from the shortcut menu, or double-click any arc range in the solid gauge.

The dialog box contains the following tabs (Designer displays the Behaviors tab only when the chart is in a library component):

* [Circular Graph Tab](#Circular)
* [Axis Tab](#Axis)
* [Pointer Tab](#Pointer)
* [Target Tab](#Target)
* [Frame Tab](#Frame)
* [Range Color Tab](#Range)
* [Hint Tab](#Hint)
* [Behaviors Tab](#Behaviors)

You see these buttons in all the tabs:

**OK**

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Apply**

Select to apply all changes and leave the dialog box open.

**Help**

Select to view information about the dialog box.

## Circular Graph

Use this tab to specify the properties for the arcs in the solid gauge.

![Format Solid Gauge dialog box - Circular Graph](https://devnet.logianalytics.com/hc/article_attachments/4404856933015/fmtsldgauge_crculr.gif)

**Size**

You can specify the size of the arcs in this box.

* **Angle**  
  Select the degree for the angle of the arcs. If you select "Customized", Designer displays the [Customize Gauge Angle dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096061-Customize-Gauge-Angle-Dialog-Box) for you to customize the angle.
* **Thickness**  
  Specify the thickness of the arcs, in pixels.
* **Hole Size**  
  Specify the relative size of an arc in a percentage of the total arc size.
* **Start Style**  
  Select the style for the start graph of the arcs: square, round, or long round.
* **End Style**   
  Select the style for the end graph of the arcs: square, round, or long round.

**Fill**

You can specify the color pattern of the arcs in this box.

* **Color**  
  Specify the color of the arcs. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Color List**  
  Select to open the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500010058302-Color-List-Dialog-Box) dialog to modify the color pattern for arcs in the same data series respectively.
* **Transparency**  
  Specify the transparency for the color of the arcs.
* **Self Settings**  
  Select to apply the color pattern to the arcs themselves. If you do not select the option, Designer synchronizes the color settings you define here to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#Pattern) on the chart object in the Report Inspector, which the data markers of other subtypes can also apply if the chart is a combo chart.
* **Background**  
  Specify the background color of the arcs.
* **Use Range Color**  
  Select to use the colors that you define for the ranges in the [Range Color tab](#Range) for the arcs.

**Border**

You can specify the properties for the border of the arcs in this box.

* **Line Style**  
  Select the line style of the border.
* **Thickness**  
  Specify the thickness of the border, in pixels.
* **Color**  
  Specify the color of the border. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Transparency**  
  Specify the transparency for the color of the border.
* **End Caps**  
  Select the ending style of the border line.
  + **butt**  
    Select to end unclosed sub paths and dash segments with no added decoration.
  + **round**  
    Select to end unclosed sub paths and dash segments with a round decoration that has a radius equal to half of the width of the pen.
  + **square**  
    Select to end unclosed sub paths and dash segments with a square projection that extends beyond the end of the segment to a distance equal to half of the line width.
* **Line Joint**  
  Select the joint style of the border line.
  + **miter**  
    Select to join path segments by extending their outside edges until they meet.
  + **round**  
    Select to join path segments by rounding off the corner at a radius of half the line width.
  + **bevel**  
    Select to join path segments by connecting the outer corners of their wide outlines with a straight segment.
  + **joint round**  
    Select to join path segments by rounding off the corner at the specified radius.

**Sample**

The box displays a preview sample of your selection.

## Axis Tab

You see the following sub tabs in the Axis tab:

* [Axis Sub Tab](#Axis1)
* [Tick Mark Sub Tab](#TickMark)
* [Label Sub Tab](#Label)
* [Format Sub Tab](#Format)

### Axis Sub Tab

Use this sub tab to specify the properties of the axis in the solid gauge.

![Format Solid Gauge dialog box - Axis - Axis](https://devnet.logianalytics.com/hc/article_attachments/4404856933271/fmtsldgauge_axis_axis1.gif)

**Show Axis**

Select to show the axis in the solid gauge.

**Type**

You can specify the position relationship of the axis and the arcs in this box.

* **Inside**  
  Select to display the axis inside the arcs.
* **Outside**  
  Select to display the axis outside the arcs.
* **Center**  
  Select to display the axis in the center of the arcs.

**Option**

You can specify the values to display on the axis in this box.

* **Minimum Value**  
  Specify the minimum value to display on the axis. You can select the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif) to [use a formula to control the value](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties).
* **Maximum Value**  
  Specify the maximum value to display on the axis. You can select the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif) to [use a formula to control the value](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties).

**Line**

You can specify the properties of the axis line in this box.

* **Color**  
  Specify the color of the line. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Style**  
  Select the style of the line.
* **Transparency**  
  Specify the transparency for the color of the line.
* **Thickness**  
  Specify the thickness of the line.
* **Use Range Color**  
  Select to use the colors that you define for the ranges in the [Range Color tab](#Range) for the line.

**Gap**

* **Circular Axis Gap**  
  Specify the gap between the axis and the arc if the axis displays inside or outside the arcs.

### Tick Mark Sub Tab

Use this sub tab to specify the properties of the tick marks on the axis.

![Format Solid Gauge dialog box - Axis - Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4404856933527/fmtsldgauge_axis_tkmk.gif)

**Type**

You can specify the position relationship of the axis and the tick marks in this box.

* **None**  
  Select if you do not want to display tick marks on the axis. It is meaningless to specify all the other tick mark properties if you select this type.
* **Top**  
  Select to display the tick marks on the top of the axis.
* **Bottom**  
  Select to display the tick marks on the bottom of the axis.
* **Center**  
  Select to display the tick marks in the center of the axis.

**Major Tick Mark Line**

You can specify the line properties of the major tick marks in this box.

* **Correlate with Axis**  
  Select to apply the [line properties](#Line) that you define for the axis in the Axis sub tab to the major tick marks. If you clear the option, you can specify the line properties for the major tick marks separately using the following options:
  + **Color**  
    Specify the color of the major tick mark line. Designer disables the option if you select [Use Range Color](#UseRangeColor) in the Axis sub tab.

    To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
  + **Style**  
    Select the style of the major tick mark line.
  + **Transparency**  
    Specify the transparency for the color of the major tick mark line. Designer disables the option if you select Use Range Color in the Axis sub tab.
  + **Thickness**  
    Specify the thickness of the major tick mark line.
* **Increment**  
  Specify the distance between two adjacent major tick marks on the axis.
* **Number of Tick Marks**  
  Specify how many major tick marks you want to display on the axis.
* **Tick Mark Length**  
  Specify the length of the major tick mark line.

**Minor Tick Mark Line**

You can specify the properties of the minor tick marks in this box.

* **Correlate with Axis**  
  Select to apply the [line properties](#Line) that you define for the axis in the Axis sub tab to the minor tick marks. If you clear the option, you can specify the line properties for the minor tick marks separately using the following options:  
  + **Color**  
    Specify the color of the major tick mark line. Designer disables the option if you select [Use Range Color](#UseRangeColor) in the Axis sub tab.

    To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
  + **Style**  
    Select the style of the minor tick mark line.
  + **Transparency**  
    Specify the color transparency of the minor tick mark line. Designer disables the option if you select Use Range Color in the Axis sub tab.
  + **Thickness**  
    Specify the thickness of the minor tick mark line.
* **Increment**  
  Specify the distance between two adjacent minor tick marks on the axis.
* **Number of Tick Marks**  
  Specify how many minor tick marks you want to display on the axis.
* **Tick Mark Length**  
  Specify the length of the minor tick mark line.

**Sample**

The box displays a preview sample of your selection.

### Label Sub Tab

Use this sub tab to specify the properties of the major tick mark labels.

![Format Solid Gauge dialog box - Axis - Label](https://devnet.logianalytics.com/hc/article_attachments/4404856933783/fmtsldgauge_axis_lbl.gif)

**Type**

You can specify in which manner to display the major tick mark labels in this box.

* **None**  
  Select if you do not want to display labels for the major tick marks.
* **Normal**  
  Select it and you can specify how to display the labels using the following options:
  + **Label Every N Major Tick Marks**  
    Specify the frequency at which to label the major tick marks.
  + **Number of Major Labels**  
    Specify how many major tick mark labels you want to display on the axis.
    - **Auto**  
      Select to display all the major tick mark labels.
    - **Fixed**  
      Select it and you can specify the number of the major tick mark labels you want to display on the axis.
* **Range Value**  
  Select to show the [range values](#Range) that you define in the Range Color tab as the labels.
* **Min and Max Values**  
  Select to show the [minimum value and maximum value](#AxisValue) that you define in the Axis sub tab as the labels.

**Gap**

You can specify the gap properties for the major tick mark labels in this box.

* **Label Axis Gap**  
  Specify the distance between the labels and the axis, in pixels.
* **Best Effect**  
  Select to adjust the labels automatically so as to place them in the best way. If you select the option, Designer hides some labels when they overlap.

**Font**

You can specify the font format of the text in the major tick mark labels in this box.

* **Font list**  
  The drop-down list contains all the font faces that you can select to apply to the text.
* **Font Size**  
  Specify the font size of the text.
* **Font Color**  
  Specify the font color of the text. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Transparency**  
  Specify the color transparency of the text.
* **Rotation**  
  Specify the rotation angle of the text around its center, in degrees. The default value is 0.
* **Shearing**  
  Specify the gradient of the text.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) Designer disables the Font Color and Transparency options if you select [Use Range Color](#UseRangeColor) in the Axis sub tab.

**Effects**

You can specify the special effects of the text in the tick mark labels in this box.

* **Style**  
  Select the font style of the text. It can be one of the following: plain, bold, italic, and bold italic.
* **Strikethrough**  
  Select the style of the horizontal line using which to strikethrough the text. It can be one of the following: none, thin line, bold line, and double lines.
* **Underline**  
  Select the style of the horizontal line under the text. It can be one of the following: none, single, single lower, bold line, bold lower, double lines, bold double, patterned line, and bold patterned. When you select "patterned line" or "bold patterned", Designer draws a line or bold line in the pattern of the text.

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4404856819991/criticalicon.gif) Web Report Studio and JDashboard do not support underlining chart text, therefore, Logi Report Engine ignores this property when the chart runs in Web Report Studio or is used in a dashboard.

* **Superscript**  
  Select to raise the text above the baseline and change the text to a smaller font size, if a smaller size is available.
* **Embossed**  
  Select to make the text appear to be raised off the page in relief.
* **Outlined**  
  Select to display the inner and outer borders of each character.
* **Subscript**  
  Select to lower the text below the baseline and change the text to a smaller font size, if a smaller size is available.
* **Engraved**  
  Select to make the text appear to be imprinted or pressed into the page.
* **Shadowed**  
  Select to add a shadow beneath and to the right of the text.

**Sample**

The box displays a preview sample of your selection.

### Format Sub Tab

Use this sub tab to specify the data format of the major tick mark labels.

![Format Solid Gauge dialog box - Axis - Format](https://devnet.logianalytics.com/hc/article_attachments/4404856934167/fmtsldgauge_axis_fmt.gif)

**Category & Format**

The two boxes list the [category types and the formats of each category](https://devnet.logianalytics.com/hc/en-us/articles/1500010096081-Data-Format-Dialog-Box#DataFormat) that Designer provides by default. Select a category and a format for this category, then select Add to add it as the format of the category. You can add only one format for each category.

**Properties**

The text box shows the properties of the format that you select in the Format box. If the default formats Designer provides for a category cannot meet your requirement, you can define your own format in the text box and select Add to add it as the format of the category.

**Auto Scale in Number**

Specify whether to automatically scale the Number values which fall into the following two ranges:

* When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.

By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property [on the chart in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#AutoScale) for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.

**Sample**

The box displays a sample for the selected format.

**Stack**

The box lists all the formats that you select from different categories.

**Add**

Select to add a format to the Stack box.

**Remove**

Select to remove the specified format from the Stack box.

**Apply**

Select to apply the specified format to the major tick mark labels.

## Pointer Tab

Use this tab to specify the properties of the pointers in the solid gauge.

![Format Solid Gauge dialog box - Pointer](https://devnet.logianalytics.com/hc/article_attachments/4404856934679/fmtsldgauge_pnt.gif)

**Pointer Style**

You can specify the style of the pointers in this box.

* **Arrow**  
  Select to use arrow for the pointers.
  + **Value Pointer**  
    Select the style of the arrow. You can select "Customized" from the drop-down list to specify an image as the pointer.
  + **Width**  
    Specify the width of the arrow.
  + **Height**  
    Specify the height of the arrow.
* **Mark**  
  Select to use mark for the pointers.
  + **Value Pointer**  
    Select the style of the mark. You can select "Customized" from the drop-down list to specify an image as the pointer.
  + **Width**  
    Specify the width of the mark.
  + **Height**  
    Specify the height of the mark.
  + **Position**  
    Select the position of the pointers relative to the arcs: top, bottom, or center.
  + **Gap**  
    Specify the distance between the pointers and the arcs, in pixels.

* **Style List**  
  Select to open the [Style List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098941-Style-List-Dialog-Box) to specify the style for pointers in the same data series respectively.

**Pointer Color**

You can specify the color properties of the pointers in this box.

* **Color**  
  Specify the color of the pointers. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Color List**   
  Select to open the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058302-Color-List-Dialog-Box) to modify the color pattern for pointers in the same data series respectively.
* **Transparency**  
  Specify the transparency for the color of the pointers.
* **Self Settings**  
  Select to apply the color pattern to the pointers themselves. If you do not select the option, Designer synchronizes the color settings you define here to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#Pattern) on the chart object in the Report Inspector, which the data markers of other subtypes can also apply if the chart is a combo chart.
* **Use Range Color**  
  Select to use the colors that you define for the ranges in the [Range Color tab](#Range) for the pointers.

**Pointer Value**

You can specify the properties of the pointer values in this box.

* **Show Pointer Value**  
  Select to show values for the pointers.
* **Position**  
  Select the position of the values relative to the pointers: top, bottom, center, on pointer, or customized. If you select "customized", you can customize the position by dragging any pointer value in the design area.

**Pointer Border**

You can specify the properties for the border of the pointers in this box.

* **Show Pointer Border**  
  Select to show the border of the pointers.
* **Line Style**  
  Select the line style to apply to the border.
* **Thickness**  
  Specify the weight of the border, in pixels.
* **Color**  
  Specify the color of the border. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Transparency**  
  Specify the transparency for the color of the border.

**Sample**

The box displays a preview sample of your selection.

## Target Tab

Use this tab to specify the properties of the target in the solid gauge.

![Format Solid Gauge dialog box - Target](https://devnet.logianalytics.com/hc/article_attachments/4404848539031/fmtsldgauge_tgt.gif)

**Use Target Value**

Select to use target value for the solid gauge.

* **Target Value**  
  Specify the target value. You can select the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif) to [use a formula to control the value](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties).

**Pointer Style**

You can specify the pointer style for the target value in this box.

* **Target Pointer**  
  Select the style of the target pointer. You can select "Customized" from the drop-down list to specify an image as the target pointer.
* **Width**  
  Specify the width of the target pointer.
* **Height**  
  Specify the height of the target pointer.
* **Position**  
  Select the position of the target pointer relative to the arcs: top, bottom, or center.
* **Gap**  
  Specify the distance between the target pointer and the arcs.

**Pointer Color**

You can specify the color properties of the target pointer in this box.

* **Color**  
  Specify the color of the target pointer. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Transparency**  
  Specify the transparency for the color of the target pointer.

**Target Value**

You can specify the properties of the target value in this box.

* **Show Target Value**  
  Select to show the target value on the solid gauge.
* **Position**  
  Select the position of the target value relative to the arcs: top, bottom, center, on pointer, or customized. If you select "customized", you can customize the position by dragging the target value in the design area.

**Sample**

The box displays a preview sample of your selection.

## Frame Tab

Use this tab to specify the properties for the frame of the solid gauge.

![Format Solid Gauge dialog box - Frame](https://devnet.logianalytics.com/hc/article_attachments/4404856935191/fmtsldgauge_frm.gif)

**Size**

You can specify the size properties of the frame in this box.

* **Frame Size**  
  Specify the size of the frame.

**Fill**

You can specify the color and transparency of the frame in this box.

* **Fill**  
  Specify the color to fill the frame. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Transparency**  
  Specify the transparency of the color to fill the frame.

**Border**

You can specify the properties for the border of the frame in this box.

* **Border Type**  
  Select the type of the border.
  + **none**  
    Select if you do not want to show the border.
  + **raised**  
    Select to show 3-D border which appears as if it is raised off the page.
  + **recess**  
    Select to show 3-D border which appears as if it is pressed into the page.
  + **shadow**  
    Select to show two shadowed borders, beneath and to the right of the object.
  + **solid**  
    Select to use single-line border.
* **Color**  
  Specify the color of the border. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Line Style**  
  Select the line style of the border.
* **Transparency**  
  Specify the transparency for color of the border.
* **Thickness**  
  Specify the thickness of the border, in pixels.
* **End Caps**  
  Select the ending style of the border line.
  + **butt**  
    Select to end unclosed sub paths and dash segments with no added decoration.
  + **round**  
    Select to end unclosed sub paths and dash segments with a round decoration that has a radius equal to half of the width of the pen.
  + **square**  
    Select to end unclosed sub paths and dash segments with a square projection that extends beyond the end of the segment to a distance equal to half of the line width.
* **Line Joint**  
  Select the joint style of the border line.
  + **miter**  
    Select to join path segments by extending their outside edges until they meet.
  + **round**  
    Select to join path segments by rounding off the corner at a radius of half the line width.
  + **bevel**  
    Select to join path segments by connecting the outer corners of their wide outlines with a straight segment.
  + **joint round**  
    Select to join path segments by rounding off the corner at the specified radius.
* **Path**  
  Specify the fill pattern of the border.
  + **Outline Path**  
    Select to use outline path for the border.
  + **Fill Path**  
    Select to use whole path for the border.
* **Dash**  
  Specify the dash size of the border if you select a dash line style for the border.
  + **Auto Adjust Dash**  
    Select to adjust the dash size automatically.
  + **Fixed Dash Size**  
    Select to use fixed dash size.

**Gauge Group Name**

You can specify the properties for the gauge group names in this box.

* **Show Gauge Group Name**  
  Select to show names for the arcs in the solid gauge which are values of the field on the category axis. If the solid gauge contains no category field, the group name shows "Report" by default.
* **Position**  
  Select the position of the names relative to the arcs: top, bottom, center, or customized. If you select "customized", you can customize the position by dragging any name in the design area.

**Sample**

The box displays a preview sample of your selection.

## Range Color Tab

Use this tab to specify the value ranges for the solid gauge and the color and name of each range.

![Format Solid Gauge dialog box - Range Color](https://devnet.logianalytics.com/hc/article_attachments/4404856935447/fmtsldgauge_rgclr.gif)

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**

Select to add a new range.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**

Select to delete the specified range.

**Minimum**

The column shows the minimum values that you specify for the ranges.

**Maximum**

The column shows the maximum values that you specify for the ranges.

**Color**

The column shows the colors that you specify for the ranges. To edit the color, select in the cell and customize the color in the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette).

**Name**

The column shows the names that you specify for the ranges.

**Others**

You can specify the properties for values that do not fall into any of the ranges you define in this box.

* **Name**  
  Specify the name for the values.
* **Color**  
  Specify the color for the values. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.

## Hint Tab

Use this tab to specify the properties for the hint of the solid gauge.

![Format Solid Gauge dialog box - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404856935703/fmtsldgauge_hint.gif)

**Show Category and Series**

Select to include the category and series values in the hint.

**Auto Scale in Number**

Specify whether to automatically scale the Number values in the hint which fall into the following two ranges:

* When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.

By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property [on the chart in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#AutoScale) for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.

* When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.

By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property [on the chart in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#AutoScale) for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.

## Behaviors Tab

Designer displays the Behaviors tab only when the solid gauge chart is in a library component. You can use it to specify web behaviors to the solid gauge.

![Format Solid Gauge dialog box - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404848539287/fmtsldgauge_bhvr.gif)

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**

Select to add a new web behavior line.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**

Select to delete the specified web behavior.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Up button**

Select to move the specified web behavior higher in the list. At runtime, when an event bound with more than one action happens, JDashboard triggers the upper action first.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Down button**

Select to move the specified web behavior lower in the list.

**Events**

The column shows the events that you select to trigger the web actions.

**Actions**

The column shows the actions that you specify for the events to trigger. To bind a web action to an event, select the ellipsis button ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif) in the action cell and Designer displays the [Web Action List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060822-Web-Action-List-Dialog-Box) for you to specify the web action.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010097241-Format-Series-Z-Gridline-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010097281-Format-Stock-Dialog-Box)
