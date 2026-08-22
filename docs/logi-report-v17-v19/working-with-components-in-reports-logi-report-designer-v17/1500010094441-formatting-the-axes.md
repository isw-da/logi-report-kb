---
title: "Formatting the Axes"
id: 1500010094441
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010094441-Formatting-the-Axes
updated_at: 2021-07-23T19:14:38Z
---

# Formatting the Axes

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094641-Formatting-the-Wall-Floor)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094481-Formatting-the-Gridlines)

# Formatting the Axes

A chart may contain the following axes: category axis, value axis, and series axis. Pie, indicator, heat map, and organization charts do not have axes. This topic introduces how you can format each axis of a chart.

This topic contains the following sections:

* [Formatting the Category Axis](#Category)
* [Formatting the Value Axis](#Value)
* [Formatting the Series Axis](#Series)

## Formatting the Category Axis

1. Right-click any chart element and select **Format Axes** > **Format Category (X) Axis** on the shortcut menu, or double-click the category axis of the chart. Designer displays the [Format Category (X) Axis dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097021-Format-Category-X-Axis-Dialog-Box).

   ![Format Category (X) Axis dialog box - Axis](https://devnet.logianalytics.com/hc/article_attachments/4404856956951/fmtctgryaxis_axis.gif)
2. In the **Axis** tab, specify the properties of the category axis.

   In the **Option** box, select **Show Gridlines** if you want to show gridlines perpendicular to the axis. For a scatter chart or a bubble chart which shows different fields on the category axis and bubble X axis, you can also specify the maximum and minimum values to display on the axis, the distance between two adjacent values on the axis, and the number of tick marks to show on the axis.

   In the **Line** box, specify the color, line style, color transparency, and thickness of the axis (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box).

   In the **Label** box, specify the gap between the labels and the axis, and select **Best Effect** to draw the axis labels for the best result effect. By default, Designer uses the values of the field on the category axis as the major tick mark labels of the axis. If you want to customize the labels, clear **Auto**, then from the **Label Text** drop-down list, select the field the values of which you prefer to display as the label text, or use a formula to [control the label text](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties). You can also select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848471319/btn_x.gif) to type the label text manually.
3. In the **Tick Mark** tab, specify the properties of the tick marks on the category axis.
   1. In the **Major Tick Mark** and **Minor Tick Mark** sub tabs, set properties of the major and minor tick marks respectively.

      ![Format Category (X) Axis dialog box - Tick Mark - Major Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4404856957207/fmtctgryaxis_mark_major.gif)

      In the **Type** box, specify whether to show the tick marks and their position which can be inside/outside the axis or across the axis.

      In the **Line** box, keep **Correlate with Axis** selected to apply the line settings that you specify for the axis to the tick marks; otherwise, clear the option and specify the color, line style, color transparency, and thickness of the tick marks. In the **Tick Mark Length** text box, specify the length of the tick marks.

      In the **Option** box, specify whether to show the tick mark labels on the axis; if yes, specify the frequency at which to label the tick marks, and the number of the tick mark labels to display on the axis. For the major tick mark labels, you can also specify whether to display the complete label text when the mouse pointer points at a major tick mark label on the axis.
   2. When the field on the category axis is one of the following types: Number, Date, Time, and DateTime, Designer enables the **Scale** sub tab (for a bubble chart, only when the category field is one of the above types and the Bubble X Axis uses the category field). You can specify to label the major and minor tick marks on the axis with constant interval (you cannot apply constant interval to scatter charts).

      ![Format Category (X) Axis dialog box - Tick Mark - Scale](https://devnet.logianalytics.com/hc/article_attachments/4404848561431/fmtctgryaxis_mark_scale.gif)

      Select **Use Constant Interval** and specify the minimum and maximum values to label the tick marks, and the unit between two adjacent tick marks. Designer then increases the values for the tick marks continually based on the specified interval instead of just using values from database. This handles cases where data is missing such as weekend days may not show any activity but still need to show in the chart. For more information, see the example in [Labeling Time Series Data by Constant Interval](https://devnet.logianalytics.com/hc/en-us/articles/1500010057062-Labeling-Time-Series-Data-by-Constant-Interval).

      Once you specify to label the tick marks by constant interval, Designer ignores the [customized major tick labels](#LabelText) in the Axis tab.
4. In the **Font** tab, format the font of the major and minor tick mark labels on the category axis respectively, including the font face, size, color, color transparency, rotation angle, and shearing angle, and special effects such as style, strikethrough, and underline. If you want to apply the font settings of the major tick mark labels to the minor tick marks, select **Correlate with Major Label** in the Minor Label sub tab.

   ![Format Category (X) Axis dialog box - Font - Major Label](https://devnet.logianalytics.com/hc/article_attachments/4404848561687/fmtctgryaxis_font_major.gif)
5. In the **Orientation** tab, specify the rotation angle of the major and minor tick mark labels on the category axis respectively.

   ![Format Catergory (X) Axis dialog box - Orientation - Major Label](https://devnet.logianalytics.com/hc/article_attachments/4404856958231/fmtctgryaxis_orntatn_major.gif)

   Select **Automatic** if you want to adjust the rotation angle of the tick mark label text on the axis automatically according to the length of the text, in degrees. Then,

   * If the text can completely display horizontally, the default rotation angle is 0.
   * If the text cannot completely display horizontally, the default rotation angle is 30 anticlockwise, and the cut off part shows as suspension points.

   Select **Angle** if you want to customize the rotation angle by yourself. You can either drag the **Text** hand in the **Orientation** box or type a value in the text box to specify the rotation angle.

   If you want to apply the orientation settings of the major tick mark labels to the minor tick mark labels, select **Correlate with Major Label** in the Minor Label sub tab.
6. In the **Format** tab, specify the data format of the major and minor tick mark labels on the category axis respectively.

   ![Format Catergory (X) Axis dialog box - Format - Major Label](https://devnet.logianalytics.com/hc/article_attachments/4404856958487/fmtctgryaxis_fmt_major.gif)

   Select a category from the **Category** box, then select a format from the **Format** box and select **Add** to add it to the **Stack** box (for more information about each format, [select here](https://devnet.logianalytics.com/hc/en-us/articles/1500010096081-Data-Format-Dialog-Box#DataFormat)). If the formats that Designer provides in the Format box cannot meet your requirement, you can define the format in the **Properties** text box and add it as the format of the selected category. You can add more than one format, but for each category, only one format is allowed. If you do not need a format any more, select it in the Stack box and select **Remove** to clear it.

   Set the **Auto Scale in Number** option to specify whether to automatically scale the big and small Number values.

   For major tick mark labels, select **Truncate** if you want to truncate the label text when the text is more than 10 characters.

   To apply the format settings of the major tick marks to the minor tick mark labels, select **Correlate with Major Label** in the Minor Label sub tab.
7. If the chart is of the Bar, Bench, Line, or Area type and its value fields do not contain detail information, you can divide the category values into different range groups and edit data labels for them in the **Range** tab. For more information, see [Editing Range Groups on Category Values](https://devnet.logianalytics.com/hc/en-us/articles/1500010057102-Editing-Range-Groups-on-Category-Values).
8. For a chart in a library component, you can define web behaviors on its category axis in the **Behaviors** tab.
   A web behavior contains a trigger event and a web action to be triggered when the event occurs on the axis at runtime. You can add as many web behaviors to the axis as you need.

   ![Format Catergory (X) Axis dialog box for library component - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404848563223/fmtctgryaxis_bhvr.gif)

   To define the web behavior, select a [trigger event](https://devnet.logianalytics.com/hc/en-us/articles/1500010057562-Using-Basic-Web-Controls-in-a-Report#Event) from the drop-down list in the **Events** column, then select in the **Actions** column and select the **ellipsis** button ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif) in the text box. In the Web Action List dialog box, bind a web action [the same as you do to web controls](https://devnet.logianalytics.com/hc/en-us/articles/1500010057562-Using-Basic-Web-Controls-in-a-Report#Action) in the library component. The web actions you can bind include Filter, Sort, Parameter, Property, and SendMessage.

   You can select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add and define more web behaviors; if a web behavior is not required, select it and select the **Remove** button ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif) to delete it. Select a web behavior and select the **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif) button to adjust the order of the behaviors, then at runtime, when an event that is bound with more than one action happens, JDashboard triggers the upper action first.
9. Select **OK** to accept the changes and close the dialog box.

## Formatting the Value Axis

1. Right-click any chart element and do either of the following:
   * Select **Format Axes** > **Format Value (Y) Axis** on the shortcut menu, or double-click the value axis of the chart. Designer displays the [Format Value (Y) Axis dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097301-Format-Value-Y-Axis-Dialog-Box).
   * Select **Format Axes** > **Format Value (Y2) Axis** on the shortcut menu, or double-click the Y2 axis of the chart. Designer displays the [Format Value (Y2) Axis dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059422-Format-Value-Y2-Axis-Dialog-Box) for a combo chart.

   The following takes Format Value (Y) Axis dialog box for example.

   ![Format Value (Y) Axis dialog box - Axis](https://devnet.logianalytics.com/hc/article_attachments/4404848534295/fmtvalueaxis_axis.gif)
2. In the **Axis** tab, specify settings for the axis.

   In the **Option** box, specify the maximum and minimum values to display and the distance between two adjacent values on the axis, the number of tick marks to show on the axis, and whether or not to show the value labels on the axis in percent. Select **Show Gridlines** if you want to show gridlines perpendicular to the axis.

   In the **Line** box, specify the color, line style, color transparency, and thickness of the axis (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box).

   In the **Label** box, set the gap between the labels and the axis, and select **Best Effect** to draw the axis labels for the best result effect.
3. In the **Tick Mark** tab, specify properties of the major and minor tick marks respectively.

   ![Format Value (Y) Axis dialog box - Major Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4404856929047/fmtvalueaxis_mark_major.gif)

   In the **Type** box, specify whether to show the tick marks and their position which can be inside/outside the axis or across the axis.

   In the **Line** box, keep **Correlate with Axis** selected to apply the line settings that you specify for the axis to the tick marks; otherwise, clear the option and specify the color, line style, color transparency, and thickness of the tick marks. In the **Tick Mark Length** text box, specify the length of the tick marks.

   For major tick marks, in the **Option** box, specify whether to show the major tick mark labels on the axis; if yes, specify the frequency at which to label the major tick marks, the number of the major tick mark labels to display on the axis, and whether to display the complete label text when the mouse pointer points at a major tick mark label on the axis.
4. In the **Font** tab, format the font of the major tick mark labels on the axis, including the font face, size, color, color transparency, rotation angle, and shearing angle, and special effects such as style, strikethrough, and underline.

   ![Format Value (Y) Axis dialog box - Font](https://devnet.logianalytics.com/hc/article_attachments/4404848534935/fmtvalueaxis_font.gif)
5. In the **Orientation** tab, specify the rotation angle of the major tick mark labels on the axis.

   ![Format Value (Y) Axis dialog box - Orientation](https://devnet.logianalytics.com/hc/article_attachments/4404856929815/fmtvalueaxis_orntatn.gif)

   Select **Automatic** if you want to adjust the rotation angle of the major tick mark label text on the axis automatically according to the length of the text, in degrees. Then,

   * If the text can completely display horizontally, the default rotation angle is 0.
   * If the text cannot completely display horizontally, the default rotation angle is 30 anticlockwise, and the cut off part shows as suspension points.

   Select **Angle** if you want to customize the rotation angle by yourself. You can either drag the **Text** hand in the **Orientation** box or type a value in the text box to specify the rotation angle.
6. In the **Format** tab, specify the data format of the major tick mark labels on the axis.

   ![Format Value (Y) Axis dialog box - Format](https://devnet.logianalytics.com/hc/article_attachments/4404848535447/fmtvalueaxis_fmt.gif)

   Select a category from the **Category** box, then select a format from the **Format** box and select **Add** to add it to the **Stack** box (for more information about each format, [select here](https://devnet.logianalytics.com/hc/en-us/articles/1500010096081-Data-Format-Dialog-Box#DataFormat)). If the formats that Designer provides in the Format box cannot meet your requirement, you can define the format in the **Properties** text box and add it as the format of the selected category. You can add more than one format, but for each category, only one format is allowed. If you do not need a format any more, select it in the Stack box and select **Remove** to clear it.

   Set the **Auto Scale in Number** option to specify whether to automatically scale the big and small Number values.
7. Select **OK** to accept the changes and close the dialog box.

## Formatting the Series Axis

1. Right-click any chart element and select **Format Axes** > **Format Series (Z) Axis** from the shortcut menu, or double-click the series axis of the chart. Designer displays the [Format Series (Z) Axis dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097221-Format-Series-Z-Axis-Dialog-Box).

   ![Format Series (Z) Axis dialog box - Axis](https://devnet.logianalytics.com/hc/article_attachments/4404856936215/fmtseriesaxis_axis.gif)
2. In the **Axis** tab, specify the properties of the series axis.

   In the **Option** box, specify whether or not to only draw the axis (hide the labels); if not, specify the number of the labels to display along the axis, the frequency at which to label the axis, and whether or not to display the label text when the mouse pointer points at a label on the axis. If you want to show gridlines perpendicular to the axis, select **Show Gridlines**.

   In the **Line** box, specify the color, line style, color transparency, and thickness of the axis (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box).

   In the **Label** box, specify the gap between the labels and the axis, and select **Best Effect** to draw the axis labels for the best result effect. If the axis displays a field, Designer uses the values of the field as the major tick mark labels on the axis by default. If you want to customize the labels, clear **Auto**, then from the **Label Text** drop-down list, select a field the values of which you prefer to display as the label text, or use a formula to [control the label text](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties). You can also select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848471319/btn_x.gif) to type the label text manually.
3. In the **Tick Mark** tab, specify the properties of the tick marks on the series axis.

   ![Format Series (Z) Axis dialog box - Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4404856936471/fmtseriesaxis_mark.gif)

   In the **Tick Mark** box, keep **Correlate with Axis** selected to apply the line settings that you specify for the axis to the tick marks; otherwise, clear the option and specify the color, line style, color transparency, and thickness of the tick marks. In the Tick Mark Length text box, specify the length of the tick marks.

   In the **Major Tick Mark** and **Minor Tick Mark** boxes, specify the properties for the major and minor tick marks respectively, including whether to show these marks, the position, and the length of the marks.
4. In the **Font** tab, format the font of the text in the major tick mark labels on the series axis, including the font face, size, color, color transparency, rotation angle, and shearing angle, and special effects such as style, strikethrough, and underline.

   ![Format Series (Z) Axis dialog box - Font](https://devnet.logianalytics.com/hc/article_attachments/4404848540055/fmtseriesaxis_font.gif)
5. In the **Orientation** tab, specify the rotation angle of the major tick mark labels on the series axis.

   ![Format Series (Z) Axis dialog box - Orientation](https://devnet.logianalytics.com/hc/article_attachments/4404848540311/fmtseriesaxis_orntatn.gif)

   Select **Automatic** if you want to adjust the rotation angle of the major tick mark label text on the axis automatically according to the length of the text, in degrees. Then,

   * If the text can completely display horizontally, the default rotation angle is 0.
   * If the text cannot completely display horizontally, the default rotation angle is 30 anticlockwise, and the cut off part shows as suspension points.

   Select **Angle** if you want to customize the rotation angle by yourself. You can either drag the **Text** hand in the **Orientation** box or type a value in the text box to specify the rotation angle.
6. In the **Format** tab, specify the data format of the major tick mark labels on the series axis.

   ![Format Series (Z) Axis dialog box - Format](https://devnet.logianalytics.com/hc/article_attachments/4404848540567/fmtseriesaxis_fmt.gif)

   Select a category from the **Category** box, then select a format from the **Format** box and select **Add** to add it to the **Stack** box (for more information about each format, [select here](https://devnet.logianalytics.com/hc/en-us/articles/1500010096081-Data-Format-Dialog-Box#DataFormat)). If the formats that Designer provides in the Format box cannot meet your requirement, you can define the format in the **Properties** text box and add it as the format of the selected category. You can add more than one format, but for each category, only one format is allowed. If you do not need a format any more, select it in the Stack box and select **Remove** to clear it.

   Set the **Auto Scale in Number** option to specify whether to automatically scale the big and small Number values.
7. Select **OK** to accept the changes and close the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094641-Formatting-the-Wall-Floor)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094481-Formatting-the-Gridlines)
