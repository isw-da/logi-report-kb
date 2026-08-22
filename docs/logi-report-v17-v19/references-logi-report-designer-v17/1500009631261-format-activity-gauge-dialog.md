---
title: "Format Activity Gauge Dialog"
id: 1500009631261
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009631261-Format-Activity-Gauge-Dialog
updated_at: 2021-07-24T16:04:38Z
---

# Format Activity Gauge Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009631181-Flash-Parameter-dialog-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009608322-Format-Area-Dialog)

# Format Activity Gauge Dialog

The Format Activity Gauge dialog helps you to [format an activity gauge](https://devnet.logianalytics.com/hc/en-us/articles/1500009628601-Formatting-the-Gauge-in-a-Gauge-Chart#Activity). It appears when you right-click on an activity gauge chart and select Format Activity Gauge from the shortcut menu.

The dialog contains the following tabs: [Circular Graph](#Circular), [Pointer](#Pointer), [Target](#Target), [Frame](#Frame), [Range Color](#Range), [Hint](#Hint) and [Behaviors](#Behaviors) (the Behaviors tab is available to charts in library components only).

**Sample**

Displays a preview sample of your selection.

**OK**

Applies the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Apply**

Applies all changes and leaves the dialog open.

**Help**

Displays the help document about this feature.

## Circular Graph

Specifies properties for the circles in the activity gauge.

![Format Activity Gauge dialog - Circular Graph](https://devnet.logianalytics.com/hc/article_attachments/4404904338711/fmtactvtygauge_crculr.gif)

**Size**

Specifies the size of the circles.

* **Hole Size**  
  Specifies the relative size of a circle in a percentage of total circle size.
* **Circular Gap**  
  Specifies the distance between the circles.
* **Start Style**  
  Specifies the style for the start graph of the circles.
* **End Style**  
  Specifies the style for the end graph of the circles.
* **Start Mark**  
  Specifies the mark for the start graph of the circles.
* **Stop Mark**  
  Specifies the mark for the stop graph of the circles.

**Fill**

Specifies the color of the circles.

* **Color**  
  Specifies the color of the circles.
* **Color List**  
   Opens the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009630161-Color-List-Dialog) dialog to modify the color pattern for each circle.
* **Transparency**  
  Specifies the transparency for color of the circles.
* **Self Settings**  
  Specifies whether to edit the color pattern for the circles themselves. When the option is unselected, the color settings defined here will be synchronized to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#Pattern) on the chart object in the Report Inspector, which can also be applied by data markers of other subtypes if the chart is a combo chart.
* **Background**  
  Specifies the background color of the circles.
  + **Auto**  
    Specifies to use colors that are lighter than the circles automatically. The Background option is disabled when Auto is selected.
* **Use Range Color**  
  Specifies whether to use the color you defined for the ranges as the color of the circles. If the option is selected, the Color, Color List and Transparency options will be disabled.

**Value**

Specifies the values to be displayed in the chart.

* **Minimum**  
  Specifies the minimum value to be displayed in the chart. You can also [use a formula to control the property](https://devnet.logianalytics.com/hc/en-us/articles/1500009634221-Using-Formulas-to-Control-Object-Properties).
* **Maximum**  
  Specifies the maximum value to be displayed in the chart. You can also [use a formula to control the property](https://devnet.logianalytics.com/hc/en-us/articles/1500009634221-Using-Formulas-to-Control-Object-Properties).

## Pointer

Specifies properties for the pointers in the activity gauge.

![Format Activity Gauge dialog - Pointer](https://devnet.logianalytics.com/hc/article_attachments/4404916804119/fmtactvtygauge_pnt.gif)

**Pointer Value**

Specifies the pointer value properties.

* **Show Pointer Value**  
  Specifies whether to show the pointer values.
  + **Position**  
     Specifies the position relationship of the value and the pointers. Select the position from the drop-down list or select customized to customize the position by dragging any pointer value in the design area.

## Target

Specifies properties of the target in the activity gauge.

![Format Activity Gauge dialog - Target](https://devnet.logianalytics.com/hc/article_attachments/4404916804375/fmtactvtygauge_tgt.gif)

**Use Target Value**

Specifies whether to use the target value for the activity gauge.

* **Target Value**   
   Specifies the value of the target. You can also [use a formula to control the value](https://devnet.logianalytics.com/hc/en-us/articles/1500009634221-Using-Formulas-to-Control-Object-Properties).

**Target Value**

Specifies properties of the target value.

* **Show Target Value**  
   Specifies whether to show the target value on the activity gauge.
  + **Position**  
     Specifies the position of the target value relative to the circle. Select the position from the drop-down list or select customized to customize the position by dragging the target value in the design area.

## Frame

Specifies properties for the frame of the activity gauge chart.

![Format Activity Gauge dialog - Frame](https://devnet.logianalytics.com/hc/article_attachments/4404916804631/fmtactvtygauge_frm.gif)

**Size**

Specifies the size properties of the frame.

* **Frame Size**  
  Specifies the size of the frame.

**Fill**

Specifies the color and transparency of the frame.

* **Fill**  
  Specifies the color to fill the frame.
* **Transparency**  
  Specifies the transparency to fill the frame.

**Border**

Specifies properties for border of the frame.

* **Border Type**  
   Displays the type of the border.
* **Color**  
  Specifies the color of the border. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Line Style**  
  Specifies the line style to apply to the border.
* **Transparency**  
  Specifies the transparency for color of the border.
* **Thickness**  
  Specifies the thickness of the border, in pixels.
* **End Caps**  
  Specifies the ending style of the border line.

+ **butt**  
   Ends unclosed sub paths and dash segments with no added decoration.
+ **round**  
  Ends unclosed sub paths and dash segments with a round decoration that has a radius equal to half of the width of the pen.
+ **square**  
   Ends unclosed sub paths and dash segments with a square projection that extends beyond the end of the segment to a distance equal to half of the line width.

* **Line Joint**  
  Specifies the line joint style for the border line.
  + **miter**  
    Joins path segments by extending their outside edges until they meet.
  + **round**  
    Joins path segments by rounding off the corner at a radius of half the line width.
  + **bevel**  
     Joins path segments by connecting the outer corners of their wide outlines with a straight segment.
  + **joint round**  
    Joins path segments by rounding off the corner at the specified radius.
* **Path**  
  Specifies the fill pattern of the border line.

  + **Outline Path**  
    Specifies the fill pattern of the border line to be outline path.
  + **Fill Path**  
    Specifies the fill pattern of the border line to be whole path.
* **Dash**  
  Specifies the dash size of border line.
  + **Auto Adjust Dash**  
     If selected, the dash size will be adjusted automatically.
  + **Fixed Dash Size**  
    If selected, the dash size will be fixed size.

**Gauge Group Name**

Specifies properties for the gauge group name.

* **Show Gauge Group Name**   
  Specifies whether to show names for the circles in the activity gauge which are values of the field on its category axis. If the activity gauge contains no category field, the group name shows Report by default.
  + **Position**  
    Specifies the position of the names relative to the circles.

## Range Color

Specifies different colors to fill the circles in different ranges.

![Format Activity Gauge dialog - Range Color](https://devnet.logianalytics.com/hc/article_attachments/4404904339095/fmtactvtygauge_rgclr.gif)

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif)

Adds a new color range.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif)

Removes the selected color range.

**Minimum**

Specifies the minimum value of the range.

**Maximum**

Specifies the maximum value of the range.

**Color**

Specifies the color schema of the range. Select in the color cell to customize the color on the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette).

**Name**

Displays the name of the range.

**Others**

Specifies the properties for values that do not fall into any of the ranges you define.

* **Name**  
  Specifies the name for the values.
* **Color**  
   Specifies the color for the values. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.

## Hint

Specifies properties for the hint of the activity gauge.

![Format Activity Gauge dialog - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404904339351/fmtactvtygauge_hint.gif)

**Show Category and Series**

Specifies whether to include the category and series values in the hint.

**Auto Scale in Number**

Specifies whether to automatically scale the values displayed in the hint that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

The option "auto" means that the property setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#AutoScale).

## Behaviors

Specifies web behaviors to the activity gauge. This tab is only available to charts in library components.

![Format Activity Gauge dialog - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404904339607/fmtactvtygauge_bhvr.gif)

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif)

Adds a new web behavior line.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif)

Removes the selected web behavior.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif)

Moves the selected web behavior up a step.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif)

Moves the selected web behavior down a step.

**Events**

Specifies the trigger event.

**Actions**

Specifies the action you want the event to trigger.

* ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif)  
   Opens the [Web Action List](https://devnet.logianalytics.com/hc/en-us/articles/1500009633961-Web-Action-List-Dialog) dialog to bind a web action to the event.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009631181-Flash-Parameter-dialog-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009608322-Format-Area-Dialog)
