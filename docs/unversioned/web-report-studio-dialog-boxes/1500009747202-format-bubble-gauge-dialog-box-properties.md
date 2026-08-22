---
title: "Format Bubble Gauge Dialog Box Properties"
id: 1500009747202
section: "Web Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009747202-Format-Bubble-Gauge-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:25Z
---

# Format Bubble Gauge Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009747182-Format-Bench-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009775441-Format-Category-X-Axis-Dialog-Box-Properties)

# Format Bubble Gauge Dialog Box Properties

This topic describes how you can use the Format Bubble Gauge dialog box to format the bubble gauges in a bubble gauge chart. Server displays the dialog box when you right-click on a bubble gauge chart and select **Format Graph** from the shortcut menu.

This topic contains the following sections:

* [Staff Graph Tab Properties](#Staff)
* [Frame Tab Properties](#Frame)
* [Range Color Tab Properties](#Range)
* [Hint Tab Properties](#Hint)

You see these elements on all the tabs:

**OK**

Select **OK** to apply any changes you made here.

**Cancel**

Select **Cancel** to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Select to view information about the Format Bubble Gauge dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Select to close the dialog box without saving any changes.

## Staff Graph Tab Properties

Specifies properties for bubbles in the bubble gauge.

![Format Bubble Gauge dialog - Staff Graph](https://devnet.logianalytics.com/hc/article_attachments/4404885479447/fmtbublgauge_stfgraph.gif)

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

Specifies properties for border of the bubbles.

* **Show Border**Specifies whether to show the border of the bubbles. When it is selected, the following border properties are enabled.

  + **Line Style**  
     Specifies the line style to apply to the border.
  + **Color**  
     Specifies the color of the border.
  + **Transparency**  
    Specifies the transparency for color of the border.
  + **Thickness**  
     Specifies the thickness of the border, in inches.

**Value**

Specifies the minimum and maximum values for the color range. The values are equally divided into three ranges, each of which is filled with the color you specify in the Range Color tab automatically. Applied only when you do not specify ranges for the values in the Range Color tab.

* **Minimum Value**  
   Specifies the minimum value to be displayed in the chart. You can also use a formula to control the property.
* **Maximum Value**  
   Specifies the maximum value to be displayed in the chart. You can also use a formula to control the property.

## Frame Tab Properties

Specifies properties for the frame of the bubble gauge chart.

![Format Bubble Gauge dialog - Frame](https://devnet.logianalytics.com/hc/article_attachments/4404880381207/fmtbublgauge_frm.gif)

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
   Specifies the color of the border. To change the color, select the color indicator to select a new color from the color palette, or select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009746842-Color-Picker-Dialog-Box-Properties) dialog box in which you can select a color within a wider range.
* **Transparency**  
   Specifies the transparency for color of the border.
* **Thickness**  
   Specifies the thickness of the border, in inches.

**Gauge Group Name**

Specifies properties for the gauge group name.

* **Show Gauge Group Name**   
   Specifies whether to show names for the bubbles in the bubble gauge which are values of the field on its category axis. If the bubble gauge contains no category field, the group name shows Report by default.
  + **Position**  
     Specifies the position of the names relative to the bubbles. Select the position from the drop-down list. If customized is selected, the X and Y settings in the General tab of the [Format Gauge Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009747222-Format-Gauge-Label-Dialog-Box-Properties#General) dialog box will take effect.

## Range Color Tab Properties

Specifies different colors to fill the bubbles in bubble gauge in different ranges.

![Format Bubble Gauge dialog - Range Color](https://devnet.logianalytics.com/hc/article_attachments/4404880381463/fmtbublgauge_rgclr.gif)

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404880163351/btn_add1.gif)

Adds a new color range.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404885309335/btn_delete.gif)

Removes the selected color range.

**Minimum**

Specifies the minimum value of the range.

**Maximum**

Specifies the maximum value of the range.

**Color**

Specifies the color schema of the range. Select in the color cell to select a color from the color palette, or select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009746842-Color-Picker-Dialog-Box-Properties) dialog box in which you can select a color within a wider range.

**Name**

Displays the name of the range.

**Others**

Specifies the properties for values that do not fall into any of the ranges you define.

* **Name**  
   Specifies the name for the values.
* **Color**  
   Specifies the color for the values. To change the color, select the color indicator to select a new color from the color palette, or select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009746842-Color-Picker-Dialog-Box-Properties) dialog box in which you can select a color within a wider range.

## Hint Tab Properties

Specifies properties of the data marker hint.

![Format Bubble Gauge dialog - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404880381719/fmtbublgauge_hint.gif)

**Show Category and Series**

Specifies whether to include the category and series values in the data marker hint.

**Auto Scale in Number**

Specifies whether to
automatically scale the values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

The value **auto** means the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009777861-Chart-Properties#AutoScale).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009747182-Format-Bench-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009775441-Format-Category-X-Axis-Dialog-Box-Properties)
