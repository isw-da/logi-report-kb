---
title: "Formatting the Legend"
id: 1500010056962
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010056962-Formatting-the-Legend
updated_at: 2021-07-23T19:14:40Z
---

# Formatting the Legend

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094541-Formatting-the-Paper)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094641-Formatting-the-Wall-Floor)

# Formatting the Legend

This topic describes how you can format the legend of chart.

1. Right-click any chart element and select **Format Legend** from the shortcut menu, or double-click the legend of the chart. Designer displays the [Format Legend dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059222-Format-Legend-Dialog-Box).

   ![Format Legend dialog box - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404848549143/fmtlgnd_fill.gif)
2. In the **Fill** tab, specify the color and transparency of the color to fill the legend (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box).
3. In the **Border** tab, specify the properties for the border of the legend.

   ![Format Legegnd dialog box - Border](https://devnet.logianalytics.com/hc/article_attachments/4404848549527/fmtlgnd_border.gif)

   Specify the type, color, color transparency, line style, thickness, end caps style, and line joint mode of the border.

   In the **Path** box, specify the fill pattern of the border: Outline Path or Fill Path.

   In the **Dash** box, select to automatically adjust the dash size or use fixed dash size if you select a dash line style for the border.
4. In the **Placement** tab, specify in which manner to place the legend in the chart.

   ![Format Legegnd dialog box - Placement](https://devnet.logianalytics.com/hc/article_attachments/4404848550039/fmtlgnd_plcmnt.gif)

   In the **Position** box, specify whether to place the legend at the left, right, top, or bottom of the chart, and then select the alignment style accordingly in the **Alignment** box. If you select **Customized**, you can drag the legend on the chart manually in the design area to specify its location.

   In the **Legend Label Gap** box, specify the vertical and horizontal margins between the legend entries and the legend boundaries, and the vertical and horizontal spacing between the legend entry labels.

   Select **Reverse Legend** if you want to arrange the legend entries in a reverse order.

   Select **Show Scrollbar** in order to show the legend scrollbar to fully view the legend content when the content does not fit into the legend.

   Select **Truncate** to truncate the legend entry label text when the text overflows the labels.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) Usually, it is easier to select the legend and use the grab handles to resize and move the legend as needed anywhere in the chart.
5. In the **Font** tab, specify the font formats of the legend entry labels, including the font face, size, color, transparency, rotation angle, shearing angle, and effects such as style, strikethrough, and underline.

   ![Format Legend dialog box - Font](https://devnet.logianalytics.com/hc/article_attachments/4404848550295/fmtlgnd_font.gif)
6. In the **Orientation** tab, specify the rotation angle for legend entry labels. You can either drag the **Text** hand in the **Orientation** box or type a value in the **Angle** text box to set the angle.

   ![Format Legend dialog box - Orientation](https://devnet.logianalytics.com/hc/article_attachments/4404856946071/fmtlgnd_orntatn.gif)
7. In the **Format** tab, specify the data format of the legend entry labels, which Designer applies only when you set the property [Label Format Source](https://devnet.logianalytics.com/hc/en-us/articles/1500010061942-Chart-Legend-Properties#LabelFormatSource) of the chart legend to **Legend Label Format** in the Report Inspector.

   ![Format Legend dialog box - Format](https://devnet.logianalytics.com/hc/article_attachments/4404856946327/fmtlgnd_fmt.gif)

   Select a category from the **Category** box, then select a format from the **Format** box and select **Add** to add it to the **Stack** box (for more information about each format, [select here](https://devnet.logianalytics.com/hc/en-us/articles/1500010096081-Data-Format-Dialog-Box#DataFormat)). If the formats that Designer provides in the Format box cannot meet your requirement, you can define the format in the **Properties** text box and add it as the format of the selected category. You can add more than one format, but for each category, only one format is allowed. If you do not need a format any more, select it in the Stack box and select **Remove** to clear it.

   Set the **Auto Scale in Number** option to specify whether to automatically scale the big and small Number values.
8. In the **Mark** tab, specify the properties of the legend entry marks.

   ![Format Legend dialog box - Mark](https://devnet.logianalytics.com/hc/article_attachments/4404848550679/fmtlgnd_mark.gif)

   By default, Designer selects **Customize**, meaning, you can customize the format of the legend entry marks by yourself. To specify the style for a mark item, select the item in the **Mark Items** box and then select the style from the drop-down list in the box. You can select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add more items to the Mark Items box and define their style. To delete a mark item, select it and select the **Remove** button ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif); to adjust the order of the items, select a mark item and select the **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif) button. The legend entry marks repeat within the mark items you define. If you define more mark items than the actual legend entry marks, Designer ignores the redundant mark items.

   In the **Icon** box, specify the width and height of the legend entry marks, the horizontal and vertical alignment of the marks relative to the entry labels, and the gap between each entry mark and entry label.

   In the **Border** box, set the color, style, thickness, and color transparency of the mark border. If the chart uses a query resource, you can [use a formula to control](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties) the border color and transparency.

   For a line chart, you can also select **Use Node as Mark** or **Use Line and Node as Mark** to apply the style and color of the line nodes or lines and line nodes automatically to the legend entry marks. When you select either of these two options, Designer disables the Mark Items and Border boxes, but you can still specify the properties of marks in the Icon box.
9. Designer enables the options in the **Label** tab, if the legend entry labels show the values of the field displaying on the category or series axis of the chart. You can customize the text of the legend entry labels as follows: clear **Auto**, then from the **Label Text** drop-down list, select a field the values of which you prefer to display as the entry labels, or use a formula to [control the label text](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties); you can also select the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848471319/btn_x.gif) and type the text that you want to show in the labels in the text box manually.

   ![Format Legend dialog box - Label](https://devnet.logianalytics.com/hc/article_attachments/4404848550935/fmtlgnd_lbl.gif)
10. For a chart in a library component, you can define web behaviors on its legend in the **Behaviors** tab.
    A web behavior contains a trigger event and a web action to be triggered when the event occurs on the legend at runtime. You can add as many web behaviors to the legend as you need.

    ![Format Legend dialog box for library component - Behavior](https://devnet.logianalytics.com/hc/article_attachments/4404856947351/fmtlgnd_bhvr.gif)

    To define the web behavior, select a [trigger event](https://devnet.logianalytics.com/hc/en-us/articles/1500010057562-Using-Basic-Web-Controls-in-a-Report#Event) from the drop-down list in the **Events** column, then select in the **Actions** column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif) in the text box. In the Web Action List dialog box, bind a web action [the same as you do to web controls](https://devnet.logianalytics.com/hc/en-us/articles/1500010057562-Using-Basic-Web-Controls-in-a-Report#Action) in the library component. The web actions you can bind include Filter, Sort, Parameter, Property, and SendMessage.

    You can select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add and define more web behaviors; if a web behavior is not required, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif) to delete it. Select a web behavior and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif) to adjust the order of the behaviors, then at runtime, when an event that is bound with more than one action happens, JDashboard triggers the upper action first.
11. Select **OK** to apply the settings and close the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094541-Formatting-the-Paper)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094641-Formatting-the-Wall-Floor)
