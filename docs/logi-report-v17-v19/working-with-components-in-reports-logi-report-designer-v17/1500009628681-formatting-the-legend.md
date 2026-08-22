---
title: "Formatting the Legend"
id: 1500009628681
section: "Working with Components in Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009628681-Formatting-the-Legend
updated_at: 2021-07-24T16:05:20Z
---

# Formatting the Legend

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009605882-Formatting-the-Paper) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009606022-Formatting-the-Wall-Floor)

# Formatting the Legend

The chart legend is a box used to identify the patterns or colors assigned to the data categories in a chart. This topic introduces how to customize the chart legend.

1. Right-click any chart element and select **Format Legend** from the shortcut menu, or double-click the legend of the chart. The [Format Legend](https://devnet.logianalytics.com/hc/en-us/articles/1500009608482-Format-Legend-Dialog) dialog appears.

   ![Format Legend dialog - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404904306839/fmtlgnd_fill.gif)
2. In the Fill tab, set the color and transparency of the color for the legend (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box).
3. In the Border tab, set the border mode for the legend, including the border style, color, transparency, line style, thickness, end caps style, and line joint mode, and if you specify the line joint mode to be joint round, you can set the the radius for the border joint. You can also specify whether the border is to be outlined, and whether or not to automatically resize the border dashes if the border is drawn with dashes.

   ![Format Legegnd dialog - Border](https://devnet.logianalytics.com/hc/article_attachments/4404904307095/fmtlgnd_border.gif)
4. In the Placement tab, specify the way in which the legend will be placed.

   ![Format Legegnd dialog - Placement](https://devnet.logianalytics.com/hc/article_attachments/4404904307735/fmtlgnd_plcmnt.gif)

   In the Position box, specify whether the legend will be placed at the left, right, top, or bottom of the chart, and then set the alignment style accordingly in the Alignment box. If Auto is selected, the legend will be placed somewhere automatically.

   In the Legend Label Gap box, specify the vertical and horizontal margins between the legend entries and the legend boundaries, and the vertical and horizontal spacing between legend entry labels.

   Select **Reverse Legend** if you want to have the legend entries re-arranged in a reverse order. To show the legend scrollbar to fully view the legend content when the content does not fit into the legend, select **Show Scrollbar**. Select **Truncate** to truncate the legend entry label text when the text overflow the labels.

   **Tip:** Often it is easier to select the legend and use the grab handles to resize and move the legend as needed anywhere on the chart.
5. In the Font tab, specify the font formats of the legend entry labels, including the font face, size, color, transparency, rotation angle, shearing angle, and effects such as style, strikeout, underline, and so on (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box).

   ![Format Legend dialog - Font](https://devnet.logianalytics.com/hc/article_attachments/4404904307991/fmtlgnd_font.gif)
6. In the Orientation tab, set an angle for legend entry labels so as to rotate them. You can either drag the Text hand in the Orientation box or type a value in the Angle spinner to set the angle.

   ![Format Legend dialog - Orientation](https://devnet.logianalytics.com/hc/article_attachments/4404904308375/fmtlgnd_orntatn.gif)
7. In the Format tab, specify the data format of the legend entry labels, which takes effect when the property [Label Format Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009635181-Chart-Legend-Properties#LabelFormatSource) of the chart legend in the Report Inspector is set to Legend Label Format.

   ![Format Legend dialog - Format](https://devnet.logianalytics.com/hc/article_attachments/4404904308759/fmtlgnd_fmt.gif)

   Select a category from the Category box, then select a format from the Format box and select **Add** to add it to the Stack box (for details about each format, [go here](https://devnet.logianalytics.com/hc/en-us/articles/1500009607682-Data-Format-Dialog#DataFormat)). If the formats listed in the Format box cannot meet your requirement, define the format in the Properties text box and select **Add** to add it as the format of the selected category. For the Number category, you can specify whether to scale big and small numbers by setting the [Auto Scale in Number](https://devnet.logianalytics.com/hc/en-us/articles/1500009608482-Format-Legend-Dialog#AutoScale) option. You can add more than one format, and in the event that one of the formats is not necessary, you can clear it by selecting Remove.
8. In the Mark tab, specify the options for the legend entry marks.

   ![Format Legend dialog - Mark](https://devnet.logianalytics.com/hc/article_attachments/4404904309143/fmtlgnd_mark.gif)

   By default, Customize is selected, which enables you to customize the format of the legend entry marks. Logi Report Designer uses 16 styles for the marks by default. To add a style, select a mark item from the Mark Items drop-down list, and then select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) to add it to the Mark Items box. The legend entry marks will repeat within the mark items you have defined. If you have defined more mark items than the actual legend entry marks, the redundant mark items will be ignored. You can select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif), ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif), or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif) to remove a mark item, or to arrange the order of the items. To change the style of a mark item, select it in the Mark Items box and then choose a new one from the Mark Items drop-down list.

   In the Icon box, specify the horizontal and vertical alignment styles, and the gap between each entry mark and entry label. You can also set the width and height for the legend entry marks.

   In the Border box, set the color, style, thickness and transparency properties of the icon border. If the chart is created using a query resource, you can [use a formula to control](https://devnet.logianalytics.com/hc/en-us/articles/1500009634221-Using-Formulas-to-Control-Object-Properties) the border color and transparency.

   For a line chart, you can also select **Use Node as Mark** or **Use Line and Node as Mark** to apply the style and color of the line nodes or lines and line nodes automatically to the legend entry marks. When either of these two is selected, you can also specify the properties of icons in the Icon box.
9. If you want to customize the text of the legend entry labels, go to the Label tab (the legend entry labels can be customized only when they show the values of the field displayed on the category or series axis of the chart).

   ![Format Legend dialog - Label](https://devnet.logianalytics.com/hc/article_attachments/4404904309399/fmtlgnd_lbl.gif)

   Clear **Auto**, then from the Label Text drop-down list select a field the values of which will be displayed as the entry labels, or use a formula to [control the label text](https://devnet.logianalytics.com/hc/en-us/articles/1500009634221-Using-Formulas-to-Control-Object-Properties). You can also select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404904223383/btn_x.gif) to type in the desired label text manually.
10. For a chart in a library component, you can define web behaviors on its legend in the Behaviors tab.

    ![Format Legend dialog for library component - Behavior](https://devnet.logianalytics.com/hc/article_attachments/4404904309911/fmtlgnd_bhvr.gif)

    Select a trigger event from the drop-down list in the Events column, then select in the Actions column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) that appears in the text box. In the Web Action List dialog, bind a web action to the legend [the same as you do to web controls](https://devnet.logianalytics.com/hc/en-us/articles/1500009629441-Using-Basic-Web-Controls-in-a-Report#Action) in the library component, which will be triggered when the specified event occurs on the legend. The web actions you can bind include Filter, Sort, Parameter, Property and SendMessage.

    To add a web behavior line, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif), and if a web behavior is not required, select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif) to remove it.

    Select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif) to adjust the order of the behaviors. Then, when an event that has been bound with more than one action happens, the upper action will be triggered first.
11. Select **OK** to apply the settings and close the dialog.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009605882-Formatting-the-Paper) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009606022-Formatting-the-Wall-Floor)
