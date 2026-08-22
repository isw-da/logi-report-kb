---
title: "Format Line Dialog Box"
id: 1500010059242
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010059242-Format-Line-Dialog-Box
updated_at: 2021-07-23T19:15:30Z
---

# Format Line Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010059222-Format-Legend-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010059262-Format-Paper-Dialog-Box)

# Format Line Dialog Box

You can use the Format Line dialog box to [format the lines in a line chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010094521-Formatting-the-Lines-in-a-Line-Chart). This topic describes the options in the dialog box.

Designer displays the Format Line dialog box when you right-click a line in a line chart and select Format Line from the shortcut menu, or double-click any line in a line chart.

The dialog box contains the following tabs (Designer displays the Node tab for a 2-D line chart, the Border tab for a 3-D line chart, and the Behaviors tab if the chart is in a library component):

* [General Tab](#General)
* [Fill Tab](#Fill)
* [Node Tab](#Node)
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

Designer displays different options in the General tab for a [2-D line chart](#2D) and a [3-D line chart](#3D). You can use it to specify the general properties of the lines.

### For 2-D Line Chart

![Format Line - General 2-D](https://devnet.logianalytics.com/hc/article_attachments/4404848546839/fmtln_gnrl_1.gif)

**Layout**

You can specify the layout of the lines in this box.

* **None**  
  Select to display trend over categories on the lines.
* **Stacked**  
  Select to display the trend of the contribution of each data value over categories on the stacked lines.
* **100% Stacked**  
  Select to display the trend of the percentage that each data value contributes over categories on the 100% stacked lines.

**Depth**

You can specify the depth properties of the lines in this box.

* **Use Depth**  
  Specify whether to make the lines three-dimensional. You can select the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif) to [use a formula to control the property](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties) if the chart uses a query resource.
  + **Depth**  
    Specify the depth of the lines, in pixels.
  + **Direction**  
    Specify the direction for depth of the lines, in degrees.

**Ignore Null Value**

Select to ignore the null data values when drawing lines in the chart. If you select the option, when a null data value appears on a line, Designer ignores the value and draws the line from the previous data value to the next data value directly; otherwise, the line is broken at the point of the null data value.

**Smoothed Line**

Select to draw the lines smoothly without the sharp joints.

### For 3-D Line Chart

![Format Line - General 3-D](https://devnet.logianalytics.com/hc/article_attachments/4404848547095/fmtln_gnrl_2.gif)

**Thickness**

Specify the thickness of the lines, in pixels.

**Ignore Null Value**

Select to ignore the null data values when drawing lines in the chart. If you select the option, when a null data value appears on a line, Designer ignores the value and draws the line from the previous data value to the next data value directly; otherwise, the line is broken at the point of the null data value.

## Fill Tab

Use this tab to specify the color pattern to fill the chart lines.

![Format Line - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404856944535/fmtln_fill.gif)

**Use Single Color**

Select to apply single color pattern to the chart lines.

* **Self Settings**  
  Select to apply the color pattern to the chart lines themselves only. If you do not select the option, Designer synchronizes the color settings you define here to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#Pattern) on the chart object in the Report Inspector, which the data markers of other subtypes can also apply if the chart is a combo chart.
* **Fill**/**Normal Fill**  
  You can specify the fill effect of the chart lines in this box. Designer disables the options in the box for a 2-D line chart when you select Apply Color to Line in the Node tab.
  + **Color**  
    Specify the color for the selected chart line. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
  + **Transparency**  
    Specify the transparency of the color.
  + **Pattern List**/**Color List**  
    Select to open the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058302-Color-List-Dialog-Box) to modify the color pattern for each line in the chart.
* **Area**  
  Designer displays the box for a 2-D line chart. You can use it to specify the properties of the areas that are formed by the chart axes and the lines.
  + ![Marks content and feature updates for Logi Report v17.1. New feature new content.](https://devnet.logianalytics.com/hc/article_attachments/4404856832151/___newv17.1.jpg "New for Logi Report v17.1.")**Fill Area**  
    Select to fill the areas. Designer enables the other options in the box when you select this option.
  + **Color**  
    Specify the color to fill the selected chart line area. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
  + **Transparency**  
    Specify the transparency of the color.
  + **Area Pattern List**  
    Select to open the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058302-Color-List-Dialog-Box) to modify the color pattern of the areas formed by each chart line and the axes.
* **Line**  
  Designer displays the box for a 2-D line chart. You can use it to specify the line pattern of the chart lines.
  + **Line Style**  
    Select the style of the selected chart line.
  + **Thickness**  
    Specify the thickness of the selected chart line, in pixels.
  + **Line Pattern List**  
    Select to open the [Line Pattern List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097841-Line-Pattern-List-Dialog-Box) to modify the line pattern for each line in the chart.

**Use Single Color with Condition**

Designer enables this option for a 2-D line chart. Select it if you want to make each line apply its own single color pattern based on the defined conditions. You can select the Advanced or Normal button to switch between the two editing modes to edit the conditions.

* **Normal**
  + **Select Field**  
    The drop-down list contains all the available fields to which you can apply the conditional fill. Select the field on which you want to define the conditions.
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**  
    Select to add a new condition.
  + ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404856829719/btn_edit.gif)**Edit button**  
    Select to open the [Edit Line Style dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096321-Edit-Line-Style-Dialog-Box) to edit the line properties for values which meet the specified condition.
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
  + **Style**  
    The column shows the line styles that you specify for the conditions.
  + **Label**  
    Select to modify the expression of the specified condition, which Designer displays as its legend entry label.
  + **Value**  
    Designer displays the option after you select a value field of the chart, or a field containing numeric values from the Select Field drop-down list.
    Select it if you want to display data in the condition expression as value.
  + **Percent**  
    Designer displays the option after you select a value field of the chart, or a field containing numeric values from the Select Field drop-down list, and enables it only when the chart is of the 100% Stacked Line 2-D type. Select it if you want to display data in the condition expression in percent.
* **Advanced**
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**  
    Select to open the [Edit Conditions dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058702-Edit-Conditions-Dialog-Box#ChartLine) to create a condition and define the line properties for values which meet the condition.
  + ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404856829719/btn_edit.gif)**Edit button**  
    Select to open the [Edit Line Style dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096321-Edit-Line-Style-Dialog-Box) for editing the line properties if you select the default condition "Other"; or open the [Edit Conditions dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058702-Edit-Conditions-Dialog-Box#ChartLine) to edit the condition and the line properties for values which meet the condition, if you select a user-defined condition.
  + ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**  
    Select to delete the specified user-defined condition.
  + **Condition**  
    The column shows the default condition "Other" and the expressions of the conditions that you define in the Edit Condition dialog box
  + **Color**  
    The column shows the colors that you specify to apply to the values which meet the conditions. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box. Designer disables the column when you select Apply Color to Line in the Node tab.
  + **Transparency**  
    The column shows the transparency of the colors that you specify for the conditions. Designer disables the column when you select Apply Color to Line in the Node tab.

    ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) For a user-defined condition, Designer disables the Color and Transparency columns for it, if you edit the condition using Imported Condition. You can only use the Edit Condition dialog box to edit the two properties for the condition.
  + **Style**  
    The column shows the line styles that you specify for the conditions.
  + **Label**  
    Select to modify the expression of the specified condition, which Designer displays as its legend entry label.
  + **Value**  
    The option indicates that Designer displays data in the condition expressions as value. You cannot change it.
  + **Percent**  
    Designer does not support the option when you edit conditions in the advanced mode.

**Use Multiple Colors with Condition**

Designer does not support this fill type on line charts.

**Sample**

The box displays a preview sample of your selection.

## Node Tab

Designer displays the Node tab if the chart is a 2-D line chart. You can use it to specify the properties for the nodes on chart lines.

![Format Line - Node](https://devnet.logianalytics.com/hc/article_attachments/4404848547351/fmtln_node.gif)

**Use Single Color**

Select to apply single color pattern to the nodes.

* **Self Settings**  
  Select to apply the color pattern to the nodes themselves only. If you do not select the option, Designer synchronizes the color settings you define here to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#Pattern) on the chart object in the Report Inspector, which the data markers of other subtypes can also apply if the chart is a combo chart.
* **Shape**  
  You can specify the shape properties of the nodes in the selected chart line in this box.
  + **Style**  
    Select the style of the nodes in the selected chart line.
  + **Transparency**  
    Specify the color transparency of the nodes in the selected chart line.
  + **Width**  
    Specify the width of the nodes in the selected chart line, in pixels.
  + **Height**  
    Specify the height of the nodes in the selected chart line, in pixels.
  + **Show Node**  
    Specify whether to show nodes in the selected chart line. Designer applies the node related properties for the line only when you select "true" for the option; however, it does not control the options Show High Point and Show Low Point and the Color property for each.
    - **Color**  
      Specify the color of the nodes in the selected chart line. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
  + **Show High Point**  
    Specify whether to show the line node in the highest point in the selected chart line.
    - **Color**  
      Specify the color of the node in the highest point in the selected chart line. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
  + **Show Low Point**  
    Specify whether to show the line node in the lowest point in the selected chart line.
    - **Color**  
      Specify the color of the node in the lowest point in the selected chart line. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
  + **Show Highlight Point**  
    Specify whether to show the highlight point when you hover the mouse over a node in the selected chart line.
    - **Color**  
      Specify the color of the highlight point in the selected chart line. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Border**  
  Designer displays the box when you select a node style other than any of the following: plus, multiplication, star1, or star2. You can use it to specify the border properties of the nodes in the selected chart line.
  + **Border Color**  
    Specify the color for the border of the nodes in the selected chart line. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
  + **Transparency**  
    Specify the transparency for the border of the nodes in the selected chart line.
  + **Thickness**  
     Specify the thickness for the border of the nodes in the selected chart line, in pixels.
  + **Line Style**  
    Select the line style for the border of the nodes in the selected chart line.
* **Line**  
  Designer displays the box when you select the node style as one of the following: plus, multiplication, star1, and star2. You can use it to specify the line properties of the nodes in the selected chart line.
  + **Line Style**  
    Select the line style of the nodes in the selected chart line.
  + **Thickness**  
    Specify the line thickness of the nodes in the selected chart line.
* ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif)  
  Designer displays the button for some options if the chart uses a query resource. It indicates that you [use a formula to control the value of an option](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties).
* **Node Pattern List**  
  Select to open the [Node Pattern List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059862-Node-Pattern-List-Dialog-Box) to modify the node pattern for each chart line.

**Use Single Color with Condition**

Select to make each node apply its own single color pattern based on the defined conditions. You can select the Advanced or Normal button to switch between the two editing modes to edit the conditions.

* **Normal**
  + **Select Field**  
    The drop-down list contains all the available fields to which you can apply the conditional fill. Select the field on which you want to define the conditions.
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**  
    Select to add a new condition.
  + ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404856829719/btn_edit.gif)**Edit button**  
    Select to open the [Edit Node Style dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058782-Edit-Node-Style-Dialog-Box) to edit the node properties for the selected condition.
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
  + **Style**  
    The column shows the node styles that you specify for the conditions.
  + **Label**  
    Select to modify the expression of the specified condition, which Designer displays as its legend entry label.
  + **Value**  
    Designer displays the option after you select a value field of the chart, or a field containing numeric values from the Select Field drop-down list.
    Select it if you want to display data in the condition expression as value.
  + **Percent**  
    Designer displays the option after you select a value field of the chart, or a field containing numeric values from the Select Field drop-down list, and enables it only when the chart is of the 100% Stacked Line 2-D type. Select it if you want to display data in the condition expression in percent.
* **Advanced**
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**  
    Select to open the [Edit Conditions dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058702-Edit-Conditions-Dialog-Box#ChartLine) to create a condition and define the node properties for values which meet the condition.
  + ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404856829719/btn_edit.gif)**Edit button**  
    Select to open the [Edit Node Style dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059862-Node-Pattern-List-Dialog-Box) for editing the node properties if you select the default condition "Other"; or open the [Edit Conditions dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058702-Edit-Conditions-Dialog-Box#ChartNode) to edit the condition and the node properties for values which meet the condition, if you select a user-defined condition.
  + ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**  
    Select to delete the specified user-defined condition.
  + **Condition**  
    The column shows the default condition "Other" and the expressions of the conditions that you define in the Edit Condition dialog box.
  + **Color**  
    The column shows the colors that you specify to apply to the values which meet the conditions. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
  + **Transparency**  
    The column shows the transparency of the colors that you specify for the conditions.

    ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) For a user-defined condition, Designer disables the Color and Transparency columns for it, if you edit the condition using Imported Condition. You can only use the Edit Condition dialog box to edit the two properties for the condition.
  + **Style**  
    The column shows the node styles that you specify for the conditions.
  + **Label**  
    Select to modify the expression of the specified condition, which Designer displays as its legend entry label.
  + **Value**  
    The option indicates that Designer displays data in the condition expressions as value. You cannot change it.
  + **Percent**  
    Designer does not support the option when you edit conditions in the advanced mode.

**Use Multiple Colors with Condition**

Designer does not support this fill type on line charts.

**Apply Color to Line**

Select to apply the color pattern that you specify on the nodes apply to the corresponding lines.

**Sample**

The box displays a preview sample of your selection.

## Border Tab

Designer displays the Border tab if the chart is a 3-D line chart. You can use it to specify the properties for the border of the 3-D lines.

![Format Line - Border](https://devnet.logianalytics.com/hc/article_attachments/4404848548119/fmtln_brdr.gif)

**Show Border**

Select to show the border of the 3-D lines. Designer enables the other border properties in this tab after you select the option.

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

Use this tab to specify the properties of the data labels on the lines.

![Format Line - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4404856945303/fmtln_data.gif)

**Static Data Label**

You can specify the properties of the static data labels on the lines in this box. Designer disables the options in the box for a 3-D line chart.

* **Show Static Data Label**  
  Select to show the static data labels. Designer enables the other static data label properties after you select this option.
* **Position**  
  Select the position of the static data labels on the lines.
  + **auto fit**  
    Select to display the static data labels automatically.
  + **top center**  
    Select to display the static data labels on the top center of the line nodes.
  + **top left**  
    Select to display the static data labels on the top left of the line nodes.
  + **top right**  
    Select to display the static data labels on the top right of the line nodes.
  + **bottom left**  
    Select to display the static data labels at the bottom left of the line nodes.
  + **bottom center**  
    Select to display the static data labels at the bottom center of the line nodes.
  + **bottom right**  
    Select to display the static data labels at the bottom right of the line nodes.
* **Data Label Type**  
  Select in which way to display the values in the static data labels.
  + **value**  
    Select to show the value for each line node.
  + **percent**  
     Select to show the percentage of each line node to the total.
  + **value and percent**  
    Select to show the value and the percentage for each line node.
* **Auto Scale in Number**  
  Specify whether to automatically scale the Number values in the static data labels which fall into the following two ranges:
  + When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
  + When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.

  By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property [on the chart in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#AutoScale) for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.
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

Use this tab to specify the properties for the hint of the lines.

![Format Line - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404848548631/fmtln_hint.gif)

**Show Category and Series**

Select to include the category and series values in the hint.

**Auto Scale in Number**

Specify whether to automatically scale the Number values in the hint which fall into the following two ranges:

* When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.

By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property [on the chart in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#AutoScale) for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.

## Behaviors Tab

Designer displays the Behaviors tab only when the line chart is in a library component. You can use it to specify web behaviors to the lines.

![Format Line - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404856945559/fmtln_bhvr.gif)

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010059222-Format-Legend-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010059262-Format-Paper-Dialog-Box)
