---
title: "Formatting Bubble Chart"
id: 5735563915671
section: "Working with Components in Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735563915671-Formatting-Bubble-Chart
updated_at: 2022-11-02T04:27:55Z
---

# Formatting Bubble Chart

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735520686359-Formatting-Pie-Donut-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735520622999-Formatting-Indicator-Chart)

# Formatting Bubble Chart

This topic describes how you can format the bubbles in a bubble chart.

1. Right-click any bubble in the bubble chart and select **Format Bubble** on the shortcut menu, or double-click any bubble in the chart. Designer displays the [Format Bubble dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735523015959-Format-Bubble-Dialog-Box).

   ![Format Bubble dialog box - General tab](https://devnet.logianalytics.com/hc/article_attachments/9898535682071/fmtbubl_gnrl.gif)
2. In the **General** tab, specify whether to apply a three-dimensional visual effect to the bubbles, and you can use the **Cut Bubble Based on XY Area** option to control whether to cut the bubbles when they are beyond the chart wall (the area formed by the X axis and Y axis). While, Designer still cuts the bubbles if they go beyond the chart paper.
3. In the **Fill** tab, set the color pattern to fill the bubbles.

   ![Format Bubble dialog box - Fill tab](https://devnet.logianalytics.com/hc/article_attachments/9898535692823/fmtbubl_fill.gif)

   * Make your choice for the **Self Settings** option. When Self Settings is cleared (the default behavior), Designer synchronizes the color pattern that you specify here with the [Pattern List](https://devnet.logianalytics.com/hc/en-us/articles/5735545992599-Chart-Properties#Pattern) property of the chart in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart. When you select Self Settings, it indicates that the color pattern is private to the current data markers themselves (the bubbles in this case), which Designer remembers and applies to data markers of the new type automatically if you change the type of the chart later.
   * If the chart has no series field, set the color and transparency to fill all bubbles (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box).
   * If the chart has series field, set the color and transparency to fill the bubbles in the current data series, that is, the bubbles in the same data series as the one you have selected on to open the Format Bubble dialog box. You can also select **Color List** to specify the color pattern for bubbles in each data series respectively using the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522093463-Color-List-Dialog-Box).
4. In the **Border** tab, select **Show Border** if you want to display border for the bubbles, then specify the border properties.

   ![Format Bubble dialog box - Border tab](https://devnet.logianalytics.com/hc/article_attachments/9898535703959/fmtbubl_border.gif)

   * Specify the color, transparency, line style, thickness, ending style, and line joint mode of the border.
   * In the **Path** box, specify the fill pattern of the border: Outline Path or Fill Path.
   * In the **Dash** box, select to automatically adjust the dash size or use fixed dash size if you select a dash line style for the border.
5. Skip the Data Label tab because Designer does not support displaying data labels in bubble charts.
6. In the **Hint** tab, specify properties of the chart hint. A hint displays the value a bubble represents when you point to the bubble in Designer view mode, in HTML output, or at runtime.

   ![Format Bubble - Hint](https://devnet.logianalytics.com/hc/article_attachments/9898519477399/fmtbubl_hint.gif)

   * Clear **Show Category and Series** if you do not want to include the category and series values in the hint.
   * Specify whether to scale big and small numbers in the hint.
   * Select **Customize Chart Value Name** to use customized names for the fields on the value axis in the hint and select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898423153431/btn_ellipsis1.gif) to customize the names as you want.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) You should not edit the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/5735546052119-Chart-Paper-Properties#ShowTips) property of the Chart Paper object in the Report Inspector which is "true" by default, if you want to display the hint.
7. Select **OK** to accept the changes and close the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735520686359-Formatting-Pie-Donut-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735520622999-Formatting-Indicator-Chart)
