---
title: "Format Bubble Gauge Dialog"
id: 1500010066301
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010066301-Format-Bubble-Gauge-Dialog
updated_at: 2021-07-24T10:38:50Z
---

# Format Bubble Gauge Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010066281-Format-Bubble-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010030882-Format-Bullet-Dialog)

# Format Bubble Gauge Dialog

The Format Bubble Gauge dialog helps you to [format a bubble gauge](https://devnet.logianalytics.com/hc/en-us/articles/1500010028842-Formatting-the-Gauge-in-a-Gauge-Chart#Bubble). It appears when you right-click any bubble in a bubble gauge chart and then select Format Bubble Gauge from the shortcut menu.

The dialog contains the following tabs: [Staff Graph](#Staff), [Frame](#Frame), [Range Color](#Range), [Hint](#Hint) and [Behaviors](#Behaviors) (the Behaviors tab is available to charts in library components only).

**OK**

Applies the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Apply**

Applies all changes and leaves the dialog open.

**Help**

Displays the help document about this feature.

## Staff Graph

Specifies properties for the bubbles in the bubble gauge.

![Format Bubble Gauge dialog - Staff Graph](https://devnet.logianalytics.com/hc/article_attachments/4404909216279/fmtbublgauge_stfgraph.gif)

**Bubbles**

Specifies properties of the bubbles.

* **Left Margin**  
   Specifies the gap between the left labels and left bubbles, in pixels.
* **Top Margin**  
   Specifies the gap between top labels and top bubbles, in pixels.
* **Range Radius**  
   Specifies the relative size of a bubble in a percentage of total bubble size.
* **Draw Category (X) Grid**  
   Specifies whether to draw category grid.
* **Draw Series (Z) Grid**  
   Specifies whether to draw series grid.

**Border**

Specifies properties for the border of the bubbles.

* **Show Border**Specifies whether to show the border of the bubbles. When it is checked, the other border properties will be enabled.

  + **Line Style**  
     Specifies the line style to apply to the border.
  + **Thickness**  
     Specifies the thickness of the border, in pixels.
  + **Color**  
     Specifies the color of the border.
  + **Transparency**  
     Specifies the transparency for color of the border.

**Value**

Specifies the minimum and maximum values for the color range. The values are equally divided into three ranges, each of which is filled with the color you specify in the Range Color tab automatically. Applied only when you do not specify ranges for the values in the Range Color tab.

* **Minimum**  
   Specifies the minimum value to be displayed in the chart. You can also [use a formula to control the property](https://devnet.logianalytics.com/hc/en-us/articles/1500010033202-Using-Formulas-to-Control-Object-Properties).
* **Maximum**  
   Specifies the maximum value to be displayed in the chart. You can also [use a formula to control the property](https://devnet.logianalytics.com/hc/en-us/articles/1500010033202-Using-Formulas-to-Control-Object-Properties).

## Frame

Specifies properties for the frame of the bubble gauge.

![Format Bubble Gauge dialog - Frame](https://devnet.logianalytics.com/hc/article_attachments/4404901252759/fmtbublgauge_frm.gif)

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

Specifies the properties for border of the frame.

* **Border Type**  
   Displays the type of the border.
* **Color**  
   Specifies the color of the border. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010035022-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color directly in the text box.
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
   Specifies whether to show names for the bubbles in the bubble gauge which are values of the field on its category axis. If the bubble gauge contains no category field, the group name shows Report by default.
  + **Position**  
     Specifies the position of the names relative to the bubbles.

## Range Color

Specifies different colors to fill the bubbles in different ranges.

![Format Bubble Gauge dialog - Range Color](https://devnet.logianalytics.com/hc/article_attachments/4404901253015/fmtbublgauge_rgclr.gif)

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif)

Adds a new color range.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif)

Removes the selected color range.

**Minimum**

Specifies the minimum value of the range.

**Maximum**

Specifies the maximum value of the range.

**Color**

Specifies the color schema of the range. Select in the color cell to customize the color on the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010035022-Menu-Tabs#Palette).

**Name**

Displays the name of the range.

**Others**

Specifies the properties for values that do not fall into any of the ranges you defined.

* **Name**  
   Specifies the name for the values.
* **Color**  
   Specifies the color for the values. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010035022-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color directly in the text box.

## Hint

Specifies properties for the hint of the bubble gauge.

![Format Bubble Gauge dialog - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404901253271/fmtbublgauge_hint.gif)

**Show Category and Series**

Specifies whether to include the category and series values in the hint.

**Auto Scale in Number**

Specifies whether to automatically scale the values displayed in the hint that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

The option "auto" means that the property setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010069721-Chart-Properties#AutoScale).

## Behaviors

Specifies web behaviors to the bubble gauge. This tab is only available to charts in library components.

![Format Bubble Gauge dialog - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404901253527/fmtbublgauge_bhvr.gif)

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif)

Adds a new web behavior line.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif)

Removes the selected web behavior.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif)

Moves the selected web behavior up a step.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif)

Moves the selected web behavior down a step.

**Events**

Specifies the trigger event.

**Actions**

Specifies the action you want the event to trigger.

* ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404909121559/btn_chsr1.gif)  
   Opens the [Web Action List](https://devnet.logianalytics.com/hc/en-us/articles/1500010068321-Web-Action-List-Dialog) dialog to bind a web action to the event.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010066281-Format-Bubble-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010030882-Format-Bullet-Dialog)
