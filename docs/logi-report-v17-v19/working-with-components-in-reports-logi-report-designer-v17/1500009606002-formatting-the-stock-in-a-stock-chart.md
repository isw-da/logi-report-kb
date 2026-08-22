---
title: "Formatting the Stock in a Stock Chart"
id: 1500009606002
section: "Working with Components in Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009606002-Formatting-the-Stock-in-a-Stock-Chart
updated_at: 2021-07-24T16:05:19Z
---

# Formatting the Stock in a Stock Chart

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009605962-Formatting-the-Scatter-in-a-Scatter-Chart) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009605602-Applying-Conditional-Color-Fills-to-Charts)

# Formatting the Stock in a Stock Chart

This topic introduces how to format a stock chart.

1. Right-click any stock line in the stock chart and select **Format Stock** on the shortcut menu, or double-click any stock line. The [Format Stock](https://devnet.logianalytics.com/hc/en-us/articles/1500009631661-Format-Stock-Dialog) dialog appears.

   ![Format Stock dialog - General](https://devnet.logianalytics.com/hc/article_attachments/4404904288791/fmtstck_gnrl.gif)
2. In the General tab, set the color and thickness of the stock lines (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box).

   If the chart is an Open-High-Low-Close stock chart, you can specify the up color to indicate that the opening price is lower than the closing price, the down color to indicate that the opening price is higher than the closing price, and the width of the stock bars.
3. For an Open-High-Low-Close stock chart, in the Border tab select **Show Border** to show the border of the stock bars, then set properties of the border including the border color, transparency, line style, thickness, end caps style, and line joint mode. You can also specify whether the border is to be outlined, and whether or not to automatically resize the border dashes if the border is drawn with dashes.

   ![Format Stock dialog - Border](https://devnet.logianalytics.com/hc/article_attachments/4404916788887/fmtstck_brdr.gif)
4. Skip the Data Label tab since data labels are not supported on stock chart.
5. In the Hint tab, specify whether to
   include the category and series values and whether to scale big and small numbers in the stock hint. A hint displays the value a stock line represents when the mouse pointer points at the stock line in Logi Report Designer view mode, in HTML result, or at server runtime. To make the hint shown, you need to make sure the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/1500009612142-Chart-Paper-Properties#ShowTips) property in the Report Inspector is set to true.

   ![Format Stock - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404904289175/fmtstck_hint.gif)
6. Select **OK** to accept the changes and close the dialog.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009605962-Formatting-the-Scatter-in-a-Scatter-Chart) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009605602-Applying-Conditional-Color-Fills-to-Charts)
