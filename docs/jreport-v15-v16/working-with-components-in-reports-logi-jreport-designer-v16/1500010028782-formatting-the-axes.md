---
title: "Formatting the Axes"
id: 1500010028782
section: "Working with Components in Reports - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010028782-Formatting-the-Axes
updated_at: 2021-07-24T10:39:28Z
---

# Formatting the Axes

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010063581-Formatting-the-Wall-Floor) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010028862-Formatting-the-Gridlines)

# Formatting the Axes

A chart may contain the following axes: category axis, value axis and series axis. Pie, indicator, heat map and organization charts do not have axes. This topic introduces how to format the axes on a chart.

Below is a list of the sections covered in this topic:

* [Formatting the Category Axis](#Category)
* [Formatting the Value Axis](#Value)
* [Formatting the Series Axis](#Series)

## Formatting the Category Axis

1. Right-click any chart element and select **Format Axes** > **Format Category (X) Axis** on the shortcut menu, or double-click the category axis of the chart. The [Format Category (X) Axis](https://devnet.logianalytics.com/hc/en-us/articles/1500010066361-Format-Category-X-Axis-Dialog) dialog appears.

   ![Format Category (X) Axis dialog - Axis](https://devnet.logianalytics.com/hc/article_attachments/4404901243927/fmtctgryaxis_axis.gif)
2. In the Axis tab, specify settings for the axis.

   In the Option box, check **Show Gridlines** if you want to show gridlines perpendicular to the axis. For a scatter chart or a bubble chart which shows different fields on the category axis and bubble X axis, you can also specify the maximum and minimum values to be displayed, the distance between two adjacent values on the axis, and the number of tick marks to be shown on the axis.

   In the Line box, set the line color, style, transparency, and thickness of the axis (to change the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010035022-Menu-Tabs#Palette) or input the hexadecimal value of a color directly in the text box).

   In the Label box, set the gap between the labels and the axis, and check **Best Effect** to draw the axis labels for the best result effect. By default the values of the field displayed on the category axis are used as the major tick mark labels. If you want to customize the labels, uncheck **Auto**, then from the Label Text drop-down list select a field the values of which will be displayed as the label text, or use a formula to [control the label text](https://devnet.logianalytics.com/hc/en-us/articles/1500010033202-Using-Formulas-to-Control-Object-Properties). You can also select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404901161879/btn_x.gif) to input the desired label text manually.
3. Go to the Tick Mark tab to specify properties for the tick marks.
   1. In the Major Tick Mark and Minor Tick Mark sub tabs, set properties of the major and minor tick marks respectively.

      ![Format Category (X) Axis dialog - Tick Mark - Major Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4404901244183/fmtctgryaxis_mark_major.gif)

      In the Type box, specify whether to show the tick marks and their position which can be inside/outside the chart or across the axis.

      In the Line box, specify the color, style, transparency and thickness of the tick marks. If you want to use the same line setting as that of the axis for the tick marks, check **Correlate with Axis**. Then specify the length of the tick marks.

      In the Option box, specify whether to show the tick mark labels. When the tick mark labels are shown on the axis, you can control the frequency at which the tick marks will be labeled, whether to display the complete label text when the mouse pointer points at a label on the axis, and the number of the tick mark labels to be displayed on the axis.
   2. When the field on the category axis is one of the following types: Number, Date, DateTime, and Time, the Scale sub tab is activated (for a bubble chart only when the category field is one of the above types and the Bubble X Axis uses the category field), where you can specify to label the major and minor tick marks on the axis with constant interval. Constant interval is not supported on scatter charts.

      ![Format Category (X) Axis dialog - Tick Mark - Scale](https://devnet.logianalytics.com/hc/article_attachments/4404901244439/fmtctgryaxis_mark_scale.gif)

      Check **Use Constant Interval** and specify the minimum and maximum values used to label the tick marks, and the unit between two adjacent tick marks. Then the values for the tick marks will be increased continually based on the specified interval instead of just using values from database. This handles cases where data is missing such as weekend days may not show any activity but still need to be shown in the chart. For additional information, see the example in [Labeling Time Series Data by Constant Interval](https://devnet.logianalytics.com/hc/en-us/articles/1500010028982-Labeling-Time-Series-Data-by-Constant-Interval).

      Once you specify to label the tick marks by constant interval, the [customized major tick labels](#LabelText) in the Axis tab are ignored.
4. In the Font tab, format the font of the major and minor tick mark labels respectively, including the font face, size, color, transparency, rotation angle, shearing angle, and effects such as style, strikeout, underline and so on. If you want to apply the font setting of the major tick mark labels to the minor tick marks, check **Correlate with Major Label** in the Minor Label sub tab.

   ![Format Category (X) Axis dialog - Font - Major Label](https://devnet.logianalytics.com/hc/article_attachments/4404909211799/fmtctgryaxis_font_major.gif)
5. In the Orientation tab, set the angles for the major and minor tick mark labels respectively so as to rotate them. You can either drag the Text hand in the Orientation box or type a value in the Angle spinner to perform the operation. You can also make the minor tick marks take the same orientation setting as that of the major tick marks.

   ![Format Catergory (X) Axis dialog - Orientation - Major Label](https://devnet.logianalytics.com/hc/article_attachments/4404909212055/fmtctgryaxis_orntatn_major.gif)
6. In the Format tab, specify the data format of the major and minor tick mark labels respectively.

   ![Format Catergory (X) Axis dialog - Format - Major Label](https://devnet.logianalytics.com/hc/article_attachments/4404909212439/fmtctgryaxis_fmt_major.gif)

   Select a category from the Category box, then select a format from the Format box and select **Add** to add it to the Stack box. If the formats listed in the Format box cannot meet your requirement, define the format in the Properties text box and select **Add** to add it as the format of the selected category. For the Number category, you can specify whether to scale big and small numbers by setting the [Auto Scale in Number](https://devnet.logianalytics.com/hc/en-us/articles/1500010066361-Format-Category-X-Axis-Dialog#AutoScale) option. You can add more than one format, but for each category only one format can be added. In the event that a format is not necessary, select it in the Stack box select **Remove** to clear it. For major tick mark labels, check **Truncate** if you want to truncate the label text when the text is more than 10 characters.

   To make the minor tick mark labels apply the format setting of the major tick marks, check **Correlate with Major Label** in the Minor Label sub tab.
7. For a chart of Bar, Bench, Line or Area type that is created based on a business view, you can divide the category values into different range groups and edit data labels for them in the Range tab. For details, refer to [Editing Range Groups on Category Values](https://devnet.logianalytics.com/hc/en-us/articles/1500010029022-Editing-Range-Groups-on-Category-Values).
8. For a chart in a library component, you can define web behaviors on its axis in the Behaviors tab.

   ![Format Catergory (X) Axis dialog for library component - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404909213847/fmtctgryaxis_bhvr.gif)

   Select a trigger event from the drop-down list in the Events column, then select in the Actions column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404909121559/btn_chsr1.gif) that appears in the text box. In the Web Action List dialog, bind a web action to the axis [the same as you do to web controls](https://devnet.logianalytics.com/hc/en-us/articles/1500010029382-Using-Basic-Web-Controls-in-a-Report#Action) in the library component, which will be triggered when the specified event occurs on the axis. The web actions you can bind include Filter, Sort, Parameter, Property and SendMessage.

   To add a web behavior line, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif), and if a web behavior is not required, select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif) to remove it.

   Select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif) to adjust the order of the behaviors. Then, when an event that has been bound with more than one action happens, the upper action will be triggered first.
9. Select **OK** to accept the changes and close the dialog.

## Formatting the Value Axis

1. Right-click any chart element and do either of the following:
   * Select **Format Axes** > **Format Value (Y) Axis** on the shortcut menu, or double-click the value axis of the chart to bring up the [Format Value (Y) Axis](https://devnet.logianalytics.com/hc/en-us/articles/1500010031162-Format-Value-Y-Axis-Dialog) dialog.
   * Select **Format Axes** > **Format Value (Y2) Axis** on the shortcut menu, or double-click the Y2 axis of the chart to bring up the [Format Value (Y2) Axis](https://devnet.logianalytics.com/hc/en-us/articles/1500010031182-Format-Value-Y2-Axis-Dialog) dialog for a combo chart.

   Take Format Value (Y) Axis dialog for example.

   ![Format Value (Y) Axis dialog - Axis](https://devnet.logianalytics.com/hc/article_attachments/4404901220375/fmtvalueaxis_axis.gif)
2. In the Axis tab, specify settings for the axis.

   In the Option box, specify the maximum and minimum values to be displayed and the distance between two adjacent values on the axis, the number of tick marks to be shown on the axis, and whether or not to show the value labels on the axis in percent. If you want to show gridlines perpendicular to the axis, check **Show Gridlines**.

   In the Line box, set the line color, style, transparency, and thickness of the axis (to change the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010035022-Menu-Tabs#Palette) or input the hexadecimal value of a color directly in the text box).

   In the Label box, set the gap between the labels and the axis, and check **Best Effect** to draw the axis labels for the best result effect.
3. In the Tick Mark tab, specify properties of the major and minor tick marks respectively.

   ![Format Value (Y) Axis dialog - Major Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4404909194391/fmtvalueaxis_mark_major.gif)

   In the Type box, specify whether to show the tick marks and their position which can be inside/outside the chart or across the axis.

   In the Line box, specify the color, style, transparency and thickness of the tick marks. If you want to use the same line setting as that of the axis for the tick marks, check **Correlate with Axis**. Then specify the length of the major/minor tick marks.

   In the Option box (only available for minor tick marks), specify whether to show the major tick mark labels. When the major tick mark labels are shown on the axis, you can control the frequency at which the major tick marks will be labeled, whether to display the complete label text when the mouse pointer points at a label on the axis, and the number of the major tick mark labels to be displayed on the axis.
4. In the Font tab, format the font for text in the major tick mark labels on the axis, including the font face, size, color, transparency, rotation angle, shearing angle, and effects such as style, strikeout, underline and so on.

   ![Format Value (Y) Axis dialog - Font](https://devnet.logianalytics.com/hc/article_attachments/4404909194647/fmtvalueaxis_font.gif)
5. In the Orientation tab, set an angle for the major tick mark labels on the axis so as to rotate them. You can either drag the Text hand in the Orientation box or type a value in the Angle spinner to perform the operation.

   ![Format Value (Y) Axis dialog - Orientation](https://devnet.logianalytics.com/hc/article_attachments/4404901220887/fmtvalueaxis_orntatn.gif)
6. In the Format tab, specify the data format of the major tick mark labels on the axis.

   ![Format Value (Y) Axis dialog - Format](https://devnet.logianalytics.com/hc/article_attachments/4404909194903/fmtvalueaxis_fmt.gif)

   Select a category from the Category box, then select a format from the Format box and select **Add** to add it to the Stack box. If the formats listed in the Format box cannot meet your requirement, define the format in the Properties text box and select **Add** to add it as the format of the selected category. For the Number category, you can specify whether to scale big and small numbers by setting the [Auto Scale in Number](https://devnet.logianalytics.com/hc/en-us/articles/1500010031162-Format-Value-Y-Axis-Dialog#AutoScale) option. You can add more than one format, while for each category, only one format can be added. In the event that a format is not necessary, select it in the Stack box select **Remove** to clear it.
7. Select **OK** to accept the changes and close the dialog.

## Formatting the Series Axis

1. Right-click any chart element and select **Format Axes** > **Format Series (Z) Axis** on the shortcut menu, or double-click the series axis of the chart. The [Format Series (Z) Axis](https://devnet.logianalytics.com/hc/en-us/articles/1500010031142-Format-Series-Z-Axis-Dialog) dialog appears.

   ![Format Series (Z) Axis dialog - Axis](https://devnet.logianalytics.com/hc/article_attachments/4404909198999/fmtseriesaxis_axis.gif)
2. In the Axis tab, specify settings for the axis.

   In the Option box, specify whether or not to only draw the axis (hide the labels), and if not, specify the number of labels to be shown along the axis, the frequency at which the axis will be labeled, whether or not to display the label text when the mouse pointer points at a label on the axis. If you want to show gridlines perpendicular to the axis, check **Show Gridlines**.

   In the Line box, set the line color, style, transparency, and thickness of the axis (to change the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010035022-Menu-Tabs#Palette) or input the hexadecimal value of a color directly in the text box).

   In the Label box, set the gap between the labels and the axis, and check **Best Effect** to draw the axis labels for the best result effect. If the series axis displays a field, by default the values of the field are used as the major tick mark labels on the axis. If you want to customize the labels, uncheck **Auto**, then from the Label Text drop-down list select a field the values of which will be displayed as the label text, or use a formula to [control the label text](https://devnet.logianalytics.com/hc/en-us/articles/1500010033202-Using-Formulas-to-Control-Object-Properties). You can also select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404901161879/btn_x.gif) to input the desired label text manually.
3. In the Tick Mark tab, specify properties of the tick marks.

   ![Format Series (Z) Axis dialog - Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4404909199255/fmtseriesaxis_mark.gif)

   In the Tick Mark box, specify the color, style, transparency and thickness of the tick marks. If you want to use the same line setting as that of the axis for the tick marks, check **Correlate with Axis**.

   In the Major Tick Mark and Minor Tick Mark boxes, set properties for the major and minor tick marks respectively, including whether to show these marks, the position, and length of the marks.
4. In the Font tab, format the font for text in the major tick mark labels on the axis, including the font face, size, color, transparency, rotation angle, shearing angle, and effects such as style, strikeout, underline and so on.

   ![Format Series (Z) Axis dialog - Font](https://devnet.logianalytics.com/hc/article_attachments/4404901224087/fmtseriesaxis_font.gif)
5. In the Orientation tab, set an angle for the major tick mark labels on the axis so as to rotate them. You can either drag the Text hand in the Orientation box or type a value in the Angle spinner to perform the operation.

   ![Format Series (Z) Axis dialog - Orientation](https://devnet.logianalytics.com/hc/article_attachments/4404909199511/fmtseriesaxis_orntatn.gif)
6. In the Format tab, specify the data format of the major tick mark labels on the axis.

   ![Format Series (Z) Axis dialog - Format](https://devnet.logianalytics.com/hc/article_attachments/4404901224343/fmtseriesaxis_fmt.gif)

   Select a category from the Category box, then select a format from the Format box and select **Add** to add it to the Stack box. If the formats listed in the Format box cannot meet your requirement, define the format in the Properties text box and select **Add** to add it as the format of the selected category. For the Number category, you can specify whether to scale big and small numbers by setting the [Auto Scale in Number](https://devnet.logianalytics.com/hc/en-us/articles/1500010031142-Format-Series-Z-Axis-Dialog#AutoScale) option. You can add more than one format, while for each category, only one format can be added. In the event that a format is not necessary, select it in the Stack box select **Remove** to clear it.
7. Select **OK** to accept the changes and close the dialog.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010063581-Formatting-the-Wall-Floor) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010028862-Formatting-the-Gridlines)
