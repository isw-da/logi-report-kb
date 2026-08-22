---
title: "Formatting the Bars"
id: 1500009583481
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009583481-Formatting-the-Bars
updated_at: 2021-07-24T05:56:08Z
---

# Formatting the Bars

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583521-Formatting-the-Labels)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563142-Formatting-the-Lines)

# Formatting the Bars

To format the bars in a bar or bench chart, follow the steps below:

1. Right-click any bar in a bar/bench chart and select **Format 2D Bar** or **Format 3D Bar** from the shortcut menu to bring up the Format Bar dialog.

   ![Format Bar dialog - General](https://devnet.logianalytics.com/hc/article_attachments/4404889357847/fmtbar_gnrl_1.gif)
2. In the General tab, specify the general settings of the bars.

   In the Layout box, set the layout of the bars. For a 3-D chart, specify the size of the bars. For a 2-D chart, you can also set the style of the bars to be normal or cylinder, and if you want to add a 3-dimensional effect to the bars, set the Use Depth option to **true** and specify the depth and direction as required.
3. For a 2-D chart, in the Size tab, specify the size of the bars which can either be dynamic or fixed.

   To use dynamic bar width, make sure Fixed Bar Width is unchecked, specify the general bar width as a percentage of the unit width. If the chart is a clustered 2-D bar/bench chart which contains data on the series axis or has more than one value on the value axis, you can specify the gap between the bars as a percentage of the unit width. In the Individual Bar Width box, specify how much the selected bars in the same data series is wider or narrower than a general bar in percentage. You can also select the **Size List** button to specify the size for bars in the same data series respectively in the [Size List](https://devnet.logianalytics.com/hc/en-us/articles/1500009588641-Size-List-Dialog) dialog.

   ![Format Bar dialog - Size - Dynamic Bar Width](https://devnet.logianalytics.com/hc/article_attachments/4404893912215/fmtbar_size_dynmc.gif)

   To use fixed bar width, check **Fixed Bar Width**, specify the general bar width. If the chart is a clustered 2-D bar/bench chart which contains data on the series axis or has more than one value on the value axis, you can specify the gap between the bars within a group, and the outer gap between bars out of a group. In the Individual Bar Width box, specify the width and gap for the selected bars in the same data series. You can also select the **Size List** button to specify the size for bars in the same data series respectively in the [Size List](https://devnet.logianalytics.com/hc/en-us/articles/1500009588641-Size-List-Dialog) dialog.

   ![Format Bar dialog - Size - Fixed Bar Width](https://devnet.logianalytics.com/hc/article_attachments/4404893912471/fmtbar_size_fix.gif)
4. In the Fill tab, specify the fill type: Use Single Color, Use Single Color with Condition or Use Multiple Color with Condition.

   If you select Use Single Color as the fill type,

   ![Format Bar dialog - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404889358103/fmtbar_fill.gif)

   * If the chart has no series field, specify the color and the transparency of the color schema to fill the selected bar (to change the color, select the color image and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette) or input the hexadecimal value of a color directly in the text box). If you want to make the bar colors vary, check **Vary Colors by Color List**, then select the **Color List** button to specify the color pattern for each bar in the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009564822-Color-List-Dialog) dialog.
   * If the chart has series field, specify the color and transparency of the color schema to fill the selected bars in the same data series. You can also select the **Color List** button to specify the color pattern for bars in the same data series respectively in the Color List dialog.

   If you select Use Single Color with Condition or Use Multiple Color with Condition as the fill type, specify the conditions and the color pattern bound with each condition respectively. For details, refer to [Adding Conditional Color Fill to a Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009583381-Adding-Conditional-Color-Fill-to-a-Chart).
5. In the Border tab, set the border mode for the bars, including the border style, color, transparency, line style, thickness, end caps style, and line joint mode, and if you specify the line joint mode to be joint round, you can set the the radius for the border joint. You can also specify whether the border is to be outlined, and whether or not to automatically resize the border dashes if the border is drawn with dashes.

   ![Format Bar dialog - Border](https://devnet.logianalytics.com/hc/article_attachments/4404893912727/fmtbar_border.gif)
6. In the Data Label tab, specify whether or not to show static data labels for every bar, and if to show, the position of the label related to the bar. When the position of the static data label is set to one of the following: inside center, inside top or inside bottom, you can further specify whether or not to display the data labels inside the bars at the best position. Then in the Font and Effects boxes, set the font formats and effects of the data labels.

   ![Format Bar dialog - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4404893912983/fmtbar_data.gif)
7. For a bar chart in a library component, you can define web behaviors on the bars in the Behaviors tab.

   ![Format Bar dialog - Behavior](https://devnet.logianalytics.com/hc/article_attachments/4404893914903/fmtbar_bhvr.gif)

   Select a trigger event from the drop-down list in the Events column, then select in the Actions column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) that appears in the text box to open the Web Action List dialog, where you can bind a web action to the bars which will be triggered when the specified event occurs on the bars. The web actions you can bind include Filter, Sort, Parameter, Property and SendMessage. For details about these web actions, refer to [Applying Web Actions to a Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009584021-Applying-Web-Actions-to-a-Label).

   To add a web behavior line, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif), and if a web behavior is not required, select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif) to remove it.

   Select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif) to adjust the order of the behaviors. Then, when an event that has been bound with more than one action happens, the upper action will be triggered first.
8. When done, select **OK** to accept the changes and close the dialog.

See also the Format Bar dialog for [page report](https://devnet.logianalytics.com/hc/en-us/articles/1500009565722-Format-Bar-Dialog-for-Page-Report-), [web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009587021-Format-Bar-Dialog-for-Web-Report-), or [library component](https://devnet.logianalytics.com/hc/en-us/articles/1500009565702-Format-Bar-Dialog-for-Library-Component-) for detailed explanation about options in the dialog.

**Notes:**

* If the chart is a combo chart composed by bars and areas/lines, when you set the depth properties for the bars, they will be applied to the areas/lines as well, and vice versa.
* For 3-D charts, the Show Static Data Label checkbox in the Data Label tab is grayed out. However, you can still see the data labels by moving the mouse pointer over the bars when viewing the report result in Designer view mode, in HTML format, or in Page Report Studio.
* If you set the style of the bars to be cylinder, the style can take effect only when the Use Depth option is set to true at the same time.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583521-Formatting-the-Labels)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563142-Formatting-the-Lines)
