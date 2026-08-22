---
title: "Format Bar Gauge Dialog Box Properties"
id: 1500009744382
section: "Page Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009744382-Format-Bar-Gauge-Dialog-Box-Properties
updated_at: 2021-07-24T00:49:15Z
---

# Format Bar Gauge Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744362-Format-Bar-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009772261-Format-Bench-Dialog-Box-Properties)

# Format Bar Gauge Dialog Box Properties

You can use the Format Bar Gauge dialog box to format a bar gauge chart. This topic describes the options in the dialog box.

This topic contains the following sections:

* [Staff Graph Tab Properties](#Staff)
* [Axis Tab Properties](#Axis)
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

## Staff Graph Tab Properties

Specifies the properties for bars in the bar gauge.

![Format Bar Gauge dialog - Staff Graph](https://devnet.logianalytics.com/hc/article_attachments/4404880533783/fmtbargauge_stfgraph.gif)

**Bar**

Specifies the properties of the bars.

* **Layout**  
   Specifies the layout of the bars. It can be vertical or horizontal.
* **Thickness**  
   Specifies the thickness of the bars, in inches.
* **Start Style**  
   Specifies the style for the start graph of the bars.
* **End Style**  
   Specifies the style for the end graph of the bars.

**Border**

Specifies properties of the bar border.

* **Line Style**  
   Specifies the line style of the border.
* **Thickness**  
   Specifies the thickness of the border, in inches.
* **Color**  
   Specifies the color of the border. To change the color, select the color indicator to specify a new color in the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009745022-Select-Color-Dialog-Box-Properties) dialog box, or type a color string in the format #RRGGBB. If you want to make the background transparent, type Transparent in the text box.
* **Transparency**  
   Specifies the transparency for the border color.

**Show Range Name**

Specifies whether to show the names of the ranges defined in the [Range Color](#Range) tab. When the option is selected you can continue to specify the font properties of the text in the range names.

* **Font**  
   Lists all the available font faces that can be selected to apply to the text.
* **Size**  
   Specifies the font size of the text.
* **Fill Type**  
   Specifies the fill type of the text. It can be one of the following: none, color, gradient and texture.
* **Color**  
   Specifies the font color of the text.
* **Font Style**  
   Specifies the font style of the text. It can be one of the following: plain, bold, italic, and bold italic.
* **Transparency**  
   Specifies the color transparency of the text.

## Axis Tab Properties

The tab consists of four sub tabs: [Axis](#Axis1), [Tick Mark](#TickMark), [Label](#Label), and [Format](#Format).

### Axis

Specifies properties of the axis in the bar gauge.

![Format Bar Gauge dialog - Axis - Axis tab](https://devnet.logianalytics.com/hc/article_attachments/4404880534295/fmtbargauge_axis_axis.gif)

**Show Axis**

Specifies whether to show the axis.

**Type**

Specifies the position relationship of the axis and the bar. When Layout is set to horizontal in the [Staff Graph](#Staff) tab, the following are available:

* **Top**  
   The axis will be on the top of the bar.
* **Bottom**  
   The axis will be on the bottom of the bar.
* **Center**  
   The axis will be in the center of the bar.

When Layout is set to vertical in the [Staff Graph](#Staff) tab, the following are available:

* **Left**  
   The axis will be on the left of the bar.
* **Right**  
   The axis will be on the right of the bar.
* **Center**  
   The axis will be in the center of the bar.

**Option**

Specifies the values to be displayed in the chart.

* **Minimum Value**  
   Specifies the minimum value to be displayed in the chart.
* **Maximum Value**  
   Specifies the maximum value to be displayed in the chart.

**Line**

Specifies the properties of the axis line.

* **Color**  
   Specifies the color of the line.
* **Style**  
   Specifies the style of the line.
* **Transparency**  
   Specifies the color transparency of the line.
* **Thickness**  
   Specifies the thickness of the line.
* **Use Range Color**   
   Specifies whether the axis line color follows [the colors of the ranges](#Range), that is, the axis line part for the range of blue color will become blue and the part for the range of red color will become red. If the option is selected, the Color and Transparency options will be disabled.

**Gap**

* **Staff Axis Gap**   
   Specifies the gap between the axis and the bar when the axis is not in the center of the bar. The option is disabled when Type is set to center in the tab.

### Tick Mark

Specifies the properties of the tick marks on the axis.

![Format Bar Gauge dialog - Axis - Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4404885589143/fmtbargauge_axis_tkmk.gif)

**Type**

Specifies the position relationship of the axis and the tick marks. When Layout is set to horizontal in the [Staff Graph](#Staff) tab, the following are available:

* **None**  
   Specifies not to display the tick marks on the axis. It is meaningless to specify all the other tick mark related properties if this type is selected.
* **Top**  
   Specifies to display the tick marks on the top of the axis.
* **Bottom**  
   Specifies to display the tick marks on the bottom of the axis.
* **Center**  
   Specifies to display the tick marks in the center of the axis.

When Layout is set to vertical in the [Staff Graph](#Staff) tab, the following are available:

* **None**  
   Specifies not to display the tick marks on the axis. It is meaningless to specify all the other tick mark related properties if this type is selected.
* **Left**  
   Specifies to display the tick marks on the left of the axis.
* **Right**  
   Specifies to display the tick marks on the right of the axis.
* **Center**  
   Specifies to display the tick marks in the center of the axis.

**Major Tick Mark Line**

Specifies the properties of the major tick mark line.

* **Correlate with Axis**   
   If the option is selected, the line properties of the major tick marks will correlate with [that of the axis](#Line) automatically.
  + **Color**  
     Specifies the color of the major tick mark line. Disabled when Use Range Color in the Axis sub tab is selected.
  + **Style**  
     Specifies the style of the major tick mark line.
  + **Transparency**  
     Specifies the color transparency of the major tick mark line. Disabled when Use Range Color in the Axis sub tab is selected.
  + **Thickness**  
     Specifies the thickness of the major tick mark line.
* **Increment**  
   Specifies the distance between two adjacent major tick marks on the axis.
* **Number of Tick Marks**  
   Specifies how many major tick marks to be displayed on the axis.
* **Tick Mark Length**  
   Specifies the length of the major tick mark line.

**Minor Tick Mark Line**

Specifies the properties of the minor tick mark line.

* **Correlate with Axis**  
   If the option is selected, the line properties of the minor tick marks will correlate with [that of the axis](#Line) automatically.
  + **Color**  
     Specifies the color of the minor tick mark line. Disabled when Use Range Color in the Axis sub tab is selected.
  + **Style**  
     Specifies the style of the minor tick mark line.
  + **Transparency**  
     Specifies the color transparency of the minor tick mark line. Disabled when Use Range Color in the Axis sub tab is selected.
  + **Thickness**  
     Specifies the thickness of the minor tick mark line.
* **Increment**  
   Specifies the distance between two adjacent minor tick marks on the axis.
* **Number of Tick Marks**  
   Specifies how many minor tick marks to be displayed on the axis.
* **Tick Mark Length**  
   Specifies the length of the minor tick mark line.

### Label

Specifies the properties of the major tick mark labels.

![Format Bar Gauge dialog - Axis - Label](https://devnet.logianalytics.com/hc/article_attachments/4404880534807/fmtbargauge_axis_lbl.gif)

**Option**

Specifies the type of the labels.

* **None**  
   If selected, the labels will not be shown.
* **Normal**  
   If selected, the labels will be shown as you specify.
  + **Label Every N Major Tick Marks**  
     Specifies the frequency at which the major tick marks will be labeled.
  + **Number of Major Labels**  
     Specifies how many major tick mark labels to be displayed on the axis.
    - **Auto**  
       If the option is selected, all major tick mark labels will be shown.
    - **Fixed**  
       If the option is selected, you can specify the number of the major tick mark labels to be displayed on the axis.
* **Range Value**  
   If selected, the labels will show the [range values](#Range).

**Gap**

Specifies the gap properties for the data labels.

* **Label Axis Gap**  
   Specifies the distance between the data labels and the axis, in inches.
* **Best Effect**  
   Specifies whether to adjust the data labels automatically to make them placed best. If the option is selected, some labels will be hidden when they are overlapped.

**Font**

Specifies the font format of text in the data labels.

* **Font**  
   Lists all the available font faces that can be selected to apply to the text.
* **Size**  
   Specifies the font size of the text.
* **Fill Type**  
   Specifies the fill type of the text. It can be one of the following: none, color, texture, and gradient.
* **Color**   
   Specifies the font color of the text. Disabled when Use Range Color in the Axis sub tab is selected.
* **Font Style**  
   Specifies the font style of the text. It can be one of the following: plain, bold, italic, and bold italic.
* **Transparency**  
   Specifies the color transparency of the text. Disabled when Use Range Color in the Axis sub tab is selected.

**Orientation**

* **Angle**  
   Specifies the rotation angle of the data labels.

### Format

Specifies the data format of the major tick mark labels.

![Format Bar Gauge dialog - Axis - Format](https://devnet.logianalytics.com/hc/article_attachments/4404880535063/fmtbargauge_axis_fmt.gif)

**Category**

Lists the category types. Select one to customize its format.

**Format**

Displays all the [formats](https://devnet.logianalytics.com/hc/en-us/articles/1500009775121-Data-Format-Dialog-Box-Properties#DataFormat) of the selected category. Select the required one and select Add to add it as the format of the specified category. You can add only one format for each category.

**Properties**

Displays the properties of the format you select. If the formats listed in the Format box cannot meet your requirement, define the format in the text box and then select Add to add it as the format of the specified category.

**Auto Scale in Number**

Specifies whether to
automatically scale the values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

The default value **auto** means that the setting follows [that of the chart platform](https://devnet.logianalytics.com/hc/en-us/articles/1500009772421-Format-Platform-Dialog-Box-Properties#AutoScale). When you set the property to **true**, the specified format will apply to the integer part of the values after being scaled; but if the specified format conflicts with the Number data type, Logi Report will ignore the Auto Scale in Number setting.

**Sample**

Displays a preview sample of your selection.

**Stack**

Lists all the formats you select from different categories.

**Add**

Adds a format to the Stack list box.

**Remove**

Removes a format from the Stack list box.

**Apply**

Applies the specified format in the Stack list box to the major tick mark labels.

## Pointer Tab Properties

Specifies the properties of the pointers in the bar gauge.

![Format Bar Gauge dialog - Pointer](https://devnet.logianalytics.com/hc/article_attachments/4404880535575/fmtbargauge_pnt.gif)

**Use Pointer**

Specifies to use pointers to indicate values in the bar gauge.

* **Pointer Style**  
   Specifies properties of the pointers.
  + **Value Pointer**  
     Specifies the style of the value pointers. Select a style from the drop-down list or select Customized to specify another image as the value pointers in the [Insert Image](https://devnet.logianalytics.com/hc/en-us/articles/1500009744722-Insert-Image-Dialog-Box-Properties#Gauge) dialog box.
  + **Width**  
     Specifies the width of the pointers.
  + **Height**  
     Specifies the height of the pointers.
  + **Position**  
     Specifies the position of the pointers relative to the bar.
  + **Gap**  
     Specifies the distance between the pointers and the bar.
  + **Style List**  
     Opens the [Style List](https://devnet.logianalytics.com/hc/en-us/articles/1500009773101-Style-List-Dialog-Box-Properties) dialog box to specify the style for pointers in the same data series respectively.
* **Pointer Color**  
   Specifies color properties of the pointers.
  + **Color**  
     Specifies the color of the pointers.
  + **Color List**   
     Opens the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009775061-Color-List-Dialog-Box-Properties) dialog box to specify the color pattern for pointers in the same data series respectively.
  + **Transparency**  
     Specifies the transparency for color of the pointers.
  + **Use Range Color**  
     Specifies whether to use the color [defined for the ranges](#Range) as the pointer color. If the option is selected, the three properties above will be disabled.
* **Pointer Value**  
   Specifies properties for values of the pointers.
  + **Show Pointer Value**  
     Specifies whether to show values for the pointers.
    - **Position**  
       Specifies the position relationship between the values and the pointers. Select the position from the drop-down list. If customized is selected, the X and Y settings in the General tab of the [Format Pointer Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009744522-Format-Pointer-Label-Dialog-Box-Properties#General) dialog box will take effect.

**Use Color Bar**

Specifies to use color bars to indicate values in the bar gauge.

* **Pointer Color**  
   Specifies the properties of the color bars.
  + **Color**  
     Specifies the color of the bars.
  + **Transparency**  
     Specifies the transparency for color of the bars.
  + **Thickness**  
     Specifies the thickness of the color bars.
  + **Color List**   
     Opens the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009744162-Color-List-Dialog-Box-Properties) dialog box to specify the color pattern for color bars in the same data series respectively.
* **Pointer Value**  
   Specifies properties for values of the color bars.
  + **Show Pointer Value**  
     Specifies whether to show values for the color bars.
  + **Position**  
     Specifies the position relationship between the values and the color bars. Select the position from the drop-down list. If customized is selected, the X and Y settings in the General tab of the [Format Pointer Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009744522-Format-Pointer-Label-Dialog-Box-Properties#General) dialog box will take effect.

**Pointer Border**

Specifies properties of the pointer border.

* **Show Pointer Border**  
   Specifies whether to show the border of the pointers. When the option is selected, the following border properties are enabled.
  + **Line Style**Specifies the line style to apply to the border.
  + **Color**  
     Specifies the color of the border.
  + **Thickness**Specifies the weight of the border, in inches.
  + **Transparency**Specifies the transparency for color of the border.

## Target Tab Properties

Specifies the properties of the target in the bar gauge.

![Format Bar Gauge dialog - Target](https://devnet.logianalytics.com/hc/article_attachments/4404885589783/fmtbargauge_tgt.gif)

**Use Target Value**

Specifies whether to use the target value for the bar gauge.

* **Target Value**   
   Specifies the target value.

**Pointer Style**

Specifies the pointer style for the target value.

* **Target Pointer**  
   Specifies the style of the target pointer. Select a style from the drop-down list or select Customized to specify another image as the target pointer in the [Insert Image](https://devnet.logianalytics.com/hc/en-us/articles/1500009744722-Insert-Image-Dialog-Box-Properties#Gauge) dialog box.
* **Width**  
   Specifies the width of the target pointer.
* **Height**  
   Specifies the height of the target pointer.
* **Position**  
   Specifies the position of the target pointer relative to the bar.
* **Gap**  
   Specifies the distance between the target pointer and the bar.

**Pointer Color**

Specifies color properties of the target pointer.

* **Color**  
   Specifies the color of the target pointer.
* **Transparency**  
   Specifies the transparency for color of the target pointer.

**Target Value**

Specifies the properties of the target value.

* **Show Target Value**   
   Specifies whether to show the target value on the bar gauge.
  + **Position**  
     Specifies the position of the target value relative to the bar. Select the position from the drop-down list. If customized is selected, the X and Y settings in the General tab of the [Format Target Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009772501-Format-Target-Label-Dialog-Box-Properties#General) dialog box will take effect.

## Frame Tab Properties

Specifies properties for the frame of the bar gauge chart.

![Format Bar Gauge dialog - Frame](https://devnet.logianalytics.com/hc/article_attachments/4404880535959/fmtbargauge_frm.gif)

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
   Specifies whether to show names for the bars in the bar gauge which are values of the field on its category axis. If the bar gauge contains no category field, the group name shows Report by default.
  + **Position**  
     Specifies the position of the names relative to the bars. Select the position from the drop-down list. If customized is selected, the X and Y settings in the General tab of the [Format Gauge Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009772321-Format-Gauge-Label-Dialog-Box-Properties#General) dialog box will take effect.

## Range Color Tab Properties

Specifies different colors to fill the bars in bar gauge in different ranges.

![Format Bar Gauge dialog - Range Color](https://devnet.logianalytics.com/hc/article_attachments/4404880536471/fmtbargauge_rgclr.gif)

**Use Gradient Effect**

Specifies whether to use gradient effect for the color.

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

![Format Bar Gauge dialog - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404885590295/fmtbargauge_hint.gif)

**Show Category and Series**

Specifies whether to include the category and series values in the data marker hint.

**Auto Scale in Number**

Specifies whether to
automatically scale the values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

The default value **auto** means that the setting follows [that of the chart platform](https://devnet.logianalytics.com/hc/en-us/articles/1500009772421-Format-Platform-Dialog-Box-Properties#AutoScale).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744362-Format-Bar-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009772261-Format-Bench-Dialog-Box-Properties)
