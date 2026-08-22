---
title: "Format Bar Gauge Dialog Box Properties"
id: 4405683824279
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683824279-Format-Bar-Gauge-Dialog-Box-Properties
updated_at: 2022-01-27T07:59:18Z
---

# Format Bar Gauge Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683823255-Format-Bar-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683825559-Format-Bench-Dialog-Box-Properties)

# Format Bar Gauge Dialog Box Properties

This topic describes how you can use the Format Bar Gauge dialog box to format the bar gauges in a bar gauge chart. Server displays the dialog box when you right-click on a bar gauge chart and select **Format Graph** from the shortcut menu.

This topic contains the following sections:

* [Staff Graph Tab Properties](#Staff)
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

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4420447202071/btn_help.gif)

Select to view information about the Format Bar Gauge dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420447202455/btn_close.gif)

Select to close the dialog box without saving any changes.

## Staff Graph Tab Properties

Specifies the properties for bars in the bar gauge.

![Format Bar Gauge dialog - Staff Graph](https://devnet.logianalytics.com/hc/article_attachments/4420447245847/fmtbargauge_stfgraph.gif)

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
   Specifies the color of the border. To change the color, select the color indicator to select a new color from the color palette, or select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/4405683802391-Color-Picker-Dialog-Box-Properties) dialog box in which you can select a color within a wider range.
* **Transparency**  
   Specifies the transparency for the border color.

**Show Range Name**

