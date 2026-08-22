---
title: "Format Bar Gauge Dialog"
id: 1500010066261
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010066261-Format-Bar-Gauge-Dialog
updated_at: 2021-07-24T10:38:49Z
---

# Format Bar Gauge Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010066241-Format-Bar-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010066281-Format-Bubble-Dialog)

# Format Bar Gauge Dialog

The Format Bar Gauge dialog helps you to [format a bar gauge](https://devnet.logianalytics.com/hc/en-us/articles/1500010028842-Formatting-the-Gauge-in-a-Gauge-Chart#Bar). It appears when you double-click a bar gauge of a chart, or right-click it and select Format Bar Gauge from the shortcut menu.

The dialog contains the following tabs: [Staff Graph](#Staff), [Axis](#Axis), [Pointer](#Pointer), [Target](#Target), [Frame](#Frame), [Range Color](#Range), [Hint](#Hint) and [Behaviors](#Behaviors) (the Behaviors tab is available to charts in library components only).

**Sample**

Displays a preview sample of your selection.

**OK**

Applies the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Apply**

Applies all changes and leaves the dialog open.

**Help**

Displays the help document about this feature.

## Staff Graph

Specifies properties for the bars in the bar gauge.

![Foramt Bar Gauge dialog - Staff Graph](https://devnet.logianalytics.com/hc/article_attachments/4404901254167/fmtbargauge_stfgraph.gif)

**Bar**

Specifies the properties of the bars.

* **Layout**  
   Specifies the layout of the bars. It can be vertical or horizontal.
* **Thickness**  
   Specifies the thickness of the bars, in pixels.
* **Start Style**  
   Specifies the style for the start graph of the bars.
* **End Style**  
   Specifies the style for the end graph of the bars.

**Range Border**

Specifies properties of the bar border.

* **Color**  
   Specifies the color of the border. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010035022-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color directly in the text box.
* **Line Style**  
   Specifies the line style of the border.
* **Transparency**  
   Specifies the transparency for the border color.
* **Thickness**  
   Specifies the thickness of the border, in pixels.

**Show Range Name**

Specifies whether to show the names of the ranges defined in the [Range Color](#Range) tab. When it is checked, the following options are enabled.

* **Font**  
   Specifies the font format of text in the range names.
  + **Font list**  
     Lists all the available font faces that can be selected to apply to the text.
  + **Font Size**  
     Specifies the font size of the text.
  + **Font Color**  
     Specifies the font color of the text.
  + **Transparency**  
     Specifies the color transparency of the text.
  + **Rotation**  
     Specifies the rotation angle of the text around its center, in degrees. The default value is 0.
  + **Shearing**  
     Specifies the gradient of the text.
* **Effects**  
   Specifies the special effects of text in the range names.
  + **Style**  
     Specifies the font style of the text. It can be one of the following: plain, bold, italic, and bold italic.
  + **Strikethrough**  
     Specifies the style of the horizontal line with which the text is struck through. It can be one of the following: none, thin line, bold line, and double lines.
  + **Underline**  
     Specifies the style of the horizontal line under the text. It can be one of the following: none, single, single lower, bold line, bold lower, double lines, bold double, patterned line, and bold patterned. When patterned line or bold patterned is selected, a line or bold line in the pattern of the text will be drawn.

    **Note:** Web Report Studio and JDashboard do not support underlining chart text so this property will be ignored when the chart runs in Web Report Studio or is used in a dashboard.
  + **Superscript**  
     Raises the text above the baseline and changes the text to a smaller font size, if a smaller size is available.
  + **Embossed**  
     Makes the text appear to be raised off the page in relief.
  + **Outlined**  
     Displays the inner and outer borders of each character.
  + **Subscript**  
     Lowers the text below the baseline and changes the text to a smaller font size, if a smaller size is available.
  + **Engraved**  
     Makes the text appear to be imprinted or pressed into the page.
  + **Shadowed**  
     Adds a shadow beneath and to the right of the text.

## Axis

The tab consists of four sub tabs: [Axis](#Axis1), [Tick Mark](#TickMark), [Label](#Label) and [Format](#Format).

### Axis

Specifies properties of the axis in the bar gauge.

![Foramt Bar Gauge dialog - Axis - Axis1](https://devnet.logianalytics.com/hc/article_attachments/4404909217815/fmtbargauge_axis_axis1.gif)

**Show Axis**

Specifies whether to show the axis.

**Type**

Specifies the position relationship of the axis and the bar. When Layout is set to horizontal in the [Staff Graph](#Staff) tab, the following are available:

* **Top**  
   The axis will be on the top of the bar.
* **Bottom**  
   The axis will be on the bottom of the bar.
* **Center**  
   The axis will be in the center of the bar.

When Layout is set to vertical in the [Staff Graph](#Staff) tab, the following are available:

* **Left**  
   The axis will be on the left of the bar.
* **Right**  
   The axis will be on the right of the bar.
* **Center**  
   The axis will be in the center of the bar.

**Option**

Specifies the values to be displayed in the chart.

* **Minimum**  
   Specifies the minimum value to be displayed in the chart. You can also [use a formula to control the property](https://devnet.logianalytics.com/hc/en-us/articles/1500010033202-Using-Formulas-to-Control-Object-Properties).
* **Maximum**  
   Specifies the maximum value to be displayed in the chart. You can also [use a formula to control the property](https://devnet.logianalytics.com/hc/en-us/articles/1500010033202-Using-Formulas-to-Control-Object-Properties).

**Line**

Specifies the properties of the axis line.

* **Color**  
   Specifies the color of the line.
* **Transparency**  
  Specifies the color transparency of the line.
* **Style**  
   Specifies the style of the line.
* **Thickness**  
   Specifies the thickness of the line.
* **Use Range Color**   
  Specifies whether the axis line color follows [the colors of the ranges](#Range), that is, the axis line part for the range of blue color will become blue and the part for the range of red color will become red. If checked, the Color and Transparency options will be disabled.

**Gap**

Specifies the gap between the axis and the bar when the axis is not in the center of the bar. The option is disabled when Type is set to center in the tab.

### Tick Mark

Specifies properties of the tick marks on the axis.

![Format Bar Gauge dialog - Axis - Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4404909218071/fmtbargauge_axis_tkmk.gif)

**Type**

Specifies the position relationship of the axis and the tick marks. When Layout is set to horizontal in the [Staff Graph](#Staff) tab, the following are available:

* **None**  
   Specifies not to display the tick marks on the axis. It's meaningless to specify all the other tick mark related properties if this type is selected.
* **Top**  
   Specifies to display the tick marks on the top of the axis.
* **Bottom**  
   Specifies to display the tick marks on the bottom of the axis.
* **Center**  
   Specifies to display the tick marks in the center of the axis.

When Layout is set to vertical in the [Staff Graph](#Staff) tab, the following are available:

* **None**  
   Specifies not to display the tick marks on the axis. It's meaningless to specify all the other tick mark related properties if this type is selected.
* **Left**  
   Specifies to display the tick marks on the left of the axis.
* **Right**  
   Specifies to display the tick marks on the right of the axis.
* **Center**  
   Specifies to display the tick marks in the center of the axis.

**Major Tick Mark Line**

Specifies the properties of the major tick mark line.

* **Correlate with Axis**   
   If checked, the line properties of the major tick marks will correlate with [that of the axis](#Line) automatically.
  + **Color**  
     Specifies the color of the major tick mark line. Disabled when Use Range Color in the Axis sub tab is checked.
  + **Style**  
     Specifies the style of the major tick mark line.
  + **Transparency**  
     Specifies the color transparency of the major tick mark line. Disabled when Use Range Color in the Axis sub tab is checked.
  + **Thickness**  
     Specifies the thickness of the major tick mark line.
* **Increment**  
   Specifies the distance between two adjacent major tick marks on the axis.
* **Number of Tick Marks**  
   Specifies how many major tick marks to be displayed on the axis.
* **Tick Mark Length**  
   Specifies the length of the major tick mark line.

**Minor Tick Mark Line**

Specifies the properties of the minor tick mark line.

* **Correlate with Axis**  
   If checked, the line properties of the minor tick marks will correlate with [that of the axis](#Line) automatically.
  + **Color**  
     Specifies the color of the minor tick mark line. Disabled when Use Range Color in the Axis sub tab is checked.
  + **Style**  
     Specifies the style of the minor tick mark line.
  + **Transparency**  
     Specifies the color transparency of the minor tick mark line. Disabled when Use Range Color in the Axis sub tab is checked.
  + **Thickness**  
     Specifies the thickness of the minor tick mark line.
* **Increment**  
   Specifies the distance between two adjacent minor tick marks on the axis.
* **Number of Tick Marks**  
   Specifies how many minor tick marks to be displayed on the axis.
* **Tick Mark Length**  
   Specifies the length of the minor tick mark line.

### Label

Specifies properties of the major tick mark labels.

![Format Bar Gauge dialog - Axis - Label](https://devnet.logianalytics.com/hc/article_attachments/4404901254423/fmtbargauge_axis_lbl.gif)

**Type**

Specifies the type of the labels.

* **None**  
   If selected, the labels will not be shown.
* **Normal**  
   If selected, the labels will be shown as you specify.
  + **Label Every N Major Tick Marks**  
     Specifies the frequency at which the major tick marks will be labeled.
  + **Number of Major Labels**  
     Specifies how many major tick mark labels to be displayed on the axis.
    - **Auto**  
       If checked, all major tick mark labels will be shown.
    - **Fixed**  
       If checked, you can specify the number of the major tick mark labels to be displayed on the axis.
* **Range Value**  
   If selected, the labels will show the [range values](#Range).

**Gap**

Specifies the gap properties for the major tick mark labels.

* **Label Axis Gap**  
   Specifies the distance between the labels and the axis, in pixels.
* **Best Effect**  
   Specifies whether to adjust the labels automatically to make them placed best. If checked, some labels will be hidden when they are overlapped.

**Font**

Specifies the font format of text in the major tick mark labels.

* **Font list**  
   Lists all the available font faces that can be selected to apply to the text.
* **Font Size**  
   Specifies the font size of the text.
* **Font Color**   
   Specifies the font color of the text. Disabled when Use Range Color in the Axis sub tab is checked.
* **Transparency**  
   Specifies the color transparency of the text. Disabled when Use Range Color in the Axis sub tab is checked.
* **Rotation**  
   Specifies the rotation angle of the text around its center, in degrees. The default value is 0.
* **Shearing**  
   Specifies the gradient of the text.

**Effects**

Specifies the special effects of text in the tick mark labels.

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

### Format

Specifies the data format of the major tick mark labels.

![Format Bar Gauge dialog - Axis - Format](https://devnet.logianalytics.com/hc/article_attachments/4404909218327/fmtbargauge_axis_fmt.gif)

**Category**

Lists the category types. Select one to customize its format.

**Format**

Displays all the [formats](https://devnet.logianalytics.com/hc/en-us/articles/1500010030282-Data-Format-Dialog#DataFormat) of the selected category. Select the required one and select Add to add it as the format of the specified category. You can add only one format for each category.

**Properties**

Displays the properties of the format you select. If the formats listed in the Format box cannot meet your requirement, define the format in the text field and then select Add to add it as the format of the specified category.

**Auto Scale in Number**

Specifies whether to
automatically scale the major tick mark labels that are of the Number data type when the label values fall into the two ranges:

* When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

By default it is set to auto which means that the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010069721-Chart-Properties#AutoScale). When it is true, the specified format applies to the integer part of the values after scaled, but if the specified format conflicts with Auto Scale in Number, for example the values are displayed in percentage, then the Auto Scale in Number setting is ignored.

**Stack**

Lists all the formats you select from different categories.

**Add**

Adds a format to the Stack list box.

**Remove**

Removes a format from the Stack list box.

**Apply**

Applies the specified format in the Stack list box to the major tick mark labels.

## Pointer

Specifies properties of the pointers in the bar gauge.

![Format Bar Gauge dialog - Pointer](https://devnet.logianalytics.com/hc/article_attachments/4404901254679/fmtbargauge_pnt.gif)

**Use Pointer**

Specifies to use pointers to indicate values in the bar gauge.

* **Pointer Style**  
   Specifies properties of the pointers.
  + **Value Pointer**  
     Specifies the style of the pointers. Select a style from the drop-down list or select Customized and specify another image as the pointer.
  + **Width**  
     Specifies the width of the pointers.
  + **Height**  
     Specifies the height of the pointers.
  + **Position**  
     Specifies the position of the pointers relative to the bar.
  + **Gap**  
     Specifies the distance between the pointers and the bar, in pixels.
  + **Style List**  
     Opens the [Style List](https://devnet.logianalytics.com/hc/en-us/articles/1500010068061-Style-List-Dialog) dialog to specify the style for pointers in the same data series respectively.
* **Pointer Color**  
   Specifies color properties of the pointers.
  + **Color**  
     Specifies the color of the pointers.
  + **Color List**   
     Opens the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500010030022-Color-List-Dialog) dialog to specify the color pattern for pointers in the same data series respectively.
  + **Transparency**  
     Specifies the transparency for color of the pointers.
  + **Self Settings**Specifies whether to edit the color pattern for the pointers themselves. When unchecked, the color settings defined here will be synchronized to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500010069721-Chart-Properties#Pattern) on the chart object in the Report Inspector, which can also be applied by data markers of other subtypes if the chart is a combo chart.
  + **Use Range Color**  
    Specifies whether to use the color [defined for the ranges](#Range) as the pointer color. If checked, the three properties above will be disabled.
* **Pointer Value**  
  Specifies properties for values of the pointers.
  + **Show Pointer Value**  
     Specifies whether to show values for the pointers.
    - **Position**  
       Specifies the position relationship between the values and the pointers. Select the position from the drop-down list or select customized to customize the position by dragging any pointer value in the design area.
* **Pointer Border**Specifies properties for border of the pointers.
  + **Show Pointer Border**  
     Specifies whether to show the border of the pointers. When it is checked, the following border properties are enabled.
    - **Line Style**Specifies the line style to apply to the border.
    - **Thickness**Specifies the weight of the border, in pixels.
    - **Color**  
       Specifies the color of the border.
    - **Transparency**Specifies the transparency for color of the border.

**Use Color Bar**

Specifies to use color bars to indicate values in the bar gauge.

* **Pointer Color**  
   Specifies the properties of the color bars.
  + **Color**  
     Specifies the color of the bars.
  + **Transparency**  
     Specifies the transparency for color of the bars.
  + **Color List**   
    Opens the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500010030022-Color-List-Dialog) dialog to specify the color pattern for color bars in the same data series respectively.
  + **Self Settings**Specifies whether to edit the color pattern for the color bars themselves. When unchecked, the color settings defined here will be synchronized to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500010069721-Chart-Properties#Pattern) on the chart object in the Report Inspector, which can also be applied by data markers of other subtypes if the chart is a combo chart.
  + **Thickness**  
    Specifies the thickness of the color bars.
* **Pointer Value**  
  Specifies properties for values of the color bars.
  + **Show Pointer Value**  
     Specifies whether to show values for the color bars.
    - **Position**  
       Specifies the position relationship between the values and the color bars. Select the position from the drop-down list or select customized to customize the position by dragging any value in the design area.
* **Pointer Border**Specifies properties for border of the pointers.
  + **Show Pointer Border**  
     Specifies whether to show the border of the pointers. When it is checked, the following border properties are enabled.
    - **Line Style**Specifies the line style to apply to the border.
    - **Thickness**Specifies the weight of the border, in pixels.
    - **Color**  
       Specifies the color of the border.
    - **Transparency**Specifies the transparency for color of the border.

## Target

Specifies properties of the target in the bar gauge.

![Format Bar Gauge dialog - Target](https://devnet.logianalytics.com/hc/article_attachments/4404901254935/fmtbargauge_tgt.gif)

**Use Target Value**

Specifies whether to use target value for the bar gauge.

* **Target Value**   
   Specifies the target value. You can also [use a formula to control the value](https://devnet.logianalytics.com/hc/en-us/articles/1500010033202-Using-Formulas-to-Control-Object-Properties).

**Pointer Style**

Specifies the pointer style for the target value.

* **Target Pointer**  
   Specifies the style of the target pointer. Select a style from the drop-down list or select Customized and specify another image as the target pointer.
* **Width**  
   Specifies the width of the target pointer.
* **Height**  
   Specifies the height of the target pointer.
* **Position**  
   Specifies the position of the target pointer relative to the bar.
* **Gap**  
   Specifies the distance between the target pointer and the bar.

**Pointer Color**

Specifies color properties of the target pointer.

* **Color**  
   Specifies the color of the target pointer.
* **Transparency**  
   Specifies the color transparency of the target pointer.

**Target Value**

Specifies the properties of the target value.

* **Show Target Value**   
   Specifies whether to show the target value on the bar gauge.
  + **Position**  
     Specifies the position of the target value relative to the bar. Select the position from the drop-down list or select customized to customize the position by dragging the target value in the design area.

## Frame

Specifies properties for the frame of the bar gauge.

![Format Bar Gauge dialog - Frame](https://devnet.logianalytics.com/hc/article_attachments/4404901255191/fmtbargauge_frm.gif)

**Size**

Specifies the size properties of the frame.

* **Frame Size**   
   Specifies the size of the frame.

**Fill**

Specifies the color and transparency of the frame.

* **Fill**  
   Specifies the color to fill the frame.
* **Transparency**  
   Specifies the transparency to fill the frame.

**Border**

Specifies the properties for borders of the frame.

* **Border Type**  
   Displays the type of the border.
* **Color**  
   Specifies the color of the border. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010035022-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color directly in the text box.
* **Line Style**  
   Specifies the line style to apply to the border.
* **Transparency**  
   Specifies the transparency for color of the border.
* **Thickness**  
   Specifies the thickness of the border, in pixels.
* **End Caps**  
   Specifies the ending style of the border line.

+ **butt**  
   Ends unclosed sub paths and dash segments with no added decoration.
+ **round**  
   Ends unclosed sub paths and dash segments with a round decoration that has a radius equal to half of the width of the pen.
+ **square**  
   Ends unclosed sub paths and dash segments with a square projection that extends beyond the end of the segment to a distance equal to half of the line width.

* **Line Joint**  
   Specifies the line joint style for the border line.
  + **miter**  
     Joins path segments by extending their outside edges until they meet.
  + **round**  
     Joins path segments by rounding off the corner at a radius of half the line width.
  + **bevel**  
     Joins path segments by connecting the outer corners of their wide outlines with a straight segment.
  + **joint round**  
     Joins path segments by rounding off the corner at the specified radius.
* **Path**  
   Specifies the fill pattern of the border line.

  + **Outline Path**  
     Specifies the fill pattern of the border line to be outline path.
  + **Fill Path**  
     Specifies the fill pattern of the border line to be whole path.
* **Dash**  
   Specifies the dash size of border line.
  + **Auto Adjust Dash**  
     If selected, the dash size will be adjusted automatically.
  + **Fixed Dash Size**  
     If selected, the dash size will be fixed size.

**Gauge Group Name**

Specifies properties for the gauge group name.

* **Show Gauge Group Name**   
   Specifies whether to show names for the bars in the bar gauge which are values of the field on its category axis. If the bar gauge contains no category field, the group name shows Report by default.
  + **Position**  
     Specifies the position of the names relative to the bars.

## Range Color

Specifies different colors to fill the bars in different ranges.

![Format Bar Gauge dialog - Range Color](https://devnet.logianalytics.com/hc/article_attachments/4404901255447/fmtbargauge_rgclr.gif)

**Use Gradient Effect**

Specifies whether to use gradient effect for the color.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif)

Adds a new color range.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif)

Removes the selected color range.

**Minimum**

Specifies the minimum value of the range.

**Maximum**

Specifies the maximum value of the range.

**Color**

Specifies the color schema of the range. Select in the color cell to customize the color on the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010035022-Menu-Tabs#Palette).

**Name**

Displays the name of the range.

**Others**

Specifies the properties for values that do not fall into any of the ranges you defined.

* **Name**  
   Specifies the name for the values.
* **Color**  
   Specifies the color for the values. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010035022-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color directly in the text box.

## Hint

Specifies properties for the hint of the bar gauge.

![Format Bar Gauge dialog - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404901255703/fmtbargauge_hint.gif)

**Show Category and Series**

Specifies whether to include the category and series values in the hint.

**Auto Scale in Number**

Specifies whether to automatically scale the values displayed in the hint that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

The option "auto" means that the property setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010069721-Chart-Properties#AutoScale).

## Behaviors

Specifies web behaviors to the bar gauge. This tab is only available to charts in library components.

![Format Bar Gauge dialog - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404909218839/fmtbargauge_bhvr.gif)

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010066241-Format-Bar-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010066281-Format-Bubble-Dialog)
