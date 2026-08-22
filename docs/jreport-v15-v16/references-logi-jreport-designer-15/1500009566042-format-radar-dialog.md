---
title: "Format Radar Dialog"
id: 1500009566042
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009566042-Format-Radar-Dialog
updated_at: 2021-07-24T05:55:11Z
---

# Format Radar Dialog

![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic[Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009587341-Format-Rectangle-Dialog-for-Library-Component-)

# Format Radar Dialog

The Format Radar dialog appears when you double-click radar in a chart, or right-click it and select Format Radar from the shortcut menu. It helps you to [format radars in a chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009583581-Formatting-the-Radar-Chart), and consists of the following tabs:

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

Specifies the general format of the radar chart. [See the tab](javascript:%20void(null)).

![Format Radar dialog - General](https://devnet.logianalytics.com/hc/article_attachments/4404889344151/fmtradr_gnrl.gif)

**Options**

* **Show Category Name**  
   Specifies whether to show the category names on the radar chart.
* **Use Fill Radar**  
   Specifies whether to use colors to fill the radar areas.
  + **Radar Fill Transparency**  
     Specifies the transparency for colors of the radar areas.

**Line**

* **Thickness**  
   Specifies the thickness for the radar lines, in pixels.
* **Node Style**  
   Specifies the type of node styles on the radar lines.
* **Width**  
   Specifies the width for node styles on the radar lines, in pixels.
* **Height**  
   Specifies the height for node styles on the radar lines, in pixels.

**Arrow Style**

Specifies the style for arrows on the lines.

* **None**  
   If selected, no style will be applied to the arrows.
* **Sharp**  
   If selected, arrows will be sharp.
* **Round**  
   If selected, arrows will be round.
* **Plain**  
   If selected, arrows will be plain.

## Fill

Specifies the color, fill effect and transparency for the radar areas. [See the tab](javascript:%20void(null)).

![Format Radar dialog - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404889344407/fmtradr_fill.gif)

**Color**

Specifies the color schema for the selected radar areas in the same data series. To edit the color, select the color image and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color directly in the text box.

**Transparency**

Specifies the transparency of the color schema.

**Color List**

Opens the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009564822-Color-List-Dialog) dialog to modify color pattern for radar areas in the same data series respectively.

**Sample**

Displays a preview sample of your selection.

## Border

Specifies properties for border of the radar, which take effect only when the [Border](https://devnet.logianalytics.com/hc/en-us/articles/1500009591241-Properties-of-Chart-Paper-in-Page-Report#Border) property on chart paper is set to true in the Report Inspector. [See the tab](javascript:%20void(null)).

![Format Radar dialog - Border](https://devnet.logianalytics.com/hc/article_attachments/4404893887255/fmtradr_brdr.gif)

**Border Type**

Displays the type for border of the radar. The default value is solid, and cannot be changed.

**Color**

Specifies the color for border of the radar.

**Transparency**

Specifies the transparency for color of the border.

**Line Style**

Specifies the line style to apply to border of the radar.

**Thickness**

Specifies the weight of the border.

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

Specifies properties for data labels displayed on the radar. [See the tab](javascript:%20void(null)).

![Format Radar dialog - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4404893887511/fmtradr_data.gif)

**Static Data Label**

Specifies properties of the static data labels on the radar.

* **Show Static Data Label**  
   Specifies whether or not to show the static data labels on the radar. Only when it is checked can the following static data label related properties take effect.
* **Position**  
   Specifies the position of the static data labels on the radar.
  + **auto fit**  
     The static data labels will be displayed automatically.
* **Suppress Label When 0**  
   If true, the static data label whose value is 0 will not be displayed on the chart. Available to 2-D radar chart only.

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

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009587321-Format-Platform-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009587341-Format-Rectangle-Dialog-for-Library-Component-)
