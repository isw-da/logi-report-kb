---
title: "Formatting Scatter Chart"
id: 5735527353239
section: "Working with Components in Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735527353239-Formatting-Scatter-Chart
updated_at: 2022-11-02T04:28:03Z
---

# Formatting Scatter Chart

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735564083863-Formatting-Radar-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735527361815-Formatting-Stock-Chart)

# Formatting Scatter Chart

This topic describes how you can format a scatter chart.

1. Right-click any scatter marker in the scatter chart and select **Format Scatter** on the shortcut menu, or double-click any scatter marker in the chart. Designer displays the [Format Scatter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735523198999-Format-Scatter-Dialog-Box).

   ![Format Scatter dialog box - General](https://devnet.logianalytics.com/hc/article_attachments/9898480099351/fmtsctr_gnrl.gif)
2. In the **General** tab, set the general properties of the scatter chart.
   * In the **Layout** box, select **None** if you do not want to use lines to connect the markers in the scatter chart, or select **Straight Line** or **Curved Line** to connect the markers using lines of the corresponding style.
   * In the **Line** box, specify the thickness of the lines that connect the markers in the scatter chart.
   * In the **Node** box, specify the style, width, and height of the markers in the scatter chart.
3. In the **Fill** tab, set the color pattern to fill the scatter markers.

   ![Format Scatter dialog box - Fill](https://devnet.logianalytics.com/hc/article_attachments/9898463018135/fmtsctr_fill.gif)

   * Make your choice for the **Self Settings** option. When Self Settings is cleared (the default behavior), Designer synchronizes the color pattern that you specify here with the [Pattern List](https://devnet.logianalytics.com/hc/en-us/articles/5735545992599-Chart-Properties#Pattern) property of the chart in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart. When you select Self Settings, it indicates that the color pattern is private to the current data markers themselves (the scatter markers in this case), which Designer remembers and applies to data markers of the new type automatically if you change the type of the chart later.
   * Specify the color and transparency to fill the selected scatter markers in the same data series (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box)
   * You can also select **Color List** to specify the color pattern for scatter markers in the same data series respectively in the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522093463-Color-List-Dialog-Box).
4. Skip the Data Label tab because Designer does not support displaying data labels in scatter charts.
5. In the **Hint** tab, specify properties of the chart hint. A hint displays the value a marker in the scatter chart represents when you point to the marker in Designer view mode, in HTML output, or at runtime.

   ![Format Scatter dialog box - Hint](https://devnet.logianalytics.com/hc/article_attachments/9898463028887/fmtsctr_hint.gif)

   * Clear **Show Category and Series** if you do not want to include the category and series values in the hint.
   * Specify whether to scale big and small numbers in the hint.
   * Select **Customize Chart Value Name** to use customized names for the fields on the value axis in the hint and select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898423153431/btn_ellipsis1.gif) to customize the names as you want.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) You should not edit the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/5735546052119-Chart-Paper-Properties#ShowTips) property of the Chart Paper object in the Report Inspector which is "true" by default, if you want to display the hint.
6. Select **OK** to apply the settings and close the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735564083863-Formatting-Radar-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735527361815-Formatting-Stock-Chart)
