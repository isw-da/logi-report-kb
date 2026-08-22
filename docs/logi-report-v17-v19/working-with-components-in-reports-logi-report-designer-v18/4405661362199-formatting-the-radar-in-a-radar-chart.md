---
title: "Formatting the Radar in a Radar Chart"
id: 4405661362199
section: "Working with Components in Reports - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661362199-Formatting-the-Radar-in-a-Radar-Chart
updated_at: 2022-01-27T20:34:26Z
---

# Formatting the Radar in a Radar Chart

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664385175-Formatting-the-Surface-in-a-Surface-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661364119-Formatting-the-Scatter-in-a-Scatter-Chart)

# Formatting the Radar in a Radar Chart

This topic describes how you can format a radar chart.

1. Right-click any line which connects two value nodes in the radar chart and select **Format Radar** on the shortcut menu, or double-click any line connecting two value nodes in the radar chart. Designer displays the [Format Radar dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664498583-Format-Radar-Dialog-Box).

   ![Format Radar dialog box - General](https://devnet.logianalytics.com/hc/article_attachments/4420556165783/fmtradr_gnrl.gif)
2. In the **General** tab, specify the general properties of the radar.

   In the **Option** box, set whether to show the category name in the radar, select **Use Fill Radar** to fill the areas formed by value nodes of a same data series in the radar and set the transparency of the color to fill the areas.

   In the **Line** box, set the thickness, node style, and node width and height for the lines connecting the value nodes in the radar.

   In **Arrow Style** box, specify the style of the arrows on the numeric axes in the radar.
3. In the **Fill** tab, set the color pattern to fill the radar areas, which also applies to the corresponding value nodes.

   ![Format Radar dialog box - Fill](https://devnet.logianalytics.com/hc/article_attachments/4420550898711/fmtradr_fill.gif)

   To specify the color pattern, first make a choice for the **Self Settings** checkbox: when Self Settings is cleared (the default behavior), Designer synchronizes the color pattern that you specify here with the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/4405664650263-Chart-Properties#Pattern) on the chart object in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart; when you select Self Settings, it indicates that the color pattern is private to the current data markers themselves (the radar areas in this case), which Designer remembers and applies to the data markers of a new type automatically if later you change the type of the chart. Then, specify the color and the transparency of the color to fill the selected radar areas in the same data series (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box). You can also select **Color List** to specify the color pattern for radar areas in the same data series respectively in the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661476887-Color-List-Dialog-Box).
4. In the **Border** tab, specify properties for the border of the radar areas.

   ![Format Radar dialog box - Border](https://devnet.logianalytics.com/hc/article_attachments/4420542127639/fmtradr_brdr.gif)

   Select **Show Border** if you want to show the border of the radar areas, then specify the color, color transparency, line style, thickness, end caps style, and line joint mode of the border.

   In the **Path** box, specify the fill pattern of the border: Outline Path or Fill Path.

   In the **Dash** box, select to automatically adjust the dash size or use fixed dash size if you select a dash line style for the border.
5. In the **Data Label** tab, specify properties of the static data labels in the radar chart.

   ![Format Radar dialog box - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4420550899479/fmtradr_data.gif)

   In the **Static Data Label** box, select **Show Static Data Label** if you want to show static data labels for the value nodes in the radar, then select the position of the data labels relative to the nodes, in which way to display the values in the data labels, whether to scale big and small numbers in the data labels, and whether to hide the data label whose value is 0.

   In the **Font** box, specify the font format of the text in the data labels, including the font face, size, color, color transparency, rotation angle, shearing angle.

   In the **Effects** box, specify the special effects for the text in the data labels such as style, strikethrough, and underline.
6. In the **Hint** tab, specify options of the chart hint (the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/4405661845015-Chart-Paper-Properties#ShowTips) property of the chart paper in the Report Inspector should be "true" if you want to show the hint): specify whether to include the category and series values in the hint, whether to scale big and small numbers, and whether to use customized names for the fields on the value axis in the hint, and customize the names as you want. A hint displays the value a node in the radar chart represents when you point to the node in Designer view mode, in HTML output, or at runtime.

   ![Format Radar - Hint](https://devnet.logianalytics.com/hc/article_attachments/4420550899863/fmtradr_hint.gif)
7. Select **OK** to accept the changes and close the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664385175-Formatting-the-Surface-in-a-Surface-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661364119-Formatting-the-Scatter-in-a-Scatter-Chart)
