---
title: "Format Pie Dialog (for Report)"
id: 1500009566002
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009566002-Format-Pie-Dialog-for-Report
updated_at: 2021-07-24T05:55:12Z
---

# Format Pie Dialog (for Report)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009587301-Format-Pie-Dialog-for-Library-Component-)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009587321-Format-Platform-Dialog)

# Format Pie Dialog (for Report)

The Format Pie dialog for page/web report appears when you double-click a pie of a chart in a page report or web report, or right-click it and select Format Pie from the shortcut menu. It helps you to [format pies of a chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009563162-Formatting-the-Pies-Donuts), and consists of the following tabs:

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

Specifies the options which are available when you format a pie chart. [See the tab](javascript:%20void(null)).

![Format Pie dialog - General](https://devnet.logianalytics.com/hc/article_attachments/4404893888279/fmtpie_gnrl.gif)

**Gap Amount**

Specifies the gap between two pies.

**Explode Amount**

Specifies the gap between every section and the central point of a pie.

**Data Label Type**

Specifies the display type for data value in the data label.

* **value**  
   Shows the value for each pie section.
* **category name**  
   Shows the category name for each pie section.
* **percent**  
   Shows the percentage of each pie section to the total.
* **value percent**  
   Shows the value and the percentage for each pie section.
* **category name, value**   
   Shows the category name and value for each pie section.
* **category name, percent**   
   Shows the category name and percentage for each pie section.
* **category name, value, percent**   
   Shows the category name, value and percentage for each pie section.

**Show Pie Name**

Specifies whether to show the name of the pie.

## Fill

Specifies the color, fill effect and transparency for the pie sections. [See the tab](javascript:%20void(null)).

![Format Pie dialog - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404889344919/fmtpie_fill.gif)

**Use Single Color**

If checked, the pie sections will use the single color pattern.

* **Color**  
   Specifies the color schema for the selected pie sections in the same data series. To edit the color, select the color image and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color directly in the text box.
* **Transparency**  
   Specifies the transparency of the color schema.
* **Color List**  
   Opens the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009564822-Color-List-Dialog) dialog to modify color pattern for pie sections in the same data series respectively.

**Use Single Color with Condition**

If checked, each pie section can have its single color pattern based on defined conditions. You can select the Advanced or Normal button to switch between the two editing modes to edit the conditions.

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
     Adds a new condition line.
  + ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893855383/btn_rmv1.gif)  
     Removes the selected condition line.
  + **Label**  
     If checked, you can modify the condition expression of the selected condition line which will be shown as the legend entry label.
  + **Value**  
     Specifies to display data in the condition expression as value. Available only when you select a value field or a field that returns a number from the Select Field drop-down list.
  + **Percent**  
     Specifies to display data in the condition expression in percent. Available only when you select a value field or a field that returns a number from the Select Field drop-down list.
* **Advanced**
  + **Condition**  
     Displays the condition you have defined in the Edit Condition dialog.
  + **Color**  
     Specifies the color that will be applied to the values which meet the condition.
  + **Transparency**  
     Specifies the transparency for the color of the condition.
  + ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404893791511/btn_edit.gif)  
     Opens the [Edit Conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009586381-Edit-Conditions-Dialog#Chart) dialog to create or edit a condition.
  + **Label**  
     If checked, you can modify the condition expression of the selected condition line which will be shown as the legend entry label.
  + **Value**  
     Specifies to display data in the condition expression as value. Available only when you select a value field or a field that returns a number from the Select Field drop-down list.
  + **Percent**  
     Specifies to display data in the condition expression in percent. Available only when you select a value field or a field that returns a number from the Select Field drop-down list.

**Use Multiple Colors with Condition**

Not supported on pie chart.

**Sample**

Displays a preview sample of your selection.

## Border

Specifies the properties for the border of the pies, which take effect only when the [Border](https://devnet.logianalytics.com/hc/en-us/articles/1500009591241-Properties-of-Chart-Paper-in-Page-Report#Border) property on chart paper is set to true in the Report Inspector. [See the tab](javascript:%20void(null)).

![Format Pie dialog - Border](https://devnet.logianalytics.com/hc/article_attachments/4404889345175/fmtpie_border.gif)

**Border Type**

Displays the type for border of the pies. The default value is solid, and cannot be changed.

**Color**

Specifies the color for the border of the pies.

**Transparency**

Specifies the transparency for color of the border.

**Line Style**

Specifies the line style to apply to the border of the pies.

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

Specifies properties for data labels displayed on the pies. [See the tab](javascript:%20void(null)).

![Format Pie dialog - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4404889345431/fmtpie_data.gif)

**Static Data Label**

Specifies properties of the static data labels on the pies.

* **Show Static Data Label**  
   Specifies whether or not to show the static data labels on the pies.
* **Position**  
   Specifies the position of the static data labels on the pies. Only when it is checked can the following static data label related properties take effect.
  + **auto fit**  
     If selected, the static data labels will be displayed automatically.
  + **sticker**  
     If selected, the static data labels will be displayed beside the pie sections.
  + **slim leg**  
     If selected, the static data labels will be displayed beside the pie sections and pointed by thin lines.
  + **best fit**  
     If selected, the static data labels will be displayed at the best fit position automatically.
  + **on slices**  
     If selected, the static data labels will be displayed on the pie sections (slices).
* **Suppress Label When 0**  
   If true, the static data label whose value is 0 will not be displayed on the chart.
* **Line Color**  
  Specifies the color of the thin lines that are used to point to the static data labels.

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

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009587301-Format-Pie-Dialog-for-Library-Component-)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009587321-Format-Platform-Dialog)
