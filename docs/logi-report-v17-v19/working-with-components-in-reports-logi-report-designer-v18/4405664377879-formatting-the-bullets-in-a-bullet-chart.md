---
title: "Formatting the Bullets in a Bullet Chart"
id: 4405664377879
section: "Working with Components in Reports - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664377879-Formatting-the-Bullets-in-a-Bullet-Chart
updated_at: 2022-01-27T20:34:24Z
---

# Formatting the Bullets in a Bullet Chart

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661356695-Formatting-the-Indicators-in-an-Indicator-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664384279-Formatting-the-Rectangles-and-Rectangle-Titles-in-a-Heat-Map)

# Formatting the Bullets in a Bullet Chart

This topic describes how you can format the bullets in a bullet chart.

1. Right-click any bullet in the bullet chart and select **Format Bullet** from the shortcut menu, or double-click any bullet in the chart. Designer displays the [Format Bullet dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664486807-Format-Bullet-Dialog-Box).

   ![Format Bullet dialog box - General](https://devnet.logianalytics.com/hc/article_attachments/4420556260887/fmtbult_gnrl.gif)
2. In the **General** tab, specify the size of the bullets by setting the width of the featured measure, comparative measure, and qualitative ranges respectively.
3. In the **Fill** tab, set the color pattern to fill the bullets.

   ![Format Bullet dialog box - Fill](https://devnet.logianalytics.com/hc/article_attachments/4420556261271/fmtbult_fill.gif)

   In the **Featured Measure Color List** box, first decide whether to define the color pattern on the featured measures themselves by using the **Self Settings** checkbox: when Self Settings is cleared (the default behavior), Designer synchronizes the color pattern that you specify here with the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/4405664650263-Chart-Properties#Pattern) on the chart object in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart; when you select Self Settings, it indicates that the color pattern is private to the current data markers themselves (the bullets in this case), which Designer remembers and applies to the data markers of a new type automatically if later you change the type of the chart. Then, specify the color pattern as follows: set the color and the transparency of the color to fill all the featured measures (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box); if you want to apply different colors to the featured measures, select **Vary Colors by Color List**, then select **Color List** to specify the color pattern for each featured measure in the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661476887-Color-List-Dialog-Box).

   In the **Comparative Measure Color List**/ **Qualitative Ranges Color List** box, specify the color and the transparency of the color to fill the selected comparative measures/qualitative ranges in the same data series, or select **Color List** to specify the color pattern for comparative measures/qualitative ranges in the same data series respectively.
4. In the **Border** tab, specify properties for the border of the bullets.

   ![Format Bullet dialog box - Border](https://devnet.logianalytics.com/hc/article_attachments/4420542221207/fmtbult_border.gif)

   Select **Show Border** if you want to show the border of the bullets, then specify the color, color transparency, line style, thickness, end caps style, and line joint mode of the border.

   In the **Path** box, specify the fill pattern of the border: Outline Path or Fill Path.

   In the **Dash** box, select to automatically adjust the dash size or use fixed dash size if you select a dash line style for the border.
5. Skip the Data Label tab because Designer does not support displaying data labels in bullet charts.
6. In the **Hint** tab, specify options of the chart hint (the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/4405661845015-Chart-Paper-Properties#ShowTips) property of the chart paper in the Report Inspector should be "true" if you want to show the hint): specify whether to include the category and series values in the hint, whether to scale big and small numbers, and whether to use customized names for the fields on the value axis in the hint, and customize the names as you want. A hint displays the value a bullet represents when you point to the bullet in Designer view mode, in HTML output, or at runtime.

   ![Format Bullet - Hint](https://devnet.logianalytics.com/hc/article_attachments/4420542221463/fmtbult_hint.gif)
7. For a bullet chart in a library component, you can define web behaviors on the bullets in the **Behaviors** tab. A web behavior contains a trigger event and a web action to be triggered when the event occurs on the bullets at runtime. You can add as many web behaviors to the bullets as you need.

   ![Format Bullet dialog box - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4420556263063/fmtbult_bhvr.gif)

   To define the web behavior, select a [trigger event](https://devnet.logianalytics.com/hc/en-us/articles/4405661415703-Using-Basic-Web-Controls-in-a-Report#Event) from the drop-down list in the **Events** column, then select in the **Actions** column and select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420550841879/btn_ellipsis1.gif). In the Web Action List dialog box, bind a web action [the same as you do to web controls](https://devnet.logianalytics.com/hc/en-us/articles/4405661415703-Using-Basic-Web-Controls-in-a-Report#Action) in the library component. The web actions you can bind include Filter, Sort, Parameter, Property, and SendMessage.

   You can select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif) to add and define more web behaviors; to delete a web behavior, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420542080407/btn_trashcan.gif). You can also select a web behavior and select **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420542078103/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420542078359/btn_mvdwn.gif) to adjust the order of the behaviors, then at runtime, when an event that is bound with more than one action happens, JDashboard triggers the upper action first.
8. Select **OK** to accept the changes and close the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661356695-Formatting-the-Indicators-in-an-Indicator-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664384279-Formatting-the-Rectangles-and-Rectangle-Titles-in-a-Heat-Map)
