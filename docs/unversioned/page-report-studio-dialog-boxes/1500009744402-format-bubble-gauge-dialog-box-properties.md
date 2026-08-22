---
title: "Format Bubble Gauge Dialog Box Properties"
id: 1500009744402
section: "Page Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009744402-Format-Bubble-Gauge-Dialog-Box-Properties
updated_at: 2021-07-24T00:49:15Z
---

# Format Bubble Gauge Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009772261-Format-Bench-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009772281-Format-Category-X-Axis-Dialog-Box-Properties)

# Format Bubble Gauge Dialog Box Properties

You can use the Format Bubble Gauge dialog box to format a bubble gauge chart. This topic describes the options in the dialog box.

This topic contains the following sections:

* [Staff Graph Tab Properties](#Staff)
* [Frame Tab Properties](#Frame)
* [Range Color Tab Properties](#Range)
* [Hint Tab Properties](#Hint)

**OK**

Applies the changes and closes the dialog box.

**Cancel**

Does not retain any changes and closes the dialog box.

**Help**

Displays the help document about this feature.

## Staff Graph Tab Properties

Specifies properties for bubbles in the bubble gauge.

![Format Bubble Gauge dialog - Staff Graph](https://devnet.logianalytics.com/hc/article_attachments/4404880532503/fmtbublgauge_stfgraph.gif)

**Bubbles**

Specifies properties of the bubbles.

* **Left Margin**  
   Specifies the gap between the left labels and left bubbles, in inches.
* **Top Margin**  
   Specifies the gap between top labels and top bubbles, in inches.
* **Range Radius**  
   Specifies the relative size of a bubble in a percentage of total bubble size.
* **Draw Category (X) Grid**  
   Specifies whether to draw category grid.
* **Draw Series (Z) Grid**  
   Specifies whether to draw series grid.

**Border**

Specifies the properties for border of the bubbles.

* **Show Border**Specifies whether to show the border of the bubbles. When the option is selected, the following border properties are enabled.

  + **Line Style**  
     Specifies the line style to apply to the border.
  + **Color**  
    Specifies the color of the border.
  + **Thickness**  
     Specifies the thickness of the border, in inches.
  + **Transparency**  
     Specifies the transparency for color of the border.

**Value**

Specifies the minimum and maximum values for the color range. The values are equally divided into three ranges, each of which is filled with the color you specify in the Range Color tab automatically. Applied only when you do not specify ranges for the values in the Range Color tab.

* **Minimum Value**  
   Specifies the minimum value to be displayed in the chart.
* **Maximum Value**  
   Specifies the maximum value to be displayed in the chart.

## Frame Tab Properties

Specifies properties for the frame of the bubble gauge chart.

![Format Bubble Gauge dialog - Frame](https://devnet.logianalytics.com/hc/article_attachments/4404885587863/fmtbublgauge_frm.gif)

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

Specifies the properties for border of the frame.

* **Line Style**  
  Specifies the line style to apply to the border.
* **Border Type**  
   Specifies the type of the border.
* **Color**  
   Specifies the color of the border. To change the color, select the color indicator to specify a new color in the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009745022-Select-Color-Dialog-Box-Properties) dialog box, or type a color string in the format #RRGGBB. If you want to make the background transparent, type Transparent in the text box.
* **Transparency**  
   Specifies the transparency for color of the border.
* **Thickness**  
   Specifies the thickness of the border, in inches.

**Gauge Group Name**

Specifies properties for the gauge group name.

* **Show Gauge Group Name**   
   Specifies whether to show names for the bubbles in the bubble gauge which are values of the field on its category axis. If the bubble gauge contains no category field, the group name shows Report by default.
  + **Position**  
     Specifies the position of the names relative to the bubbles. Select the position from the drop-down list. If customized is selected, the X and Y settings in the General tab of the [Format Gauge Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009772321-Format-Gauge-Label-Dialog-Box-Properties#General) dialog box will take effect.

## Range Color Tab Properties

Specifies different colors to fill the bubbles in bubble gauge in different ranges.

![Format Bubble Gauge dialog - Range Color](https://devnet.logianalytics.com/hc/article_attachments/4404885588119/fmtbublgauge_rgclr.gif)

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404880163351/btn_add1.gif)

Adds a new color range.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404885309335/btn_delete.gif)

Removes the selected color range.

**Minimum**

Specifies the minimum value of the range.

**Maximum**

Specifies the maximum value of the range.

**Color**

Specifies the color schema of the range. Select in the color cell to specify a new color in the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009745022-Select-Color-Dialog-Box-Properties) dialog box.

**Name**

Displays the name of the range.

**Others**

Specifies the properties for values that do not fall into any of the ranges you define.

* **Name**  
   Specifies the name for the values.
* **Color**  
   Specifies the color for the values. To change the color, select the color indicator to specify a new color in the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009745022-Select-Color-Dialog-Box-Properties) dialog box, or type a color string in the format #RRGGBB. If you want to make the background transparent, type Transparent in the text box.

## Hint Tab Properties

Specifies properties of the data marker hint.

![Format Bubble Gauge dialog - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404880533143/fmtbublgauge_hint.gif)

**Show Category and Series**

Specifies whether to include the category and series values in the data marker hint.

**Auto Scale in Number**

Specifies whether to
automatically scale the values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

The default value **auto** means that the setting follows [that of the chart platform](https://devnet.logianalytics.com/hc/en-us/articles/1500009772421-Format-Platform-Dialog-Box-Properties#AutoScale).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009772261-Format-Bench-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009772281-Format-Category-X-Axis-Dialog-Box-Properties)
