---
title: "Format Bar Dialog (for Web Report)"
id: 1500009587021
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009587021-Format-Bar-Dialog-for-Web-Report
updated_at: 2021-07-24T05:55:18Z
---

# Format Bar Dialog (for Web Report)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009565722-Format-Bar-Dialog-for-Page-Report-)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009587041-Format-Bar-Gauge-Dialog-for-Library-Component-)

# Format Bar Dialog (for Web Report)

The Format Bar dialog for web report appears when you double-click a bar of a chart in a web report, or right-click it and then select Format Bar from the shortcut menu. It helps you to [format the bars](https://devnet.logianalytics.com/hc/en-us/articles/1500009583481-Formatting-the-Bars) of a 2-D bar/bench chart, and consists of the following tabs:

* [General](#General)
* [Size](#Size)
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

Specifies the general format of the 2-D bar/bench chart. [See the tab](javascript:%20void(null)).

![Format Bar for Web Report - General](https://devnet.logianalytics.com/hc/article_attachments/4404893913239/fmtbar_gnrl_1_wb.gif)

**Style**

Specifies the style of the bars in the chart. It can be Normal or Cylinder.

**Layout**

Specifies the layout of the chart.

* **Clustered - 2-D**  
   Displays and compares data values across categories.
* **Stacked - 2-D**  
   Displays and compares the contribution of each data value to a total across categories.
* **100% Stacked - 2-D**  
   Displays and compares the percentage that each data value contributes to a total across categories.

**Depth**

Specifies the depth properties for bars of the chart.

* **Use Depth**  
   Specifies whether to make the bars in the chart three-dimensional. You can also [use a formula to control the property](https://devnet.logianalytics.com/hc/en-us/articles/1500009568362-Using-Formulas-to-Control-Object-Properties).
  + **Depth**  
     Specifies the depth of the bars, in pixels.
  + **Direction**  
     Specifies the direction for depth of the bars, in degrees.

## Size

Specifies the size of the bars in the chart. The options on the tab vary when using [dynamic bar width](#Dynamic) or [fixed bar width](#Fix).

### Using dynamic bar width

To use dynamic bar width, make sure Fixed Bar Width is unchecked. [See the tab](javascript:%20void(null)).

![Format Bar for Web Report - Size - Dynamic bar width](https://devnet.logianalytics.com/hc/article_attachments/4404893912215/fmtbar_size_dynmc.gif)

**Bar Width**

Specifies the general bar width as a percentage of the unit width.

**Bar Gap**

Specifies the distance between two bars within a group as a percentage of the unit width. Available only to clustered bar/bench chart which contains data on the series axis or has more than one value on the value axis.

**Individual Bar Width**

Specifies properties of the individual bars. Available only to clustered bar/bench chart which contains data on the series axis or has more than one value on the value axis.

* ![Wider button](https://devnet.logianalytics.com/hc/article_attachments/4404889321879/btn_wider.gif)/![Narrower button](https://devnet.logianalytics.com/hc/article_attachments/4404889322135/btn_narrower.gif)  
   Specifies how much the selected bars in the same data series is wider/narrower than a general bar, in percentage.
* **Size List**  
   Opens the [Size List](https://devnet.logianalytics.com/hc/en-us/articles/1500009588641-Size-List-Dialog) dialog to specify the width and gap for the bars in the same data series respectively.

### Using fixed bar width

To use fixed bar width, make sure Fixed Bar Width is checked. [See the tab](javascript:%20void(null)).

![Format Bar for Web Report - Size - Fixed bar width](https://devnet.logianalytics.com/hc/article_attachments/4404893912471/fmtbar_size_fix.gif)

**Bar Width**

Specifies the general bar width.

**Bar Gap**

Specifies the distance between two bars within a group. Available only to clustered bar/bench chart which contains data on the series axis or has more than one value on the value axis.

**Outer Gap**

Specifies the distance between bars out of a group. Available only to clustered bar/bench chart which contains data on the series axis or has more than one value on the value axis.

**Individual Bar Width**

Specifies properties of the individual bars. Available only to clustered bar/bench chart which contains data on the series axis or has more than one value on the value axis.

* **Width**  
   Specifies the width of the selected bars in the same data series.
* **Gap**  
   Specifies the gap between the selected bars in the same data series and the bars beside it.
* **Size List**  
   Opens the [Size List](https://devnet.logianalytics.com/hc/en-us/articles/1500009588641-Size-List-Dialog) dialog to specify the width and gap for the bars in the same data series respectively.

![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404893837335/btn_fmla.gif)

Indicates the value of an option can be [controlled by a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009568362-Using-Formulas-to-Control-Object-Properties).

## Fill

Specifies the color, fill effect and transparency for bars of the chart. [See the tab](javascript:%20void(null)).

![Format Bar for Web Report - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404889358103/fmtbar_fill.gif)

**Use Single Color**

If checked, the bars will use the single color pattern.

* **Color**  
   Specifies the color schema for the bars. To edit the color, select the color image and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color directly in the text box.
* **Transparency**  
   Specifies the transparency of the color schema.
* **Vary Colors by Color List**  
   Specifies whether or not to make the bar colors vary.
  Available only for clustered bar types and when the chart has no series
  field. If checked, you can specify the color for each bar in the Color List dialog.
* **Color List**  
   Opens the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009564822-Color-List-Dialog) dialog to modify color pattern for bars in the same data series respectively.

**Use Single Color with Condition**

If checked, each bar can have its single color pattern based on defined conditions. You can select the Advanced or Normal button to switch between the two editing modes to edit the conditions.

* **Normal**
  + **Select Field**  
     Lists all the available fields to which the conditional fill can be applied. Select the field on which you want to define the conditions from the drop-down list.
  + **Values**  
     Specifies the value of the condition. Available when you select a category or series field or a field whose return value is not a number from the Select Field drop-down list.
  + **Start Value**  
     Specifies the start value of the condition. Available only when you select a value field or a field that returns a number from the Select Field drop-down list.
  + **End Value**  
     Specifies the end value of the condition. Available only when you select a value field or a field that returns a number from the Select Field drop-down list.
  + **Color**  
     Specifies the color that will be applied to the values which meet the condition.
  + **Transparency**  
     Specifies the transparency for the color of the condition.
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)  
     Adds a new condition.
  + ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893855383/btn_rmv1.gif)  
     Removes the selected condition.
  + **Label**  
     If checked, you can modify the condition expression of the selected condition which will be shown as the legend entry label.
  + **Value**  
     Specifies to display data in the condition expression as value. Available only when you select a value field or a field that returns a number from the Select Field drop-down list.
  + **Percent**  
     Specifies to display data in the condition expression in percent. Available only when you select a value field or a field that returns a number from the Select Field drop-down list and takes effect only on 100% Stacked Bar/Bench 2-D chart.
* **Advanced**
  + **Condition**  
     Displays the condition you have defined in the Edit Condition dialog.
  + **Color**  
     Specifies the color that will be applied to the values which meet the condition.
  + **Transparency**  
     Specifies the transparency for the color of the condition.
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)  
     Opens the [Edit Conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009586381-Edit-Conditions-Dialog#Chart) dialog to create a new condition.
  + ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404893791511/btn_edit.gif)  
     Opens the [Edit Conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009586381-Edit-Conditions-Dialog#Chart) dialog to edit the selected condition.
  + **Label**  
     If checked, you can modify the condition expression of the selected condition which will be shown as the legend entry label.
  + **Value**  
     Specifies to display data in the condition expression as value. Available only when you select a value field or a field that returns a number from the Select Field drop-down list.
  + **Percent**  
     Specifies to display data in the condition expression in percent. Available only when you select a value field or a field that returns a number from the Select Field drop-down list and takes effect only on 100% Stacked Bar/Bench 2-D chart.

**Use Multiple Colors with Condition**

If checked, each bar can have multiple color patterns based on defined conditions. You can divide each bar into different parts based on different value ranges, along the direction of the value axis, and then specify different conditional colors to different value ranges for distinguishing.

* **Select Field**  
   Lists all the available fields to which the conditional fill can be applied. Select the field on which you want to define the conditions from the drop-down list.
* **Start Value**  
   Specifies the start value of the condition.
* **End Value**  
   Specifies the end value of the condition.
* **Color**  
   Specifies the color that will be applied to the values which meet the condition.
* **Transparency**  
   Specifies the transparency for the color of the condition.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)  
   Adds a new condition.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893855383/btn_rmv1.gif)  
   Removes the selected condition.
* **Label**  
   If checked, you can modify the condition expression of the selected condition which will be shown as the legend entry label.

**Sample**

Displays a preview sample of your selection.

## Border

Specifies the properties for border of the bars, which take effect only when the [Border](https://devnet.logianalytics.com/hc/en-us/articles/1500009591241-Properties-of-Chart-Paper-in-Page-Report#Border) property on chart paper is set to true in the Report Inspector. [See the tab](javascript:%20void(null)).

![Format Bar for Web Report - Border](https://devnet.logianalytics.com/hc/article_attachments/4404893912727/fmtbar_border.gif)

**Border Type**

Displays the type for border of the bars. The default value is solid, and cannot be changed.

**Color**

Specifies the color for border of the bars.

**Transparency**

Specifies the transparency for color of the border.

**Line Style**

Specifies the line style to apply to border of the bars.

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

* **Auto Adjusted Dash**  
   If selected, the dash size will be adjusted automatically.
* **Fixed Dash Size**  
   If selected, the dash size will be fixed size.

## Data Label

Specifies properties for data labels displayed on the bars. [See the tab](javascript:%20void(null)).

![Format Bar for Web Report - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4404893912983/fmtbar_data.gif)

**Static Data Label**

Specifies properties of the static data labels on the bars.

* **Show Static Data Label**  
   Specifies whether or not to show the static data labels on the bars. Only when it is checked can the following static data label related properties take effect.
* **Position**  
   Specifies the position of the static data labels on the bars.
  + **auto fit**  
     If selected, the static data labels will be displayed automatically.
  + **outside top**   
     If selected, the static data labels will be displayed on the outside top of the bars.
  + **inside top**  
     If selected, the static data labels will be displayed on the inside top of the bars.
  + **inside center**  
     If selected, the static data labels will be displayed at the inside center of the bars.
  + **inside bottom**  
     If selected, the static data labels will be displayed at the inside bottom of the bars.
* **Suppress Label When 0**  
   If true, the static data label whose value is 0 will not be displayed on the chart.
* **Auto Arrange**  
  Specifies whether to display the static data labels inside the bars at the best position. Available only when the static data label's position is set to one of the following: inside center, inside top and inside bottom.
  + **true**  
     The static data label will be displayed horizontally at the specified position if the bar has enough room horizontally, otherwise, it will be displayed vertically. If a bar does not have enough room both vertically and horizontally, its static data label will not be displayed.
  + **false**  
     The static data labels will be displayed at the specified position, and if the labels get overlapping, some of them will not be displayed.

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

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009565722-Format-Bar-Dialog-for-Page-Report-)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009587041-Format-Bar-Gauge-Dialog-for-Library-Component-)
