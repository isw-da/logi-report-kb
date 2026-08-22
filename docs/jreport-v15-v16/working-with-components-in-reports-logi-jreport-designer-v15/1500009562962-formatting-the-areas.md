---
title: "Formatting the Areas"
id: 1500009562962
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009562962-Formatting-the-Areas
updated_at: 2021-07-24T05:56:10Z
---

# Formatting the Areas

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563142-Formatting-the-Lines)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563162-Formatting-the-Pies-Donuts)

# Formatting the Areas

To format the area of an area chart, follow the steps below:

1. Right-click any area in the area chart and select **Format 2D Area** or **Format 3D Area** on the shortcut menu to bring up the Format Area dialog.

   ![Format Area dialog - General](https://devnet.logianalytics.com/hc/article_attachments/4404893915159/fmtarea_gnrl_1.gif)
2. In the General tab, set the layout style of the area chart. Check **Ignore Null Value** if you want the areas to be drawn from the previous data values to the next data values directly when null data values appear to avoid breaks on the areas.

   For a 2-D area chart, if you want to add a 3-dimensional effect to the areas, set the Use Depth option to **true** and specify the depth and direction as required. You can also set to show the lines that represent the data categories by checking High-Low Lines.
3. In the Fill tab, specify the fill type: Use Single Color or Use Multiple Colors with Condition.

   If you select Use Single Color as the fill type, specify the color and the transparency of the color schema to fill the selected area (to change the color, select the color image and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette) or input the hexadecimal value of a color directly in the text box). If required, select the **Color List** button to specify the color pattern for each area in the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009564822-Color-List-Dialog) dialog.

   ![Format Area dialog - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404889359511/fmtarea_fill.gif)

   If you select Use Multiple Colors with Condition as the fill type (only applied to Area 2-D and Area 3-D types), specify the conditions and the color pattern bound with each condition respectively. For details, refer to [Adding Conditional Color Fill to a Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009583381-Adding-Conditional-Color-Fill-to-a-Chart).
4. In the Border tab, set the border mode for the areas, including the border style, color, transparency, line style, thickness, end caps style, and line joint mode. You can also specify whether the border is to be outlined, and whether or not to automatically resize the border dashes if the border is drawn with dashes.

   ![Format Area dialog - Border](https://devnet.logianalytics.com/hc/article_attachments/4404889359767/fmtarea_border.gif)
5. In the Data Label tab, specify whether or not to show static data labels for every area node, and if to show, the position of the label related to the area node. In the Font and Effects boxes, set the font formats and effects of the data labels.

   ![Format Area dialog - Data](https://devnet.logianalytics.com/hc/article_attachments/4404893915799/fmtarea_data.gif)
6. For an area chart in a library component, you can define web behaviors on the areas in the Behaviors tab.

   ![Format Area dialog - Behavior](https://devnet.logianalytics.com/hc/article_attachments/4404893916695/fmtarea_bhvr.gif)

   Select a trigger event from the drop-down list in the Events column, then select in the Actions column and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) that appears in the text box to open the Web Action List dialog, where you can bind a web action to the areas which will be triggered when the specified event occurs on the areas. The web actions you can bind include Filter, Sort, Parameter, Property and SendMessage. For details about these web actions, refer to [Applying Web Actions to a Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009584021-Applying-Web-Actions-to-a-Label).

   To add a web behavior line, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif), and if a web behavior is not required, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif) to remove it.

   Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif) to adjust the order of the behaviors. Then, when an event that has been bound with more than one action happens, the upper action will be triggered first.
7. When done, select **OK** to apply the settings and close the dialog.

See also the Format Area dialog for [page report](https://devnet.logianalytics.com/hc/en-us/articles/1500009587001-Format-Area-Dialog-for-Page-Report-), [web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009586981-Format-Area-Dialog-for-Web-Report-), or [library component](https://devnet.logianalytics.com/hc/en-us/articles/1500009565682-Format-Area-Dialog-for-Library-Component-) for detailed explanation about options in the dialog.

**Notes:**

* If the chart is a combo chart composed by areas and bars/lines, when you set the depth properties for the areas, they will be applied to the bars/lines as well, and vice versa.
* For 3-D charts, the Show Static Data Label checkbox in the Data Label tab is grayed out. However, you can still see the data labels by moving the mouse pointer over the areas when viewing the report result in Designer view mode, in HTML format, or in Page Report Studio.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563142-Formatting-the-Lines)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563162-Formatting-the-Pies-Donuts)
