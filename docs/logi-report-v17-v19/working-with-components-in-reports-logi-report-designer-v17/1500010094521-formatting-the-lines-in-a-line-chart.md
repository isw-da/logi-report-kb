---
title: "Formatting the Lines in a Line Chart"
id: 1500010094521
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010094521-Formatting-the-Lines-in-a-Line-Chart
updated_at: 2021-07-23T19:14:40Z
---

# Formatting the Lines in a Line Chart

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094461-Formatting-the-Bars-in-a-Bar-Bench-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094421-Formatting-the-Areas-in-an-Area-Chart)

# Formatting the Lines in a Line Chart

This topic describes how you can format the lines in a line chart.

1. Right-click any line in the line chart and select **Format 2D Line** or **Format 3D Line** on the shortcut menu, or double-click any line in the chart. Designer displays the [Format Line dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059242-Format-Line-Dialog-Box).
2. In the **General** tab, specify the general properties of the lines.
   * For a 2-D line chart, set the layout style of the lines. To add a 3-dimensional effect to the lines, set the **Use Depth** option to **true** and then specify the depth and direction. Select **Ignore Null Value** to draw the lines from the previous data values to the next data values directly when null data values appear to avoid breaks on the lines. Select **Smoothed Line** if you want to draw the lines smoothly without the sharp joints.

     ![Format Line dialog box - General 2-D](https://devnet.logianalytics.com/hc/article_attachments/4404848546839/fmtln_gnrl_1.gif)
   * For a 3-D line chart, specify the thickness of the lines, and select **Ignore Null Value** to draw the lines from the previous data values to the next data values directly when null data values appear to avoid breaks on the lines.

     ![Format Line dialog box - General 3-D](https://devnet.logianalytics.com/hc/article_attachments/4404848547095/fmtln_gnrl_2.gif)
3. In the **Fill** tab, specify the fill type and the color pattern to fill the chart lines.

   ![Format Line dialog box - Fill 2-D](https://devnet.logianalytics.com/hc/article_attachments/4404856944535/fmtln_fill.gif)

   * For a 2-D line chart, specify the fill type and the color pattern to fill the lines.

     If you select the **Use Single Color** fill type, first make a choice for the **Self Settings** checkbox: when Self Settings is unselected (the default behavior), Designer synchronizes the color pattern that you specify here with the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#Pattern) on the chart object in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart; when you select Self Settings, it indicates that the color pattern is private to the current data markers themselves (the lines in this case), which Designer remembers and applies to the data markers of a new type automatically if later you change the type of the chart. Then, in the **Fill** box, specify the color and the transparency of the color to fill the current line, that is, the line you have selected on to open the Format Line dialog box (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box), or select the **Pattern List** button to specify the color pattern for each line in the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058302-Color-List-Dialog-Box). In the **Area** box, ![Marks content and feature updates for Logi Report v17.1. New feature new content.](https://devnet.logianalytics.com/hc/article_attachments/4404856832151/___newv17.1.jpg "New for Logi Report v17.1.")select **Fill Area** if you want to fill the areas that are formed by the chart axes and the lines, and then in the **Color** and **Transparency** text boxes, set the color and transparency of the color to fill the area for the current line, or select **Area Pattern List** to specify the color pattern for each area formed by each line and the chart axes in the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058302-Color-List-Dialog-Box). In the **Line** box, specify the line style and line thickness of the current line, or select **Line Pattern List** to set the line pattern for each line in the [Line Pattern List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097841-Line-Pattern-List-Dialog-Box).

     If you select the **Use Single Color with Condition** fill type, specify the conditions and the line pattern for each condition respectively. For more information, see [Adding Conditional Color Fills to Charts](https://devnet.logianalytics.com/hc/en-us/articles/1500010094361-Applying-Conditional-Color-Fills-to-Charts).
   * For a 3-D line chart, first decide whether or not to select the [Self Setting](#SelfSettings) checkbox, then specify the color and the transparency of the color to fill the current line, or select the **Color List** button to specify the color pattern for each line in the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058302-Color-List-Dialog-Box).
4. For a 2-D line chart, in the **Node** tab, specify the fill type and the color pattern to fill the nodes in the lines.

   ![Format Line dialog box - Node](https://devnet.logianalytics.com/hc/article_attachments/4404848547351/fmtln_node.gif)

   If you select the **Use Single Color** fill type, first make a choice for the **Self Settings** checkbox: when Self Settings is unselected (the default behavior), Designer synchronizes the color pattern that you specify here with the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#Pattern) on the chart object in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart; when you select Self Settings, it indicates that the color pattern is private to the current data markers themselves (the line nodes in this case), which Designer remembers and applies to the data markers of a new type automatically if later you change the type of the chart. Then, in the **Shape** box, set **Show Node** to **true** to show nodes in the current line, and then specify the style, transparency, width, height, and color of the nodes, and specify whether or not to display the nodes in the highest and lowest points with other colors and whether to show the highlight point in a distinguishing color when mouse hovering on a node in the line. If you select a node style other than any of the following: plus, multiplication, star1, or star2, in the **Border** box, set the border properties of the nodes in the current line, including the border color, color transparency, line style, and thickness; otherwise, in the **Line** box, specify the line style and thickness for the nodes. You can also select the **Node Pattern List** button to specify the node pattern for each line in the [Node Pattern List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059862-Node-Pattern-List-Dialog-Box).

   If you select the **Use Single Color with Condition** fill type, specify the conditions and the node pattern for each condition respectively. For more information, see [Adding Conditional Color Fills to Charts](https://devnet.logianalytics.com/hc/en-us/articles/1500010094361-Applying-Conditional-Color-Fills-to-Charts).

   If you want to apply the color pattern that you specify for the nodes to the corresponding lines, select **Apply Color to Line**, Designer then ignores the color and transparency settings on the lines.
5. For a 3-D line chart, in the **Border** tab, specify the properties for the border of the chart lines.

   ![Format Line - Border](https://devnet.logianalytics.com/hc/article_attachments/4404848548119/fmtln_brdr.gif)

   Select **Show Border** if you want to show the border of the chart lines, then specify the color, color transparency, line style, thickness, end caps style, and line joint mode of the border.

   In the **Path** box, specify the fill pattern of the border: Outline Path or Fill Path.

   In the **Dash** box, select to automatically adjust the dash size or use fixed dash size if you select a dash line style for the border.
6. In the **Data Label** tab, specify the properties of the static data labels in the line chart.

   ![Format Line dialog box - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4404856945303/fmtln_data.gif)

   For a 2-D line chart, in the **Static Data Label** box, select **Show Static Data Label** if you want to show static data labels for the line nodes, then select the position of the data labels relative to the nodes, in which way to display the values in the data labels, whether to scale big and small numbers in the data labels, and whether to hide the data label whose value is 0.

   In the **Font** box, specify the font format of the text in the data labels, including the font face, size, color, color transparency, rotation angle, shearing angle.

   In the **Effects** box, specify the special effects for the text in the data labels such as style, strikethrough, and underline.
7. In the **Hint** tab, specify whether to include the category and series values and whether to scale big and small numbers in the line hint (you need to set the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/1500010100301-Chart-Paper-Properties#ShowTips) property on the chart paper to "true" in the Report Inspector if you want to show the hint). A hint displays the value a line node represents when you point the mouse pointer at the node in Designer view mode, in HTML output, or at runtime.

   ![Format Line - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404848548631/fmtln_hint.gif)
8. For a line chart in a library component, you can define web behaviors on the lines in the **Behaviors** tab.
   A web behavior contains a trigger event and a web action to be triggered when the event occurs on the lines at runtime. You can add as many web behaviors to the lines as you need.

   ![Format Line dialog box for library component - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404856945559/fmtln_bhvr.gif)

   To define the web behavior, select a [trigger event](https://devnet.logianalytics.com/hc/en-us/articles/1500010057562-Using-Basic-Web-Controls-in-a-Report#Event) from the drop-down list in the **Events** column, then select in the **Actions** column and select the **ellipsis** button ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif) in the text box. In the Web Action List dialog box, bind a web action [the same as you do to web controls](https://devnet.logianalytics.com/hc/en-us/articles/1500010057562-Using-Basic-Web-Controls-in-a-Report#Action) in the library component. The web actions you can bind include Filter, Sort, Parameter, Property, and SendMessage.

   You can select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add and define more web behaviors; if a web behavior is not required, select it and select the **Remove** button ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif) to delete it. Select a web behavior and select the **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif) button to adjust the order of the behaviors, then at runtime, when an event that is bound with more than one action happens, JDashboard triggers the upper action first.
9. Select **OK** to apply the settings and close the dialog box.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* If the chart is a combo chart composed by lines and areas/bars, when you set the depth properties for the lines, Designer applies them to the areas/bars as well, and vice versa.
* For a 3-D line chart, Designer disables the Show Static Data Label option in the Data Label tab of the Format Line dialog box; however, you can still see the data labels by moving the mouse pointer over the lines when viewing the report result in Designer view mode, in HTML output, or in Page Report Studio.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094461-Formatting-the-Bars-in-a-Bar-Bench-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094421-Formatting-the-Areas-in-an-Area-Chart)
