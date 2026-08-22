---
title: "Formatting the Rectangles"
id: 1500009563182
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009563182-Formatting-the-Rectangles
updated_at: 2021-07-24T05:56:06Z
---

# Formatting the Rectangles

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563022-Formatting-the-Bullets)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583601-Formatting-the-Rectangle-Titles)

# Formatting the Rectangles

To format the rectangles in a heat map, follow the steps below:

1. When there is only one group in the heat map, right-click on the heat map and select **Format Rectangle** from the shortcut menu to bring up the Format Rectangle dialog.

   When there are two or more groups in the heat map, right-click on the heat map, then from the Format Rectangle submenu, select a desired group field to bring up the Format Rectangle dialog for the field.
2. In the Fill tab, specify the fill type: Use Single Color, or Use Single Color with Condition.

   If you select Use Single Color as the fill type,

   * When the heat map is colored by one of the following cases: no field, 1 to n groups, 1 to n groups and 1 summary, specify the color and the transparency of the color schema to fill the selected rectangle (to change the color, select the color image and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette) or input the hexadecimal value of a color directly in the text box). If you want to make the rectangle colors vary, check **Vary Colors by Color List**, then select the **Color List** button to specify the color pattern for each rectangle in the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009564822-Color-List-Dialog) dialog.

     ![Format Rectangle - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404889423511/cmpnt_cht_frmt_rctgl1.gif)
   * When the heat map is colored by a summary, specify the start color for the minimum value and the end color for the maximum value. To exchange the start color and the end color, check the **Reversed** option. If you want to specify a color for the zero value, check **Color When Zero** and then define the color, then the gradient color will change from the start color to the zero value color, and then from the zero value color to the end color. You can also specify a color for the null values.

     ![Format Rectangle - Fill of color by a summary](https://devnet.logianalytics.com/hc/article_attachments/4404894002583/cmpnt_cht_frmt_rctgl2.gif)

   If you select Use Single Color with Condition as the fill type, specify the conditions and the color pattern bound with each condition respectively. For details, refer to [Adding Conditional Color Fill to a Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009583381-Adding-Conditional-Color-Fill-to-a-Chart).
3. In the Separator tab, specify the color, transparency, line style, and thickness of the rectangle separators.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889343127/fmtrctgl_sprtr.gif)
4. For a heat map chart in a library component, you can define web behaviors on the rectangles in the Behaviors tab.

   ![Format Rectangle - Behavior](https://devnet.logianalytics.com/hc/article_attachments/4404889343895/fmtrctgl_bhvr.gif)

   Select a trigger event from the drop-down list in the Events column, then select in the Actions column and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) that appears in the text box to open the Web Action List dialog, where you can bind a web action to the rectangles which will be triggered when the specified event occurs on the rectangles. The web actions you can bind include Filter, Sort, Parameter, Property and SendMessage. For details about these web actions, refer to [Applying Web Actions to a Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009584021-Applying-Web-Actions-to-a-Label).

   To add a web behavior line, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif), and if a web behavior is not required, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif) to remove it.

   Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif) to adjust the order of the behaviors. Then, when an event that has been bound with more than one action happens, the upper action will be triggered first.
5. When done, select **OK** to apply the settings and close the dialog.

See also the Format Rectangle dialog for [report](https://devnet.logianalytics.com/hc/en-us/articles/1500009587381-Format-Rectangle-Dialog-for-Report-) or [library component](https://devnet.logianalytics.com/hc/en-us/articles/1500009587341-Format-Rectangle-Dialog-for-Library-Component-) for detailed explanation about options in the dialog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563022-Formatting-the-Bullets)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583601-Formatting-the-Rectangle-Titles)
