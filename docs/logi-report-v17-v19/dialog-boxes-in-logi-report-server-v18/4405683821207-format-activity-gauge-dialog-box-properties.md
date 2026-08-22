---
title: "Format Activity Gauge Dialog Box Properties"
id: 4405683821207
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683821207-Format-Activity-Gauge-Dialog-Box-Properties
updated_at: 2022-01-27T07:59:16Z
---

# Format Activity Gauge Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683847959-Font-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683822231-Format-Area-Dialog-Box-Properties)

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

Select **OK** to apply any changes you made here.

**Cancel**

Select **Cancel** to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4420447202071/btn_help.gif)

Select to view information about the Format Activity Gauge dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420447202455/btn_close.gif)

Select to close the dialog box without saving any changes.

## Circular Graph Tab Properties

Specifies the properties for circles in the activity gauge.

![Format Activity Gauge dialog - Circular Graph](https://devnet.logianalytics.com/hc/article_attachments/4420453583127/fmtactvtygauge_crculr.gif)

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
   Opens the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/4405683801367-Color-List-Dialog-Box-Properties) dialog box for you to specify the color of the circles.
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
   Specifies the minimum value to be displayed in the chart. You can also use a formula to control the property.
* **Maximum Value**  
   Specifies the maximum value to be displayed in the chart. You can also use a formula to control the property.

## Pointer Tab Properties

Specifies properties of the pointers in the activity gauge.

![Format Activity Gauge dialog - Pointer](https://devnet.logianalytics.com/hc/article_attachments/4420447248791/fmtactvtygauge_pnt.gif)

**Show Pointer Value**

Specifies whether to show the pointer values.

* **Position**  
   Specifies the position relationship of the value and the pointers. Select the position from the drop-down list. If customized is selected, the X and Y settings in the General tab of the [Format Pointer Label](https://devnet.logianalytics.com/hc/en-us/articles/4405690586647-Format-Pointer-Label-Dialog-Box-Properties#General) dialog box will take effect.

## Target Tab Properties

Specifies properties of the target in the activity gauge.

![Format Activity Gauge dialog - Target](https://devnet.logianalytics.com/hc/article_attachments/4420447249047/fmtactvtygauge_tgt.gif)

**Use Target Value**

Specifies whether to use the target value for the activity gauge.

* **Target Value**   
   Specifies the value of the target. You can also use a formula to control the value.

**Target Value**

Specifies properties of the target value.

* **Show Target Value**  
   Specifies whether to show the target value on the activity gauge.
  + **Position**  
     Specifies the position of the target value relative to the circle. Select the position from the drop-down list. If customized is selected, the X and Y settings in the General tab of the [Format Target Label](https://devnet.logianalytics.com/hc/en-us/articles/4405683842455-Format-Target-Label-Dialog-Box-Properties#General) dialog box will take effect.

## Frame Tab Properties

Specifies properties for the frame of the activity gauge chart.

![Format Activity Gauge dialog - Frame](https://devnet.logianalytics.com/hc/article_attachments/4420447249431/fmtactvtygauge_frm.gif)

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
   Specifies the color of the border. To change the color, select the color indicator to select a new color from the color palette, or select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/4405683802391-Color-Picker-Dialog-Box-Properties) dialog box in which you can select a color within a wider range.
* **Transparency**  
   Specifies the transparency for color of the border.
* **Thickness**  
   Specifies the thickness of the border, in inches.

**Gauge Group Name**

Specifies properties for the gauge group name.

* **Show Gauge Group Name**   
   Specifies whether to show names for the circles in the activity gauge which are values of the field on its category axis. If the activity gauge contains no category field, the group name shows Report by default.
  + **Position**  
     Specifies the position of the names relative to the circles. Select the position from the drop-down list. If customized is selected, the X and Y settings in the General tab of the [Format Gauge Label](https://devnet.logianalytics.com/hc/en-us/articles/4405683832215-Format-Gauge-Label-Dialog-Box-Properties#General) dialog box will take effect.

## Range Color Tab Properties

Specifies different colors to fill the circles in the activity gauge in different ranges.

![Format Activity Gauge dialog - Range Color](https://devnet.logianalytics.com/hc/article_attachments/4420461651223/fmtactvtygauge_rgclr.gif)

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420447073687/btn_add1.gif)

Adds a new color range.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420453394455/btn_delete.gif)

Removes the selected color range.

**Minimum**

Specifies the minimum value of the range.

**Maximum**

Specifies the maximum value of the range.

**Color**

Specifies the color schema of the range. Select in the color cell to select a color from the color palette, or select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/4405683802391-Color-Picker-Dialog-Box-Properties) dialog box in which you can select a color within a wider range.

**Name**

Displays the name of the range.

**Others**

Specifies the properties for values that do not fall into any of the ranges you define.

* **Name**  
   Specifies the name for the values.
* **Color**  
   Specifies the color for the values. To change the color, select the color indicator to select a new color from the color palette, or select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/4405683802391-Color-Picker-Dialog-Box-Properties) dialog box in which you can select a color within a wider range.

## Hint Tab Properties

Specifies properties of the data marker hint.

![Format Activity Gauge dialog - Hint](https://devnet.logianalytics.com/hc/article_attachments/4420447249687/fmtactvtygauge_hint.gif)

**Show Category and Series**

Select to include the category and series values in the data marker hint.

**Auto Scale in Number**

Select **true** if you want to automatically scale the values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

The default value **auto** means that the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/4411830859799-Setting-Web-Report-Object-Properties-Using-the-Inspector-Panel#AutoScale).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683847959-Font-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683822231-Format-Area-Dialog-Box-Properties)
