---
title: "Formatting the Gauge"
id: 1500009583501
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009583501-Formatting-the-Gauge
updated_at: 2021-07-24T05:56:08Z
---

# Formatting the Gauge

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583601-Formatting-the-Rectangle-Titles)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563202-Formatting-the-Surface)

# Formatting the Gauge

The appearance of a gauge chart can be customized using many options. The formatting options vary with the subtypes: [Gauge Dial 2-D](#Dial), [Gauge Bar 2-D](#Bar), and [Gauge Bubble 2-D](#Bubble).

**To format a dial gauge chart:**

1. Right-click any pointer in a dial of the dial gauge chart, and then select **Format Dial Gauge** on the shortcut menu to bring up the Format Dial Gauge dialog.

   ![Format Dial Gauge dialog - General](https://devnet.logianalytics.com/hc/article_attachments/4404893901463/fmtdlgauge_gnrl.gif)
2. In the General tab, specify the general options for the dials in the chart.

   In the Circular box, set the start angle and stop angle of the dials, the dial curve style, the width of the dials, and the relative size of a dial.

   In the Pointer box, set the pointer style and arrow style.

   In the Color Range box, specify whether or not to fill the dial with colors, and if to fill, select in the corresponding cells to set the minimum and maximum values and colors from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette) for the three predefined ranges in each dial.
3. In the Fill tab, specify the color and the transparency of the color schema to fill the selected pointers in the same data series (to change the color, select the color image and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette) or input the hexadecimal value of a color directly in the text box). If required, select the **Color List** button to specify the color pattern for pointers in the same data series respectively in the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009564822-Color-List-Dialog) dialog.

   ![Format Dial Gauge dialog - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404893901719/fmtdlgauge_fill.gif)
4. In the Border tab, set the border mode for the pointers, including the border style, color, transparency, line style, thickness, end caps style, and line joint mode. You can also specify whether the border is to be outlined, and whether or not to automatically resize the border dashes if the border is drawn with dashes.
![Format Dial Gauge dialog - Border](https://devnet.logianalytics.com/hc/article_attachments/4404889351447/fmtdlgauge_brdr.gif)5. In the Data Label tab, set the font formats and effects of the data labels.
6. For a dial gauge chart in a library component, you can define web behaviors on the dial gauges in the Behaviors tab.

   ![Format Dial Gauge dialog - Behavior](https://devnet.logianalytics.com/hc/article_attachments/4404893902743/fmtdlgauge_bhvr.gif)

   Select a trigger event from the drop-down list in the Events column, then select in the Actions column and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) that appears in the text box to open the Web Action List dialog, where you can bind a web action to the dial gauges which will be triggered when the specified event occurs on the dial gauges. The web actions you can bind include Filter, Sort, Parameter, Property and SendMessage. For details about these web actions, refer to [Applying Web Actions to a Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009584021-Applying-Web-Actions-to-a-Label).

   To add a web behavior line, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif), and if a web behavior is not required, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif) to remove it.

   Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif) to adjust the order of the behaviors. Then, when an event that has been bound with more than one action happens, the upper action will be triggered first.
7. When done, select **OK** to apply the settings.

**To format a bar gauge chart:**

1. Right-click any data marks in a scale of the bar gauge chart, and then select **Format Bar Gauge** on the shortcut menu to bring up the Format Bar Gauge dialog.

   ![Format Bar Gauge dialog - General](https://devnet.logianalytics.com/hc/article_attachments/4404893909911/fmtbargauge_gnrl.gif)
2. In the General tab, set the general options for the bar gauge chart.

   In the Option box, decide the layout of the scales in the gauge chart.

   In the Range Border box, set the color, style, transparency, and thickness of the scale borders (to change the color, select the color image and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette) or input the hexadecimal value of a color directly in the text box).

   In the Color Range box, select in the corresponding cells to specify the minimum and maximum values and colors from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette) for the three predefined ranges in each scale.
3. In the Fill tab, specify the color and the transparency of the color schema to fill the selected data marks in the same data series. If required, select the **Color List** button to specify the color pattern for data marks in the same data series respectively in the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009564822-Color-List-Dialog) dialog.

   ![Format Bar Gauge dialog - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404893910167/fmtbargauge_fill.gif)
