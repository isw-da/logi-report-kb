---
title: "Format Bar Dialog Box"
id: 5735529553431
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735529553431-Format-Bar-Dialog-Box
updated_at: 2022-11-02T04:17:48Z
---

# Format Bar Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735565974167-Format-Area-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735514080535-Format-Bar-Gauge-Dialog-Box)

# Format Bar Dialog Box

You can use the Format Bar dialog box to [format the bars of a bar/bench chart](https://devnet.logianalytics.com/hc/en-us/articles/5735512007575-Formatting-Bar-Bench-Chart). This topic describes the options in the dialog box.

Designer displays the Format Bar dialog box when you right-click a bar/bench in a bar/bench chart and select Format Bar from the shortcut menu, or double-click a bar/bench of a bar/bench chart.

The dialog box contains the following tabs (Designer displays the Size tab for a 2-D bar/bench chart, and the Behaviors tab when the chart is in a library component):

* [General Tab](#General)
* [Size Tab](#Size)
* [Fill Tab](#Fill)
* [Border Tab](#Border)
* [Data Label Tab](#Data)
* [Hint Tab](#Hint)
* [Behaviors Tab](#Behaviors)

Designer displays these buttons in all the tabs:

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Apply**

Select to apply all changes and leave the dialog box open.

**Help**

Select to view information about the dialog box.

## General Tab

Designer displays different options in the General tab for a [2-D bar/bench chart](#2D) and a [3-D bar/bench chart](#3D). You can use it to specify general properties of the bars/benches.

### For 2-D Bar/Bench Chart

![Format Bar - General 2-D](https://devnet.logianalytics.com/hc/article_attachments/9898464124311/fmtbar_gnrl_1.gif)

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

You can specify the depth of the bars in this box.

* **Use Depth**  
  Specify whether to add a 3-dimensional effect to the bars. You can select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/9898457345303/btn_fmla.gif) to [use a formula to control the property](https://devnet.logianalytics.com/hc/en-us/articles/5735545031703-Using-Formulas-to-Control-Object-Properties) if the chart uses a query resource.
  + **Depth**  
    Specify the 3-dimensional depth effect of the bars, in pixels.
  + **Direction**  
    Specify the direction of the depth, in degrees.

### For 3-D Bar/Bench Chart

![Format Bar - General 3-D](https://devnet.logianalytics.com/hc/article_attachments/9898464131607/fmtbar_gnrl_2.gif)

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

Designer displays the Size tab when the chart is a 2-D bar/bench chart. You can use it to specify the size of the 2-D bars.

Designer displays different options in the tab when you select to use [dynamic bar width](#Dynamic) or [fixed bar width](#Fix).

### For Dynamic Bar Width

To use dynamic bar width, make sure Fixed Bar Width is cleared.

![Format Bar - Size for dynamic bar width](https://devnet.logianalytics.com/hc/article_attachments/9898464134807/fmtbar_size_dynmc.gif)

**Bar Width**

Specify the general bar width as a percentage of the unit width.

**Bar Gap**

Designer enables this option only for a clustered bar/bench chart which contains data on the series axis or has more than one value on the value axis. You can use it to specify the distance between two bars within a group as a percentage of the unit width.

**Individual Bar Width**

Designer enables this box only for a clustered bar/bench chart which contains data on the series axis or has more than one value on the value axis. You can use the options in this box to specify properties of the individual bars.

* ![Wider button](https://devnet.logianalytics.com/hc/article_attachments/9898478023575/btn_wider.gif)/![Narrower button](https://devnet.logianalytics.com/hc/article_attachments/9898478034839/btn_narrower.gif)  
  Specify how much the selected bars in the same data series is wider/narrower than a general bar, in percentage.
* **Size List**  
  Select to open the [Size List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735567246359-Size-List-Dialog-Box) to specify the width and gap for the bars in the same data series respectively.

### For Fixed Bar Width

To use fixed bar width, make sure Fixed Bar Width is selected.

![Format Bar - Size for fixed bar width](https://devnet.logianalytics.com/hc/article_attachments/9898464141591/fmtbar_size_fix.gif)

**Bar Width**

Specify the general bar width, in inches.

**Bar Gap**

Designer enables this option only for a clustered bar/bench chart which contains data on the series axis or has more than one value on the value axis. You can use it to specify the distance between two bars within a group, in inches.

**Outer Gap**

Designer enables this option only for a clustered bar/bench chart which contains data on the series axis or has more than one value on the value axis.
You can use it to specify the distance between bars out of a group, in inches.

**Individual Bar Width**

Designer enables this box only for a clustered bar/bench chart which contains data on the series axis or has more than one value on the value axis. You can use options in this box to specify properties of the individual bars.

* **Width**  
  Specify the width of the selected bars in the same data series, in inches.
* **Gap**  
  Specify the gap between the selected bars in the same data series and the bars beside it, in inches.
* **Size List**  
  Select to open the [Size List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735567246359-Size-List-Dialog-Box) to specify the width and gap for the bars in the same data series respectively.

**Fixed Bar Gap**

Select to use a fixed bar gap. Clear this option if you want to customize the percentages of the bar width and bar gap within a group.

* **Bar Width**  
  Specify the width of the bars within a group as a percentage of the unit width between the two adjacent tick marks on the X axis.
* **Bar Gap**  
  Specify the distance between the two adjacent bars within a group as a percentage of the width of a bar. This option takes effect in a clustered bar/bench chart which contains data on the series axis or has more than one value on the value axis.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) Designer displays the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/9898457345303/btn_fmla.gif) for some options. It indicates that you can [use a formula to control the value](https://devnet.logianalytics.com/hc/en-us/articles/5735545031703-Using-Formulas-to-Control-Object-Properties) of an option.

## Fill Tab

Use this tab to specify the fill pattern of the bars.

![Format Bar - Fill](https://devnet.logianalytics.com/hc/article_attachments/9898481235863/fmtbar_fill.gif)

**Use Single Color**

Select to apply single color pattern to fill the bars.

* **Self Settings**  
  Select to apply the color pattern to the bars themselves only. When this option is cleared, Designer synchronizes the color pattern that you specify here with the [Pattern List](https://devnet.logianalytics.com/hc/en-us/articles/5735545992599-Chart-Properties#Pattern) property of the chart in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart.
* **Color**  
  Specify the color for all bars if the chart has no series field, or the color of the bars in the current data series if the chart has series field. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette), or type the hexadecimal value of a color (for example, 0xff0000) in the text box.
* **Transparency**  
  Specify the transparency of the color.
* **Vary Colors by Color List**  
  Designer enables this option only for the clustered bar types and when the chart has no series field. Select it if you want to apply different colors to the bars.
* **Color List**  
  Select to open the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522093463-Color-List-Dialog-Box) to modify the color pattern for each bar if the chart has no series field, or the color pattern for bars in the same data series if the chart has series field.

**Use Single Color with Condition**

Select to apply different color patterns to the bars based on different conditions. You can select Advanced or Normal to switch between the two editing modes to edit the conditions.

* **Normal**
  + **Select Field**  
    This drop-down list contains all the available fields to which you can apply the conditional fill. Select the field on which you want to define the conditions.
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif)**Add button**  
    Select to add a new condition.
  + ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif)**Remove button**  
    Select to delete the specified user-defined condition.
  + **Value**  
    Designer displays the column when you select the category or series field of the chart, or a field the values of which are not numbers from the Select Field drop-down list. It shows the values that you specify for each condition.
  + **Start Value**  
    Designer displays the column when you select a value field of the chart, or a field containing numeric values from the Select Field drop-down list. It shows the start values that you specify for each condition.
  + **End Value**  
    Designer displays the column when you select a value field of the chart, or a field containing numeric values from the Select Field drop-down list. It shows the end values that you specify for each condition.
  + **Color**  
    This column shows the colors you specify to apply to values that which meet the conditions. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette), or type the hexadecimal value of a color (for example, 0xff0000) in the text box.
  + **Transparency**  
    This column shows the transparency of the colors that you specify for the conditions.
  + **Label**  
    Select to modify the expression of the specified condition, which Designer displays as its legend entry label.
  + **Value**  
    Designer displays this option after you select a value field of the chart, or a field containing numeric values from the Select Field drop-down list.
    Select it if you want to display data in the condition expression as value.
  + **Percent**  
    Designer displays this option after you select a value field of the chart, or a field containing numeric values from the Select Field drop-down list, and enables it only when the chart applies the 100% Stacked Bar/Bench 2-D or 100% Stacked Bar/Bench 3-D type. Select it if you want to display data in the condition expression in percent.
* **Advanced**
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif)**Add button**  
    Select to open the [Edit Conditions dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735513701143-Edit-Conditions-Dialog-Box#Chart) to create a condition and specify its color pattern.
  + ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/9898474047383/btn_edit.gif)**Edit button**  
    Select to open the [Edit Conditions dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735513701143-Edit-Conditions-Dialog-Box#Chart) to edit the specified condition and its color pattern.
  + ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif)**Remove button**  
    Select to delete the specified user-defined condition.
  + **Condition**  
    This column shows the default condition "Other" and the expressions of the conditions that you define in the Edit Condition dialog box.
  + **Color**  
    This column shows the colors you specify to apply to values that meet the conditions you define in the Edit Condition dialog box. For the default "Other" condition, you can edit its color by selecting the color indicator and selecting a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette) or inputting the hexadecimal value (for example, 0xff0000) of a color in the text box.
  + **Transparency**  
    This column shows the transparency of the colors that you specify for the conditions in the Edit Condition dialog box. For the default "Other" condition, you can select in the cell to specify the transparency.
  + **Label**  
    Select to modify the expression of the specified condition, which Designer displays as its legend entry label.
  + **Value**  
    This option indicates that Designer displays data in the condition expressions as value. You cannot change it.
  + **Percent**  
    Designer does not support this option when you edit conditions in the advanced mode.

**Use Multiple Colors with Condition**

Designer enables this option only when the chart is one of the following types: Clustered Bar/Bench 2-D, Clustered Bar/Bench 3-D, and Bar/Bench 3-D. Select it if you want to divide each bar into several parts based on different value ranges along the direction of the value axis and apply separate color patterns to these different value ranges.

* **Select Field**  
  This drop-down list displays the first value field of the chart. All conditions are based on this field.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif)**Add button**  
  Select to add a new condition.
* ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif)**Remove button**  
  Select to delete the specified condition.
* **Start Value**  
  This column shows the start values that you specify for each condition.
* **End Value**  
  This column shows the end values that you specify for each condition.
* **Color**  
  This column shows the colors you specify to apply to values that meet the conditions. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette), or type the hexadecimal value of a color (for example, 0xff0000) in the text box.
* **Transparency**  
  This column shows the transparency of the colors that you specify for the conditions.
* **Label**  
  Select to modify the expression of the selected condition, which Designer displays as its legend entry label.
* **Value**  
  This option indicates that Designer displays data in the condition expressions as value. You cannot change it.
* **Percent**  
  Designer does not support this option for this fill type.

**Sample**

This box displays a preview sample based on your selections.

## Border Tab

Use this tab to specify properties for the border of the bars.

![Format Bar - Border](https://devnet.logianalytics.com/hc/article_attachments/9898464175511/fmtbar_border.gif)

**Show Border**

Select to show the border of the bars. Designer enables the other border properties in this tab after you select this option.

**Color**

Specify the color of the border. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette), or type the hexadecimal value of a color (for example, 0xff0000) in the text box.

**Transparency**

Specify the transparency of the border.

**Line Style**

Select the line style of the border.

**Thickness**

Specify the width of the border, in pixels.

**End Caps**

Select the ending style of the border.

* **butt**  
  Select to end unclosed subpaths and dash segments with no added decoration.
* **round**  
  Select to end unclosed subpaths and dash segments with a round decoration that has a radius equal to half of the line width.
* **square**  
  Select to end unclosed subpaths and dash segments with a square projection that extends beyond the end of the segment to a distance equal to half of the line width.

**Line Joint**

Select the joint style of the border.

* **miter**  
  Select to join path segments by extending their outside edges until they meet.
* **round**  
  Select to join path segments by rounding off the corner at a radius of half the line width.
* **bevel**  
  Select to join path segments by connecting the outer corners of their wide outlines with a straight segment.

**Sample**

This box displays a preview sample based on your selections.

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

Use this tab to specify properties of the data labels on the bars.

![Format Bar - Data Label](https://devnet.logianalytics.com/hc/article_attachments/9898464186903/fmtbar_data.gif)

**Static Data Label**

You can specify properties of the static data labels on the bars in this box. Designer disables this box for a 3-D bar/bench chart.

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
  Specify whether to automatically scale the Number values in the static data labels that fall into the two ranges:
  + When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
  + When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.

  By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property [on the chart in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/5735545992599-Chart-Properties#AutoScale) for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.
* **Auto Arrange**  
  Designer enables this option when you select the Position option of one of the following: inside center, inside top, or inside bottom. You can use it to specify whether to display the static data labels inside the bars at the best position.
  + **true**  
    Select to display the static data labels horizontally at the specified position if the bar has enough room horizontally; otherwise, display them vertically. If a bar does not have enough room both vertically and horizontally, Designer does not display its static data label.
  + **false**  
    Select to display the static data labels at the specified position. If the labels overlap, Designer does not display some of them.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) After you set a rotation angle for the label text, Designer sets Auto Arrange to "false" automatically and disables this option.
* **Suppress Label When 0**  
  Select if you do not want to display the static data label when its value is 0.

**Font**

You can specify the font style of the text in the static data labels in this box.

* **Font list**  
  This drop-down list contains all the font faces you can select to apply to the text.
* **Font Size**  
  Specify the font size of the text.
* **Font Color**  
  Specify the font color of the text. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette), or type the hexadecimal value of a color (for example, 0xff0000) in the text box.
* **Transparency**  
  Specify the transparency of the text.
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

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) Web Report Studio and JDashboard do not support underlining chart text, therefore, this property is ignored when the chart runs in Web Report Studio or is used in a dashboard.

* **Superscript**  
  Select to raise the text above the baseline and change the text to a smaller font size, if a smaller size is available.
* **Subscript**  
  Select to lower the text below the baseline and change the text to a smaller font size, if a smaller size is available.
* **Embossed**  
  Select to make the text appear to be raised off the page in relief.
* **Engraved**  
  Select to make the text appear to be imprinted or pressed into the page.
* **Outlined**  
  Select to display the exterior border around each character of the text.
* **Shadowed**  
  Select to add a shadow beneath and to the right of the text.

## Hint Tab

Use this tab to specify properties for the hint of the bars.

![Format Bar - Hint](https://devnet.logianalytics.com/hc/article_attachments/9898481266967/fmtbar_hint.gif)

**Show Category and Series**

Select to include the category and series values in the hint.

**Auto Scale in Number**

Specify whether to automatically scale the Number values in the hint that fall into the two ranges:

* When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.

By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property [on the chart in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/5735545992599-Chart-Properties#AutoScale) for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.

**Customize Chart Value Names**

Select to customize the names of the fields on the value axis which you want to display in the hint. By default, Designer applies the display names of the fields in the hint to label the values which may be not intuitive to users. You can select the option and select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898422868887/btn_ellipsis2.gif) to customize the names in the [Customize Chart Value Names dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565355927-Customize-Chart-Value-Names-Dialog-Box) to help users better understand the values.

## Behaviors Tab

Designer displays the Behaviors tab only when the bar/bench chart is in a library component. You can use it to specify web behaviors to the bars/benches.

![Format Bar - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/9898464213399/fmtbar_bhvr.gif)

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif)**Add button**

Select to add a new web behavior line.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif)**Remove button**

Select to delete the specified web behavior.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif)**Move Up button**

Select to move the specified web behavior higher in the list. At runtime, when an event bound with more than one action happens, JDashboard triggers the upper action first.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif)**Move Down button**

Select to move the specified web behavior lower in the list.

**Events**

This column shows the events that you select to trigger the web actions.

**Actions**

This column shows the web actions that you specify for the events to trigger. Select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898423153431/btn_ellipsis1.gif) in each cell to bind the web action using the [Web Action List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735531755159-Web-Action-List-Dialog-Box).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735565974167-Format-Area-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735514080535-Format-Bar-Gauge-Dialog-Box)
