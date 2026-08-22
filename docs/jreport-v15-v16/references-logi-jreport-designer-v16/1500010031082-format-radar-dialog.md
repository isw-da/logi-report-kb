---
title: "Format Radar Dialog"
id: 1500010031082
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010031082-Format-Radar-Dialog
updated_at: 2021-07-24T10:38:46Z
---

# Format Radar Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010066481-Format-Pointer-Label-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010031102-Format-Rectangle-Dialog)

# Format Radar Dialog

The Format Radar dialog helps you to [format the radar in a radar chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010063541-Formatting-the-Radar-in-a-Radar-Chart). It appears when you right-click any line which connects two value nodes in a radar chart and select Format Radar from the shortcut menu, or double-click any line connecting two value nodes in a radar chart.

The dialog contains the following tabs: [General](#General), [Fill](#Fill), [Border](#Border), [Data Label](#Data), and [Hint](#Hint).

**OK**

Applies the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Apply**

Applies all changes and leaves the dialog open.

**Help**

Displays the help document about this feature.

## General

Specifies the general format of the radar chart.

![Format Radar - General](https://devnet.logianalytics.com/hc/article_attachments/4404901225239/fmtradr_gnrl.gif)

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

Specifies the color pattern to fill the radar areas.

![Format Radar - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404909201815/fmtradr_fill.gif)

**Color**

Specifies the color schema for the selected radar areas in the same data series. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010035022-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color directly in the text box.

**Transparency**

Specifies the transparency of the color schema.

**Self Settings**

Specifies whether to edit the color pattern for the radar areas themselves. When unchecked, the color settings defined here will be synchronized to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500010069721-Chart-Properties#Pattern) on the chart object in the Report Inspector, which can also be applied by data markers of other subtypes if the chart is a combo chart.

**Color List**

Opens the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500010030022-Color-List-Dialog) dialog to modify the color pattern for radar areas in the same data series respectively.

**Sample**

Displays a preview sample of your selection.

## Border

Specifies properties for the border of the radar.

![Format Radar - Border](https://devnet.logianalytics.com/hc/article_attachments/4404909202071/fmtradr_brdr.gif)

**Show Border**

Specifies whether to show the border of the radar. When it is checked, the other border properties in the tab will be enabled.

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

* **Auto Adjust Dash**  
   If selected, the dash size will be adjusted automatically.
* **Fixed Dash Size**  
   If selected, the dash size will be fixed size.

## Data Label

Specifies properties for data labels displayed on the radar.

![Format Radar - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4404901225495/fmtradr_data.gif)

**Static Data Label**

Specifies properties of the static data labels on the radar.

* **Show Static Data Label**  
   Specifies whether or not to show the static data labels on the radar. Only when it is checked can the following static data label related properties take effect.
* **Position**  
   Specifies the position of the static data labels on the radar.
  + **auto fit**  
     The static data labels will be displayed automatically.
* **Data Label Type**  
   Specifies in which way to display the data values in the static data labels.
  + **value**  
     Shows the value for each value node.
  + **percent**  
     Shows the percentage of each value node to the total.
  + **value and percent**  
     Shows the value and the percentage for each value node.
* **Auto Scale in Number**  
   Specifies whether to automatically scale the static data labels that are of the Number data type when the label values fall into the two ranges:
  + When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
  + When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

  By default it is set to auto which means that the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010069721-Chart-Properties#AutoScale).
* **Suppress Label When 0**  
   If true, the static data label whose value is 0 will not be displayed on the chart.

**Font**

Specifies the font format of text in the data labels.

* **Font list**  
   Lists all the available font faces that can be selected to apply to the text.
* **Font Size**  
   Specifies the font size of the text.
* **Font Color**  
   Specifies the font color of the text.
* **Transparency**  
   Specifies the color transparency of the text.
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
   Specifies the style of the horizontal line under the text. It can be one of the following: none, single, single lower, bold line, bold lower, double lines, bold double, patterned line, and bold patterned. When patterned line or bold patterned is selected, a line or bold line in the pattern of the text will be drawn.

  **Note:** JDashboard does not support underlining chart text so this property will be ignored when the chart is used in a dashboard.
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

## Hint

Specifies properties for the hint of the radar.

![Format Radar - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404909202327/fmtradr_hint.gif)

**Show Category and Series**

Specifies whether to include the category and series values in the hint.

**Auto Scale in Number**

Specifies whether to automatically scale the values displayed in the hint that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

The option "auto" means that the property setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010069721-Chart-Properties#AutoScale).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010066481-Format-Pointer-Label-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010031102-Format-Rectangle-Dialog)
