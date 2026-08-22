---
title: "Format Series (Z) Axis Dialog Box"
id: 5735529792151
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735529792151-Format-Series-Z-Axis-Dialog-Box
updated_at: 2022-11-02T04:18:02Z
---

# Format Series (Z) Axis Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735523198999-Format-Scatter-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735543021975-Format-Series-Z-Gridline-Dialog-Box)

# Format Series (Z) Axis Dialog Box

You can use the Format Series (Z) Axis dialog box to [format the series axis (the Z axis) of a chart](https://devnet.logianalytics.com/hc/en-us/articles/5735527158935-Formatting-Chart-Axes#Series). This topic describes the options in the dialog box.

Designer displays the Format Series (Z) Axis dialog box when you right-click any chart element and navigate to Format Axes > Format Series (Z) Axis on the shortcut menu, or double-click the series axis of a chart.

This dialog box contains the following tabs:

* [Axis Tab](#Axis)
* [Tick Mark Tab](#Tick)
* [Font Tab](#Font)
* [Orientation Tab](#Orientation)
* [Format Tab](#Format)

Designer displays these buttons in all the tabs:

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Apply**

Select to apply all changes and leave the dialog box open.

**Help**

Select to view information about the dialog box.

## Axis Tab

Use this tab to specify the general properties of the series axis.

![Format Series (Z) Axis dialog box - Axis](https://devnet.logianalytics.com/hc/article_attachments/9898480052503/fmtseriesaxis_axis.gif)

**Option**

You can specify the axis options in this box.

* **Draw Axis Only**  
  Select if you do not want to show labels on the axis. Keep this option cleared if you want to draw the axis with labels.
* **Number of Labels**  
  Specify how many labels to display on the axis.
* **Show Axis Label Tips**  
  Select to display the complete label text when you point to a label on the axis.
* **Label Every N Tick Marks**  
  Specify to display a label every N tick marks.
* **Show Gridlines**  
  Select to show gridlines on the axis.

**Line**

You can specify line properties of the axis in this box.

* **Color**  
  Specify the color of the axis line. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette), or type the hexadecimal value of a color (for example, 0xff0000) in the text box.
* **Style**  
  Select the line style of the axis.
* **Transparency**  
  Specify the transparency of the axis line.
* **Thickness**  
  Specify the thickness of the axis line, in pixels.

**Label**

You can specify options for the labels on the axis in this box.

* **Label Axis Gap**  
  Specify the distance between the labels and the axis, in pixels.
* **Best Effect**  
  Select to adjust the labels automatically to place them at the best position on the axis. When you select this option, Designer hides some labels if they overlap.
* **Auto**  
  Designer enables this option if the axis displays a field, and uses the values of the field as the major tick mark labels on the axis by default. Clear it if you want to customize the label text.
  + **Label Text**  
    Specify the text of the major tick mark labels on the axis. Select a field from the drop-down list to use its values as the label text or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/9898459676183/btn_x.gif) and type the label text manually.

## Tick Mark Tab

Use this tab to specify properties of the tick marks on the series axis.

![Format Series (Z) Axis dialog box - Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/9898462982039/fmtseriesaxis_mark.gif)

**Tick Mark**

You can specify line properties of the tick marks in this box.

* **Correlate with Axis**  
  Select to apply the [line properties](#Line) that you define for the axis in the Axis tab to the tick marks. When you clear this option, you can specify line properties of the tick marks separately using the following options:
  + **Color**  
    Specify the color of the tick marks. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette), or type the hexadecimal value of a color (for example, 0xff0000) in the text box.
  + **Style**  
    Select the line style of the tick marks.
  + **Transparency**  
    Specify the transparency of the tick marks.
  + **Thickness**  
    Specify the thickness of the tick marks, in pixels.

**Major Tick Mark**

You can specify properties of the major tick marks on the axis in this box.

* **None**  
  Select if you do not want to display major tick marks on the axis.
* **Inside**  
  Select to display the major tick marks inside the axis.
* **Outside**  
  Select to display the major tick marks outside the axis.
* **Cross**  
  Select to display the major tick marks across the axis.
* **Major Tick Length**  
  Specify the length of the major tick marks on the axis.

**Minor Tick Mark**

You can specify properties of the minor tick marks on the axis in this box.

* **None**  
  Select if you do not want to display minor tick marks on the axis.
* **Inside**  
  Select to display the minor tick marks inside the axis.
* **Outside**  
  Select to display the minor tick marks outside the axis.
* **Cross**  
  Select to display the minor tick marks across the axis.
* **Major Tick Length**  
  Specify the length of the minor tick marks on the axis.

## Font Tab

Use this tab to specify the font style of the major tick mark labels on the series axis.

![Format Series (Z) Axis dialog box - Font](https://devnet.logianalytics.com/hc/article_attachments/9898462986647/fmtseriesaxis_font.gif)

**Font**

You can specify the font style of the text in the major tick mark labels in this box.

* **Font list**  
  This drop-down list contains all the font faces you can select to apply to the text.
* **Font Size**  
  Specify the font size of the text.
* **Font Color**  
  Specify the font color of the text. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette), or type the hexadecimal value of a color (for example, 0xff0000) in the text box.
* **Transparency**  
  Specify the transparency of the text.
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

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) Web Report Studio and JDashboard do not support underlining chart text, therefore, this property is ignored when the chart runs in Web Report Studio or is used in a dashboard.

* **Superscript**  
  Select to raise the text above the baseline and change the text to a smaller font size, if a smaller size is available.
* **Subscript**  
  Select to lower the text below the baseline and change the text to a smaller font size, if a smaller size is available.
* **Embossed**  
  Select to make the text appear to be raised off the page in relief.
* **Engraved**  
  Select to make the text appear to be imprinted or pressed into the page.
* **Outlined**  
  Select to display the exterior border around each character of the text.
* **Shadowed**  
  Select to add a shadow beneath and to the right of the text.

**Sample**

This box displays a preview sample based on your selections.

## Orientation Tab

Use this tab to specify the rotation angle of the major tick mark labels on the series axis.

![Format Series (Z) Axis dialog box - Orientation](https://devnet.logianalytics.com/hc/article_attachments/9898462990743/fmtseriesaxis_orntatn.gif)

**Automatic**

Select to adjust the rotation angle of the major tick mark labels on the axis automatically according to the length of the label text, in degrees.

**Angle**

Select and specify the rotation angle of the major tick mark labels on the axis in the text box. When you change the rotation angle in the text box, the red line in the spin box changes correspondingly, and vice versa.

## Format Tab

Use this tab to specify the data format of the major tick mark labels on the series axis.

![Format Series (Z) Axis dialog box - Format](https://devnet.logianalytics.com/hc/article_attachments/9898480084375/fmtseriesaxis_fmt.gif)

**Category & Format**

These two boxes list the [category types and the formats of each category](https://devnet.logianalytics.com/hc/en-us/articles/5735500256407-Data-Format-Dialog-Box#DataFormat) that Designer provides by default. Select a category and a format for this category, then select **Add** to add it as the format of the category. You can add only one format for each category.

**Properties**

This text box shows the properties of the format that you select in the Format box. If the default formats Designer provides for a category cannot meet your requirement, you can define your own format in the text box and select **Add** to add it as the format of the category.

**Auto Scale in Number**

Specify whether to automatically scale the Number values that fall into the two ranges:

* When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.

By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property [on the chart in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/5735545992599-Chart-Properties#AutoScale) for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.

**Sample**

This box displays a sample for the selected format.

**Stack**

This box lists all the formats that you select from different categories.

**Add**

Select to add a format to the Stack box.

**Remove**

Select to remove the specified format from the Stack box.

**Apply**

Select to apply the specified format to the major tick mark labels.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735523198999-Format-Scatter-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735543021975-Format-Series-Z-Gridline-Dialog-Box)
