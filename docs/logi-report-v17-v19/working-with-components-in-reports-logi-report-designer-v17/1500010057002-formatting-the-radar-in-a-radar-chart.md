---
title: "Formatting the Radar in a Radar Chart"
id: 1500010057002
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010057002-Formatting-the-Radar-in-a-Radar-Chart
updated_at: 2021-07-23T19:14:41Z
---

# Formatting the Radar in a Radar Chart

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094621-Formatting-the-Surface-in-a-Surface-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094581-Formatting-the-Scatter-in-a-Scatter-Chart)

# Formatting the Radar in a Radar Chart

This topic describes how you can format a radar chart.

1. Right-click any line which connects two value nodes in the radar chart and select **Format Radar** on the shortcut menu, or double-click any line connecting two value nodes in the radar chart. Designer displays the [Format Radar dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097181-Format-Radar-Dialog-Box).

   ![Format Radar dialog box - General](https://devnet.logianalytics.com/hc/article_attachments/4404848542743/fmtradr_gnrl.gif)
2. In the **General** tab, specify the general properties of the radar.

   In the **Option** box, set whether or not to show the category name in the radar, select **Use Fill Radar** to fill the areas formed by value nodes of a same data series in the radar and set the transparency of the color to fill the areas.

   In the **Line** box, set the thickness, node style, and node width and height for the lines connecting the value nodes in the radar.

   In **Arrow Style** box, specify the style of the arrows on the numeric axes in the radar.
3. In the **Fill** tab, set the color pattern to fill the radar areas, which also applies to the corresponding value nodes.

   ![Format Radar dialog box - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404856939159/fmtradr_fill.gif)

   To specify the color pattern, first make a choice for the **Self Settings** checkbox: when Self Settings is unselected (the default behavior), Designer synchronizes the color pattern that you specify here with the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#Pattern) on the chart object in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart; when you select Self Settings, it indicates that the color pattern is private to the current data markers themselves (the radar areas in this case), which Designer remembers and applies to the data markers of a new type automatically if later you change the type of the chart. Then, specify the color and the transparency of the color schema to fill the selected radar areas in the same data series (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box). You can also select the **Color List** button to specify the color pattern for radar areas in the same data series respectively in the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058302-Color-List-Dialog-Box).
4. In the **Border** tab, specify the properties for the border of the radar areas.

   ![Format Radar dialog box - Border](https://devnet.logianalytics.com/hc/article_attachments/4404856939415/fmtradr_brdr.gif)

   Select **Show Border** if you want to show the border of the radar areas, then specify the color, color transparency, line style, thickness, end caps style, and line joint mode of the border.

   In the **Path** box, specify the fill pattern of the border: Outline Path or Fill Path.

   In the **Dash** box, select to automatically adjust the dash size or use fixed dash size if you select a dash line style for the border.
5. In the **Data Label** tab, specify the properties of the static data labels in the radar chart.

   ![Format Radar dialog box - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4404856939671/fmtradr_data.gif)

   In the **Static Data Label** box, select **Show Static Data Label** if you want to show static data labels for the value nodes in the radar, then select the position of the data labels relative to the nodes, in which way to display the values in the data labels, whether to scale big and small numbers in the data labels, and whether to hide the data label whose value is 0.

   In the **Font** box, specify the font format of the text in the data labels, including the font face, size, color, color transparency, rotation angle, shearing angle.

   In the **Effects** box, specify the special effects for the text in the data labels such as style, strikethrough, and underline.
6. In the **Hint** tab, specify whether to include the category and series values and whether to scale big and small numbers in the radar hint (you need to set the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/1500010100301-Chart-Paper-Properties#ShowTips) property on the chart paper to "true" in the Report Inspector if you want to show the hint). A hint displays the value a node in the radar chart represents when you point the mouse pointer at the node in Designer view mode, in HTML output, or at runtime.

   ![Format Radar - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404848543383/fmtradr_hint.gif)
7. Select **OK** to accept the changes and close the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094621-Formatting-the-Surface-in-a-Surface-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094581-Formatting-the-Scatter-in-a-Scatter-Chart)
