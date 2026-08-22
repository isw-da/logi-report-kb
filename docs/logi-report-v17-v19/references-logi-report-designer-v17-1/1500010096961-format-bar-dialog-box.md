---
title: "Format Bar Dialog Box"
id: 1500010096961
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010096961-Format-Bar-Dialog-Box
updated_at: 2021-07-23T19:15:26Z
---

# Format Bar Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010096941-Format-Area-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010059102-Format-Bar-Gauge-Dialog-Box)

# Format Bar Dialog Box

You can use the Format Bar dialog box to [format the bars of a bar/bench chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010094461-Formatting-the-Bars-in-a-Bar-Bench-Chart). This topic describes the options in the dialog box.

Designer displays the Format Bar dialog box when you right-click a bar/bench in a bar/bench chart and select Format Bar from the shortcut menu, or double-click a bar/bench of a bar/bench chart.

The dialog box contains the following tabs (Designer displays the Size tab for a 2-D bar/bench chart, and the Behaviors tab if the chart is in a library component):

* [General Tab](#General)
* [Size Tab](#Size)
* [Fill Tab](#Fill)
* [Border Tab](#Border)
* [Data Label Tab](#Data)
* [Hint Tab](#Hint)
* [Behaviors Tab](#Behaviors)

You see these buttons in all the tabs:

**OK**

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Apply**

Select to apply all changes and leave the dialog box open.

**Help**

Select to view information about the dialog box.

## General Tab

Designer displays different options in the General tab for a [2-D bar/bench chart](#2D) and a [3-D bar/bench chart](#3D). You can use it to specify the general properties of the bars/benches.

### For 2-D Bar/Bench Chart

![Format Bar - General 2-D](https://devnet.logianalytics.com/hc/article_attachments/4404848570263/fmtbar_gnrl_1.gif)

**Style**

Select the style of the bars: Normal or Cylinder.

**Layout**

You can specify the layout of the bars in the box.

* **Clustered - 2-D**  
  Select to display and compare data values across categories.
* **Stacked - 2-D**  
  Select to display and compare the contribution of each data value to a total across categories.
* **100% Stacked - 2-D**  
  Select to display and compare the percentage that each data value contributes to a total across categories.

**Depth**

You can specify the depth properties for bars in this box.

* **Use Depth**  
  Specify whether to make the bars three-dimensional. You can select the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif) to [use a formula to control the property](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties) if the chart uses a query resource.
  + **Depth**  
    Specify the depth of the bars, in pixels.
  + **Direction**  
    Specify the direction for depth of the bars, in degrees.

### For 3-D Bar/Bench Chart

![Format Bar - General 3-D](https://devnet.logianalytics.com/hc/article_attachments/4404856965911/fmtbar_gnrl_2.gif)

**Size**

You can specify the size of the bars in this box.

* **Bar Width**  
  Specify the bar width as a percentage of the unit width.

**Layout**

You can specify the layout of the bars in this box.

* **Clustered Bar 3-D**  
  Select to apply clustered bars with a 3-D visual effect.
* **Stacked Bar 3-D**  
  Select to apply stacked bars with a 3-D visual effect.
* **100% Stacked Bar 3-D**  
  Select to apply 100% stacked bars with a 3-D visual effect.
* **Array 3-D**  
  Select to apply array bars with a 3-D visual effect.

## Size Tab

Designer displays the Size tab if the chart is a 2-D bar/bench chart. You can use it to specify the size of the 2-D bars.

Designer displays different options in the tab when you select to use [dynamic bar width](#Dynamic) or [fixed bar width](#Fix).

### For Dynamic Bar Width

To use dynamic bar width, make sure Fixed Bar Width is unselected.

![Format Bar - Size for dynamic bar width](https://devnet.logianalytics.com/hc/article_attachments/4404848570519/fmtbar_size_dynmc.gif)

**Bar Width**

Specify the general bar width as a percentage of the unit width.

**Bar Gap**

Designer enables this option only for a clustered bar/bench chart which contains data on the series axis or has more than one value on the value axis. You can use it to specify the distance between two bars within a group as a percentage of the unit width.

**Individual Bar Width**

Designer enables the options in this box only for a clustered bar/bench chart which contains data on the series axis or has more than one value on the value axis. You can use the options to specify properties of the individual bars.

* ![Wider button](https://devnet.logianalytics.com/hc/article_attachments/4404848496151/btn_wider.gif)/![Narrower button](https://devnet.logianalytics.com/hc/article_attachments/4404848497559/btn_narrower.gif)  
  Specify how much the selected bars in the same data series is wider/narrower than a general bar, in percentage.
* **Size List**  
  Select to open the [Size List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060342-Size-List-Dialog-Box) to specify the width and gap for the bars in the same data series respectively.

### For Fixed Bar Width

To use fixed bar width, make sure Fixed Bar Width is selected.

![Format Bar - Size for fixed bar width](https://devnet.logianalytics.com/hc/article_attachments/4404848570775/fmtbar_size_fix.gif)

**Bar Width**

Specify the general bar width, in inches.

**Bar Gap**

Designer enables this option only for a clustered bar/bench chart which contains data on the series axis or has more than one value on the value axis. You can use it to specify the distance between two bars within a group, in inches.

**Outer Gap**

Designer enables this option only for a clustered bar/bench chart which contains data on the series axis or has more than one value on the value axis.
You can use it to specify the distance between bars out of a group, in inches.

**Individual Bar Width**

Designer enables the options in this box only for a clustered bar/bench chart which contains data on the series axis or has more than one value on the value axis. You can use the options to specify the properties of the individual bars.

* **Width**  
  Specify the width of the selected bars in the same data series, in inches.
* **Gap**  
  Specify the gap between the selected bars in the same data series and the bars beside it, in inches.
* **Size List**  
  Select to open the [Size List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060342-Size-List-Dialog-Box) to specify the width and gap for the bars in the same data series respectively.

![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif)

Select to [use a formula to control the value](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties) of an option.

**Fixed Bar Gap**

Select to use a fixed bar gap. Clear this option if you want to customize the percentages of the bar width and bar gap within a group.

* **Bar Width**  
  Specify the width of the bars within a group as a percentage of the unit width between the two adjacent tick marks on the X axis.
* **Bar Gap**  
  Specify the distance between the two adjacent bars within a group as a percentage of the width of a bar. The option takes effect in a clustered bar/bench chart which contains data on the series axis or has more than one value on the value axis.

## Fill Tab

Use this tab to specify the color pattern to fill the bars.

![Format Bar - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404856966679/fmtbar_fill.gif)

**Use Single Color**

Select to apply single color pattern to the bars.

* **Self Settings**  
  Select to apply the color pattern to the bars themselves only. If you do not select the option, Designer synchronizes the color settings you define here to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#Pattern) on the chart object in the Report Inspector, which the data markers of other subtypes can also apply if the chart is a combo chart.
* **Color**  
  Specify the color for all the bars if the chart has no series field, or the color of the bars in the current data series if the chart has series field. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Transparency**  
  Specify the transparency of the color.
* **Vary Colors by Color List**  
  Designer enables this option only for the clustered bar types and when the chart has no series field. Select it if you want to apply different colors to the bars.
* **Color List**  
  Select to open the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058302-Color-List-Dialog-Box) to modify the color pattern for each bar if the chart has no series field, or the color pattern for bars in the same data series if the chart has series field.

**Use Single Color with Condition**

Select to apply different color patterns to the bars based on different conditions. You can select the Advanced or Normal button to switch between the two editing modes to edit the conditions.

* **Normal**
  + **Select Field**  
    The drop-down list contains all the available fields to which you can apply the conditional fill. Select the field on which you want to define the conditions.
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**  
    Select to add a new condition.
  + ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**  
    Select to delete the specified user-defined condition.
  + **Value**  
    Designer displays the column when you select the category or series field of the chart, or a field the values of which are not numbers from the Select Field drop-down list. It shows the values that you specify for each condition.
  + **Start Value**  
    Designer displays the column when you select a value field of the chart, or a field containing numeric values from the Select Field drop-down list. It shows the start values that you specify for each condition.
  + **End Value**  
    Designer displays the column when you select a value field of the chart, or a field containing numeric values from the Select Field drop-down list. It shows the end values that you specify for each condition.
  + **Color**  
    The column shows the colors that you specify to apply to the values which meet the conditions. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
  + **Transparency**  
    The column shows the transparency of the colors that you specify for the conditions.
  + **Label**  
    Select to modify the expression of the specified condition, which Designer displays as its legend entry label.
  + **Value**  
    Designer displays the option after you select a value field of the chart, or a field containing numeric values from the Select Field drop-down list.
    Select it if you want to display data in the condition expression as value.
  + **Percent**  
    Designer displays the option after you select a value field of the chart, or a field containing numeric values from the Select Field drop-down list, and enables it only when the chart is of the 100% Stacked Bar/Bench 2-D or 100% Stacked Bar/Bench 3-D type. Select it if you want to display data in the condition expression in percent.
* **Advanced**
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**  
    Select to open the [Edit Conditions dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058702-Edit-Conditions-Dialog-Box#Chart) to create a condition and specify its color pattern.
  + ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404856829719/btn_edit.gif)**Edit button**  
    Select to open the [Edit Conditions dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058702-Edit-Conditions-Dialog-Box#Chart) to edit the specified condition and its color pattern.
  + ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**  
    Select to delete the specified user-defined condition.
  + **Condition**  
    The column shows the default condition "Other" and the expressions of the conditions that you define in the Edit Condition dialog box.
  + **Color**  
    The column shows the colors that you specify to apply to the values which meet the conditions you define in the Edit Condition dialog box. For the default "Other" condition, you can edit its color by selecting the color indicator and selecting a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or inputting the hexadecimal value (for example, 0xff0000) of a color in the text box.
  + **Transparency**  
    The column shows the transparency of the colors that you specify for the conditions in the Edit Condition dialog box. For the default "Other" condition, you can select in the cell to specify the transparency.
  + **Label**  
    Select to modify the expression of the specified condition, which Designer displays as its legend entry label.
  + **Value**  
    The option indicates that Designer displays data in the condition expressions as value. You cannot change it.
  + **Percent**  
    Designer does not support the option when you edit conditions in the advanced mode.

**Use Multiple Colors with Condition**

Designer enables this option only when the chart is one of the following types: Clustered Bar/Bench 2-D, Clustered Bar/Bench 3-D, and Bar/Bench 3-D. Select it if you want to divide each bar into several parts based on different value ranges along the direction of the value axis and apply separate color patterns to these different value ranges.

* **Select Field**  
  The drop-down list displays the first value field of the chart. All conditions are based on this field.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**  
  Select to add a new condition.
* ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**  
  Select to delete the specified condition.
* **Start Value**  
  The column shows the start values that you specify for each condition.
* **End Value**  
  The column shows the end values that you specify for each condition.
* **Color**  
  The column shows the colors that you specify to apply to the values which meet the conditions. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Transparency**  
  The column shows the transparency of the colors that you specify for the conditions.
* **Label**  
  Select to modify the expression of the selected condition, which Designer displays as its legend entry label.
* **Value**  
  The option indicates that Designer displays data in the condition expressions as value. You cannot change it.
* **Percent**  
  Designer does not support the option for this fill type.

**Sample**

The box displays a preview sample of your selection.

## Border Tab

Use this tab to specify the properties for the border of the bars.

![Format Bar - Border](https://devnet.logianalytics.com/hc/article_attachments/4404848571031/fmtbar_border.gif)

**Show Border**

Select to show the border of the bars. Designer enables the other border properties in this tab after you select the option.

**Color**

Specify the color of the border. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.

**Transparency**

Specify the transparency for the color of the border.

**Line Style**

Select the line style of the border.

**Thickness**

Specify the thickness of the border, in pixels.

**End Caps**

Select the ending style of the border line.

* **butt**  
  Select to end unclosed sub paths and dash segments with no added decoration.
* **round**  
  Select to end unclosed sub paths and dash segments with a round decoration that has a radius equal to half of the width of the pen.
* **square**  
  Select to end unclosed sub paths and dash segments with a square projection that extends beyond the end of the segment to a distance equal to half of the line width.

**Line Joint**

Select the joint style of the border line.

* **miter**  
  Select to join path segments by extending their outside edges until they meet.
* **round**  
  Select to join path segments by rounding off the corner at a radius of half the line width.
* **bevel**  
  Select to join path segments by connecting the outer corners of their wide outlines with a straight segment.

**Sample**

The box displays a preview sample of your selection.

**Path**

You can specify the fill pattern of the border in this box.

* **Outline Path**  
  Select to use outline path for the border.
* **Fill Path**  
  Select to use whole path for the border.

**Dash**

You can specify the dash size of the border
in this box if you select a dash line style for the border.

* **Auto Adjust Dash**  
  Select to adjust the dash size automatically.
* **Fixed Dash Size**  
  Select to use fixed dash size.

## Data Label Tab

Use this tab to specify the properties of the data labels on the bars.

![Format Bar - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4404848571287/fmtbar_data.gif)

**Static Data Label**

You can specify the properties of the static data labels on the bars in this box. Designer disables the options in the box for a 3-D bar/bench chart.

* **Show Static Data Label**  
  Select to show the static data labels. Designer enables the other static data label properties after you select this option.
* **Position**  
  Select the position of the static data labels on the bars.
  + **auto fit**  
    Select to display the static data labels automatically.
  + **outside top**   
    Select to display the static data labels on the outside top of the bars.
  + **inside top**  
    Select to display the static data labels on the inside top of the bars.
  + **inside center**  
    Select to display the static data labels at the inside center of the bars.
  + **inside bottom**  
    Select to display the static data labels at the inside bottom of the bars.
* **Data Label Type**  
  Select in which way to display the values in the static data labels.
  + **value**  
    Select to show the value for each bar.
  + **percent**  
    Select to show the percentage of each bar to the total.
  + **value and percent**  
    Select to show the value and the percentage for each bar.
* **Auto Scale in Number**  
  Specify whether to automatically scale the Number values in the static data labels which fall into the following two ranges:
  + When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
  + When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.

  By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property [on the chart in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#AutoScale) for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.
* **Auto Arrange**  
  Designer enables this option when you select the Position option of one of the following: inside center, inside top, or inside bottom. You can use it to specify whether to display the static data labels inside the bars at the best position.
  + **true**  
    Select to display the static data labels horizontally at the specified position if the bar has enough room horizontally; otherwise, display them vertically. If a bar does not have enough room both vertically and horizontally, Designer does not display its static data label.
  + **false**  
    Select to display the static data labels at the specified position. If the labels get overlapping, Designer does not some of them.
* **Suppress Label When 0**  
  Select if you do not want to display the static data label whose value is 0 in the chart.

**Font**

You can specify the font format of the text in the static data labels in this box.

* **Font list**  
  The drop-down list contains all the font faces that you can select to apply to the text.
* **Font Size**  
  Specify the font size of the text.
* **Font Color**  
  Specify the font color of the text. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Transparency**  
  Specify the color transparency of the text.
* **Rotation**  
  Specify the rotation angle of the text around its center, in degrees. The default value is 0.
* **Shearing**  
  Specify the gradient of the text.

**Effects**

You can specify the special effects for the text in the static data labels in this box.

* **Style**  
  Select the font style of the text. It can be one of the following: plain, bold, italic, and bold italic.
* **Strikethrough**  
  Select the style of the horizontal line using which to strikethrough the text. It can be one of the following: none, thin line, bold line, and double lines.
* **Underline**  
  Select the style of the horizontal line under the text. It can be one of the following: none, single, single lower, bold line, bold lower, double lines, bold double, patterned line, and bold patterned. When you select "patterned line" or "bold patterned", Designer draws a line or bold line in the pattern of the text.

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4404856819991/criticalicon.gif) Web Report Studio and JDashboard do not support underlining chart text, therefore, Logi Report Engine ignores this property when the chart runs in Web Report Studio or is used in a dashboard.

* **Superscript**  
  Select to raise the text above the baseline and change the text to a smaller font size, if a smaller size is available.
* **Embossed**  
  Select to make the text appear to be raised off the page in relief.
* **Outlined**  
  Select to display the inner and outer borders of each character.
* **Subscript**  
  Select to lower the text below the baseline and change the text to a smaller font size, if a smaller size is available.
* **Engraved**  
  Select to make the text appear to be imprinted or pressed into the page.
* **Shadowed**  
  Select to add a shadow beneath and to the right of the text.

## Hint Tab

Use this tab to specify the properties for the hint of the bars.

![Format Bar - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404848571799/fmtbar_hint.gif)

**Show Category and Series**

Select to include the category and series values in the hint.

**Auto Scale in Number**

Specify whether to automatically scale the Number values in the hint which fall into the following two ranges:

* When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.

By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property [on the chart in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#AutoScale) for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.

## Behaviors Tab

Designer displays the Behaviors tab only when the bar/bench chart is in a library component. You can use it to specify web behaviors to the bars/benches.

![Format Bar - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404848572055/fmtbar_bhvr.gif)

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**

Select to add a new web behavior line.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**

Select to delete the specified web behavior.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Up button**

Select to move the specified web behavior higher in the list. At runtime, when an event bound with more than one action happens, JDashboard triggers the upper action first.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Down button**

Select to move the specified web behavior lower in the list.

**Events**

The column shows the events that you select to trigger the web actions.

**Actions**

The column shows the actions that you specify for the events to trigger. To bind a web action to an event, select the ellipsis button ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif) in the action cell and Designer displays the [Web Action List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060822-Web-Action-List-Dialog-Box) for you to specify the web action.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010096941-Format-Area-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010059102-Format-Bar-Gauge-Dialog-Box)
