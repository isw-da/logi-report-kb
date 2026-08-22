---
title: "Format Category (X) Axis Dialog Box Properties"
id: 4405683827735
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683827735-Format-Category-X-Axis-Dialog-Box-Properties
updated_at: 2022-01-27T07:59:18Z
---

# Format Category (X) Axis Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683826711-Format-Bubble-Gauge-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683828759-Format-Category-X-Gridline-Dialog-Box-Properties)

# Format Category (X) Axis Dialog Box Properties

This topic describes how you can use the Format Category (X) Axis dialog box to format the category (X) axis of a chart. Server displays the dialog box when you right-click a chart and then select **Format Axes** (unavailable to pie, indicator, heat map, and org charts) > **Format Category (X) Axis** from the shortcut menu.

This topic contains the following sections:

* [Axis Tab Properties](#Axis)
* [Tick Mark Tab Properties](#Tick)
* [Font Tab Properties](#Font)
* [Orientation Tab Properties](#Orientation)
* [Format Tab Properties](#Format)

You see these elements on all the tabs:

**OK**

Select **OK** to apply any changes you made here.

**Cancel**

Select **Cancel** to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4420447202071/btn_help.gif)

Select to view information about the Format Category (X) Axis dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420447202455/btn_close.gif)

Select to close the dialog box without saving any changes.

## Axis Tab Properties

This tab shows some general information of the axis.

![Format Category (X) Axis dialog - Axis](https://devnet.logianalytics.com/hc/article_attachments/4420453577367/fmtctgryaxis_axis.gif)

**Option**

Specifies the options for the axis.

* **Minimum Value**  
   Specifies the minimum value that is to be displayed on the axis. Available only to bubble chart in which no field is specified on the Bubble X-Axis.
* **Maximum Value**  
   Specifies the maximum value that is to be displayed on the axis. Available only to bubble chart in which no field is specified on the Bubble X-Axis.
* **Increment**  
   Specifies the difference between two adjacent values on the axis. Available only to bubble chart in which no field is specified on the Bubble X-Axis.
* **Number of Tick Marks**  
   Specifies how many tick marks to be displayed on the axis. Available only to bubble chart in which no field is specified on the Bubble X-Axis.
* **Show Gridlines**  
   Specifies whether to show the horizontal gridlines in the chart.

**Scrollable Chart**

Specifies whether to make the chart scrollable. If the option is selected, a scrollbar will be added in the chart, with which you can control the visible value range on the axis. Available to 2D charts of bar, bench, line, area and stock types only.

* **Scrollable Visible Values**  
   Specifies how many data items will be selected on the scrollbar and displayed on the axis by default.
* **Scrolling Area Percentage**   
   Specifies the percentage the scrollbar occupies the whole size of the chart.
* **Show Chart in Scrolling Area**   
   Specifies whether to show the thumbnail chart on the scrollbar.

**Line**

Specifies the line style for the axis.

* **Color**  
   Specifies the color of the axis.
* **Style**  
   Specifies the style for the line of the axis.
* **Transparency**  
  Specifies the transparency for the color of the axis.
* **Thickness**  
   Specifies the thickness for the line of the axis, in inches.

**Gap**

Specifies the gap properties for the labels on the axis.

* **Label Axis Gap**   
   Specifies the distance between the label and the axis, in inches.
* **Best Effect**  
   Specifies whether to adjust the labels automatically to make them placed best.
* **Auto**  
   If selected, the major tick mark labels on the axis are values of the field displayed on the axis. You can clear it to customize the label text.
  + **Label Text**  
     Specifies the text of the major tick mark labels on the axis. Type the desired label text manually or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4420447036695/btn_wbrpt_fmla.gif) to select a field from the drop-down list to use its values as the label text.

## Tick Mark Tab Properties

The tab consists of three sub tabs:

* [Major Tick Mark](#Majortm)
* [Minor Tick Mark](#Minortm)
* [Scale](#Scale)

### Major Tick Mark

Specifies properties of the major tick marks on the axis.

![Format Category (X) Axis dialog - Tick Mark - Major Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4420453577623/fmtctgryaxis_mark_major.gif)

**Type**

Specifies the type of the major tick marks on the axis.

* **None**  
   If selected, major tick marks will not be shown on the axis and it will be meaningless to specify all the other major tick mark related properties.
* **Inside**  
   If selected, major tick marks will be inside the chart.
* **Outside**  
   If selected, major tick marks will be outside the chart.
* **Cross**  
   If selected, major tick marks will be across the axis.

**Line**

Specifies the line properties of the major tick marks on the axis.

* **Correlate with Axis**  
   If the option is selected, the line properties of the major tick marks will correlate with [that of the axis](#Line) automatically.
  + **Color**  
     Specifies the color of the major tick marks.
  + **Style**  
     Specifies the type of the major tick marks.
  + **Transparency**  
     Specifies the transparency for the color of the major tick marks.
  + **Thickness**  
     Specifies the thickness of the major tick marks, in inches.
* **Tick Mark Length**  
   Specifies the length of the major tick marks, in inches.

**Option**

Specifies the other properties of the major tick mark labels on the axis.

* **Show Major Tick Mark Labels**  
   Specifies whether to display the labels of the major tick marks on the axis. If the option is selected, the following properties will be enabled.
* **Label Every N Major Tick Marks**  
   Specifies the frequency at which the major tick marks will be labeled.
* **Show Axis Label Tips**  
   Specifies whether to display the complete label text when the mouse pointer points at a label on the axis.
* **Number of Major Labels**  
   Specifies how many major tick mark labels to be displayed on the axis.
  + **Auto**  
     If the option is selected, all major tick mark labels will be shown.
  + **Fixed**  
     If the option is selected, you can specify the number of the major tick mark labels to be displayed on the axis.

### Minor Tick Mark

Specifies properties of the minor tick marks on the axis.

![Format Category (X) Axis dialog - Tick Mark - Minor Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4420453577879/fmtctgryaxis_mark_minor.gif)

**Type**

Specifies the type of the minor tick marks on the axis.

* **None**  
   If selected, minor tick marks will not be shown on the axis and it will be meaningless to specify all the other minor tick mark related properties.
* **Inside**  
   If selected, minor tick marks will be inside the chart.
* **Outside**  
   If selected, minor tick marks will be outside the chart.
* **Cross**  
   If selected, minor tick marks will be across the axis.

**Line**

Specifies the line properties for the minor tick marks on the axis.

* **Correlate with Axis**  
   If the option is selected, the line properties of the minor tick marks will correlate with [that of the axis](#Line) automatically.
  + **Color**  
     Specifies the color of the minor tick marks.
  + **Style**  
     Specifies the type of the minor tick marks.
  + **Transparency**  
     Specifies the color transparency of the minor tick marks.
  + **Thickness**  
     Specifies the thickness of the minor tick marks, in inches.
* **Tick Mark Length**  
   Specifies the length of the minor tick marks, in inches.

**Option**

Specifies the other properties of the minor tick marks on the axis.

* **Show Minor Tick Mark Labels**  
   Specifies whether to display the labels of the minor tick marks on the axis. It takes effect only when Use Constant Interval in the Scale sub tab of the Tick Mark tab is selected. If the option is selected, the following two properties will be enabled.
* **Label Every N Minor Tick Marks**  
   Specifies the frequency at which the minor tick marks will be labeled.
* **Number of Minor Labels**  
   Specifies how many minor tick mark labels to be displayed on the axis.
  + **Auto**  
     If the option is selected, all minor tick mark labels will be shown.
  + **Fixed**  
     If the option is selected, you can specify the number of the minor tick mark labels to be displayed on the axis.

### Scale

Customizes the way in which to label the major and minor tick marks on the axis with constant interval. This sub tab is activated only when the field on the category axis is one of the following types: Number, Date, DateTime, and Time (for a bubble chart only when the category field is one of the preceding types and the Bubble X-Axis uses the category field).

![Format Category (X) Axis dialog - Tick Mark - Scale](https://devnet.logianalytics.com/hc/article_attachments/4420453578135/fmtctgryaxis_mark_scale.gif)

**Use Constant Interval**

Specifies whether to use a constant interval to label the tick marks. If the option is selected, the values of the tick marks will be increased continually on the axis based on the following properties instead of just using the data values, and the [customized major tick mark labels](#LabelText) in the Axis tab are ignored.

**Minimum**

Specifies the minimum value which will be used to label the tick marks.

* **Auto**  
   If the option is selected, the minimum value will be defined by Logi Report automatically.
* **Fixed**  
   If the option is selected, you can define the minimum value as required. Type the value in the text box, or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4420447036695/btn_wbrpt_fmla.gif) to select a field from the drop-down list to control it. You can also select the **Calendar** icon ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4420461463447/btn_clndr.gif) to specify it using the calendar if the field on the category axis is of Date, DateTime, or Time type.

**Maximum**

Specifies the maximum value which will be used to label the tick marks.

* **Auto**  
   If the option is selected, the maximum value will be defined by Logi Report automatically.
* **Fixed**  
   If the option is selected, you can define the maximum value as required. Type the value in the text box, or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4420447036695/btn_wbrpt_fmla.gif) to select a field from the drop-down list to control it. You can also select the **Calendar** icon ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4420461463447/btn_clndr.gif) to specify it using the calendar if the field on the category axis is of Date, DateTime, or Time type.

**Major Unit**

Specifies the unit between two adjacent major tick marks.

* **Auto**  
   If the option is selected, the unit will be defined by Logi Report automatically.
* **Fixed**  
   If the option is selected, you can define the unit as required. Type the value in the text box, or choose the desired one from the drop-down list if the field on the category axis is of Date, DateTime or Time type.

**Minor Unit**

Specifies the unit between two adjacent minor tick marks.

* **Auto**  
   If the option is selected, the unit will be defined by Logi Report automatically.
* **Fixed**  
   If the option is selected, you can define the unit as required. Type the value in the text box, or choose the desired one from the drop-down list if the field on the category axis is of Date, DateTime or Time type.

## Font Tab Properties

The tab consists of two sub tabs:

* [Major Label](#Majorft)
* [Minor Label](#Minorft)

### Major Label

Specifies the font format of the major tick mark labels on the axis.

![Format Category (X) Axis dialog - Font - Major Label](https://devnet.logianalytics.com/hc/article_attachments/4420461646231/fmtctgryaxis_font_major.gif)

**Font**

Specifies the font face of the label text.

**Size**

Specifies the font size of the label text.

**Fill Type**

Specifies the fill type of the label text. It can be one of the following: None, Color, Texture, and Gradient.

**Color**

Specifies the color of the label text. It takes effect only when Fill Type in this tab is Color.

**Transparency**

Specifies the color transparency of the label text.

**Font Style**

Specifies the font style of the text. It can be one of the following: Plain, Bold, Italic and Bold Italic.

### Minor Label

Specifies the font format of the minor tick mark labels on the axis.

![Format Category (X) Axis dialog - Font - Minor Label](https://devnet.logianalytics.com/hc/article_attachments/4420447241495/fmtctgryaxis_font_minor.gif)

**Correlate with Major Label**

If the option is selected, the font format of the minor tick mark labels will correlate with that of the major tick mark labels automatically. Only when it is unselected can the font properties of the minor tick mark labels take effect.

**Font**

Specifies the font face of the label text.

**Size**

Specifies the font size of the label text.

**Fill Type**

Specifies the fill type of the label text. It can be one of the following: None, Color, Texture, and Gradient.

**Color**

Specifies the color of the label text. It takes effect only when Fill Type in this tab is Color.

**Transparency**

Specifies the color transparency of the label text.

**Font Style**

Specifies the font style of the text. It can be one of the following: Plain, Bold, Italic and Bold Italic.

## Orientation Tab Properties

The tab consists of two sub tabs:

* [Major Label](#Majorlb)
* [Minor Label](#Minorlb)

### Major Label

Specifies the rotation angle of the major tick mark labels on the axis.

![Format Category (X) Axis dialog - Orientation - Major Label](https://devnet.logianalytics.com/hc/article_attachments/4420447242135/fmtctgryaxis_orntatn_major.gif)

**Automatic**

Specifies to adjust the rotation angle of the major tick mark label text on the axis automatically according to the length of the label text, in degrees.

* If the text can completely display horizontally, the default rotation angle will be 0.
* If the text cannot completely display horizontally, the default rotation angle will be 30 anticlockwise. Server displays an ellipsis (…) from the right side of the label, along with part of the name instead of the entire name.

**Angle**

Specifies to customize the rotation angle of the major tick mark label text on the axis.

### Minor Label

Specifies the rotation angle of the minor tick mark labels on the axis.

![Format Category (X) Axis dialog - Orientation - Minor Label](https://devnet.logianalytics.com/hc/article_attachments/4420461646487/fmtctgryaxis_orntatn_minor.gif)

**Correlate with Major Label**

If the option is selected, the orientation setting of the minor tick mark labels will correlate with that of the major tick mark labels automatically. Only when it is unselected can the orientation properties of the minor tick mark labels take effect.

**Automatic**

Specifies to adjust the rotation angle of the minor tick mark label text on the axis automatically according to the length of the label text, in degrees.

When this option is selected by default:

* If the text can be completely displayed horizontally, the default rotation angle will be 0.
* If the text cannot be completely displayed horizontally, the default rotation angle will be 30 anticlockwise, and the cut off part will be shown as suspension points.

**Angle**

Specifies to customize the rotation angle of the minor tick mark label text on the axis.

## Format Tab Properties

The tab consists of two sub tabs:

* [Major Label](#Majorfmt)
* [Minor Label](#Minorfmt)

### Major Label

Specifies the data format of the major tick mark labels on the axis.

![Format Category (X) Axis dialog - Format - Major Label](https://devnet.logianalytics.com/hc/article_attachments/4420447243159/fmtctgryaxis_fmt_major.gif)

**Truncate**

Specifies whether to truncate the label text when the text is more than 10 characters.

For the other properties on this tab, see [Format Tab Properties](https://devnet.logianalytics.com/hc/en-us/articles/4405683640599-Format-Gauge-Label-Dialog-Box-Properties#Format).

### Minor Label

Specifies the data format of the minor tick mark labels on the axis.

![Format Category (X) Axis dialog - Format - Minor Label](https://devnet.logianalytics.com/hc/article_attachments/4420447243543/fmtctgryaxis_fmt_minor.gif)

**Correlate with Major Label**

If the option is selected, the data format of the minor tick mark labels will correlate with that of the major tick mark labels automatically. Only when it is unselected can the format properties of the minor tick mark labels take effect.

For the other properties on this tab, see [Format Tab Properties](https://devnet.logianalytics.com/hc/en-us/articles/4405683640599-Format-Gauge-Label-Dialog-Box-Properties#Format).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683826711-Format-Bubble-Gauge-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683828759-Format-Category-X-Gridline-Dialog-Box-Properties)
