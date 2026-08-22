---
title: "Formatting the Bars in a Bar/Bench Chart"
id: 1500010028802
section: "Working with Components in Reports - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010028802-Formatting-the-Bars-in-a-Bar-Bench-Chart
updated_at: 2021-07-24T10:39:28Z
---

# Formatting the Bars in a Bar/Bench Chart

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010063461-Formatting-the-Labels) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010028882-Formatting-the-Lines-in-a-Line-Chart)

# Formatting the Bars in a Bar/Bench Chart

This topic introduces how to format the bars in a bar or bench chart.

1. Right-click any bar/bench in the bar/bench chart and select **Format 2D Bar** or **Format 3D Bar** from the shortcut menu, or double-click any bar/bench in the chart. The [Format Bar](https://devnet.logianalytics.com/hc/en-us/articles/1500010066241-Format-Bar-Dialog) dialog appears.

   ![Format Bar dialog - General](https://devnet.logianalytics.com/hc/article_attachments/4404901255959/fmtbar_gnrl_1.gif)
2. In the General tab, specify the general settings of the bars.

   In the Layout box, set the layout of the bars. For a 3-D chart, specify the size of the bars. For a 2-D chart, you can also set the style of the bars to be normal or cylinder, and if you want to add a 3-dimensional effect to the bars, set the Use Depth option to **true** and specify the depth and direction as required. If the chart uses a query resource as the data source, you can [use a formula to control](https://devnet.logianalytics.com/hc/en-us/articles/1500010033202-Using-Formulas-to-Control-Object-Properties) the Use Depth option.
3. For a 2-D chart, in the Size tab, specify the size of the bars which can either be dynamic or fixed.

   To use dynamic bar width, make sure Fixed Bar Width is unchecked, specify the general bar width as a percentage of the unit width. If the chart is a clustered 2-D bar/bench chart which contains data on the series axis or has more than one value on the value axis, you can specify the gap between the bars as a percentage of the unit width, and in the Individual Bar Width box, specify how much the selected bars in the same data series is wider or narrower than a general bar in percentage. You can also select the **Size List** button to specify the size for bars in the same data series respectively in the [Size List](https://devnet.logianalytics.com/hc/en-us/articles/1500010032462-Size-List-Dialog) dialog.

   ![Format Bar dialog - Size tab for Dynamic Bar Width](https://devnet.logianalytics.com/hc/article_attachments/4404909219095/fmtbar_size_dynmc.gif)

   To use fixed bar width, check **Fixed Bar Width**, specify the general bar width. If the chart is a clustered 2-D bar/bench chart which contains data on the series axis or has more than one value on the value axis, you can specify the gap between the bars within a group, and the outer gap between bars out of a group. In the Individual Bar Width box, specify the width and gap for the selected bars in the same data series. Select the **Size List** button to specify the size for bars in the same data series respectively in the [Size List](https://devnet.logianalytics.com/hc/en-us/articles/1500010032462-Size-List-Dialog) dialog if needed. You can also [use formulas to control](https://devnet.logianalytics.com/hc/en-us/articles/1500010033202-Using-Formulas-to-Control-Object-Properties) the options.

   ![Format Bar dialog - Size tab for Fixed Bar Width](https://devnet.logianalytics.com/hc/article_attachments/4404901256599/fmtbar_size_fix.gif)
4. In the Fill tab, specify the fill type: Use Single Color, Use Single Color with Condition or Use Multiple Color with Condition.

   ![Format Bar dialog - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404909219351/fmtbar_fill.gif)

   If you select Use Single Color as the fill type, first make a choice for the Self Settings checkbox: when Self Settings is unchecked, the color pattern specified here will be synchronized to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500010069721-Chart-Properties#Pattern) on the chart object in the Report Inspector, which can also be applied by data markers of other subtypes if the chart is a combo chart; when Self Settings is checked, it indicates the color pattern is private to the current data markers themselves (the bars in this case), which can be remembered and applied to the data markers of a new type automatically if later you change the type of the chart. Then specify the color pattern as follows:

   * If the chart has no series field, specify the color and the transparency of the color schema to fill the bars (to change the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010035022-Menu-Tabs#Palette) or input the hexadecimal value of a color directly in the text box). If you want to make the bar colors vary, check **Vary Colors by Color List**, then select the **Color List** button to specify the color pattern for each bar in the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500010030022-Color-List-Dialog) dialog.
   * If the chart has series field, specify the color and transparency of the color schema to fill the bars in the current data series, that is the bars in the same data series as the one you have selected on to open the Format Bar dialog. You can also select the **Color List** button to specify the color pattern for bars in each data series respectively in the Color List dialog.

   If you select Use Single Color with Condition or Use Multiple Color with Condition as the fill type, specify the conditions and the color pattern bound with each condition respectively. For details, refer to [Adding Conditional Color Fills to Charts](https://devnet.logianalytics.com/hc/en-us/articles/1500010063341-Applying-Conditional-Color-Fills-to-Charts).
5. In the Border tab, check **Show Border** if you want to show the border of the bars, then set properties of the border including the border color, transparency, line style, thickness, end caps style, and line joint mode, and if you specify the line joint mode to be joint round, you can set the the radius for the border joint. You can also specify whether the border is to be outlined, and whether or not to automatically resize the border dashes if the border is drawn with dashes.

   ![Format Bar dialog - Border](https://devnet.logianalytics.com/hc/article_attachments/4404909219735/fmtbar_border.gif)
6. In the Data Label tab, check **Show Static Data Label** if you want to show static data labels on the bars, then decide the position of the labels relative to the bars. When the position of the static data label is set to one of the following: inside center, inside top or inside bottom, you can further specify whether or not to display the data labels inside the bars at the best position. You can also specify the display type for data values in the labels, whether to scale big and small numbers and hide the label whose value is 0. In the Font and Effects boxes, set the font formats and effects of the data labels.

   ![Format Bar dialog - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4404909219991/fmtbar_data.gif)
7. In the Hint tab, specify whether to
   include the category and series values and whether to scale big and small numbers in the bar hint. A hint displays the value a bar represents when the mouse pointer points at the bar in Logi JReport Designer view mode, in HTML result, or at server runtime. To make the hint shown, you need to make sure the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/1500010033982-Chart-Paper-Properties#ShowTips) property in the Report Inspector is set to true.

   ![Format Bar - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404909220375/fmtbar_hint.gif)
8. For a bar chart in a library component, you can define web behaviors on the bars in the Behaviors tab.

   ![Format Bar dialog for library component - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404901256855/fmtbar_bhvr.gif)

   Select a [trigger event](https://devnet.logianalytics.com/hc/en-us/articles/1500010029382-Using-Basic-Web-Controls-in-a-Report#Event) from the drop-down list in the Events column, then select in the Actions column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404909121559/btn_chsr1.gif) that appears in the text box. In the Web Action List dialog, bind a web action to the bars [the same as you do to web controls](https://devnet.logianalytics.com/hc/en-us/articles/1500010029382-Using-Basic-Web-Controls-in-a-Report#Action) in the library component, which will be triggered when the specified event occurs on the bars. The web actions you can bind include Parameter, Filter, Sort, Change Property and Send Message.

   To add more web behaviors, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif) and define them as required; if a web behavior is not required, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif). Select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif) to adjust the order of the behaviors, then at runtime when an event that has been bound with more than one action happens, the upper action will be triggered first.
9. Select **OK** to accept the changes and close the dialog.

**Notes:**

* If the chart is a combo chart composed by bars and areas/lines, when you set the depth properties for the bars, they will be applied to the areas/lines as well, and vice versa.
* For 3-D charts, the Show Static Data Label checkbox in the Data Label tab is grayed out. However, you can still see the data labels by moving the mouse pointer over the bars when viewing the report result in Designer view mode, in HTML format, or in Page Report Studio.
* If you set the style of the bars to be cylinder, the style can take effect only when the Use Depth option is set to true at the same time.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010063461-Formatting-the-Labels) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010028882-Formatting-the-Lines-in-a-Line-Chart)
