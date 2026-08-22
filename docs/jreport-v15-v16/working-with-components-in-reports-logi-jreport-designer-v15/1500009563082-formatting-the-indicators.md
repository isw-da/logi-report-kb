---
title: "Formatting the Indicators"
id: 1500009563082
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009563082-Formatting-the-Indicators
updated_at: 2021-07-24T05:56:08Z
---

# Formatting the Indicators

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563002-Formatting-the-Bubbles)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563022-Formatting-the-Bullets)

# Formatting the Indicators

An indicator chart can be formatted to take some special appearances. To format the indicators in an indicator chart, follow the steps below:

1. Right-click any indicator in the indicator chart and select **Format Indicator**  from the shortcut menu to bring up the Format Indicator dialog.
2. In the General tab, specify the general properties of the indicators.

   In the Option box, set the left margin, top margin, and range radius of the indicators.

   In the Color Range box,

   * For the indicators whose values are of Boolean type, specify the colors from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette) and define the names for the values; if you want to use images to represent the values, check **Show Image**, then specify the images for the values (to specify an image, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) in the image cell, then browse to select the required image in the displayed dialog).

     ![Format Indicator dialog - Boolean - General](https://devnet.logianalytics.com/hc/article_attachments/4404893898263/fmtindctr_gnrl_boln.gif)
   * For the indicators whose values are of String/Numeric type, specify the minimum and maximum values, colors, and names for the value ranges. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif) to add or delete a value range. In the Others box, specify the name and color for values that do not fall into any of the defined ranges (to change the color, select the color image and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette) or input the hexadecimal value of a color directly in the text box). If you want to use images to represent the values, check **Show Image** and specify the image for each value range and the Others value group respectively.

     ![Format Indicator - General String/Numeric](https://devnet.logianalytics.com/hc/article_attachments/4404889349143/fmtindctr_gnrl_numeric.gif)

   Check **Show Category Label** to show the category labels for the indicators, which display the category value each indicator represents.
3. In the Border tab, set the style and border mode for the indicators, including the style, line style, thickness, color, and transparency. All the border options can only take effect when the indicators are represented by colors.

   ![Format Indicator - Border](https://devnet.logianalytics.com/hc/article_attachments/4404889349399/fmtindctr_brdr.gif)
4. In the Data Label tab, set the font formats and effects of the data labels.
5. For an indicator chart in a library component, you can define web behaviors on the indicators in the Behaviors tab.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893899415/fmtindctr_bhvr.gif)

   Select a trigger event from the drop-down list in the Events column, then select in the Actions column and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) that appears in the text box to open the Web Action List dialog, where you can bind a web action to the indicators which will be triggered when the specified event occurs on the indicators. The web actions you can bind include Filter, Sort, Parameter, Property and SendMessage. For details about these web actions, refer to [Applying Web Actions to a Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009584021-Applying-Web-Actions-to-a-Label).

   To add a web behavior line, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif), and if a web behavior is not required, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif) to remove it.

   Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif) to adjust the order of the behaviors. Then, when an event that has been bound with more than one action happens, the upper action will be triggered first.
6. When done, select **OK** to apply the settings.

See also the Format Indicator dialog for [report](https://devnet.logianalytics.com/hc/en-us/articles/1500009587241-Format-Indicator-Dialog-for-Report-) or [library component](https://devnet.logianalytics.com/hc/en-us/articles/1500009587221-Format-Indicator-Dialog-for-Library-Component-) for detailed explanation about options in the dialog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563002-Formatting-the-Bubbles)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563022-Formatting-the-Bullets)
