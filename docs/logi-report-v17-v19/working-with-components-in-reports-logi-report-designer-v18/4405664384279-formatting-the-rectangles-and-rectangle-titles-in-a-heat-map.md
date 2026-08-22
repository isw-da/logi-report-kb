---
title: "Formatting the Rectangles and Rectangle Titles in a Heat Map"
id: 4405664384279
section: "Working with Components in Reports - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664384279-Formatting-the-Rectangles-and-Rectangle-Titles-in-a-Heat-Map
updated_at: 2022-01-27T20:34:27Z
---

# Formatting the Rectangles and Rectangle Titles in a Heat Map

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664377879-Formatting-the-Bullets-in-a-Bullet-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664379031-Formatting-the-Gauge-in-a-Gauge-Chart)

# Formatting the Rectangles and Rectangle Titles in a Heat Map

This topic introduces how you can format the rectangles and the titles of the rectangles in a heat map.

This topic contains the following sections:

* [Formatting the Rectangles in a Heat Map](#Rectangle)
* [Formatting the Titles for Rectangles in a Heat Map](#Title)

## Formatting the Rectangles in a Heat Map

1. When there is only one group in the heat map, right-click the heat map and select **Format Rectangle** on the shortcut menu. Designer displays the [Format Rectangle dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661585687-Format-Rectangle-Dialog-Box).

   When there are two or more groups in the heat map, right-click the heat map, then from the Format Rectangle submenu, select a desired group field. Designer displays the Format Rectangle dialog box for the field.
2. In the **Fill** tab, specify the fill type and the color pattern to fill the rectangles.

   If you select the **Use Single Color** fill type:

   * When the heat map is colored by one of the following cases: no field, 1 to n groups, or 1 to n groups and 1 summary, specify the color pattern as follows:

     ![Format Rectangle dialog box - Fill](https://devnet.logianalytics.com/hc/article_attachments/4420542212247/cmpnt_cht_frmt_rctgl1.gif)

     Make a choice for the **Self Settings** checkbox first: when Self Settings is cleared (the default behavior), Designer synchronizes the color pattern that you specify here with the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/4405664650263-Chart-Properties#Pattern) on the chart object in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart; when you select Self Settings, it indicates that the color pattern is private to the current data markers themselves (the rectangles in this case), which Designer remembers and applies to the data markers of a new type automatically if later you change the type of the chart. Then, specify the color for the first rectangle in the heat map and the transparency of the color (if the heat map is colored by no field, Designer fills all rectangles with this color) (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box). By default, Designer selects **Vary Colors by Color List** which means Designer fills each rectangle with a different color and you can select **Color List** to customize the color of each rectangle in the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661476887-Color-List-Dialog-Box).
   * When the heat map is colored by a summary, specify the color pattern as follows:

     ![Format Rectangle dialog box - Fill](https://devnet.logianalytics.com/hc/article_attachments/4420556251287/cmpnt_cht_frmt_rctgl2.gif)

     Specify the start color for the minimum value and the end color for the maximum value of the summary respectively on the gradient color bar. To exchange the start color and the end color, select **Reversed** (by default, Designer does not select the option and the start/end color here corresponds to the start/end color on the [chart object](https://devnet.logianalytics.com/hc/en-us/articles/4405664650263-Chart-Properties#EndColor) in the Report Inspector; when you select it, the start/end color here corresponds to the end/start color on the chart object). If you want to specify a color for the zero value, select **Color When Zero** and define the color accordingly, then the gradient color changes from the start color to the zero value color, and then from the zero value color to the end color. You can also specify a color for the null value.

   If you select the **Use Single Color with Condition** fill type, specify the conditions and the color pattern for each condition respectively. For more information, see [Adding Conditional Color Fills to Charts](https://devnet.logianalytics.com/hc/en-us/articles/4405664369943-Applying-Conditional-Color-Fills-to-Charts).
3. In the **Separator** tab, specify the color, color transparency, line style, and thickness of the lines separating the rectangles.

   ![Format Rectangle dialog box - Separator](https://devnet.logianalytics.com/hc/article_attachments/4420550986135/fmtrctgl_sprtr.gif)

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) You would get a bad layout in the preview result in Designer and in the exported result if you set the separator thickness to a big value.
4. For a heat map in a library component, you can define web behaviors on the rectangles in the **Behaviors** tab. A web behavior contains a trigger event and a web action to be triggered when the event occurs on the rectangles at runtime. You can add as many web behaviors to the rectangles as you need.

   ![Format Rectangle dialog box - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4420550986391/fmtrctgl_bhvr.gif)

   To define the web behavior, select a [trigger event](https://devnet.logianalytics.com/hc/en-us/articles/4405661415703-Using-Basic-Web-Controls-in-a-Report#Event) from the drop-down list in the **Events** column, then select in the **Actions** column and select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420550841879/btn_ellipsis1.gif). In the Web Action List dialog box, bind a web action [the same as you do to web controls](https://devnet.logianalytics.com/hc/en-us/articles/4405661415703-Using-Basic-Web-Controls-in-a-Report#Action) in the library component. The web actions you can bind include Filter, Sort, Parameter, Property, and SendMessage.

   You can select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif) to add and define more web behaviors; to delete a web behavior, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420542080407/btn_trashcan.gif). You can also select a web behavior and select **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420542078103/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420542078359/btn_mvdwn.gif) to adjust the order of the behaviors, then at runtime, when an event that is bound with more than one action happens, JDashboard triggers the upper action first.
5. Select **OK** to accept the changes and close the dialog box.

## Formatting the Titles for Rectangles in a Heat Map

1. When there is only one group in the heat map, right-click the heat map and select **Format Rectangle Title** on the shortcut menu. Designer displays the [Format Rectangle Title dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664501399-Format-Rectangle-Title-Dialog-Box).

   When there are two or more groups in the heat map, right-click the heat map, then from the Format Rectangle Title submenu, select a desired group. Designer displays the Format Rectangle Title dialog box for the group.
2. In the **General** tab, specify the height and fill color of the rectangle titles (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box).

   ![Format Rectangle Title dialog box - General](https://devnet.logianalytics.com/hc/article_attachments/4420542212887/fmtrctglttl_gnrlv18.2.gif)
3. In the **Font** tab, specify the font face, font size, font color, and alignment of the text in the rectangle titles, and specify the special effects for the text such as Bold, Underline, and Italic. By default, Logi Report Engine ignores the HTML tag elements that are included in the text at runtime and in HTML output, so they display exactly as what they are; clear **Ignore HTML Tag** if you want Logi Report Engine to transfer the HTML tag elements to the web browser, so they are translated into HTML by the web browser.

   ![Format Rectangle Title dialog box - Font](https://devnet.logianalytics.com/hc/article_attachments/4420550986647/fmtrctglttl_fontv18.2.gif)
4. In the **Border** tab, specify the color, thickness, line styles for the border of the rectangle titles; select **Shadow** to add a shadow effect to the border and specify the shadow color.

   ![Format Rectangle Title dialog box - Border](https://devnet.logianalytics.com/hc/article_attachments/4420542213271/fmtrctglttl_brdr.gif)
5. Select **OK** to accept the changes and close the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664377879-Formatting-the-Bullets-in-a-Bullet-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664379031-Formatting-the-Gauge-in-a-Gauge-Chart)
