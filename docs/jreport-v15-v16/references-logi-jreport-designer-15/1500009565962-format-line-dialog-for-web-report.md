---
title: "Format Line Dialog (for Web Report)"
id: 1500009565962
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009565962-Format-Line-Dialog-for-Web-Report
updated_at: 2021-07-24T05:55:13Z
---

# Format Line Dialog (for Web Report)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009587281-Format-Line-Dialog-for-Page-Report-)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565982-Format-Paper-Dialog)

# Format Line Dialog (for Web Report)

The Format Line dialog for web report appears when you double-click a line in a chart in a web report, or right-click it and select Format Line from the shortcut menu. It helps you to [format the chart lines](https://devnet.logianalytics.com/hc/en-us/articles/1500009563142-Formatting-the-Lines), and consists of the following tabs:

* [General](#General)
* [Fill](#Fill)
* [Node](#Node)
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

Specifies the general format of the chart lines. [See the tab](javascript:%20void(null)).

![Format Line dialog for Web Report - General](https://devnet.logianalytics.com/hc/article_attachments/4404893893015/fmtln_gnrl_1_wb.gif)

**Layout**

Specifies the layout of the lines in the chart.

* **None**  
   If selected, the lines will display trend over categories.
* **Stacked**  
   If selected, the stacked lines will display the trend of the contribution of each data value over categories.
* **100% Stacked**  
   If selected, the 100% stacked lines will display the trend of the percentage each data value contributes over categories.

**Depth**

Specifies the depth properties for lines of the chart.

* **Use Depth**  
   Specifies whether to make the lines in the chart three-dimensional. You can also [use a formula to control the property](https://devnet.logianalytics.com/hc/en-us/articles/1500009568362-Using-Formulas-to-Control-Object-Properties).
  + **Depth**  
     Specifies the depth of the lines, in pixels.
  + **Direction**  
     Specifies the direction for depth of the lines, in degrees.

**Ignore Null Value**

Specifies whether to skip null data values in order to draw continuous lines in the chart. If checked, when a null data value appears on a line, it is ignored and the line is drawn from the previous data value to the next data value directly, otherwise, the line is broken at the point of the null data value.

**Smoothed Line**

Specifies whether to draw the lines smoothly without the sharp joints.

## Fill

Specifies the fill properties of the chart lines. [See the tab](javascript:%20void(null)).

![Format Line dialog for Web Report - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404893892503/fmtln_fill.gif)

**Use Single Color**

If checked, the lines will use the single color pattern.

* **Fill**  
   Specifies the fill effect of the chart lines. Disabled when the option Apply Color to Line in the Node tab is checked.
  + **Color**  
    Specifies the color schema for the selected chart line. To edit the color, select the color image and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color directly in the text box.
  + **Transparency**  
     Specifies the transparency of the color schema for the selected chart line.
  + **Pattern List**  
     Opens the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009564822-Color-List-Dialog) dialog to modify color pattern for each line.
* **Area**  
   Specifies properties for the areas which are formed by the chart axes and the lines.
  + **Color**  
     Specifies the color schema for the selected chart line area.
  + **Transparency**  
     Specifies the transparency of the color schema for the selected chart line area.
  + **Area Pattern List**  
     Opens the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009564822-Color-List-Dialog) dialog to modify color pattern of the areas.
* **Line**  
   Specifies the pattern of the chart lines.
  + **Line Style**  
     Specifies the style of the selected chart line.
  + **Thickness**  
     Specifies the thickness of the selected chart line, in pixels.
  + **Line Pattern List**  
     Opens the [Line Pattern List](https://devnet.logianalytics.com/hc/en-us/articles/1500009587741-Line-Pattern-List-Dialog) dialog to modify pattern of the lines in the same data series respectively.

**Use Single Color with Condition**

If checked, each line can have its single color pattern based on defined conditions. You can select the Advanced or Normal button to switch between the two editing modes to edit the conditions.

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
    Disabled when the option Apply Color to Line in the Node tab is checked.
  + **Transparency**  
     Specifies the transparency for the color of the condition. Disabled when the option Apply Color to Line in the Node tab is checked.
  + **Style**  
     Specifies the line style of the condition.
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)  
     Adds a new condition.
  + ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404893791511/btn_edit.gif)  
     Opens the [Edit Line Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009565342-Edit-Line-Style-Dialog) dialog to edit the line properties for the selected condition.
  + ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893855383/btn_rmv1.gif)  
     Removes the selected user-defined condition.
  + **Value**  
     Specifies to display data in the condition expression as value. Available only when you select a value field or a field that returns a number from the Select Field drop-down list.
  + **Percent**  
     Specifies to display data in the condition expression in percent. Available only when you select a value field or a field that returns a number from the Select Field drop-down list and takes effect only on 100% Stacked Line 2-D chart.
* **Advanced**
  + **Condition**  
     Displays the condition you have defined in the Edit Condition dialog.
  + **Color**  
     Specifies the color that will be applied to the values which meet the condition.
    Disabled when the option Apply Color to Line in the Node tab is checked.
  + **Transparency**  
     Specifies the transparency for the color of the condition. Disabled when the option Apply Color to Line in the Node tab is checked.
  + **Style**  
     Specifies the line style of the condition.
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)  
     Opens the [Edit Conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009586381-Edit-Conditions-Dialog#Chart1) dialog to create a condition and define the line properties of the condition.
  + ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404893791511/btn_edit.gif)  
     When a user-defined condition is selected, selecting the button opens the [Edit Conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009586381-Edit-Conditions-Dialog#Chart1) dialog to edit the condition and its line properties. When the default condition is selected, it opens the [Edit Line Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009565342-Edit-Line-Style-Dialog) dialog for editing the line properties of the condition.
  + ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893855383/btn_rmv1.gif)  
     Removes the selected user-define condition.

**Use Multiple Colors with Condition**

Not supported on line chart.

**Sample**

Displays a preview sample of your settings.

## Node

Specifies properties for nodes of the 2-D line. [See the tab](javascript:%20void(null)).

![Format Line dialog for Web Report - Node](https://devnet.logianalytics.com/hc/article_attachments/4404893893271/fmtln_node_wb.gif)

**Use Single Color**

If checked, the line nodes will use the single color pattern.

* **Shape**  
   Specifies the shape properties of the nodes in the selected chart line.
  + **Style**  
     Specifies the style of the nodes in the selected chart line.
  + **Transparency**  
     Specifies the transparency of the nodes in the selected chart line.
  + **Width**  
     Specifies the width of the nodes in the selected chart line, in pixels.
  + **Height**  
     Specifies the height of the nodes in the selected chart line, in pixels.
  + **Show Node**  
     Specifies whether to show nodes in the selected chart line. Only when it is set to true, the node related properties for the line chart can take effect. However, it does not control the properties Show High Point and Show Low Point and the Color property for each.
    - **Color**  
       Specifies the color of the nodes in the selected chart line.
  + **Show High Point**  
     Specifies whether to show the line node in the highest point in the selected chart line.
    - **Color**  
       Specifies the color of the node in the highest point in the selected chart line.
  + **Show Low Point**  
     Specifies whether to show the line node in the lowest point in the selected chart line.
    - **Color**  
       Specifies the color of the node in the lowest point in the selected chart line.
  + **Show Highlight Point**  
     Specifies whether to show the highlight point when you hover the mouse over a node in the selected chart line.
    - **Color**  
       Specifies the color of the highlight point in the selected chart line.
* **Border**  
   Specifies the border properties of the nodes in the selected chart line. Available when the node is not of the plus, multiplication, star1 or star2 style.
  + **Border Color**  
     Specifies the color for the border of the nodes in the selected chart line.
  + **Transparency**  
     Specifies the transparency for the border of the nodes in the selected chart line.
  + **Line Style**  
     Specifies the line style for the border of the nodes in the selected chart line.
  + **Thickness**  
     Specifies the thickness for the border of the nodes in the selected chart line, in pixels.
* **Line**  
   Specifies the line properties of the nodes in the selected chart line. Available when the node is of the plus, multiplication, star1 or star2 style.
  + **Line Style**  
     Specifies the line style of the nodes in the selected chart line.
  + **Thickness**  
     Specifies the line thickness of the nodes in the selected chart line.
* **Node Pattern List**  
   Opens the [Node Pattern List](https://devnet.logianalytics.com/hc/en-us/articles/1500009566762-Node-Pattern-List-Dialog) dialog to modify the node pattern for each chart line.

**Use Single Color with Condition**

If checked, each node can have its single color pattern based on defined conditions. You can select the Advanced or Normal button to switch between the two editing modes to edit the conditions.

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
  + **Style**  
     Specifies the node style of the condition.
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)  
     Adds a new condition.
  + ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404893791511/btn_edit.gif)  
     Opens the [Edit Node Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009586501-Edit-Node-Style-Dialog) dialog to edit the node properties for the selected condition.
  + ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893855383/btn_rmv1.gif)  
     Removes the selected user-defined condition.
  + **Label**  
     If checked, you can modify the condition expression of the selected condition which will be shown as the legend entry label.
  + **Value**  
     Specifies to display data in the condition expression as value. Available only when you select a value field or a field that returns a number from the Select Field drop-down list.
  + **Percent**  
     Specifies to display data in the condition expression in percent. Available only when you select a value field or a field that returns a number from the Select Field drop-down list and takes effect only on 100% Stacked Line 2-D chart.
