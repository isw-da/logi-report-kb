---
title: "Format Bubble Gauge Dialog Box Properties"
id: 5741444911383
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741444911383-Format-Bubble-Gauge-Dialog-Box-Properties
updated_at: 2022-10-31T17:17:25Z
---

# Format Bubble Gauge Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741444898839-Format-Bench-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741450197399-Format-Category-X-Axis-Dialog-Box-Properties)

# Format Bubble Gauge Dialog Box Properties

This topic describes how you can use the Format Bubble Gauge dialog box to format the bubble gauges in a bubble gauge chart. Server displays the dialog box when you right-click on a bubble gauge chart and select **Format Graph** from the shortcut menu.

This topic contains the following sections:

* [Staff Graph Tab Properties](#Staff)
* [Frame Tab Properties](#Frame)
* [Range Color Tab Properties](#Range)
* [Hint Tab Properties](#Hint)

You see these elements on all the tabs:

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

## Staff Graph Tab Properties

Specify the properties for bubbles in the bubble gauge.

![Format Bubble Gauge dialog - Staff Graph](https://devnet.logianalytics.com/hc/article_attachments/9905732883351/fmtbublgauge_stfgraph.gif)

**Bubbles**

Specify the properties of the bubbles.

* **Left Margin**  
   Specify the gap between the left labels and left bubbles, in inches.
* **Top Margin**  
   Specify the gap between top labels and top bubbles, in inches.
* **Range Radius**  
   Specify the relative size of a bubble in a percentage of total bubble size.
* **Draw Category (X) Grid**  
   Select if you want to draw category grid.
* **Draw Series (Z) Grid**  
   Select if you want to draw series grid.

**Border**

Specify the properties for the border of the bubbles.

* **Show Border**  
  Select if you want to show the border of the bubbles. Then, Server enables the following border properties.

  + **Line Style**  
     Specify the line style you want to apply to the border.
  + **Color**  
     Specify the color of the border.
  + **Transparency**  
    Specify the transparency for color of the border.
  + **Thickness**  
     Specify the thickness of the border, in inches.

**Value**

Specify the minimum and maximum values for the color range. Server divides the values equally into three ranges, each of which uses the color you specify in the Range Color tab automatically. This setting works only when you do not specify ranges for the values in the Range Color tab.

* **Minimum Value**  
   Specify the minimum value you want to display in the chart. You can also use a formula to control the property.
* **Maximum Value**  
   Specify the maximum value you want to display in the chart. You can also use a formula to control the property.

## Frame Tab Properties

Specify the properties for the frame of the bubble gauge chart.

![Format Bubble Gauge dialog - Frame](https://devnet.logianalytics.com/hc/article_attachments/9905732907799/fmtbublgauge_frm.gif)

**Size**

Specify the size properties of the frame.

* **Frame Size**   
   Specify the size of the frame.

**Fill**

Specify the color and transparency of the frame.

* **Fill**  
   Specify the color to fill the frame.
* **Transparency**  
   Specify the transparency of the color to fill the frame.

**Border**

Specify the properties for the border of the frame.

* **Line Style**  
  Specify the line style you want to apply to the border.
* **Border Type**  
   Specify the type of the border.
* **Color**  
   Specify the color of the border. To change the color, select the color indicator. Server displays the color palette. Select a color, or select **More Colors** to access the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428592023-Color-Picker-Dialog-Box-Properties) in which you can specify a color within a wider range.
* **Transparency**  
   Specify the transparency for color of the border.
* **Thickness**  
   Specify the thickness of the border, in inches.

**Gauge Group Name**

Specify the properties for the gauge group name.

* **Show Gauge Group Name**   
   Select if you want to show names for the bubbles in the bubble gauge which are values of the field on its category axis. If the bubble gauge contains no category field, the group name shows Report by default.
  + **Position**  
     Select the position of the names relative to the bubbles. If you select **customized**, the X and Y settings in the General tab of the [Format Gauge Label dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741450295063-Format-Gauge-Label-Dialog-Box-Properties#General) will take effect.

## Range Color Tab Properties

Specify different colors to fill the bubbles in bubble gauge in different ranges.

![Format Bubble Gauge dialog - Range Color](https://devnet.logianalytics.com/hc/article_attachments/9905732929943/fmtbublgauge_rgclr.gif)

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905619223831/btn_add1.gif)**Add button**

Select to add a new color range.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/9905578411927/btn_delete.gif)**Remove button**

Select to remove the selected color range.

**Minimum**

Specify the minimum value of the range.

**Maximum**

Specify the maximum value of the range.

**Color**

Specify the color schema of the range.

Select in the color cell. Server displays the color palette. Select a color, or select **More Colors** to access the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428592023-Color-Picker-Dialog-Box-Properties) in which you can specify a color within a wider range.

**Name**

Specify the name of a range.

**Others**

Specify the properties for values that do not fall into any of the ranges you define.

* **Name**  
  Specify the name for the values.
* **Color**  
   Specify the color for the values. To change the color, select the color indicator. Server displays the color palette. Select a color, or select **More Colors** to access the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428592023-Color-Picker-Dialog-Box-Properties) in which you can specify a color within a wider range.

## Hint Tab Properties

Specify the properties of the data marker hint.

![Format Bubble Gauge dialog - Hint](https://devnet.logianalytics.com/hc/article_attachments/9905732956823/fmtbublgauge_hint.gif)

**Show Category and Series**

Select to include the category and series values in the data marker hint.

**Auto Scale in Number**

Select **true** if you want to automatically scale the values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

The default value **auto** means that the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/5741476174999-Setting-Web-Report-Object-Properties-Using-the-Inspector-Panel#AutoScale).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741444898839-Format-Bench-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741450197399-Format-Category-X-Axis-Dialog-Box-Properties)
