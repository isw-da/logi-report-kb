---
title: "Formatting the Bubbles in a Bubble Chart"
id: 1500009605782
section: "Working with Components in Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009605782-Formatting-the-Bubbles-in-a-Bubble-Chart
updated_at: 2021-07-24T16:05:21Z
---

# Formatting the Bubbles in a Bubble Chart

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009605902-Formatting-the-Pies-Donuts-and-KPI-Value-Labels-in-a-Pie-Donut-Chart) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009605842-Formatting-the-Indicators-in-an-Indicator-Chart)

# Formatting the Bubbles in a Bubble Chart

This topic introduces how to format the bubbles in a bubble chart.

1. Right-click any bubble in the bubble chart and select **Format Bubble** on the shortcut menu, or double-click any bubble in the chart. The [Format Bubble](https://devnet.logianalytics.com/hc/en-us/articles/1500009631301-Format-Bubble-Dialog) dialog appears.

   ![Format Bubble dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404904329623/fmtbubl_gnrl.gif)
2. In the General tab, specify whether or not to apply a 3D visual effect to the bubbles, and you can use the option Cut Bubble Based on XY Area to control whether or not to cut the bubbles when they are beyond the chart wall, which means the area formed by the X axis and Y axis. While, If the bubbles are beyond the chart paper, they will still be cut.
3. In the Fill tab, set the color pattern to fill the bubbles.

   ![Format Bubble dialog - Fill tab](https://devnet.logianalytics.com/hc/article_attachments/4404904329879/fmtbubl_fill.gif)

   First make a choice for the Self Settings checkbox: when Self Settings is unselected, the color pattern specified here will be synchronized to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#Pattern) on the chart object in the Report Inspector, which can also be applied by data markers of other subtypes if the chart is a combo chart; when Self Settings is selected, it indicates the color pattern is private to the current data markers themselves (the bubbles in this case), which can be remembered and applied to the data markers of a new type automatically if later you change the type of the chart. Then specify the color pattern as follows:

   * If the chart has no series field, set the color and the transparency of the color schema to fill all bubbles (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box).
   * If the chart has series field, set the color and the transparency of the color schema to fill the bubbles in the current data series, that is the bubbles in the same data series as the one you have selected on to open the Format Bubble dialog, or select the **Color List** button to specify the color pattern for bubbles in each data series respectively using the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009630161-Color-List-Dialog) dialog.
4. In the Border tab, specify whether to show the border of the bubbles. If yes, set the border properties including the border color, transparency, line style, thickness, end caps style, and line joint mode. You can also specify whether the border is to be outlined, and whether or not to automatically resize the border dashes if the border is drawn with dashes.

   ![Format Bubble dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4404904330775/fmtbubl_border.gif)
5. Skip the Data Label tab since data labels are not supported on bubble chart.
6. In the Hint tab, specify whether to
   include the category and series values and whether to scale big and small numbers in the bubble hint. A hint displays the value a bubble represents when the mouse pointer points at the bubble in Logi Report Designer view mode, in HTML result, or at server runtime. To make the hint shown, you need to make sure the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/1500009612142-Chart-Paper-Properties#ShowTips) property in the Report Inspector is set to true.

   ![Format Bubble - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404904331287/fmtbubl_hint.gif)
7. Select **OK** to accept the changes and close the dialog.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009605902-Formatting-the-Pies-Donuts-and-KPI-Value-Labels-in-a-Pie-Donut-Chart) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009605842-Formatting-the-Indicators-in-an-Indicator-Chart)
