---
title: "Formatting Radar Chart"
id: 5735564083863
section: "Working with Components in Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735564083863-Formatting-Radar-Chart
updated_at: 2022-11-02T04:28:02Z
---

# Formatting Radar Chart

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735507081751-Formatting-Surface-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735527353239-Formatting-Scatter-Chart)

# Formatting Radar Chart

This topic describes how you can format a radar chart.

1. Right-click any line which connects two value nodes in the radar chart and select **Format Radar** on the shortcut menu, or double-click any line connecting two value nodes in the radar chart. Designer displays the [Format Radar dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735514255767-Format-Radar-Dialog-Box).

   ![Format Radar dialog box - General](https://devnet.logianalytics.com/hc/article_attachments/9898480182551/fmtradr_gnrl.gif)
2. In the **General** tab, specify the general properties of the radar.
   * In the **Option** box, set whether to show the category name in the radar, select **Use Fill Radar** to fill the areas formed by value nodes of a same data series in the radar and set the transparency of the areas.
   * In the **Line** box, set the thickness, node style, and node width and height for the lines connecting the value nodes in the radar.
   * In **Arrow Style** box, specify the style of the arrows on the numeric axes in the radar.
3. In the **Fill** tab, set the color pattern to fill the radar areas, which also applies to the corresponding value nodes.

   ![Format Radar dialog box - Fill](https://devnet.logianalytics.com/hc/article_attachments/9898463083927/fmtradr_fill.gif)

   * Make your choice for the **Self Settings** option. When Self Settings is cleared (the default behavior), Designer synchronizes the color pattern that you specify here with the [Pattern List](https://devnet.logianalytics.com/hc/en-us/articles/5735545992599-Chart-Properties#Pattern) property of the chart in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart. When you select Self Settings, it indicates that the color pattern is private to the current data markers themselves (the radar areas in this case), which Designer remembers and applies to data markers of the new type automatically if you change the type of the chart later.
   * Specify the color and transparency to fill the selected radar areas in the same data series (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box).
   * You can also select **Color List** to specify the color pattern for radar areas in the same data series respectively in the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522093463-Color-List-Dialog-Box).
4. In the **Border** tab, select **Show Border** if you want to display border for the radar areas, then specify the border properties.

   ![Format Radar dialog box - Border](https://devnet.logianalytics.com/hc/article_attachments/9898480197783/fmtradr_brdr.gif)

   * Specify the color, transparency, line style, thickness, ending style, and line joint mode of the border.
   * In the **Path** box, specify the fill pattern of the border: Outline Path or Fill Path.
   * In the **Dash** box, select to automatically adjust the dash size or use fixed dash size if you select a dash line style for the border.
5. In the **Data Label** tab, specify properties of the static data labels in the radar chart.

   ![Format Radar dialog box - Data Label](https://devnet.logianalytics.com/hc/article_attachments/9898480202391/fmtradr_data.gif)

   * In the **Static Data Label** box, select **Show Static Data Label** if you want to show static data labels for the value nodes in the radar, then specify the position of the data labels relative to the nodes, the type of the data labels, whether to scale big and small numbers in the data labels, and whether to hide the data label when its value is 0.
   * In the **Font** and **Effects** box, specify the font format and special effects of the data labels, such as the font face, font size, font color, and the font style of the data labels.
6. In the **Hint** tab, specify properties of the chart hint. A hint displays the value a node in the radar chart represents when you point to the node in Designer view mode, in HTML output, or at runtime.

   ![Format Radar - Hint](https://devnet.logianalytics.com/hc/article_attachments/9898463098519/fmtradr_hint.gif)

   * Clear **Show Category and Series** if you do not want to include the category and series values in the hint.
   * Specify whether to scale big and small numbers in the hint.
   * Select **Customize Chart Value Name** to use customized names for the fields on the value axis in the hint and select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898423153431/btn_ellipsis1.gif) to customize the names as you want.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) You should not edit the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/5735546052119-Chart-Paper-Properties#ShowTips) property of the Chart Paper object in the Report Inspector which is "true" by default, if you want to display the hint.
7. Select **OK** to accept the changes and close the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735507081751-Formatting-Surface-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735527353239-Formatting-Scatter-Chart)
