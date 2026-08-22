---
title: "Format Value (Y) Axis Dialog Box Properties"
id: 4405683654551
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683654551-Format-Value-Y-Axis-Dialog-Box-Properties
updated_at: 2022-01-27T07:58:43Z
---

# Format Value (Y) Axis Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690507031-Format-Target-Label-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683655703-Format-Value-Y2-Axis-Dialog-Box-Properties)

# Format Value (Y) Axis Dialog Box Properties

You can use the Format Value (Y) Axis dialog box to format the value (Y) axis of a chart (unavailable to pie or indicator chart). This topic describes the properties in the dialog box.

This topic contains the following sections:

* [Axis Tab Properties](#Axis)
* [Tick Mark Tab Properties](#Tick)
* [Font Tab Properties](#Font)
* [Orientation Tab Properties](#Orientation)
* [Format Tab Properties](#Format)

You see these elements on all the tabs:

**OK**

Select to apply any changes you made here and exit the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## Axis Tab Properties

Specify the general properties of the axis.

![Format Value (Y) Axis dialog box - Axis tab](https://devnet.logianalytics.com/hc/article_attachments/4420447314967/fmtvalueaxis_axis.gif)

**Option**

Specify the axis properties.

* **Minimum Value**  
   Specify the minimum value to display on the axis.
* **Maximum Value**  
   Specify the maximum value to display on the axis.
* **Increment**  
   Specify the difference between two adjacent values on the axis.
* **Number of Tick Marks**  
   Specify the number of tick marks to display on the axis.
* **Show Gridlines**  
   Select to show the horizontal gridlines in the chart.
* **Show Percent**  
   Select to show the value labels on the axis in percent. This property only applies to radar, bullet, bar/bench, line, and area charts that are not 100% stacked type.

**Line**

Specify the line style for the axis.

* **Color**  
   Specify the color of the axis.
* **Style**  
   Select the style of the axis.
* **Transparency**  
   Specify the transparency for the color of the axis.
* **Thickness**  
   Specify the thickness of the axis, in inches.

**Gap**

Specify the gap properties for the labels on the axis.

* **Label Axis Gap**  
   Specify the distance between the label and the axis, in inches.
* **Best Effect**  
   Select to adjust the labels on the axis automatically to place them in the best positions.

## Tick Mark Tab Properties

The tab consists of two sub tabs:

* [Major Tick Mark](#Majortm)
* [Minor Tick Mark](#Minortm)

### Major Tick Mark

Specify the properties of the major tick marks on the axis.

![Format Value (Y) Axis dialog box - Major Tick Mark tab](https://devnet.logianalytics.com/hc/article_attachments/4420447315223/fmtvalueaxis_mark_major.gif)

**Type**

Specify the type of the major tick marks on the axis.

* **None**  
   Select if you don't want to display major tick marks on the axis. In this case, you needn't specify the other major tick mark related properties.
* **Inside**  
   Select to display major tick marks inside the chart.
* **Outside**  
   Select to display major tick marks outside the chart.
* **Cross**  
   Select to display major tick marks across the axis.

**Line**

Specify the line properties of the major tick marks on the axis.

* **Correlate with Axis**  
  Select if you want the line properties of the major tick marks to correlate with [that of the axis](#Line) automatically.
  You can clear this property and customize the line properties.
  + **Color**  
     Specify the color of the major tick marks.
  + **Transparency**  
     Specify the transparency for the color of the major tick marks.
  + **Style**  
     Select the type of the major tick marks.
  + **Thickness**  
     Specify the thickness of the major tick marks, in inches.
* **Tick Mark Length**  
   Specify the length of the major tick marks, in inches.

**Option**

Specify the other properties of the major tick mark labels on the axis.

* **Show Major Tick Mark Labels**  
   Select to display the labels of the major tick marks on the axis and enable the following properties.
* **Label Every N Major Tick Marks**  
   Specify the frequency at which you want to label the major tick marks.
* **Show Axis Label Tips**  
   Select to display the complete label text when you hover over a label on the axis.
* **Number of Major Labels**  
   Specify the number of major tick mark labels to display on the axis.
  + **Auto**  
     Select to display all major tick mark labels.
  + **Fixed**  
     Select to customize the number of the major tick mark labels to display on the axis.

### Minor Tick Mark

Specify the properties of the minor tick marks on the axis.

![Format Value (Y) Axis dialog box - Minor Tick Mark tab](https://devnet.logianalytics.com/hc/article_attachments/4420453635735/fmtvalueaxis_mark_minor.gif)

**Type**

Specify the type of the minor tick marks on the axis.

* **None**  
   Select if you don't want to display minor tick marks on the axis. In this case, you needn't specify the other minor tick mark related properties.
* **Inside**  
   Select to display minor tick marks inside the chart.
* **Outside**  
   Select to display minor tick marks outside the chart.
* **Cross**  
   Select to display minor tick marks across the axis.

**Line**

Specify the line properties of the minor tick marks on the axis.

* **Correlate with Axis**  
   Select if you want the line properties of the minor tick marks to correlate with [that of the axis](#Line) automatically.
  You can clear this property and customize the line properties.
  + **Color**  
     Specify the color of the minor tick marks.
  + **Style**  
     Select the type of the minor tick marks.
  + **Transparency**  
     Specify the transparency for the color of the minor tick marks.
  + **Thickness**  
     Specify the thickness of the minor tick marks, in inches.
* **Tick Mark Length**  
   Specify the length of the minor tick marks, in inches.

## Font Tab Properties

Specify the font format for text in the major tick mark labels on the axis.

![Format Value (Y) Axis dialog box - Font tab](https://devnet.logianalytics.com/hc/article_attachments/4420461704855/fmtvalueaxis_font.gif)

**Font**

Select the font face of the label text.

**Size**

Specify the font size of the label text.

**Fill Type**

Select the fill type of the label text: none, color, texture, and gradient.

**Color**

Specify the color of the label text. It takes effect when **Fill Type** on this tab is **color**.

**Font Style**

Select the font style of the label text: plain, bold, italic, and bold italic.

**Transparency**

Specify the color transparency of the label text.

## Orientation Tab Properties

Specify the rotation angle of the major tick mark labels on the axis.

![Format Value (Y) Axis dialog box - Orientation tab](https://devnet.logianalytics.com/hc/article_attachments/4420447315479/fmtvalueaxis_orntatn.gif)

**Automatic**

Select to adjust the rotation angle of the label text on the axis automatically according to the length of the label text, in degrees.

* If the text can completely display horizontally, the default rotation angle will be 0.
* If the text cannot completely display horizontally, the default rotation angle will be 30 anticlockwise. Server displays an ellipsis (…) from the right side of the label, along with part of the name instead of the entire name.

**Angle**

Specify the rotation angle of the label text on the axis.

## Format Tab Properties

Specify the data format of the major tick mark labels on the axis. See [Format](https://devnet.logianalytics.com/hc/en-us/articles/4405683824279-Format-Bar-Gauge-Dialog-Box-Properties#Format).

![Format Value (Y) Axis dialog box - Format tab](https://devnet.logianalytics.com/hc/article_attachments/4420453635991/fmtvalueaxis_fmt.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690507031-Format-Target-Label-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683655703-Format-Value-Y2-Axis-Dialog-Box-Properties)
