---
title: "Format Value (Y) Axis Dialog Box"
id: 4405661600023
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661600023-Format-Value-Y-Axis-Dialog-Box
updated_at: 2022-01-27T20:35:34Z
---

# Format Value (Y) Axis Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661598999-Format-Text-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661602455-Format-Value-Y-Gridline-Dialog-Box)

# Format Value (Y) Axis Dialog Box

You can use the Format Value (Y) Axis dialog box to [format the value (Y) axis of a chart](https://devnet.logianalytics.com/hc/en-us/articles/4405664375831-Formatting-the-Axes#Value). This topic describes the options in the dialog box.

Designer displays the Format Value (Y) Axis dialog box when you right-click any chart element and navigate to Format Axes > Format Value (Y) Axis on the shortcut menu, or double-click the value axis of a chart.

The dialog box contains the following tabs:

* [Axis Tab](#Axis)
* [Tick Mark Tab](#Tick)
* [Font Tab](#Font)
* [Orientation Tab](#Orientation)
* [Format Tab](#Format)

You see these buttons in the tabs:

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Apply**

Select to apply all changes and leave the dialog box open.

**Help**

Select to view information about the dialog box.

## Axis Tab

Use this tab to specify the general properties of the value axis.

![Format Value (Y) Axis - Axis](https://devnet.logianalytics.com/hc/article_attachments/4420550894359/fmtvalueaxis_axis.gif)

**Option**

You can specify the axis options in this box.

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
  Select to show the value labels on the axis in percent. Designer applies this option only when the chart is a radar or bullet chart, or a bar/bench, line, or area chart that is not of the 100% Stacked type.

**Line**

You can specify the line style for the axis in this box.

* **Color**  
  Specify the color of the axis. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value of a color (for example, 0xff0000) in the text box.
* **Style**  
  Select the line style for the axis.
* **Transparency**  
  Specify the transparency for the color of the axis.
* **Thickness**  
  Specify the thickness for the line of the axis, in pixels.

**Label**

You can specify options for the labels on the axis in this box.

* **Label Axis Gap**  
  Specify the distance between the labels and the axis, in pixels.
* **Best Effect**  
  Select to adjust the labels automatically to place them at the best position on the axis. When you select this option, Designer hides some labels if they overlap.

## Tick Mark Tab

You see the following subtabs in the Tick Mark tab:

* [Major Tick Mark Subtab](#Majortm)
* [Minor Tick Mark Subtab](#Minortm)

### Major Tick Mark Subtab

Use this subtab to specify properties of the major tick marks on the value axis.

![Format Value (Y) Axis - Major Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4420556158103/fmtvalueaxis_mark_major.gif)

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
  Select to apply the [line properties](#Line) that you define for the axis in the Axis tab to the major tick marks. When you clear this option, you can specify the line properties for the major tick marks separately using the following options:
  + **Color**  
    Specify the color of the major tick mark line. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value of a color (for example, 0xff0000) in the text box.
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
  Select to display the complete label text when you point to a label on the axis.
* **Number of Major Labels**  
  Specify how many major tick mark labels to display on the axis.
  + **Auto**  
    Select to display all the major tick mark labels.
  + **Fixed**  
    Select and specify the number of the major tick mark labels you want to display.

### Minor Tick Mark Subtab

Use this subtab to specify properties of the minor tick marks on the value axis.

![Format Value (Y) Axis - Minor Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4420542122903/fmtvalueaxis_mark_minor.gif)

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
  Select to apply the [line properties](#Line) that you define for the axis in the Axis tab to the minor tick marks. When you clear this option, you can specify the line properties for the minor tick marks separately using the following options:
  + **Color**  
    Specify the color of the minor tick mark line. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value of a color (for example, 0xff0000) in the text box.
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

![Format Value (Y) Axis - Font](https://devnet.logianalytics.com/hc/article_attachments/4420556158359/fmtvalueaxis_font.gif)

**Font**

You can specify the font format of the text in the major tick mark labels in this box.

* **Font list**  
  This drop-down list contains all the font faces that you can select to apply to the text.
* **Font Size**  
  Specify the font size of the text.
* **Font Color**  
  Specify the font color of the text. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value of a color (for example, 0xff0000) in the text box.
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

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) Web Report Studio and JDashboard do not support underlining chart text, therefore, this property is ignored when the chart runs in Web Report Studio or is used in a dashboard.

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

This box displays a preview sample based on your selections.

## Orientation Tab

Use this tab to specify the rotation angle of the major tick mark labels on the value axis.

![Format Value (Y) Axis - Orientation](https://devnet.logianalytics.com/hc/article_attachments/4420550895255/fmtvalueaxis_orntatn.gif)

**Automatic**

Select to adjust the rotation angle of the major tick mark label text on the axis automatically according to the length of the text, in degrees.

**Angle**

Select and specify the rotation angle of the major tick mark label text on the axis in the text box. When you change the rotation angle in the text box, the red line in the spin box changes correspondingly, and vice versa.

## Format Tab

Use this tab to specify the data format of the major tick mark labels on the value axis.

![Format Value (Y) Axis - Format](https://devnet.logianalytics.com/hc/article_attachments/4420556158743/fmtvalueaxis_fmt.gif)

**Category & Format**

These two boxes list the [category types and the formats of each category](https://devnet.logianalytics.com/hc/en-us/articles/4405664452759-Data-Format-Dialog-Box#DataFormat) that Designer provides by default. Select a category and a format for this category, then select **Add** to add it as the format of the category. You can add only one format for each category.

**Properties**

This text box shows the properties of the format that you select in the Format box. If the default formats Designer provides for a category cannot meet your requirement, you can define your own format in the text box and select **Add** to add it as the format of the category.

**Auto Scale in Number**

Specify whether to automatically scale the Number values that fall into the two ranges:

* When 1000 <= value < 10^15, Logi Report Engine applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Logi Report Engine uses scientific notation to scale the values.

By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property [on the chart in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/4405664650263-Chart-Properties#AutoScale) for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661598999-Format-Text-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661602455-Format-Value-Y-Gridline-Dialog-Box)
