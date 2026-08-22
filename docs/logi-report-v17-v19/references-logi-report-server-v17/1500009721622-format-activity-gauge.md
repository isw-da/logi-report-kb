---
title: "Format Activity Gauge"
id: 1500009721622
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009721622-Format-Activity-Gauge
updated_at: 2021-07-25T07:19:24Z
---

# Format Activity Gauge

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748781-Font)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009721642-Format-Area)

# Format Activity Gauge

The Format Activity Gauge dialog box is used to format an activity gauge chart. It appears when you right-click on an activity gauge chart and select Format Graph from the shortcut menu.

There are the following tabs in this dialog box: [Circular Graph](#Circular), [Pointer](#Pointer), [Target](#Target), [Frame](#Frame), [Range Color](#Range) and [Hint](#Hint).

**OK**

Applies the changes and closes the dialog box.

**Cancel**

Does not retain any changes and closes the dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404936816535/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404942519575/btn_close.gif)

Ignores the setting and closes this dialog box.

## Circular Graph

Specifies the properties for circles in the activity gauge.

![Format Activity Gauge dialog - Circular Graph](https://devnet.logianalytics.com/hc/article_attachments/4404936857623/fmtactvtygauge_crculr.gif)

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
   Opens the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009748181-Color-List) dialog box for you to specify the color of the circles.
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

## Pointer

Specifies properties of the pointers in the activity gauge.

![Format Activity Gauge dialog - Pointer](https://devnet.logianalytics.com/hc/article_attachments/4404936857879/fmtactvtygauge_pnt.gif)

**Show Pointer Value**

Specifies whether to show the pointer values.

* **Position**  
   Specifies the position relationship of the value and the pointers. Select the position from the drop-down list. If customized is selected, the X and Y settings in the General tab of the [Format Pointer Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009721862-Format-Pointer-Label#General) dialog box will take effect.

## Target

Specifies properties of the target in the activity gauge.

![Format Activity Gauge dialog - Target](https://devnet.logianalytics.com/hc/article_attachments/4404936858135/fmtactvtygauge_tgt.gif)

**Use Target Value**

Specifies whether to use the target value for the activity gauge.

* **Target Value**   
   Specifies the value of the target. You can also use a formula to control the value.

**Target Value**

Specifies properties of the target value.

* **Show Target Value**  
   Specifies whether to show the target value on the activity gauge.
  + **Position**  
     Specifies the position of the target value relative to the circle. Select the position from the drop-down list. If customized is selected, the X and Y settings in the General tab of the [Format Target Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009721922-Format-Target-Label#General) dialog box will take effect.

## Frame

Specifies properties for the frame of the activity gauge chart.

![Format Activity Gauge dialog - Frame](https://devnet.logianalytics.com/hc/article_attachments/4404936858391/fmtactvtygauge_frm.gif)

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
   Specifies whether to show names for the circles in the activity gauge which are values of the field on its category axis. If the activity gauge contains no category field, the group name shows Report by default.
  + **Position**  
     Specifies the position of the names relative to the circles. Select the position from the drop-down list. If customized is selected, the X and Y settings in the General tab of the [Format Gauge Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009721802-Format-Gauge-Label#General) dialog box will take effect.

## Range Color

Specifies different colors to fill the circles in the activity gauge in different ranges.

![Format Activity Gauge dialog - Range Color](https://devnet.logianalytics.com/hc/article_attachments/4404936858647/fmtactvtygauge_rgclr.gif)

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

![Format Activity Gauge dialog - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404942549271/fmtactvtygauge_hint.gif)

**Show Category and Series**

Specifies whether to include the category and series values in the data marker hint.

**Auto Scale in Number**

Specifies whether to automatically scale the values displayed in the data marker hint that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

By default it is set to auto which means that the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009723722-Chart#AutoScale).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748781-Font)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009721642-Format-Area)
