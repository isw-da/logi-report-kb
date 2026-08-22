---
title: "Formatting the Indicators in an Indicator Chart"
id: 1500009605842
section: "Working with Components in Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009605842-Formatting-the-Indicators-in-an-Indicator-Chart
updated_at: 2021-07-24T16:05:21Z
---

# Formatting the Indicators in an Indicator Chart

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009605782-Formatting-the-Bubbles-in-a-Bubble-Chart) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009605802-Formatting-the-Bullets-in-a-Bullet-Chart)

# Formatting the Indicators in an Indicator Chart

This topic introduces how to format the indicators in an indicator chart.

1. Right-click any indicator in the indicator chart and select **Format Indicator**  from the shortcut menu, or double-click any indicator in the chart. The [Format Indicator](https://devnet.logianalytics.com/hc/en-us/articles/1500009631401-Format-Indicator-Dialog) dialog appears.
2. In the General tab, specify the general properties of the indicators.

   ![Format Indicator dialog - General](https://devnet.logianalytics.com/hc/article_attachments/4404916798359/fmtindctr_gnrl.gif)

   In the Style box, specify to use an indicator or multiple indicators to show each value in the chart.

   In the Option box, set the left margin, top margin, range radius and the shape of the indicators, and how to fill the indicators. You can specify to fill the whole indictor or portion of the indicators calculated based on the the maximum value in the Value box. When a value in the chart is less than the minimum value, the indicator will not be filled. When a value in the chart is greater than the minimum value, the value divided by the maximum value you specify will be the portion to be filled.

   In the Border box, select **Show Border** if you want to show the border of the indicators, then set properties of the border including the line style, the thickness, the color and transparency.

   In the Value box, set the maximum and minimum values displayed on the chart. The default value is Auto, which means using the actual minimum and maximum values in the chart. You can also specify the values by yourself. Not available when the value of the indicator chart is Boolean or String type.

   In the Value Label box, specify whether to show the values of the indicators, the position relationship of the values and the indicators, and whether to scale big and small numbers in the values.
3. In the Frame tab, specify the properties for the frame of the indicator chart.

   ![Format Indicator dialog - Frame](https://devnet.logianalytics.com/hc/article_attachments/4404916798615/fmtindctr_frm.gif)

   In the Size box, specify the size of the frame.

   In the Fill box, specify the color and the transparency of the color to fill the frame.

   In the Border box, specify the properties for borders of the frame, including the type, color, line style, transparency, thickness, ending style, line joint style, fill pattern and dash size.

   In the Category Label box, select **Show Category Label** to show the category labels for the indicators, which display the category value each indicator represents, and the position relationship of the labels and the indicators.
4. In the Range Color tab, specify different colors or images to fill the indicators.
   * For the indicators whose values are of Boolean type, specify the colors from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette) and define the names for the values; if you want to use images to represent the values, select **Show Image**, then specify the images for the values (to specify an image, select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) in the image cell, then browse to select the required image in the displayed dialog).

     ![Format Indicator dialog - Range Color tabs for Boolean Type Values](https://devnet.logianalytics.com/hc/article_attachments/4404904313623/fmtindctr_range_boln.gif)
   * For the indicators whose values are of String/Numeric type, specify the minimum and maximum values, colors, and names for the value ranges. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) or ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif) to add or delete a value range. In the Others box, specify the name and color for values that do not fall into any of the defined ranges (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box). If you want to use images to represent the values, select **Show Image** and specify the image for each value range and the Others value group respectively.

     ![Format Indicator dialog - Range Color tab for String/Numeric Type Values](https://devnet.logianalytics.com/hc/article_attachments/4404904313879/fmtindctr_range_num.gif)
5. In the Hint tab, specify whether to
   include the category and series values and whether to scale big and small numbers in the indicator hint. A hint displays the value an indicator in the indicator chart represents when the mouse pointer points at the indicator in Logi Report Designer view mode, in HTML result, or at server runtime. To make the hint shown, you need to make sure the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/1500009612142-Chart-Paper-Properties#ShowTips) property in the Report Inspector is set to true.

   ![Format Indicator - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404904314775/fmtindctr_hint.gif)
6. For an indicator chart in a library component, you can define web behaviors on the indicators in the Behaviors tab.

   ![Format Indicator dialog for library component - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404904315927/fmtindctr_bhvr.gif)

   Select a [trigger event](https://devnet.logianalytics.com/hc/en-us/articles/1500009629441-Using-Basic-Web-Controls-in-a-Report#Event) from the drop-down list in the Events column, then select in the Actions column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) that appears in the text box. In the Web Action List dialog, bind a web action to the indicators [the same as you do to web controls](https://devnet.logianalytics.com/hc/en-us/articles/1500009629441-Using-Basic-Web-Controls-in-a-Report#Action) in the library component, which will be triggered when the specified event occurs on the indicators. The web actions you can bind include Parameter, Filter, Sort, Change Property and Send Message.

   To add more web behaviors, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) and define them as required; if a web behavior is not required, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif). Select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif) to adjust the order of the behaviors, then at runtime when an event that has been bound with more than one action happens, the upper action will be triggered first.
7. Select **OK** to accept the changes and close the dialog.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009605782-Formatting-the-Bubbles-in-a-Bubble-Chart) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009605802-Formatting-the-Bullets-in-a-Bullet-Chart)
