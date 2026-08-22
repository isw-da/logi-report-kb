---
title: "Format Activity Gauge Dialog Box"
id: 5735509116055
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735509116055-Format-Activity-Gauge-Dialog-Box
updated_at: 2022-11-02T04:37:30Z
---

# Format Activity Gauge Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735523419543-Find-Replace-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735565974167-Format-Area-Dialog-Box)

# Format Activity Gauge Dialog Box

You can use the Format Activity Gauge dialog box to [format an activity gauge chart](https://devnet.logianalytics.com/hc/en-us/articles/5735520602391-Formatting-Gauge-Chart#Activity). This topic describes the options in the dialog box.

Designer displays the Format Activity Gauge dialog box when you right-click any range in a circle in an activity gauge chart and select Format Solid Gauge from the shortcut menu, or double-click any circle range in the activity gauge.

The dialog box contains the following tabs (Designer displays the Behaviors tab only when the chart is in a library component):

* [Circular Graph Tab](#Circular)
* [Pointer Tab](#Pointer)
* [Target Tab](#Target)
* [Frame Tab](#Frame)
* [Range Color Tab](#Range)
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

## Circular Graph Tab

Use this tab to specify properties of the circles in the activity gauge.

![Format Activity Gauge dialog box - Circular Graph](https://devnet.logianalytics.com/hc/article_attachments/9898481320215/fmtactvtygauge_crculr.gif)

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

You can specify the fill pattern of the circles in this box.

* **Color**  
  Specify the color of the circles. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette), or type the hexadecimal value of a color (for example, 0xff0000) in the text box.
* **Color List**  
  Select to open the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522093463-Color-List-Dialog-Box) to modify the color pattern for each circle.
* **Transparency**  
  Specify the transparency of the circles.
* **Self Settings**  
  Select to apply the color pattern to the circles themselves only. When this option is cleared, Designer synchronizes the color pattern that you specify here with the [Pattern List](https://devnet.logianalytics.com/hc/en-us/articles/5735545992599-Chart-Properties#Pattern) property of the chart in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart.
* **Background**  
  Specify the background color of the circles.
  + **Auto**  
    Select to apply the color that is lighter than the color of the circles as the background color automatically. Clear it if you want to edit the background color by yourself.
* **Use Range Color**  
  Select to use the colors that you define for the ranges in the [Range Color](#Range) tab for the circles.

**Value**

You can specify the values to display in the chart in this box.

* **Minimum**  
  Specify the minimum value to display in the chart. You can select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/9898457345303/btn_fmla.gif) to [use a formula to control the value](https://devnet.logianalytics.com/hc/en-us/articles/5735545031703-Using-Formulas-to-Control-Object-Properties).
* **Maximum**  
  Specify the maximum value to display in the chart. You can select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/9898457345303/btn_fmla.gif) to use a formula to control the value.

**Sample**

This box displays a preview sample based on your selections.

## Pointer Tab

Use this tab to specify properties for the pointers in the activity gauge.

![Format Activity Gauge dialog box - Pointer](https://devnet.logianalytics.com/hc/article_attachments/9898464273559/fmtactvtygauge_pnt.gif)

**Pointer Value**

You can specify properties of the pointer values in this box.

* **Show Pointer Value**  
  Select to show the pointer values.
* **Position**  
  Select the position of the values relative to the pointers: top, bottom, center, or customized. If you select "customized", you can customize the position by dragging any pointer value in the design area.

## Target Tab

Use this tab to specify properties of the target in the activity gauge.

![Format Activity Gauge dialog box - Target](https://devnet.logianalytics.com/hc/article_attachments/9898464291095/fmtactvtygauge_tgt.gif)

**Use Target Value**

Select to use target value for the activity gauge.

* **Target Value**  
  Specify the target value. You can select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/9898457345303/btn_fmla.gif) to use a formula to control the value.

**Target Value**

You can specify properties of the target value in this box.

* **Show Target Value**  
  Select to show the target value on the activity gauge.
* **Position**  
  Select the position of the target value relative to the circles: top, bottom, center, or customized. If you select "customized", you can customize the position by dragging the target value in the design area.

## Frame Tab

Use this tab to specify properties for the frame of the activity gauge chart.

![Format Activity Gauge dialog box - Frame](https://devnet.logianalytics.com/hc/article_attachments/9898481338519/fmtactvtygauge_frm.gif)

**Size**

You can specify the frame size in this box.

* **Frame Size**  
  Specify the size of the frame.

**Fill**

You can specify the fill pattern of the frame in this box.

* **Fill**  
  Specify the fill pattern of the frame. To edit the fill pattern, select the color indicator and specify a color or effect using the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette). You can also type the hexadecimal value of a color (for example, 0xff0000) in the text box.
* **Transparency**  
  Specify the transparency of the fill pattern.

**Border**

You can specify properties for the border of the frame in this box.

* **Border Type**  
  Select the type of the border.
  + **none**  
    Select if you do not want to show the border.
  + **raised**  
    Select to show 3-D border that appears as if it is raised off the page.
  + **recess**  
    Select to show 3-D border that appears as if it is pressed into the page.
  + **shadow**  
    Select to show two shadowed borders, beneath and to the right of the object.
  + **solid**  
    Select to use single-line border.
* **Color**  
  Specify the color of the border. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette), or type the hexadecimal value of a color (for example, 0xff0000) in the text box.
* **Line Style**  
  Select the line style of the border.
* **Transparency**  
  Specify the transparency of the border.
* **Thickness**  
  Specify the width of the border, in pixels.
* **End Caps**  
  Select the ending style of the border.
  + **butt**  
    Select to end unclosed subpaths and dash segments with no added decoration.
  + **round**  
    Select to end unclosed subpaths and dash segments with a round decoration that has a radius equal to half of the line width.
  + **square**  
    Select to end unclosed subpaths and dash segments with a square projection that extends beyond the end of the segment to a distance equal to half of the line width.
* **Line Joint**  
  Select the joint style of the border.
  + **miter**  
    Select to join path segments by extending their outside edges until they meet.
  + **round**  
    Select to join path segments by rounding off the corner at a radius of half the line width.
  + **bevel**  
    Select to join path segments by connecting the outer corners of their wide outlines with a straight segment.
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

You can specify options for the gauge group names in this box.

* **Show Gauge Group Name**   
  Select to show names for the circles in the activity gauge, which are values of the field on the category axis. If the activity gauge contains no category field, the group name shows "Report" by default.
* **Position**  
  Select the position of the names relative to the circles: top, bottom, center, or customized. If you select "customized", you can customize the position by dragging any name in the design area.

**Sample**

This box displays a preview sample based on your selections.

## Range Color Tab

Use this tab to specify the value ranges for the activity gauge and the color and name of each range.

![Format Activity Gauge dialog box - Range Color](https://devnet.logianalytics.com/hc/article_attachments/9898464302615/fmtactvtygauge_rgclr.gif)

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif)**Add button**

Select to add a new range.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif)**Remove button**

Select to delete the specified range.

**Minimum**

This column shows the minimum values that you specify for the ranges.

**Maximum**

This column shows the maximum values that you specify for the ranges.

**Color**

This column shows the colors that you specify for the ranges. To edit the color, select in the cell and customize the color in the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette).

**Name**

This column shows the names that you specify for the ranges.

**Others**

You can specify the properties for values that do not fall into any of the ranges you define in this box.

* **Name**  
  Specify the name for the values.
* **Color**  
  Specify the color for the values. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette), or type the hexadecimal value of a color (for example, 0xff0000) in the text box.

## Hint Tab

Use this tab to specify properties for the hint of the activity gauge.

![Format Activity Gauge dialog box - Hint](https://devnet.logianalytics.com/hc/article_attachments/9898481368983/fmtactvtygauge_hint.gif)

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

Designer displays the Behaviors tab only when the activity gauge chart is in a library component. You can use it to specify web behaviors to the activity gauge.

![Format Activity Gauge dialog box - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/9898481376919/fmtactvtygauge_bhvr.gif)

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735523419543-Find-Replace-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735565974167-Format-Area-Dialog-Box)
