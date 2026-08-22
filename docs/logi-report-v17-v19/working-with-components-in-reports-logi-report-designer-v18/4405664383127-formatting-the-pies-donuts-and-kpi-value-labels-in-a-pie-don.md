---
title: "Formatting the Pies/Donuts and KPI Value Labels in a Pie/Donut Chart"
id: 4405664383127
section: "Working with Components in Reports - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664383127-Formatting-the-Pies-Donuts-and-KPI-Value-Labels-in-a-Pie-Donut-Chart
updated_at: 2022-01-27T20:35:06Z
---

# Formatting the Pies/Donuts and KPI Value Labels in a Pie/Donut Chart

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664374935-Formatting-the-Areas-in-an-Area-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661354135-Formatting-the-Bubbles-in-a-Bubble-Chart)

# Formatting the Pies/Donuts and KPI Value Labels in a Pie/Donut Chart

This topic describes how you can format the pies/donuts of a pie/donut chart, and the KPI value labels when the chart shows KPI values.

This topic contains the following sections:

* [Formatting Pies/Donuts](#Pie)
* [Formatting KPI Value Labels](#KPIValue)

## Formatting Pies/Donuts

1. Right-click any pie/donut in the pie/donut chart and select **Format Pie**/**Format Donut** on the shortcut menu, or double-click any section in a pie/donut in the chart. Designer displays the [Format Pie dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661581335-Format-Pie-Dialog-Box) or [Format Donut dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661569943-Format-Donut-Dialog-Box).

   ![Format Pie dialog box - General tab](https://devnet.logianalytics.com/hc/article_attachments/4420550987159/fmtpie_gnrlv18.2.gif)
2. In the **General** tab, set the general properties of the pies/donuts.

   In the **Gap Amount** text box, specify the distance between every two adjacent pies/donuts. In the **Explode Amount** text box, specify the distance between the sections in each pie/donut and the pie/donut center. For a donut chart, you can also specify the radius percentage of the donut hole to the total donut circle by setting the **Donut Hole** option.

   When you do not set the chart property [Swap Groups](https://devnet.logianalytics.com/hc/en-us/articles/4405664650263-Chart-Properties#SwapGroups) to "true" in the Report Inspector, Designer enables the options in the **KPI Value** box. You can select **Show KPI Value** to display KPI value for each pie/donut. By default, Designer uses the total value of each pie/donut as the KPI value; if you want to customize the value, clear **Auto** and type a value in the text box, or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4420556102807/btn_fmla.gif) and select a formula or summary from the drop-down list to use its value as the KPI value. Designer calculates KPI values based on series if the chart contains series field; otherwise based on the total value. From the **Position** drop-down list, select the position of the KPI value relative to the pies/donuts; if you select **customized**, you can specify the position by dragging any KPI value in the pie/donut chart. When you specify to show KPI value in the chart, you can further [format the KPI value labels](#KPIValue) according to your requirements.

   In the **Angle** box, specify the rotation angle of the pies/donuts around the X and Y axes.
3. In the **Fill** tab, specify the fill type and the color pattern to fill the pies/donuts.

   ![Format Pie dialog box - Fill tab](https://devnet.logianalytics.com/hc/article_attachments/4420556251799/fmtpie_fill.gif)

   If you select the **Use Single Color** fill type, first make a choice for the **Self Settings** checkbox: when Self Settings is cleared (the default behavior), Designer synchronizes the color pattern that you specify here with the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/4405664650263-Chart-Properties#Pattern) on the chart object in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart; when you select Self Settings, it indicates that the color pattern is private to the current data markers themselves (the pies/donuts in this case), which Designer remembers and applies to the data markers of a new type automatically if later you change the type of the chart. Then, specify the color and the transparency of the color to fill the pie/donut sections in the current data series, that is, the sections in the same data series as the one you have selected on to open the Format Pie or Format Donut dialog box (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box). You can also select **Color List** to specify the color pattern for pie/donut sections in each data series respectively in the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661476887-Color-List-Dialog-Box).

   If you select the **Use Single Color with Condition** fill type, specify the conditions and the color pattern for each condition respectively. For more information, see [Adding Conditional Color Fills to Charts](https://devnet.logianalytics.com/hc/en-us/articles/4405664369943-Applying-Conditional-Color-Fills-to-Charts).
4. In the **Border** tab, specify properties for the border of the pie/donut sections.

   ![Format Pie dialog box - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4420542213527/fmtpie_border.gif)

   Select **Show Border** if you want to show the border of the pie/donut sections, then specify the color, color transparency, line style, thickness, end caps style, and line joint mode of the border.

   In the **Path** box, specify the fill pattern of the border: Outline Path or Fill Path.

   In the **Dash** box, select to automatically adjust the dash size or use fixed dash size if you select a dash line style for the border.
5. In the **Data Label** tab, specify properties of the static data labels in the pie/donut chart.

   ![Format Pie dialog box - Data Label tab](https://devnet.logianalytics.com/hc/article_attachments/4420556252055/fmtpie_data.gif)

   In the **Static Data Label** box, select **Show Static Data Label** if you want to show static data labels for the pie/donut sections, then select the position of the data labels relative to the pie/donut sections, in which way to display the values in the data labels, whether to scale big and small numbers in the data labels, the color of the line pointing to the static data labels, and whether to hide the data label whose value is 0. Select **Show Truncated Label** if you want to truncate the static data labels that go beyond the boundaries of the chart paper instead of them being hidden altogether (the default behavior). Designer then displays an ellipsis (…) from the right side of the label, along with part of the name instead of the entire name. The truncated labels are also affected if you select the Position option as "best fit", where the label is cut off from the left or the right depending on the position of the label.

   In the **Font** box, specify the font format of the text in the data labels, including the font face, size, color, color transparency, rotation angle, shearing angle.

   In the **Effects** box, specify the special effects for the text in the data labels such as style, strikethrough, and underline.
6. In the **Hint** tab, specify options of the chart hint (the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/4405661845015-Chart-Paper-Properties#ShowTips) property of the chart paper in the Report Inspector should be "true" if you want to show the hint): specify whether to include the category and series values in the hint, whether to scale big and small numbers, and whether to use customized names for the fields on the value axis in the hint, and customize the names as you want. A hint displays the value a section in the pie/donut chart represents when you point to the section in Designer view mode, in HTML output, or at runtime.

   ![Format Pie - Hint](https://devnet.logianalytics.com/hc/article_attachments/4420556252695/fmtpie_hint.gif)
7. For a pie/donut chart in a library component, you can define web behaviors on the pies/donuts in the **Behaviors** tab. A web behavior contains a trigger event and a web action to be triggered when the event occurs on the pies/donuts at runtime. You can add as many web behaviors to the pies/donuts as you need.

   ![Format Pie dialog box - Behaviors tab](https://devnet.logianalytics.com/hc/article_attachments/4420542213911/fmtpie_bhvr.gif)

   To define the web behavior, select a [trigger event](https://devnet.logianalytics.com/hc/en-us/articles/4405661415703-Using-Basic-Web-Controls-in-a-Report#Event) from the drop-down list in the **Events** column, then select in the **Actions** column and select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420550841879/btn_ellipsis1.gif). In the Web Action List dialog box, bind a web action [the same as you do to web controls](https://devnet.logianalytics.com/hc/en-us/articles/4405661415703-Using-Basic-Web-Controls-in-a-Report#Action) in the library component. The web actions you can bind include Filter, Sort, Parameter, Property, and SendMessage.

   You can select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif) to add and define more web behaviors; to delete a web behavior, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420542080407/btn_trashcan.gif). You can also select a web behavior and select **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420542078103/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420542078359/btn_mvdwn.gif) to adjust the order of the behaviors, then at runtime, when an event that is bound with more than one action happens, JDashboard triggers the upper action first.
8. Select **OK** to accept the changes and close the dialog box.

## Formatting KPI Value Labels

When a pie/donut chart displays KPI values, you can customize the KPI value labels, for example, edit the size and border of the labels, change the label font size, font color, and so on.

**To format the KPI value labels of a pie/donut chart**

1. Right-click the KPI value for any pie/donut and select **Format KPI Label** on the shortcut menu, or double-click the KPI value for any pie/donut. Designer displays the [Format KPI Label dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661576215-Format-KPI-Label-Dialog-Box).

   ![Format KPI Label - General](https://devnet.logianalytics.com/hc/article_attachments/4420542133271/fmtkpilbl_gnrl.gif)
2. In the **General** tab, specify the general properties of the labels in the chart.

   In the **Size** box, set the width and height of the labels, the horizontal and vertical coordinate of the top left corner of the labels relative to their parent container, the alignment of the text in the labels, and whether to enable the word wrap function for the label text.

   In the **Fill** box, specify the color or effects and the transparency to fill the labels.

   In the **Border** box, specify properties for the border of the labels, including the type, color, line style, color transparency, thickness, ending style, line joint style, fill pattern, and dash size.

   In the **Orientation** box, specify the angle to rotate the labels.
3. In the **Font** tab, specify the font properties of the labels, including the font face, size, color, color transparency, rotation angle, shearing angle, and the font effects such as style, strikethrough, and underline.

   ![Format KPI Label - Font](https://devnet.logianalytics.com/hc/article_attachments/4420550904599/fmtkpilbl_font.gif)
4. In the **Format** tab, specify the data format of the labels.

   ![Format KPI Label - Format](https://devnet.logianalytics.com/hc/article_attachments/4420542133911/fmtkpilbl_fmt.gif)

   Select a category from the **Category** box, then select a format from the **Format** box and select **Add** to add it to the **Stack** box (for more information about each format, [select here](https://devnet.logianalytics.com/hc/en-us/articles/4405664452759-Data-Format-Dialog-Box#DataFormat)). If the formats that Designer provides in the Format box cannot meet your requirement, you can define the format in the **Properties** text box and add it as the format of the selected category. You can add more than one format, but for each category, only one format is allowed. If you do not need a format anymore, select it in the Stack box and select **Remove** to clear it.

   Set the **Auto Scale in Number** option to specify whether to automatically scale the big and small Number values.
5. Select **OK** to accept the changes and close the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664374935-Formatting-the-Areas-in-an-Area-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661354135-Formatting-the-Bubbles-in-a-Bubble-Chart)
