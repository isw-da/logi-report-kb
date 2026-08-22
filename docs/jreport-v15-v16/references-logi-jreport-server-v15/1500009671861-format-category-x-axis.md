---
title: "Format Category (X) Axis"
id: 1500009671861
section: "References Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009671861-Format-Category-X-Axis
updated_at: 2021-07-24T20:54:32Z
---

# Format Category (X) Axis

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009672081-Font)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009647382-Format-Category-X-Gridline)

# Format Category (X) Axis

The Format Category (X) Axis dialog appears when you right-click a chart and then select Format Axes (unavailable to pie, indicator, heat map and org charts) > Format Category (X) Axis from the shortcut menu. It helps you to format the category (X) axis of the chart, and consists of the following tabs:

* [Axis](#Axis)
* [Tick Mark](#Tick)
* [Font](#Font)
* [Orientation](#Orientation)
* [Format](#Format)

**OK**

Applies the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920501783/btn_help.gif)

Displays the help document about this feature.

![](https://devnet.logianalytics.com/hc/article_attachments/4404926700311/btn_close.gif)

Ignores the setting and closes this dialog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Axis

This tab shows some general information of the axis. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404926722967/fmtctgryaxis_axis.gif)

**Option**

Specifies the options for the axis.

* **Minimum Value**  
   Specifies the minimum value that is to be displayed on the axis. Available only to bubble charts which use the axis to show numeric data.
* **Maximum Value**  
   Specifies the maximum value that is to be displayed on the axis. Available only to bubble charts which use the axis to show numeric data.
* **Increment**  
   Specifies the difference between two adjacent values on the axis. Available only to bubble charts which use the axis to show numeric data.
* **Number of Tick Marks**  
   Specifies how many tick marks to be displayed on the axis. Available only to bubble charts which use the axis to show numeric data.
* **Show Gridlines**  
   Specifies whether to show the horizontal gridlines in the chart.

**Scrollable Chart**

Specifies whether to make the chart scrollable. If checked, a scrollbar will be added in the chart, with which you can control the visible value range on the axis. Available to 2-D charts of bar, bench, line, area and stock types only.

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

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Tick Mark

The tab consists of three sub tabs:

* [Major Tick Mark](#Majortm)
* [Minor Tick Mark](#Minortm)
* [Scale](#Scale)

### Major Tick Mark

Specifies properties of the major tick marks on the axis. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404926723223/fmtctgryaxis_mark_major.gif)

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

![](https://devnet.logianalytics.com/hc/article_attachments/4404920540823/fmtctgryaxis_mark_minor.gif)

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
   If checked, the line properties of the minor tick marks will correlate with [that of the axis](#Line) automatically.
  + **Color**  
     Specifies the color of the minor tick marks.
  + **Style**  
     Specifies the type of the minor tick marks.
  + **Transparency**  
     Specifies the transparency of the minor tick marks.
  + **Thickness**  
     Specifies the thickness of the minor tick marks, in inches.
* **Tick Mark Length**  
   Specifies the length of the minor tick marks, in inches.

**Option**

Specifies the other properties of the minor tick marks on the axis.

* **Show Minor Tick Mark Labels**  
   Specifies whether to display the labels of the minor tick marks on the axis. If checked, the following two properties will be enabled.
* **Label Every N Minor Tick Marks**  
   Specifies the frequency at which the minor tick marks will be labeled.
* **Number of Minor Labels**  
   Specifies how many minor tick mark labels to be displayed on the axis.
  + **Auto**  
     If checked, all minor tick mark labels will be shown.
  + **Fixed**  
     If checked, you can specify the number of the minor tick mark labels to be displayed on the axis.

### Scale

Customizes the way in which to label the tick marks on the axis. Available only when the field on the category axis is one of the following types: Number, Date, DateTime, and Time, and not applied when the category axis is used to show numeric data in bubble charts. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920541335/fmtctgryaxis_mark_scale.gif)

**Use Constant Interval**

Specifies whether to use a constant interval to label the tick marks. If checked, the values of the tick marks will be increased continually on the axis based on the following properties, instead of just using the data values.

**Minimum**

Specifies the minimum value which will be used to label the tick marks.

* **Auto**  
   If checked, the minimum value will be defined by Logi JReport automatically.
* **Fixed**  
   If checked, you can define the minimum value as required. Input the value in the text box, or select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920382743/btn_wbrpt_fmla.gif) to select a field from the drop-down list to control it. You can also specify it in the calendar if the field on the category axis is of Date, DateTime or Time type.

**Maximum**

Specifies the maximum value which will be used to label the tick marks.

* **Auto**  
   If checked, the maximum value will be defined by Logi JReport automatically.
* **Fixed**  
   If checked, you can define the maximum value as required. Input the value in the text box, or select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920382743/btn_wbrpt_fmla.gif) to select a field from the drop-down list to control it. You can also specify it in the calendar if the field on the category axis is of Date, DateTime or Time type.

**Major Unit**

Specifies the unit between two adjacent major tick marks.

* **Auto**  
   If checked, the unit will be defined by Logi JReport automatically.
* **Fixed**  
   If checked, you can define the unit as required. Input the value in the text box, or choose the desired one from the drop-down list if the field on the category axis is of Date, DateTime or Time type.

**Minor Unit**

Specifies the unit between two adjacent minor tick marks.

* **Auto**  
   If checked, the unit will be defined by Logi JReport automatically.
* **Fixed**  
   If checked, you can define the unit as required. Input the value in the text box, or choose the desired one from the drop-down list if the field on the category axis is of Date, DateTime or Time type.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Font

The tab consists of two sub tabs:

* [Major Label](#Majorft)
* [Minor Label](#Minorft)

### Major Label

Specifies the font format of the major tick mark labels on the axis. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920541591/fmtctgryaxis_font_major.gif)

**Font**

Specifies the font face of the label text.

**Size**

Specifies the font size of the label text.

**Fill Type**

Specifies the fill type of the label text. It can be one of the following: None, Color, Texture and Gradient.

**Color**

Specifies the color of the label text. It takes effect only when Fill Type in this tab is Color.

**Transparency**

Specifies the transparency of the label text.

**Font Style**

Specifies the font style of the text. It can be one of the following: Plain, Bold, Italic and Bold Italic.

### Minor Label

Specifies the font format of the minor tick mark labels on the axis. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404926723735/fmtctgryaxis_font_minor.gif)

**Correlate with Major Label**

If checked, the font format of the minor tick mark labels will correlate with that of the major tick mark labels automatically. Only when it is unchecked can the font properties of the minor tick mark labels take effect.

**Font**

Specifies the font face of the label text.

**Size**

Specifies the font size of the label text.

**Fill Type**

Specifies the fill type of the label text. It can be one of the following: None, Color, Texture and Gradient.

**Color**

Specifies the color of the label text. It takes effect only when Fill Type in this tab is Color.

**Transparency**

Specifies the transparency of the label text.

**Font Style**

Specifies the font style of the text. It can be one of the following: Plain, Bold, Italic and Bold Italic.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Orientation

The tab consists of two sub tabs:

* [Major Label](#Majorlb)
* [Minor Label](#Minorlb)

### Major Label

Specifies the rotation angle of the major tick mark labels on the axis. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404926724375/fmtctgryaxis_orntatn_major.gif)

**Automatic**

Specifies to adjust the rotation angle of the major tick mark label text on the axis automatically according to the length of the label text, in degrees.

When this option is checked by default:

* If the text can be completely displayed horizontally, the default rotation angle will be 0.
* If the text cannot be completely displayed horizontally, the default rotation angle will be 30 anticlockwise, and the cut off part will be shown as suspension points.

**Angle**

Specifies to customize the rotation angle of the major tick mark label text on the axis.

### Minor Label

Specifies the rotation angle of the minor tick mark labels on the axis. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404926725015/fmtctgryaxis_orntatn_minor.gif)

**Correlate with Major Label**

If checked, the orientation setting of the minor tick mark labels will correlate with that of the major tick mark labels automatically. Only when it is unchecked can the orientation properties of the minor tick mark labels take effect.

**Automatic**

Specifies to adjust the rotation angle of the minor tick mark label text on the axis automatically according to the length of the label text, in degrees.

When this option is checked by default:

* If the text can be completely displayed horizontally, the default rotation angle will be 0.
* If the text cannot be completely displayed horizontally, the default rotation angle will be 30 anticlockwise, and the cut off part will be shown as suspension points.

**Angle**

Specifies to customize the rotation angle of the minor tick mark label text on the axis.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Format

The tab consists of two sub tabs:

* [Major Label](#Majorfmt)
* [Minor Label](#Minorfmt)

### Major Label

Specifies the data format of the major tick mark labels on the axis. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920542231/fmtctgryaxis_fmt_major.gif)

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

### Minor Label

Specifies the data format of the minor tick mark labels on the axis. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404926725399/fmtctgryaxis_fmt_minor.gif)

**Correlate with Major Label**

If checked, the data format of the minor tick mark labels will correlate with that of the major tick mark labels automatically. Only when it is unchecked can the format properties of the minor tick mark labels take effect.

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

Applies the specified format in the Stack list box to the minor tick mark labels.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009672081-Font)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009647382-Format-Category-X-Gridline)
