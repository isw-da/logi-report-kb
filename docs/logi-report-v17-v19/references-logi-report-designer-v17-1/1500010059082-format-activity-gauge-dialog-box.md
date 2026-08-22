---
title: "Format Activity Gauge Dialog Box"
id: 1500010059082
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010059082-Format-Activity-Gauge-Dialog-Box
updated_at: 2021-07-23T19:15:26Z
---

# Format Activity Gauge Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010096821-Flash-Parameter-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010096941-Format-Area-Dialog-Box)

# Format Activity Gauge Dialog Box

You can use the Format Activity Gauge dialog box to [format an activity gauge chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010056922-Formatting-the-Gauge-in-a-Gauge-Chart#Activity). This topic describes the options in the dialog box.

Designer displays the Format Activity Gauge dialog box when you right-click any range in a circle in an activity gauge chart and select Format Solid Gauge from the shortcut menu, or double-click any circle range in the activity gauge.

The dialog box contains the following tabs (Designer displays the Behaviors tab only when the chart is in a library component):

* [Circular Graph Tab](#Circular)
* [Pointer Tab](#Pointer)
* [Target Tab](#Target)
* [Frame Tab](#Frame)
* [Range Color Tab](#Range)
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

## Circular Graph Tab

Use this tab to specify the properties for the circles in the activity gauge.

![Format Activity Gauge dialog box - Circular Graph](https://devnet.logianalytics.com/hc/article_attachments/4404848574615/fmtactvtygauge_crculr.gif)

**Size**

You can specify the size of the circles in this box.

* **Hole Size**  
  Specify the relative size of a circle in a percentage of total circle size.
* **Circular Gap**  
  Specify the distance between the circles.
* **Start Style**  
  Select the style for the start graph of the circles: square, round, or long round.
* **End Style**  
  Select the style for the end graph of the circles: square, round, or long round.
* **Start Mark**  
  Select the mark for the start graph of the circles.
* **Stop Mark**  
  Select the mark for the stop graph of the circles.

**Fill**

You can specify the color of the circles in this box.

* **Color**  
  Specify the color of the circles.
* **Color List**  
  Select to open the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500010058302-Color-List-Dialog-Box) dialog to modify the color pattern for each circle.
* **Transparency**  
  Specify the transparency for color of the circles.
* **Self Settings**  
  Select to apply the color pattern to the circles themselves only. If you do not select the option, Designer synchronizes the color settings you define here to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#Pattern) on the chart object in the Report Inspector, which the data markers of other subtypes can also apply if the chart is a combo chart.
* **Background**  
  Specify the background color of the circles.
  + **Auto**  
    Select to apply the color that is lighter than the color of the circles as the background color automatically. Clear the option if you want to edit the background color by yourself.
* **Use Range Color**  
  Select to use the colors that you define for the ranges in the [Range Color](#Range) tab for the circles.

**Value**

You can specify the values to display in the chart in this box.

* **Minimum**  
  Specify the minimum value to display in the chart. You can select the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif) to [use a formula to control the value](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties).
* **Maximum**  
  Specify the maximum value to display in the chart. You can select the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif) to [use a formula to control the value](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties).

**Sample**

The box displays a preview sample of your selection.

## Pointer Tab

Use this tab to specify properties for the pointers in the activity gauge.

![Format Activity Gauge dialog box - Pointer](https://devnet.logianalytics.com/hc/article_attachments/4404856969751/fmtactvtygauge_pnt.gif)

**Pointer Value**

You can specify the properties of the pointer values in this box.

* **Show Pointer Value**  
  Select to show the pointer values.
* **Position**  
  Select the position of the values relative to the pointers: top, bottom, center, or customized. If you select "customized", you can customize the position by dragging any pointer value in the design area.

## Target Tab

Use this tab to specify properties of the target in the activity gauge.

![Format Activity Gauge dialog box - Target](https://devnet.logianalytics.com/hc/article_attachments/4404848574999/fmtactvtygauge_tgt.gif)

**Use Target Value**

Select to use target value for the activity gauge.

* **Target Value**  
  Specify the target value. You can select the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif) to [use a formula to control the value](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties).

**Target Value**

You can specify the properties of the target value in this box.

* **Show Target Value**  
  Select to show the target value on the activity gauge.
* **Position**  
  Select the position of the target value relative to the circles: top, bottom, center, or customized. If you select "customized", you can customize the position by dragging the target value in the design area.

## Frame Tab

Use this tab to specify properties for the frame of the activity gauge chart.

![Format Activity Gauge dialog box - Frame](https://devnet.logianalytics.com/hc/article_attachments/4404848575511/fmtactvtygauge_frm.gif)

**Size**

You can specify the size properties of the frame in this box.

* **Frame Size**  
  Specify the size of the frame.

**Fill**

You can specify the color and transparency of the frame in this box.

* **Fill**  
  Specify the color to fill the frame. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Transparency**  
  Specify the transparency of the color to fill the frame.

**Border**

You can specify the properties for the border of the frame in this box.

* **Border Type**  
  Select the type of the border.
  + **none**  
    Select if you do not want to show the border.
  + **raised**  
    Select to show 3-D border which appears as if it is raised off the page.
  + **recess**  
    Select to show 3-D border which appears as if it is pressed into the page.
  + **shadow**  
    Select to show two shadowed borders, beneath and to the right of the object.
  + **solid**  
    Select to use single-line border.
* **Color**  
  Specify the color of the border. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Line Style**  
  Select the line style of the border.
* **Transparency**  
  Specify the transparency for color of the border.
* **Thickness**  
  Specify the thickness of the border, in pixels.
* **End Caps**  
  Select the ending style of the border line.
  + **butt**  
    Select to end unclosed sub paths and dash segments with no added decoration.
  + **round**  
    Select to end unclosed sub paths and dash segments with a round decoration that has a radius equal to half of the width of the pen.
  + **square**  
    Select to end unclosed sub paths and dash segments with a square projection that extends beyond the end of the segment to a distance equal to half of the line width.
* **Line Joint**  
  Select the joint style of the border line.
  + **miter**  
    Select to join path segments by extending their outside edges until they meet.
  + **round**  
    Select to join path segments by rounding off the corner at a radius of half the line width.
  + **bevel**  
    Select to join path segments by connecting the outer corners of their wide outlines with a straight segment.
  + **joint round**  
    Select to join path segments by rounding off the corner at the specified radius.
* **Path**  
  Specify the fill pattern of the border.
  + **Outline Path**  
    Select to use outline path for the border.
  + **Fill Path**  
    Select to use whole path for the border.
* **Dash**  
  Specify the dash size of the border if you select a dash line style for the border.
  + **Auto Adjust Dash**  
    Select to adjust the dash size automatically.
  + **Fixed Dash Size**  
    Select to use fixed dash size.

**Gauge Group Name**

You can specify the properties for the gauge group names in this box.

* **Show Gauge Group Name**   
  Select to show names for the circles in the activity gauge, which are values of the field on the category axis. If the activity gauge contains no category field, the group name shows "Report" by default.
* **Position**  
  Select the position of the names relative to the circles: top, bottom, center, or customized. If you select "customized", you can customize the position by dragging any name in the design area.

**Sample**

The box displays a preview sample of your selection.

## Range Color Tab

Use this tab to specify the value ranges for the activity gauge and the color and name of each range.

![Format Activity Gauge dialog box - Range Color](https://devnet.logianalytics.com/hc/article_attachments/4404856970007/fmtactvtygauge_rgclr.gif)

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**

Select to add a new range.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**

Select to delete the specified range.

**Minimum**

The column shows the minimum values that you specify for the ranges.

**Maximum**

The column shows the maximum values that you specify for the ranges.

**Color**

The column shows the colors that you specify for the ranges. To edit the color, select in the cell and customize the color in the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette).

**Name**

The column shows the names that you specify for the ranges.

**Others**

You can specify the properties for values that do not fall into any of the ranges you define in this box.

* **Name**  
  Specify the name for the values.
* **Color**  
  Specify the color for the values. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.

## Hint

Use this tab to specify the properties for the hint of the activity gauge.

![Format Activity Gauge dialog box - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404848575767/fmtactvtygauge_hint.gif)

**Show Category and Series**

Select to include the category and series values in the hint.

**Auto Scale in Number**

Specify whether to automatically scale the Number values in the hint which fall into the following two ranges:

* When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.

By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property [on the chart in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#AutoScale) for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.

* When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.

By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property [on the chart in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#AutoScale) for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.

## Behaviors Tab

Designer displays the Behaviors tab only when the activity gauge chart is in a library component. You can use it to specify web behaviors to the activity gauge.

![Format Activity Gauge dialog box - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404856970519/fmtactvtygauge_bhvr.gif)

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010096821-Flash-Parameter-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010096941-Format-Area-Dialog-Box)
