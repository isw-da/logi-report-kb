---
title: "Format Line Dialog"
id: 1500009631481
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009631481-Format-Line-Dialog
updated_at: 2021-07-24T16:04:35Z
---

# Format Line Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009608482-Format-Legend-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009608502-Format-Paper-Dialog)

# Format Line Dialog

The Format Line dialog helps you to [format the selected chart line](https://devnet.logianalytics.com/hc/en-us/articles/1500009628721-Formatting-the-Lines-in-a-Line-Chart). It appears when you right-click a line in a line chart and select Format Line from the shortcut menu, or double-click a line in a line chart.

The dialog contains the following tabs: [General](#General), [Fill](#Fill), [Node](#Node), [Border](#Border), [Data Label](#Data), [Hint](#Hint) and [Behaviors](#Behaviors) (some tabs are available to specific chart types only).

**OK**

Applies the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Apply**

Applies all changes and leaves the dialog open.

**Help**

Displays the help document about this feature.

## General

Specifies the general format of the line chart. The options on the tab vary for [2-D line charts](#2D) and [3-D line charts](#3D).

### For 2-D lines

![Format Line - General 2-D](https://devnet.logianalytics.com/hc/article_attachments/4404904304535/fmtln_gnrl_1.gif)

**Layout**

Specifies the layout of the 2-D lines in the chart.

* **None**  
   If selected, the lines will display trend over categories.
* **Stacked**  
   If selected, the stacked lines will display the trend of the contribution of each data value over categories.
* **100% Stacked**  
   If selected, the 100% stacked lines will display the trend of the percentage each data value contributes over categories.

**Depth**

Specifies the depth properties for lines of the chart.

* **Use Depth**  
   Specifies whether to make the lines in the chart three-dimensional. You can also [use a formula to control the property](https://devnet.logianalytics.com/hc/en-us/articles/1500009634221-Using-Formulas-to-Control-Object-Properties) if the chart uses a query resource as the data resource.
  + **Depth**  
     Specifies the depth of the lines, in pixels.
  + **Direction**  
     Specifies the direction for depth of the lines, in degrees.

**Ignore Null Value**

Specifies whether to ignore null data values when drawing lines in the chart. If the option is selected, when a null data value appears on a line, it is ignored and the line is drawn from the previous data value to the next data value directly, otherwise, the line is broken at the point of the null data value.

**Smoothed Line**

Specifies whether to draw the lines smoothly without the sharp joints.

### For 3-D lines

![Format Line - General 3-D](https://devnet.logianalytics.com/hc/article_attachments/4404916793111/fmtln_gnrl_2.gif)

**Thickness**

Specifies the thickness of the 3-D lines in the chart, in pixels.

**Ignore Null Value**

Specifies whether to ignore null data values when drawing lines in the chart. If the option is selected, when a null data value appears on a line, it is ignored and the line is drawn from the previous data value to the next data value directly, otherwise, the line is broken at the point of the null data value.

## Fill

Specifies the fill properties of the chart lines.

![Format Line - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404904304919/fmtln_fill.gif)

**Use Single Color**

If the option is selected, the lines will use the single color pattern.

* **Self Settings**  
  Specifies whether to edit the color pattern for the lines themselves. When the option is unselected, the color settings defined in the Fill/Normal Fill box will be synchronized to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#Pattern) on the chart object in the Report Inspector, which can also be applied by data markers of other subtypes if the chart is a combo chart.
* **Fill**/**Normal Fill**  
  Specifies the fill effect of the chart lines. Disabled for 2-D lines when the option Apply Color to Line in the Node tab is selected.
  + **Color**  
    Specifies the color schema for the selected chart line. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
  + **Transparency**  
    Specifies the transparency of the color schema for the selected chart line.
  + **Pattern List**/**Color List**  
    Opens the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009630161-Color-List-Dialog) dialog to modify the color pattern for each line.
* **Area**  
  Specifies properties for the areas which are formed by the chart axes and the lines. Applies to 2-D lines only.
  + **Color**  
    Specifies the color schema for the selected chart line area.
  + **Transparency**  
    Specifies the transparency of the color schema for the selected chart line area.
  + **Area Pattern List**  
     Opens the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009630161-Color-List-Dialog) dialog to modify the color pattern of the areas.
* **Line**  
  Specifies the pattern of the chart lines.
  Applies to 2-D lines only.
  + **Line Style**  
    Specifies the style of the selected chart line.
  + **Thickness**  
    Specifies the thickness of the selected chart line, in pixels.
  + **Line Pattern List**  
    Opens the [Line Pattern List](https://devnet.logianalytics.com/hc/en-us/articles/1500009609002-Line-Pattern-List-Dialog) dialog to modify pattern of the lines in the same data series respectively.

**Use Single Color with Condition**

If the option is selected, each line can have its single color pattern based on defined conditions. You can select the Advanced or Normal button to switch between the two editing modes to edit the conditions. Applies to 2-D lines only.

* **Normal**
  + **Select Field**  
     Lists all the available fields to which the conditional fill can be applied. Select the field on which you want to define the conditions from the drop-down list.
  + **Value**  
     Specifies the value of the condition. Available when you select a category or series field or a field whose return value is not a number from the Select Field drop-down list.
  + **Start Value**  
     Specifies the start value of the condition. Available only when you select a value field or a field that returns a number from the Select Field drop-down list.
  + **End Value**  
     Specifies the end value of the condition. Available only when you select a value field or a field that returns a number from the Select Field drop-down list.
  + **Color**  
     Specifies the color that will be applied to the values which meet the condition.
    Disabled when the option Apply Color to Line in the Node tab is selected.
  + **Transparency**  
     Specifies the transparency for the color of the condition. Disabled when the option Apply Color to Line in the Node tab is selected.
  + **Style**  
     Specifies the line style of the condition.
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif)  
     Adds a new condition.
  + ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404911588375/btn_edit.gif)  
     Opens the [Edit Line Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009607922-Edit-Line-Style-Dialog) dialog to edit the line properties for the selected condition.
  + ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904239767/btn_rmv1.gif)  
     Removes the selected user defined condition.
  + **Value**  
     Specifies to display data in the condition expression as value. Available only when you select a value field or a field that returns a number from the Select Field drop-down list.
  + **Percent**  
     Specifies to display data in the condition expression in percent. Available only when you select a value field or a field that returns a number from the Select Field drop-down list and takes effect only on 100% Stacked Line 2-D chart.
* **Advanced**
  + **Condition**  
     Displays the condition you have defined in the Edit Condition dialog.
  + **Color**  
     Specifies the color that will be applied to the values which meet the condition.
    Disabled when the option Apply Color to Line in the Node tab is selected.
  + **Transparency**  
     Specifies the transparency for the color of the condition. Disabled when the option Apply Color to Line in the Node tab is selected.
  + **Style**  
     Specifies the line style of the condition.
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif)  
     Opens the [Edit Conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009607862-Edit-Conditions-Dialog#Chart1) dialog to create a condition and define the line properties of the condition.
  + ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404911588375/btn_edit.gif)  
     When a user defined condition is selected, selecting the button opens the [Edit Conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009607862-Edit-Conditions-Dialog#Chart1) dialog to edit the condition and its line properties. When the default condition is selected, it opens the [Edit Line Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009607922-Edit-Line-Style-Dialog) dialog for editing the line properties of the condition.
  + ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904239767/btn_rmv1.gif)  
     Removes the selected user-define condition.

**Use Multiple Colors with Condition**

Not supported on line chart.

**Sample**

Displays a preview sample of your settings.

## Node

Specifies properties for nodes of the 2-D line chart.

![Format Line - Node](https://devnet.logianalytics.com/hc/article_attachments/4404904305175/fmtln_node.gif)

**Use Single Color**

If the option is selected, the line nodes will use the single color pattern.

* **Self Settings**Specifies whether to edit the color pattern for the line nodes themselves. When the option is unselected, the color settings defined here will be synchronized to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#Pattern) on the chart object in the Report Inspector, which can also be applied by data markers of other subtypes if the chart is a combo chart.
* **Shape**  
   Specifies the shape properties of the nodes in the selected chart line.
  + **Style**  
     Specifies the style of the nodes in the selected chart line.
  + **Transparency**  
     Specifies the color transparency of the nodes in the selected chart line.
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
* ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404904189591/btn_fmla.gif)  
   Indicates the value of an option can be [controlled by a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009634221-Using-Formulas-to-Control-Object-Properties). Available only when the chart uses a query resource as the data resource.
* **Node Pattern List**  
   Opens the [Node Pattern List](https://devnet.logianalytics.com/hc/en-us/articles/1500009632521-Node-Pattern-List-Dialog) dialog to modify the node pattern for each chart line.

**Use Single Color with Condition**

If the option is selected, each node can have its single color pattern based on defined conditions. You can select the Advanced or Normal button to switch between the two editing modes to edit the conditions.

* **Normal**
  + **Select Field**  
     Lists all the available fields to which the conditional fill can be applied. Select the field on which you want to define the conditions from the drop-down list.
  + **Value**  
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
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif)  
     Adds a new condition line.
  + ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404911588375/btn_edit.gif)  
     Opens the [Edit Node Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009607942-Edit-Node-Style-Dialog) dialog to edit the node properties for the selected condition.
  + ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904239767/btn_rmv1.gif)  
     Removes the selected user defined condition.
  + **Label**  
     If the option is selected, you can modify the condition expression of the selected condition line which will be shown as the legend entry label.
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
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif)  
     Opens the [Edit Conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009607862-Edit-Conditions-Dialog#Chart1) dialog to create a condition and define the node properties of the condition.
  + ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404911588375/btn_edit.gif)  
     When a user defined condition is selected, selecting the button opens the [Edit Conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009607862-Edit-Conditions-Dialog#Chart2) dialog to edit the condition and its node properties. When the default condition is selected, it opens the [Edit Node Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009632521-Node-Pattern-List-Dialog) dialog for editing node properties of the condition.
  + ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904239767/btn_rmv1.gif)  
     Removes the selected user defined condition.

