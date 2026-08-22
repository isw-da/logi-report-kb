---
title: "Formatting the Surface in a Surface Chart"
id: 1500009628861
section: "Working with Components in Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009628861-Formatting-the-Surface-in-a-Surface-Chart
updated_at: 2021-07-24T16:05:19Z
---

# Formatting the Surface in a Surface Chart

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009628601-Formatting-the-Gauge-in-a-Gauge-Chart) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009605942-Formatting-the-Radar-in-a-Radar-Chart)

# Formatting the Surface in a Surface Chart

This topic introduces how to format the surface of a surface chart.

1. Right-click any vertex on the surface and select **Format Surface** on the shortcut menu, or double-click any vertex on the surface. The [Format Surface](https://devnet.logianalytics.com/hc/en-us/articles/1500009631641-Format-Surface-Dialog) dialog appears.

   ![Format Surface dialog - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404904289431/fmtsrfc_fill.gif)
2. In the Fill tab, set the color pattern to fill the range sections on the surface.

   First make a choice for the Self Settings checkbox: when Self Settings is unselected, the color pattern specified here will be synchronized to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#Pattern) on the chart object in the Report Inspector, which can also be applied by data markers of other subtypes if the chart is a combo chart; when Self Settings is selected, it indicates the color pattern is private to the current data markers themselves (the range sections on the surface in this case), which can be remembered and applied to the data markers of a new type automatically if later you change the type of the chart. Then specify the color and transparency of the color schema to fill the selected range sections in the same data series (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box). You can also select the **Color List** button to specify the color pattern for range sections in the same data series respectively in the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009630161-Color-List-Dialog) dialog.
3. In the Border tab, select **Show Border** if you want to show the border of the range sections on the surface, then set properties of the border including the border color, transparency, line style, thickness, end caps style, and line joint mode. You can also specify whether the border is to be outlined, and whether or not to automatically resize the border dashes if the border is drawn with dashes.

   ![Format Surface dialog - Border](https://devnet.logianalytics.com/hc/article_attachments/4404904289815/fmtsrfc_brdr.gif)
4. Skip the Data Label tab since data labels are not supported on surface chart.
5. In the Hint tab, specify whether to
   include the category and series values and whether to scale big and small numbers in the surface hint. A hint displays the value a vertex on the surface chart represents when the mouse pointer points at the vertex in Logi Report Designer view mode, in HTML result, or at server runtime. To make the hint shown, you need to make sure the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/1500009612142-Chart-Paper-Properties#ShowTips) property in the Report Inspector is set to true.

   ![Format Surface - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404904290327/fmtsrfc_hint.gif)
6. Select **OK** to accept the changes and close the dialog.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009628601-Formatting-the-Gauge-in-a-Gauge-Chart) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009605942-Formatting-the-Radar-in-a-Radar-Chart)
