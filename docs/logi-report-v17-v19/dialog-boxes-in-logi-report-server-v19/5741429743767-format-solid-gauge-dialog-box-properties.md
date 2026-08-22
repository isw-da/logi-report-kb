---
title: "Format Solid Gauge Dialog Box Properties"
id: 5741429743767
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741429743767-Format-Solid-Gauge-Dialog-Box-Properties
updated_at: 2022-10-31T17:17:31Z
---

# Format Solid Gauge Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741445375895-Format-Series-Z-Gridline-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741465630999-Format-Target-Label-Dialog-Box-Properties)

# Format Solid Gauge Dialog Box Properties

This topic describes how you can use the Format Solid Gauge dialog box to format the solid gauges in a solid gauge chart.

Server displays the dialog box when you right-click a solid gauge chart and select **Format Graph** from the shortcut menu.

This topic contains the following sections:

* [Circular Graph Tab Properties](#Circular)
* [Axis Tab Properties](#Axis)
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

Specify the properties for arcs in the solid gauge.

![Format Solid Gauge dialog - Circular Graph](https://devnet.logianalytics.com/hc/article_attachments/9905731232407/fmtsldgauge_crculr.gif)

**Circular**

Specify the size of the arcs.

* **Angle**  
   Specify the degree for angles of the arcs. Select the angle of the gauge from the drop-down list, or select **Customized** to open the [Customize Gauge Angle dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741422604311-Customize-Gauge-Angle-Dialog-Box-Properties) to specify the start angle and end angle.
* **Thickness**  
   Specify the thickness of the arcs, in inches.
* **Hole Size**  
   Specify the relative size of an arc in a percentage of total arc size.
* **Start Style**  
   Specify the style of the start graph of the arcs.
* **End Style**   
   Specify the style of the end graph of the arcs.

**Fill**

Specify the color of the arcs.

* **Color**  
   Specify the color of the arcs.
* **Color List**  
   Select to open the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741449488023-Color-List-Dialog-Box-Properties) to specify the color of the arcs.
* **Transparency**  
   Specify the transparency for color of the arcs.
* **Background**  
   Specify the background color of the arcs.
* **Use Range Color**  
   Select if you want to use the color you defined for the ranges as the color of the arcs. Then, server disables the Color, Color List, and Transparency properties.

**Border**

Specify the properties for the border of the arcs.

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

## Axis Tab Properties

The tab consists of four sub tabs: [Axis](#Axis1), [Tick Mark](#TickMark), [Label](#Label), and [Format](#Format).

### Axis

Specify the properties of the axis in the solid gauge.

![Format Solid Gauge dialog - Axis - Axis tab](https://devnet.logianalytics.com/hc/article_attachments/9905731256087/fmtsldgauge_axis_axis.gif)

**Show Axis**

Select if you want to show the axis in the solid gauge.

**Type**

Specify the position relationship of the axis and the arcs.

* **Inside**  
  Select if you want to display the axis inside the arcs.
* **Outside**  
   Select if you want to display the axis outside the arcs.
* **Center**  
   Select if you want to display the axis in the center of the arcs.

**Option**

Specify the values you want to display on the axis.

* **Minimum Value**  
   Specify the minimum value of the axis. You can also use a formula to control the property.
* **Maximum Value**  
   Specify the maximum value of the axis. You can also use a formula to control the property.

**Line**

Specify the properties of the axis line.

* **Color**  
   Specify the color of the line.
* **Style**  
  Select the style of the line.
* **Transparency**  
   Specify the transparency for the color of the line.
* **Thickness**  
   Specify the thickness of the line.
* **Use Range Color**  
   Select to use the color you define for the ranges as the line color. In this case, Server disables the Color and Transparency properties.

**Gap**

* **Circular Axis Gap**   
   Specify the gap between the axis and the arcs if the axis is inside or outside of the arcs.

### Tick Mark

Specify the properties of the tick marks on the axis.

![Format Solid Gauge dialog - Axis - Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/9905731304983/fmtsldgauge_axis_tkmk.gif)

**Type**

Specify the type of the tick marks on the axis.

* **None**  
   Select if you don't want to display the tick marks on the axis. It is meaningless to specify all the other tick mark related properties when you select this type.
* **Inside**  
   Select to display the tick marks inside the axis.
* **Outside**  
   Select to display the tick marks outside the axis.
* **Center**  
   Select to display the tick marks in the center of the axis.

**Major Tick Mark Line**

Specify the properties of the major tick mark line.

* **Correlate with Axis**   
   Select if you want the line properties of the major tick marks to correlate with [that of the axis](#Line) automatically.
  + **Color**  
     Specify the color of the major tick mark line. Server disables this property when you select **Use Range Color** on the Axis > Axis tab.
  + **Style**  
     Select the style of the major tick mark line.
  + **Transparency**  
     Specify the color transparency of the major tick mark line. Server disables this property when you select **Use Range Color** on the Axis > Axis tab.
  + **Thickness**  
     Specify the thickness of the major tick mark line.
* **Increment**  
   Specify the distance between two adjacent major tick marks on the axis.
* **Number of Tick Marks**  
   Specify the number major tick marks you want to display on the axis.
* **Tick Mark Length**  
   Specify the length of the major tick mark line, in inches.

**Minor Tick Mark Line**

Specify the properties of the minor tick mark line.

* **Correlate with Axis**  
   Select if you want the line properties of the minor tick marks to correlate with [that of the axis](#Line) automatically.
  + **Color**  
     Specify the color of the minor tick mark line. Server disables this property when you select **Use Range Color** on the Axis > Axis tab.
  + **Style**  
     Select the style of the minor tick mark line.
  + **Transparency**  
     Specify the color transparency of the minor tick mark line. Server disables this property when you select **Use Range Color** on the Axis > Axis tab.
  + **Thickness**  
     Specify the thickness of the minor tick mark line.
* **Increment**  
   Specify the distance between two adjacent minor tick marks on the axis.
* **Number of Tick Marks**  
  Specify the number of minor tick marks you want to display on the axis.
* **Tick Mark Length**  
   Specify the length of the minor tick mark line, in inches.

### Label

Specify the properties of the major tick mark labels.

![Format Solid Gauge dialog - Axis - Label](https://devnet.logianalytics.com/hc/article_attachments/9905719540375/fmtsldgauge_axis_lbl.gif)

**Option**

Specify the type of the labels.

* **None**  
   Select if you don't want the labels to show.
* **Normal**  
   Select if you want to customize the labels.
  + **Label Every N Major Tick Marks**  
     Specify the frequency at which you want to label the major tick marks.
  + **Number of Major Labels**  
     Specify the number of major tick mark labels to display on the axis.
    - **Auto**  
       Select to display all major tick mark labels.
    - **Fixed**  
       Select and then specify the number of the major tick mark labels to display on the axis.
* **Range Value**  
   Select if you want the labels to show the [range values](#Range) you define.
* **Min and Max Value**  
   Select if you want the labels to show the [minimum value and maximum value](#AxisValue) you define on the Axis > Axis tab.

**Gap**

Specify the gap properties for the data labels.

* **Label Axis Gap**  
   Specify the distance between the data labels and the axis, in inches.
* **Best Effect**  
   Select to adjust the data labels automatically to place them in the best positions. In this case, Server hides some labels when they overlap.

**Font**

Specify the font format of text in the data labels.

* **Font**  
   Select the font face of the text.
* **Size**  
   Specify the font size of the text.
* **Fill Type**  
   Select the fill type of the text: none, color, texture, or gradient.
* **Color**   
   Specify the font color of the text. Server disables this property when you select **Use Range Color** on the Axis > Axis tab.
* **Font Style**  
   Select the font style of the text: plain, bold, italic, or bold italic.
* **Transparency**  
   Specify the color transparency of the text. Server disables this property when you select **Use Range Color** on the Axis > Axis tab.

**Orientation**

* **Angle**  
   Specify the rotation angle of the data labels.

### Format

Specify the data format of the major tick mark labels. See [Format](https://devnet.logianalytics.com/hc/en-us/articles/5741450135575-Format-Bar-Gauge-Dialog-Box-Properties#Format).

![Format Solid Gauge dialog - Axis - Format](https://devnet.logianalytics.com/hc/article_attachments/9905731343895/fmtsldgauge_axis_fmt.gif)

## Pointer Tab Properties

Specify the properties of the pointers in the solid gauge.

![Format Solid Gauge dialog - Pointer](https://devnet.logianalytics.com/hc/article_attachments/9905719586327/fmtsldgauge_pnt.gif)

**Pointer Style**

Specify the style of the pointers.

* **Arrow**  
   Select if you want to use arrow as the pointer style.
  + **Value Pointer**  
     Specify the style of the value pointers. Select a style from the drop-down list, or select **Customized** to specify another image as the value pointers in the [Insert Image dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741459251991-Insert-Image-Dialog-Box-Properties).
  + **Width**   
     Specify the width of the arrow.
  + **Height**   
     Specify the height of the arrow.
* **Mark**  
   Select if you want to use mark as the pointer style.
  + **Value Pointer**  
     Specify the style of the value pointers. Select a style from the drop-down list, or select **Customized** to specify another image as the value pointers in the [Insert Image dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741459251991-Insert-Image-Dialog-Box-Properties).
  + **Width**   
     Specify the width of the marks.
  + **Height**   
     Specify the height of the marks.
  + **Position**   
     Specify the position of the mark relative to the arc.
  + **Gap**   
     Specify the distance between the mark and the arc, in inches.
* **Style List**  
   Select to open the [Style List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741466876439-Style-List-Dialog-Box-Properties) to specify the style for pointers in the same data series respectively.

**Pointer Color**

Specify color properties of the pointers.

* **Color**  
   Specify the color of the pointers.
* **Color List**   
   Select to open the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741449488023-Color-List-Dialog-Box-Properties) to specify the pointer color.
* **Transparency**  
   Specify the transparency for color of the pointers.
* **Use Range Color**  
   Select if you want to use the color [defined for the ranges](#Range) as the pointer color. Then, Server disables the preceding three properties.

**Pointer Value**

Specify the pointer value properties.

* **Show Pointer Value**   
   Select if you want to show the pointer values.
  + **Position**  
     Select the position relationship between the values and the pointers. If you select **customized**, the X and Y settings in the General tab of the [Format Pointer Label dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741435429655-Format-Pointer-Label-Dialog-Box-Properties#General) will take effect.

**Pointer Border**

Specify the pointer border properties.

* **Show Pointer Border**  
   Select if you want to show the border of the pointers. Then, Server enables the following border properties.
  + **Line Style**Specify the line style you want to apply to the border.
  + **Color**  
     Specify the color of the border.
  + **Transparency**Specify the transparency for color of the border.
  + **Thickness**Specify the weight of the border, in inches.

## Target Tab Properties

Specify the properties of the target in the solid gauge.

![Format Solid Gauge dialog - Target](https://devnet.logianalytics.com/hc/article_attachments/9905719624727/fmtsldgauge_tgt.gif)

**Use Target Value**

Select if you want to use the target value for the solid gauge.

* **Target Value**   
   Specify the target value. You can also use a formula to control the value.

**Pointer Style**

Specify the pointer style for the target value.

* **Target Pointer**  
   Specify the style of the target pointer. Select a style from the drop-down list, or select **Customized** to specify another image as the target pointer in the [Insert Image dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741459251991-Insert-Image-Dialog-Box-Properties).
* **Width**  
   Specify the width of the target pointer.
* **Height**  
   Specify the height of the target pointer.
* **Position**  
   Specify the position of the target pointer relative to the arc.
* **Gap**  
   Specify the distance between the target pointer and the arc.

**Pointer Color**

Specify color properties of the target pointer.

* **Color**  
   Specify the color of the target pointer.
* **Transparency**  
   Specify the transparency for color of the target pointer.

**Target Value**

Specify the properties of the target value.

* **Show Target Value**  
   Select if you want to show the target value on the solid gauge.
  + **Position**  
     Select the position of the target value relative to the arc. If you select **customized**, the X and Y settings in the General tab of the [Format Target Label dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741465630999-Format-Target-Label-Dialog-Box-Properties#General) will take effect.

## Frame Tab Properties

Specify the properties for the frame of the solid gauge chart.

![Format Solid Gauge dialog - Frame](https://devnet.logianalytics.com/hc/article_attachments/9905719660311/fmtsldgauge_frm.gif)

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
   Select if you want to show names for the arcs in the solid gauge which are values of the field on its category axis. If the solid gauge contains no category field, the group name shows Report by default.
  + **Position**  
     Select the position of the names relative to the arcs. If you select **customized**, the X and Y settings in the General tab of the [Format Gauge Label dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741450295063-Format-Gauge-Label-Dialog-Box-Properties#General) will take effect.

## Range Color Tab Properties

Specify different colors to fill the arcs in solid gauge in different ranges.

![Format Solid Gauge dialog - Range Color](https://devnet.logianalytics.com/hc/article_attachments/9905719676439/fmtsldgauge_rgclr.gif)

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

![Format Solid Gauge dialog - Hint](https://devnet.logianalytics.com/hc/article_attachments/9905731467927/fmtsldgauge_hint.gif)

**Show Category and Series**

Select to include the category and series values in the data marker hint.

**Auto Scale in Number**

Select **true** if you want to automatically scale the values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

The default value **auto** means that the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/5741476174999-Setting-Web-Report-Object-Properties-Using-the-Inspector-Panel#AutoScale).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741445375895-Format-Series-Z-Gridline-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741465630999-Format-Target-Label-Dialog-Box-Properties)
