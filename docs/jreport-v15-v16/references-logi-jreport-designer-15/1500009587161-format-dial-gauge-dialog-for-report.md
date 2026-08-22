---
title: "Format Dial Gauge Dialog (for Report)"
id: 1500009587161
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009587161-Format-Dial-Gauge-Dialog-for-Report
updated_at: 2021-07-24T05:55:15Z
---

# Format Dial Gauge Dialog (for Report)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009565842-Format-Dial-Gauge-Dialog-for-Library-Component-)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565862-Format-Donut-Dialog-for-Library-Component-)

# Format Dial Gauge Dialog (for Report)

The Format Dial Gauge dialog for page/web report appears when you right-click a dial gauge of a chart in a page report or web report and select Format Dial Gauge from the shortcut menu. It helps you to [format dial gauges in a chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009583501-Formatting-the-Gauge), and consists of the following tabs:

* [General](#General)
* [Fill](#Fill)
* [Border](#Border)
* [Data Label](#Data)

**OK**

Applies the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Apply**

Applies all changes and leaves the dialog open.

**Help**

Displays the help document about this feature.

## General

Specifies the general format of the dial gauges. [See the tab](javascript:%20void(null)).

![Format Dial Gauge dialog - General](https://devnet.logianalytics.com/hc/article_attachments/4404893901463/fmtdlgauge_gnrl.gif)

**Circular**

Specifies properties for circles of dial gauges in the chart.

* **Start Angle**  
   Specifies the degree of start angles of the circles.
* **Stop Angle**  
   Specifies the degree of stop angles of the circles.
* **Circular Style**  
   Specifies the position of a dial gauge curve, related to the position of a circle in the chart.
* **Thickness**  
   Specifies the thickness for the circles, in pixels.
* **Range Radius**  
   Specifies the relative size of a dial in a percentage of total dial size.

**Pointer**

Specifies properties for pointers of dial gauges in the chart.

* **Pointer Style**  
   Specifies the style applied to pointers of the dial gauges.
  + **triangle**  
     If selected, pointers will be triangle shapes.
  + **diamond**  
     If selected, pointers will be diamond shapes.
  + **arrow**  
     If selected, pointers will be arrow shapes.
    - **Arrow Style**  
       Specifies the style applied to arrows of the pointers.
      * **sharp**  
         If selected, arrows will be sharp ones.
      * **round**  
         If selected, arrows will be round ones.
      * **plain**  
         If selected, arrows will be plain ones.

**Color Range**

Specifies different colors to fill the dial gauges in different ranges.

* **Use Fill**  
   Specifies to fill the dial gauges with colors. It is meaningful to specify the following properties when it is checked.
* **Minimum**  
   Specifies the minimum value of the range.
* **Maximum**  
   Specifies the maximum value of the range.
* **Color**  
   Specifies the color schema of the range. Select in the color cell to customize the color on the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette).
* **Name**  
   Displays the name of the range.

## Fill

Specifies the color, fill effect and transparency for the pointers. [See the tab](javascript:%20void(null)).

![Format Dial Gauge dialog - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404893901719/fmtdlgauge_fill.gif)

**Color**

Specifies the color schema for the selected pointers in the same data series. To edit the color, select the color image and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color directly in the text box.

**Transparency**

Specifies the transparency of the color schema.

**Color List**

Opens the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009564822-Color-List-Dialog) dialog to modify color pattern for pointers in the same data series respectively.

**Sample**

Displays a preview sample of your selection.

## Border

Specifies the properties for borders of the pointers, which take effect only when the [Border](https://devnet.logianalytics.com/hc/en-us/articles/1500009591241-Properties-of-Chart-Paper-in-Page-Report#Border) property on chart paper is set to true in the Report Inspector. [See the tab](javascript:%20void(null)).

![Format Dial Gauge dialog - Border](https://devnet.logianalytics.com/hc/article_attachments/4404889351447/fmtdlgauge_brdr.gif)

**Border Type**

Displays the type of the border. The default value is solid, and cannot be changed.

**Color**

Specifies the color of the border.

**Transparency**

Specifies the transparency for color of the border.

**Line Style**

Specifies the line style to apply to the border.

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

Specifies the dash size of border line.

* **Auto Adjusted Dash**  
   If selected, the dash size will be adjusted automatically.
* **Fixed Dash Size**  
   If selected, the dash size will be fixed size.

## Data Label

Specifies properties for data labels displayed on the dial gauges. [See the tab](javascript:%20void(null)).

![Format Dial Gauge dialog - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4404893901975/fmtdlgauge_data.gif)

**Static Data Label**

Specifies properties of the static data labels. Not supported on gauge chart.

**Font**

Specifies the font format of text in the data labels.

* **Font list**  
   Lists all the available font faces that can be selected to apply to the text.
* **Font Size**  
   Specifies the font size of the text.
* **Font Color**  
   Specifies the font color of the text.
* **Transparency**  
  Specifies the transparency of the text.
* **Rotation**  
   Specifies the rotation angle of the text around its center, in degrees. The default value is 0.
* **Shearing**  
   Specifies the gradient of the text.

**Effects**

Specifies the special effects of text in the data labels.

* **Style**  
   Specifies the font style of the text. It can be one of the following: plain, bold, italic, and bold italic.
* **Strikethrough**  
   Specifies the style of the horizontal line with which the text is struck through. It can be one of the following: none, thin line, bold line, and double lines.
* **Underline**  
   Specifies the style of the horizontal line under the text. It can be one of the following: none, single, single lower, bold line, bold lower, double lines, bold double, patterned line, and bold patterned.
* **Superscript**  
   Raises the text above the baseline and changes the text to a smaller font size, if a smaller size is available.
* **Embossed**  
   Makes the text appear to be raised off the page in relief.
* **Outlined**  
   Displays the inner and outer borders of each character.
* **Subscript**  
   Lowers the text below the baseline and changes the text to a smaller font size, if a smaller size is available.
* **Engraved**  
   Makes the text appear to be imprinted or pressed into the page.
* **Shadowed**  
   Adds a shadow beneath and to the right of the text.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009565842-Format-Dial-Gauge-Dialog-for-Library-Component-)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565862-Format-Donut-Dialog-for-Library-Component-)
