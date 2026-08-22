---
title: "Formatting the Scatter in a Scatter Chart"
id: 4405661364119
section: "Working with Components in Reports - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661364119-Formatting-the-Scatter-in-a-Scatter-Chart
updated_at: 2022-01-27T20:34:26Z
---

# Formatting the Scatter in a Scatter Chart

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661362199-Formatting-the-Radar-in-a-Radar-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661365143-Formatting-the-Stock-in-a-Stock-Chart)

# Formatting the Scatter in a Scatter Chart

This topic describes how you can format a scatter chart.

1. Right-click any scatter marker in the scatter chart and select **Format Scatter** on the shortcut menu, or double-click any scatter marker in the chart. Designer displays the [Format Scatter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661589143-Format-Scatter-Dialog-Box).

   ![Format Scatter dialog box - General](https://devnet.logianalytics.com/hc/article_attachments/4420410731287/fmtsctr_gnrl.gif)
2. In the **General** tab, set the general properties of the scatter chart.

   In the **Layout** box, select **None** if you do not want to use lines to connect the markers in the scatter chart, or select **Straight Line** or **Curved Line** to connect the markers using lines of the corresponding style.

   In the **Line** box, specify the thickness of the lines that connect the markers in the scatter chart.

   In the **Node** box, specify the style, width, and height of the markers in the scatter chart.
3. In the **Fill** tab, set the color pattern to fill the scatter markers.

   ![Format Scatter dialog box - Fill](https://devnet.logianalytics.com/hc/article_attachments/4420410731543/fmtsctr_fill.gif)

   Make a choice for the **Self Settings** checkbox first: when Self Settings is cleared (the default behavior), Designer synchronizes the color pattern that you specify here with the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/4405664650263-Chart-Properties#Pattern) on the chart object in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart; when you select Self Settings, it indicates that the color pattern is private to the current data markers themselves (the scatter markers in this case), which Designer remembers and applies to the data markers of a new type automatically if later you change the type of the chart. Then, specify the color and transparency of the color to fill the selected scatter markers in the same data series (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box). You can also select **Color List** to specify the color pattern for scatter markers in the same data series respectively in the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661476887-Color-List-Dialog-Box).
4. Skip the Data Label tab because Designer does not support displaying data labels in scatter charts.
5. In the **Hint** tab, specify options of the chart hint (the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/4405661845015-Chart-Paper-Properties#ShowTips) property of the chart paper in the Report Inspector should be "true" if you want to show the hint): specify whether to include the category and series values in the hint, whether to scale big and small numbers, and whether to use customized names for the fields on the value axis in the hint, and customize the names as you want. A hint displays the value a marker in the scatter chart represents when you point to the marker in Designer view mode, in HTML output, or at runtime.

   ![Format Scatter dialog box - Hint](https://devnet.logianalytics.com/hc/article_attachments/4420394774551/fmtsctr_hint.gif)
6. Select **OK** to apply the settings and close the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661362199-Formatting-the-Radar-in-a-Radar-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661365143-Formatting-the-Stock-in-a-Stock-Chart)
