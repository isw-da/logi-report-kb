---
title: "Formatting the Areas in an Area Chart"
id: 1500010063381
section: "Working with Components in Reports - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010063381-Formatting-the-Areas-in-an-Area-Chart
updated_at: 2021-07-24T10:39:28Z
---

# Formatting the Areas in an Area Chart

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010028882-Formatting-the-Lines-in-a-Line-Chart) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010063521-Formatting-the-Pies-Donuts-and-KPI-Value-Labels-in-a-Pie-Donut-Chart)

# Formatting the Areas in an Area Chart

This topic introduces how to format the area of an area chart.

1. Right-click any area in the area chart and select **Format 2D Area** or **Format 3D Area** on the shortcut menu, or double-click any area in the chart. The [Format Area](https://devnet.logianalytics.com/hc/en-us/articles/1500010066221-Format-Area-Dialog) dialog appears.

   ![Format Area dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404901257111/fmtarea_gnrl_1.gif)
2. In the General tab, set the layout style of the area chart. Check **Ignore Null Value** if you want the areas to be drawn from the previous data values to the next data values directly when null data values appear to avoid breaks on the areas.

   For a 2-D area chart, if you want to add a 3-dimensional effect to the areas, set the Use Depth option to **true** and specify the depth and direction as required. If the chart uses a query resource, you can [use a formula to control](https://devnet.logianalytics.com/hc/en-us/articles/1500010033202-Using-Formulas-to-Control-Object-Properties) the Use Depth option. You can also set to show the lines that represent the data categories by checking High-Low Lines.
3. In the Fill tab, specify the fill type: Use Single Color or Use Multiple Colors with Condition.

   ![Format Area dialog - Fill tab](https://devnet.logianalytics.com/hc/article_attachments/4404901257623/fmtarea_fill.gif)

   If you select Use Single Color as the fill type, first make a choice for the Self Settings checkbox: when Self Settings is unchecked, the color pattern specified here will be synchronized to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500010069721-Chart-Properties#Pattern) on the chart object in the Report Inspector, which can also be applied by data markers of other subtypes if the chart is a combo chart; when Self Settings is checked, it indicates the color pattern is private to the current data markers themselves (the areas in this case), which can be remembered and applied to the data markers of a new type automatically if later you change the type of the chart. Then specify the color pattern as follows: set the color and the transparency of the color schema to fill the current area, that is the area you have right-clicked on to open the Format Area dialog (to change the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010035022-Menu-Tabs#Palette) or input the hexadecimal value of a color directly in the text box), or select the **Color List** button to specify the color pattern for each area in the area chart using the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500010030022-Color-List-Dialog) dialog.

   If you select Use Multiple Colors with Condition as the fill type (only applied to Area 2-D and Area 3-D types), specify the conditions and the color pattern bound with each condition respectively. For details, refer to [Adding Conditional Color Fills to Charts](https://devnet.logianalytics.com/hc/en-us/articles/1500010063341-Applying-Conditional-Color-Fills-to-Charts).
4. In the Border tab, check **Show Border** if you want to show the border of the areas, then set properties of the border including the color, transparency, line style, thickness, end caps style and line joint mode. You can also specify whether the border is to be outlined, and whether or not to automatically resize the border dashes if the border is drawn with dashes.

   ![Format Area dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4404901257879/fmtarea_border.gif)
5. In the Data Label tab, check **Show Static Data Label** if you want to show static data labels on the area nodes, then decide the position of the labels relative to the area nodes, the display type for data values in the labels, whether to scale big and small numbers, and whether to hide the label whose value is 0. In the Font and Effects boxes, set the font formats and effects of the data labels.

   ![Format Area dialog - Data Label tab](https://devnet.logianalytics.com/hc/article_attachments/4404901258135/fmtarea_data.gif)
6. In the Hint tab, specify whether to
   include the category and series values and whether to scale big and small numbers in the area hint. A hint displays the value an area represents when the mouse pointer points at the area in Logi JReport Designer view mode, in HTML result, or at server runtime. To make the hint shown, you need to make sure the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/1500010033982-Chart-Paper-Properties#ShowTips) property in the Report Inspector is set to true.

   ![Format Area dialog - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404901258391/fmtarea_hint.gif)
7. For an area chart in a library component, you can define web behaviors on the areas in the Behaviors tab.

   ![Format Area dialog for library component - Behaviors tab](https://devnet.logianalytics.com/hc/article_attachments/4404901258647/fmtarea_bhvr.gif)

   Select a [trigger event](https://devnet.logianalytics.com/hc/en-us/articles/1500010029382-Using-Basic-Web-Controls-in-a-Report#Event) from the drop-down list in the Events column, then select in the Actions column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404909121559/btn_chsr1.gif) that appears in the text box. In the Web Action List dialog, bind a web action to the areas [the same as you do to web controls](https://devnet.logianalytics.com/hc/en-us/articles/1500010029382-Using-Basic-Web-Controls-in-a-Report#Action) in the library component, which will be triggered when the specified event occurs on the areas. The web actions you can bind include Parameter, Filter, Sort, Change Property and Send Message.

   To add more web behaviors, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif) and define them as required; if a web behavior is not required, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif). Select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif) to adjust the order of the behaviors, then at runtime when an event that has been bound with more than one action happens, the upper action will be triggered first.
8. Select **OK** to accept the changes and close the dialog.

**Notes:**

* If the chart is a combo chart composed by areas and bars/lines, when you set the depth properties for the areas, they will be applied to the bars/lines as well, and vice versa.
* For 3-D charts, the Show Static Data Label checkbox in the Data Label tab is grayed out. However, you can still see the data labels by moving the mouse pointer over the areas when viewing the report result in Logi JReport Designer view mode, in HTML format, or in Page Report Studio.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010028882-Formatting-the-Lines-in-a-Line-Chart) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010063521-Formatting-the-Pies-Donuts-and-KPI-Value-Labels-in-a-Pie-Donut-Chart)