4. In the Border tab, set the border mode for the data marks, including the border style, color, transparency, line style, thickness, end caps style, and line joint mode. You can also specify whether the border is to be outlined, and whether or not to automatically resize the border dashes if the border is drawn with dashes.

   ![Format Bar Gauge dialog - Border](https://devnet.logianalytics.com/hc/article_attachments/4404893910423/fmtbargauge_border.gif)
5. In the Data Label tab, set the font formats and effects of the data labels.
6. For a bar gauge chart in a library component, you can define web behaviors on the bar gauges in the Behaviors tab.

   ![Format Bar Gauge dialog - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404893911703/fmtbargauge_bhvr.gif)

   Select a trigger event from the drop-down list in the Events column, then select in the Actions column and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) that appears in the text box to open the Web Action List dialog, where you can bind a web action to the bar gauges which will be triggered when the specified event occurs on the bar gauges. The web actions you can bind include Filter, Sort, Parameter, Property and SendMessage. For details about these web actions, refer to [Applying Web Actions to a Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009584021-Applying-Web-Actions-to-a-Label).

   To add a web behavior line, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif), and if a web behavior is not required, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif) to remove it.

   Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif) to adjust the order of the behaviors. Then, when an event that has been bound with more than one action happens, the upper action will be triggered first.
7. When done, select **OK** to apply the settings.

**To format a bubble gauge chart:**

1. Right-click any bubble in the bubble gauge chart, and then select **Format Bubble Gauge** on the shortcut menu to bring up the Format Bubble Gauge dialog.

   ![Format Bubble Gauge dialog - General](https://devnet.logianalytics.com/hc/article_attachments/4404889356055/fmtbublgauge_gnrl.gif)
2. In the General tab, set the general options for the bubbles in the chart.

   In the Option box, set the left margin, top margin, relative radius of the bubbles, and whether or not to draw horizontal/vertical grids.

   In the Value box, specifies the minimum and maximum values for the color range. The values will be equally divided into three ranges, each of which will be filled with the color specified in the Color Range box automatically. Values beyond the minimum and maximum will be filled with gray color by default.

   In the Color Range box, select in the corresponding cells to specify the minimum and maximum values, colors from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette) and names for the three predefined ranges in each scale. Then, in the Others box, specify the name and color for values that do not fall into any of the defined ranges (to change the color, select the color image and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette) or input the hexadecimal value of a color directly in the text box).
3. In the Border tab, set the border mode for the bubbles, including the border style, color, transparency, line style, thickness, end caps style, and line joint mode. You can also specify whether the border is to be outlined, and whether or not to automatically resize the border dashes if the border is drawn with dashes.

   ![Format Bubble Gauge dialog - Border](https://devnet.logianalytics.com/hc/article_attachments/4404889356311/fmtbublgauge_brdr.gif)
4. In the Data Label tab, set the font formats and effects of the data labels.
5. For a bubble gauge chart in a library component, you can define web behaviors on the bubble gauges in the Behaviors tab.

   ![Format Bubble Gauge dialog - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404893909399/fmtbublgauge_bhvr.gif)

   Select a trigger event from the drop-down list in the Events column, then select in the Actions column and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) that appears in the text box to open the Web Action List dialog, where you can bind a web action to the bubble gauges which will be triggered when the specified event occurs on the bubble gauges. The web actions you can bind include Filter, Sort, Parameter, Property and SendMessage. For details about these web actions, refer to [Applying Web Actions to a Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009584021-Applying-Web-Actions-to-a-Label).

   To add a web behavior line, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif), and if a web behavior is not required, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif) to remove it.

   Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif) to adjust the order of the behaviors. Then, when an event that has been bound with more than one action happens, the upper action will be triggered first.
6. When done, select **OK** to apply the settings.

See the following dialogs for detailed explanation about options in each dialog:

* [Format Dial Gauge (for Report)](https://devnet.logianalytics.com/hc/en-us/articles/1500009587161-Format-Dial-Gauge-Dialog-for-Report-)
* [Format Dial Gauge (for Library Component)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565842-Format-Dial-Gauge-Dialog-for-Library-Component-)
* [Format Bar Gauge (for Report)](https://devnet.logianalytics.com/hc/en-us/articles/1500009587061-Format-Bar-Gauge-Dialog-for-Report-)
* [Format Bar Gauge (for Library Component)](https://devnet.logianalytics.com/hc/en-us/articles/1500009587041-Format-Bar-Gauge-Dialog-for-Library-Component-)
* [Format Bubble Gauge (for Report)](https://devnet.logianalytics.com/hc/en-us/articles/1500009587081-Format-Bubble-Gauge-Dialog-for-Report-)
* [Format Bubble Gauge (for Library Component)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565762-Format-Bubble-Gauge-Dialog-for-Library-Component-)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583601-Formatting-the-Rectangle-Titles)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563202-Formatting-the-Surface)
