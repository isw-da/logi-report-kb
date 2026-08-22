---
title: "Formatting the Gauge in a Gauge Chart"
id: 1500009628601
section: "Working with Components in Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009628601-Formatting-the-Gauge-in-a-Gauge-Chart
updated_at: 2021-07-24T16:05:21Z
---

# Formatting the Gauge in a Gauge Chart

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009628801-Formatting-the-Rectangles-and-Rectangle-Titles-in-a-Heat-Map) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009628861-Formatting-the-Surface-in-a-Surface-Chart)

# Formatting the Gauge in a Gauge Chart

The format options for a gauge vary with the gauge subtypes: Gauge Solid 2-D, Gauge Dial 2-D, Gauge Activity 2-D, Gauge Bar 2-D, and Gauge Bubble 2-D. This topic introduces how to format gauges based on the type of gauge chart.

This topic includes the following sections:

> * [Formatting a Solid Gauge](#Solid)
> * [Formatting a Dial Gauge](#Dial)
> * [Formatting an Activity Gauge](#Activity)
> * [Formatting a Bar Gauge](#Bar)
> * [Formatting a Bubble Gauge](#Bubble)
> * [Formatting the Pointer/Gauge/Target Labels](#Label)

## Formatting a Solid Gauge

1. Right-click any range in an arc in the solid gauge and select **Format Solid Gauge** on the shortcut menu, or double-click any arc range in the solid gauge. The [Format Solid Gauge](https://devnet.logianalytics.com/hc/en-us/articles/1500009631621-Format-Solid-Gauge-Dialog) dialog appears.

   ![Format Solid Gauge dialog - Circular Graph](https://devnet.logianalytics.com/hc/article_attachments/4404904290711/fmtsldgauge_crculr.gif)
2. In the Circular Graph tab, specify properties for the arcs in the solid gauge.

   In the Size box, set the angle of the arcs (you can select the angle from the drop-down list or select **Customized** to open the [Customize Gauge Angle](https://devnet.logianalytics.com/hc/en-us/articles/1500009607622-Customize-Gauge-Angle-Dialog) dialog to specify the start angle and stop angle), the width of the arcs, the relative size of a circle, and the styles of the start graph and end graph of the arcs.

   In the Fill box,

   * To [use the color defined for the ranges](#SolidRangeColor) as the arc color, select **Use Range Color**, then in the Background text box set the background color of the arcs (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box).
   * To specify the color for the arcs separately, make sure Use Range Color is unselected. First make a choice for the Self Settings checkbox: when Self Settings is unselected, the color pattern specified here will be synchronized to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#Pattern) on the chart object in the Report Inspector, which can also be applied by data markers of other subtypes if the chart is a combo chart; when Self Settings is selected, it indicates the color pattern is private to the current data markers themselves (the arcs in this case), which can be remembered and applied to the data markers of a new type automatically if later you change the type of the chart. Then specify the color and the transparency of the color schema to fill the ranges in the arcs that are in the same data series as the arc range you have selected on to open the Format Solid Gauge dialog, or select the **Color List** button to specify the color pattern for arc ranges in the same data series respectively in the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009630161-Color-List-Dialog) dialog. Set the background color of the arcs in the Background text box. The colors defined for the ranges will also apply to the corresponding pointers if you specify to [display value pointers](#PointerColor) in the solid gauge in the Pointer tab.

   In the Border box, set the line style, thickness, color, transparency, ending style and line joint style for border of the arcs.
3. In the Axis tab, specify properties of the chart axis.
   1. In the Axis sub tab, set properties of the axis.

      ![Format Solid Gauge dialog - Axis - Axis1](https://devnet.logianalytics.com/hc/article_attachments/4404916789399/fmtsldgauge_axis_axis1.gif)

      Select **Show Axis** to display axis in the solid gauge. It is meaningful to select the option so that the other properties related with the axis can work.

      In the Type box, specify the position of the axis, which can be inside, outside or in the center of the arcs.

      In the Option box, specify the minimum and maximum values to be displayed on the axis or [use a formula to control the values](https://devnet.logianalytics.com/hc/en-us/articles/1500009634221-Using-Formulas-to-Control-Object-Properties).

      In the Line box, specify the color and transparency of the axis or select **Use Range Color** to [use the color defined for the ranges](#SolidRangeColor) as the axis color. Specify the style and thickness of the axis.

      In the Gap box, specify the gap between the axis and the arcs if the axis is displayed inside or outside of the arcs.
   2. In the Tick Mark sub tab, specify properties of the tick marks on the axis.

      ![Format Solid Gauge dialog - Axis - Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4404904290967/fmtsldgauge_axis_tkmk.gif)

      To display tick marks on the axis, select how to show it in the Type box: inside, outside or in the center of the axis.

      In the Major Tick Mark Line and Minor Tick Mark Line boxes, specify the distance between two adjacent tick marks on the axis, how many tick marks to display on the axis, and the color, style, transparency, thickness and length of the tick marks respectively. If you want to use the same line setting as that of the axis for the tick mark lines, select **Correlate with Axis**.
   3. In the Label sub tab, specify properties for the data labels on the axis.

      ![Format Solid Gauge dialog - Axis - Label](https://devnet.logianalytics.com/hc/article_attachments/4404904291351/fmtsldgauge_axis_lbl.gif)

      In the Type box, specify the type of the data labels.

      * **None**  
         If selected, the data labels will not be shown on the axis.
      * **Normal**  
         If selected, the data labels will be shown as you specify: in the Label Every N Major Tick Marks combo box, set
        the frequency at which the major tick marks will be labeled;
        select **Auto** if you want all major tick mark labels to be shown on the axis or **Fixed** to show only the specified number of major tick mark labels.
      * **Range Value**  
         If selected, the data labels will show the [range values](#SolidRangeColor) you defined.
      * **Min and Max Values**  
         If selected, the data labels will show the [minimum value and maximum value](#SolidAxisValue) defined in the Axis sub tab.

      In the Gap box, specify the distance between the data labels and the axis in pixels and whether to adjust the labels automatically to make them placed best. When Best Effect is selected, some labels will be hidden when they are overlapped.

      In the Font box, format the font of the data labels, including the font face, size, color, transparency, rotation angle and shearing angle.

      In the Effects box, specify the font effects of the data labels, including the style, strikeout, underline, and so on.
   4. In the Format sub tab, specify the data format of the data labels on the axis.

      ![Format Solid Gauge dialog - Axis - Format](https://devnet.logianalytics.com/hc/article_attachments/4404904291735/fmtsldgauge_axis_fmt.gif)

      Select a category from the Category box, then select a format from the Format box and select **Add** to add it to the Stack box. If the formats listed in the Format box cannot meet your requirement, define the format in the Properties text box and select **Add** to add it as the format of the selected category. For the Number category, you can specify whether to scale big and small numbers by setting the [Auto Scale in Number](https://devnet.logianalytics.com/hc/en-us/articles/1500009631621-Format-Solid-Gauge-Dialog#AutoScale) option. You can add more than one format, but for each category only one format can be added. In the event that a format is not necessary, select it in the Stack box select **Remove** to clear it.
4. In the Pointer tab, specify properties for the pointers of the arcs in the solid gauge.

   ![Format Solid Gauge dialog - Pointer](https://devnet.logianalytics.com/hc/article_attachments/4404904292247/fmtsldgauge_pnt.gif)

   In the Pointer Style box,

   * To use arrow as the pointer style, select **Arrow**, then specify the style of the value pointer, and the width and height of the arrow. You can also select **Style List** to specify the style for pointers in the same data series respectively in the [Style List](https://devnet.logianalytics.com/hc/en-us/articles/1500009633841-Style-List-Dialog) dialog.
   * To use mark as the pointer style, select **Mark**, then specify the style of the value pointer, the width and height of the mark, the position of the mark relative to the arc, and the distance between the pointer and the arc in pixels. You can also select **Style List** to specify the style for pointers in the same data series respectively in the [Style List](https://devnet.logianalytics.com/hc/en-us/articles/1500009633841-Style-List-Dialog) dialog.

   In the Pointer Color box,

   * To use the [color defined for the ranges](#SolidRangeColor) as the pointer color, select **Use Range Color**.
   * To specify color for the pointers separately, leave Use Range Color unselected. First make a choice for the Self Settings checkbox: when Self Settings is unselected, the color pattern specified here will be synchronized to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#Pattern) on the chart object in the Report Inspector, which can also be applied by data markers of other subtypes if the chart is a combo chart; when Self Settings is selected, it indicates the color pattern is private to the current data markers themselves (the pointers in this case), which can be remembered and applied to the data markers of a new type automatically if later you change the type of the chart. Then specify the color and the transparency of the color schema to fill the pointers in the same data series as the arc range you have selected on to open the Format Solid Gauge dialog, or select the **Color List** button to specify the color pattern for pointers in the same data series respectively in the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009630161-Color-List-Dialog) dialog. The colors defined for the pointers will also apply to the corresponding [ranges in the arcs](#ArcColor).

   In the Pointer Value box, specify whether to show values for the pointers and the position relationship between the values and the pointers. You can select the position from the drop-down list or select **customized** to customize the position by dragging any pointer value in the design area.

   In the Pointer Border box, select **Show Pointer Border** if you want to show the border of the pointers, then set properties of the border including line style, thickness, color, and transparency for color.
5. In the Target tab, specify properties of the target in the solid gauge.

   ![Format Solid Gauge dialog - Target](https://devnet.logianalytics.com/hc/article_attachments/4404916789911/fmtsldgauge_tgt.gif)

   Select **Use Target Value** if you want to use target value for the solid gauge, and specify the target value as required. You can type the value in the text box or [use a formula to control the value](https://devnet.logianalytics.com/hc/en-us/articles/1500009634221-Using-Formulas-to-Control-Object-Properties).

   In the Pointer Style box, select the style of the target pointer from the Target Pointer drop-down list. Specify the width and height of the target pointer, the position of the target pointer relative to the arc, and the distance between the target pointer and the arc.

   In the Pointer Color box, specify the color and transparency of the target pointer.

   In the Target Value box, specify whether to show the target value on the solid gauge and the position of the target value relative to the arc. You can select the position from the drop-down list or select customized to customize the position by dragging the target value in the design area.
6. In the Frame tab, specify properties for the frame of the solid gauge.

   ![Format Solid Gauge dialog - Frame](https://devnet.logianalytics.com/hc/article_attachments/4404904292759/fmtsldgauge_frm.gif)

   In the Size box, specify the size of the frame.

   In the Fill box, specify the color and the transparency of the color to fill the frame.

   In the Border box, specify the properties for borders of the frame, including the type, color, line style, transparency, thickness, ending style, line joint style, fill pattern and dash size.

   In the Gauge Group Name box, specify whether to show names for the arcs in the solid gauge which are values of the field on its category axis, and the position of the names relative to the arcs. If the solid gauge contains no category field, the group name shows Report by default.
7. In the Range Color tab, select in the corresponding cells to set the minimum and maximum values, colors from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette), and names for the three predefined value ranges in each arc to fill the arcs with colors. To add a new color range, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif), and if a color range is not required, select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif) to remove it. Then in the Others box, specify the name and color for the values that do not fall into any of the ranges you define.

   ![Format Solid Gauge dialog - Range Color](https://devnet.logianalytics.com/hc/article_attachments/4404904293015/fmtsldgauge_rgclr.gif)
8. In the Hint tab, specify whether to
   include the category and series values and whether to scale big and small numbers in the gauge hint. A hint displays the value a range/pointer of an arc in the solid gauge represents when the mouse pointer points at the range/pointer in Logi Report Designer view mode, in HTML result, or at server runtime. To make the hint shown, you need to make sure the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/1500009612142-Chart-Paper-Properties#ShowTips) property in the Report Inspector is set to true.

   ![Format Solid Gauge dialog - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404904293399/fmtsldgauge_hint.gif)
9. For a solid gauge chart in a library component, you can define web behaviors on it in the Behaviors tab.

   ![Format Solid Gauge dialog - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404904293655/fmtsldgauge_bhvr.gif)

   Select a [trigger event](https://devnet.logianalytics.com/hc/en-us/articles/1500009629441-Using-Basic-Web-Controls-in-a-Report#Event) from the drop-down list in the Events column, then select in the Actions column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) that appears in the text box. In the Web Action List dialog, bind a web action to the solid gauge [the same as you do to web controls](https://devnet.logianalytics.com/hc/en-us/articles/1500009629441-Using-Basic-Web-Controls-in-a-Report#Action) in the library component, which will be triggered when the specified event occurs on the arcs or pointers in the solid gauge. The web actions you can bind include Parameter, Filter, Sort, Change Property and Send Message.

   To add more web behaviors, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) and define them as required; if a web behavior is not required, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif). Select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif) to adjust the order of the behaviors, then at runtime when an event that has been bound with more than one action happens, the upper action will be triggered first.
10. Select **OK** to accept the changes and close the dialog.

## Formatting a Dial Gauge

1. Right-click any pointer in a dial of the dial gauge and select **Format Dial Gauge** on the shortcut menu, or double-click any pointer in the dial gauge. The [Format Dial Gauge](https://devnet.logianalytics.com/hc/en-us/articles/1500009631361-Format-Dial-Gauge-Dialog) dialog appears.

   ![Format Dial Gauge dialog - Circular Graph](https://devnet.logianalytics.com/hc/article_attachments/4404904321687/fmtdlgauge_crculr.gif)
2. In the Circular Graph tab, specify properties for the dials in the dial gauge.

   In the Size box, set the angle of the dials (you can select the angle from the drop-down list or select **Customized** to open the [Customize Gauge Angle](https://devnet.logianalytics.com/hc/en-us/articles/1500009607622-Customize-Gauge-Angle-Dialog) dialog to specify the start angle and stop angle), the width of the dials, the relative size of a dial, and the styles of the start graph and end graph of the dials.

   In the Border box, set the line style, the thickness, the color, the transparency, the ending style and line joint style for borders of the dials.

   Select **Show Range Name** if you want to show the names of the ranges you define, then specify the font formats and effects of the range names in the Font and Effects boxes.
3. Go to the Axis tab to specify properties of the chart axis.
   1. In the Axis sub tab, set properties of the axis.

      ![Format Dial Gauge dialog - Axis - Axis1](https://devnet.logianalytics.com/hc/article_attachments/4404916799639/fmtdlgauge_axis_axis1.gif)

      Select **Show Axis** to display the axis. In the Type box, specify the position of the axis, which can be inside, outside or in the center of the dials.

      In the Option box, specify the minimum and maximum values to be displayed on the axis, or [use a formula to control the values](https://devnet.logianalytics.com/hc/en-us/articles/1500009634221-Using-Formulas-to-Control-Object-Properties). The values will be equally divided into three ranges, each of which will be filled with the color specified in the Color Range tab automatically.

      In the Line box, specify the color and transparency of the axis or select **Use Range Color** to [use the color defined for the ranges](#DialRangeColor) as the axis color. Specify the style and thickness of the axis.

      In the Gap box, specify the gap between the axis and the dials if the axis is displayed inside or outside of the arcs.
   2. In the Tick Mark sub tab, specify properties of the tick marks on the axis.

      ![Format Dial Gauge dialog - Axis - Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4404904321943/fmtdlgauge_axis_tkmk.gif)

      To display tick marks on the axis, select how to show it in the Type box: inside, outside or in the center of the axis.

      In the Major Tick Mark Line and Minor Tick Mark Line boxes, specify the distance between two adjacent tick marks on the axis, how many tick marks to display on the axis, and the color, style, transparency, thickness and length of the tick marks respectively. If you want to use the same line setting as that of the axis for the tick mark lines, select **Correlate with Axis**.
   3. In the Label sub tab, specify properties for the data labels on the axis.

      ![Format Dial Gauge dialog - Axis - Label](https://devnet.logianalytics.com/hc/article_attachments/4404904322199/fmtdlgauge_axis_lbl.gif)

      In the Type box, specify the type of the data labels.

      * **None**  
         If selected, the data labels will not be shown on the axis.
      * **Normal**  
         If selected, the data labels will be shown as you specify: in the Label Every N Major Tick Marks combo box, set the frequency at which the major tick marks will be labeled; select **Auto** if you want all major tick mark labels to be shown on the axis or **Fixed** to show only the specified number of major tick mark labels.
      * **Range Value**  
         If selected, the data labels will show the [range values](#DialRangeColor) you defined.
      * **Min and Max Values**  
         If selected, the data labels will show the [minimum value and maximum value](#DialAxisValue) defined in the Axis sub tab.

      In the Gap box, specify the distance between the data labels and the axis in pixels and whether to adjust the labels automatically to make them placed best. When Best Effect is selected, some labels will be hidden when they are overlapped.

      In the Font box, format the font of the data labels, including the font face, size, color, transparency, rotation angle and shearing angle.

      In the Effects box, specify the font effects of the data labels, including the style, strikeout, underline, and so on.
   4. In the Format sub tab, specify the data format of the data labels on the axis.

      ![Format Dial Gauge dialog - Axis - Format](https://devnet.logianalytics.com/hc/article_attachments/4404904322583/fmtdlgauge_axis_fmt.gif)

      Select a category from the Category box, then select a format from the Format box and select **Add** to add it to the Stack box. If the formats listed in the Format box cannot meet your requirement, define the format in the Properties text box and select **Add** to add it as the format of the selected category. For the Number category, you can specify whether to scale big and small numbers by setting the [Auto Scale in Number](https://devnet.logianalytics.com/hc/en-us/articles/1500009631361-Format-Dial-Gauge-Dialog#AutoScale) option. You can add more than one format, but for each category only one format can be added. In the event that a format is not necessary, select it in the Stack box select **Remove** to clear it.
4. In the Pointer tab, specify properties for the dial pointers.

   ![Format Dial Gauge dialog - Pointer](https://devnet.logianalytics.com/hc/article_attachments/4404904322839/fmtdlgauge_pnt.gif)

   In the Pointer Style box,

   * To use arrow as the pointer style, select **Arrow**, then specify the style of the value pointer, and the width and height of the arrow. You can select **Style List** to specify the style for pointers in the same data series respectively in the [Style List](https://devnet.logianalytics.com/hc/en-us/articles/1500009633841-Style-List-Dialog) dialog.
   * To use mark as the pointer style, select **Mark**, then specify the style of the value pointer, the width and height of the mark, the position relationship of the marks relative to the dial, and the distance between the pointer and the dial in pixels. You can select **Style List** to specify the style for pointers in the same data series respectively in the [Style List](https://devnet.logianalytics.com/hc/en-us/articles/1500009633841-Style-List-Dialog) dialog.

   In the Pointer Color box,

   * To use the [color defined for the ranges](#DialRangeColor) as the pointer color, select **Use Range Color**.
   * To specify color for the pointers separately, leave Use Range Color unselected. First make a choice for the Self Settings checkbox: when Self Settings is unselected, the color pattern specified here will be synchronized to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#Pattern) on the chart object in the Report Inspector, which can also be applied by data markers of other subtypes if the chart is a combo chart; when Self Settings is selected, it indicates the color pattern is private to the current data markers themselves (the pointers in this case), which can be remembered and applied to the data markers of a new type automatically if later you change the type of the chart. Then specify the color and the transparency of the color schema to fill the pointers in the same data series as the pointer you have selected on to open the Format Dial Gauge dialog, or select the **Color List** button to specify the color pattern for pointers in the same data series respectively in the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009630161-Color-List-Dialog) dialog.

   In the Pointer Value box, specify whether to show values for the pointers and the position relationship between the values and the pointers. You can select the position from the drop-down list or select **customized** to customize the position by dragging any pointer value in the design area.

   In the Pointer Border box, select **Show Pointer Border** if you want to show the border of the pointers, then set properties of the border including line style, thickness, color, and transparency for color.
5. In the Target tab, specify the properties of the target in the dial gauge.

   ![Format Dial Gauge dialog - Target](https://devnet.logianalytics.com/hc/article_attachments/4404916799895/fmtdlgauge_tgt.gif)

   Select **Use Target Value** if you want to use target value for the dial gauge, and specify the target value as required. You can type the value in the text box or [use a formula to control the value](https://devnet.logianalytics.com/hc/en-us/articles/1500009634221-Using-Formulas-to-Control-Object-Properties).

   In the Pointer Style box, select the style of the target pointer from the Target Pointer drop-down list. Specify the width and height of the target pointer, the position of the target pointer relative to the arc, and the distance between the target pointer and the dial.

   In the Pointer Color box, specify the transparency for color of the target pointer.

   In the Target Value box, specify whether to show the target value on the dial gauge and the position of the target value relative to the dial. You can select the position from the drop-down list or select customized to customize the position by dragging the target value in the design area.
6. In the Frame tab, specify properties for the frame of the dial gauge.

   ![Format Dial Gauge dialog - Frame](https://devnet.logianalytics.com/hc/article_attachments/4404904323095/fmtdlgauge_frm.gif)

   In the Size box, specify the size of the frame.

   In the Fill box, specify the color and the transparency of the color to fill the frame.

   In the Border box, specify the properties for borders of the frame, including the type, color, line style, transparency, thickness, ending style, line joint style, fill pattern and dash size.

   In the Gauge Group Name box, specify whether to show names for the arcs in the dial gauge which are values of the field on its category axis, and the position of the names relative to the arcs. If the dial gauge contains no category field, the group name shows Report by default.
7. In the Color Range tab, select in the corresponding cells to set the minimum and maximum values, colors from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette), and names for the three predefined value ranges in each dial to fill the dials with colors. To add a new color range, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif), and if a color range is not required, select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif) to remove it. Then in the Others box, specify the name and color for the values that do not fall into any of the ranges you define.

   ![Format Dial Gauge dialog - Range Color](https://devnet.logianalytics.com/hc/article_attachments/4404916800151/fmtdlgauge_rgclr.gif)
8. In the Hint tab, specify whether to
   include the category and series values and whether to scale big and small numbers in the gauge hint. A hint displays the value a pointer in the dial gauge represents when the mouse pointer points at the pointer in Logi Report Designer view mode, in HTML result, or at server runtime. To make the hint shown, you need to make sure the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/1500009612142-Chart-Paper-Properties#ShowTips) property in the Report Inspector is set to true.

   ![Format Dial Gauge dialog - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404904323607/fmtdlgauge_hint.gif)
9. For a dial gauge chart in a library component, you can define web behaviors on it in the Behaviors tab.

   ![Format Dial Gauge dialog - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404916800407/fmtdlgauge_bhvr.gif)

   Select a [trigger event](https://devnet.logianalytics.com/hc/en-us/articles/1500009629441-Using-Basic-Web-Controls-in-a-Report#Event) from the drop-down list in the Events column, then select in the Actions column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) that appears in the text box. In the Web Action List dialog, bind a web action to the dial gauge [the same as you do to web controls](https://devnet.logianalytics.com/hc/en-us/articles/1500009629441-Using-Basic-Web-Controls-in-a-Report#Action) in the library component, which will be triggered when the specified event occurs on the dial pointers. The web actions you can bind include Parameter, Filter, Sort, Change Property and Send Message.

   To add more web behaviors, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) and define them as required; if a web behavior is not required, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif). Select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif) to adjust the order of the behaviors, then at runtime when an event that has been bound with more than one action happens, the upper action will be triggered first.
10. Select **OK** to accept the changes and close the dialog.

## Formatting an Activity Gauge

1. Right-click any circle in the activity gauge and select **Format Solid Gauge** on the shortcut menu, or double-click any circle in the activity gauge. The [Format Activity Gauge](https://devnet.logianalytics.com/hc/en-us/articles/1500009631261-Format-Activity-Gauge-Dialog) dialog displays.

   ![Format Activity Gauge dialog - Circular Graph](https://devnet.logianalytics.com/hc/article_attachments/4404904338711/fmtactvtygauge_crculr.gif)
2. In the Circular Graph tab, specify properties for the circles in the activity gauge.

   In the Size box, set the relative size of a circle, the distance between the circles, and the styles and marks for the start graph and end graph of the circles.

   In the Fill box,

   * To use the [color defined for the ranges](#ActivityRangeColor) as the circle color, select **Use Range Color**.
   * To specify color for the circles separately, leave Use Range Color unselected. First make a choice for the Self Settings checkbox: when Self Settings is unselected, the color pattern specified here will be synchronized to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#Pattern) on the chart object in the Report Inspector, which can also be applied by data markers of other subtypes if the chart is a combo chart; when Self Settings is selected, it indicates the color pattern is private to the current data markers themselves (the circles in this case), which can be remembered and applied to the data markers of a new type automatically if later you change the type of the chart. Then specify the color and the transparency of the color schema to fill the circles in the same data series as the circle you have selected on to open the Format Activity Gauge dialog, or select the **Color List** button to specify the color pattern for circles in the same data series respectively in the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009630161-Color-List-Dialog) dialog. In the Background textbox, set the background color of the circles. To use colors that are lighter than the circles automatically as the background color, select **Auto**, then Background is disabled.

     In the Value box, specifies the minimum and maximum values to be displayed in the chart or [use a formula to control the property](https://devnet.logianalytics.com/hc/en-us/articles/1500009634221-Using-Formulas-to-Control-Object-Properties).
3. In the Pointer tab, specify whether to show values for the pointers and the position relationship between the values and the pointers. You can select the position from the drop-down list or select **customized** to customize the position by dragging any pointer value in the design area.

   ![Format Activity Gauge dialog - Pointer](https://devnet.logianalytics.com/hc/article_attachments/4404916804119/fmtactvtygauge_pnt.gif)
4. In the Target tab, select **Use Target Value** if you want to use target value for the activity gauge, and specify the target value as required. You can type the value in the text box or [use a formula to control the value](https://devnet.logianalytics.com/hc/en-us/articles/1500009634221-Using-Formulas-to-Control-Object-Properties).
   Then in the Target Value box, specify whether to show the target value on the activity gauge and the position of the target value relative to the circle. You can select the position from the drop-down list or select customized to customize the position by dragging the target value in the design area.

   ![Format Activity Gauge dialog - Target](https://devnet.logianalytics.com/hc/article_attachments/4404916804375/fmtactvtygauge_tgt.gif)
5. In the Frame tab, specify properties for the frame of the activity gauge.

   ![Format Activity Gauge dialog - Frame](https://devnet.logianalytics.com/hc/article_attachments/4404916804631/fmtactvtygauge_frm.gif)

   In the Size box, specify the size of the frame.

   In the Fill box, specify the color and the transparency of the color to fill the frame.

   In the Border box, specify the properties for borders of the frame, including the type, color, line style, transparency, thickness, ending style, line joint style, fill pattern and dash size.

   In the Gauge Group Name box, specify whether to show names for the circles in the activity gauge which are values of the field on its category axis, and the position of the names relative to the circles. If the activity gauge contains no category field, the group name shows Report by default.
6. In the Range Color tab, select in the corresponding cells to set the minimum and maximum values, colors from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette), and names for the three predefined value ranges in each circle to fill the circles with colors. To add a new color range, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif), and if a color range is not required, select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif) to remove it. Then in the Others box, specify the name and color for the values that do not fall into any of the ranges you define.

   ![Format Activity Gauge dialog - Range Color](https://devnet.logianalytics.com/hc/article_attachments/4404904339095/fmtactvtygauge_rgclr.gif)
7. In the Hint tab, specify whether to
   include the category and series values and whether to scale big and small numbers in the gauge hint. A hint displays the value a data range in a circle of the activity gauge represents when the mouse pointer points at the range in Logi Report Designer view mode, in HTML result, or at server runtime. To make the hint shown, you need to make sure the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/1500009612142-Chart-Paper-Properties#ShowTips) property in the Report Inspector is set to true.

   ![Format Activity Gauge dialog - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404904339351/fmtactvtygauge_hint.gif)
8. For an activity gauge chart in a library component, you can define web behaviors on it in the Behaviors tab.

   ![Format Activity Gauge dialog - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404904339607/fmtactvtygauge_bhvr.gif)

   Select a [trigger event](https://devnet.logianalytics.com/hc/en-us/articles/1500009629441-Using-Basic-Web-Controls-in-a-Report#Event) from the drop-down list in the Events column, then select in the Actions column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) that appears in the text box. In the Web Action List dialog, bind a web action to the activity gauge [the same as you do to web controls](https://devnet.logianalytics.com/hc/en-us/articles/1500009629441-Using-Basic-Web-Controls-in-a-Report#Action) in the library component, which will be triggered when the specified event occurs on the data ranges of the circles in the activity gauge. The web actions you can bind include Parameter, Filter, Sort, Change Property and Send Message.

   To add more web behaviors, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) and define them as required; if a web behavior is not required, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif). Select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif) to adjust the order of the behaviors, then at runtime when an event that has been bound with more than one action happens, the upper action will be triggered first.
9. Select **OK** to accept the changes and close the dialog.

## Formatting a Bar Gauge

1. Right-click any data marks in a scale of the bar gauge chart and select **Format Bar Gauge** on the shortcut menu, or double-click any arc in the bar gauge. The [Format Bar Gauge](https://devnet.logianalytics.com/hc/en-us/articles/1500009631281-Format-Bar-Gauge-Dialog) dialog.

   ![Format Bar Gauge dialog - Staff Graph](https://devnet.logianalytics.com/hc/article_attachments/4404904331543/fmtbargauge_stfgraph.gif)
2. In the Staff Graph tab, specify properties for bars in the bar gauge.

   In the Bar box, decide the layout of the scales in the bar gauge, the thickness of the bars, and the style of the start graph and end graph of the bars.

   In the Range Border box, set the color, style, transparency, and thickness of the scale borders (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box).

   Select **Show Range Name** if you want to show the names of the ranges you have defined, then specify the font formats and effects of the range names in the Font and Effect boxes.
3. Go to the Axis tab to specify properties of the chart axis.
   1. In the Axis sub tab, set properties of the axis.

      ![Format Bar Gauge dialog - Axis - Axis1](https://devnet.logianalytics.com/hc/article_attachments/4404904331799/fmtbargauge_axis_axis.gif)

      Select **Show Axis** to display axis in the bar gauge, then in the Type box, specify the position of the axis, which can be on the top or bottom of the bar, or in the center of the bar.

      In the Option box, specify the minimum and maximum values to be displayed in the chart or [use a formula to control the property](https://devnet.logianalytics.com/hc/en-us/articles/1500009634221-Using-Formulas-to-Control-Object-Properties). The values will be equally divided into three ranges, each of which will be filled with the color specified in the Color Range tab automatically.

      In the Line box, specify the color and transparency of the axis or select **Use Range Color** to [use the color defined for the ranges](#BarRangeColor) as the axis color. Specify the style and thickness of the axis.

      In the Gap box, specify the gap between the axis and the bars if the axis is displayed inside or outside of the arcs.
   2. In the Tick Mark sub tab, specify properties of the tick marks on the axis.

      ![Format Bar Gauge dialog - Axis - Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4404904332055/fmtbargauge_axis_tkmk.gif)

      To display tick marks on the axis, select how to show it in the Type box: on the top or bottom of the axis, or in the center of the axis.

      In the Major Tick Mark Line and Minor Tick Mark Line boxes, specify the distance between two adjacent tick marks on the axis, how many tick marks to display on the axis, and the color, style, transparency, thickness and length of the tick marks respectively. If you want to use the same line setting as that of the axis for the tick mark lines, select **Correlate with Axis**.
   3. In the Label sub tab, specify properties for the data labels on the axis.

      ![Format Bar Gauge dialog - Axis - Label](https://devnet.logianalytics.com/hc/article_attachments/4404904332311/fmtbargauge_axis_lbl.gif)

      In the Type box, specify the type of the data labels.

      * **None**  
         If selected, the data labels will not be shown on the axis.
      * **Normal**  
         If selected, the data labels will be shown as you specify: in the Label Every N Major Tick Marks combo box, set the frequency at which the major tick marks will be labeled; select **Auto** if you want all major tick mark labels to be shown on the axis or **Fixed** to show only the specified number of major tick mark labels.
      * **Range Value**  
         If selected, the data labels will show the [range values](#BarRangeColor) you defined.
      * **Min and Max Values**  
         If selected, the data labels will show the [minimum value and maximum value](#BarAxisValue) defined in the Axis sub tab.

      In the Gap box, specify the distance between the data label and the axis in pixels and whether to adjust the labels automatically to make them placed best. When Best Effect is selected, some labels will be hidden when they are overlapped.

      In the Font box, format the font of the data labels, including the font face, size, color, transparency, rotation angle and shearing angle.

      In the Effects box, specify the font effects of the data labels, including the style, strikeout, underline, and so on.
   4. In the Format sub tab, specify the data format of the data labels on the axis.

      ![Format Bar Gauge dialog - Axis - Format](https://devnet.logianalytics.com/hc/article_attachments/4404904332567/fmtbargauge_axis_fmt.gif)

      Select a category from the Category box, then select a format from the Format box and select **Add** to add it to the Stack box. If the formats listed in the Format box cannot meet your requirement, define the format in the Properties text box and select **Add** to add it as the format of the selected category. For the Number category, you can specify whether to scale big and small numbers by setting the [Auto Scale in Number](https://devnet.logianalytics.com/hc/en-us/articles/1500009631281-Format-Bar-Gauge-Dialog#AutoScale) option. You can add more than one format, but for each category only one format can be added. In the event that a format is not necessary, select it in the Stack box select **Remove** to clear it.
4. In the Pointer tab, specify the properties for the pointers on the bar gauge.

   ![Format Bar Gauge dialog - Pointer](https://devnet.logianalytics.com/hc/article_attachments/4404916802455/fmtbargauge_pnt.gif)

   Specify the way to show the point: pointer or color bar.

   In the Pointer Style box (available only when Use Pointer is selected), specify the style of the value pointer, the width and height of the pointer, the position relationship of the pointer and the bar, and the distance between the pointer and the bar in pixels. You can select **Style List** to specify the style for pointers in the same data series respectively in the [Style List](https://devnet.logianalytics.com/hc/en-us/articles/1500009633841-Style-List-Dialog) dialog.

   In the Pointer Color box,

   * To use the [color defined for the value ranges](#BarRangeColor) as the pointer color, select **Use Range Color**.
   * To specify color for the pointers separately, leave Use Range Color unselected. First make a choice for the Self Settings checkbox: when Self Settings is unselected, the color pattern specified here will be synchronized to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#Pattern) on the chart object in the Report Inspector, which can also be applied by data markers of other subtypes if the chart is a combo chart; when Self Settings is selected, it indicates the color pattern is private to the current data markers themselves (the pointers in this case), which can be remembered and applied to the data markers of a new type automatically if later you change the type of the chart. Then specify the color and the transparency of the color schema to fill the pointers in the same data series as the pointer you have selected on to open the Format Bar Gauge dialog, or select the **Color List** button to specify the color pattern for pointers in the same data series respectively in the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009630161-Color-List-Dialog) dialog.

   In the Pointer Value box, specify whether to show values for the pointers and the position relationship between the values and the pointers. You can select the position from the drop-down list or select **customized** to customize the position by dragging any pointer value in the design area.

   In the Pointer Border box, select **Show Pointer Border** if you want to show the border of the pointers, then set properties of the border including line style, thickness, color, and transparency for color.
5. In the Target tab, specify properties of the target in the bar gauge.

   ![Format Bar Gauge dialog - Target](https://devnet.logianalytics.com/hc/article_attachments/4404904333207/fmtbargauge_tgt.gif)

   Select **Use Target Value** if you want to use target value for the bar gauge, and specify the target value as required. You can type the value in the text box or [use a formula to control the value](https://devnet.logianalytics.com/hc/en-us/articles/1500009634221-Using-Formulas-to-Control-Object-Properties).

   In the Pointer Style box, select the style of the target pointer from the Target Pointer drop-down list. Specify the width and height of the target pointer, the position of the target pointer relative to the bar, and the distance between the target pointer and the bar.

   In the Pointer Color box, specify the transparency of the target pointer.

   In the Target Value box, specify whether to show the target value on the bar gauge and the position of the target value relative to the bar. You can select the position from the drop-down list or select customized to customize the position by dragging the target value in the design area.
6. In the Frame tab, specify properties for the frame of the bar gauge.

   ![Format Bar Gauge dialog - Frame](https://devnet.logianalytics.com/hc/article_attachments/4404904333463/fmtbargauge_frm.gif)

   In the Size box, specify the size of the frame.

   In the Fill box, specify the color and the transparency of the color to fill the frame.

   In the Border box, specify the properties for borders of the frame, including the type, color, line style, transparency, thickness, ending style, line joint style, fill pattern and dash size.

   In the Gauge Group Name box, specify whether to show names for the arcs in the bar gauge which are values of the field on its category axis, and the position of the names relative to the bars. If the bar gauge contains no category field, the group name shows Report by default.
7. In the Range Color tab, specify whether to use gradient effect, select in the corresponding cells to specify the minimum and maximum values, colors from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette), and names for the three predefined value ranges in each bar to fill the bars with colors. To add a new color range, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif), and if a color range is not required, select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif) to remove it. Then in the Others box, specify the name and color for the values that do not fall into any of the ranges you define.

   ![Format Bar Gauge dialog - Rane Color](https://devnet.logianalytics.com/hc/article_attachments/4404904333719/fmtbargauge_rgclr.gif)
8. In the Hint tab, specify whether to
   include the category and series values and whether to scale big and small numbers in the gauge hint. A hint displays the value a pointer in the bar gauge represents when the mouse pointer points at the pointer in Logi Report Designer view mode, in HTML result, or at server runtime. To make the hint shown, you need to make sure the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/1500009612142-Chart-Paper-Properties#ShowTips) property in the Report Inspector is set to true.

   ![Format Bar Gauge dialog - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404916802711/fmtbargauge_hint.gif)
9. For a bar gauge chart in a library component, you can define web behaviors on it in the Behaviors tab.

   ![Format Bar Gauge dialog - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404904334231/fmtbargauge_bhvr.gif)

   Select a [trigger event](https://devnet.logianalytics.com/hc/en-us/articles/1500009629441-Using-Basic-Web-Controls-in-a-Report#Event) from the drop-down list in the Events column, then select in the Actions column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) that appears in the text box. In the Web Action List dialog, bind a web action to the bar gauge [the same as you do to web controls](https://devnet.logianalytics.com/hc/en-us/articles/1500009629441-Using-Basic-Web-Controls-in-a-Report#Action) in the library component, which will be triggered when the specified event occurs on the pointers of the bar gauge. The web actions you can bind include Parameter, Filter, Sort, Change Property and Send Message.

   To add more web behaviors, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) and define them as required; if a web behavior is not required, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif). Select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif) to adjust the order of the behaviors, then at runtime when an event that has been bound with more than one action happens, the upper action will be triggered first.
10. Select **OK** to accept the changes and close the dialog.

## Formatting a Bubble Gauge

1. Right-click any bubble in the bubble gauge chart and select **Format Bubble Gauge** on the shortcut menu, or double-click any bubble in the bubble gauge. The [Format Bubble Gauge](https://devnet.logianalytics.com/hc/en-us/articles/1500009608362-Format-Bubble-Gauge-Dialog) dialog displays.

   ![Format Bubble Gauge dialog - Staff Graph](https://devnet.logianalytics.com/hc/article_attachments/4404904328599/fmtbublgauge_stfgraph.gif)
2. In the Staff Graph tab, set the properties for the bubbles in the chart.

   In the Bubbles box, set the left margin, top margin, relative radius of the bubbles, and whether or not to draw horizontal/vertical grids.

   In the Border box, select **Show Border** if you want to show the border of the bubbles, then set properties of the border including the line style, thickness, color and color transparency.

   In the Value box, specifies the minimum and maximum values to be displayed in the chart or [use a formula to control the property](https://devnet.logianalytics.com/hc/en-us/articles/1500009634221-Using-Formulas-to-Control-Object-Properties). The values will be equally divided into three ranges, each of which will be filled with the color specified in the Color Range tab automatically.
3. In the Frame tab, specify properties for the frame of the bubble gauge.

   ![Format Bubble Gauge dialog - Frame](https://devnet.logianalytics.com/hc/article_attachments/4404916801943/fmtbublgauge_frm.gif)

   In the Size box, specify the size of the frame.

   In the Fill box, specify the color and the transparency of the color to fill the frame.

   In the Border box, specify the properties for borders of the frame, including the type, color, line style, transparency, thickness, ending style, line joint style, fill pattern and dash size.

   In the Gauge Group Name box, specify whether to show names for the bubbles in the bubble gauge which are values of the field on its category axis, and the position of the names relative to the arcs. If the bubble gauge contains no category field, the group name shows Report by default.
4. In the Range Color tab, select in the corresponding cells to specify the minimum and maximum values, colors from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette) and names for the three predefined value ranges in each bubble to fill the bubbles with colors. To add a new color range, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif), and if a color range is not required, select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif) to remove it. Then in the Others box, specify the name and color for values that do not fall into any of the range you define.

   ![Format Bubble Gauge dialog - Range Color](https://devnet.logianalytics.com/hc/article_attachments/4404904328855/fmtbublgauge_rgclr.gif)
5. In the Hint tab, specify whether to
   include the category and series values and whether to scale big and small numbers in the gauge hint. A hint displays the value a bubble in the bubble gauge represents when the mouse pointer points at the bubble in Logi Report Designer view mode, in HTML result, or at server runtime. To make the hint shown, you need to make sure the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/1500009612142-Chart-Paper-Properties#ShowTips) property in the Report Inspector is set to true.

   ![Format Bubble Gauge dialog - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404904329111/fmtbublgauge_hint.gif)
6. For a bubble gauge chart in a library component, you can define web behaviors on it in the Behaviors tab.

   ![Format Bubble Gauge dialog - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404904329367/fmtbublgauge_bhvr.gif)

   Select a [trigger event](https://devnet.logianalytics.com/hc/en-us/articles/1500009629441-Using-Basic-Web-Controls-in-a-Report#Event) from the drop-down list in the Events column, then select in the Actions column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) that appears in the text box. In the Web Action List dialog, bind a web action to the bubble gauge [the same as you do to web controls](https://devnet.logianalytics.com/hc/en-us/articles/1500009629441-Using-Basic-Web-Controls-in-a-Report#Action) in the library component, which will be triggered when the specified event occurs on the bubbles. The web actions you can bind include Parameter, Filter, Sort, Change Property and Send Message.

   To add more web behaviors, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) and define them as required; if a web behavior is not required, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif). Select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif) to adjust the order of the behaviors, then at runtime when an event that has been bound with more than one action happens, the upper action will be triggered first.
7. Select **OK** to accept the changes and close the dialog.

## Formatting the Gauge/Pointer/Target Labels

When a solid, dial, activity, or bar gauge chart displays the gauge labels, pointer labels and target labels, you can format the labels accordingly, for example, edit the size and border of the labels, change the label font size, font color, and so on.

1. Right-click any label of the required type and select **Format Gauge****Label**/**Format Pointer Label**/**Format Target Label** on the shortcut menu to bring up the [Format Gauge Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009631381-Format-Gauge-Label-Dialog) dialog, [Format Pointer Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009631541-Format-Pointer-Label-Dialog) dialog or [Format Target Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009608622-Format-Target-Label-Dialog) dialog.

   The following takes the Format Pointer Label dialog as an example.

   ![Format Pointer Label dialog - General](https://devnet.logianalytics.com/hc/article_attachments/4404904299671/fmtpntlbl_gnrl.gif)
2. In the General tab, set the general information for the labels in the chart.

   In the Size box, set the width and height of the labels, the horizontal and vertical coordinate of the top left corner of the labels, relative to their parent container, the alignment of the label text, and whether to enable the word wrap function for the label text.

   In the Fill box, specify the fill color and color transparency to fill the labels.

   In the Border box, specify the properties for borders of the labels, including the type, color, line style, transparency, thickness, ending style, line joint style, fill pattern and dash size.

   In the Orientation box, specify the angle of the labels so as to rotate them.
3. In the Font tab, format the font of the labels, including the font face, size, color, transparency, rotation angle, shearing angle, and effects such as style, strikeout, underline, and so on.

   ![Format Pointer Label dialog - Font](https://devnet.logianalytics.com/hc/article_attachments/4404916792599/fmtpntlbl_font.gif)
4. In the Format tab, specify the data format of the labels.

   ![Format Pointer Label dialog - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404904300055/fmtpntlbl_fmt.gif)

   Select a category from the Category box, then select a format from the Format box and select **Add** to add it to the Stack box. If the formats listed in the Format box cannot meet your requirement, define the format in the Properties text box and select **Add** to add it as the format of the selected category. For the Number category, you can specify whether to scale big and small numbers by setting the [Auto Scale in Number](https://devnet.logianalytics.com/hc/en-us/articles/1500009631541-Format-Pointer-Label-Dialog#AutoScale) option. You can add more than one format, but for each category only one format can be added. In the event that a format is not necessary, select it in the Stack box select **Remove** to clear it.
5. Select **OK** to accept the changes and close the dialog.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009628801-Formatting-the-Rectangles-and-Rectangle-Titles-in-a-Heat-Map) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009628861-Formatting-the-Surface-in-a-Surface-Chart)