**Use Multiple Colors with Condition**

Not supported on line chart.

**Apply Color to Line**

Specifies whether to make the color pattern specified on the node apply to the corresponding line.

**Sample**

Displays a preview sample of your selection.

## Border

Specifies properties for the border of the 3-D lines.

![Format Line - Border](https://devnet.logianalytics.com/hc/article_attachments/4404904305431/fmtln_brdr.gif)

**Show Border**

Specifies whether to show the border of the lines. When it is selected, the other border properties in the tab will be enabled.

**Color**

Specifies the color for border of the lines.

**Transparency**

Specifies the transparency for the color of the border.

**Line Style**

Specifies the line style to apply to border of lines.

**Thickness**

Specifies the thickness for the border, in pixels.

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

Specifies properties for data labels displayed on the lines.

![Format Line - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4404904305687/fmtln_data.gif)

**Static Data Label**

Specifies properties of the static data labels on the lines. Not supported on 3-D line charts.

* **Show Static Data Label**  
   Specifies whether or not to show the static data labels on the lines. Only when it is selected can the following static data label related properties take effect.
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
* **Data Label Type**Specifies in which way to display the data values in the static data labels.
  + **value**  
     Shows the value for each line node.
  + **percent**  
     Shows the percentage of each line node to the total.
  + **value and percent**  
     Shows the value and the percentage for each line node.
* **Auto Scale in Number**  
   Specifies whether to automatically scale the static data labels that are of the Number data type when the label values fall into the two ranges:
  + When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
  + When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

  By default it is set to auto which means that the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#AutoScale).
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

Specifies properties for the hint of the lines.

![Format Line - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404904306071/fmtln_hint.gif)

**Show Category and Series**

Specifies whether to include the category and series values in the hint.

**Auto Scale in Number**

Specifies whether to automatically scale the values displayed in the hint that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

The option "auto" means that the property setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#AutoScale).

## Behaviors

Specifies web behaviors to the lines. This tab is only available to charts in library components.

![Format Line - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404904306583/fmtln_bhvr.gif)

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif)

Adds a new web behavior line.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif)

Removes the selected web behavior.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif)

Moves the selected web behavior up a step.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif)

Moves the selected web behavior down a step.

**Events**

Specifies the trigger event.

**Actions**

Specifies the action you want the event to trigger.

* ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif)  
   Opens the [Web Action List](https://devnet.logianalytics.com/hc/en-us/articles/1500009633961-Web-Action-List-Dialog) dialog to bind a web action to the event.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009608482-Format-Legend-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009608502-Format-Paper-Dialog)
