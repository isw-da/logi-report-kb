---
title: "Format Bubble Dialog"
id: 1500009631301
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009631301-Format-Bubble-Dialog
updated_at: 2021-07-24T16:04:38Z
---

# Format Bubble Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009631281-Format-Bar-Gauge-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009608362-Format-Bubble-Gauge-Dialog)

# Format Bubble Dialog

The Format Bubble dialog helps you to [format the bubbles in a bubble chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009605782-Formatting-the-Bubbles-in-a-Bubble-Chart). It appears when you right-click a bubble in a bubble chart and select Format Bubble from the shortcut menu, or double-click a bubble of a bubble chart.

The dialog contains the following tabs: [General](#General), [Fill](#Fill), [Border](#Border), [Data Label](#Data) and [Hint](#Hint).

**OK**

Applies the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Apply**

Applies all changes and leaves the dialog open.

**Help**

Displays the help document about this feature.

## General

Specifies the general format of the bubble chart.

![Format Bubble - General](https://devnet.logianalytics.com/hc/article_attachments/4404904329623/fmtbubl_gnrl.gif)

**Use 3-D Visual Effect**

Specifies whether to apply a three-dimensional visual effect to these bubbles.

**Cut Bubble Based on XY Area**

Specifies whether to cut the bubbles when they are beyond the chart wall, which means the area formed by the X axis and Y axis. While, If the bubbles are beyond the chart paper, they will still be cut.

## Fill

Specifies the color, fill effect and transparency of the bubbles.

![Format Bubble - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404904329879/fmtbubl_fill.gif)

**Color**

Specifies the color schema for all bubbles if the chart has no series field, or the selected bubbles in the same data series. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.

**Transparency**

Specifies the transparency of the color schema.

**Self Settings**

Specifies whether to edit the color pattern for the bubbles themselves. When the option is unselected, the color settings defined here will be synchronized to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#Pattern) on the chart object in the Report Inspector, which can also be applied by data markers of other subtypes if the chart is a combo chart.

**Color List**

Opens the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009630161-Color-List-Dialog) dialog to modify the color pattern for bubbles in the same data series respectively.

**Sample**

Displays a preview sample of your selection.

## Border

Specifies properties for the border of the bubbles.

![Format Bubble - Border](https://devnet.logianalytics.com/hc/article_attachments/4404904330775/fmtbubl_border.gif)

**Show Border**

Specifies whether to show the border of the bubbles. When it is selected, the other border properties in the tab will be enabled.

**Color**

Specifies the color for border of the bubbles.

**Transparency**

Specifies the transparency for color of the border.

**Line Style**

Specifies the line style to apply to border of the bubbles.

**Thickness**

Specifies the thickness of the border, in pixels.

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

Specifies the dash size of the border line.

* **Auto Adjust Dash**  
   If selected, the dash size will be adjusted automatically.
* **Fixed Dash Size**  
   If selected, the dash size will be fixed size.

## Data Label

Specifies properties for data labels displayed on the chart. Not supported on bubble chart.

![Format Bubble - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4404904331031/fmtbubl_data.gif)

## Hint

Specifies properties for the hint of the bubbles.

![Format Bubble - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404904331287/fmtbubl_hint.gif)

**Show Category and Series**

Specifies whether to include the category and series values in the hint.

**Auto Scale in Number**

Specifies whether to automatically scale the values displayed in the hint that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

The option "auto" means that the property setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#AutoScale).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009631281-Format-Bar-Gauge-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009608362-Format-Bubble-Gauge-Dialog)
