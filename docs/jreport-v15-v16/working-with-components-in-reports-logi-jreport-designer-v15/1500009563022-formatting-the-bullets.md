---
title: "Formatting the Bullets"
id: 1500009563022
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009563022-Formatting-the-Bullets
updated_at: 2021-07-24T05:56:08Z
---

# Formatting the Bullets

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563082-Formatting-the-Indicators)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563182-Formatting-the-Rectangles)

# Formatting the Bullets

To format the bullets in a bullet chart, follow the steps below:

1. Right-click any bullet in the bullet chart, and then select **Format Bullet** from the shortcut menu to bring up the Format Bullet dialog.

   ![Format Bullet - General](https://devnet.logianalytics.com/hc/article_attachments/4404893907351/fmtbult_gnrl.gif)
2. In the General tab, specify the size of the bullets by setting the width of the featured measure, comparative measure and qualitative ranges respectively.
3. In the Fill tab, specify the fill properties of the bullets.

   ![Format Bullet - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404893907607/fmtbult_fill.gif)

   * In the Featured Measure Color List box, specify the color and the transparency of the color schema to fill all the featured measures (to change the color, select the color image and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette) or input the hexadecimal value of a color directly in the text box). If you want to make the featured measure colors vary, check **Vary Colors by Color List**, then select the **Color List** button to specify the color pattern for each featured measure in the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009564822-Color-List-Dialog) dialog.
   * In the Comparative Measure Color List, specify the color and the transparency of the color schema to fill the selected comparative measures in the same data series. Select the **Color List** button to specify the color pattern for comparative measures in the same data series respectively if needed.
   * In the Qualitative Ranges Color List box, specify the color and the transparency of the color schema to fill the selected qualitative ranges in the same data series. Select the **Color List** button to specify the color pattern for qualitative ranges in the same data series respectively if necessary.
4. In the Border tab, set the border mode for the bullets, including the border style, color, transparency, line style, thickness, end caps style, and line joint mode. You can also specify whether the border is to be outlined, and whether or not to automatically resize the border dashes if the border is drawn with dashes.

   ![Format Bullet - Border](https://devnet.logianalytics.com/hc/article_attachments/4404889355031/fmtbult_border.gif)
5. In the Data Label tab, specify the font formats and effects of the data labels.
6. For a bullet chart in a library component, you can define web behaviors on the bullets in the Behaviors tab.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889355799/fmtbult_bhvr.gif)

   Select a trigger event from the drop-down list in the Events column, then select in the Actions column and select ![Chosse button](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) that appears in the text box to open the Web Action List dialog, where you can bind a web action to the bullets which will be triggered when the specified event occurs on the bullets. The web actions you can bind include Filter, Sort, Parameter, Property and SendMessage. For details about these web actions, refer to [Applying Web Actions to a Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009584021-Applying-Web-Actions-to-a-Label).

   To add a web behavior line, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif), and if a web behavior is not required, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif) to remove it.

   Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif) to adjust the order of the behaviors. Then, when an event that has been bound with more than one action happens, the upper action will be triggered first.
7. When done, select **OK** to accept the changes and close the dialog.

See also the Format Bullet dialog for [report](https://devnet.logianalytics.com/hc/en-us/articles/1500009565782-Format-Bullet-Dialog-for-Report-) or [library component](https://devnet.logianalytics.com/hc/en-us/articles/1500009587101-Format-Bullet-Dialog-for-Library-Component-) for detailed explanation about options in the dialog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563082-Formatting-the-Indicators)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563182-Formatting-the-Rectangles)
