---
title: "Format Activity Gauge Dialog Box Properties"
id: 1500009744342
section: "Page Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009744342-Format-Activity-Gauge-Dialog-Box-Properties
updated_at: 2021-07-24T00:49:17Z
---

# Format Activity Gauge Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744322-Filter-Control-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009772241-Format-Area-Dialog-Box-Properties)

# Format Activity Gauge Dialog Box Properties

You can use the Format Activity Gauge dialog box to format an activity gauge chart. This topic describes the options in the dialog box.

This topic contains the following sections:

* [Circular Graph Tab Properties](#Circular)
* [Pointer Tab Properties](#Pointer)
* [Target Tab Properties](#Target)
* [Frame Tab Properties](#Frame)
* [Range Color Tab Properties](#Range)
* [Hint Tab Properties](#Hint)

**OK**

Applies the changes and closes the dialog box.

**Cancel**

Does not retain any changes and closes the dialog box.

**Help**

Displays the help document about this feature.

## Circular Graph Tab Properties

Specifies the properties for circles in the activity gauge.

![Format Activity Gauge dialog - Circular Graph](https://devnet.logianalytics.com/hc/article_attachments/4404880537495/fmtactvtygauge_crculr.gif)

**Circular**

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
   Opens the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009744162-Color-List-Dialog-Box-Properties) dialog box for you to specify the color of the circles.
* **Transparency**  
   Specifies the transparency for color of the circles.
* **Background**  
   Specifies the background color of the circles.
  + **Auto**  
     Specifies to use colors that are lighter than the circles automatically. The Background option is disabled when Auto is selected.
* **Use Range Color**  
   Specifies whether to use the color you defined for the ranges as the color of the circles. If the option is selected, the Color, Color List and Transparency options will be disabled.

**Value**

Specifies the values to be displayed in the chart.

* **Minimum Value**  
   Specifies the minimum value to be displayed in the chart.
* **Maximum Value**  
   Specifies the maximum value to be displayed in the chart.

## Pointer Tab Properties

Specifies properties of the pointers in the activity gauge.

![Format Activity Gauge dialog - Pointer](https://devnet.logianalytics.com/hc/article_attachments/4404885591063/fmtactvtygauge_pnt.gif)

**Show Pointer Value**

Specifies whether to show the pointer values.

* **Position**  
   Specifies the position relationship of the value and the pointers. Select the position from the drop-down list. If customized is selected, the X and Y settings in the General tab of the [Format Pointer Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009744522-Format-Pointer-Label-Dialog-Box-Properties#General) dialog box will take effect.

## Target Tab Properties

Specifies properties of the target in the activity gauge.

![Format Activity Gauge dialog - Target](https://devnet.logianalytics.com/hc/article_attachments/4404885591575/fmtactvtygauge_tgt.gif)

**Use Target Value**

Specifies whether to use the target value for the activity gauge.

* **Target Value**   
   Specifies the value of the target.

**Target Value**

Specifies properties of the target value.

* **Show Target Value**  
   Specifies whether to show the target value on the activity gauge.
  + **Position**  
     Specifies the position of the target value relative to the circle. Select the position from the drop-down list. If customized is selected, the X and Y settings in the General tab of the [Format Target Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009772501-Format-Target-Label-Dialog-Box-Properties#General) dialog box will take effect.

## Frame Tab Properties

Specifies properties for the frame of the activity gauge chart.

![Format Activity Gauge dialog - Frame](https://devnet.logianalytics.com/hc/article_attachments/4404885592215/fmtactvtygauge_frm.gif)

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
   Specifies whether to show names for the circles in the activity gauge which are values of the field on its category axis. If the activity gauge contains no category field, the group name shows Report by default.
  + **Position**  
     Specifies the position of the names relative to the circles. Select the position from the drop-down list. If customized is selected, the X and Y settings in the General tab of the [Format Gauge Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009772321-Format-Gauge-Label-Dialog-Box-Properties#General) dialog box will take effect.

## Range Color Tab Properties

Specifies different colors to fill the circles in the activity gauge in different ranges.

![Format Activity Gauge dialog - Range Color](https://devnet.logianalytics.com/hc/article_attachments/4404885592471/fmtactvtygauge_rgclr.gif)

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

![Format Activity Gauge dialog - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404880538263/fmtactvtygauge_hint.gif)

**Show Category and Series**

Specifies whether to include the category and series values in the data marker hint.

**Auto Scale in Number**

Specifies whether to
automatically scale the values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

The default value **auto** means that the setting follows [that of the chart platform](https://devnet.logianalytics.com/hc/en-us/articles/1500009772421-Format-Platform-Dialog-Box-Properties#AutoScale).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744322-Filter-Control-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009772241-Format-Area-Dialog-Box-Properties)
