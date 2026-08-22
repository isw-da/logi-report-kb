---
title: "Format Stock Dialog Box"
id: 1500010097281
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010097281-Format-Stock-Dialog-Box
updated_at: 2021-07-23T19:15:33Z
---

# Format Stock Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010097261-Format-Solid-Gauge-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010059362-Format-Surface-Dialog-Box)

# Format Stock Dialog Box

You can use the Format Stock dialog box to [format the stock in a stock chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010094601-Formatting-the-Stock-in-a-Stock-Chart).

Designer displays the Format Stock dialog box when you right-click a stock line in a stock chart and select Format Stock from the shortcut menu, or double-click a stock line of a stock chart.

The dialog box contains the following tabs:

* [General Tab](#General)
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

Use this tab to specify the general properties of the stock chart.

![Format Stock - General](https://devnet.logianalytics.com/hc/article_attachments/4404848537623/fmtstck_gnrl.gif)

**Stock Line**

You can specify the properties of the stock lines in this box.

* **Color**  
  Specify the color of the stock lines. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Thickness**  
  Specify the thickness of the stock lines, in pixels.

**Stock Bar**

You can specify the properties for the stock bars of an Open-High-Low-Close stock chart in this box.

* **Up color**  
  Specify the color of the stock bars that stand for the stocks that the Open value is lower than the Close value.
* **Down color**  
  Specify the color for the stock bars that stand for the stocks that the Open value is higher than the Close value.
* **Bar Width**  
  Specify the width of the stock bars.

## Border Tab

Use this tab to specify the properties for the border of the stock bars of an Open-High-Low-Close stock chart.

![Format Stock - Border](https://devnet.logianalytics.com/hc/article_attachments/4404856930583/fmtstck_brdr.gif)

**Show Border**

Select to show the border of the stock bars. Designer enables the other border properties in this tab after you select the option.

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

Designer does not support displaying data labels in stock charts, so you can skip this tab.

![Format Stock - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4404856931095/fmtstck_data.gif)

## Hint Tab

Use this tab to specify the properties for the hint of the stock chart.

![Format Stock - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404848537879/fmtstck_hint.gif)

**Show Category and Series**

Select to include the category and series values in the hint.

**Auto Scale in Number**

Specify whether to automatically scale the Number values in the hint which fall into the following two ranges:

* When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.

By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property [on the chart in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#AutoScale) for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010097261-Format-Solid-Gauge-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010059362-Format-Surface-Dialog-Box)
