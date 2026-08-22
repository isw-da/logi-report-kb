---
title: "Formatting the Lines in a Line Chart"
id: 1500009628721
section: "Working with Components in Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009628721-Formatting-the-Lines-in-a-Line-Chart
updated_at: 2021-07-24T16:05:20Z
---

# Formatting the Lines in a Line Chart

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009628561-Formatting-the-Bars-in-a-Bar-Bench-Chart) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009605722-Formatting-the-Areas-in-an-Area-Chart)

# Formatting the Lines in a Line Chart

This topic introduces how to format the lines in a line chart.

1. Right-click any line in the line chart and select **Format 2D Line** or **Format 3D Line** on the shortcut menu, or double-click any line in the chart. The [Format Line](https://devnet.logianalytics.com/hc/en-us/articles/1500009631481-Format-Line-Dialog) dialog appears.
2. In the General tab, specify whether to draw the lines from the previous data values to the next data values directly when null data values appear to avoid breaks on the lines using the Ignore Null Value checkbox.
   * For a 2-D line chart, set the layout style of the lines. To add a 3-dimensional effect to the lines, set the Use Depth option to **true** and specify the depth and direction as required. Select **Smoothed Line** if you want to make the lines smoothed.

     ![Format Line dialog - General 2-D](https://devnet.logianalytics.com/hc/article_attachments/4404904304535/fmtln_gnrl_1.gif)
   * For a 3-D line chart, set the thickness of the lines.

     ![Format Line dialog - General 3-D](https://devnet.logianalytics.com/hc/article_attachments/4404916793111/fmtln_gnrl_2.gif)
3. In the Fill tab, specify the fill pattern of the chart lines.

   ![Format Line dialog - Fill 2-D](https://devnet.logianalytics.com/hc/article_attachments/4404904304919/fmtln_fill.gif)

   * For a 2-D line chart, specify the fill type of the lines: Use Single Color or Use Single Color with Condition.

     If you select Use Single Color as the fill type, first make a choice for the Self Settings checkbox: when Self Settings is unselected, the color pattern specified here will be synchronized to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#Pattern) on the chart object in the Report Inspector, which can also be applied by data markers of other subtypes if the chart is a combo chart; when Self Settings is selected, it indicates the color pattern is private to the current data markers themselves (the lines in this case), which can be remembered and applied to the data markers of a new type automatically if later you change the type of the chart. Then in the Fill box, specify the color and the transparency of the color schema to fill the current line, that is the line you have selected on to open the Format Line dialog (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box), or select the **Pattern List** button to specify the color pattern for each line in the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009630161-Color-List-Dialog) dialog. In the Area box, set the fill and transparency settings of the area that are formed by the chart axes and the current line, or select **Area Pattern List** to specify the color pattern for each area formed by each line and the chart axes in the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009630161-Color-List-Dialog) dialog. In the Line box, specify the line style and line thickness of the current line, or select **Line Pattern List** to set the line pattern for each line in the [Line Pattern List](https://devnet.logianalytics.com/hc/en-us/articles/1500009609002-Line-Pattern-List-Dialog) dialog.

     If you select Use Single Color with Condition as the fill type, specify the conditions and the line pattern bound with each condition respectively. For details, refer to [Adding Conditional Color Fills to Charts](https://devnet.logianalytics.com/hc/en-us/articles/1500009605602-Applying-Conditional-Color-Fills-to-Charts).
   * For a 3-D line chart, first decide whether or not to select the [Self Setting](#SelfSettings) checkbox, then specify the color and the transparency of the color schema to fill the current line, or select the **Color List** button to specify the color pattern for each line in the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009630161-Color-List-Dialog) dialog.
4. In the Node tab (the tab is available to 2-D lines only), specify the fill type of the nodes: Use Single Color or Use Single Color with Condition.

   ![Format Line dialog - Node](https://devnet.logianalytics.com/hc/article_attachments/4404904305175/fmtln_node.gif)

   If you select Use Single Color as the fill type, first make a choice for the Self Settings checkbox: when Self Settings is unselected, the color pattern specified here will be synchronized to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#Pattern) on the chart object in the Report Inspector, which can also be applied by data markers of other subtypes if the chart is a combo chart; when Self Settings is selected, it indicates the color pattern is private to the current data markers themselves (the line nodes in this case), which can be remembered and applied to the data markers of a new type automatically if later you change the type of the chart. Then in the Shape box, set Show Node to **true** to show nodes in the current line, and then specify the style, transparency, width, height and color of the nodes, and specify whether or not to display the nodes in the highest and lowest points with other colors and whether to show the highlight point in a distinguishing color when you hover the mouse over a node in the line; in the Border box, set the border properties of the nodes in the current line, including border color, transparency, line style and thickness. If you set the node style to plus, multiplication, star1 or star2, the Line box is available instead of the Border box, in which you can specify the line style and thickness for the nodes with selected styles. You can also select the **Node Pattern List** button to specify the node pattern for each line in the [Node Pattern List](https://devnet.logianalytics.com/hc/en-us/articles/1500009632521-Node-Pattern-List-Dialog) dialog.

   If you select Use Single Color with Condition as the fill type, specify the conditions and the node pattern bound with each condition respectively. For details, refer to [Adding Conditional Color Fills to Charts](https://devnet.logianalytics.com/hc/en-us/articles/1500009605602-Applying-Conditional-Color-Fills-to-Charts).

   If you want to make the color pattern specified on the nodes apply to the corresponding lines, select **Apply Color to Line**, then the color and transparency settings on the corresponding lines will be ignored.
5. In the Border tab (the tab is available to 3-D lines only), select **Show Border** if you want to show the border of the lines, then set properties of the border including the border color, transparency, line style, thickness, end caps style, and line joint mode. You can also specify whether the border is to be outlined, and whether or not to automatically resize the border dashes if the border is drawn with dashes.

   ![Format Line - Border](https://devnet.logianalytics.com/hc/article_attachments/4404904305431/fmtln_brdr.gif)
6. In the Data Label tab, select **Show Static Data Label** if you want to show static data labels on the line nodes, then decide the position of the labels related to the nodes, the display type for data values in the labels, whether to scale big and small numbers, and whether to hide the label whose value is 0. In the Font and Effects boxes, set the font formats and effects of the data labels.

   ![Format Line dialog - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4404904305687/fmtln_data.gif)
7. In the Hint tab, specify whether to
   include the category and series values and whether to scale big and small numbers in the line hint. A hint displays the value a line node represents when the mouse pointer points at the node in Logi Report Designer view mode, in HTML result, or at server runtime. To make the hint shown, you need to make sure the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/1500009612142-Chart-Paper-Properties#ShowTips) property in the Report Inspector is set to true.

   ![Format Line - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404904306071/fmtln_hint.gif)
8. For a line chart in a library component, you can define web behaviors on the lines in the Behaviors tab.

   ![Format Line dialog for library component - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404904306583/fmtln_bhvr.gif)

   Select a [trigger event](https://devnet.logianalytics.com/hc/en-us/articles/1500009629441-Using-Basic-Web-Controls-in-a-Report#Event) from the drop-down list in the Events column, then select in the Actions column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) that appears in the text box. In the Web Action List dialog, bind a web action to the lines [the same as you do to web controls](https://devnet.logianalytics.com/hc/en-us/articles/1500009629441-Using-Basic-Web-Controls-in-a-Report#Action) in the library component, which will be triggered when the specified event occurs on the lines. The web actions you can bind include Parameter, Filter, Sort, Change Property and Send Message.

   To add more web behaviors, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) and define them as required; if a web behavior is not required, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif). Select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif) to adjust the order of the behaviors, then at runtime when an event that has been bound with more than one action happens, the upper action will be triggered first.
9. Select **OK** to apply the settings and close the dialog.

**Notes:**

* If the chart is a combo chart composed by lines and areas/bars, when you set the depth properties for the lines, they will be applied to the areas/bars as well, and vice versa.
* For 3-D charts, the Show Static Data Label checkbox in the Data Label tab is grayed out. However, you can still see the data labels by moving the mouse pointer over the lines when viewing the report result in Designer view mode, in HTML format, or in Page Report Studio.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009628561-Formatting-the-Bars-in-a-Bar-Bench-Chart) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009605722-Formatting-the-Areas-in-an-Area-Chart)
