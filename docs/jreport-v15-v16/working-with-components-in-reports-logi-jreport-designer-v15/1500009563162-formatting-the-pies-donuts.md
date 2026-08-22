---
title: "Formatting the Pies/Donuts"
id: 1500009563162
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009563162-Formatting-the-Pies-Donuts
updated_at: 2021-07-24T05:56:07Z
---

# Formatting the Pies/Donuts

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562962-Formatting-the-Areas)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563002-Formatting-the-Bubbles)

# Formatting the Pies/Donuts

To format the pies/donuts of a pie/donut chart, follow the steps below:

1. Right-click any portion of a pie/donut in the pie/donut chart, and then select **Format Pie**/**Donut** on the shortcut menu to bring up the Format Pie/Donut dialog.

   ![Format Pie dialog - General](https://devnet.logianalytics.com/hc/article_attachments/4404893888279/fmtpie_gnrl.gif)
2. In the General tab, set the general settings for the pies/donuts.

   In the Gap Amount field, enter a number to set the distance between every two adjacent pies/donuts. In the Explode Amount field, enter a number to specify the distance between the sections in each pie/donut and the pie/donut center. In the Data Label Type field, specify the type of the data labels for the pie/donut sections. For a donut chart, you can also specify the radius percentage of the donut hole to the total pie circle by setting the option Donut Hole.
3. In the Fill tab, specify the fill type: Use Single Color or Use Single Color with Condition.

   If you select Use Single Color as the fill type, specify the color and the transparency of the color schema to fill the selected sections in the same data series (to change the color, select the color image and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette) or input the hexadecimal value of a color directly in the text box). If required, select the **Color List** button to specify the color pattern for sections in the same data series respectively in the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009564822-Color-List-Dialog) dialog.

   ![Format Pie dialog - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404889344919/fmtpie_fill.gif)

   If you select Use Single Color with Condition, specify the conditions and the color pattern bound with each condition respectively. For details, refer to [Adding Conditional Color Fill to a Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009583381-Adding-Conditional-Color-Fill-to-a-Chart).
4. In the Border tab, set the border mode for the sections, including the border style, color, transparency, line style, thickness, end caps style, and line joint mode. You can also specify whether the border is to be outlined, and whether or not to automatically resize the border dashes if the border is drawn with dashes.

   ![Format Pie dialog - Border](https://devnet.logianalytics.com/hc/article_attachments/4404889345175/fmtpie_border.gif)
5. In the Data Label tab, specify whether or not to show static data labels for every section, and if to show, the position of the label related to the section and the color of the thin lines that are used to point to the static data labels. In the Font and Effects boxes, set the font formats and effects of the data labels.

   ![Format Pie dialog - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4404889345431/fmtpie_data.gif)
6. For a pie/donut chart in a library component, you can define web behaviors on the pies/donuts in the Behaviors tab.

   ![Format Pie dialog - Behavior](https://devnet.logianalytics.com/hc/article_attachments/4404893889559/fmtpie_bhvr.gif)

   Select a trigger event from the drop-down list in the Events column, then select in the Actions column and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) that appears in the text box to open the Web Action List dialog, where you can bind a web action to the pies/donuts which will be triggered when the specified event occurs on the pies/donuts. The web actions you can bind include Filter, Sort, Parameter, Property and SendMessage. For details about these web actions, refer to [Applying Web Actions to a Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009584021-Applying-Web-Actions-to-a-Label).

   To add a web behavior line, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif), and if a web behavior is not required, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif) to remove it.

   Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif) to adjust the order of the behaviors. Then, when an event that has been bound with more than one action happens, the upper action will be triggered first.
7. When done, select **OK** to apply the settings and close the dialog.

See the following dialogs for detailed explanation about options in each dialog:

* [Format Pie (for Report)](https://devnet.logianalytics.com/hc/en-us/articles/1500009566002-Format-Pie-Dialog-for-Report-)
* [Format Pie (for Library Component)](https://devnet.logianalytics.com/hc/en-us/articles/1500009587301-Format-Pie-Dialog-for-Library-Component-)
* [Format Donut (for Report)](https://devnet.logianalytics.com/hc/en-us/articles/1500009587181-Format-Donut-Dialog-for-Report-)
* [Format Donut (for Library Component)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565862-Format-Donut-Dialog-for-Library-Component-)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562962-Formatting-the-Areas)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563002-Formatting-the-Bubbles)
