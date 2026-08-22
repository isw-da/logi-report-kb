---
title: "Formatting the Pies/Donuts and KPI Value Labels in a Pie/Donut Chart"
id: 1500009605902
section: "Working with Components in Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009605902-Formatting-the-Pies-Donuts-and-KPI-Value-Labels-in-a-Pie-Donut-Chart
updated_at: 2021-07-24T16:05:19Z
---

# Formatting the Pies/Donuts and KPI Value Labels in a Pie/Donut Chart

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009605722-Formatting-the-Areas-in-an-Area-Chart)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009605722-Formatting-the-Areas-in-an-Area-Chart) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009605782-Formatting-the-Bubbles-in-a-Bubble-Chart)

# Formatting the Pies/Donuts and KPI Value Labels in a Pie/Donut Chart

For a pie/donut chart, you can format the pies/donuts of the chart, and if the chart shows KPI values, you can also format the KPI value labels as you want.

This topic includes the following sections:

* [Formatting Pies/Donuts](#Pie)
* [Formatting KPI Value Labels](#KPIValue)

## Formatting Pies/Donuts

1. Right-click any pie/donut in the pie/donut chart and select **Format Pie**/**Donut** on the shortcut menu, or double-click any pie/donut in the chart. The [Format Pie](https://devnet.logianalytics.com/hc/en-us/articles/1500009608522-Format-Pie-Dialog) dialog or [Format Donut](https://devnet.logianalytics.com/hc/en-us/articles/1500009608422-Format-Donut-Dialog) dialog appears.

   ![Format Pie dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404904300951/fmtpie_gnrl.gif)
2. In the General tab, set the general settings for the pies/donuts.

   In the Gap Amount text box, type a number to set the distance between every two adjacent pies/donuts. In the Explode Amount text box, type a number to specify the distance between the sections in each pie/donut and the pie/donut center. For a donut chart, you can also specify the radius percentage of the donut hole to the total pie circle by setting the Donut Hole option.

   When the chart property [Swap Groups](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#SwapGroups) is not true, the KPI Value box is activated. You can select the **Show KPI Value** option to display KPI value for each pie/donut. By default, the total value of each pie/donut will be used as the KPI value. If you want to customize the value, clear **Auto** and type a value in the text box, or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404904189591/btn_fmla.gif) and select a formula or summary from the drop-down list to use its value as the KPI value. KPI values are calculated based on series if the chart contains series field, otherwise based on the total value. From the Position drop-down list, select the position of the KPI value relative to the pies/donuts. When you specify to show KPI value on the chart, you can further [format the KPI value labels](#KPIValue) according to your requirements.
3. In the Fill tab, specify the fill type: Use Single Color or Use Single Color with Condition.

   ![Format Pie dialog - Fill tab](https://devnet.logianalytics.com/hc/article_attachments/4404904301207/fmtpie_fill.gif)

   If you select Use Single Color as the fill type, first make a choice for the Self Settings checkbox: when Self Settings is unselected, the color pattern specified here will be synchronized to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#Pattern) on the chart object in the Report Inspector, which can also be applied by data markers of other subtypes if the chart is a combo chart; when Self Settings is selected, it indicates the color pattern is private to the current data markers themselves (the pies/donuts in this case), which can be remembered and applied to the data markers of a new type automatically if later you change the type of the chart. Then specify the color and the transparency of the color schema to fill the pie/donut sections in the current data series, that is the sections in the same data series as the one you have selected on to open the Format Pie dialog (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box). You can also select the **Color List** button to specify the color pattern for pie/donut sections in each data series respectively in the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009630161-Color-List-Dialog) dialog.

   If you select Use Single Color with Condition, specify the conditions and the color pattern bound with each condition respectively. For details, refer to [Adding Conditional Color Fills to Charts](https://devnet.logianalytics.com/hc/en-us/articles/1500009605602-Applying-Conditional-Color-Fills-to-Charts).
4. In the Border tab, select **Show Border** to show the border of the pie/donut sections, then set properties of the border including the border color, transparency, line style, thickness, end caps style, and line joint mode. You can also specify whether the border is to be outlined, and whether or not to automatically resize the border dashes if the border is drawn with dashes.

   ![Format Pie dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4404904301463/fmtpie_border.gif)
5. In the Data Label tab, select **Show Static Data Label** if you want to show static data labels on the pie/donut sections, then decide the position of the labels relative to the sections, the display type for data values in the labels, the color of the thin lines that are used to point to the static data labels, and whether to scale big and small numbers, hide the label whose value is 0, ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404911621015/___newv17.jpg "New for version 17.")and truncate labels that would go beyond the boundaries on the chart paper. In the Font and Effects boxes, set the font formats and effects of the data labels.

   ![Format Pie dialog - Data Label tab](https://devnet.logianalytics.com/hc/article_attachments/4404916792855/fmtpie_data.gif)
6. In the Hint tab, specify whether to
   include the category and series values and whether to scale big and small numbers in the pie/donut hint. A hint displays the value a section in the pie/donut chart represents when the mouse pointer points at the section in Logi Report Designer view mode, in HTML result, or at server runtime. To make the hint shown, you need to make sure the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/1500009612142-Chart-Paper-Properties#ShowTips) property in the Report Inspector is set to true.

   ![Format Pie - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404904301719/fmtpie_hint.gif)
7. For a pie/donut chart in a library component, you can define web behaviors on the pies/donuts in the Behaviors tab.

   ![Format Pie dialog for library component - Behaviors tab](https://devnet.logianalytics.com/hc/article_attachments/4404904301975/fmtpie_bhvr.gif)

   Select a [trigger event](https://devnet.logianalytics.com/hc/en-us/articles/1500009629441-Using-Basic-Web-Controls-in-a-Report#Event) from the drop-down list in the Events column, then select in the Actions column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) that appears in the text box. In the Web Action List dialog, bind a web action to the pies/donuts [the same as you do to web controls](https://devnet.logianalytics.com/hc/en-us/articles/1500009629441-Using-Basic-Web-Controls-in-a-Report#Action) in the library component, which will be triggered when the specified event occurs on the pies/donuts. The web actions you can bind include Parameter, Filter, Sort, Change Property and Send Message.

   To add more web behaviors, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) and define them as required; if a web behavior is not required, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif). Select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif) to adjust the order of the behaviors, then at runtime when an event that has been bound with more than one action happens, the upper action will be triggered first.
8. Select **OK** to accept the changes and close the dialog.

## Formatting KPI Value Labels

When a pie/donut chart displays KPI values, you can customize the KPI value labels, for example, edit the size and border of the labels, change the label font size, font color, and so on.

1. Right-click the KPI value for any pie/donut and select **Format KPI Label** from the shortcut menu, or double-click the KPI value for any pie/donut. The [Format KPI Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009631421-Format-KPI-Label-Dialog) dialog appears.

   ![Format KPI Label - General](https://devnet.logianalytics.com/hc/article_attachments/4404904311831/fmtkpilbl_gnrl.gif)
2. In the General tab, set the general information for the labels.

   In the Size box, set the width and height of the labels, the horizontal and vertical coordinate of the top left corner of the labels, relative to their parent container, the alignment of the label text, and whether to enable the word wrap function for the label text.

   In the Fill box, specify the fill color and color transparency to fill the labels.

   In the Border box, specify the properties for borders of the labels, including the type, color, line style, transparency, thickness, ending style, line joint style, fill pattern and dash size.

   In the Orientation box, specify the angle of the labels so as to rotate them.
3. In the Font tab, format the font of the labels, including the font face, size, color, transparency, rotation angle, shearing angle, and effects such as style, strikethrough, underline, and so on.

   ![Format KPI Label - Font](https://devnet.logianalytics.com/hc/article_attachments/4404904312471/fmtkpilbl_font.gif)
4. In the Format tab, specify the data format of the labels.

   ![Format KPI Label - Format](https://devnet.logianalytics.com/hc/article_attachments/4404904313239/fmtkpilbl_fmt.gif)

   Select a category from the Category box, then select a format from the Format box and select **Add** to add it to the Stack box. If the formats listed in the Format box cannot meet your requirement, define the format in the Properties text box and select **Add** to add it as the format of the selected category. For the Number category, you can specify whether to scale big and small numbers by setting the [Auto Scale in Number](https://devnet.logianalytics.com/hc/en-us/articles/1500009631421-Format-KPI-Label-Dialog#AutoScale) option. You can add more than one format, but for each category only one format can be added. In the event that a format is not necessary, select it in the Stack box select **Remove** to clear it.
5. Select **OK** to accept the changes and close the dialog.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009605722-Formatting-the-Areas-in-an-Area-Chart) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009605782-Formatting-the-Bubbles-in-a-Bubble-Chart)
