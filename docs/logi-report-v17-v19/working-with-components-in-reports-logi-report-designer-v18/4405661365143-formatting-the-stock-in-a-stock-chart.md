---
title: "Formatting the Stock in a Stock Chart"
id: 4405661365143
section: "Working with Components in Reports - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661365143-Formatting-the-Stock-in-a-Stock-Chart
updated_at: 2022-01-27T20:34:27Z
---

# Formatting the Stock in a Stock Chart

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661364119-Formatting-the-Scatter-in-a-Scatter-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664369943-Applying-Conditional-Color-Fills-to-Charts)

# Formatting the Stock in a Stock Chart

This topic describes how you can format a stock chart.

1. Right-click any stock line in the stock chart and select **Format Stock** on the shortcut menu, or double-click any stock line. Designer displays the [Format Stock dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661597719-Format-Stock-Dialog-Box).

   ![Format Stock dialog box - General](https://devnet.logianalytics.com/hc/article_attachments/4420556159895/fmtstck_gnrl.gif)
2. In the **General** tab, specify the color and thickness of the stock lines (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box).

   If the chart is an Open-High-Low-Close stock chart, you can specify the up color to indicate that the opening price is lower than the closing price, the down color to indicate that the opening price is higher than the closing price, and the width of the stock bars.
3. For an Open-High-Low-Close stock chart, in the **Border** tab, specify properties for the border of the stock bars.

   ![Format Stock dialog box - Border](https://devnet.logianalytics.com/hc/article_attachments/4420550896023/fmtstck_brdr.gif)

   Select **Show Border** if you want to show the border of the stock bars, then specify the color, color transparency, line style, thickness, end caps style, and line joint mode of the border.

   In the **Path** box, specify the fill pattern of the border: Outline Path or Fill Path.

   In the **Dash** box, select to automatically adjust the dash size or use fixed dash size if you select a dash line style for the border.
4. Skip the Data Label tab because Designer does not support displaying data labels in stock charts.
5. In the **Hint** tab, specify options of the chart hint (the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/4405661845015-Chart-Paper-Properties#ShowTips) property of the chart paper in the Report Inspector should be "true" if you want to show the hint): specify whether to include the category and series values in the hint, whether to scale big and small numbers, and whether to use customized names for the fields on the value axis in the hint, and customize the names as you want. A hint displays the value a stock line represents when you point to the stock line in Designer view mode, in HTML output, or at runtime.

   ![Format Stock dialog box - Hint](https://devnet.logianalytics.com/hc/article_attachments/4420556162583/fmtstck_hint.gif)
6. Select **OK** to accept the changes and close the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661364119-Formatting-the-Scatter-in-a-Scatter-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664369943-Applying-Conditional-Color-Fills-to-Charts)
