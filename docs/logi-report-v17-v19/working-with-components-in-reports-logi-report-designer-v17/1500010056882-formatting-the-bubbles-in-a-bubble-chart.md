---
title: "Formatting the Bubbles in a Bubble Chart"
id: 1500010056882
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010056882-Formatting-the-Bubbles-in-a-Bubble-Chart
updated_at: 2021-07-23T19:14:39Z
---

# Formatting the Bubbles in a Bubble Chart

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010056982-Formatting-the-Pies-Donuts-and-KPI-Value-Labels-in-a-Pie-Donut-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010056942-Formatting-the-Indicators-in-an-Indicator-Chart)

# Formatting the Bubbles in a Bubble Chart

This topic describes how you can format the bubbles in a bubble chart.

1. Right-click any bubble in the bubble chart and select **Format Bubble** on the shortcut menu, or double-click any bubble in the chart. Designer displays the [Format Bubble dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059122-Format-Bubble-Dialog-Box).

   ![Format Bubble dialog box - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404848565783/fmtbubl_gnrl.gif)
2. In the **General** tab, specify whether or not to apply a three-dimensional visual effect to the bubbles, and you can use the option **Cut Bubble Based on XY Area** to control whether or not to cut the bubbles when they are beyond the chart wall (the area formed by the X axis and Y axis). While, Designer still cuts the bubbles if they go beyond the chart paper.
3. In the **Fill** tab, set the color pattern to fill the bubbles.

   ![Format Bubble dialog box - Fill tab](https://devnet.logianalytics.com/hc/article_attachments/4404848566295/fmtbubl_fill.gif)

   First make a choice for the **Self Settings** checkbox: when Self Settings is unselected (the default behavior), Designer synchronizes the color pattern that you specify here to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#Pattern) on the chart object in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart; when you select Self Settings, it indicates that the color pattern is private to the current data markers themselves (the bubbles in this case), which Designer remembers and applies to the data markers of a new type automatically if later you change the type of the chart. Then, specify the color pattern as follows:

   * If the chart has no series field, set the color and the transparency of the color to fill all bubbles (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box).
   * If the chart has series field, set the color and the transparency of the color to fill the bubbles in the current data series, that is the bubbles in the same data series as the one you have selected on to open the Format Bubble dialog box, or select the **Color List** button to specify the color pattern for bubbles in each data series respectively using the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058302-Color-List-Dialog-Box).
4. In the **Border** tab, specify the properties for the border of the bubbles.

   ![Format Bubble dialog box - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4404856962711/fmtbubl_border.gif)

   Select **Show Border** if you want to show the border of the bubbles, then specify the color, color transparency, line style, thickness, end caps style, and line joint mode of the border.

   In the **Path** box, specify the fill pattern of the border: Outline Path or Fill Path.

   In the **Dash** box, select to automatically adjust the dash size or use fixed dash size if you select a dash line style for the border.
5. Skip the Data Label tab because Designer does not support displaying data labels in bubble charts.
6. In the **Hint** tab, specify whether to include the category and series values and whether to scale big and small numbers in the bubble hint (you need to set the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/1500010100301-Chart-Paper-Properties#ShowTips) property on the chart paper to "true" in the Report Inspector if you want to show the hint). A hint displays the value a bubble represents when you point the mouse pointer at the bubble in Designer view mode, in HTML output, or at runtime.

   ![Format Bubble - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404848567319/fmtbubl_hint.gif)
7. Select **OK** to accept the changes and close the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010056982-Formatting-the-Pies-Donuts-and-KPI-Value-Labels-in-a-Pie-Donut-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010056942-Formatting-the-Indicators-in-an-Indicator-Chart)
