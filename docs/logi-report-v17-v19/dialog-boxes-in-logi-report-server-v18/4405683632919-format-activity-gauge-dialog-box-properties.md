---
title: "Format Activity Gauge Dialog Box Properties"
id: 4405683632919
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683632919-Format-Activity-Gauge-Dialog-Box-Properties
updated_at: 2022-01-27T07:58:39Z
---

# Format Activity Gauge Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683630871-Filter-Control-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683633943-Format-Area-Dialog-Box-Properties)

# Format Activity Gauge Dialog Box Properties

You can use the Format Activity Gauge dialog box to format an activity gauge chart. This topic describes the properties in the dialog box.

This topic contains the following sections:

* [Circular Graph Tab Properties](#Circular)
* [Pointer Tab Properties](#Pointer)
* [Target Tab Properties](#Target)
* [Frame Tab Properties](#Frame)
* [Range Color Tab Properties](#Range)
* [Hint Tab Properties](#Hint)

You see these elements on all the tabs:

**OK**

Select to apply any changes you made here and exit the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## Circular Graph Tab Properties

Specify the properties for circles in the activity gauge.

![Format Activity Gauge dialog box - Circular Graph](https://devnet.logianalytics.com/hc/article_attachments/4420453646103/fmtactvtygauge_crculr.gif)

**Circular**

Specify the size of the circles.

* **Hole Size**  
   Specify the relative size of a circle in a percentage of the total circle size.
* **Circular Gap**  
   Specify the distance between the circles.
* **Start Style**  
   Select the style for the start graph of the circles.
* **End Style**  
   Select the style for the end graph of the circles.
* **Start Mark**  
   Select the mark for the start graph of the circles.
* **Stop Mark**  
   Select the mark for the stop graph of the circles.

**Fill**

Specify the fill color of the circles.

* **Color**  
   Specify the color of the circles.
* **Color List**  
   Select to open the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405690501271-Color-List-Dialog-Box-Properties) to specify the color of the circles.
* **Transparency**  
   Specify the transparency for the color of the circles.
* **Background**  
   Specify the background color of the circles.
  + **Auto**  
     Select to use colors that are lighter than the circles automatically. You cannot specify the Background color when you select **Auto**.
* **Use Range Color**  
   Select to use the color you defined for the ranges as the color of the circles. Then, Server disables the Color, Color List, and Transparency properties.

**Value**

Specify the values you want to display in the chart.

* **Minimum Value**  
   Specify the minimum value in the chart.
* **Maximum Value**  
   Specify the maximum value in the chart.

## Pointer Tab Properties

Specify properties of the pointers in the activity gauge.

![Format Activity Gauge dialog box - Pointer](https://devnet.logianalytics.com/hc/article_attachments/4420461711895/fmtactvtygauge_pnt.gif)

**Show Pointer Value**

Select to show the pointer values.

* **Position**  
   Select the position relationship of the value and the pointers. If you select **customized**, the X and Y settings on the General tab of the [Format Pointer Label dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683648279-Format-Pointer-Label-Dialog-Box-Properties#General) will take effect.

## Target Tab Properties

Specify properties of the target in the activity gauge.

![Format Activity Gauge dialog box - Target](https://devnet.logianalytics.com/hc/article_attachments/4420447323543/fmtactvtygauge_tgt.gif)

**Use Target Value**

Select to use the target value for the activity gauge.

* **Target Value**   
   Specify the value of the target.

**Target Value**

Specify the properties of the target value.

* **Show Target Value**  
   Select to show the target value on the activity gauge.
  + **Position**  
     Select the position of the target value relative to the circle. If you select **customized**, the X and Y settings on the General tab of the [Format Target Label dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405690507031-Format-Target-Label-Dialog-Box-Properties#General) will take effect.

## Frame Tab Properties

Specify the frame properties of the activity gauge chart.

![Format Activity Gauge dialog box - Frame](https://devnet.logianalytics.com/hc/article_attachments/4420447323799/fmtactvtygauge_frm.gif)

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
  Select the line style of the border.
* **Border Type**  
   Select the type of the border.
* **Color**  
   Specify the color of the border. To change the color, select the color indicator to access the [Select Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683679639-Select-Color-Dialog-Box-Properties), and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff.
* **Transparency**  
   Specify the transparency for the color of the border.
* **Thickness**  
   Specify the thickness of the border, in inches.

**Gauge Group Name**

Specify the properties for the gauge group name.

* **Show Gauge Group Name**   
   Select to show the names for the circles in the activity gauge, which are values of the field on the category axis. If the activity gauge contains no category field, the group name shows **Report** by default.
  + **Position**  
     Select the position of the names relative to the circles. If you select **customized**, the X and Y settings on the General tab of the [Format Gauge Label dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683640599-Format-Gauge-Label-Dialog-Box-Properties#General) will take effect.

## Range Color Tab Properties

Specify different colors to fill the circles in the activity gauge in different ranges.

![Format Activity Gauge dialog - Range Color](https://devnet.logianalytics.com/hc/article_attachments/4420453646359/fmtactvtygauge_rgclr.gif)

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420447073687/btn_add1.gif)**Add button**

Select to add a new color range.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420453394455/btn_delete.gif)**Remove button**

Select to remove the selected color range.

**Range table**

* **Minimum**  
  Specify the minimum value of a range.
* **Maximum**  
  Specify the maximum value of a range.
* **Color**  
  Select the color cell to open the [Select Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683679639-Select-Color-Dialog-Box-Properties), and specify a new color.
* **Name**  
  Specify the name of a range.

**Others**

Specify the properties for values that do not fall into any of the ranges you define in the range table.

* **Name**  
   Specify the name for the values.
* **Color**  
   Specify the color for the values. To change the color, select the color indicator to access the [Select Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683679639-Select-Color-Dialog-Box-Properties), and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff.

## Hint Tab Properties

Specify the properties of the data marker hint.

![Format Activity Gauge dialog box - Hint](https://devnet.logianalytics.com/hc/article_attachments/4420447327255/fmtactvtygauge_hint.gif)

**Show Category and Series**

Select to include the category and series values in the data marker hint.

**Auto Scale in Number**

Select **true** if you want to automatically scale the values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

The default value **auto** means that the setting follows [that of the chart platform](https://devnet.logianalytics.com/hc/en-us/articles/4405690506135-Format-Platform-Dialog-Box-Properties#AutoScale).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683630871-Filter-Control-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683633943-Format-Area-Dialog-Box-Properties)
