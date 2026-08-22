---
title: "Format Donut Dialog (for Library Component)"
id: 1500009565862
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009565862-Format-Donut-Dialog-for-Library-Component
updated_at: 2021-07-24T05:55:15Z
---

# Format Donut Dialog (for Library Component)

![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic[Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009587181-Format-Donut-Dialog-for-Report-)

# Format Donut Dialog (for Library Component)

The Format Donut dialog for library component appears when you double-click a donut of a chart in a library component, or right-click it and select Format Donut from the shortcut menu. It helps you to [format donuts of a chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009563162-Formatting-the-Pies-Donuts), and consists of the following tabs:

* [General](#General)
* [Fill](#Fill)
* [Border](#Border)
* [Data Label](#Data)
* [Behaviors](#Behaviors)

**OK**

Accepts the formatting of the donuts and closes the dialog.

**Cancel**

Cancels the formatting of the donuts and closes the dialog.

**Apply**

Accepts the formatting of the donuts and leaves the dialog open.

**Help**

Displays the help document about this feature.

## General

Specifies the options which are available when you format a donut chart. [See the tab](javascript:%20void(null)).

![Format Donut for Library Component - General](https://devnet.logianalytics.com/hc/article_attachments/4404893900439/fmtdonut_gnrl_lc.gif)

**Gap Amount**

Specifies the gap between two donuts.

**Explode Amount**

Specifies the gap between every section and the central point of a donut.

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

**Donut Hole**

Specifies the radius percentage of the donut hole to the total pie circle.

**Show Donut Name**

Specifies whether to show the name of the donut.

## Fill

Specifies the color, fill effect and transparency for the donut sections. [See the tab](javascript:%20void(null)).

![Format Donut for Library Component - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404889350679/fmtdonut_fill_lc.gif)

**Use Single Color**

If checked, the donut sections will use the single color pattern.

* **Color**  
   Specifies the color schema for the selected donut sections in the same data series. To edit the color, select the color image and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color directly in the text box.
* **Transparency**  
   Specifies the transparency of the color schema.
* **Color List**  
   Opens the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009564822-Color-List-Dialog) dialog to modify color pattern for donut sections in the same data series respectively.

**Use Single Color with Condition**

If checked, each donut section can have its single color pattern based on defined conditions. You can select the Advanced or Normal button to switch between the two editing modes to edit the conditions.

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
     Specifies to display data in the condition expression in percent. Available only when you select a value field or a field that returns a number from the Select Field drop-down list and takes effect only on 100% Stacked Bar/Bench 2-D chart and 100% Stacked Bar/Bench 3-D chart.
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

Not supported on donut chart.

**Sample**

Displays a preview sample of your selection.

## Border

Specifies the properties for the border of the donuts, which take effect only when the [Border](https://devnet.logianalytics.com/hc/en-us/articles/1500009591241-Properties-of-Chart-Paper-in-Page-Report#Border) property on chart paper is set to true in the Report Inspector. [See the tab](javascript:%20void(null)).

![Format Donut for Library Component - Border](https://devnet.logianalytics.com/hc/article_attachments/4404893900823/fmtdonut_border_lc.gif)

**Border Type**

Displays the type for border of the donuts. The default value is solid, and cannot be changed.

**Color**

Specifies the color for the border of the donuts.

**Transparency**

Specifies the transparency for color of the border.

**Line Style**

Specifies the line style to apply to the border of the donuts.

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

Specifies properties for data labels displayed on the donuts. [See the tab](javascript:%20void(null)).

![Format Donut for Library Component - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4404889350935/fmtdonut_data_lc.gif)

**Static Data Label**

Specifies properties of the static data labels on the donuts.

* **Show Static Data Label**  
   Specifies whether or not to show the static data labels on the donuts. Only when it is checked can the following static data label related properties take effect.
* **Position**  
   Specifies the position of the static data labels on the donuts.
  + **auto fit**  
     If selected, the static data labels will be displayed automatically.
  + **sticker**  
     If selected, the static data labels will be displayed beside the donut sections.
  + **slim leg**  
     If selected, the static data labels will be displayed beside the donut sections and pointed by thin lines.
  + **best fit**  
     If selected, the static data labels will be displayed at the best fit position automatically.
  + **on slices**  
     If selected, the static data labels will be displayed on the donut sections (slices).
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

## Behaviors

Specifies some web behaviors to the donuts. [See the tab](javascript:%20void(null)).

![Format Donut for Library Component - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404889351191/fmtdonut_bhvr.gif)

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)

Adds a new web behavior line.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)

Removes the selected web behavior.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the selected web behavior up a step.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the selected web behavior down a step.

**Events**

Specifies the trigger event.

**Actions**

Specifies the action you want the event to trigger.

* ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif)  
   Opens the [Web Action List](https://devnet.logianalytics.com/hc/en-us/articles/1500009567862-Web-Action-List-Dialog) dialog to bind a web action to the event.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009587161-Format-Dial-Gauge-Dialog-for-Report-)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009587181-Format-Donut-Dialog-for-Report-)
