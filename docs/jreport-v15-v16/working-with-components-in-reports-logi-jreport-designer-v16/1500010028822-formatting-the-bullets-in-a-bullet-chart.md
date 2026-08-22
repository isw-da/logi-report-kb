---
title: "Formatting the Bullets in a Bullet Chart"
id: 1500010028822
section: "Working with Components in Reports - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010028822-Formatting-the-Bullets-in-a-Bullet-Chart
updated_at: 2021-07-24T10:39:27Z
---

# Formatting the Bullets in a Bullet Chart

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010063441-Formatting-the-Indicators-in-an-Indicator-Chart) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010063561-Formatting-the-Rectangles-and-Rectangle-Titles-in-a-Heat-Map)

# Formatting the Bullets in a Bullet Chart

This topic introduces how to format the bullets in a bullet chart.

1. Right-click any bullet in the bullet chart and select **Format Bullet** from the shortcut menu, or double-click any bullet in the chart. The [Format Bullet](https://devnet.logianalytics.com/hc/en-us/articles/1500010030882-Format-Bullet-Dialog) dialog appears.

   ![Format Bullet dialog - General](https://devnet.logianalytics.com/hc/article_attachments/4404901250327/fmtbult_gnrl.gif)
2. In the General tab, specify the size of the bullets by setting the width of the featured measure, comparative measure and qualitative ranges respectively.
3. In the Fill tab, set the color pattern to fill the bullets.

   ![Format Bullet dialog - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404901250967/fmtbult_fill.gif)

   In the Featured Measure Color List box, first decide whether to define the color pattern on the featured measures themselves by using the Self Settings checkbox. When Self Settings is unchecked, the color settings specified here will be synchronized to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500010069721-Chart-Properties#Pattern) on the chart object in the Report Inspector, which can also be applied by data markers of other subtypes if the chart is a combo chart. Then specify the color and the transparency of the color schema to fill all the featured measures (to change the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010035022-Menu-Tabs#Palette) or input the hexadecimal value of a color directly in the text box). If you want to make the featured measure colors vary, check **Vary Colors by Color List**, then select the **Color List** button to specify the color pattern for each featured measure in the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500010030022-Color-List-Dialog) dialog.

   In the Comparative Measure Color List, specify the color and the transparency of the color schema to fill the selected comparative measures in the same data series, or select the **Color List** button to specify the color pattern for comparative measures in the same data series respectively.

   In the Qualitative Ranges Color List box, specify the color and the transparency of the color schema to fill the selected qualitative ranges in the same data series, or select the **Color List** button to specify the color pattern for qualitative ranges in the same data series respectively.
4. In the Border tab, check **Show Border** if you want to show the border of the bullets, then set properties of the border including the border color, transparency, line style, thickness, end caps style, and line joint mode. You can also specify whether the border is to be outlined, and whether or not to automatically resize the border dashes if the border is drawn with dashes.

   ![Format Bullet dialog - Border](https://devnet.logianalytics.com/hc/article_attachments/4404909215767/fmtbult_border.gif)
5. Skip the Data Label tab since data labels are not supported on bullet chart.
6. In the Hint tab, specify whether to
   include the category and series values and whether to scale big and small numbers in the bullet hint. A hint displays the value a bullet represents when the mouse pointer points at the bullet in Logi JReport Designer view mode, in HTML result, or at server runtime. To make the hint shown, you need to make sure the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/1500010033982-Chart-Paper-Properties#ShowTips) property in the Report Inspector is set to true.

   ![Format Bullet - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404901252503/fmtbult_hint.gif)
7. For a bullet chart in a library component, you can define web behaviors on the bullets in the Behaviors tab.

   ![Format Bullet dialog for library component - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404909216023/fmtbult_bhvr.gif)

   Select a [trigger event](https://devnet.logianalytics.com/hc/en-us/articles/1500010029382-Using-Basic-Web-Controls-in-a-Report#Event) from the drop-down list in the Events column, then select in the Actions column and select ![Chosse button](https://devnet.logianalytics.com/hc/article_attachments/4404909121559/btn_chsr1.gif) that appears in the text box. In the Web Action List dialog, bind a web action to the bullets [the same as you do to web controls](https://devnet.logianalytics.com/hc/en-us/articles/1500010029382-Using-Basic-Web-Controls-in-a-Report#Action) in the library component, which will be triggered when the specified event occurs on the bullets. The web actions you can bind include Parameter, Filter, Sort, Change Property and Send Message.

   To add more web behaviors, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif) and define them as required; if a web behavior is not required, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif). Select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif) to adjust the order of the behaviors, then at runtime when an event that has been bound with more than one action happens, the upper action will be triggered first.
8. Select **OK** to accept the changes and close the dialog.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010063441-Formatting-the-Indicators-in-an-Indicator-Chart) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010063561-Formatting-the-Rectangles-and-Rectangle-Titles-in-a-Heat-Map)
