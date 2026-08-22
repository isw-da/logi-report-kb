---
title: "Formatting the Stock in a Stock Chart"
id: 1500010094601
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010094601-Formatting-the-Stock-in-a-Stock-Chart
updated_at: 2021-07-23T19:14:42Z
---

# Formatting the Stock in a Stock Chart

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094581-Formatting-the-Scatter-in-a-Scatter-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094361-Applying-Conditional-Color-Fills-to-Charts)

# Formatting the Stock in a Stock Chart

This topic describes how you can format a stock chart.

1. Right-click any stock line in the stock chart and select **Format Stock** on the shortcut menu, or double-click any stock line. Designer displays the [Format Stock dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097281-Format-Stock-Dialog-Box).

   ![Format Stock dialog box - General](https://devnet.logianalytics.com/hc/article_attachments/4404848537623/fmtstck_gnrl.gif)
2. In the **General** tab, specify the color and thickness of the stock lines (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box).

   If the chart is an Open-High-Low-Close stock chart, you can specify the up color to indicate that the opening price is lower than the closing price, the down color to indicate that the opening price is higher than the closing price, and the width of the stock bars.
3. For an Open-High-Low-Close stock chart, in the **Border** tab, specify the properties for the border of the stock bars.

   ![Format Stock dialog box - Border](https://devnet.logianalytics.com/hc/article_attachments/4404856930583/fmtstck_brdr.gif)

   Select **Show Border** if you want to show the border of the stock bars, then specify the color, color transparency, line style, thickness, end caps style, and line joint mode of the border.

   In the **Path** box, specify the fill pattern of the border: Outline Path or Fill Path.

   In the **Dash** box, select to automatically adjust the dash size or use fixed dash size if you select a dash line style for the border.
4. Skip the Data Label tab because Designer does not support displaying data labels in stock charts.
5. In the **Hint** tab, specify whether to include the category and series values and whether to scale big and small numbers in the stock hint (you need to set the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/1500010100301-Chart-Paper-Properties#ShowTips) property on the chart paper to "true" in the Report Inspector if you want to show the hint). A hint displays the value a stock line represents when you point the mouse pointer at the stock line in Designer view mode, in HTML output, or at runtime.

   ![Format Stock - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404848537879/fmtstck_hint.gif)
6. Select **OK** to accept the changes and close the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094581-Formatting-the-Scatter-in-a-Scatter-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094361-Applying-Conditional-Color-Fills-to-Charts)
