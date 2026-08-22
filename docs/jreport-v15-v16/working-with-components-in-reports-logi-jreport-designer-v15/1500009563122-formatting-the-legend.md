---
title: "Formatting the Legend"
id: 1500009563122
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009563122-Formatting-the-Legend
updated_at: 2021-07-24T05:56:07Z
---

# Formatting the Legend

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583541-Formatting-the-Paper)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562982-Formatting-the-Axes)

# Formatting the Legend

The chart legend is a box to identify the patterns or colors assigned to the data categories in a chart. A chart legend may contain one or more legend entries, and each entry is composed of a mark and a label. You can show or hide the legend by right-clicking the chart and then selecting Show/Hide legend form the shortcut menu. An indicator chart whose values are represented by images and an organization chart does not have the legend.

**To format the legend of a chart:**

1. Right-click any chart element and select **Format Legend** from the shortcut menu to bring up the Format Legend dialog.

   ![Format Legend dialog - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404893894295/fmtlgnd_fill.gif)
2. In the Fill tab, set the color and transparency of the color for the legend (to change the color, select the color image and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette) or input the hexadecimal value of a color directly in the text box).
3. In the Border tab, set the border mode for the legend, including the border style, color, transparency, line style, thickness, end caps style, and line joint mode, and if you specify the line joint mode to be joint round, you can set the the radius for the border joint. You can also specify whether the border is to be outlined, and whether or not to automatically resize the border dashes if the border is drawn with dashes.

   ![Format Legegnd dialog - Border](https://devnet.logianalytics.com/hc/article_attachments/4404889347351/fmtlgnd_border.gif)
4. In the Placement tab, specify the way in which the legend will be placed.

   ![Format Legegnd dialog - Placement](https://devnet.logianalytics.com/hc/article_attachments/4404893894551/fmtlgnd_plcmnt.gif)

   In the Position box, specify whether the legend will be placed at the left, right, top, or bottom of the chart, and then set the alignment style accordingly in the Alignment box. If Auto is selected, the legend will be placed somewhere automatically.

   In the Legend-Label Gap box, specify the vertical and horizontal margins between the legend entries and the legend boundaries, and the vertical and horizontal spacing between legend entry labels.

   Check **Reverse Legend** if you want to have the legend entries re-arranged in a reverse order.

   Check **Show Scrollbar** if you want to show the legend scrollbar to fully view the legend content when the content does not fit into the legend.

   Check **Truncate** if you want to truncate the legend entry label text when the text overflow the labels.

   **Tip:** Often it is easier to select the legend and use the grab handles to resize and move the legend as needed anywhere on the chart.
5. In the Font tab, specify the font formats of the legend entry labels, including the font face, size, color, transparency, rotation angle, shearing angle, and effects such as style, strikeout, underline and so on (to change the color, select the color image and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette) or input the hexadecimal value of a color directly in the text box).

   ![Format Legend dialog - Font](https://devnet.logianalytics.com/hc/article_attachments/4404893894807/fmtlgnd_font.gif)
6. In the Orientation tab, set an angle for legend entry labels so as to rotate them. You can either drag the Text hand in the Orientation box or type a value in the Angle spinner to set the angle.

   ![Format Legend dialog - Orientation](https://devnet.logianalytics.com/hc/article_attachments/4404893895063/fmtlgnd_orntatn.gif)
7. In the Format tab, specify the data format of the legend entry labels. However, the settings in this tab take effect only when the property [Label Format Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009569482-Properties-of-Chart-Legend-in-Page-Report#LabelFormatSource) of the chart legend in the Report Inspector has been set to Legend Label Format.

   ![Format Legend dialog - Format](https://devnet.logianalytics.com/hc/article_attachments/4404889347607/fmtlgnd_fmt.gif)

   Select a category from the Category box, then select a format from the Format box and select **Add** to add it to the Stack box. You can add more than one format, and in the event that one of the formats is not necessary, you can clear it by selecting Remove.
8. In the Mark tab, specify the options for the legend entry marks.

   ![Format Legend dialog - Mark](https://devnet.logianalytics.com/hc/article_attachments/4404893895319/fmtlgnd_mark.gif)

   * By default, Customize is checked, which enables you to customize the format of the legend entry marks.

     Logi JReport Designer uses 16 styles for the marks by default. To add a style, select a mark item from the Mark Items drop-down list, and then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) to add it to the Mark Items box. The legend marks will repeat within the mark items you have defined. If you have defined more mark items than the actual legend marks, the redundant mark items will be ignored. You can select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif), ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif), or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif) to remove a mark item, or to arrange the order of the these items.

     To change the style of a mark item, select it in the Mark Items box and then choose a new one from the Mark Items drop-down list.

     In the Icon box, specify the horizontal and vertical alignment styles, and the gap between each entry mark and entry label. You can also set the width and height for the legend entry marks.

     In the Border box, set the color, style, thickness and transparency properties of the icon border.
   * For a line chart, you can also check Use Node as Mark or Use Line and Node as Mark to apply the style and color of the line nodes or lines and line nodes automatically to the legend entry marks. When either of these two is checked, you can also specify the properties of icons in the Icon box.
9. For a chart in a library component, you can define web behaviors on its legend in the Behaviors tab.

   ![Format Legend dialog - Behavior](https://devnet.logianalytics.com/hc/article_attachments/4404889348375/fmtlgnd_bhvr.gif)

   Select a trigger event from the drop-down list in the Events column, then select in the Actions column and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) that appears in the text box to open the Web Action List dialog, where you can bind a web action to the legend which will be triggered when the specified event occurs on the legend. The web actions you can bind include Filter, Sort, Parameter, Property and SendMessage. For details about these web actions, refer to [Applying Web Actions to a Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009584021-Applying-Web-Actions-to-a-Label).

   To add a web behavior line, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif), and if a web behavior is not required, select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif) to remove it.

   Select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif) to adjust the order of the behaviors. Then, when an event that has been bound with more than one action happens, the upper action will be triggered first.
10. When done, select **OK** to apply the settings and close the dialog.

See also the Format Legend dialog for [page report](https://devnet.logianalytics.com/hc/en-us/articles/1500009565922-Format-Legend-Dialog-for-Page-Report-), [web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009565902-Format-Legend-Dialog-for-Web-Report-), or [library component](https://devnet.logianalytics.com/hc/en-us/articles/1500009587261-Format-Legend-Dialog-for-Library-Component-) for detailed explanation about options in the dialog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583541-Formatting-the-Paper)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562982-Formatting-the-Axes)
