---
title: "Formatting Chart Legend"
id: 5735527262487
section: "Working with Components in Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735527262487-Formatting-Chart-Legend
updated_at: 2022-11-02T04:27:59Z
---

# Formatting Chart Legend

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735564051223-Formatting-Chart-Paper)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735507095959-Formatting-Chart-Wall-Floor)

# Formatting Chart Legend

This topic describes how you can format the legend of chart.

1. Right-click any chart element and select **Format Legend** from the shortcut menu, or double-click the legend of the chart. Designer displays the [Format Legend dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735566098071-Format-Legend-Dialog-Box).

   ![Format Legend dialog box - Fill](https://devnet.logianalytics.com/hc/article_attachments/9898480533783/fmtlgnd_fill.gif)
2. In the **Fill** tab, specify the color and transparency to fill the legend (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box).
3. In the **Border** tab, specify properties for the border of the legend.

   ![Format Legegnd dialog box - Border](https://devnet.logianalytics.com/hc/article_attachments/9898480539671/fmtlgnd_border.gif)

   * From the **Border Type** drop-down list, select how you want to display the border.
   * Specify the color, transparency, line style, thickness, ending style, and line joint mode of the border.
   * In the **Path** box, specify the fill pattern of the border: Outline Path or Fill Path.
   * In the **Dash** box, select to automatically adjust the dash size or use fixed dash size if you select a dash line style for the border.
4. In the **Placement** tab, specify how you want to place the legend in the chart.

   ![Format Legegnd dialog box - Placement](https://devnet.logianalytics.com/hc/article_attachments/9898480550679/fmtlgnd_plcmnt.gif)

   * In the **Position** box, specify whether to place the legend on the left, right, top, or bottom of the chart, and then select the alignment accordingly in the **Alignment** box. If you select **Customized**, you can manually drag the legend on the chart in the design area to specify its location. Usually, it is easier to select the legend and use the grab handles to resize and move the legend as needed anywhere in the chart.
   * In the **Legend Label Gap** box, specify the vertical and horizontal margin between the legend entries and legend border, and the vertical and horizontal spacing between the legend entry labels.
   * Select **Reverse Legend** if you want to arrange the legend entries in a reverse order.
   * Select **Show Scrollbar** to show the legend scroll bar to fully view the legend content when the content does not fit into the legend.
   * Select **Truncate** to truncate the legend entry label text when the text overflows the label.
5. In the **Font** tab, specify the font properties of the legend entry labels, including the font face, size, color, transparency, rotation angle, and shearing angle. You can also apply some special effects to the entry labels, such as italicizing the labels and adding a horizontal line under the labels.

   ![Format Legend dialog box - Font](https://devnet.logianalytics.com/hc/article_attachments/9898463465751/fmtlgnd_font.gif)
6. In the **Orientation** tab, specify the rotation angle for the legend entry labels. You can either drag the **Text** hand in the **Orientation** box or type a value in the **Angle** text box to set the angle.

   ![Format Legend dialog box - Orientation](https://devnet.logianalytics.com/hc/article_attachments/9898480572823/fmtlgnd_orntatn.gif)
7. In the **Format** tab, specify the data format of the legend entry labels.

   ![Format Legend dialog box - Format](https://devnet.logianalytics.com/hc/article_attachments/9898463482135/fmtlgnd_fmt.gif)

   * Select a category from the **Category** box, then select a format from the **Format** box and select **Add** to add it to the **Stack** box. [Select here](https://devnet.logianalytics.com/hc/en-us/articles/5735500256407-Data-Format-Dialog-Box#DataFormat) for more information about each format.
   * When the formats Designer provides in the Format box cannot meet your requirement, you can define the format in the **Properties** text box and add it as the format of the selected category. You can add more than one format, but for each category, only one format is allowed.
   * If you do not need a format anymore, select it in the Stack box and select **Remove** to clear it.
   * Set the **Auto Scale in Number** option to specify whether to automatically scale the big and small Number values.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) The data format you specify for the legend entry labels takes effect only when you set the [Label Format Source](https://devnet.logianalytics.com/hc/en-us/articles/5735517009559-Chart-Legend-Properties#LabelFormatSource) property of the legend to "Legend Label Format" in the Report Inspector.
8. In the **Mark** tab, specify properties of the legend entry marks.

   ![Format Legend dialog box - Mark](https://devnet.logianalytics.com/hc/article_attachments/9898480595351/fmtlgnd_mark.gif)

   * By default, Designer selects **Customize**, meaning, you can customize the style of the legend entry marks by yourself. To specify the style for a mark item, select the item in the **Mark Items** box and then select the style from the drop-down list in the box. You can select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif) to add more items to the Mark Items box and define their style. To delete a mark item, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif); to adjust the order of the items, select a mark item and select **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif). The entry marks repeat within the mark items you define. If you define more mark items than the actual entry marks, Designer ignores the redundant mark items.
   * In the **Icon** box, specify the width and height of the legend entry marks, the horizontal and vertical alignment of the marks relative to the entry labels, and the gap between each entry mark and entry label.
   * In the **Border** box, set the color, style, thickness, and transparency of the mark border. If the chart uses a query resource, you can [use a formula to control](https://devnet.logianalytics.com/hc/en-us/articles/5735545031703-Using-Formulas-to-Control-Object-Properties) the border color and transparency.
   * For a line chart, you can also select **Use Node as Mark** or **Use Line and Node as Mark** to apply the style and color of the line nodes or lines and line nodes automatically to the legend entry marks. When you select either of these two options, Designer disables the Mark Items and Border boxes, but you can still specify the mark properties in the Icon box.
9. Designer enables options in the **Label** tab, when the legend entry labels show values of the field on the category or series axis of the chart. You can customize the text of the entry labels as follows: clear **Auto**, then from the **Label Text** drop-down list, select a field the values of which you prefer to display as the entry labels, or use a formula to [control the label text](https://devnet.logianalytics.com/hc/en-us/articles/5735545031703-Using-Formulas-to-Control-Object-Properties); you can also select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/9898459676183/btn_x.gif) and type the text you want to display in the labels in the text box.

   ![Format Legend dialog box - Label](https://devnet.logianalytics.com/hc/article_attachments/9898463505047/fmtlgnd_lbl.gif)
10. For a chart in a library component, you can [specify web behaviors](https://devnet.logianalytics.com/hc/en-us/articles/9898540480023-Defining-Web-Behaviors-of-Objects-in-a-Report#WebControl) for it in the **Behaviors** tab, to enable users to trigger different web actions when they perform specific operations such as Click and Mouse Over on the legend at runtime.

    ![Format Legend dialog box - Behavior](https://devnet.logianalytics.com/hc/article_attachments/9898480614551/fmtlgnd_bhvr.gif)
11. Select **OK** to apply the settings and close the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735564051223-Formatting-Chart-Paper)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735507095959-Formatting-Chart-Wall-Floor)
