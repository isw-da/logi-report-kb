---
title: "Format Area Dialog (for Web Report)"
id: 1500009586981
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009586981-Format-Area-Dialog-for-Web-Report
updated_at: 2021-07-24T05:55:18Z
---

# Format Area Dialog (for Web Report)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009587001-Format-Area-Dialog-for-Page-Report-)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565702-Format-Bar-Dialog-for-Library-Component-)

# Format Area Dialog (for Web Report)

The Format Area dialog for web report appears when you double-click an area of a chart in a web report, or right-click it and then select Format Area from the shortcut menu. It helps you to [format areas in a chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009562962-Formatting-the-Areas), and consists of the following tabs:

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

Specifies the general format of the 2-D area chart. [See the tab](javascript:%20void(null)).

![Format Area for Web Report - General](https://devnet.logianalytics.com/hc/article_attachments/4404889360023/fmtarea_gnrl_1_wb.gif)

**Layout**

Specifies the layout for 2-D areas of the chart.

* **None 2-D**  
   If selected, 2-D area will be applied to display the trend of the values over time or categories.
* **Stacked 2-D**  
   If selected, stacked 2-D area will be applied to display the trend of the contribution of each data value over categories.
* **100% Stacked 2-D**  
   If selected, 100% stacked 2-D area will be applied to display the trend of the percentage each data value contributes over categories.

**Depth**

Specifies the depth properties for areas of the chart.

* **Use Depth**  
   Specifies whether to make the areas in the chart three-dimensional.
  + **Depth**  
     Specifies the depth of the areas, in pixels.
  + **Direction**  
     Specifies the direction for depth of the lines, in degrees.

**High-Low Lines**

Specifies whether to show the high-low lines in areas of a chart.

**Ignore Null Value**

Specifies whether to ignore null data values when drawing areas in the chart. If checked, when a null data value appears, it is ignored and the area is drawn from the previous data value to the next data value directly, otherwise, the area is broken at the point of the null data value.

## Fill

Specifies the color, fill effect and transparency for areas of the chart. [See the tab](javascript:%20void(null)).

![Format Area for Web Report - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404889359511/fmtarea_fill.gif)

**Use Single Color**

If checked, the selected area will use the single color pattern.

* **Color**  
   Specifies the color schema for the selected area. To edit the color, select the color image and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color directly in the text box.
* **Transparency**  
   Specifies the transparency of the color schema.
* **Color List**  
   Opens the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009564822-Color-List-Dialog) dialog to modify color pattern for each area.

**Use Single Color with Condition**

Not supported on area chart.

**Use Multiple Colors with Condition**

If checked, each area can have multiple color patterns based on defined conditions. You can divide each area into different parts based on different value ranges, along the direction of the value axis, and then specify different conditional colors to different value ranges for distinguishing.

* **Select Field**  
   Lists the value field on which you can apply the conditional fill.
* **Start Value**  
   Specifies the start value of the condition.
* **End Value**  
   Specifies the end value of the condition.
* **Color**  
   Specifies the color that will be applied to the values which meet the condition.
* **Transparency**  
   Specifies the transparency for the color of the condition.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)  
   Adds a new condition line.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893855383/btn_rmv1.gif)  
   Removes the selected condition line.
* **Label**  
   If checked, you can modify the condition expression of the selected condition line which will be shown as the legend entry label.

**Sample**

Displays a preview sample of your selection.

## Border

Specifies properties for border of the areas, which take effect only when the [Border](https://devnet.logianalytics.com/hc/en-us/articles/1500009591241-Properties-of-Chart-Paper-in-Page-Report#Border) property on chart paper is set to true in the Report Inspector. [See the tab](javascript:%20void(null)).

![Format Area for Web Report - Border](https://devnet.logianalytics.com/hc/article_attachments/4404889359767/fmtarea_border.gif)

**Border Type**

Displays the type for border of the areas. Its default value is solid, and cannot be changed.

**Color**

Specifies the color for border of the areas.

**Transparency**

Specifies the transparency for color of the border.

**Line Style**

Specifies the line style to apply to border of the areas.

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
   Specify the fill pattern of the border line to be outline path.
* **Fill Path**  
   Specify the fill pattern of the border line to be whole path.

**Dash**

Specifies the dash size of the border line.

* **Auto Adjusted Dash**  
   If selected, the dash size will be adjusted automatically.
* **Fixed Dash Size**  
   If selected, the dash size will be fixed size.

## Data Label

Specifies properties for data labels on areas in the chart. [See the tab](javascript:%20void(null)).

![Format Area for Web Report - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4404893915799/fmtarea_data.gif)

**Static Data Label**

Specifies properties of the static data labels on the areas. Not supported on 3-D area charts.

* **Show Static Data Label**  
   Specifies whether or not to show the static data labels. Only when it is checked can the following static data label related properties take effect.
* **Position**  
   Specifies the position of the static data labels on the areas.
  + **auto fit**  
     If selected, the static data labels will be displayed automatically.
  + **top center**  
     If selected, the static data labels will be displayed in the top center of the nodes on the areas.
  + **top left**  
     If selected, the static data labels will be displayed on the top left of the nodes on the areas.
  + **top right**  
     If selected, the static data labels will be displayed on the top right of the nodes on the areas.
  + **bottom left**  
    If selected, the static data labels will be displayed on the bottom left of the nodes on the areas.
  + **bottom center**  
     If selected, the static data labels will be displayed in the bottom center of the nodes on the areas.
  + **bottom right**  
     If selected, the static data labels will be displayed on the bottom right of the nodes on the areas.
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

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009587001-Format-Area-Dialog-for-Page-Report-)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565702-Format-Bar-Dialog-for-Library-Component-)
