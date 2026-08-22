---
title: "Format Indicator Dialog Box"
id: 1500010097081
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010097081-Format-Indicator-Dialog-Box
updated_at: 2021-07-23T19:15:29Z
---

# Format Indicator Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010097061-Format-Gauge-Label-Dialog-Box)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010097101-Format-KPI-Label-Dialog-Box)

# Format Indicator Dialog Box

You can use the Format Indicator dialog box to [format the indicators in an indicator chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010056942-Formatting-the-Indicators-in-an-Indicator-Chart). This topic describes the options in the dialog box.

Designer displays the Format Indicator dialog box when you right-click an indicator in an indicator chart and select Format Indicator from the shortcut menu, or double-click any indicator in an indicator chart.

The dialog box contains the following tabs (Designer displays the Behaviors tab only when the chart is in a library component):

* [General Tab](#General)
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

## General Tab

Use this tab to specify the general properties of the indicators.

![Format Indicator - General](https://devnet.logianalytics.com/hc/article_attachments/4404856950423/fmtindctr_gnrl.gif)

**Style**

You can specify the style of the indicators in this box.

* **Single**  
  Select to use an indicator to show each value.
* **Multiple**  
  Select to use multiple indicators to show each value.

**Option**

You can specify the options of the indicators in this box.

* **Left Margin**  
  Specify the gap between the left labels and the left indicators, in pixels.
* **Top Margin**  
  Specify the gap between the top labels and the top indicators, in pixels.
* **Range Radius**  
  Specify the relative size of an indicator in a percentage of the total indicator size.
* **Style**  
  Select the shape of the indicator graph.
* **Fill Type**  
  Designer enables this option when the indicator chart displays numeric values. You can use it to specify how to fill the indicators.
  + **all**  
    Select to fill the whole indicator.
  + **base on max value**  
    Select to fill the portion of the indicators calculated based on the maximum value of the chart.

**Border**

You can specify the properties for the border of the indicators in this box.

* **Show Border**  
  Select to show the border of the indicators. Designer enables the other border properties in this box after you select the option.
* **Line Style**  
  Select the line style of the border.
* **Thickness**  
  Specify the thickness of the border, in pixels.
* **Color**  
  Specify the color of the border. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Transparency**  
  Specify the transparency of the color.

**Value**

Designer enables the options in this box when the indicator chart displays numeric values. You can use the options to specify the minimum and maximum values to display in the chart.

* **Minimum**  
  Specify the minimum value to display in the chart.
* **Maximum**  
  Specify the maximum value to display in the chart.

**Value Label**

You can specify the properties for the value labels of the indicators in this box.

* **Show Value**  
  Select to show the value labels for the indicators.
* **Position**  
  Select the position of the value labels relative to the indicators: top, bottom, or center.
* **Auto Scale in Number**  
  Specify whether to automatically scale the Number values in the labels which fall into the following two ranges:
  + When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
  + When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.

  By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property [on the chart in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#AutoScale) for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.

**Sample**

The box displays a preview sample of your selection.

## Frame Tab

Use this tab to specify the properties for the frame of the indicator chart.

![Format Indicator - Frame](https://devnet.logianalytics.com/hc/article_attachments/4404856950935/fmtindctr_frm.gif)

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

**Category Label**

You can specify the properties for the category labels of the indicators in this box.

* **Show Category Label**  
  Select to show the category labels for the indicators, which display the category value each indicator represents.
* **Position**  
  Select the position of the category labels relative to the indicators: top, bottom, or center.

**Sample**

The box displays a preview sample of your selection.

## Range Color Tab

Use this tab to specify different colors or images to fill the indicators. Designer displays different options in the tab based on the different data types of the values in the indicator chart: [Boolean](#Boolean) and [Numeric/String](#Numeric).

### For Boolean Values

![Format Indicator - Range Color for Boolean Values](https://devnet.logianalytics.com/hc/article_attachments/4404856951191/fmtindctr_range_boln.gif)

**Show Image**

Select to use images instead of colors to represent the two values in the indicator chart. When you select the option, Designer ignores the colors that you specify in the Color column for the ranges.

**Value**

The column shows the two values of the indicator chart, True and False. You cannot change the values.

**Color**

The column shows the colors that you specify for the two values in the indicator chart. Select the cell to customize the color in the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette).

**Image**

The column shows the images that you specify to represent the two values of the indicator chart. Select the cell and select the ellipsis button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404848397591/btn_ellipsis.gif) in the cell to select the image.

**Name**

The column shows the names that you specify to display for the two values of the indicator chart.

### For Numeric/String Values

![Format Indicator - Range Color for String/Numeric Values](https://devnet.logianalytics.com/hc/article_attachments/4404856951575/fmtindctr_range_num.gif)

**Show Image**

Select to use images instead of colors to represent the values in different ranges. When you select the option, Designer ignores the colors that you specify in the Color column for the ranges.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**

Select to add a new value range.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**

Select to delete the specified value range.

**Minimum**

The column shows the minimum values that you specify for the ranges.

**Maximum**

The column shows the maximum values that you specify for the ranges.

**Color**

The column shows the colors that you specify for the ranges. Select the color cell to customize the color in the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette).

**Image**

The column shows the images that you specify to represent the values in the ranges. Select the cell and select the ellipsis button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404848397591/btn_ellipsis.gif) in the cell to select the image.

**Name**

The column shows the names that you specify for the ranges.

**Others**

You can specify the properties for values that do not fall into any of the ranges that you define in this box.

* **Name**  
  Specify the name for the values.
* **Color**  
  Specify the color for the values. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Image**  
  Specify the image to represent the values. Select ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404848397591/btn_ellipsis.gif) to select the image.

## Hint Tab

Use this tab to specify the properties for the hint of the indicators.

![Format Indicator - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404848553623/fmtindctr_hint.gif)

**Show Category and Series**

Select to include the category and series values in the hint.

**Auto Scale in Number**

Specify whether to automatically scale the Number values in the hint which fall into the following two ranges:

* When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.

By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property [on the chart in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#AutoScale) for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.

## Behaviors Tab

Designer displays the Behaviors tab only when the indicator chart is in a library component. You can use it to specify web behaviors to the indicators.

![Format Indicator - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404848553879/fmtindctr_bhvr.gif)

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010097061-Format-Gauge-Label-Dialog-Box)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010097101-Format-KPI-Label-Dialog-Box)
