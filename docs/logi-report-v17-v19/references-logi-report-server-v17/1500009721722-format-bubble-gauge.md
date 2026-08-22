---
title: "Format Bubble Gauge"
id: 1500009721722
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009721722-Format-Bubble-Gauge
updated_at: 2021-07-25T07:19:23Z
---

# Format Bubble Gauge

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009721702-Format-Bench)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009721742-Format-Category-X-Axis)

# Format Bubble Gauge

The Format Bubble Gauge dialog box is used to format the bubble gauges in a bubble gauge chart. It appears when you right-click on a bubble gauge chart and select Format Graph from the shortcut menu.

There are the following tabs in this dialog box: [Staff Graph](#Staff), [Frame](#Frame), [Range Color](#Range) and [Hint](#Hint).

**OK**

Applies the changes and closes the dialog box.

**Cancel**

Does not retain any changes and closes the dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404936816535/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404942519575/btn_close.gif)

Ignores the setting and closes this dialog box.

## Staff Graph

Specifies properties for bubbles in the bubble gauge.

![Format Bubble Gauge dialog - Staff Graph](https://devnet.logianalytics.com/hc/article_attachments/4404936854039/fmtbublgauge_stfgraph.gif)

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

## Frame

Specifies properties for the frame of the bubble gauge chart.

![Format Bubble Gauge dialog - Frame](https://devnet.logianalytics.com/hc/article_attachments/4404936854295/fmtbublgauge_frm.gif)

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
   Specifies the color of the border. To change the color, select the color indicator to select a new color from the color palette, or select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009721402-Color-Picker-) dialog box in which you can select a color within a wider range.
* **Transparency**  
   Specifies the transparency for color of the border.
* **Thickness**  
   Specifies the thickness of the border, in inches.

**Gauge Group Name**

Specifies properties for the gauge group name.

* **Show Gauge Group Name**   
   Specifies whether to show names for the bubbles in the bubble gauge which are values of the field on its category axis. If the bubble gauge contains no category field, the group name shows Report by default.
  + **Position**  
     Specifies the position of the names relative to the bubbles. Select the position from the drop-down list. If customized is selected, the X and Y settings in the General tab of the [Format Gauge Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009721802-Format-Gauge-Label#General) dialog box will take effect.

## Range Color

Specifies different colors to fill the bubbles in bubble gauge in different ranges.

![Format Bubble Gauge dialog - Range Color](https://devnet.logianalytics.com/hc/article_attachments/4404942547991/fmtbublgauge_rgclr.gif)

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936734999/btn_add1.gif)

Adds a new color range.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404936717719/btn_delete.gif)

Removes the selected color range.

**Minimum**

Specifies the minimum value of the range.

**Maximum**

Specifies the maximum value of the range.

**Color**

Specifies the color schema of the range. Select in the color cell to select a color from the color palette, or select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009721402-Color-Picker-) dialog box in which you can select a color within a wider range.

**Name**

Displays the name of the range.

**Others**

Specifies the properties for values that do not fall into any of the ranges you define.

* **Name**  
   Specifies the name for the values.
* **Color**  
   Specifies the color for the values. To change the color, select the color indicator to select a new color from the color palette, or select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009721402-Color-Picker-) dialog box in which you can select a color within a wider range.

## Hint

Specifies properties of the data marker hint.

![Format Bubble Gauge dialog - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404936854551/fmtbublgauge_hint.gif)

**Show Category and Series**

Specifies whether to include the category and series values in the data marker hint.

**Auto Scale in Number**

Specifies whether to automatically scale the values displayed in the data marker hint that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

By default it is set to auto which means that the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009723722-Chart#AutoScale).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009721702-Format-Bench)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009721742-Format-Category-X-Axis)
