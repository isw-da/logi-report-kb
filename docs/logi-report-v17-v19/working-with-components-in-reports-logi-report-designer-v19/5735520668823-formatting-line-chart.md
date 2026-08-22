---
title: "Formatting Line Chart"
id: 5735520668823
section: "Working with Components in Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735520668823-Formatting-Line-Chart
updated_at: 2022-11-02T04:27:59Z
---

# Formatting Line Chart

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735512007575-Formatting-Bar-Bench-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735506840727-Formatting-Area-Chart)

# Formatting Line Chart

This topic describes how you can format the lines in a line chart.

1. Right-click any line in the line chart and select **Format 2D Line** or **Format 3D Line** on the shortcut menu, or double-click any line in the chart. Designer displays the [Format Line dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735509343767-Format-Line-Dialog-Box).
2. In the **General** tab, specify the general properties of the lines.
   * For a 2-D line chart, set the layout style of the lines. To add a 3-dimensional effect to the lines, set **Use Depth** to **true** and then specify the depth and direction. Select **Ignore Null Value** to draw the lines from the previous data values to the next data values directly when null data values appear to avoid breaks on the lines. Select **Smoothed Line** if you want to draw the lines smoothly without the sharp joints.

     ![Format Line dialog box - General 2-D](https://devnet.logianalytics.com/hc/article_attachments/9898480434711/fmtln_gnrl_1.gif)
   * For a 3-D line chart, specify the thickness of the lines, and select **Ignore Null Value** to draw the lines from the previous data values to the next data values directly when null data values appear to avoid breaks on the lines.

     ![Format Line dialog box - General 3-D](https://devnet.logianalytics.com/hc/article_attachments/9898463296407/fmtln_gnrl_2.gif)
3. In the **Fill** tab, specify the fill type and the color pattern to fill the chart lines.

   ![Format Line dialog box - Fill 2-D](https://devnet.logianalytics.com/hc/article_attachments/9898463310103/fmtln_fill.gif)

   * For a 2-D line chart, specify the fill type and the color pattern to fill the lines.
     + When you select the **Use Single Color** fill type,
       - Make your choice for the **Self Settings** option. When Self Settings is cleared (the default behavior), Designer synchronizes the color pattern that you specify here with the [Pattern List](https://devnet.logianalytics.com/hc/en-us/articles/5735545992599-Chart-Properties#Pattern) property of the chart in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart. When you select Self Settings, it indicates that the color pattern is private to the current data markers themselves (the lines in this case), which Designer remembers and applies to data markers of the new type automatically if you change the type of the chart later.
       - In the **Fill** box, specify the color and transparency to fill the current line, that is, the line you have selected on to open the Format Line dialog box (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box), or select **Pattern List** to specify the color pattern for each line in the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522093463-Color-List-Dialog-Box).
       - In the **Area** box, select **Fill Area** if you want to fill the areas that are formed by the chart axes and the lines, and then in the **Color** and **Transparency** text boxes, set the color and transparency to fill the area for the current line, or select **Area Pattern List** to specify the color pattern for each area formed by each line and the chart axes in the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522093463-Color-List-Dialog-Box).
       - In the **Line** box, specify the line style and line thickness of the current line, or select **Line Pattern List** to set the line pattern for each line in the [Line Pattern List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735551885847-Line-Pattern-List-Dialog-Box).
     + When you select the **Use Single Color with Condition** fill type, specify the conditions and the line pattern for each condition respectively. See [Adding Conditional Color Fills to Charts](https://devnet.logianalytics.com/hc/en-us/articles/5735511924119-Applying-Conditional-Color-Fills-to-Charts).
   * For a 3-D line chart, first decide whether to select [Self Setting](#SelfSettings), then specify the color and transparency to fill the current line, or select **Color List** to specify the color pattern for each line in the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522093463-Color-List-Dialog-Box).
4. For a 2-D line chart, in the **Node** tab, specify the fill type and the color pattern to fill the nodes in the lines.

   ![Format Line dialog box - Node](https://devnet.logianalytics.com/hc/article_attachments/9898463319191/fmtln_node.gif)

   * When you select the **Use Single Color** fill type,
     + Make your choice for the **Self Settings** option. When Self Settings is cleared (the default behavior), Designer synchronizes the color pattern that you specify here with the [Pattern List](https://devnet.logianalytics.com/hc/en-us/articles/5735545992599-Chart-Properties#Pattern) property of the chart in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart. When you select Self Settings, it indicates that the color pattern is private to the current data markers themselves (the line nodes in this case), which Designer remembers and applies to data markers of the new type automatically if you change the type of the chart later.
     + In the **Shape** box, set **Show Node** to **true** to show nodes in the current line, and then specify the style, transparency, width, height, and color of the nodes, and specify whether to display the nodes in the highest and lowest points with other colors and whether to show the highlight point in a distinguishing color when mouse hovering on a node in the line.
     + When you select a node style other than any of the following: plus, multiplication, star1, or star2, in the **Border** box, set the border properties of the nodes in the current line, including the border color, transparency, line style, and thickness; otherwise, in the **Line** box, specify the line style and thickness for the nodes.
     + You can also select **Node Pattern List** to specify the node pattern for each line in the [Node Pattern List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735514860695-Node-Pattern-List-Dialog-Box).
   * When you select the **Use Single Color with Condition** fill type, specify the conditions and the node pattern for each condition respectively. See [Adding Conditional Color Fills to Charts](https://devnet.logianalytics.com/hc/en-us/articles/5735511924119-Applying-Conditional-Color-Fills-to-Charts).
   * If you want to apply the color pattern that you specify for the nodes to the corresponding lines, select **Apply Color to Line**, Designer then ignores the color and transparency settings on the lines.
5. For a 3-D line chart, in the **Border** tab, select **Show Border** if you want to display border for the chart lines, then specify the border properties.

   ![Format Line dialog box - Border](https://devnet.logianalytics.com/hc/article_attachments/9898463342871/fmtln_brdr.gif)

   * Specify the color, transparency, line style, thickness, ending style, and line joint mode of the border.
   * In the **Path** box, specify the fill pattern of the border: Outline Path or Fill Path.
   * In the **Dash** box, select to automatically adjust the dash size or use fixed dash size if you select a dash line style for the border.
6. In the **Data Label** tab, specify properties of the static data labels in the line chart.

   ![Format Line dialog box - Data Label](https://devnet.logianalytics.com/hc/article_attachments/9898463362711/fmtln_data.gif)

   * For a 2-D line chart, in the **Static Data Label** box, select **Show Static Data Label** if you want to show static data labels for the line nodes, then specify the position of the data labels relative to the nodes, the type of the data labels, whether to scale big and small numbers in the data labels, and whether to hide the data label when its value is 0.
   * In the **Font** and **Effects** box, specify the font format and special effects of the data labels, such as the font face, font size, font color, and the font style of the data labels.
7. In the **Hint** tab, specify properties of the chart hint. A hint displays the value a line node represents when you point to the node in Designer view mode, in HTML output, or at runtime.

   ![Format Line dialog box - Hint](https://devnet.logianalytics.com/hc/article_attachments/9898480507031/fmtln_hint.gif)

   * Clear **Show Category and Series** if you do not want to include the category and series values in the hint.
   * Specify whether to scale big and small numbers in the hint.
   * Select **Customize Chart Value Name** to use customized names for the fields on the value axis in the hint and select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898423153431/btn_ellipsis1.gif) to customize the names as you want.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) You should not edit the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/5735546052119-Chart-Paper-Properties#ShowTips) property of the Chart Paper object in the Report Inspector which is "true" by default, if you want to display the hint.
8. For a line chart in a library component, you can [specify web behaviors](https://devnet.logianalytics.com/hc/en-us/articles/9898540480023-Defining-Web-Behaviors-of-Objects-in-a-Report#WebControl) for it in the **Behaviors** tab, to enable users to trigger different web actions when they perform specific operations such as Click and Mouse Over on the lines at runtime.

   ![Format Line dialog box - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/9898480516759/fmtln_bhvr.gif)
9. Select **OK** to apply the settings and close the dialog box.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)

* If the chart is a combo chart composed by lines and areas/bars, when you set the depth properties for the lines, Designer applies them to the areas/bars as well, and vice versa.
* For a 3-D line chart, Designer disables the Show Static Data Label option in the Data Label tab of the Format Line dialog box. However, you can still see the data labels by pointing to the lines when viewing the report in Designer view mode, in HTML output, or in Page Report Studio.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735512007575-Formatting-Bar-Bench-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735506840727-Formatting-Area-Chart)
