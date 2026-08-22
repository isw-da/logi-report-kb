---
title: "Format Surface Dialog Box"
id: 1500010059362
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010059362-Format-Surface-Dialog-Box
updated_at: 2021-07-23T19:15:33Z
---

# Format Surface Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010097281-Format-Stock-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010059382-Format-Target-Label-Dialog-Box)

# Format Surface Dialog Box

You can use the Format Surface dialog box to [format the surface in a surface chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010094621-Formatting-the-Surface-in-a-Surface-Chart). This topic describes the options in the dialog box.

Designer displays the Format Surface dialog box when you right-click a vertex in a surface chart and select Format Surface from the shortcut menu, or double-click a vertex in a surface chart.

The dialog box contains the following tabs:

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

## Fill Tab

Use this tab to specify the color pattern to fill the range sections in the surface chart.

![Format Surface - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404856931735/fmtsrfc_fill.gif)

**Color**

Specify the color for the selected range sections in the same data series. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.

**Transparency**

Specify the transparency of the color.

**Self Settings**

Select to apply the color pattern to the range sections themselves. When the option is unselected, the color settings defined here will be synchronized to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#Pattern) on the chart object in the Report Inspector, which can also be applied by data markers of other subtypes if the chart is a combo chart.

**Color List**

Select to open the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058302-Color-List-Dialog-Box) to modify the color pattern for the range sections in the same data series respectively.

**Sample**

The box displays a preview sample of your selection.

## Border Tab

Use this tab to specify the properties for the border of the range sections in the surface chart.

![Format Surface - Border](https://devnet.logianalytics.com/hc/article_attachments/4404856931991/fmtsrfc_brdr.gif)

**Show Border**

Select to show the border of the range sections. Designer enables the other border properties in this tab after you select the option.

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

Designer does not support displaying data labels in surface charts, so you can skip in this tab.

![Format Surface - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4404856932247/fmtsrfc_data.gif)

## Hint Tab

Use this tab to specify the properties for the hint of the surface chart.

![Format Surface - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404856932759/fmtsrfc_hint.gif)

**Show Category and Series**

Select to include the category and series values in the hint.

**Auto Scale in Number**

Specify whether to automatically scale the Number values in the hint which fall into the following two ranges:

* When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.

By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property [on the chart in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#AutoScale) for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010097281-Format-Stock-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010059382-Format-Target-Label-Dialog-Box)
