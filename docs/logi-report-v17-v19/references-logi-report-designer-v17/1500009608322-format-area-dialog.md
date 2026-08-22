---
title: "Format Area Dialog"
id: 1500009608322
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009608322-Format-Area-Dialog
updated_at: 2021-07-24T16:04:38Z
---

# Format Area Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009631261-Format-Activity-Gauge-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009608342-Format-Bar-Dialog)

# Format Area Dialog

The Format Area dialog helps you to [format areas in a chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009605722-Formatting-the-Areas-in-an-Area-Chart). It appears when you right-click an area in an area chart and then select Format Area from the shortcut menu, or double-click an area of an area chart.

The dialog contains the following tabs: [General](#General), [Fill](#Fill), [Border](#Border), [Data Label](#Data), [Hint](#Hint) and [Behaviors](#Behaviors) (the Behaviors tab is available to charts in library components only).

**OK**

Applies the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Apply**

Applies all changes and leaves the dialog open.

**Help**

Displays the help document about this feature.

## General

Specifies the general format of the area chart. The options on the tab vary for [2-D area charts](#2D) and [3-D area charts](#3D).

## For 2-D area charts

![Format Area dialog - General 2-D](https://devnet.logianalytics.com/hc/article_attachments/4404904337303/fmtarea_gnrl_1.gif)

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
   Specifies whether to make the areas in the chart three-dimensional. You can also [use a formula to control the property](https://devnet.logianalytics.com/hc/en-us/articles/1500009634221-Using-Formulas-to-Control-Object-Properties) if the chart uses a query resource as the data resource.
  + **Depth**  
     Specifies the depth of the areas, in pixels.
  + **Direction**  
     Specifies the direction for depth of the lines, in degrees.

**High-Low Lines**

Specifies whether to show the high-low lines in areas of a chart.

**Ignore Null Value**

Specifies whether to ignore null data values when drawing areas in the chart. If the option is selected, when a null data value appears, it is ignored and the area is drawn from the previous data value to the next data value directly, otherwise, the area is broken at the point of the null data value.

### For 3-D area charts

![Format Area dialog - General 3-D](https://devnet.logianalytics.com/hc/article_attachments/4404916803607/fmtarea_gnrl_2.gif)

**Layout**

Specifies the layout for 3-D areas of the chart.

* **None 3-D**  
   If selected, area with a 3-D visual effect will be applied.
* **Stacked 3-D**  
   If selected, stacked area with a 3-D visual effect will be applied.
* **100% Stacked 3-D**  
   If selected, 100% stacked area with a 3-D visual effect will be applied.

**Ignore Null Value**

Specifies whether to ignore null data values when drawing areas in the chart. If the option is selected, when a null data value appears, it is ignored and the area is drawn from the previous data value to the next data value directly, otherwise, the area is broken at the point of the null data value.

## Fill

Specifies the color, fill effect and transparency for areas of the chart.

![Format Area dialog - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404904337559/fmtarea_fill.gif)

**Use Single Color**

If the option is selected, the selected area will use the single color pattern.

* **Self Settings**  
  Specifies whether to edit the color pattern for the areas themselves. When the option is unselected, the color settings defined here will be synchronized to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#Pattern) on the chart object in the Report Inspector, which can also be applied by data markers of other subtypes if the chart is a combo chart.
* **Color**  
  Specifies the color schema for the selected area. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Transparency**  
  Specifies the transparency of the color schema.
* **Color List**  
  Opens the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009630161-Color-List-Dialog) dialog to modify the color pattern for each area.

**Use Single Color with Condition**

Not supported on area chart.

**Use Multiple Colors with Condition**

If the option is selected, each area can have multiple color patterns based on defined conditions. You can divide each area into different parts based on different value ranges, along the direction of the value axis, and then specify different conditional colors to different value ranges for distinguishing.

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
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif)  
  Adds a new condition line.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904239767/btn_rmv1.gif)  
  Removes the selected condition line.
* **Label**  
  If the option is selected, you can modify the condition expression of the selected condition line which will be shown as the legend entry label.

**Sample**

Displays a preview sample of your selection.

## Border

Specifies properties for the border of the areas.

![Format Area dialog - Border](https://devnet.logianalytics.com/hc/article_attachments/4404904337815/fmtarea_border.gif)

**Show Border**

Specifies whether to show the border of the areas. When it is selected, the other border properties in the tab will be enabled.

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

* **Auto Adjust Dash**  
   If selected, the dash size will be adjusted automatically.
* **Fixed Dash Size**  
   If selected, the dash size will be fixed size.

## Data Label

Specifies properties for data labels on areas in the chart.

![Format Area dialog - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4404904338071/fmtarea_data.gif)

**Static Data Label**

Specifies properties of the static data labels on the areas. Not supported on 3-D area charts.

* **Show Static Data Label**  
   Specifies whether to show the static data labels. Only when it is selected can the following static data label related properties take effect.
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
* **Data Label Type**  
  Specifies in which way to display the data values in the static data labels.
  + **value**  
     Shows the value for each area node.
  + **percent**  
     Shows the percentage of each area node to the total.
  + **value and percent**  
     Shows the value and the percentage for each area node.
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

  **Note:** Web Report Studio and JDashboard do not support underlining chart text so this property will be ignored when the chart runs in Web Report Studio or is used in a dashboard.
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

Specifies properties for the hint of the areas.

![Format Area dialog - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404904338327/fmtarea_hint.gif)

**Show Category and Series**

Specifies whether to include the category and series values in the hint.

**Auto Scale in Number**

Specifies whether to automatically scale the values displayed in the hint that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

The option "auto" means that the property setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#AutoScale).

## Behaviors

Specifies web behaviors to the areas. This tab is only available to charts in library components.

![Format Area dialog - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404916803863/fmtarea_bhvr.gif)

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009631261-Format-Activity-Gauge-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009608342-Format-Bar-Dialog)
