---
title: "Formatting Heat Map Rectangles"
id: 5735527346839
section: "Working with Components in Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735527346839-Formatting-Heat-Map-Rectangles
updated_at: 2022-11-02T04:28:03Z
---

# Formatting Heat Map Rectangles

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735520593815-Formatting-Bullet-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735520602391-Formatting-Gauge-Chart)

# Formatting Heat Map Rectangles

This topic introduces how you can format the rectangles and titles of the rectangles in a heat map.

This topic contains the following sections:

* [Formatting the Rectangles in a Heat Map](#Rectangle)
* [Formatting the Titles for Rectangles in a Heat Map](#Title)

## Formatting the Rectangles in a Heat Map

1. When there is only one group in the heat map, right-click the heat map and select **Format Rectangle** on the shortcut menu. Designer displays the [Format Rectangle dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735514268823-Format-Rectangle-Dialog-Box).

   When there are two or more groups in the heat map, right-click the heat map, then from the Format Rectangle submenu, select a group field. Designer displays the Format Rectangle dialog box for the group.
2. In the **Fill** tab, specify the fill type and the color pattern to fill the rectangles.
   * When you select the **Use Single Color with Condition** fill type, specify the conditions and the color pattern for each condition respectively. See [Adding Conditional Color Fills to Charts](https://devnet.logianalytics.com/hc/en-us/articles/5735511924119-Applying-Conditional-Color-Fills-to-Charts).
   * When you select the **Use Single Color** fill type,
     + When the heat map is colored by one of the following cases: no field, 1 to n groups, or 1 to n groups and 1 summary,

       ![Format Rectangle dialog box - Fill](https://devnet.logianalytics.com/hc/article_attachments/9898519339287/cmpnt_cht_frmt_rctgl1.gif)

       - Make your choice for the **Self Settings** option. When Self Settings is cleared (the default behavior), Designer synchronizes the color pattern that you specify here with the [Pattern List](https://devnet.logianalytics.com/hc/en-us/articles/5735545992599-Chart-Properties#Pattern) property of the chart in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart. When you select Self Settings, it indicates that the color pattern is private to the current data markers themselves (the rectangles in this case), which Designer remembers and applies to data markers of the new type automatically if you change the type of the chart later.
       - Specify the color and transparency of the first rectangle (or all rectangles when the heat map has no color-by field) in the heat map (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box).
       - By default, Designer selects **Vary Colors by Color List** which means Designer fills each rectangle with a different color. You can select **Color List** to customize the color of each rectangle in the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522093463-Color-List-Dialog-Box).
     + When the heat map is colored by a summary,

       ![Format Rectangle dialog box - Fill](https://devnet.logianalytics.com/hc/article_attachments/9898519348247/cmpnt_cht_frmt_rctgl2.gif)

       - Specify the starting color for the minimum value and ending color for maximum value of the summary respectively on the gradient color bar. To exchange the starting color and ending color, select **Reversed**.
       - If you want to specify a color for the zero value, select **Color When Zero** and define the color accordingly, then the gradient changes from the starting color to the zero value color, and then from the zero value color to the ending color.
       - You can also specify a color for the null value by setting **Color When Null**.
3. In the **Separator** tab, specify the color, transparency, style, and thickness of the line separating the rectangles.

   ![Format Rectangle dialog box - Separator](https://devnet.logianalytics.com/hc/article_attachments/9898480158487/fmtrctgl_sprtr.gif)

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) You could get a bad layout in the preview result in Designer and in the report outputs, when you set the separator thickness to a big value.
4. For a heat map chart in a library component, you can [specify web behaviors](https://devnet.logianalytics.com/hc/en-us/articles/9898540480023-Defining-Web-Behaviors-of-Objects-in-a-Report#WebControl) for it in the **Behaviors** tab, to enable users to trigger different web actions when they perform specific operations such as Click and Mouse Over on the rectangles at runtime.

   ![Format Rectangle dialog box - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/9898480176023/fmtrctgl_bhvr.gif)
5. Select **OK** to accept the changes and close the dialog box.

## Formatting the Titles for Rectangles in a Heat Map

1. When there is only one group in the heat map, right-click the heat map and select **Format Rectangle Title** on the shortcut menu. Designer displays the [Format Rectangle Title dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735529772183-Format-Rectangle-Title-Dialog-Box).

   When there are two or more groups in the heat map, right-click the heat map, then from the Format Rectangle Title submenu, select a group field. Designer displays the Format Rectangle Title dialog box for the group.
2. In the **General** tab, specify the height and fill color of the rectangle titles (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box).

   ![Format Rectangle Title dialog box - General](https://devnet.logianalytics.com/hc/article_attachments/9898480127639/fmtrctglttl_gnrl.gif)
3. In the **Font** tab, specify font properties of the rectangle titles.

   ![Format Rectangle Title dialog box - Font](https://devnet.logianalytics.com/hc/article_attachments/9898480134295/fmtrctglttl_font.gif)

   * In the **Font** box, specify the font face, font size, font color, and alignment of the rectangle titles.
   * In the **Effects** box, apply some special effects to the rectangle titles, such as italicizing the titles and adding a horizontal line under the titles.
   * By default, Logi Report Engine ignores the HTML tag elements that are included in the rectangle titles at runtime and in HTML output, so they display exactly as what they are. Clear **Ignore HTML Tag** if you want Logi Report Engine to transfer the HTML tag elements to the web browser, so they are translated into HTML by the web browser.
4. In the **Border** tab, specify the color, thickness, line styles for the border of the rectangle titles; select **Shadow** to add a shadow effect to the border and specify the shadow color.

   ![Format Rectangle Title dialog box - Border](https://devnet.logianalytics.com/hc/article_attachments/9898463046807/fmtrctglttl_brdr.gif)
5. Select **OK** to accept the changes and close the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735520593815-Formatting-Bullet-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735520602391-Formatting-Gauge-Chart)
