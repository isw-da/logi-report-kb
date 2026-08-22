---
title: "Format Indicator Dialog"
id: 1500009631401
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009631401-Format-Indicator-Dialog
updated_at: 2021-07-24T16:04:36Z
---

# Format Indicator Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009631381-Format-Gauge-Label-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009631421-Format-KPI-Label-Dialog)

# Format Indicator Dialog

The Format Indicator dialog helps you to [format the indicators in an indicator chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009605842-Formatting-the-Indicators-in-an-Indicator-Chart). It appears when you right-click an indicator in an indicator chart and select Format Indicator from the shortcut menu, or double-click an indicator of an indicator chart.

The dialog contains the following tabs: [General](#General), [Frame](#Frame), [Range Color](#Range), [Hint](#Hint) and [Behaviors](#Behaviors) (the Behaviors tab is available to charts in library components only).

**OK**

Applies the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Apply**

Applies all changes and leaves the dialog open.

**Help**

Displays the help document about this feature.

## General

Specifies the general properties of the indicators.

![Format Indicator - General](https://devnet.logianalytics.com/hc/article_attachments/4404916798359/fmtindctr_gnrl.gif)

**Style**

Specifies the style of the indicators.

* **Single**  
   Specifies to use an indicator to show each value.
* **Multiple**  
   Specifies to use multiple indicators to show each value.

**Option**

* **Left Margin**  
   Specifies the gap between the left labels and the left indicators, in pixels.
* **Top Margin**  
   Specifies the gap between the top labels and the top indicators, in pixels.
* **Range Radius**  
   Specifies the relative size of an indicator in a percentage of the total indicator size.
* **Style**  
   Specifies the shape of the indicator graph.
* **Fill Type**  
   Specifies how to fill the indicators. Not available when the value of the indicator chart is Boolean or String type.
  + **all**  
     Specifies to fill the whole indicator.
  + **base on max value**  
     Specifies to fill the portion of the indicators calculated based on the the [maximum value](#Value). When a value in the chart is less than the minimum value, the indicator will not be filled. When a value in the chart is greater than the minimum value, the value divided by the maximum value you specify will be the portion to be filled.

**Border**

Specifies properties for the border of the indicators.

* **Show Border**Specifies whether to show the border of the indicators. When it is selected, the other border properties will be enabled.

  + **Line Style**  
     Specifies the line style to apply to the border.
  + **Thickness**  
     Specifies the thickness of the border, in pixels.
  + **Color**  
     Specifies the color of the border.
  + **Transparency**  
     Specifies the transparency for color of the border.

**Value**

Specifies the maximum and minimum values displayed on the chart. The default value is Auto, which means using the actual minimum and maximum values in the chart. You can also specify the values by yourself. Not available when the value of the indicator chart is Boolean or String type.

**Value Label**

Specifies the values of the indicators.

* **Show Value**   
   Specifies whether to show the values of the indicators.
  + **Position**  
     Specifies the position relationship of the values and the indicators. Select the position from the drop-down list.
  + **Auto Scale in Number**  
    Specifies whether to automatically scale the values that are of the Number data type when the values fall into the two ranges:
    - When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
    - When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

    The option "auto" means that the property setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#AutoScale).

**Sample**

Displays a preview sample of your selection.

## Frame

Specifies properties for the frame of the indicator chart.

![Format Indicator - Frame](https://devnet.logianalytics.com/hc/article_attachments/4404916798615/fmtindctr_frm.gif)

**Size**

Specifies the size properties of the frame.

* **Frame Size**   
   Specifies the size of the frame.

**Fill**

Specifies the color and transparency of the frame.

* **Fill**  
   Specifies the color to fill the frame.
* **Transparency**  
   Specifies the transparency of the color to fill the frame.

**Border**

Specifies the properties for borders of the frame.

* **Border Type**  
  Specifies the type of the border.
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
     Specifies to adjust the dash size automatically.
  + **Fixed Dash Size**  
     Specifies to use fixed dash size.

**Category Label**

Specifies properties for the category labels.

* **Show Category Label**  
   Specifies whether to show the category labels for the indicators. The label displays the category value each indicator represents.
  + **Position**  
    Specifies the position relationship of the labels and the indicators.

**Sample**

Displays a preview sample of your selection.

## Range Color

The options in the tab differ with value types of the indicator chart: [Boolean type](#Boolean), or [Numeric/String type](#Numeric).

### Range Color tab for Boolean type values

Specifies different colors or images to fill the indicators.

![Format Indicator - Range Color for Boolean type values](https://devnet.logianalytics.com/hc/article_attachments/4404904313623/fmtindctr_range_boln.gif)

**Show Image**

Specifies whether to use images instead of colors to represent the values. If the option is selected, you can select an image to represent a specified value, and the color setting in the Color column will be ignored.

**Value**

Lists the value for the indicator chart.

**Color**

Specifies the color schema for the value. Select in the color cell to customize the color on the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette).

**Image**

Specifies the image to represent the value.

**Name**

Specifies the name of the value.

### Range Color tab for Numeric/String type values

Specifies the general properties of the indicators.

![Format Indicator - Range Color for String/Numeric type values](https://devnet.logianalytics.com/hc/article_attachments/4404904313879/fmtindctr_range_num.gif)

**Show Image**

Specifies whether to use images instead of colors to represent the values. If the option is selected, you can select an image to represent a specified value, and the color setting in the Color column will be ignored.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif)

Adds a new value range.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif)

Removes the selected value range.

**Minimum**

Specifies the minimum value of the range.

**Maximum**

Specifies the maximum value of the range.

**Color**

Specifies the color schema for the value. Select in the color cell to customize the color on the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette).

**Image**

Specifies the image to represent the value.

**Name**

Specifies the name of the value.

**Others**

Specifies the properties for values that do not fall into any of the ranges you have defined.

* **Name**  
  Specifies the name for the values.
* **Color**  
  Specifies the color for the values. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Image**  
  Specifies the image to represent the values.

## Hint

Specifies properties for the hint of the indicators.

![Format Indicator - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404904314775/fmtindctr_hint.gif)

**Show Category and Series**

Specifies whether to include the category and series values in the hint.

**Auto Scale in Number**

Specifies whether to automatically scale the values displayed in the hint that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

The option "auto" means that the property setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#AutoScale).

## Behaviors

Specifies web behaviors to the indicators. This tab is only available to charts in library components.

![Format Indicator - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404904315927/fmtindctr_bhvr.gif)

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009631381-Format-Gauge-Label-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009631421-Format-KPI-Label-Dialog)
