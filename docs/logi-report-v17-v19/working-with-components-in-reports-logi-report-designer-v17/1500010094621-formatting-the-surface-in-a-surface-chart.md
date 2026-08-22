---
title: "Formatting the Surface in a Surface Chart"
id: 1500010094621
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010094621-Formatting-the-Surface-in-a-Surface-Chart
updated_at: 2021-07-23T19:14:42Z
---

# Formatting the Surface in a Surface Chart

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010056922-Formatting-the-Gauge-in-a-Gauge-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057002-Formatting-the-Radar-in-a-Radar-Chart)

# Formatting the Surface in a Surface Chart

This topic describes how you can format the surface of a surface chart.

1. Right-click any vertex in the surface chart and select **Format Surface** on the shortcut menu, or double-click any vertex in the surface chart. Designer displays the [Format Surface dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059362-Format-Surface-Dialog-Box).

   ![Format Surface dialog box - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404856931735/fmtsrfc_fill.gif)
2. In the **Fill** tab, specify the color pattern to fill the range sections in the surface chart.

   Make a choice for the **Self Settings** checkbox first: when Self Settings is unselected (the default behavior), Designer synchronizes the color pattern that you specify here with the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#Pattern) on the chart object in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart; when you select Self Settings, it indicates that the color pattern is private to the current data markers themselves (the range sections in this case), which Designer remembers and applies to the data markers of a new type automatically if later you change the type of the chart. Then, specify the color and transparency of the color schema to fill the selected range sections in the same data series (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box). You can also select the **Color List** button to specify the color pattern for range sections in the same data series respectively in the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058302-Color-List-Dialog-Box).
3. In the **Border** tab, select **Show Border** if you want to show the border of the range sections in the surface chart.

   ![Format Surface dialog box - Border](https://devnet.logianalytics.com/hc/article_attachments/4404856931991/fmtsrfc_brdr.gif)

   Select **Show Border** if you want to show the border of the range sections, then specify the color, color transparency, line style, thickness, end caps style, and line joint mode of the border.

   In the **Path** box, specify the fill pattern of the border: Outline Path or Fill Path.

   In the **Dash** box, select to automatically adjust the dash size or use fixed dash size if you select a dash line style for the border.
4. Skip the Data Label tab because Designer does not support displaying data labels in surface charts.
5. In the **Hint** tab, specify whether to include the category and series values and whether to scale big and small numbers in the surface hint (you need to set the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/1500010100301-Chart-Paper-Properties#ShowTips) property on the chart paper to "true" in the Report Inspector if you want to show the hint). A hint displays the value a vertex in the surface chart represents when you point the mouse pointer at the vertex in Designer view mode, in HTML output, or at runtime.

   ![Format Surface - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404856932759/fmtsrfc_hint.gif)
6. Select **OK** to accept the changes and close the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010056922-Formatting-the-Gauge-in-a-Gauge-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057002-Formatting-the-Radar-in-a-Radar-Chart)