Specifies whether to show the names of the ranges defined in the [Range Color](#Range) tab. When it is selected you can continue to specify the font properties of the text in the range names.

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

Specifies the properties of the axis in the bar gauge.

![Format Bar Gauge dialog - Axis - Axis tab](https://devnet.logianalytics.com/hc/article_attachments/4420461647383/fmtbargauge_axis_axis.gif)

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
   Specifies the minimum value to be displayed in the chart. You can also use a formula to control the property.
* **Maximum Value**  
   Specifies the maximum value to be displayed in the chart. You can also use a formula to control the property.

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

* **Staff Axis Gap**   
   Specifies the gap between the axis and the bar when the axis is not in the center of the bar. The option is disabled when Type is set to center in the tab.

### Tick Mark

Specifies the properties of the tick marks on the axis.

![Format Bar Gauge dialog - Axis - Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4420453581975/fmtbargauge_axis_tkmk.gif)

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

Specifies the properties of the major tick mark labels.

![Format Bar Gauge dialog - Axis - Label](https://devnet.logianalytics.com/hc/article_attachments/4420447246615/fmtbargauge_axis_lbl.gif)

**Option**

Specifies the type of the labels.

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
       Select and specify the number of the major tick mark labels to display on the axis.
* **Range Value**  
   Select if you want the labels to show the [range values](#Range) you define.

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
   Specifies the rotation angle of the data labels.

### Format

Specifies the data format of the major tick mark labels.

![Format Bar Gauge dialog - Axis - Format](https://devnet.logianalytics.com/hc/article_attachments/4420461648151/fmtbargauge_axis_fmt.gif)

**Category**

Select a category type to customize its format.

**Format**

Select a [format](https://devnet.logianalytics.com/hc/en-us/articles/4405683807895-Data-Format-Dialog-Box-Properties#DataFormat), and then select **Add** to add it as the format of the specified category. You can add only one format for each category.

**Properties**

Server displays the properties of the format you select. If the formats listed in the **Format** box cannot meet your requirement, define the format in the **Properties** text box, and then select **Add** to add it as the format of the specified category.

**Auto Scale in Number**

Select **true** if you want to automatically scale the values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

The default value **auto** means that the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/4411830859799-Setting-Web-Report-Object-Properties-Using-the-Inspector-Panel#AutoScale). When you set the property to **true**, the specified format will apply to the integer part of the values after being scaled. If the specified format conflicts with the Number data type, Logi Report will ignore the **Auto Scale in Number** setting.

**Sample**

Server displays a preview sample of your settings.

**Stack**

Server displays all the formats you select for different categories.

**Add**

Select to add a format to the **Stack** box.

**Remove**

Select to remove a format from the **Stack** box.

**Apply**

Select to apply the specified format in the **Stack** box to the major tick mark labels.

## Pointer Tab Properties

Specifies the properties of the pointers in the bar gauge.

![Format Bar Gauge dialog - Pointer](https://devnet.logianalytics.com/hc/article_attachments/4420461648407/fmtbargauge_pnt.gif)

**Use Pointer**

Specifies to use pointers to indicate values in the bar gauge.

* **Pointer Style**  
   Specifies properties of the pointers.
  + **Value Pointer**  
     Specifies the style of the value pointers. Select a style from the drop-down list or select Customized to specify another image as the value pointers in the [Insert Image](https://devnet.logianalytics.com/hc/en-us/articles/4405683856151-Insert-Image-Dialog-Box-Properties) dialog box.
  + **Width**  
     Specifies the width of the pointers.
  + **Height**  
     Specifies the height of the pointers.
  + **Position**  
     Specifies the position of the pointers relative to the bar.
  + **Gap**  
     Specifies the distance between the pointers and the bar.
  + **Style List**  
     Opens the [Style List](https://devnet.logianalytics.com/hc/en-us/articles/4405683886359-Style-List-Dialog-Box-Properties) dialog box to specify the style for pointers in the same data series respectively.
* **Pointer Color**  
   Specifies color properties of the pointers.
  + **Color**  
     Specifies the color of the pointers.
  + **Color List**   
     Opens the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/4405683801367-Color-List-Dialog-Box-Properties) dialog box to specify the color pattern for pointers in the same data series respectively.
  + **Transparency**  
     Specifies the transparency for color of the pointers.
  + **Use Range Color**  
     Specifies whether to use the color [defined for the ranges](#Range) as the pointer color. If the option is selected, the preceding three properties will be disabled.
* **Pointer Value**  
  Specifies properties for values of the pointers.
  + **Show Pointer Value**  
     Specifies whether to show values for the pointers.
    - **Position**  
       Specifies the position relationship between the values and the pointers. Select the position from the drop-down list. If customized is selected, the X and Y settings in the General tab of the [Format Pointer Label](https://devnet.logianalytics.com/hc/en-us/articles/4405690586647-Format-Pointer-Label-Dialog-Box-Properties#General) dialog box will take effect.
* **Pointer Border**  
   Specifies the pointer border properties.
  + **Show Pointer Border**  
     Specifies whether to show the border of the pointers. When it is selected, the following border properties are enabled.
    - **Line Style**Specifies the line style to apply to the border.
    - **Color**  
       Specifies the color of the border.
    - **Transparency**Specifies the transparency for color of the border.
    - **Thickness**Specifies the weight of the border, in inches.

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
     Opens the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/4405683801367-Color-List-Dialog-Box-Properties) dialog box to specify the color pattern for color bars in the same data series respectively.
* **Pointer Value**  
  Specifies properties for values of the color bars.
  + **Show Pointer Value**  
     Specifies whether to show values for the color bars.
  + **Position**  
     Specifies the position relationship between the values and the color bars. Select the position from the drop-down list. If customized is selected, the X and Y settings in the General tab of the [Format Pointer Label](https://devnet.logianalytics.com/hc/en-us/articles/4405690586647-Format-Pointer-Label-Dialog-Box-Properties#General) dialog box will take effect.
* **Pointer Border**  
  Specifies the pointer border properties.
  + **Show Pointer Border**  
     Specifies whether to show the border of the pointers. When it is selected, the following border properties are enabled.
    - **Line Style**Specifies the line style to apply to the border.
    - **Color**  
       Specifies the color of the border.
    - **Transparency**Specifies the transparency for color of the border.
    - **Thickness**Specifies the weight of the border, in inches.

## Target Tab Properties

Specifies the properties of the target in the bar gauge.

![Format Bar Gauge dialog - Target](https://devnet.logianalytics.com/hc/article_attachments/4420447248151/fmtbargauge_tgt.gif)

**Use Target Value**

Specifies whether to use the target value for the bar gauge.

* **Target Value**   
   Specifies the target value. You can also use a formula to control the value.

**Pointer Style**

Specifies the pointer style for the target value.

* **Target Pointer**  
   Specifies the style of the target pointer. Select a style from the drop-down list or select Customized to specify another image as the target pointer in the [Insert Image](https://devnet.logianalytics.com/hc/en-us/articles/4405683856151-Insert-Image-Dialog-Box-Properties) dialog box.
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
     Specifies the position of the target value relative to the bar. Select the position from the drop-down list. If customized is selected, the X and Y settings in the General tab of the [Format Target Label](https://devnet.logianalytics.com/hc/en-us/articles/4405683842455-Format-Target-Label-Dialog-Box-Properties#General) dialog box will take effect.

## Frame Tab Properties

Specifies properties for the frame of the bar gauge chart.

![Format Bar Gauge dialog - Frame](https://devnet.logianalytics.com/hc/article_attachments/4420453582615/fmtbargauge_frm.gif)

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
   Specifies whether to show names for the bars in the bar gauge which are values of the field on its category axis. If the bar gauge contains no category field, the group name shows Report by default.
  + **Position**  
     Specifies the position of the names relative to the bars. Select the position from the drop-down list. If customized is selected, the X and Y settings in the General tab of the [Format Gauge Label](https://devnet.logianalytics.com/hc/en-us/articles/4405683832215-Format-Gauge-Label-Dialog-Box-Properties#General) dialog box will take effect.

## Range Color Tab Properties

Specifies different colors to fill the bars in bar gauge in different ranges.

![Format Bar Gauge dialog - Range Color](https://devnet.logianalytics.com/hc/article_attachments/4420461650455/fmtbargauge_rgclr.gif)

**Use Gradient Effect**

Specifies whether to use gradient effect for the color.

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

![Format Bar Gauge dialog - Hint](https://devnet.logianalytics.com/hc/article_attachments/4420461650711/fmtbargauge_hint.gif)

**Show Category and Series**

Select to include the category and series values in the data marker hint.

**Auto Scale in Number**

Specifies whether to automatically scale the values displayed in the data marker hint that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

The default value **auto** means that the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/4411830859799-Setting-Web-Report-Object-Properties-Using-the-Inspector-Panel#AutoScale).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683823255-Format-Bar-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683825559-Format-Bench-Dialog-Box-Properties)
