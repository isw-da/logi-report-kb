---
title: "Formatting Stock Chart"
id: 5735527361815
section: "Working with Components in Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735527361815-Formatting-Stock-Chart
updated_at: 2022-11-02T04:28:04Z
---

# Formatting Stock Chart

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735527353239-Formatting-Scatter-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735511924119-Applying-Conditional-Color-Fills-to-Charts)

# Formatting Stock Chart

This topic describes how you can format a stock chart.

1. Right-click any stock line in the stock chart and select **Format Stock** on the shortcut menu, or double-click any stock line. Designer displays the [Format Stock dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735543135511-Format-Stock-Dialog-Box).

   ![Format Stock dialog box - General](https://devnet.logianalytics.com/hc/article_attachments/9898535566487/fmtstck_gnrl.gif)
2. In the **General** tab, specify the color and thickness of the stock lines (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box). For an Open-High-Low-Close stock chart, you can also specify the up color to indicate that the opening price is lower than the closing price, the down color to indicate that the opening price is higher than the closing price, and the width of the stock bars.
3. For an Open-High-Low-Close stock chart, in the **Border** tab, select **Show Border** if you want to display border for the stock bars, then specify the border properties.

   ![Format Stock dialog box - Border](https://devnet.logianalytics.com/hc/article_attachments/9898535572887/fmtstck_brdr.gif)

   * Specify the color, transparency, line style, thickness, ending style, and line joint mode of the border.
   * In the **Path** box, specify the fill pattern of the border: Outline Path or Fill Path.
   * In the **Dash** box, select to automatically adjust the dash size or use fixed dash size if you select a dash line style for the border.
4. Skip the Data Label tab because Designer does not support displaying data labels in stock charts.
5. In the **Hint** tab, specify properties of the chart hint. A hint displays the value a stock line represents when you point to the stock line in Designer view mode, in HTML output, or at runtime.

   ![Format Stock dialog box - Hint](https://devnet.logianalytics.com/hc/article_attachments/9898519331351/fmtstck_hint.gif)

   * Clear **Show Category and Series** if you do not want to include the category and series values in the hint.
   * Specify whether to scale big and small numbers in the hint.
   * Select **Customize Chart Value Name** to use customized names for the fields on the value axis in the hint and select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898423153431/btn_ellipsis1.gif) to customize the names as you want.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) You should not edit the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/5735546052119-Chart-Paper-Properties#ShowTips) property of the Chart Paper object in the Report Inspector which is "true" by default, if you want to display the hint.
6. Select **OK** to accept the changes and close the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735527353239-Formatting-Scatter-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735511924119-Applying-Conditional-Color-Fills-to-Charts)
