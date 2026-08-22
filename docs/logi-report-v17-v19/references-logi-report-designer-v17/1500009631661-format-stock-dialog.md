---
title: "Format Stock Dialog"
id: 1500009631661
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009631661-Format-Stock-Dialog
updated_at: 2021-07-24T16:04:32Z
---

# Format Stock Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009631621-Format-Solid-Gauge-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009631641-Format-Surface-Dialog)

# Format Stock Dialog

The Format Stock dialog helps you to [format the stock in a stock chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009606002-Formatting-the-Stock-in-a-Stock-Chart). It appears when you right-click a stock line in a stock chart and select Format Stock from the shortcut menu, or double-click a stock line of a stock chart.

The dialog contains the following tabs: [General](#General), [Border](#Border) and [Data Label](#Data) and [Hint](#Hint).

**OK**

Applies the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Apply**

Applies all changes and leaves the dialog open.

**Help**

Displays the help document about this feature.

## General

Specifies the general format of the stock chart.

![Format Stock - General](https://devnet.logianalytics.com/hc/article_attachments/4404904288791/fmtstck_gnrl.gif)

**Stock Line**

Specifies properties for the stock lines.

* **Color**  
  Specifies the color schema for the stock lines. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Thickness**  
   Specifies the thickness of the stock lines, in pixels.

**Stock Bar**

Specifies properties for stock bars of an Open-High-Low-Close stock chart.

* **Up color**  
   Specifies the color schema for stock bars that stand for the stocks that the Open value is lower than the Close value.
* **Down color**  
   Specifies the color schema for stock bars that stand for the stocks that the Open value is higher than the Close value.
* **Bar Width**  
   Specifies the width of the stock bars.

## Border

Specifies properties for the border of the stock bars.

![Format Stock - Border](https://devnet.logianalytics.com/hc/article_attachments/4404916788887/fmtstck_brdr.gif)

**Show Border**

Specifies whether to show the border of the stock bars. When it is selected, the other border properties in the tab will be enabled.

**Color**

Specifies the color of the border.

**Transparency**

Specifies the transparency for color of the border.

**Line Style**

Specifies the line style to apply to the border.

**Thickness**

Specifies the weight of the border, in pixels.

**End Caps**

Specifies the ending style of the border line.

* **butt**  
   Ends unclosed sub paths and dash segments with no added decoration.
* **round**  
   Ends unclosed sub paths and dash segments with a round decoration that has a radius equal to half of the width of the pen.
* **square**  
   Ends unclosed sub paths and dash segments with a square projection that extends beyond the end of the segment to a distance equal to half of the line width.

**Line Joint**

Specifies the line joint style for the border line.

* **miter**  
   Joins path segments by extending their outside edges until they meet.
* **round**  
   Joins path segments by rounding off the corner at a radius of half the line width.
* **bevel**  
   Joins path segments by connecting the outer corners of their wide outlines with a straight segment.

**Sample**

Displays a preview sample of your selection.

**Path**

Specifies the fill pattern of the border line.

* **Outline Path**  
   Specifies the fill pattern of the border line to be outline path.
* **Fill Path**  
   Specifies the fill pattern of the border line to be whole path.

**Dash**

Specifies the dash size of border line.

* **Auto Adjust Dash**  
   If selected, the dash size will be adjusted automatically.
* **Fixed Dash Size**  
   If selected, the dash size will be fixed size.

## Data Label

Specifies properties for the data labels displayed on the chart. Not supported on stock chart.

![Format Stock - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4404916789143/fmtstck_data.gif)

## Hint

Specifies properties for the hint of the stock chart.

![Format Stock - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404904289175/fmtstck_hint.gif)

**Show Category and Series**

Specifies whether to include the category and series values in the hint.

**Auto Scale in Number**

Specifies whether to automatically scale the values displayed in the hint that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

The option "auto" means that the property setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#AutoScale).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009631621-Format-Solid-Gauge-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009631641-Format-Surface-Dialog)
