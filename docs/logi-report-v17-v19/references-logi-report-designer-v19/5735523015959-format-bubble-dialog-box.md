---
title: "Format Bubble Dialog Box"
id: 5735523015959
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735523015959-Format-Bubble-Dialog-Box
updated_at: 2022-11-02T08:24:41Z
---

# Format Bubble Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/7933644552087/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735514080535-Format-Bar-Gauge-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/7933656663191/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735514090903-Format-Bubble-Gauge-Dialog-Box)

# Format Bubble Dialog Box

You can use the Format Bubble dialog box to [format the bubbles in a bubble chart](https://devnet.logianalytics.com/hc/en-us/articles/5735563915671-Formatting-the-Bubbles-in-a-Bubble-Chart). This topic describes the options in the dialog box.

Designer displays the Format Bubble dialog box when you right-click a bubble in a bubble chart and select Format Bubble from the shortcut menu, or double-click any bubble in the bubble chart.

This dialog box contains the following tabs:

* [General Tab](#General)
* [Fill Tab](#Fill)
* [Border Tab](#Border)
* [Data Label Tab](#Data)
* [Hint Tab](#Hint)

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

Use this tab to specify general properties of the bubbles.

![Format Bubble - General](https://devnet.logianalytics.com/hc/article_attachments/7933700772887/fmtbubl_gnrl.gif)

**Use 3-D Visual Effect**

Select to apply a three-dimensional visual effect to the bubbles.

**Cut Bubble Based on XY Area**

Select to cut the bubbles when they are beyond the chart wall (the area formed by the X axis and Y axis). However, Designer still cuts the bubbles if they go beyond the chart paper.

## Fill Tab

Use this tab to specify the fill pattern of the bubbles.

![Format Bubble - Fill](https://devnet.logianalytics.com/hc/article_attachments/7933727507351/fmtbubl_fill.gif)

**Color**

Specify the color for all bubbles if the chart has no series field, or the color of the bubbles in the current data series if the chart has series field. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette), or type the hexadecimal value of a color (for example, 0xff0000) in the text box.

**Transparency**

Specify the transparency of the bubbles.

**Self Settings**

Select to apply the color pattern to the bubbles themselves only. When this option is cleared, Designer synchronizes the color pattern that you specify here with the [Pattern List](https://devnet.logianalytics.com/hc/en-us/articles/5735545992599-Chart-Properties#Pattern) property of the chart in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart.

**Color List**

Select to open the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522093463-Color-List-Dialog-Box) to modify the color pattern for bubbles in the same data series respectively.

**Sample**

This box displays a preview sample based on your selections.

## Border Tab

Use this tab to specify properties for the border of the bubbles.

![Format Bubble - Border](https://devnet.logianalytics.com/hc/article_attachments/7933754470679/fmtbubl_border.gif)

**Show Border**

Select to show the border of the bubbles. Designer enables the other border properties in this tab after you select this option.

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

Designer does not support displaying data labels in bubble charts, so you can skip this tab.

![Format Bubble - Data Label](https://devnet.logianalytics.com/hc/article_attachments/7933724928919/fmtbubl_data.gif)

## Hint Tab

Use this tab to specify properties for the hint of the bubbles.

![Format Bubble - Hint](https://devnet.logianalytics.com/hc/article_attachments/7933727558679/fmtbubl_hint.gif)

**Show Category and Series**

Select to include the category and series values in the hint.

**Auto Scale in Number**

Specify whether to automatically scale the Number values in the hint that fall into the two ranges:

* When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.

By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property [on the chart in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/5735545992599-Chart-Properties#AutoScale) for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.

**Customize Chart Value Names**

Select to customize the names of the fields on the value axis which you want to display in the hint. By default, Designer applies the display names of the fields in the hint to label the values which may be not intuitive to users. You can select the option and select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/7933688270615/btn_ellipsis2.gif) to customize the names in the [Customize Chart Value Names dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565355927-Customize-Chart-Value-Names-Dialog-Box) to help users better understand the values.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/7933644552087/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735514080535-Format-Bar-Gauge-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/7933656663191/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735514090903-Format-Bubble-Gauge-Dialog-Box)
