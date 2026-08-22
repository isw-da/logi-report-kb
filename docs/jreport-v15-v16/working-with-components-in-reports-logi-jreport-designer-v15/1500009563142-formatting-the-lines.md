---
title: "Formatting the Lines"
id: 1500009563142
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009563142-Formatting-the-Lines
updated_at: 2021-07-24T05:56:07Z
---

# Formatting the Lines

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583481-Formatting-the-Bars)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562962-Formatting-the-Areas)

# Formatting the Lines

To format the lines in a line chart, follow the steps below:

1. Right-click any line in the line chart and select **Format 2D Line** or **Format 3D Line** on the shortcut menu to bring up the Format Line dialog.
2. In the General tab, check **Ignore Null Value** if you want the lines to be drawn from the previous data values to the next data values directly when null data values appear to avoid breaks on the lines.
   * For a 2-D line chart, set the layout style of the lines. If you want to add a 3-dimensional effect to the lines, set the Use Depth option to **true** and specify the depth and direction as required. Then check Smoothed Line if you want to make the lines smoothed.

     ![Format Line dialog - General 2-D](https://devnet.logianalytics.com/hc/article_attachments/4404893891863/fmtln_gnrl_1.gif)
   * For a 3-D line chart, set the thickness of the lines.

     ![Format Line dialog - General 3-D](https://devnet.logianalytics.com/hc/article_attachments/4404893892247/fmtln_gnrl_2.gif)
3. In the Fill tab,
   * For a 2-D line chart, specify the fill type of the lines: Use Single Color or Use Single Color with Condition.

     If you select Use Single Color as the fill type, in the Fill box, specify the color and the transparency of the color schema to fill the selected line (to change the color, select the color image and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette) or input the hexadecimal value of a color directly in the text box). You can also select the **Pattern List** button to specify the color pattern for each line in the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009564822-Color-List-Dialog) dialog. In the Area box, set the fill and transparency settings of the area that are formed by the chart axes and the selected line. If required, select **Area Pattern List** to specify the color pattern for each area formed by each line and the chart axes in the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009564822-Color-List-Dialog) dialog. In the Line box, specify the line style and line thickness of the selected line. Select **Line Pattern List** to set the line pattern for each line in the [Line Pattern List](https://devnet.logianalytics.com/hc/en-us/articles/1500009587741-Line-Pattern-List-Dialog) dialog.

     ![Format Line dialog - Fill 2-D](https://devnet.logianalytics.com/hc/article_attachments/4404893892503/fmtln_fill.gif)

     If you select Use Single Color with Condition as the fill type, specify the conditions and the line pattern bound with each condition respectively. For details, refer to [Adding Conditional Color Fill to a Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009583381-Adding-Conditional-Color-Fill-to-a-Chart).
   * For a 3-D line chart, specify the color and the transparency of the color schema to fill the selected line. You can also select the **Color List** button to specify the color pattern for each line.
4. In the Node tab (the tab is available to 2-D lines only), specify the fill type of the nodes: Use Single Color or Use Single Color with Condition.

   If you select Use Single Color as the fill type, in the Shape box, set Show Node to **true**, then specify the style, transparency, width, height and color of the nodes in the selected line, and specify whether or not to display the line nodes in the highest and lowest points with other colors and whether to show the highlight point in a distinguishing color when you hover the mouse over a node in the line. In the Border box, set the border properties of the nodes on the selected line, including border color, transparency, line style and thickness. If you set the node style to plus, multiplication, star1 or star2, the Line box is available instead of the Border box, in which you can specify the line style and thickness for the nodes with selected styles. You can also select the **Node Pattern List** button to specify the node pattern for each line in the [Node Pattern List](https://devnet.logianalytics.com/hc/en-us/articles/1500009566762-Node-Pattern-List-Dialog) dialog.

   ![Format Line dialog - Node](https://devnet.logianalytics.com/hc/article_attachments/4404893892759/fmtln_node.gif)

   If you select Use Single Color with Condition as the fill type, specify the conditions and the node pattern bound with each condition respectively. For details, refer to [Adding Conditional Color Fill to a Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009583381-Adding-Conditional-Color-Fill-to-a-Chart).

   If you want to make the color pattern specified on the nodes apply to the corresponding lines, check **Apply Color to Line**, then the color and transparency settings on the corresponding lines will be ignored.
5. In the Border tab (the tab is available to 3-D lines only), set the border mode of the lines, including the border style, color, transparency, line style, thickness, end caps style, and line joint mode. You can also specify whether the border is to be outlined, and whether or not to automatically resize the border dashes if the border is drawn with dashes.

   ![Format Line - Border](https://devnet.logianalytics.com/hc/article_attachments/4404889346199/fmtln_brdr.gif)
6. In the Data Label tab, specify whether or not to show static data labels for every line node, and if to show, the position of the label related to the node. In the Font and Effects boxes, set the font formats and effects of the data labels.

   ![Format Line - Data](https://devnet.logianalytics.com/hc/article_attachments/4404889346455/fmtln_data.gif)
7. For a line chart in a library component, you can define web behaviors on the lines in the Behaviors tab.

   ![Format Line - Behavior](https://devnet.logianalytics.com/hc/article_attachments/4404893894039/fmtln_bhvr.gif)

   Select a trigger event from the drop-down list in the Events column, then select in the Actions column and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) that appears in the text box to open the Web Action List dialog, where you can bind a web action to the lines which will be triggered when the specified event occurs on the lines. The web actions you can bind include Filter, Sort, Parameter, Property and SendMessage. For details about these web actions, refer to [Applying Web Actions to a Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009584021-Applying-Web-Actions-to-a-Label).

   To add a web behavior line, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif), and if a web behavior is not required, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif) to remove it.

   Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif) to adjust the order of the behaviors. Then, when an event that has been bound with more than one action happens, the upper action will be triggered first.
8. Select **OK** to apply the settings and close the dialog.

See also the Format Line dialog for [page report](https://devnet.logianalytics.com/hc/en-us/articles/1500009587281-Format-Line-Dialog-for-Page-Report-), [web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009565962-Format-Line-Dialog-for-Web-Report-), or [library component](https://devnet.logianalytics.com/hc/en-us/articles/1500009565942-Format-Line-Dialog-for-Library-Component-) for detailed explanation about options in the dialog.

**Notes:**

* If the chart is a combo chart composed by lines and areas/bars, when you set the depth properties for the lines, they will be applied to the areas/bars as well, and vice versa.
* For 3-D charts, the Show Static Data Label checkbox in the Data Label tab is grayed out. However, you can still see the data labels by moving the mouse pointer over the lines when viewing the report result in Designer view mode, in HTML format, or in Page Report Studio.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583481-Formatting-the-Bars)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562962-Formatting-the-Areas)
