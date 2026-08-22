---
title: "Format Value(Y) Axis Dialog Box"
id: 1500010097301
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010097301-Format-Value-Y-Axis-Dialog-Box
updated_at: 2021-07-23T19:15:34Z
---

# Format Value(Y) Axis Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010059402-Format-Text-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010059442-Format-Value-Y-Gridline-Dialog-Box)

# Format Value (Y) Axis Dialog Box

You can use the Format Value (Y) Axis dialog box to [format the value (Y) axis of a chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010094441-Formatting-the-Axes#Value). This topic describes the options in the dialog box.

Designer displays the Format Value (Y) Axis dialog box when you right-click any chart element and select Format Axes > Format Value (Y) Axis from the shortcut menu, or double-click the value axis of a chart.

The dialog box contains the following tabs:

* [Axis Tab](#Axis)
* [Tick Mark Tab](#Tick)
* [Font Tab](#Font)
* [Orientation Tab](#Orientation)
* [Format Tab](#Format)

You see these buttons in all the tabs:

**OK**

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Apply**

Select to apply all changes and leave the dialog box open.

**Help**

Select to view information about the dialog box.

## Axis Tab

Use this tab to specify the general properties of the value axis.

![Format Value (Y) Axis - Axis](https://devnet.logianalytics.com/hc/article_attachments/4404848534295/fmtvalueaxis_axis.gif)

**Option**

You can specify the options for the axis in this box.

* **Minimum Value**  
  Specify the minimum value to display on the axis.
* **Maximum Value**  
  Specify the maximum value to display on the axis.
* **Increment**  
  Specify the distance between two adjacent values on the axis.
* **Number of Tick Marks**  
  Specify how many tick marks to display on the axis.
* **Show Gridlines**  
  Select to show gridlines on the axis.
* **Show Percent**  
  Select to show the value labels on the axis in percent. Designer applies this option only if the chart is a radar or bullet chart, or a bar/bench, line, or area chart that is not of the 100% Stacked type.

**Line**

You can specify the line style for the axis in this box.

* **Color**  
  Specify the color of the axis. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Style**  
  Select the line style for the axis.
* **Transparency**  
  Specify the transparency for the color of the axis.
* **Thickness**  
  Specify the thickness for the line of the axis, in pixels.

**Label**

You can specify the properties for the labels on the axis in this box.

* **Label Axis Gap**  
  Specify the distance between the labels and the axis, in pixels.
* **Best Effect**  
  Select to adjust the labels automatically to have them placed in the best way. If you select the option, Designer hides some labels when they overlap.

## Tick Mark Tab

You see the following sub tabs in the Tick Mark tab:

* [Major Tick Mark Sub Tab](#Majortm)
* [Minor Tick Mark Sub Tab](#Minortm)

### Major Tick Mark Sub Tab

Use this sub tab to specify the properties of the major tick marks on the value axis.

![Format Value (Y) Axis - Major Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4404856929047/fmtvalueaxis_mark_major.gif)

**Type**

You can specify the type of the major tick marks on the axis in this box.

* **None**  
  Select if you do not want to display major tick marks on the axis. It is meaningless to specify all the other major tick mark properties if you select this type.
* **Inside**  
  Select to display the major tick marks inside the axis.
* **Outside**  
  Select to display the major tick marks outside the axis.
* **Cross**  
  Select to display the major tick marks across the axis.

**Line**

You can specify the line properties of the major tick marks on the axis in this box.

* **Correlate with Axis**  
  Select to apply the [line properties](#Line) that you define for the axis in the Axis tab to the major tick marks. If you clear the option, you can specify the line properties for the major tick marks separately using the following options:
  + **Color**  
    Specify the color of the major tick mark line. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
  + **Style**  
    Select the style of the major tick mark line.
  + **Transparency**  
    Specify the transparency for the color of the major tick mark line.
  + **Thickness**  
    Specify the thickness of the major tick mark line, in pixels.
* **Tick Mark Length**  
  Specify the length of the major tick marks, in pixels.

**Option**

You can specify the other properties of the major tick mark labels on the axis in this box.

* **Show Major Tick Mark Labels**  
  Select to display the labels of the major tick marks on the axis. Designer enables the other options in the Options box when you select this option.
* **Label Every N Major Tick Marks**  
  Specify the frequency at which to label the major tick marks.
* **Show Axis Label Tips**  
  Select to display the complete label text when the mouse pointer points at a label on the axis.
* **Number of Major Labels**  
  Specify how many major tick mark labels to display on the axis.
  + **Auto**  
    Select to display all the major tick mark labels.
  + **Fixed**  
    Select and specify the number of the major tick mark labels you want to display.

### Minor Tick Mark Sub Tab

Use this sub tab to specify the properties of the minor tick marks on the value axis.

![Format Value (Y) Axis - Minor Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4404856929303/fmtvalueaxis_mark_minor.gif)

**Type**

You can specify the type of the minor tick marks on the axis in this box.

* **None**  
  Select if you do not want to display minor tick marks on the axis. It is meaningless to specify all the other minor tick mark properties if you select this type.
* **Inside**  
  Select to display the minor tick marks inside the axis.
* **Outside**  
  Select to display the minor tick marks outside the axis.
* **Cross**  
  Select to display the minor tick marks across the axis.

**Line**

You can specify the line properties of the minor tick marks on the axis in this box.

* **Correlate with Axis**  
  Select to apply the [line properties](#Line) that you define for the axis in the Axis tab to the minor tick marks. If you clear the option, you can specify the line properties for the minor tick marks separately using the following options:
  + **Color**  
    Specify the color of the minor tick mark line. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
  + **Style**  
    Select the style of the minor tick mark line.
  + **Transparency**  
    Specify the transparency for the color of the minor tick mark line.
  + **Thickness**  
    Specify the thickness of the minor tick mark line, in pixels.
* **Tick Mark Length**  
  Specify the length of the minor tick marks, in pixels.

## Font Tab

Use this tab to specify the font format of the major tick mark labels on the value axis.

![Format Value (Y) Axis - Font](https://devnet.logianalytics.com/hc/article_attachments/4404848534935/fmtvalueaxis_font.gif)

**Font**

You can specify the font format of the text in the major tick mark labels in this box.

* **Font list**  
  The drop-down list contains all the font faces that you can select to apply to the text.
* **Font Size**  
  Specify the font size of the text.
* **Font Color**  
  Specify the font color of the text. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Transparency**  
  Specify the color transparency of the text.
* **Rotation**  
  Specify the rotation angle of the text around its center, in degrees. The default value is 0.
* **Shearing**  
  Specify the gradient of the text.

**Effects**

You can specify the special effects of the text in the major tick mark labels in this box.

* **Style**  
  Select the font style of the text. It can be one of the following: plain, bold, italic, and bold italic.
* **Strikethrough**  
  Select the style of the horizontal line using which to strikethrough the text. It can be one of the following: none, thin line, bold line, and double lines.
* **Underline**  
  Select the style of the horizontal line under the text. It can be one of the following: none, single, single lower, bold line, bold lower, double lines, bold double, patterned line, and bold patterned. When you select "patterned line" or "bold patterned", Designer draws a line or bold line in the pattern of the text.

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4404856819991/criticalicon.gif) Web Report Studio and JDashboard do not support underlining chart text, therefore, Logi Report Engine ignores this property when the chart runs in Web Report Studio or is used in a dashboard.

* **Superscript**  
  Select to raise the text above the baseline and change the text to a smaller font size, if a smaller size is available.
* **Embossed**  
  Select to make the text appear to be raised off the page in relief.
* **Outlined**  
  Select to display the inner and outer borders of each character.
* **Subscript**  
  Select to lower the text below the baseline and change the text to a smaller font size, if a smaller size is available.
* **Engraved**  
  Select to make the text appear to be imprinted or pressed into the page.
* **Shadowed**  
  Select to add a shadow beneath and to the right of the text.

**Sample**

The box displays a preview sample of your selection.

## Orientation Tab

Use this tab to specify the rotation angle of the major tick mark labels on the value axis.

![Format Value (Y) Axis - Orientation](https://devnet.logianalytics.com/hc/article_attachments/4404856929815/fmtvalueaxis_orntatn.gif)

**Automatic**

Select to adjust the rotation angle of the major tick mark label text on the axis automatically according to the length of the text, in degrees.

**Angle**

Select and specify the rotation angle of the major tick mark label text on the axis in the text box. When you change the rotation angle in the text box, the red line in the spin box changes correspondingly, and vice versa.

## Format Tab

Use this tab to specify the data format of the major tick mark labels on the value axis.

![Format Value (Y) Axis - Format](https://devnet.logianalytics.com/hc/article_attachments/4404848535447/fmtvalueaxis_fmt.gif)

**Category & Format**

The two boxes list the [category types and the formats of each category](https://devnet.logianalytics.com/hc/en-us/articles/1500010096081-Data-Format-Dialog-Box#DataFormat) that Designer provides by default. Select a category and a format for this category, then select Add to add it as the format of the category. You can add only one format for each category.

**Properties**

The text box shows the properties of the format that you select in the Format box. If the default formats Designer provides for a category cannot meet your requirement, you can define your own format in the text box and select Add to add it as the format of the category.

**Auto Scale in Number**

Specify whether to automatically scale the Number values which fall into the following two ranges:

* When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.

By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property [on the chart in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#AutoScale) for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.

**Sample**

The box displays a sample for the selected format.

**Stack**

The box lists all the formats that you select from different categories.

**Add**

Select to add a format to the Stack box.

**Remove**

Select to remove the specified format from the Stack box.

**Apply**

Select to apply the specified format to the major tick mark labels.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010059402-Format-Text-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010059442-Format-Value-Y-Gridline-Dialog-Box)
