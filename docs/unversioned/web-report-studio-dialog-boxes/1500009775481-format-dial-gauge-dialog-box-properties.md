---
title: "Format Dial Gauge Dialog Box Properties"
id: 1500009775481
section: "Web Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009775481-Format-Dial-Gauge-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:24Z
---

# Format Dial Gauge Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009775461-Format-Category-X-Gridline-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009775501-Format-Donut-Dialog-Box-Properties)

# Format Dial Gauge Dialog Box Properties

This topic describes how you can use the Format Dial Gauge dialog box to format a dial gauge chart. Server displays the dialog box when you right-click on a dial gauge chart and select **Format Graph** from the shortcut menu.

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

Select **OK** to apply any changes you made here.

**Cancel**

Select **Cancel** to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Select to view information about the Format Dial Gauge dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Select to close the dialog box without saving any changes.

## Circular Graph Tab Properties

Specifies properties for dials in the dial gauge chart.

![Format Dial Gauge dialog - Circular Graph](https://devnet.logianalytics.com/hc/article_attachments/4404885474071/fmtdlgauge_crculr.gif)

**Circular**

Specifies the size of the dials.

* **Angle**  
   Specifies the degree for angles of the dials. Select the angle of the gauge from the drop-down list or select Customized to open the [Customize Gauge Angle](https://devnet.logianalytics.com/hc/en-us/articles/1500009746882-Customize-Gauge-Angle-Dialog-Box-Properties) dialog box to specify the start angle and end angle.
* **Thickness**  
   Specifies the thickness of the dials, in inches.
* **Hole Size**  
   Specifies the relative size of a dial in a percentage of total dial size.
* **Start Style**  
   Specifies the style of the start graph of the dials.
* **End Style**   
   Specifies the style of the end graph of the dials.

**Border**

Specifies properties for borders of the dials.

* **Line Style**  
   Specifies the line style to apply to the border.
* **Border Type**  
  Specifies the type of the border.
* **Color**  
   Specifies the color of the border.
* **Transparency**  
   Specifies the transparency for color of the border.
* **Thickness**  
   Specifies the thickness of the border, in inches.

**Show Range Name**

Specifies whether to show the names of the ranges defined in the [Range Color](#Range) tab. When it is selected, you can use the following font properties to specify the format of the name text.

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

The tab consists of four sub tabs: [Axis](#Axis1), [Tick Mark](#TickMark), [Label](#Label) and [Format](#Format).

### Axis

Specifies properties of the axis in the dial gauge.

![Format Dial Gauge dialog - Axis - Axis tab](https://devnet.logianalytics.com/hc/article_attachments/4404880374295/fmtdlgauge_axis_axis.gif)

**Show Axis**

Specifies whether to show the axis in the dial gauge.

**Type**

Specifies the position relationship of the axis and the dials.

* **Inside**  
   If selected, the axis will be inside the dials.
* **Outside**  
   If selected, the axis will be outside the dials.
* **Center**  
   If selected, the axis will be in the center of the dials.

**Option**

Specifies the values to display on the axis.

* **Minimum Value**  
   Specifies the minimum value of the axis. You can also use a formula to control the property.
* **Maximum Value**  
   Specifies the maximum value of the axis. You can also use a formula to control the property.

**Line**

Specifies the properties of the axis line.

* **Color**  
   Specifies the color of the line.
* **Style**  
  Specifies the style of the line.
* **Transparency**  
   Specifies the transparency for color of the line.
* **Thickness**  
   Specifies the thickness of the line.
* **Use Range Color**   
   Specifies whether to use the color you define for the ranges as the line color. If the option is selected, the Color and Transparency options will be disabled.

**Gap**

* **Circular Axis Gap**   
   Specifies the gap between the axis and the dials if the axis is inside or outside of the dials.

### Tick Mark

Specifies properties of the tick marks on the axis.

![Format Dial Gauge dialog - Axis - Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4404880374807/fmtdlgauge_axis_tkmk.gif)

**Type**

Specifies the type of the tick marks on the axis.

* **None**  
   Specifies not to display the tick marks on the axis. It is meaningless to specify all the other tick mark related properties if this type is selected.
* **Inside**  
   Specifies to display the tick marks inside the axis.
* **Outside**  
   Specifies to display the tick marks outside the axis.
* **Center**  
   Specifies to display the tick marks in the center of the axis.

**Major Tick Mark Line**

Specifies properties of the major tick mark line.

* **Correlate with Axis**   
   If the option is selected, the line properties of the major tick marks will correlate with [that of the axis](#Line) automatically.
  + **Color**  
     Specifies the color of the major tick mark line. Disabled when Use Range Color in the Axis sub tab is selected.
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

Specifies properties of the minor tick mark line.

* **Correlate with Axis**  
   If the option is selected, the line properties of the minor tick marks will correlate with [that of the axis](#Line) automatically.
  + **Color**  
     Specifies the color of the line. Disabled when Use Range Color in the Axis sub tab is selected.
  + **Style**  
     Specifies the style of the line.
  + **Transparency**  
     Specifies the color transparency of the line. Disabled when Use Range Color in the Axis sub tab is selected.
  + **Thickness**  
     Specifies the thickness of the line.
* **Increment**  
   Specifies the distance between two adjacent minor tick marks on the axis.
* **Number of Tick Marks**  
   Specifies how many minor tick marks to be displayed on the axis.
* **Tick Mark Length**  
   Specifies the length of the minor tick mark line.

### Label

Specifies properties of the major tick mark labels.

![Format Dial Gauge dialog - Axis - Label](https://devnet.logianalytics.com/hc/article_attachments/4404885474583/fmtdlgauge_axis_lbl.gif)

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
   If selected, the labels will show the [range values](#Range) you define.
* **Min and Max Value**  
   If selected, the labels will show the [minimum value and maximum value](#AxisValue) defined in the Axis sub tab.

**Gap**

Specifies the gap properties for the data labels.

* **Label Axis Gap**  
   Specifies the distance between the data label and the axis, in inches.
* **Best Effect**  
   Specifies whether to adjust the data labels automatically to make them placed best. If the option is selected, some labels will be hidden when they are overlapped.

**Font**

Specifies the font format of text in the data labels.

* **Font**  
   Lists all the available font faces that can be selected to apply to the text.
* **Size**  
   Specifies the font size of the text.
* **Fill Type**Specifies the fill type of the text. It can be one of the following: none, color, texture, and gradient.
* **Color**   
   Specifies the font color of the text. Disabled when Use Range Color in the Axis sub tab is selected.
* **Font Style**Specifies the font style of the text. It can be one of the following: plain, bold, italic, and bold italic.
* **Transparency**  
   Specifies the transparency for color of the text. Disabled when Use Range Color in the Axis sub tab is selected.

**Orientation**

* **Angle**  
   Specifies the rotation angle of the data labels.

### Format

Specifies the data format of the major tick mark labels.

![Format Dial Gauge dialog - Axis - Format](https://devnet.logianalytics.com/hc/article_attachments/4404885474967/fmtdlgauge_axis_fmt.gif)

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

The value **auto** means the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009777861-Chart-Properties#AutoScale). When you set the property to **true**, the specified format will apply to the integer part of the values after being scaled; but if the specified format conflicts with the Number data type, Logi Report will ignore the Auto Scale in Number setting.

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

Specifies the properties of the pointers in the dial gauge.

![Format Dial Gauge dialog - Pointer](https://devnet.logianalytics.com/hc/article_attachments/4404885475223/fmtdlgauge_pnt.gif)

**Pointer Style**

Specifies the style of the pointers.

* **Arrow**  
   Specifies to use arrow as the pointer style.
  + **Value Pointer**  
     Specifies the style of the value pointers. Select a style from the drop-down list or select Customized to specify another image as the value pointers in the [Insert Image](https://devnet.logianalytics.com/hc/en-us/articles/1500009747622-Insert-Image-Dialog-Box-Properties) dialog box.
  + **Width**   
     Specifies the width of the arrow.
  + **Height**   
     Specifies the height of the arrow.
* **Mark**  
   Specifies to use mark as the pointer style.
  + **Value Pointer**  
     Specifies the style of the value pointers. Select a style from the drop-down list or select Customized to specify another image as the value pointers in the [Insert Image](https://devnet.logianalytics.com/hc/en-us/articles/1500009747622-Insert-Image-Dialog-Box-Properties) dialog box.
  + **Width**   
     Specifies the width of the marks.
  + **Height**   
     Specifies the height of the marks.
  + **Position**   
     Specifies the position relationship of the marks and the dial.
  + **Gap**   
     Specifies the distance between the pointer and the dial, in inches.
* **Style List**  
   Opens the [Style List](https://devnet.logianalytics.com/hc/en-us/articles/1500009748122-Style-List-Dialog-Box-Properties) dialog box to specify the style for pointers in the same data series respectively.

**Pointer Color**

Specifies color properties of the pointers.

* **Color**  
   Specifies the color of the pointers.
* **Color List**   
   Opens the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009775061-Color-List-Dialog-Box-Properties) dialog box for you to specify the pointer color.
* **Transparency**  
   Specifies the transparency for color of the pointers.
* **Use Range Color**  
   Specifies whether to use the color [defined for the ranges](#Range) as the pointer color. If the option is selected, the three properties above will be disabled.

**Pointer Value**

Specifies the pointer value properties.

* **Show Pointer Value**   
   Specifies whether to show the pointer values.
  + **Position**  
     Specifies the position relationship between the values and the pointers. Select the position from the drop-down list. If customized is selected, the X and Y settings in the General tab of the [Format Pointer Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009775641-Format-Pointer-Label-Dialog-Box-Properties#General) dialog box will take effect.

**Pointer Border**

Specifies the pointer border properties.

* **Show Pointer Border**  
   Specifies whether to show the border of the pointers. When it is selected, the following border properties are enabled.
  + **Line Style**Specifies the line style to apply to the border.
  + **Color**  
     Specifies the color of the border.
  + **Transparency**Specifies the transparency for color of the border.
  + **Thickness**Specifies the weight of the border, in inches.

## Target Tab Properties

Specifies the properties of the target in the dial gauge.

![Format Dial Gauge dialog - Target](https://devnet.logianalytics.com/hc/article_attachments/4404885475479/fmtdlgauge_tgt.gif)

**Use Target Value**

Specifies whether to use the target value for the dial gauge.

* **Target Value**   
   Specifies the target value. You can also use a formula to control the value.

**Pointer Style**

Specifies the pointer style for the target value.

* **Target Pointer**  
   Specifies the style of the target pointer. Select a style from the drop-down list or select Customized to specify another image as the target pointer in the [Insert Image](https://devnet.logianalytics.com/hc/en-us/articles/1500009747622-Insert-Image-Dialog-Box-Properties) dialog box.
* **Width**  
   Specifies the width of the target pointer.
* **Height**  
   Specifies the height of the target pointer.
* **Position**  
   Specifies the position of the target pointer relative to the dial.
* **Gap**  
   Specifies the distance between the target pointer and the dial.

**Pointer Color**

Specifies color properties of the target pointer.

* **Color**  
   Specifies the color of the target pointer.
* **Transparency**  
   Specifies the transparency for color of the target pointer.

**Target Value**

Specifies properties of the target value.

* **Show Target Value**  
   Specifies whether to show the target value on the dial gauge.
  + **Position**  
     Specifies the position of the target value relative to the dial. Select the position from the drop-down list. If customized is selected, the X and Y settings in the General tab of the [Format Target Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009775721-Format-Target-Label-Dialog-Box-Properties#General) dialog box will take effect.

## Frame Tab Properties

Specifies properties for the frame of the dial gauge chart.

![Format Dial Gauge dialog - Frame](https://devnet.logianalytics.com/hc/article_attachments/4404880376471/fmtdlgauge_frm.gif)

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
   Specifies whether to show names for the arcs in the dial gauge which are values of the field on its category axis. If the dial gauge contains no category field, the group name shows Report by default.
  + **Position**  
     Specifies the position of the names relative to the dial. Select the position from the drop-down list. If customized is selected, the X and Y settings in the General tab of the [Format Gauge Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009747222-Format-Gauge-Label-Dialog-Box-Properties#General) dialog box will take effect.

## Range Color Tab Properties

Specifies different colors to fill the dials in dial gauge in different ranges.

![Format Dial Gauge dialog - Range Color](https://devnet.logianalytics.com/hc/article_attachments/4404880376727/fmtdlgauge_rgclr.gif)

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

![Format Dial Gauge dialog - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404885476375/fmtdlgauge_hint.gif)

**Show Category and Series**

Specifies whether to include the category and series values in the data marker hint.

**Auto Scale in Number**

Specifies whether to automatically scale the values displayed in the data marker hint that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

The value **auto** means the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009777861-Chart-Properties#AutoScale).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009775461-Format-Category-X-Gridline-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009775501-Format-Donut-Dialog-Box-Properties)
