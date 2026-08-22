---
title: "Format Value (Y) Axis Dialog Box Properties"
id: 5741429791639
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741429791639-Format-Value-Y-Axis-Dialog-Box-Properties
updated_at: 2022-10-31T17:17:32Z
---

# Format Value (Y) Axis Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741465630999-Format-Target-Label-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741445492119-Format-Value-Y-Gridline-Dialog-Box-Properties)

# Format Value (Y) Axis Dialog Box Properties

This topic describes how you can use the Format Value (Y) Axis dialog box to format the value (Y) axis of a chart. Server displays the dialog box when you right-click a chart and select **Format Axes** (unavailable to pie, indicator, heat map, and org charts) > **Format Value (Y) Axis** from the shortcut menu.

This topic contains the following sections:

* [Axis Tab Properties](#Axis)
* [Tick Mark Tab Properties](#Tick)
* [Font Tab Properties](#Font)
* [Orientation Tab Properties](#Orientation)
* [Format Tab Properties](#Format)

You see these elements on all the tabs:

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

## Axis Tab Properties

Specify the general properties for the axis.

![Format Value (Y) Axis dialog box - Axis tab](https://devnet.logianalytics.com/hc/article_attachments/9905719126295/fmtvalueaxis_axis.gif)

**Option**

Specify the axis properties.

* **Minimum Value**  
   Specify the minimum value you want to display on the axis.
* **Maximum Value**  
   Specify the maximum value you want to display on the axis.
* **Increment**  
   Specify the difference between two adjacent values on the axis.
* **Number of Tick Marks**  
   Specify the number of tick marks you want to display on the axis.
* **Show Gridlines**  
  Select if you want to show the horizontal gridlines in the chart.
* **Show Percent**  
   Select if you want to show the value labels on the axis in percent. This property only applies to bullet, bar/bench, line, and area charts that are not 100% stacked type.

**Line**

Specify the line properties for the axis.

* **Color**  
   Specify the color of the line.
* **Style**  
   Specify the style of the line.
* **Transparency**  
  Specify the transparency for the color of the line.
* **Thickness**  
   Specify the thickness of the line, in inches.

**Gap**

Specify the gap properties for the labels on the axis.

* **Label Axis Gap**  
   Specify the distance between the label and the axis, in inches.
* **Best Effect**  
   Select if you want to adjust the labels on the axis automatically to make them placed best.

## Tick Mark Tab Properties

The tab consists of two sub tabs:

* [Major Tick Mark](#Majortm)
* [Minor Tick Mark](#Minortm)

### Major Tick Mark

Specify the properties of the major tick marks on the axis.

![Format Value (Y) Axis dialog box - Major Tick Mark tab](https://devnet.logianalytics.com/hc/article_attachments/9905730884375/fmtvalueaxis_mark_major.gif)

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
     Specify the line color.
  + **Style**  
     Select the line type.
  + **Transparency**  
     Specify the transparency for the line color.
  + **Thickness**  
     Specify the line thickness in inches.
* **Tick Mark Length**  
   Specify the line length in inches.

**Option**

Specify the other properties of the major tick mark labels on the axis.

* **Show Major Tick Mark Labels**  
   Select if you want to display the labels of the major tick marks on the axis. Then, Server enables the following properties.
* **Label Every N Major Tick Marks**  
   Specify the frequency at which you want to label the major tick marks.
* **Show Axis Label Tips**  
   Select if you want to display the complete label text when you hover over a label on the axis.
* **Number of Major Labels**  
   Specify the number of major tick mark labels you want to display on the axis.
  + **Auto**  
     Select if you want all major tick mark labels to show.
  + **Fixed**  
     Select and then you can specify the number of the major tick mark labels to display on the axis.

### Minor Tick Mark

Specify the properties of the minor tick marks on the axis.

![Format Value (Y) Axis dialog box - Minor Tick Mark tab](https://devnet.logianalytics.com/hc/article_attachments/9905719166743/fmtvalueaxis_mark_minor.gif)

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
     Specify the line color.
  + **Style**  
     Select the line type.
  + **Transparency**  
     Specify the transparency for the line color.
  + **Thickness**  
     Specify the line thickness in inches.
* **Tick Mark Length**  
   Specify the line length in inches.

## Font Tab Properties

Specify the font format for text in the major tick mark labels on the axis.

![Format Value (Y) Axis dialog box - Font tab](https://devnet.logianalytics.com/hc/article_attachments/9905730943127/fmtvalueaxis_font.gif)

**Font**

Specify the font face of the label text.

**Size**

Specify the font size of the label text.

**Fill Type**

Select the fill type of the label text: None, Color, Texture, or Gradient.

**Color**

Specify the color of the label text. It takes effect only when Fill Type in this tab is Color.

**Transparency**

Specify the color transparency of the label text.

**Font Style**

Select the font style of the label text: Plain, Bold, Italic, or Bold Italic.

## Orientation Tab Properties

Specify the rotation angle of the major tick mark labels on the axis.

![Format Value (Y) Axis dialog box - Orientation tab](https://devnet.logianalytics.com/hc/article_attachments/9905719216407/fmtvalueaxis_orntatn.gif)

**Automatic**

Select if you want to adjust the rotation angle of the major tick mark label text on the axis automatically according to the length of the label text, in degrees.

* If the text can completely display horizontally, the default rotation angle will be 0.
* If the text cannot completely display horizontally, the default rotation angle will be 30 anticlockwise. Server displays an ellipsis (…) from the right side of the label, along with part of the name instead of the entire name.

**Angle**

Select and then customize the rotation angle of the major tick mark label text on the axis.

## Format Tab Properties

Specify the data format of the major tick mark labels on the axis. See [Format](https://devnet.logianalytics.com/hc/en-us/articles/5741450135575-Format-Bar-Gauge-Dialog-Box-Properties#Format).

![Format Value (Y) Axis dialog box - Format tab](https://devnet.logianalytics.com/hc/article_attachments/9905719291799/fmtvalueaxis_fmt.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741465630999-Format-Target-Label-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741445492119-Format-Value-Y-Gridline-Dialog-Box-Properties)
