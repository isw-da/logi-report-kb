---
title: "Format Series(Z) Axis Dialog Box"
id: 1500010097221
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010097221-Format-Series-Z-Axis-Dialog-Box
updated_at: 2021-07-23T19:15:33Z
---

# Format Series(Z) Axis Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010097201-Format-Scatter-Dialog-Box)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010097241-Format-Series-Z-Gridline-Dialog-Box)

# Format Series (Z) Axis Dialog Box

You can use the Format Series (Z) Axis dialog box to [format the series (Z) axis of a chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010094441-Formatting-the-Axes#Series). This topic describes the options in the dialog box.

Designer displays the Format Series (Z) Axis dialog box when you right-click any chart element and select Format Axes > Format Series (Z) Axis from the shortcut menu, or double-click the series axis of a chart.

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

Use this tab to specify the general properties of the series axis.

![Format Series (Z) Axis dialog box - Axis](https://devnet.logianalytics.com/hc/article_attachments/4404856936215/fmtseriesaxis_axis.gif)

**Option**

You can specify the options for the axis in this box.

* **Draw Axis Only**  
  Select if you do not want to show labels on the axis. Keep the option unselected if you want to draw the axis with labels.
* **Number of Labels**  
  Specify how many labels to display on the axis.
* **Show Axis Label Tips**  
  Select to display the complete label text when the mouse pointer points at a label on the axis.
* **Label Every N Tick Marks**  
  Specify to display a label every N tick marks.
* **Show Gridlines**  
  Select to show gridlines on the axis.

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
* **Auto**  
  Designer enables this option if the axis displays a field, and uses the values of the field as the major tick mark labels on the axis by default. Clear the option if you want to customize the label text.
  + **Label Text**  
    Specify the text of the major tick mark labels on the axis. Select a field from the drop-down list to use its values as the label text or select the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848471319/btn_x.gif) to type the label text manually.

## Tick Mark Tab

Use this sub tab to specify the properties of the tick marks on the series axis.

![Format Series (Z) Axis dialog box - Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4404856936471/fmtseriesaxis_mark.gif)

**Tick Mark**

You can specify the line properties of the tick marks in this box.

* **Correlate with Axis**  
  Select to apply the [line properties](#Line) that you define for the axis in the Axis tab to the tick marks. If you clear the option, you can specify the line properties for the tick marks separately using the following options:
  + **Color**  
    Specify the color of the major tick mark line. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
  + **Style**  
    Select the style of the major tick mark line.
  + **Transparency**  
    Specify the transparency for the color of the major tick mark line.
  + **Thickness**  
    Specify the thickness of the major tick mark line, in pixels.

**Major Tick Mark**

You can specify the properties of the major tick marks on the axis in this box.

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

You can specify the properties of the minor tick marks on the axis in this box.

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

Use this tab to specify the font format of the major tick mark labels on the series axis.

![Format Series (Z) Axis dialog box - Font](https://devnet.logianalytics.com/hc/article_attachments/4404848540055/fmtseriesaxis_font.gif)

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

Use this tab to specify the rotation angle of the major tick mark labels on the series axis.

![Format Series (Z) Axis dialog box - Orientation](https://devnet.logianalytics.com/hc/article_attachments/4404848540311/fmtseriesaxis_orntatn.gif)

**Automatic**

Select to adjust the rotation angle of the major tick mark label text on the axis automatically according to the length of the text, in degrees.

**Angle**

Select and specify the rotation angle of the major tick mark label text on the axis in the text box. When you change the rotation angle in the text box, the red line in the spin box changes correspondingly, and vice versa.

## Format Tab

Use this tab to specify the data format of the major tick mark labels on the series axis.

![Format Series (Z) Axis dialog box - Format](https://devnet.logianalytics.com/hc/article_attachments/4404848540567/fmtseriesaxis_fmt.gif)

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010097201-Format-Scatter-Dialog-Box)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010097241-Format-Series-Z-Gridline-Dialog-Box)
