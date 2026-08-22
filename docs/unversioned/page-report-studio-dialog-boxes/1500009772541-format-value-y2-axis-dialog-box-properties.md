---
title: "Format Value (Y2) Axis Dialog Box Properties"
id: 1500009772541
section: "Page Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009772541-Format-Value-Y2-Axis-Dialog-Box-Properties
updated_at: 2021-07-24T00:49:12Z
---

# Format Value (Y2) Axis Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009772521-Format-Value-Y-Axis-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009772221-Formula-Editor-Properties)

# Format Value (Y2) Axis Dialog Box Properties

You can use the Format Value (Y2) Axis dialog box to format the value (Y2) axis of a chart (unavailable to pie or indicator chart). This topic describes the options in the dialog box.

This topic contains the following sections:

* [Axis Tab Properties](#Axis)
* [Tick Mark Tab Properties](#Tick)
* [Font Tab Properties](#Font)
* [Orientation Tab Properties](#Orientation)
* [Format Tab Properties](#Format)

**OK**

Applies the changes and closes the dialog box.

**Cancel**

Does not retain any changes and closes the dialog box.

**Help**

Displays the help document about this feature.

## Axis Tab Properties

Specifies the general properties for the axis.

![Format Value (Y2) Axis dialog - Axis tab](https://devnet.logianalytics.com/hc/article_attachments/4404885562135/fmtvalueaxis2_axis.gif)

**Option**

Specifies the options for the axis.

* **Minimum Value**  
   Specifies the minimum value that is to be displayed on the axis.
* **Maximum Value**  
   Specifies the maximum value that is to be displayed on the axis.
* **Increment**  
   Specifies the difference between two adjacent values on the axis.
* **Number of Tick Marks**  
   Specifies how many tick marks to be displayed on the axis.
* **Show Gridlines**  
  Specifies whether to show the horizontal gridlines in the chart.
* **Show Percent**  
   Specifies whether to show the value labels on the axis in percent. Only applies to radar, bullet, bar/bench, line, and area chart that are not 100% stacked type.

**Line**

Specifies the line style for the axis.

* **Color**  
   Specifies the color of the axis.
* **Style**  
   Specifies the style of the axis.
* **Transparency**  
  Specifies the transparency for the color of the axis.
* **Thickness**  
   Specifies the thickness of the axis, in inches.

**Gap**

Specifies the gap properties for the labels on the axis.

* **Label Axis Gap**  
   Specifies the distance between the label and the axis, in inches.
* **Best Effect**  
   Specifies whether to adjust the labels on the axis automatically to make them placed best.

## Tick Mark Tab Properties

The tab consists of two sub tabs:

* [Major Tick Mark](#Majortm)
* [Minor Tick Mark](#Minortm)

### Major Tick Mark

Specifies the properties of the major tick marks on the axis.

![Format Value (Y2) Axis dialog - Major Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4404885562391/fmtvalueaxis2_mark_major.gif)

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
  + **Transparency**  
     Specifies the transparency for the color of the major tick marks.
  + **Style**  
     Specifies the type of the major tick marks.
  + **Thickness**  
     Specifies the thickness of the major tick marks, in inches.
* **Tick Mark Length**  
   Specifies the length for the major tick marks, in inches.

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

Specifies the properties of the minor tick marks on the axis.

![Format Value (Y2) Axis dialog - Minor Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4404885562903/fmtvalueaxis2_mark_minor.gif)

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

Specifies the line properties of the minor tick marks on the axis.

* **Correlate with Axis**  
   If the option is selected, the line properties of the minor tick marks will correlate with [that of the axis](#Line) automatically.
  + **Color**  
     Specifies the color of the minor tick marks.
  + **Style**  
     Specifies the type of the minor tick marks.
  + **Transparency**  
     Specifies the transparency for the color of the minor tick marks.
  + **Thickness**  
     Specifies the thickness of the minor tick marks, in inches.
* **Tick Mark Length**  
   Specifies the length of the minor tick marks, in inches.

## Font Tab Properties

Specifies the font format for text in the major tick mark labels on the axis.

![Format Value (Y2) Axis dialog - Font tab](https://devnet.logianalytics.com/hc/article_attachments/4404880498711/fmtvalueaxis2_font.gif)

**Font**

Specifies the font face of the label text.

**Size**

Specifies the font size of the label text.

**Fill Type**

Specifies the fill type of the label text.

**Color**

Specifies the color of the label text.

**Transparency**

Specifies the transparency for the color of the label text.

**Font Style**

Specifies the font style of the text. It can be one of the following: Plain, Bold, Italic and Bold Italic.

## Orientation Tab Properties

Specifies the rotation angle of the major tick mark labels on the axis.

![Format Value (Y2) Axis dialog - Orientation tab](https://devnet.logianalytics.com/hc/article_attachments/4404885563799/fmtvalueaxis2_orntatn.gif)

**Automatic**

Specifies whether to adjust the rotation angle of the label text on the axis automatically according to the length of the label text, in degrees.

When this option is selected by default:

* If the text can be completely displayed horizontally, the default rotation angle will be 0.
* If the text cannot be completely displayed horizontally, the default rotation angle will be 30 anticlockwise, and the cut off part will be shown as suspension points.

**Angle**

Specifies to customize the rotation angle of the label text on the axis.

## Format Tab Properties

Specifies data format of the major tick mark labels on the axis.

![Format Value (Y2) Axis dialog - Format tab](https://devnet.logianalytics.com/hc/article_attachments/4404885564311/fmtvalueaxis2_fmt.gif)

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

Displays the selected format effects.

**Stack**

Lists all the formats you select from different categories.

**Add**

Adds a format to the Stack list box.

**Remove**

Removes a format from the Stack list box.

**Apply**

Applies the specified format in the Stack list box to the major tick mark labels.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009772521-Format-Value-Y-Axis-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009772221-Formula-Editor-Properties)
