---
title: "Formatting the Gauge in a Gauge Chart"
id: 4405664379031
section: "Working with Components in Reports - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664379031-Formatting-the-Gauge-in-a-Gauge-Chart
updated_at: 2022-01-27T20:34:25Z
---

# Formatting the Gauge in a Gauge Chart

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664384279-Formatting-the-Rectangles-and-Rectangle-Titles-in-a-Heat-Map)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664385175-Formatting-the-Surface-in-a-Surface-Chart)

# Formatting the Gauge in a Gauge Chart

Designer provides different format options for different gauge subtypes: Gauge Solid 2-D, Gauge Dial 2-D, Gauge Bar 2-D, Gauge Activity 2-D, and Gauge Bubble 2-D. This topic describes how you can format the different gauges and the labels in a gauge chart.

This topic contains the following sections:

* [Formatting a Solid Gauge](#Solid)
* [Formatting a Dial Gauge](#Dial)
* [Formatting a Bar Gauge](#Bar)
* [Formatting an Activity Gauge](#Activity)
* [Formatting a Bubble Gauge](#Bubble)
* [Formatting the Pointer/Gauge/Target Labels](#Label)

## Formatting a Solid Gauge

1. Right-click any range in an arc in the solid gauge and select **Format Solid Gauge** on the shortcut menu, or double-click any arc range in the solid gauge. Designer displays the [Format Solid Gauge dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661595031-Format-Solid-Gauge-Dialog-Box).

   ![Format Solid Gauge dialog box - Circular Graph](https://devnet.logianalytics.com/hc/article_attachments/4420556258327/fmtsldgauge_crculr.gif)
2. In the **Circular Graph** tab, specify properties for the arcs in the solid gauge.

   In the **Size** box, set the angle of the arcs (you can select the angle from the drop-down list or select **Customized** to open the [Customize Gauge Angle dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664448919-Customize-Gauge-Angle-Dialog-Box) to specify the start angle and stop angle), the width of the arcs, the hole size of the arcs (meaning the relative size of an arc in a percentage of the total arc size), and the styles of the start graph and end graph of the arcs.

   In the **Fill** box,

   * To apply the colors that you [define for the ranges](#SolidRangeColor) to the arcs, select **Use Range Color**, then in the **Background** text box, set the background color of the arcs (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box).
   * To specify colors for the arcs separately, leave Use Range Color cleared. Make a choice for the **Self Settings** checkbox: when Self Settings is cleared (the default behavior), Designer synchronizes the color pattern that you specify here with the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/4405664650263-Chart-Properties#Pattern) on the chart object in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart; when you select Self Settings, it indicates that the color pattern is private to the current data markers themselves (the arcs in this case), which Designer remembers and applies to the data markers of a new type automatically if later you change the type of the chart. Then, specify the color and the transparency of the color to fill the ranges in the arcs that are in the same data series as the arc range you have selected on to open the Format Solid Gauge dialog box, or select **Color List** to specify the color pattern for arc ranges in the same data series respectively in the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661476887-Color-List-Dialog-Box). Set the background color of the arcs in the Background text box. The colors defined for the ranges also apply to the corresponding pointers if you specify to [display value pointers](#PointerColor) in the solid gauge in the Pointer tab.

   In the **Border** box, set the line style, thickness, color, color transparency, ending style, and line joint style for border of the arcs.
3. In the **Axis** tab, specify properties of the axis in the solid gauge.
   1. In the **Axis** subtab, set properties of the axis.

      ![Format Solid Gauge dialog box - Axis - Axis1](https://devnet.logianalytics.com/hc/article_attachments/4420550995095/fmtsldgauge_axis_axis1.gif)

      Select **Show Axis** to display axis in the solid gauge. Only when you select the option, it is meaningful to set the other options for the axis in this tab.

      In the **Type** box, specify the position of the axis, which can be inside, outside, or in the center of the arcs.

      In the **Option** box, specify the minimum and maximum values to display on the axis, or [use a formula to control the values](https://devnet.logianalytics.com/hc/en-us/articles/4405664601367-Using-Formulas-to-Control-Object-Properties). By default, Designer calculates the minimum and maximum values based on the real values in the chart using certain algorithm, which is the meaning of the default value "Auto"; if you set either value to 0, Designer applies it as "Auto".

      In the **Line** box, specify the color and transparency of the color for the axis, or select **Use Range Color** to apply the color that you [define for the ranges](#SolidRangeColor) to the axis. Specify the style and thickness of the axis.

      In the **Gap** box, specify the gap between the axis and the arc if the axis shows inside or outside the arcs.
   2. In the **Tick Mark** subtab, specify properties of the tick marks on the axis.

      ![Format Solid Gauge dialog box - Axis - Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4420542217879/fmtsldgauge_axis_tkmk.gif)

      To display tick marks on the axis, select how to show it in the **Type** box: inside, outside, or in the center of the axis.

      In the **Major Tick Mark Line** and **Minor Tick Mark Line** boxes, specify the distance between two adjacent tick marks on the axis, how many tick marks to display on the axis, and the color, style, color transparency, thickness, and the length of the tick marks respectively. Select **Correlate with Axis** if you want to apply the [line properties](#SolidAxisLine) that you define for the axis in the Axis subtab to the tick mark lines.
   3. In the **Label** subtab, specify properties for the data labels on the axis.

      ![Format Solid Gauge dialog box - Axis - Label](https://devnet.logianalytics.com/hc/article_attachments/4420542218263/fmtsldgauge_axis_lbl.gif)

      In the **Type** box, specify the type of the data labels.

      * **None**  
        Select if you do not want to display tick mark labels on the axis. It is meaningless to specify all the other tick mark label properties if you select this type.
      * **Normal**  
        Select it and the data labels display as you specify: in the **Label Every N Major Tick Marks** combo box, set the frequency at which to label the major tick marks; select **Auto** if you want to show all major tick mark on the axis, or **Fixed** to show only the specified number of major tick mark labels.
      * **Range Value**  
        Select to show the [range values](#SolidRangeColor) that you define in the Range Color tab in the data labels.
      * **Min and Max Values**  
        Select to show the [minimum value and maximum value](#SolidAxisValue) that you define in the Axis subtab in the data labels.

      In the **Gap** box, specify the distance between the data labels and the axis in pixels. Select **Best Effect** if you want to adjust the position of the labels automatically so as to place them in the best way; while, Designer hides some labels when they overlap for the best effect.

      In the **Font** box, format the font of the data labels, including the font face, size, color, color transparency, rotation angle, and shearing angle.

      In the **Effects** box, specify the font effects of the data labels, including the style, strikeout, underline, and so on.
   4. In the **Format** subtab, specify the data format of the data labels on the axis.

      ![Format Solid Gauge dialog box - Axis - Format](https://devnet.logianalytics.com/hc/article_attachments/4420556259351/fmtsldgauge_axis_fmt.gif)

      Select a category from the **Category** box, then select a format from the **Format** box and select **Add** to add it to the **Stack** box (for more information about each format, [select here](https://devnet.logianalytics.com/hc/en-us/articles/4405664452759-Data-Format-Dialog-Box#DataFormat)). If the formats that Designer provides in the Format box cannot meet your requirement, you can define the format in the **Properties** text box and add it as the format of the selected category. You can add more than one format, but for each category, only one format is allowed. If you do not need a format anymore, select it in the Stack box and select **Remove** to clear it.

      Set the **Auto Scale in Number** option to specify whether to automatically scale the big and small Number values.
4. In the **Pointer** tab, specify properties for the pointers of the arcs in the solid gauge.

   ![Format Solid Gauge dialog box - Pointer](https://devnet.logianalytics.com/hc/article_attachments/4420542218903/fmtsldgauge_pnt.gif)

   In the **Pointer Style** box,

   * To use arrow as the pointer style, select **Arrow**, then select the arrow style and specify the width and height of the arrow. You can also select **Style List** to specify the style for pointers in the same data series respectively in the [Style List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664583063-Style-List-Dialog-Box).
   * To use mark as the pointer style, select **Mark**, then select the mark style, specify the width and height of the mark, the position of the pointers relative to the arcs, and the distance between the pointers and the arcs in pixels. You can also select **Style List** to specify the style for pointers in the same data series respectively in the [Style List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664583063-Style-List-Dialog-Box).

   In the **Pointer Color** box,

   * To apply the colors that you [define for the ranges](#SolidRangeColor) to the pointers, select **Use Range Color**.
   * To specify colors for the pointers separately, leave Use Range Color cleared. Make a choice for the **Self Settings** checkbox: when Self Settings is cleared (the default behavior), Designer synchronizes the color pattern that you specify here with the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/4405664650263-Chart-Properties#Pattern) on the chart object in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart; when you select Self Settings, it indicates that the color pattern is private to the current data markers themselves (the pointers in this case), which Designer remembers and applies to the data markers of a new type automatically if later you change the type of the chart. Then, specify the color and the transparency of the color to fill the pointers in the same data series as the arc range you have selected on to open the Format Solid Gauge dialog box, or select **Color List** to specify the color pattern for pointers in the same data series respectively in the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661476887-Color-List-Dialog-Box). The colors defined for the pointers also apply to the corresponding [ranges in the arcs](#ArcColor).

   In the **Pointer Value** box, specify whether to show values for the pointers and the position of the values relative to the pointers. If you select **customized** from the **Position** drop-down list, you can customize the position of the pointer values by dragging any pointer value in the design area.

   In the **Pointer Border** box, select **Show Pointer Border** if you want to show the border of the pointers, then set properties of the border including line style, thickness, color, and color transparency.
5. In the **Target** tab, specify properties of the target in the solid gauge.

   ![Format Solid Gauge dialog box - Target](https://devnet.logianalytics.com/hc/article_attachments/4420542219159/fmtsldgauge_tgt.gif)

   Select **Use Target Value** if you want to use target value for the solid gauge, then specify the target value in the **Target Value** text box or [use a formula to control the value](https://devnet.logianalytics.com/hc/en-us/articles/4405664601367-Using-Formulas-to-Control-Object-Properties).

   In the **Pointer Style** box, select the style of the target pointer from the **Target Pointer** drop-down list. Specify the width and height of the target pointer, the position of the target pointer relative to the arcs, and the distance between the target pointer and the arcs.

   In the **Pointer Color** box, specify the color and transparency of the color for the target pointer.

   In the **Target Value** box, specify whether to show the target value on the solid gauge and the position of the target value relative to the arcs. If you select **customized** from the **Position** drop-down list, you can customize the position of the target value by dragging it in the design area.
6. In the **Frame** tab, specify properties for the frame of the solid gauge.

   ![Format Solid Gauge dialog box - Frame](https://devnet.logianalytics.com/hc/article_attachments/4420556259863/fmtsldgauge_frm.gif)

   In the **Size** box, specify the size of the frame.

   In the **Fill** box, specify the color and the transparency of the color to fill the frame.

   In the **Border** box, specify properties for the border of the frame, including the type, color, line style, color transparency, thickness, ending style, line joint style, fill pattern, and dash size.

   In the **Gauge Group Name** box, specify whether to show names for the arcs in the solid gauge which are values of the field on the category axis, and the position of the names relative to the arcs. If the solid gauge contains no category field, the group name shows "Report" by default.
7. In the **Range Color** tab, specify the value ranges for the solid gauge and the color and name of each range.

   ![Format Solid Gauge dialog box - Range Color](https://devnet.logianalytics.com/hc/article_attachments/4420542219415/fmtsldgauge_rgclr.gif)

   By default, Designer provides three predefined value ranges and calculates the minimum and maximum values for each range using certain algorithm according to the minimum and maximum values that you [specify on the axis](#SolidAxisValue) in the Axis subtab, which is the meaning of the default value "Auto". You can select in the corresponding columns to edit the minimum and maximum values, colors from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette), and names for the ranges according to your own requirements. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif) to add and define more ranges; to delete a range, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420542080407/btn_trashcan.gif).

   In the **Others** box, specify the name and color for the values that do not fall into any of the ranges you define.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) If you only edit the minimum and maximum values for one range but keep the default "Auto" value for all the rest ranges, Designer regards that there is only one value range in the solid gauge; therefore, you should either keep the default "Auto" value for all the ranges to let Designer calculates them for you, or edit them all to apply your own values.
8. In the **Hint** tab, specify options of the chart hint (the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/4405661845015-Chart-Paper-Properties#ShowTips) property of the chart paper in the Report Inspector should be "true" if you want to show the hint): specify whether to include the category and series values in the hint, whether to scale big and small numbers, and whether to use customized names for the fields on the value axis in the hint, and customize the names as you want. A hint displays the value a range/pointer of an arc in the solid gauge represents when you hover over the range/pointer in Designer view mode, in HTML output, or at runtime.

   ![Format Solid Gauge dialog box - Hint](https://devnet.logianalytics.com/hc/article_attachments/4420550997271/fmtsldgauge_hint.gif)
9. For a solid gauge chart in a library component, you can define web behaviors on it in the **Behaviors** tab. A web behavior contains a trigger event and a web action to be triggered when the event occurs on the arcs or pointers in the solid gauge at runtime. You can add as many web behaviors to the solid gauge as you need.

   ![Format Solid Gauge dialog box - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4420542219799/fmtsldgauge_bhvr.gif)

   To define the web behavior, select a [trigger event](https://devnet.logianalytics.com/hc/en-us/articles/4405661415703-Using-Basic-Web-Controls-in-a-Report#Event) from the drop-down list in the **Events** column, then select in the **Actions** column and select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420550841879/btn_ellipsis1.gif). In the Web Action List dialog box, bind a web action [the same as you do to web controls](https://devnet.logianalytics.com/hc/en-us/articles/4405661415703-Using-Basic-Web-Controls-in-a-Report#Action) in the library component. The web actions you can bind include Filter, Sort, Parameter, Property, and SendMessage.

   You can select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif) to add and define more web behaviors; to delete a web behavior, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420542080407/btn_trashcan.gif). You can also select a web behavior and select **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420542078103/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420542078359/btn_mvdwn.gif) to adjust the order of the behaviors, then at runtime, when an event that is bound with more than one action happens, JDashboard triggers the upper action first.
10. Select **OK** to accept the changes and close the dialog box.

## Formatting a Dial Gauge

1. Right-click any pointer in a dial of the dial gauge and select **Format Dial Gauge** on the shortcut menu, or double-click any pointer in the dial gauge. Designer displays the [Format Dial Gauge dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664489111-Format-Dial-Gauge-Dialog-Box).

   ![Format Dial Gauge dialog box - Circular Graph](https://devnet.logianalytics.com/hc/article_attachments/4420542136855/fmtdlgauge_crculr.gif)
2. In the **Circular Graph** tab, specify properties for the dials in the dial gauge.

   In the **Size** box, set the angle of the dials (you can select the angle from the drop-down list or select **Customized** to open the [Customize Gauge Angle dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664448919-Customize-Gauge-Angle-Dialog-Box) to specify the start angle and stop angle), the width of the dials, the relative size of a dial, and the styles of the start graph and end graph of the dials.

   In the **Border** box, set the line style, thickness, color, color transparency, ending style, and line joint style for border of the dials.

   Select **Show Range Name** if you want to show [the names of the ranges](#DialRangeColor) that you define in the Range Color tab in the dials, then specify the font formats and effects of the range names in the **Font** and **Effects** boxes.
3. In the **Axis** tab, specify properties of the axis in the dial gauge.
   1. In the **Axis** subtab, set properties of the axis.

      ![Format Dial Gauge dialog box - Axis - Axis1](https://devnet.logianalytics.com/hc/article_attachments/4420542137239/fmtdlgauge_axis_axis1.gif)

      Select **Show Axis** to display axis in the dial gauge. Only when you select the option, it is meaningful to set the other options for the axis in this tab.

      In the **Type** box, specify the position of the axis, which can be inside, outside, or in the center of the dials.

      In the **Option** box, specify the minimum and maximum values to display on the axis, or [use a formula to control the values](https://devnet.logianalytics.com/hc/en-us/articles/4405664601367-Using-Formulas-to-Control-Object-Properties). By default, Designer calculates the minimum and maximum values based on the real values in the chart using certain algorithm, which is the meaning of the default value "Auto"; if you set either value to 0, Designer applies it as "Auto".

      In the **Line** box, specify the color and transparency of the color for the axis, or select **Use Range Color** to apply the color that you [define for the ranges](#DialRangeColor) to the axis. Specify the style and thickness of the axis.

      In the **Gap** box, specify the gap between the axis and the dials if the axis shows inside or outside the dials.
   2. In the **Tick Mark** subtab, specify properties of the tick marks on the axis.

      ![Format Dial Gauge dialog box - Axis - Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4420550908055/fmtdlgauge_axis_tkmk.gif)

      To display tick marks on the axis, select how to show it in the **Type** box: inside, outside, or in the center of the axis.

      In the **Major Tick Mark Line** and **Minor Tick Mark Line** boxes, specify the distance between two adjacent tick marks on the axis, how many tick marks to display on the axis, and the color, style, color transparency, thickness, and length of the tick marks respectively. Select **Correlate with Axis** if you want to apply the [line properties](#DialAxisLine) that you define for the axis in the Axis subtab to the tick mark lines.
   3. In the **Label** subtab, specify properties for the data labels on the axis.

      ![Format Dial Gauge dialog box - Axis - Label](https://devnet.logianalytics.com/hc/article_attachments/4420556178455/fmtdlgauge_axis_lbl.gif)

      In the **Type** box, specify the type of the data labels.

      * **None**  
        Select if you do not want to display tick mark labels on the axis. It is meaningless to specify all the other tick mark label properties if you select this type.
      * **Normal**  
        Select it and the data labels display as you specify: in the **Label Every N Major Tick Marks** combo box, set the frequency at which to label the major tick marks; select **Auto** if you want to show all major tick mark on the axis, or **Fixed** to show only the specified number of major tick mark labels.
      * **Range Value**  
        Select to show the [range values](#DialRangeColor) that you define in the Range Color tab in the data labels.
      * **Min and Max Values**  
        Select to show the [minimum value and maximum value](#DialAxisValue) that you define in the Axis subtab in the data labels.

      In the **Gap** box, specify the distance between the data labels and the axis in pixels. Select **Best Effect** if you want to adjust the position of the labels automatically so as to place them in the best way; while, Designer hides some labels when they overlap for the best effect.

      In the **Font** box, format the font of the data labels, including the font face, size, color, color transparency, rotation angle, and shearing angle.

      In the **Effects** box, specify the font effects of the data labels, including the style, strikeout, underline, and so on.
   4. In the **Format** subtab, specify the data format of the data labels on the axis.

      ![Format Dial Gauge dialog box - Axis - Format](https://devnet.logianalytics.com/hc/article_attachments/4420542137751/fmtdlgauge_axis_fmt.gif)

      Select a category from the **Category** box, then select a format from the **Format** box and select **Add** to add it to the **Stack** box (for more information about each format, [select here](https://devnet.logianalytics.com/hc/en-us/articles/4405664452759-Data-Format-Dialog-Box#DataFormat)). If the formats that Designer provides in the Format box cannot meet your requirement, you can define the format in the **Properties** text box and add it as the format of the selected category. You can add more than one format, but for each category, only one format is allowed. If you do not need a format anymore, select it in the Stack box and select **Remove** to clear it.

      Set the **Auto Scale in Number** option to specify whether to automatically scale the big and small Number values.
4. In the **Pointer** tab, specify properties for the pointers of the dials in the dial gauge.

   ![Format Dial Gauge dialog box - Pointer](https://devnet.logianalytics.com/hc/article_attachments/4420556178967/fmtdlgauge_pnt.gif)

   In the **Pointer Style** box,

   * To use arrow as the pointer style, select **Arrow**, then select the arrow style and specify the width and height of the arrow. You can also select **Style List** to specify the style for pointers in the same data series respectively in the [Style List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664583063-Style-List-Dialog-Box).
   * To use mark as the pointer style, select **Mark**, then select the mark style, specify the width and height of the mark, the position of the pointers relative to the dials, and the distance between the pointers and the dials in pixels. You can also select **Style List** to specify the style for pointers in the same data series respectively in the [Style List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664583063-Style-List-Dialog-Box).

   In the **Pointer Color** box,

   * To apply the colors that you [define for the ranges](#DialRangeColor) to the pointers, select **Use Range Color**.
   * To specify color for the pointers separately, leave Use Range Color cleared. Make a choice for the **Self Settings** checkbox: when Self Settings is cleared (the default behavior), Designer synchronizes the color pattern that you specify here with the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/4405664650263-Chart-Properties#Pattern) on the chart object in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart; when you select Self Settings, it indicates that the color pattern is private to the current data markers themselves (the pointers in this case), which Designer remembers and applies to the data markers of a new type automatically if later you change the type of the chart. Then, specify the color and the transparency of the color to fill the pointers in the same data series as the pointer you have selected on to open the Format Dial Gauge dialog box, or select **Color List** to specify the color pattern for pointers in the same data series respectively in the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661476887-Color-List-Dialog-Box).

   In the **Pointer Value** box, specify whether to show values for the pointers and the position of the values relative to the pointers. If you select **customized** from the **Position** drop-down list, you can customize the position of the pointer values by dragging any pointer value in the design area.

   In the **Pointer Border** box, select **Show Pointer Border** if you want to show the border of the pointers, then set properties of the border including line style, thickness, color, and color transparency.
5. In the **Target** tab, specify properties of the target in the dial gauge.

   ![Format Dial Gauge dialog box - Target](https://devnet.logianalytics.com/hc/article_attachments/4420542138135/fmtdlgauge_tgt.gif)

   Select **Use Target Value** if you want to use target value for the dial gauge, then specify the target value in the **Target Value** text box or [use a formula to control the value](https://devnet.logianalytics.com/hc/en-us/articles/4405664601367-Using-Formulas-to-Control-Object-Properties).

   In the **Pointer Style** box, select the style of the target pointer from the **Target Pointer** drop-down list. Specify the width and height of the target pointer, the position of the target pointer relative to the dials, and the distance between the target pointer and the dials.

   In the **Pointer Color** box, specify the color and transparency of the color for the target pointer.

   In the **Target Value** box, specify whether to show the target value on the dial gauge and the position of the target value relative to the dials. If you select **customized** from the **Position** drop-down list, you can customize the position of the target value by dragging it in the design area.
6. In the **Frame** tab, specify properties for the frame of the dial gauge.

   ![Format Dial Gauge dialog box - Frame](https://devnet.logianalytics.com/hc/article_attachments/4420542138391/fmtdlgauge_frm.gif)

   In the **Size** box, specify the size of the frame.

   In the **Fill** box, specify the color and the transparency of the color to fill the frame.

   In the **Border** box, specify properties for the border of the frame, including the type, color, line style, color transparency, thickness, ending style, line joint style, fill pattern, and dash size.

   In the **Gauge Group Name** box, box, specify whether to show names for the dials in the dial gauge which are values of the field on the category axis, and the position of the names relative to the dials. If the dial gauge contains no category field, the group name shows "Report" by default.
7. In the **Range Color** tab, specify the value ranges for the dial gauge and the color and name of each range.

   ![Format Dial Gauge dialog box - Range Color](https://devnet.logianalytics.com/hc/article_attachments/4420556179479/fmtdlgauge_rgclr.gif)

   By default, Designer provides three predefined value ranges and calculates the minimum and maximum values for each range using certain algorithm according to the minimum and maximum values that you [specify on the axis](#DialAxisValue) in the Axis subtab, which is the meaning of the default value "Auto". You can select in the corresponding columns to edit the minimum and maximum values, colors from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette), and names for the ranges according to your own requirements. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif) to add and define more ranges; to delete a range, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420542080407/btn_trashcan.gif).

   In the **Others** box, specify the name and color for the values that do not fall into any of the ranges you define.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) If you only edit the minimum and maximum values for one range but keep the default "Auto" value for all the rest ranges, Designer regards that there is only one value range in the dial gauge; therefore, you should either keep the default "Auto" value for all the ranges to let Designer calculates them for you, or edit them all to apply your own values.
8. In the **Hint** tab, specify options of the chart hint (the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/4405661845015-Chart-Paper-Properties#ShowTips) property of the chart paper in the Report Inspector should be "true" if you want to show the hint): specify whether to include the category and series values in the hint, whether to scale big and small numbers, and whether to use customized names for the fields on the value axis in the hint, and customize the names as you want. A hint displays the value a pointer in the dial gauge represents when you point to the dial pointer in Designer view mode, in HTML output, or at runtime.

   ![Format Dial Gauge dialog box - Hint](https://devnet.logianalytics.com/hc/article_attachments/4420542138647/fmtdlgauge_hint.gif)
9. For a dial gauge chart in a library component, you can define web behaviors on it in the **Behaviors** tab. A web behavior contains a trigger event and a web action to be triggered when the event occurs on the dial pointers at runtime. You can add as many web behaviors to the dial gauge as you need.

   ![Format Dial Gauge dialog box - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4420550909207/fmtdlgauge_bhvr.gif)

   To define the web behavior, select a [trigger event](https://devnet.logianalytics.com/hc/en-us/articles/4405661415703-Using-Basic-Web-Controls-in-a-Report#Event) from the drop-down list in the **Events** column, then select in the **Actions** column and select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420550841879/btn_ellipsis1.gif). In the Web Action List dialog box, bind a web action [the same as you do to web controls](https://devnet.logianalytics.com/hc/en-us/articles/4405661415703-Using-Basic-Web-Controls-in-a-Report#Action) in the library component. The web actions you can bind include Filter, Sort, Parameter, Property, and SendMessage.

   You can select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif) to add and define more web behaviors; to delete a web behavior, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420542080407/btn_trashcan.gif). You can also select a web behavior and select **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420542078103/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420542078359/btn_mvdwn.gif) to adjust the order of the behaviors, then at runtime, when an event that is bound with more than one action happens, JDashboard triggers the upper action first.
10. Select **OK** to accept the changes and close the dialog box.

## Formatting a Bar Gauge

1. Right-click any range in a bar in the bar gauge and select **Format Bar Gauge** from the shortcut menu, or double-click any pointer in the bar gauge. Designer displays the [Format Bar Gauge dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661560727-Format-Bar-Gauge-Dialog-Box).

   ![Format Bar Gauge dialog box - Staff Graph](https://devnet.logianalytics.com/hc/article_attachments/4420550912791/fmtbargauge_stfgraph.gif)
2. In the **Staff Graph** tab, specify properties for the bars in the bar gauge.

   In the **Bar** box, specify the layout of the bars, vertical or horizontal, the thickness of the bars, and the style of the start graph and end graph of the bars.

   In the **Range Border** box, set the color, line style, color transparency, and thickness of the bar border (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box).

   Select **Show Range Name** if you want to show [the names of the ranges](#BarRangeColor) that you define in the Range Color tab in the bars, then specify the font formats and effects of the range names in the **Font** and **Effect** boxes.
3. In the **Axis** tab, specify properties of the axis in the bar gauge.
   1. In the **Axis** subtab, set properties of the axis.

      ![Format Bar Gauge dialog box - Axis - Axis1](https://devnet.logianalytics.com/hc/article_attachments/4420556182935/fmtbargauge_axis_axis.gif)

      Select **Show Axis** to display axis in the bar gauge. Only when you select the option, it is meaningful to set the other options for the axis in this tab.

      In the **Type** box, specify the position of the axis, which can be on the top or bottom of the bar, or in the center of the bar.

      In the **Option** box, specify the minimum and maximum values to display on the axis, or [use a formula to control the values](https://devnet.logianalytics.com/hc/en-us/articles/4405664601367-Using-Formulas-to-Control-Object-Properties). By default, Designer calculates the minimum and maximum values based on the real values in the chart using certain algorithm, which is the meaning of the default value "Auto"; if you set either value to 0, Designer applies it as "Auto".

      In the **Line** box, specify the color and transparency of the color for the axis, or select **Use Range Color** to apply the color that you [define for the ranges](#BarRangeColor) to the axis. Specify the style and thickness of the axis.

      In the **Gap** box, specify the gap between the axis and the bars if the axis shows inside or outside the bars.
   2. In the **Tick Mark** subtab, specify properties of the tick marks on the axis.

      ![Format Bar Gauge dialog box - Axis - Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4420542143767/fmtbargauge_axis_tkmk.gif)

      To display tick marks on the axis, select how to show it in the **Type** box: on the top or bottom of the axis if you specify to display the bars horizontally in the [Staff Graph tab](#BarLayout), or on the left or right of the axis if the bars display vertically, or in the center of the axis.

      In the **Major Tick Mark Line** and **Minor Tick Mark Line** boxes, specify the distance between two adjacent tick marks on the axis, how many tick marks to display on the axis, and the color, style, color transparency, thickness, and length of the tick marks respectively. Select **Correlate with Axis** if you want to apply the [line properties](#BarAxisLine) that you define for the axis in the Axis subtab to the tick mark lines.
   3. In the **Label** subtab, specify properties for the data labels on the axis.

      ![Format Bar Gauge dialog box - Axis - Label](https://devnet.logianalytics.com/hc/article_attachments/4420542144023/fmtbargauge_axis_lbl.gif)

      In the **Type** box, specify the type of the data labels.

      * **None**  
        Select if you do not want to display tick mark labels on the axis. It is meaningless to specify all the other tick mark label properties if you select this type.
      * **Normal**  
        Select it and the data labels display as you specify: in the **Label Every N Major Tick Marks** combo box, set the frequency at which to label the major tick marks; select **Auto** if you want to show all major tick mark on the axis, or **Fixed** to show only the specified number of major tick mark labels.
      * **Range Value**  
        Select to show the [range values](#BarRangeColor) that you define in the Range Color tab in the data labels.
      * **Min and Max Values**  
        Select to show the [minimum value and maximum value](#BarAxisValue) that you define in the Axis subtab in the data labels.

      In the **Gap** box, specify the distance between the data labels and the axis in pixels. Select **Best Effect** if you want to adjust the position of the labels automatically so as to place them in the best way; while, Designer hides some labels when they overlap for the best effect.

      In the **Font** box, format the font of the data labels, including the font face, size, color, color transparency, rotation angle, and shearing angle.

      In the **Effects** box, specify the font effects of the data labels, including the style, strikeout, underline, and so on.
   4. In the **Format** subtab, specify the data format of the data labels on the axis.

      ![Format Bar Gauge dialog box - Axis - Format](https://devnet.logianalytics.com/hc/article_attachments/4420550913047/fmtbargauge_axis_fmt.gif)

      Select a category from the **Category** box, then select a format from the **Format** box and select **Add** to add it to the **Stack** box (for more information about each format, [select here](https://devnet.logianalytics.com/hc/en-us/articles/4405664452759-Data-Format-Dialog-Box#DataFormat)). If the formats that Designer provides in the Format box cannot meet your requirement, you can define the format in the **Properties** text box and add it as the format of the selected category. You can add more than one format, but for each category, only one format is allowed. If you do not need a format anymore, select it in the Stack box and select **Remove** to clear it.

      Set the **Auto Scale in Number** option to specify whether to automatically scale the big and small Number values.
4. In the **Pointer** tab, specify properties of the pointers in the bar gauge.

   ![Format Bar Gauge dialog box - Pointer](https://devnet.logianalytics.com/hc/article_attachments/4420556183575/fmtbargauge_pnt.gif)

   Specify the way to show the pointer: pointer or color bar.

   If you select **Use Pointer**, in the **Pointer Style** box, specify the style of the value pointers, the width and height of the pointers, the position of the pointers relative to the bars, and the distance between the pointers and the bars in pixels. You can select **Style List** to specify the style for pointers in the same data series respectively in the [Style List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664583063-Style-List-Dialog-Box).

   In the **Pointer Color** box,

   * To apply the colors that you [define for the ranges](#BarRangeColor) to the pointers, select **Use Range Color**.
   * To specify color for the pointers separately, leave Use Range Color cleared. Make a choice for the **Self Settings** checkbox: when Self Settings is cleared (the default behavior), Designer synchronizes the color pattern that you specify here with the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/4405664650263-Chart-Properties#Pattern) on the chart object in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart; when you select Self Settings, it indicates that the color pattern is private to the current data markers themselves (the pointers in this case), which Designer remembers and applies to the data markers of a new type automatically if later you change the type of the chart. Then, specify the color and the transparency of the color to fill the pointers in the same data series as the pointer you have selected on to open the Format Bar Gauge dialog box, or select **Color List** to specify the color pattern for pointers in the same data series respectively in the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661476887-Color-List-Dialog-Box).

   In the **Pointer Value** box, specify whether to show values for the pointers and the position of the values relative to the pointers. If you select **customized** from the **Position** drop-down list, you can customize the position of the pointer values by dragging any pointer value in the design area.

   In the **Pointer Border** box, select **Show Pointer Border** if you want to show the border of the pointers, then set properties of the border including line style, thickness, color, and color transparency.
5. In the **Target** tab, specify properties of the target in the bar gauge.

   ![Format Bar Gauge dialog box - Target](https://devnet.logianalytics.com/hc/article_attachments/4420550913303/fmtbargauge_tgt.gif)

   Select **Use Target Value** if you want to use target value for the bar gauge, then specify the target value in the **Target Value** text box or [use a formula to control the value](https://devnet.logianalytics.com/hc/en-us/articles/4405664601367-Using-Formulas-to-Control-Object-Properties).

   In the **Pointer Style** box, select the style of the target pointer from the **Target Pointer** drop-down list. Specify the width and height of the target pointer, the position of the target pointer relative to the bars, and the distance between the target pointer and the bars.

   In the **Pointer Color** box, specify the color and transparency of the color for the target pointer.

   In the **Target Value** box, specify whether to show the target value on the bar gauge and the position of the target value relative to the bars. If you select **customized** from the Position drop-down list, you can customize the position of the target value by dragging it in the design area.
6. In the **Frame** tab, specify properties for the frame of the bar gauge.

   ![Format Bar Gauge dialog box - Frame](https://devnet.logianalytics.com/hc/article_attachments/4420542144791/fmtbargauge_frm.gif)

   In the **Size** box, specify the size of the frame.

   In the **Fill** box, specify the color and the transparency of the color to fill the frame.

   In the **Border** box, specify properties for the border of the frame, including the type, color, line style, color transparency, thickness, ending style, line joint style, fill pattern, and dash size.

   In the **Gauge Group Name** box, specify whether to show names for the bars in the bar gauge which are values of the field on the category axis, and the position of the names relative to the bars. If the bar gauge contains no category field, the group name shows "Report" by default.
7. In the **Range Color** tab, specify the value ranges for the bar gauge and the color and name of each range.

   ![Format Bar Gauge dialog box - Rane Color](https://devnet.logianalytics.com/hc/article_attachments/4420542145047/fmtbargauge_rgclr.gif)

   By default, Designer provides three predefined value ranges and calculates the minimum and maximum values for each range using certain algorithm according to the minimum and maximum values that you [specify on the axis](#BarAxisValue) in the Axis subtab, which is the meaning of the default value "Auto". You can select in the corresponding columns to edit the minimum and maximum values, colors from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette), and names for the ranges according to your own requirements. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif) to add and define more ranges; to delete a range, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420542080407/btn_trashcan.gif).

   In the **Others** box, specify the name and color for the values that do not fall into any of the ranges you define.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) If you only edit the minimum and maximum values for one range but keep the default "Auto" value for all the rest ranges, Designer regards that there is only one value range in the bar gauge; therefore, you should either keep the default "Auto" value for all the ranges to let Designer calculates them for you, or edit them all to apply your own values.
8. In the **Hint** tab, specify options of the chart hint (the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/4405661845015-Chart-Paper-Properties#ShowTips) property of the chart paper in the Report Inspector should be "true" if you want to show the hint): specify whether to include the category and series values in the hint, whether to scale big and small numbers, and whether to use customized names for the fields on the value axis in the hint, and customize the names as you want. A hint displays the value a pointer in the bar gauge represents when you hover over the pointer in Designer view mode, in HTML output, or at runtime.

   ![Format Bar Gauge dialog box - Hint](https://devnet.logianalytics.com/hc/article_attachments/4420556184087/fmtbargauge_hint.gif)
9. For a bar gauge chart in a library component, you can define web behaviors on it in the **Behaviors** tab. A web behavior contains a trigger event and a web action to be triggered when the event occurs on the pointers of the bar gauge at runtime. You can add as many web behaviors to the bar gauge as you need.

   ![Format Bar Gauge dialog box - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4420550914583/fmtbargauge_bhvr.gif)

   To define the web behavior, select a [trigger event](https://devnet.logianalytics.com/hc/en-us/articles/4405661415703-Using-Basic-Web-Controls-in-a-Report#Event) from the drop-down list in the **Events** column, then select in the **Actions** column and select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420550841879/btn_ellipsis1.gif). In the Web Action List dialog box, bind a web action [the same as you do to web controls](https://devnet.logianalytics.com/hc/en-us/articles/4405661415703-Using-Basic-Web-Controls-in-a-Report#Action) in the library component. The web actions you can bind include Filter, Sort, Parameter, Property, and SendMessage.

   You can select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif) to add and define more web behaviors; to delete a web behavior, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420542080407/btn_trashcan.gif). You can also select a web behavior and select **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420542078103/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420542078359/btn_mvdwn.gif) to adjust the order of the behaviors, then at runtime, when an event that is bound with more than one action happens, JDashboard triggers the upper action first.
10. Select **OK** to accept the changes and close the dialog box.

## Formatting an Activity Gauge

1. Right-click any range in a circle in the activity gauge and select **Format Solid Gauge** from the shortcut menu, or double-click any circle range in the activity gauge. Designer displays the [Format Activity Gauge dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661557143-Format-Activity-Gauge-Dialog-Box).

   ![Format Activity Gauge dialog box - Circular Graph](https://devnet.logianalytics.com/hc/article_attachments/4420542146967/fmtactvtygauge_crculr.gif)
2. In the **Circular Graph** tab, specify properties for the circles in the activity gauge.

   In the **Size** box, specify the hole size of the circles (meaning the relative size of a circle in a percentage of the total circle size), the distance between the circles, and the styles and marks for the start graph and end graph of the circles.

   In the **Fill** box,

   * To apply the [colors that you define for the ranges](#ActivityRangeColor) to the circles, select **Use Range Color**.
   * To specify color for the circles separately, leave Use Range Color cleared. Make a choice for the **Self Settings** checkbox: when Self Settings is cleared (the default behavior), Designer synchronizes the color pattern that you specify here with the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/4405664650263-Chart-Properties#Pattern) on the chart object in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart; when you select Self Settings, it indicates that the color pattern is private to the current data markers themselves (the circles in this case), which Designer remembers and applies to the data markers of a new type automatically if later you change the type of the chart. Then, specify the color and the transparency of the color to fill the circles in the same data series as the circle you have selected on to open the Format Activity Gauge dialog box, or select **Color List** to specify the color pattern for circles in the same data series respectively in the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661476887-Color-List-Dialog-Box).

   By default, Designer applies the color that is lighter than the color of the circles as the background color of the circles automatically. If you want to customize the background color by yourself, clear **Auto**, then in the **Background** text box, set the background color of the circles (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box).

   In the **Value** box, specify the minimum and maximum values to display in the activity chart, or [use a formula to control the values](https://devnet.logianalytics.com/hc/en-us/articles/4405664601367-Using-Formulas-to-Control-Object-Properties). By default, Designer calculates the minimum and maximum values based on the real values in the chart using certain algorithm, which is the meaning of the default value "Auto"; if you set either value to 0, Designer applies it as "Auto".
3. In the **Pointer** tab, specify whether to show the pointer values and the position of the values relative to the pointers. If you select **customized** from the **Position** drop-down list, you can customize the position of the pointer values by dragging any pointer value in the design area.

   ![Format Activity Gauge dialog box - Pointer](https://devnet.logianalytics.com/hc/article_attachments/4420556188951/fmtactvtygauge_pnt.gif)
4. In the **Target** tab, select **Use Target Value** if you want to use target value for the activity gauge, then specify the target value in the **Target Value** text box or [use a formula to control the value](https://devnet.logianalytics.com/hc/en-us/articles/4405664601367-Using-Formulas-to-Control-Object-Properties). In the **Target Value** box, specify whether to show the target value on the activity gauge and the position of the target value relative to the circles. If you select **customized** from the Position drop-down list, you can customize the position of the target value by dragging it in the design area.

   ![Format Activity Gauge dialog box - Target](https://devnet.logianalytics.com/hc/article_attachments/4420550917143/fmtactvtygauge_tgt.gif)
5. In the **Frame** tab, specify properties for the frame of the activity gauge.

   ![Format Activity Gauge dialog box - Frame](https://devnet.logianalytics.com/hc/article_attachments/4420550917399/fmtactvtygauge_frm.gif)

   In the **Size** box, specify the size of the frame.

   In the **Fill** box, specify the color and the transparency of the color to fill the frame.

   In the **Border** box, specify properties for the border of the frame, including the type, color, line style, color transparency, thickness, ending style, line joint style, fill pattern, and dash size.

   In the **Gauge Group Name** box, specify whether to show names for the circles in the activity gauge which are values of the field on the category axis, and the position of the names relative to the circles. If the activity gauge contains no category field, the group name shows "Report" by default.
6. In the **Range Color** tab, specify the value ranges for the activity gauge and the color and name of each range.

   ![Format Activity Gauge dialog box - Range Color](https://devnet.logianalytics.com/hc/article_attachments/4420556191511/fmtactvtygauge_rgclr.gif)

   By default, Designer provides three predefined value ranges and calculates the minimum and maximum values for each range using certain algorithm according to the minimum and maximum values that you [specify for the activity chart](#ActivityAxisValue) in the Circular Graph tab, which is the meaning of the default value "Auto". You can select in the corresponding columns to edit the minimum and maximum values, colors from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette), and names for the ranges according to your own requirements. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif) to add and define more ranges; to delete a range, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420542080407/btn_trashcan.gif).

   In the **Others** box, specify the name and color for the values that do not fall into any of the ranges you define.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) If you only edit the minimum and maximum values for one range but keep the default "Auto" value for all the rest ranges, Designer regards that there is only one value range in the activity gauge; therefore, you should either keep the default "Auto" value for all the ranges to let Designer calculates them for you, or edit them all to apply your own values.
7. In the **Hint** tab, specify options of the chart hint (the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/4405661845015-Chart-Paper-Properties#ShowTips) property of the chart paper in the Report Inspector should be "true" if you want to show the hint): specify whether to include the category and series values in the hint, whether to scale big and small numbers, and whether to use customized names for the fields on the value axis in the hint, and customize the names as you want. A hint displays the value a data range in a circle of the activity gauge represents when you point to the range in Designer view mode, in HTML output, or at runtime.

   ![Format Activity Gauge dialog box - Hint](https://devnet.logianalytics.com/hc/article_attachments/4420542149143/fmtactvtygauge_hint.gif)
8. For an activity gauge chart in a library component, you can define web behaviors on it in the **Behaviors** tab. A web behavior contains a trigger event and a web action to be triggered when the event occurs on the data ranges of the circles in the activity gauge at runtime. You can add as many web behaviors to the activity gauge as you need.

   ![Format Activity Gauge dialog box - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4420542150039/fmtactvtygauge_bhvr.gif)

   To define the web behavior, select a [trigger event](https://devnet.logianalytics.com/hc/en-us/articles/4405661415703-Using-Basic-Web-Controls-in-a-Report#Event) from the drop-down list in the **Events** column, then select in the **Actions** column and select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420550841879/btn_ellipsis1.gif). In the Web Action List dialog box, bind a web action [the same as you do to web controls](https://devnet.logianalytics.com/hc/en-us/articles/4405661415703-Using-Basic-Web-Controls-in-a-Report#Action) in the library component. The web actions you can bind include Filter, Sort, Parameter, Property, and SendMessage.

   You can select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif) to add and define more web behaviors; to delete a web behavior, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420542080407/btn_trashcan.gif). You can also select a web behavior and select **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420542078103/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420542078359/btn_mvdwn.gif) to adjust the order of the behaviors, then at runtime, when an event that is bound with more than one action happens, JDashboard triggers the upper action first.
9. Select **OK** to accept the changes and close the dialog box.

## Formatting a Bubble Gauge

1. Right-click any bubble in the bubble gauge and select **Format Bubble Gauge** on the shortcut menu, or double-click any bubble in the bubble gauge. Designer displays the [Format Bubble Gauge dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661562391-Format-Bubble-Gauge-Dialog-Box).

   ![Format Bubble Gauge dialog box - Staff Graph](https://devnet.logianalytics.com/hc/article_attachments/4420550997783/fmtbublgauge_stfgraph.gif)
2. In the **Staff Graph** tab, set properties for the bubbles in the chart.

   In the **Bubbles** box, specify the gap between the left/top labels and left/top bubbles, the radius of the bubbles (meaning the relative size of a bubble in a percentage of the total bubble size), and whether to draw horizontal/vertical grids.

   In the **Border** box, select **Show Border** if you want to show the border of the bubbles, then set properties of the border including the line style, thickness, color, and color transparency.

   In the **Value** box, specify the minimum and maximum values to display in the bubble chart, or [use a formula to control the values](https://devnet.logianalytics.com/hc/en-us/articles/4405664601367-Using-Formulas-to-Control-Object-Properties). By default, Designer calculates the minimum and maximum values based on the real values in the chart using certain algorithm, which is the meaning of the default value "Auto"; if you set either value to 0, Designer applies it as "Auto".
3. In the **Frame** tab, specify properties for the frame of the bubble gauge.

   ![Format Bubble Gauge dialog box - Frame](https://devnet.logianalytics.com/hc/article_attachments/4420556260247/fmtbublgauge_frm.gif)

   In the **Size** box, specify the size of the frame.

   In the **Fill** box, specify the color and the transparency of the color to fill the frame.

   In the **Border** box, specify properties for the border of the frame, including the type, color, line style, color transparency, thickness, ending style, line joint style, fill pattern, and dash size.

   In the **Gauge Group Name** box, specify whether to show names for the bubbles in the bubble gauge which are values of the field on the category axis, and the position of the names relative to the bubbles. If the bubble gauge contains no category field, the group name shows "Report" by default.
4. In the **Range Color** tab, specify the value ranges for the bubble gauge and the color and name of each range.

   ![Format Bubble Gauge dialog box - Range Color](https://devnet.logianalytics.com/hc/article_attachments/4420550998295/fmtbublgauge_rgclr.gif)

   By default, Designer provides three predefined value ranges and calculates the minimum and maximum values for each range using certain algorithm according to the minimum and maximum values that you [specify for the bubble chart](#BubbleAxisValue) in the Staff Graph tab, which is the meaning of the default value "Auto". You can select in the corresponding columns to edit the minimum and maximum values, colors from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette), and names for the ranges according to your own requirements. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif) to add and define more ranges; to delete a range, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420542080407/btn_trashcan.gif).

   In the **Others** box, specify the name and color for the values that do not fall into any of the ranges you define.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) If you only edit the minimum and maximum values for one range but keep the default "Auto" value for all the rest ranges, Designer regards that there is only one value range in the bubble gauge; therefore, you should either keep the default "Auto" value for all the ranges to let Designer calculates them for you, or edit them all to apply your own values.
5. In the **Hint** tab, specify options of the chart hint (the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/4405661845015-Chart-Paper-Properties#ShowTips) property of the chart paper in the Report Inspector should be "true" if you want to show the hint): specify whether to include the category and series values in the hint, whether to scale big and small numbers, and whether to use customized names for the fields on the value axis in the hint, and customize the names as you want. A hint displays the value a bubble in the bubble gauge represents when you point to the bubble in Designer view mode, in HTML output, or at runtime.

   ![Format Bubble Gauge dialog box - Hint](https://devnet.logianalytics.com/hc/article_attachments/4420550998551/fmtbublgauge_hint.gif)
6. For a bubble gauge chart in a library component, you can define web behaviors on it in the **Behaviors** tab. A web behavior contains a trigger event and a web action to be triggered when the event occurs on the bubbles of the bubble gauge at runtime. You can add as many web behaviors to the bubble gauge as you need.

   ![Format Bubble Gauge dialog box - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4420556260503/fmtbublgauge_bhvr.gif)

   To define the web behavior, select a [trigger event](https://devnet.logianalytics.com/hc/en-us/articles/4405661415703-Using-Basic-Web-Controls-in-a-Report#Event) from the drop-down list in the **Events** column, then select in the **Actions** column and select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420550841879/btn_ellipsis1.gif). In the Web Action List dialog box, bind a web action [the same as you do to web controls](https://devnet.logianalytics.com/hc/en-us/articles/4405661415703-Using-Basic-Web-Controls-in-a-Report#Action) in the library component. The web actions you can bind include Filter, Sort, Parameter, Property, and SendMessage.

   You can select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif) to add and define more web behaviors; to delete a web behavior, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420542080407/btn_trashcan.gif). You can also select a web behavior and select **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420542078103/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420542078359/btn_mvdwn.gif) to adjust the order of the behaviors, then at runtime, when an event that is bound with more than one action happens, JDashboard triggers the upper action first.
7. Select **OK** to accept the changes and close the dialog box.

## Formatting the Gauge/Pointer/Target Labels

When a solid, dial, activity, or bar gauge chart displays the gauge labels, pointer labels, and target labels, you can format the labels accordingly, for example, edit the size and border of the labels, change the label font size, font color, and so on.

1. Right-click any label of the required type and select **Format Gauge Label**/**Format Pointer Label**/**Format Target Label** from the shortcut menu, or double-click any label of the required type in the gauge chart. Designer displays the [Format Gauge Label dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664491543-Format-Gauge-Label-Dialog-Box), [Format Pointer Label dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661582743-Format-Pointer-Label-Dialog-Box), or [Format Target Label dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664506391-Format-Target-Label-Dialog-Box).

   The following takes the Format Pointer Label dialog box as an example.

   ![Format Pointer Label dialog box - General](https://devnet.logianalytics.com/hc/article_attachments/4420542127895/fmtpntlbl_gnrl.gif)
2. In the **General** tab, specify the general properties of the labels in the chart.

   In the **Size** box, set the width and height of the labels, the horizontal and vertical coordinate of the top left corner of the labels relative to their parent container, the alignment of the text in the labels, and whether to enable the word wrap function for the label text.

   In the **Fill** box, specify the color or effects and the transparency to fill the labels.

   In the **Border** box, specify properties for the border of the labels, including the type, color, line style, color transparency, thickness, ending style, line joint style, fill pattern, and dash size.

   In the **Orientation** box, specify the angle to rotate the labels.
3. In the **Font** tab, specify the font properties of the labels, including the font face, size, color, color transparency, rotation angle, shearing angle, and the font effects such as style, strikethrough, and underline.

   ![Format Pointer Label dialog box - Font](https://devnet.logianalytics.com/hc/article_attachments/4420550900375/fmtpntlbl_font.gif)
4. In the **Format** tab, specify the data format of the labels.

   ![Format Pointer Label dialog box - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4420550900631/fmtpntlbl_fmt.gif)

   Select a category from the **Category** box, then select a format from the **Format** box and select **Add** to add it to the **Stack** box (for more information about each format, [select here](https://devnet.logianalytics.com/hc/en-us/articles/4405664452759-Data-Format-Dialog-Box#DataFormat)). If the formats that Designer provides in the Format box cannot meet your requirement, you can define the format in the **Properties** text box and add it as the format of the selected category. You can add more than one format, but for each category, only one format is allowed. If you do not need a format anymore, select it in the Stack box and select **Remove** to clear it.

   Set the **Auto Scale in Number** option to specify whether to automatically scale the big and small Number values.
5. Select **OK** to accept the changes and close the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664384279-Formatting-the-Rectangles-and-Rectangle-Titles-in-a-Heat-Map)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664385175-Formatting-the-Surface-in-a-Surface-Chart)
