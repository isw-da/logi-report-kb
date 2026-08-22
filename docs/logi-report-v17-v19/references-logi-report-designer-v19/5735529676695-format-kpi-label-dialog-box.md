---
title: "Format KPI Label Dialog Box"
id: 5735529676695
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735529676695-Format-KPI-Label-Dialog-Box
updated_at: 2022-11-02T08:24:43Z
---

# Format KPI Label Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/7933644552087/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735529673623-Format-Indicator-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/7933656663191/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735514200983-Format-Label-Dialog-Box)

# Format KPI Label Dialog Box

You can use the Format KPI Label dialog box to [format the KPI value labels in a pie/donut chart](https://devnet.logianalytics.com/hc/en-us/articles/5735520686359-Formatting-the-Pies-Donuts-and-KPI-Value-Labels-in-a-Pie-Donut-Chart#KPIValue). This topic describes the options in the dialog box.

Designer displays the Format KPI Label dialog box when you right-click the KPI value for a pie/donut in the chart and select Format KPI Label from the shortcut menu, or double-click the KPI value for any pie/donut in the chart.

This dialog box contains the following tabs:

* [General Tab](#General)
* [Font Tab](#Font)
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

## General Tab

Use this tab to specify the general properties of the labels.

![Format KPI Label - General](https://devnet.logianalytics.com/hc/article_attachments/7933723369111/fmtkpilbl_gnrl.gif)

**Size**

You can specify the size of the labels in this box.

* **Width**  
  Specify the width of the labels, in pixels.
* **Height**  
  Specify the height of the labels, in pixels.
* **X**  
  Specify the horizontal coordinate of the top left corner of the labels, relative to their parent container.
* **Y**  
  Specify the vertical coordinate of the top left corner of the labels, relative to their parent container.
* **Alignment**  
  Select the alignment of the text in the labels.
* **Word Wrap**  
  Select to wrap the text according to the width of the labels.

**Fill**

You can specify the fill pattern of the labels in this box.

* **Fill**  
  Specify the fill pattern of the labels. To edit the fill pattern, select the color indicator and specify a color or effect using the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette). You can also type the hexadecimal value of a color (for example, 0xff0000) in the text box.
* **Transparency**  
  Specify the transparency of the fill pattern.

**Border**

You can specify properties for the border of the labels in this box.

* **Border Type**  
  Select the type of the border.
  + **none**  
    Select if you do not want to show the border.
  + **raised**  
    Select to show 3-D border that appears as if it is raised off the page.
  + **recess**  
    Select to show 3-D border that appears as if it is pressed into the page.
  + **shadow**  
    Select to show two shadowed borders, beneath and to the right of the object.
  + **solid**  
    Select to use single-line border.
* **Color**  
  Specify the color of the border. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette), or type the hexadecimal value of a color (for example, 0xff0000) in the text box.
* **Line Style**  
  Select the line style of the border.
* **Transparency**  
  Specify the transparency of the border.
* **Thickness**  
  Specify the width of the border, in pixels.
* **End Caps**  
  Select the ending style of the border.
  + **butt**  
    Select to end unclosed subpaths and dash segments with no added decoration.
  + **round**  
    Select to end unclosed subpaths and dash segments with a round decoration that has a radius equal to half of the line width.
  + **square**  
    Select to end unclosed subpaths and dash segments with a square projection that extends beyond the end of the segment to a distance equal to half of the line width.
* **Line Joint**  
  Select the joint style of the border.
  + **miter**  
    Select to join path segments by extending their outside edges until they meet.
  + **round**  
    Select to join path segments by rounding off the corner at a radius of half the line width.
  + **bevel**  
    Select to join path segments by connecting the outer corners of their wide outlines with a straight segment.
* **Path**  
  Specify the fill pattern of the border.
  + **Outline Path**  
    Select to use outline path for the border.
  + **Fill Path**  
    Select to use whole path for the border.
* **Dash**  
  Specify the dash size of the border if you select a dash line style for the border.
  + **Auto Adjust Dash**  
    Select to adjust the dash size automatically.
  + **Fixed Dash Size**  
    Select to use fixed dash size.

**Orientation**

You can specify the orientation of the labels in this box.

* **Label Orientation**   
  Specify the rotation angle of the labels.

**Sample**

This box displays a preview sample based on your selections.

## Font Tab

Use this tab to specify the font properties of the text in the labels.

![Format KPI Label - Font](https://devnet.logianalytics.com/hc/article_attachments/7933714574999/fmtkpilbl_font.gif)

**Font**

You can specify the font style of the text in the labels in this box.

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

You can specify the special effects of the text in the labels in this box.

* **Style**  
  Select the font style of the text. It can be one of the following: plain, bold, italic, and bold italic.
* **Strikethrough**  
  Select the style of the horizontal line using which to strikethrough the text. It can be one of the following: none, thin line, bold line, and double lines.
* **Underline**  
  Select the style of the horizontal line under the text. It can be one of the following: none, single, single lower, bold line, bold lower, double lines, bold double, patterned line, and bold patterned. When you select "patterned line" or "bold patterned", Designer draws a line or bold line in the pattern of the text.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/7933685587863/noteicon.jpg) Web Report Studio and JDashboard do not support underlining chart text, therefore, this property is ignored when the chart runs in Web Report Studio or is used in a dashboard.

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

## Format Tab

Use this tab to specify the data format of the labels.

![Format KPI Label - Format](https://devnet.logianalytics.com/hc/article_attachments/7933752966167/fmtkpilbl_fmt.gif)

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

Select to apply the specified format to the labels.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/7933644552087/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735529673623-Format-Indicator-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/7933656663191/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735514200983-Format-Label-Dialog-Box)
