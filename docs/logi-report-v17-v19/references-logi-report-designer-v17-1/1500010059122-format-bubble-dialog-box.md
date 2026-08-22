---
title: "Format Bubble Dialog Box"
id: 1500010059122
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010059122-Format-Bubble-Dialog-Box
updated_at: 2021-07-23T19:15:27Z
---

# Format Bubble Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010059102-Format-Bar-Gauge-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010096981-Format-Bubble-Gauge-Dialog-Box)

# Format Bubble Dialog Box

You can use the Format Bubble dialog box to [format the bubbles in a bubble chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010056882-Formatting-the-Bubbles-in-a-Bubble-Chart). This topic describes the options in the dialog box.

Designer displays the Format Bubble dialog box when you right-click a bubble in a bubble chart and select Format Bubble from the shortcut menu, or double-click any bubble in the bubble chart.

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

Use this tab to specify the general properties of the bubble chart.

![Format Bubble - General](https://devnet.logianalytics.com/hc/article_attachments/4404848565783/fmtbubl_gnrl.gif)

**Use 3-D Visual Effect**

Select to apply a three-dimensional visual effect to the bubbles.

**Cut Bubble Based on XY Area**

Select to cut the bubbles when they are beyond the chart wall (the area formed by the X axis and Y axis). While, Designer still cuts the bubbles if they go beyond the chart paper.

## Fill Tab

Use this tab to specify the color pattern to fill the bubbles.

![Format Bubble - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404848566295/fmtbubl_fill.gif)

**Color**

Specify the color for all bubbles if the chart has no series field, or the color of the bubbles in the current data series if the chart has series field. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.

**Transparency**

Specify the transparency of the color.

**Self Settings**

Select to apply the color pattern to the bubbles themselves only. If you do not select the option, Designer synchronizes the color settings you define here to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#Pattern) on the chart object in the Report Inspector, which the data markers of other subtypes can also apply if the chart is a combo chart.

**Color List**

Select to open the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058302-Color-List-Dialog-Box) to modify the color pattern for bubbles in the same data series respectively.

**Sample**

The box displays a preview sample of your selection.

## Border Tab

Use this tab to specify the properties for the border of the bubbles.

![Format Bubble - Border](https://devnet.logianalytics.com/hc/article_attachments/4404856962711/fmtbubl_border.gif)

**Show Border**

Select to show the border of the bubbles. Designer enables the other border properties in this tab after you select the option.

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

Designer does not support displaying data labels in bubble charts, so you can skip this tab.

![Format Bubble - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4404848567063/fmtbubl_data.gif)

## Hint Tab

Use this tab to specify the properties for the hint of the bubbles.

![Format Bubble - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404848567319/fmtbubl_hint.gif)

**Show Category and Series**

Select to include the category and series values in the hint.

**Auto Scale in Number**

Specify whether to automatically scale the Number values in the hint which fall into the following two ranges:

* When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.

By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property [on the chart in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#AutoScale) for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010059102-Format-Bar-Gauge-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010096981-Format-Bubble-Gauge-Dialog-Box)
