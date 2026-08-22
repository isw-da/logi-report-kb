---
title: "Format Value (Y) Axis"
id: 1500009645162
section: "References Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009645162-Format-Value-Y-Axis
updated_at: 2021-07-24T20:55:09Z
---

# Format Value (Y) Axis

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009669741-Format-Platform)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009669761-Format-Value-Y2-Axis)

# Format Value (Y) Axis

The Format Value (Y) Axis dialog appears when you right-click a chart and select Format Axis (unavailable to pie or indicator chart) > Format Value (Y) Axis from the shortcut menu. It helps you to format the value (Y) axis of the chart and contains the following tabs:

* [Axis](#Axis)
* [Tick Mark](#Tick)
* [Font](#Font)
* [Orientation](#Orientation)
* [Format](#Format)

**OK**

Applies the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Axis

Specifies the general properties for the axis. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920626071/fmtvalueaxis_axis.gif)

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
   Specifies the thickness of the axis, in pixels.

**Gap**

Specifies the gap properties for the labels on the axis.

* **Label Axis Gap**  
   Specifies the distance between the label and the axis, in pixels.
* **Best Effect**  
   Specifies whether to adjust the labels on the axis automatically to make them placed best.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Tick Mark

The tab consists of two sub tabs:

* [Major Tick Mark](#Majortm)
* [Minor Tick Mark](#Minortm)

### Major Tick Mark

Specifies properties of the major tick marks on the axis. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920626583/fmtvalueaxis_mark_major.gif)

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
   If checked, the line properties of the major tick marks will correlate with [that of the axis](#Line) automatically.
  + **Color**  
     Specifies the color of the major tick marks.
  + **Transparency**  
     Specifies the transparency for the color of the major tick marks.
  + **Style**  
     Specifies the type of the major tick marks.
  + **Thickness**  
     Specifies the thickness of the major tick marks, in pixels.
* **Tick Mark Length**  
   Specifies the length for the major tick marks, in pixels.

**Option**

Specifies the other properties of the major tick mark labels on the axis.

* **Show Major Tick Mark Labels**  
   Specifies whether to display the labels of the major tick marks on the axis. If checked, the following properties will be enabled.
* **Label Every N Major Tick Marks**  
   Specifies the frequency at which the major tick marks will be labeled.
* **Show Axis Label Tips**  
   Specifies whether to display the complete label text when the mouse pointer points at a label on the axis.
* **Number of Major Labels**  
   Specifies how many major tick mark labels to be displayed on the axis.
  + **Auto**  
     If checked, all major tick mark labels will be shown.
  + **Fixed**  
     If checked, you can specify the number of the major tick mark labels to be displayed on the axis.

### Minor Tick Mark

Specifies properties of the minor tick marks on the axis. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404926769687/fmtvalueaxis_mark_minor.gif)

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
   If checked, the line properties of the minor tick marks will correlate with [that of the axis](#Line) automatically.
  + **Color**  
     Specifies the color of the minor tick marks.
  + **Style**  
     Specifies the type of the minor tick marks.
  + **Transparency**  
     Specifies the transparency for the color of the minor tick marks.
  + **Thickness**  
     Specifies the thickness of the minor tick marks, in pixels.
* **Tick Mark Length**  
   Specifies the length of the minor tick marks, in pixels.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Font

Specifies the font format for text in the major tick mark labels on the axis. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920626839/fmtvalueaxis_font.gif)

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

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Orientation

Specifies the rotation angle of the major tick mark labels on the axis. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920627095/fmtvalueaxis_orntatn.gif)

**Automatic**

Specifies whether to adjust the rotation angle of the label text on the axis automatically according to the length of the label text, in degrees.

When this option is checked by default:

* If the text can be completely displayed horizontally, the default rotation angle will be 0.
* If the text cannot be completely displayed horizontally, the default rotation angle will be 30 anticlockwise, and the cut off part will be shown as suspension points.

**Angle**

Specifies to customize the rotation angle of the label text on the axis.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Format

Specifies the data format of the major tick mark labels on the axis. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920627351/fmtvalueaxis_fmt.gif)

**Category**

Lists the category types. Select one to customize its format.

**Format**

Displays all the formats of the selected category. Select the required one and select Add to add it as the format of the specified category. You can add only one format for each category.

**Properties**

Displays the properties of the format you select. If the formats listed in the Format box cannot meet your requirement, define the format in the text field and then select Add to add it as the format of the specified category.

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

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009669741-Format-Platform)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009669761-Format-Value-Y2-Axis)
