---
title: "Formatting Surface Chart"
id: 5735507081751
section: "Working with Components in Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735507081751-Formatting-Surface-Chart
updated_at: 2022-11-02T04:28:05Z
---

# Formatting Surface Chart

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735520602391-Formatting-Gauge-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735564083863-Formatting-Radar-Chart)

# Formatting Surface Chart

This topic describes how you can format the surface of a surface chart.

1. Right-click any vertex in the surface chart and select **Format Surface** on the shortcut menu, or double-click any vertex in the surface chart. Designer displays the [Format Surface dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735551436695-Format-Surface-Dialog-Box).

   ![Format Surface dialog box - Fill](https://devnet.logianalytics.com/hc/article_attachments/9898462811927/fmtsrfc_fill.gif)
2. In the **Fill** tab, specify the color pattern to fill the range sections in the surface chart.
   * Make your choice for the **Self Settings** option. When Self Settings is cleared (the default behavior), Designer synchronizes the color pattern that you specify here with the [Pattern List](https://devnet.logianalytics.com/hc/en-us/articles/5735545992599-Chart-Properties#Pattern) property of the chart in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart. When you select Self Settings, it indicates that the color pattern is private to the current data markers themselves (the range sections in this case), which Designer remembers and applies to data markers of the new type automatically if you change the type of the chart later.
   * Specify the color and transparency to fill the selected range sections in the same data series (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box).
   * You can also select **Color List** to specify the color pattern for range sections in the same data series respectively in the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522093463-Color-List-Dialog-Box).
3. In the **Border** tab, select **Show Border** if you want to show the border of the range sections in the surface chart, then specify the border properties.

   ![Format Surface dialog box - Border](https://devnet.logianalytics.com/hc/article_attachments/9898479911447/fmtsrfc_brdr.gif)

   * Specify the color, transparency, line style, thickness, ending style, and line joint mode of the border.
   * In the **Path** box, specify the fill pattern of the border: Outline Path or Fill Path.
   * In the **Dash** box, select to automatically adjust the dash size or use fixed dash size if you select a dash line style for the border.
4. Skip the Data Label tab because Designer does not support displaying data labels in surface charts.
5. In the **Hint** tab, specify properties of the chart hint. A hint displays the value a vertex in the surface chart represents when you point to the vertex in Designer view mode, in HTML output, or at runtime.

   ![Format Surface dialog box - Hint](https://devnet.logianalytics.com/hc/article_attachments/9898462830615/fmtsrfc_hint.gif)

   * Clear **Show Category and Series** if you do not want to include the category and series values in the hint.
   * Specify whether to scale big and small numbers in the hint.
   * Select **Customize Chart Value Name** to use customized names for the fields on the value axis in the hint and select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898423153431/btn_ellipsis1.gif) to customize the names as you want.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) You should not edit the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/5735546052119-Chart-Paper-Properties#ShowTips) property of the Chart Paper object in the Report Inspector which is "true" by default, if you want to display the hint.
6. Select **OK** to accept the changes and close the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735520602391-Formatting-Gauge-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735564083863-Formatting-Radar-Chart)
