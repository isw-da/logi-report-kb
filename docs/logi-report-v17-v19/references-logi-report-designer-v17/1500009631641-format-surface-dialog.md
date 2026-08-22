---
title: "Format Surface Dialog"
id: 1500009631641
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009631641-Format-Surface-Dialog
updated_at: 2021-07-24T16:04:32Z
---

# Format Surface Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009631661-Format-Stock-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009608622-Format-Target-Label-Dialog)

# Format Surface Dialog

The Format Surface dialog helps you to [format the surface in a surface chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009628861-Formatting-the-Surface-in-a-Surface-Chart). It appears when you right-click a vertex on a surface chart and select Format Surface from the shortcut menu, double-click a vertex on a surface chart.

The dialog contains the following tabs: [Fill](#Fill), [Border](#Border), [Data Label](#Data) and [Hint](#Hint).

**OK**

Applies the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Apply**

Applies all changes and leaves the dialog open.

**Help**

Displays the help document about this feature.

## Fill

Specifies the color pattern to fill the surface.

![Format Surface - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404904289431/fmtsrfc_fill.gif)

**Color**

Specifies the color schema for the selected range section in the same data series on the surface. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.

**Transparency**

Specifies the transparency of the color schema.

**Self Settings**

Specifies whether to edit the color pattern for the surface itself. When the option is unselected, the color settings defined here will be synchronized to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#Pattern) on the chart object in the Report Inspector, which can also be applied by data markers of other subtypes if the chart is a combo chart.

**Color List**

Opens the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009630161-Color-List-Dialog) dialog to modify the color pattern for range sections in the same data series respectively.

**Sample**

Displays a preview sample of your selection.

## Border

Specifies properties for the border of the surface.

![Format Surface - Border](https://devnet.logianalytics.com/hc/article_attachments/4404904289815/fmtsrfc_brdr.gif)

**Show Border**

Specifies whether to show the border of the range sections on the surface. When it is selected, the other border properties in the tab will be enabled.

**Color**

Specifies the color of the border.

**Transparency**

Specifies the transparency for color of the border.

**Line Style**

Specifies the line style to apply to the border.

**Thickness**

Specifies the thickness of the border, in pixels.

**End Caps**

Specify the ending style of the border line.

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
   Specify the fill pattern of the border line to be outline path.
* **Fill Path**  
   Specify the fill pattern of the border line to be whole path.

**Dash**

Specifies the dash size of the border line.

* **Auto Adjust Dash**  
   If selected, the dash size will be adjusted automatically.
* **Fixed Dash Size**  
   If selected, the dash size will be fixed size.

## Data Label

Specifies properties for the data labels displayed on the chart. Not supported on surface chart.

![Format Surface - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4404904290071/fmtsrfc_data.gif)

## Hint

Specifies properties for the hint of the surface chart.

![Format Surface - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404904290327/fmtsrfc_hint.gif)

**Show Category and Series**

Specifies whether to include the category and series values in the hint.

**Auto Scale in Number**

Specifies whether to automatically scale the values displayed in the hint that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

The option "auto" means that the property setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#AutoScale).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009631661-Format-Stock-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009608622-Format-Target-Label-Dialog)