* **Advanced**
  + **Condition**  
     Displays the condition you have defined in the Edit Condition dialog.
  + **Color**  
     Specifies the color that will be applied to the values which meet the condition.
  + **Transparency**  
     Specifies the transparency for the color of the condition.
  + **Style**  
     Specifies the node style of the condition.
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)  
     Opens the [Edit Conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009586381-Edit-Conditions-Dialog#Chart2) dialog to create a condition and define the node properties of the condition.
  + ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404893791511/btn_edit.gif)  
     When a user-defined condition is selected, selecting the button opens the [Edit Conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009586381-Edit-Conditions-Dialog#Chart2) dialog to edit the condition and its node properties. When the default condition is selected, it opens the [Edit Node Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009586501-Edit-Node-Style-Dialog) dialog for editing node properties of the condition.
  + ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893855383/btn_rmv1.gif)  
     Removes the selected user-defined condition.

**Use Multiple Colors with Condition**

Not supported on line chart.

**Apply Color to Line**

Specifies whether to make the color pattern specified on the node apply to the corresponding line.

**Sample**

Displays a preview sample of your selection.

## Data Label

Specifies properties for data labels displayed on the lines. [See the tab](javascript:%20void(null)).

![Format Line dialog for Web Report - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4404889346455/fmtln_data.gif)

**Static Data Label**

Specifies properties of the static data labels on the lines.

* **Show Static Data Label**  
   Specifies whether or not to show the static data labels on the lines. Only when it is checked can the following static data label related properties take effect.
* **Position**  
   Specifies the position of the static data labels on the lines.
  + **auto fit**  
     If selected, the static data labels will be displayed automatically.
  + **top center**  
     If selected, the static data labels will be displayed on the top center of the line nodes.
  + **top left**  
     If selected, the static data labels will be displayed on the top left of the line nodes.
  + **top right**  
     If selected, the static data labels will be displayed on the top right of the line nodes.
  + **bottom left**  
     If selected, the static data labels will be displayed at the bottom left of the line nodes.
  + **bottom center**  
     If selected, the static data labels will be displayed at the bottom center of the line nodes.
  + **bottom right**  
     If selected, the static data labels will be displayed at the bottom right of the line nodes.
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

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009587281-Format-Line-Dialog-for-Page-Report-)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565982-Format-Paper-Dialog)
