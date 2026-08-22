---
title: "Format Activity Gauge Dialog Box Properties"
id: 5741423070743
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741423070743-Format-Activity-Gauge-Dialog-Box-Properties
updated_at: 2022-10-31T17:17:23Z
---

# Format Activity Gauge Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741445554839-Font-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741429164823-Format-Area-Dialog-Box-Properties)

# Format Activity Gauge Dialog Box Properties

This topic describes how you can use the Format Activity Gauge dialog box to format an activity gauge chart. Server displays the dialog box when you right-click on an activity gauge chart and select **Format Graph** from the shortcut menu.

This topic contains the following sections:

* [Circular Graph Tab Properties](#Circular)
* [Pointer Tab Properties](#Pointer)
* [Target Tab Properties](#Target)
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

## Circular Graph Tab Properties

Specify the properties for circles in the activity gauge.

![Format Activity Gauge dialog - Circular Graph](https://devnet.logianalytics.com/hc/article_attachments/9905733286295/fmtactvtygauge_crculr.gif)

**Circular**

Specify the size of the circles.

* **Hole Size**  
   Specify the relative size of a circle in a percentage of total circle size.
* **Circular Gap**  
   Specify the distance between the circles.
* **Start Style**  
   Specify the style for the start graph of the circles.
* **End Style**  
   Specify the style for the end graph of the circles.
* **Start Mark**  
   Specify the mark for the start graph of the circles.
* **Stop Mark**  
   Specify the mark for the stop graph of the circles.

**Fill**

Specify the color of the circles.

* **Color**  
   Specify the color of the circles.
* **Color List**  
   Select to open the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741449488023-Color-List-Dialog-Box-Properties), and then specify the color of the circles.
* **Transparency**  
   Specify the transparency for color of the circles.
* **Background**  
   Specify the background color of the circles.
  + **Auto**  
     Select if you want to use colors that are lighter than the circles automatically. Server disables the Background property when Auto is selected.
* **Use Range Color**  
   Select if you want to use the color you defined for the ranges as the color of the circles. Then, Server disables the Color, Color List, and Transparency properties in the tab.

**Value**

Specify the values you want to display in the chart.

* **Minimum Value**  
   Specify the minimum value in the chart. You can also use a formula to control the property.
* **Maximum Value**  
   Specify the maximum value in the chart. You can also use a formula to control the property.

## Pointer Tab Properties

Specify properties of the pointers in the activity gauge.

![Format Activity Gauge dialog - Pointer](https://devnet.logianalytics.com/hc/article_attachments/9905755108503/fmtactvtygauge_pnt.gif)

**Show Pointer Value**

Select if you want to show the pointer values.

* **Position**  
   Select the position relationship of the value and the pointers. If you select **customized**, the X and Y settings in the General tab of the [Format Pointer Label dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741435429655-Format-Pointer-Label-Dialog-Box-Properties#General) will take effect.

## Target Tab Properties

Specify properties of the target in the activity gauge.

![Format Activity Gauge dialog - Target](https://devnet.logianalytics.com/hc/article_attachments/9905755148695/fmtactvtygauge_tgt.gif)

**Use Target Value**

Select if you want to use the target value for the activity gauge.

* **Target Value**   
   Specify the value of the target. You can also use a formula to control the value.

**Target Value**

Specify properties of the target value.

* **Show Target Value**  
   Select if you want to show the target value on the activity gauge.
  + **Position**  
     Select the position of the target value relative to the circle. If you select **customized**, the X and Y settings in the General tab of the [Format Target Label dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741465630999-Format-Target-Label-Dialog-Box-Properties#General) will take effect.

## Frame Tab Properties

Specify properties for the frame of the activity gauge chart.

![Format Activity Gauge dialog - Frame](https://devnet.logianalytics.com/hc/article_attachments/9905733380759/fmtactvtygauge_frm.gif)

**Size**

Specify the size properties of the frame.

* **Frame Size**   
   Specify the size of the frame.

**Fill**

Specify the color and transparency of the frame.

* **Fill**  
   Specify the color you want to fill the frame.
* **Transparency**  
   Specify the transparency of the color you want to fill the frame.

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
   Select if you want to show names for the circles in the activity gauge which are values of the field on its category axis. If the activity gauge contains no category field, the group name shows Report by default.
  + **Position**  
     Select the position of the names relative to the circles. If you select **customized**, the X and Y settings in the General tab of the [Format Gauge Label dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741450295063-Format-Gauge-Label-Dialog-Box-Properties#General) will take effect.

## Range Color Tab Properties

Specify different colors to fill the circles in the activity gauge in different ranges.

![Format Activity Gauge dialog - Range Color](https://devnet.logianalytics.com/hc/article_attachments/9905733399319/fmtactvtygauge_rgclr.gif)

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

Specify properties of the data marker hint.

![Format Activity Gauge dialog - Hint](https://devnet.logianalytics.com/hc/article_attachments/9905755229975/fmtactvtygauge_hint.gif)

**Show Category and Series**

Select to include the category and series values in the data marker hint.

**Auto Scale in Number**

Select **true** if you want to automatically scale the values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

The default value **auto** means that the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/5741476174999-Setting-Web-Report-Object-Properties-Using-the-Inspector-Panel#AutoScale).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741445554839-Font-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741429164823-Format-Area-Dialog-Box-Properties)
