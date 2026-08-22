---
title: "Format Radar Dialog Box"
id: 1500010097181
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010097181-Format-Radar-Dialog-Box
updated_at: 2021-07-23T19:15:32Z
---

# Format Radar Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010059302-Format-Pointer-Label-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010059322-Format-Rectangle-Dialog-Box)

# Format Radar Dialog Box

You can use the Format Radar dialog box to [format the radar in a radar chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010057002-Formatting-the-Radar-in-a-Radar-Chart). This topic describes the options in the dialog box.

Designer displays the Format Radar dialog box when you right-click any line which connects two value nodes in a radar chart and select Format Radar from the shortcut menu, or double-click any line connecting two value nodes in a radar chart.

The dialog box contains the following tabs:

* [General Tab](#General)
* [Fill Tab](#Fill)
* [Border Tab](#Border)
* [Data Label Tab](#Data)
* [Hint Tab](#Hint)

You see these buttons in all the tabs:

**OK**

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Apply**

Select to apply all changes and leave the dialog box open.

**Help**

Select to view information about the dialog box.

## General Tab

Use this tab to specify the general properties of the radar chart.

![Format Radar - General](https://devnet.logianalytics.com/hc/article_attachments/4404848542743/fmtradr_gnrl.gif)

**Options**

You can specify the options of the radar chart in this box.

* **Show Category Name**  
  Select to show the category names in the radar chart.
* **Use Fill Radar**  
  Select to fill the areas formed by value nodes of a same data series in the radar.
  + **Radar Fill Transparency**  
    Specify the transparency of the color to fill the areas.

**Line**

You can specify the properties of the lines connecting the value nodes in the radar in this box.

* **Thickness**  
  Specify the thickness of the lines, in pixels.
* **Node Style**  
  Select the style of the nodes on the lines.
* **Width**  
  Specify the width of the nodes on the lines, in pixels.
* **Height**  
  Specify the height of the nodes on the lines, in pixels.

**Arrow Style**

You can specify the style of the arrows on the numeric axes in the radar in this box.

* **None**  
  Select to apply no style to the arrows.
* **Sharp**  
  Select to use sharp arrows.
* **Round**  
  Select to use round arrows.
* **Plain**  
  Select to use plain arrows.

## Fill Tab

Use this tab to specify the color pattern to fill the radar areas.

![Format Radar - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404856939159/fmtradr_fill.gif)

**Color**

Specify the color for the selected radar areas in the same data series. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.

**Transparency**

Specify the transparency of the color.

**Self Settings**

Select to apply the color pattern to the radar areas themselves only. If you do not select the option, Designer synchronizes the color settings you define here to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#Pattern) on the chart object in the Report Inspector, which the data markers of other subtypes can also apply if the chart is a combo chart.

**Color List**

Select to open the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058302-Color-List-Dialog-Box) to modify the color pattern for radar areas in the same data series respectively.

**Sample**

The box displays a preview sample of your selection.

## Border Tab

Use this tab to specify the properties for the border of the radar areas.

![Format Radar - Border](https://devnet.logianalytics.com/hc/article_attachments/4404856939415/fmtradr_brdr.gif)

**Show Border**

Select to show the border of the radar areas. Designer enables the other border properties in this tab after you select the option.

**Color**

Specify the color of the border. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.

**Transparency**

Specify the transparency for the color of the border.

**Line Style**

Select the line style of the border.

**Thickness**

Specify the thickness of the border, in pixels.

**End Caps**

Select the ending style of the border line.

* **butt**  
  Select to end unclosed sub paths and dash segments with no added decoration.
* **round**  
  Select to end unclosed sub paths and dash segments with a round decoration that has a radius equal to half of the width of the pen.
* **square**  
  Select to end unclosed sub paths and dash segments with a square projection that extends beyond the end of the segment to a distance equal to half of the line width.

**Line Joint**

Select the joint style of the border line.

* **miter**  
  Select to join path segments by extending their outside edges until they meet.
* **round**  
  Select to join path segments by rounding off the corner at a radius of half the line width.
* **bevel**  
  Select to join path segments by connecting the outer corners of their wide outlines with a straight segment.

**Sample**

The box displays a preview sample of your selection.

**Path**

You can specify the fill pattern of the border in this box.

* **Outline Path**  
  Select to use outline path for the border.
* **Fill Path**  
  Select to use whole path for the border.

**Dash**

You can specify the dash size of the border
in this box if you select a dash line style for the border.

* **Auto Adjust Dash**  
  Select to adjust the dash size automatically.
* **Fixed Dash Size**  
  Select to use fixed dash size.

## Data Label Tab

Use this tab to specify the properties of the data labels on the radar.

![Format Radar - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4404856939671/fmtradr_data.gif)

**Static Data Label**

You can specify the properties of the static data labels on the radar in this box.

* **Show Static Data Label**  
  Select to show the static data labels. Designer enables the other static data label properties after you select this option.
* **Position**  
  Select the position of the static data labels on the radar.
  + **auto fit**  
    Select to display the static data labels automatically.
* **Data Label Type**  
  Select in which way to display the values in the static data labels.
  + **value**  
     Select to show the value for each value node.
  + **percent**  
     Select to show the percentage of each value node to the total.
  + **value and percent**  
    Select to show the value and the percentage for each value node.
* **Auto Scale in Number**  
  Specify whether to automatically scale the Number values in the static data labels which fall into the following two ranges:
  + When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
  + When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.

  By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property [on the chart in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#AutoScale) for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.
* **Suppress Label When 0**  
  Select if you do not want to display the static data label whose value is 0 in the chart.

**Font**

You can specify the font format of the text in the static data labels in this box.

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

You can specify the special effects for the text in the static data labels in this box.

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

## Hint Tab

Use this tab to specify the properties for the hint of the radar.

![Format Radar - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404848543383/fmtradr_hint.gif)

**Show Category and Series**

Select to include the category and series values in the hint.

**Auto Scale in Number**

Specify whether to automatically scale the Number values in the hint which fall into the following two ranges:

* When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.

By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property [on the chart in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#AutoScale) for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010059302-Format-Pointer-Label-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010059322-Format-Rectangle-Dialog-Box)
