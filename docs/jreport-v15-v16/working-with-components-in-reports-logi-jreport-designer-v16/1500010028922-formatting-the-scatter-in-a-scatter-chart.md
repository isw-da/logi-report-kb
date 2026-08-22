---
title: "Formatting the Scatter in a Scatter Chart"
id: 1500010028922
section: "Working with Components in Reports - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010028922-Formatting-the-Scatter-in-a-Scatter-Chart
updated_at: 2021-07-24T10:39:26Z
---

# Formatting the Scatter in a Scatter Chart

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010063541-Formatting-the-Radar-in-a-Radar-Chart) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010028942-Formatting-the-Stock-in-a-Stock-Chart)

# Formatting the Scatter in a Scatter Chart

This topic introduces how to format a scatter chart.

1. Right-click any scatter marker in the scatter chart and select **Format Scatter** on the shortcut menu, or double-click any scatter marker in the chart. The [Format Scatter](https://devnet.logianalytics.com/hc/en-us/articles/1500010066541-Format-Scatter-Dialog) dialog appears.

   ![Format Scatter dialog - General](https://devnet.logianalytics.com/hc/article_attachments/4404901224599/fmtsctr_gnrl.gif)
2. In the General tab, set the general options for the scatter.

   In the Layout box, specify the layout of the scatter. In the Line box, specify the thickness of the lines that connect the nodes if you have set the layout to Straight Line or Curved Line. In the Node box, set the node style, width and height as required.
3. In the Fill tab, set the color pattern to fill the scatter markers.

   ![Format Scatter dialog - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404909199767/fmtsctr_fill.gif)

   First make a choice for the Self Settings checkbox: when Self Settings is unchecked, the color pattern specified here will be synchronized to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500010069721-Chart-Properties#Pattern) on the chart object in the Report Inspector, which can also be applied by data markers of other subtypes if the chart is a combo chart; when Self Settings is checked, it indicates the color pattern is private to the current data markers themselves (the scatter markers in this case), which can be remembered and applied to the data markers of a new type automatically if later you change the type of the chart. Then specify the color and transparency of the color schema to fill the selected scatter markers in the same data series (to change the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010035022-Menu-Tabs#Palette) or input the hexadecimal value of a color directly in the text box). You can also select the **Color List** button to specify the color pattern for scatter markers in the same data series respectively in the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500010030022-Color-List-Dialog) dialog.
4. Skip the Data Label tab since data labels are not supported on scatter chart.
5. In the Hint tab, specify whether to
   include the category and series values and whether to scale big and small numbers in the scatter hint. A hint displays the value a marker in the scatter chart represents when the mouse pointer points at the marker in Logi JReport Designer view mode, in HTML result, or at server runtime. To make the hint shown, you need to make sure the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/1500010033982-Chart-Paper-Properties#ShowTips) property in the Report Inspector is set to true.

   ![Format Scatter - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404909200279/fmtsctr_hint.gif)
6. Select **OK** to apply the settings and close the dialog.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010063541-Formatting-the-Radar-in-a-Radar-Chart) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010028942-Formatting-the-Stock-in-a-Stock-Chart)
