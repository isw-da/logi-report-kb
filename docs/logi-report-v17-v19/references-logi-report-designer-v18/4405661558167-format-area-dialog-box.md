---
title: "Format Area Dialog Box"
id: 4405661558167
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661558167-Format-Area-Dialog-Box
updated_at: 2022-01-27T20:36:09Z
---

# Format Area Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661557143-Format-Activity-Gauge-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661559447-Format-Bar-Dialog-Box)

# Format Area Dialog Box

You can use the Format Area dialog box to [format the areas of an area chart](https://devnet.logianalytics.com/hc/en-us/articles/4405664374935-Formatting-the-Areas-in-an-Area-Chart). This topic describes the options in the dialog box.

Designer displays the Format Area dialog box when you right-click an area in an area chart and select Format Area from the shortcut menu, or double-click an area of an area chart.

The dialog box contains the following tabs (Designer displays the Behaviors tab only when the chart is in a library component):

* [General Tab](#General)
* [Fill Tab](#Fill)
* [Border Tab](#Border)
* [Data Label Tab](#Data)
* [Hint Tab](#Hint)
* [Behaviors Tab](#Behaviors)

You see these buttons in the tabs:

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Apply**

Select to apply all changes and leave the dialog box open.

**Help**

Select to view information about the dialog box.

## General Tab

Designer displays different options in the General tab for a [2-D area chart](#2D) and a [3-D area chart](#3D). You can use ito specify the general properties of the areas.

### For 2-D Area Chart

![Format Area dialog box - General 2-D](https://devnet.logianalytics.com/hc/article_attachments/4420402478999/fmtarea_gnrl_1.gif)

**Layout**

You can specify the layout of the areas in this box.

* **None 2-D**  
  Select to apply 2-D areas to display the trend of the values over time or categories.
* **Stacked 2-D**  
  Select to apply stacked 2-D areas to display the trend of the contribution of each data value over categories.
* **100% Stacked 2-D**  
  Select to apply 100% stacked 2-D areas to display the trend of the percentage each data value contributes over categories.

**Depth**

You can specify the depth properties of the areas in this box.

* **Use Depth**  
  Specify whether to make the areas three-dimensional. You can select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4420410598551/btn_fmla.gif) to [use a formula to control the property](https://devnet.logianalytics.com/hc/en-us/articles/4405664601367-Using-Formulas-to-Control-Object-Properties) if the chart uses a query resource.
  + **Depth**  
    Specify the depth of the areas, in pixels.
  + **Direction**  
    Specifythe direction for depth of the lines, in degrees.

**High-Low Lines**

Select to show the high-low lines in the areas.

**Ignore Null Value**

Select to ignore null data values when drawing the areas. If you select this option, when a null data value appears, Designer ignores it and draws the area from the previous data value to the next data value directly; otherwise, the area is broken at the point of the null data value.

### For 3-D Area Chart

![Format Area dialog box - General 3-D](https://devnet.logianalytics.com/hc/article_attachments/4420410780311/fmtarea_gnrl_2.gif)

**Layout**

You can specify the layout for the areas in this box.

* **None 3-D**  
  Select to make the areas with a 3-D visual effect.
* **Stacked 3-D**  
  Select to apply stacked areas with a 3-D visual effect.
* **100% Stacked 3-D**  
  Select to apply 100% stacked areas with a 3-D visual effect.

**Ignore Null Value**

Select to ignore null data values when drawing the areas. If you select this option, when a null data value appears, Designer ignores it and draws the area from the previous data value to the next data value directly; otherwise, the area is broken at the point of the null data value.

## Fill Tab

Use this tab to specify the color pattern to fill the areas.

![Format Area dialog box - Fill](https://devnet.logianalytics.com/hc/article_attachments/4420394804887/fmtarea_fill.gif)

**Use Single Color**

Select to apply single color pattern to the areas.

* **Self Settings**  
  Select to apply the color pattern to the areas themselves only. If you do not select the option, Designer synchronizes the color settings you define here to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/4405664650263-Chart-Properties#Pattern) on the chart object in the Report Inspector, which the data markers of other subtypes can also apply if the chart is a combo chart.
* **Color**  
  Specify the color for the selected area. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value of a color (for example, 0xff0000) in the text box.
* **Transparency**  
  Specify the transparency of the color.
* **Color List**  
  Select to open the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661476887-Color-List-Dialog-Box) to modify the color pattern for each area.

**Use Single Color with Condition**

Designer does not support this fill type on area charts.

**Use Multiple Colors with Condition**

Designer enables this option only when the chart is of the Area 2-D or Area 3-D type. Select it if you want to divide each area into several parts based on different value ranges along the direction of the value axis and apply separate color patterns to these different value ranges.

* **Select Field**  
  This drop-down list displays the first value field of the chart. All conditions are based on this field.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420394650391/btn_add.gif)**Add button**  
  Select to add a new condition.
* ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420402325015/btn_trashcan.gif)**Remove button**  
  Select to delete the specified user-defined condition.
* **Start Value**  
  This column shows the start values that you specify for each condition.
* **End Value**  
  This column shows the end values that you specify for each condition.
* **Color**  
  This column shows the colors that you specify to apply to the values which meet the conditions. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value of a color (for example, 0xff0000) in the text box.
* **Transparency**  
  This column shows the transparency of the colors that you specify for the conditions.
* **Label**  
  Select to modify the expression of the selected condition, which Designer displays as the legend entry label.
* **Value**  
  This option indicates that Designer displays data in the condition expression as value. You cannot change it.
* **Percent**  
  Designer does not support this option for this fill type.

**Sample**

This box displays a preview sample based on your selections.

## Border Tab

Use this tab to specify properties for the border of the areas.

![Format Area dialog box - Border](https://devnet.logianalytics.com/hc/article_attachments/4420410780567/fmtarea_border.gif)

**Show Border**

Select to show the border of the areas. Designer enables the other border properties in this tab after you select this option.

**Color**

Specify the color of the border. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value of a color (for example, 0xff0000) in the text box.

**Transparency**

Specify the transparency for the color of the border.

**Line Style**

Select the line style of the border.

**Thickness**

Specify the width of the border, in pixels.

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

Use this tab to specify properties of the data labels for the area nodes.

![Format Area dialog box - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4420410780823/fmtarea_data.gif)

**Static Data Label**

You can specify properties of the static data labels for the area nodes in this box. Designer disables this box for a 3-D area chart.

* **Show Static Data Label**  
  Select to show the static data labels. Designer enables the other static data label properties after you select this option.
* **Position**  
  Select the position of the static data labels relative to the area nodes.
  + **auto fit**  
    Select to display the static data labels automatically.
  + **top center**  
    Select to display the static data labels in the top center of the nodes on the areas.
  + **top left**  
    Select to display the static data labels on the top left of the nodes on the areas.
  + **top right**  
    Select to display the static data labels on the top right of the nodes on the areas.
  + **bottom left**  
    Select to display the static data labels on the bottom left of the nodes on the areas.
  + **bottom center**  
    Select to display the static data labels in the bottom center of the nodes on the areas.
  + **bottom right**  
    Select to display the static data labels on the bottom right of the nodes on the areas.
* **Data Label Type**  
  Select in which way to display the values in the static data labels.
  + **value**  
    Select to show the value for each area node.
  + **percent**  
    Select to show the percentage of each area node to the total.
  + **value and percent**  
    Select to show the value and the percentage for each area node.
* **Auto Scale in Number**  
  Specify whether to automatically scale the Number values in the static data labels that fall into the two ranges:
  + When 1000 <= value < 10^15, Logi Report Engine applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
  + When 0 < value < 0.001 or value >= 10^15, Logi Report Engine uses scientific notation to scale the values.

  By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property [on the chart in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/4405664650263-Chart-Properties#AutoScale) for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.
* **Suppress Label When 0**  
  Select if you do not want to display the static data label whose value is 0 in the chart.

**Font**

You can specify the font format of the text in the static data labels in this box.

* **Font list**  
  This drop-down list contains all the font faces that you can select to apply to the text.
* **Font Size**  
  Specify the font size of the text.
* **Font Color**  
  Specify the font color of the text. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value of a color (for example, 0xff0000) in the text box.
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

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420394642839/noteicon.jpg) Web Report Studio and JDashboard do not support underlining chart text, therefore, this property is ignored when the chart runs in Web Report Studio or is used in a dashboard.

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

Use this tab to specify properties for the hint of the areas.

![Format Area dialog box - Hint](https://devnet.logianalytics.com/hc/article_attachments/4420410781079/fmtarea_hint.gif)

**Show Category and Series**

Select to include the category and series values in the hint.

**Auto Scale in Number**

Specify whether to automatically scale the Number values in the hint that fall into the two ranges:

* When 1000 <= value < 10^15, Logi Report Engine applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Logi Report Engine uses scientific notation to scale the values.

By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property [on the chart in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/4405664650263-Chart-Properties#AutoScale) for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.

**Customize Chart Value Names**

Select to customize the names of the fields on the value axis which you want to display in the hint. By default, Designer applies the display names of the fields in the hint to label the values which may be not intuitive to users. You can select the option and select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420402297111/btn_ellipsis2.gif) to customize the names in the [Customize Chart Value Names dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661488279-Customize-Chart-Value-Names-Dialog-Box) to help users better understand the values.

## Behaviors Tab

Designer displays the Behaviors tab only when the area chart is in a library component. You can use it to specify web behaviors to the areas.

![Format Area dialog box - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4420410781335/fmtarea_bhvr.gif)

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420394650391/btn_add.gif)**Add button**

Select to add a new web behavior line.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420402325015/btn_trashcan.gif)**Remove button**

Select to delete the specified web behavior.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420410588439/btn_mvup.gif)**Move Up button**

Select to move the specified web behavior higher in the list. At runtime, when an event bound with more than one action happens, JDashboard triggers the upper action first.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420410588695/btn_mvdwn.gif)**Move Down button**

Select to move the specified web behavior lower in the list.

**Events**

This column shows the events that you select to trigger the web actions.

**Actions**

This column shows the web actions that you specify for the events to trigger. Select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420410588951/btn_ellipsis1.gif) in each cell to bind the web action using the [Web Action List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661744791-Web-Action-List-Dialog-Box).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661557143-Format-Activity-Gauge-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661559447-Format-Bar-Dialog-Box)
