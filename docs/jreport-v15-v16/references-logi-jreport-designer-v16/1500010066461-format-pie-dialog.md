---
title: "Format Pie Dialog"
id: 1500010066461
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010066461-Format-Pie-Dialog
updated_at: 2021-07-24T10:38:47Z
---

# Format Pie Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010066501-Format-Pattern-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010031062-Format-Platform-Dialog)

# Format Pie Dialog

The Format Pie dialog helps you to [format pies of a chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010063521-Formatting-the-Pies-Donuts-and-KPI-Value-Labels-in-a-Pie-Donut-Chart). It appears when you right-click a pie in a pie chart and select Format Pie from the shortcut menu, or double-click a pie of a pie chart.

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

Specifies the options which are available when you format a pie chart.

![Format Pie - General](https://devnet.logianalytics.com/hc/article_attachments/4404901226519/fmtpie_gnrl.gif)

**Option**

* **Gap Amount**Specifies the gap between two pies.
* **Explode Amount**Specifies the gap between every section and the central point of a pie.
* **Show Pie Name**Specifies whether to show the name of the pie.

**KPI Value**

Enabled when the chart property [Swap Groups](https://devnet.logianalytics.com/hc/en-us/articles/1500010069721-Chart-Properties#SwapGroups) is not true.

* **Show KPI Value**  
   Specifies whether to show KPI value for each pie.
  + **KPI Value**  
     Specifies the KPI value to display on each pie. By default, the total value of each pie will be used as the KPI value. If you want to customize the value, uncheck Auto and input a value in the text box, or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404901133335/btn_fmla.gif) and select a formula or summary from the drop-down list to use its value as the KPI value.
  + **Position**  
     Specifies the position of the KPI value on the left, right, top, bottom of each pie or customized by dragging on any pie manually.

## Fill

Specifies the color, fill effect and transparency for the pie sections.

![Format Pie - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404909203607/fmtpie_fill.gif)

**Use Single Color**

If checked, the pie sections will use the single color pattern.

* **Self Settings**Specifies whether to edit the color pattern for the pie sections themselves. When unchecked, the color settings defined here will be synchronized to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500010069721-Chart-Properties#Pattern) on the chart object in the Report Inspector, which can also be applied by data markers of other subtypes if the chart is a combo chart.
* **Color**  
   Specifies the color schema for the selected pie sections in the same data series. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010035022-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color directly in the text box.
* **Transparency**  
   Specifies the transparency of the color schema.
* **Color List**  
   Opens the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500010030022-Color-List-Dialog) dialog to modify the color pattern for pie sections in the same data series respectively.

**Use Single Color with Condition**

If checked, each pie section can have its single color pattern based on defined conditions. You can select the Advanced or Normal button to switch between the two editing modes to edit the conditions.

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
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif)  
     Adds a new condition line.
  + ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404901177495/btn_rmv1.gif)  
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
  + ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404901116439/btn_edit.gif)  
     Opens the [Edit Conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500010065521-Edit-Conditions-Dialog#Chart) dialog to create or edit a condition.
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

Specifies properties for the border of the pies.

![Format Pie - Border](https://devnet.logianalytics.com/hc/article_attachments/4404901226775/fmtpie_border.gif)

**Show Border**

Specifies whether to show the border of the pies. When it is checked, the other border properties in the tab will be enabled.

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

* **Auto Adjust Dash**  
   If selected, the dash size will be adjusted automatically.
* **Fixed Dash Size**  
   If selected, the dash size will be fixed size.

## Data Label

Specifies properties for data labels displayed on the pies.

![Format Pie - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4404901227031/fmtpie_data.gif)

**Static Data Label**

Specifies properties of the static data labels on the pies.

* **Show Static Data Label**  
   Specifies whether or not to show the static data labels on the pies. Only when it is checked can the following static data label related properties take effect.
* **Position**  
   Specifies the position of the static data labels on the pies.
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
* **Data Label Type**Specifies in which way to display the data values in the static data labels.
  + **value**  
     Shows the value for each pie section.
  + **category name**  
     Shows the category name for each pie section.
  + **percent**  
     Shows the percentage of each pie section to the total.
  + **value and percent**  
     Shows the value and the percentage for each pie section.
  + **category name, value**   
     Shows the category name and value for each pie section.
  + **category name, percent**   
     Shows the category name and percentage for each pie section.
  + **category name, value, percent**   
     Shows the category name, value and percentage for each pie section.
* **Auto Scale in Number**  
   Specifies whether to automatically scale the static data labels that are of the Number data type when the label values fall into the two ranges:
  + When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
  + When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

  By default it is set to auto which means that the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010069721-Chart-Properties#AutoScale).
* **Line Color**  
   Specifies the color of the thin lines that are used to point to the static data labels.
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

Specifies properties for the hint of the pie sections.

![Format Pie - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404909204119/fmtpie_hint.gif)

**Show Category and Series**

Specifies whether to include the category and series values in the hint.

**Auto Scale in Number**

Specifies whether to automatically scale the values displayed in the hint that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

The option "auto" means that the property setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010069721-Chart-Properties#AutoScale).

## Behaviors

Specifies web behaviors to the pies. This tab is only available to charts in library components.

![Format Pie - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404901227287/fmtpie_bhvr.gif)

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif)

Adds a new web behavior line.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif)

Removes the selected web behavior.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif)

Moves the selected web behavior up a step.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif)

Moves the selected web behavior down a step.

**Events**

Specifies the trigger event.

**Actions**

Specifies the action you want the event to trigger.

* ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404909121559/btn_chsr1.gif)  
   Opens the [Web Action List](https://devnet.logianalytics.com/hc/en-us/articles/1500010068321-Web-Action-List-Dialog) dialog to bind a web action to the event.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010066501-Format-Pattern-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010031062-Format-Platform-Dialog)
