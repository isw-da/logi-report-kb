---
title: "Formatting the Rectangles and Rectangle Titles in a Heat Map"
id: 1500010063561
section: "Working with Components in Reports - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010063561-Formatting-the-Rectangles-and-Rectangle-Titles-in-a-Heat-Map
updated_at: 2021-07-24T10:39:25Z
---

# Formatting the Rectangles and Rectangle Titles in a Heat Map

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010028822-Formatting-the-Bullets-in-a-Bullet-Chart) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010028842-Formatting-the-Gauge-in-a-Gauge-Chart)

# Formatting the Rectangles and Rectangle Titles in a Heat Map

This topic introduces how to format the rectangles and titles for rectangles in a heat map.

Below is a list of the sections covered in this topic:

* [Formatting the Rectangles in a Heat Map](#Rectangle)
* [Formatting the Titles for Rectangles in a Heat Map](#Title)

## Formatting the Rectangles in a Heat Map

1. When there is only one group in the heat map, right-click on the heat map and select **Format Rectangle** from the shortcut menu to bring up the [Format Rectangle](https://devnet.logianalytics.com/hc/en-us/articles/1500010031102-Format-Rectangle-Dialog) dialog.

   When there are two or more groups in the heat map, right-click on the heat map, then from the Format Rectangle submenu, select a desired group field to bring up the Format Rectangle dialog for the field.
2. In the Fill tab, specify the fill color of the rectangles: Use Single Color, or Use Single Color with Condition.

   If you select Use Single Color:

   * When the heat map is colored by one of the following cases: no field, 1 to n groups, 1 to n groups and 1 summary

     ![Format Rectangle dialog - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404909286807/cmpnt_cht_frmt_rctgl1.gif)

     First make a choice for the Self Settings checkbox: when Self Settings is unchecked, the color pattern specified here will be synchronized to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500010069721-Chart-Properties#Pattern) on the chart object in the Report Inspector, which can also be applied by data markers of other subtypes if the chart is a combo chart; when Self Settings is checked, it indicates the color pattern is private to the current data markers themselves (the rectangles in this case), which can be remembered and applied to the data markers of a new type automatically if later you change the type of the chart. Then specify the color for the first rectangle (when colored by no field, all rectangles are filled with this color) and the transparency of the color schema to fill the rectangle (to change the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010035022-Menu-Tabs#Palette) or input the hexadecimal value of a color directly in the text box). By default Vary Colors by Color List is checked which means each rectangle is filled with a different color, and you can select the **Color List** button to customize the color of each rectangle in the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500010030022-Color-List-Dialog) dialog as you want.
   * When the heat map is colored by a summary

     ![Format Rectangle dialog - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404901338647/cmpnt_cht_frmt_rctgl2.gif)

     Specify the start color for the minimum value and the end color for the maximum value of the summary respectively on the gradient color bar. To exchange the start color and the end color, check **Reversed** (by default the option is unchecked and the start/end color here corresponds to the start/end color on the [chart object](https://devnet.logianalytics.com/hc/en-us/articles/1500010069721-Chart-Properties#EndColor) in the Report Inspector; when it is checked, the start/end color here corresponds to the end/start color on the chart object). If you want to specify a color for the zero value, check **Color When Zero** and define the color accordingly, then the gradient color will change from the start color to the zero value color, and then from the zero value color to the end color. You can also specify a color for the null values.

   If you select Use Single Color with Condition to fill the rectangles, specify the conditions and the color pattern bound with each condition respectively. For details, refer to [Adding Conditional Color Fills to Charts](https://devnet.logianalytics.com/hc/en-us/articles/1500010063341-Applying-Conditional-Color-Fills-to-Charts).
3. In the Separator tab, specify the color, transparency, line style and thickness of the lines separating the rectangles. Note that you will get a bad layout in the preview result in Logi JReport Designer and in the exported result when the separator thickness is set to a big value.

   ![Format Rectangle dialog - Separator](https://devnet.logianalytics.com/hc/article_attachments/4404909201303/fmtrctgl_sprtr.gif)
4. For a heat map chart in a library component, you can define web behaviors on the rectangles in the Behaviors tab.

   ![Format Rectangle dialog for library component - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404909201559/fmtrctgl_bhvr.gif)

   Select a [trigger event](https://devnet.logianalytics.com/hc/en-us/articles/1500010029382-Using-Basic-Web-Controls-in-a-Report#Event) from the drop-down list in the Events column, then select in the Actions column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404909121559/btn_chsr1.gif) that appears in the text box. In the Web Action List dialog, bind a web action to the rectangles [the same as you do to web controls](https://devnet.logianalytics.com/hc/en-us/articles/1500010029382-Using-Basic-Web-Controls-in-a-Report#Action) in the library component, which will be triggered when the specified event occurs on the rectangles. The web actions you can bind include Parameter, Filter, Sort, Change Property and Send Message.

   To add more web behaviors, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif) and define them as required; if a web behavior is not required, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif). Select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif) to adjust the order of the behaviors, then at runtime when an event that has been bound with more than one action happens, the upper action will be triggered first.
5. Select **OK** to accept the changes and close the dialog.

## Formatting the Titles for Rectangles in a Heat Map

1. When there is only one group in the heat map, right-click on the heat map and select **Format Rectangle Title** from the shortcut menu to bring up the [Format Rectangle Title](https://devnet.logianalytics.com/hc/en-us/articles/1500010066521-Format-Rectangle-Title-Dialog) dialog.

   When there are two or more groups in the heat map, right-click on the heat map, then from the Format Rectangle Title submenu, select a desired group to bring up the Format Rectangle Title dialog for the group.
2. In the General tab, specify the height, fill color, and font color of the rectangle titles (to change a color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010035022-Menu-Tabs#Palette) or input the hexadecimal value of a color directly in the text box).

   ![Format Rectangle Title dialog - General](https://devnet.logianalytics.com/hc/article_attachments/4404909200535/fmtrctglttl_gnrl.gif)
3. In the Font tab, set the font settings for the titles.

   ![Format Rectangle Title dialog - Font](https://devnet.logianalytics.com/hc/article_attachments/4404909200791/fmtrctglttl_font.gif)
4. In the Border tab, set the border color, thickness, line styles, and whether the borders have shadow effect and the shadow color if yes.

   ![Format Rectangle Title dialog - Border](https://devnet.logianalytics.com/hc/article_attachments/4404909201047/fmtrctglttl_brdr.gif)
5. Select **OK** to accept the changes and close the dialog.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010028822-Formatting-the-Bullets-in-a-Bullet-Chart) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010028842-Formatting-the-Gauge-in-a-Gauge-Chart)
