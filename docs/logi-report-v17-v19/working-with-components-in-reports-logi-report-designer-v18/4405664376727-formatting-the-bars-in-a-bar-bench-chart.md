---
title: "Formatting the Bars in a Bar/Bench Chart"
id: 4405664376727
section: "Working with Components in Reports - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664376727-Formatting-the-Bars-in-a-Bar-Bench-Chart
updated_at: 2022-01-27T20:34:23Z
---

# Formatting the Bars in a Bar/Bench Chart

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664380951-Formatting-the-Labels)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661359255-Formatting-the-Lines-in-a-Line-Chart)

# Formatting the Bars in a Bar/Bench Chart

This topic describes how you can format the bars in a bar or bench chart.

1. Right-click any bar/bench in the bar/bench chart and select **Format 2D Bar** or **Format 3D Bar** from the shortcut menu, or double-click any bar/bench in the chart. Designer displays the [Format Bar dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661559447-Format-Bar-Dialog-Box).
2. In the **General** tab, specify the general properties of the bars.
   * For a 2-D bar/bench chart, specify the style and layout of the bars. If you want to add a 3-dimensional effect to the bars, set **Use Depth** to **true** and specify the depth and direction. If the chart uses a query resource, you can [use a formula to control](https://devnet.logianalytics.com/hc/en-us/articles/4405664601367-Using-Formulas-to-Control-Object-Properties) the Use Depth option.

     ![Format Bar dialog box - General 2-D](https://devnet.logianalytics.com/hc/article_attachments/4420556184599/fmtbar_gnrl_1.gif)
   * For a 3-D bar/bench chart, specify the bar width as a percentage of the unit width, and the layout of the bars.

     ![Format Bar dialog box - General 3-D](https://devnet.logianalytics.com/hc/article_attachments/4420542145815/fmtbar_gnrl_2.gif)
3. For a 2-D bar/bench chart, in the **Size** tab, specify the size of the bars which can either be dynamic or fixed.

   To use dynamic bar width, make sure **Fixed Bar Width** is cleared, specify the general bar width as a percentage of the unit width. If the chart is a clustered 2-D bar/bench chart which contains data on the series axis or has more than one value on the value axis, you can specify the gap between the bars as a percentage of the unit width, and in the **Individual Bar Width** box, specify how much the selected bars in the same data series is wider or narrower than a general bar in percentage. You can also select **Size List** to specify the size for bars in the same data series respectively in the [Size List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664568343-Size-List-Dialog-Box).

   ![Format Bar dialog box - Size tab for Dynamic Bar Width](https://devnet.logianalytics.com/hc/article_attachments/4420542146071/fmtbar_size_dynmc.gif)

   To use fixed bar width, select **Fixed Bar Width**, specify the general bar width. If the chart is a clustered 2-D bar/bench chart which contains data on the series axis or has more than one value on the value axis, you can specify the gap between the bars within a group, and the outer gap between bars out of a group. In the **Individual Bar Width** box, specify the width and gap for the selected bars in the same data series, or select **Size List** to specify the size for bars in the same data series respectively in the [Size List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664568343-Size-List-Dialog-Box). You can [use formulas to control](https://devnet.logianalytics.com/hc/en-us/articles/4405664601367-Using-Formulas-to-Control-Object-Properties) the options. To customize the bar gap by percentage, clear **Fixed Bar Gap** and specify the percentages of the bar width and bar gap within a group.

   ![Format Bar dialog box - Size tab for Fixed Bar Width](https://devnet.logianalytics.com/hc/article_attachments/4420556185367/fmtbar_size_fix.gif)
4. In the **Fill** tab, specify the fill type and the color pattern to fill the bars.

   ![Format Bar dialog box - Fill](https://devnet.logianalytics.com/hc/article_attachments/4420550915607/fmtbar_fill.gif)

   If you select the **Use Single Color** fill type, first make a choice for the **Self Settings** checkbox: when Self Settings is cleared (the default behavior), Designer synchronizes the color pattern that you specify here with the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/4405664650263-Chart-Properties#Pattern) on the chart object in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart; when you select Self Settings, it indicates that the color pattern is private to the current data markers themselves (the bars in this case), which Designer remembers and applies to the data markers of a new type automatically if later you change the type of the chart. Then, specify the color pattern as follows:

   * If the chart has no series field, specify the color and the transparency of the color to fill the bars (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box). If you want to apply different colors to the bars, select **Vary Colors by Color List**, then select **Color List** to specify the color pattern for each bar in the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661476887-Color-List-Dialog-Box).
   * If the chart has series field, specify the color and transparency of the color to fill the bars in the current data series, that is the bars in the same data series as the one you have selected on to open the Format Bar dialog box. You can also select **Color List** to specify the color pattern for bars in each data series respectively in the Color List dialog box if the chart is a clustered bar chart.

   If you select the **Use Single Color with Condition** or **Use Multiple Color with Condition** fill type, specify the conditions and the color pattern for each condition respectively. For more information, see [Adding Conditional Color Fills to Charts](https://devnet.logianalytics.com/hc/en-us/articles/4405664369943-Applying-Conditional-Color-Fills-to-Charts).
5. In the **Border** tab, specify properties for the border of the bars/benches.

   ![Format Bar dialog box - Border](https://devnet.logianalytics.com/hc/article_attachments/4420556185623/fmtbar_border.gif)

   Select **Show Border** if you want to show the border of the bars, then specify the color, color transparency, line style, thickness, end caps style, and line joint mode of the border.

   In the **Path** box, specify the fill pattern of the border: Outline Path or Fill Path.

   In the **Dash** box, select to automatically adjust the dash size or use fixed dash size if you select a dash line style for the border.
6. In the **Data Label** tab, specify properties of the static data labels in the bar chart.

   ![Format Bar dialog box - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4420556186007/fmtbar_data.gif)

   For a 2-D bar/bench chart, in the **Static Data Label** box, select **Show Static Data Label** if you want to show static data labels for the bars, then select the position of the data labels relative to the bars, in which way to display the values in the data labels, whether to scale big and small numbers in the data labels, and whether to hide the data label whose value is 0. When you select the Position option of "inside center", "inside top", or "inside bottom", Designer enables the **Auto Arrange** drop-down list, from which you can specify whether to display the data labels inside the bars at the best position.

   In the **Font** box, specify the font format of the text in the data labels, including the font face, size, color, color transparency, rotation angle, shearing angle.

   In the **Effects** box, specify the special effects for the text in the data labels such as style, strikethrough, and underline.
7. In the **Hint** tab, specify options of the chart hint (the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/4405661845015-Chart-Paper-Properties#ShowTips) property of the chart paper in the Report Inspector should be "true" if you want to show the hint): specify whether to include the category and series values in the hint, whether to scale big and small numbers, and whether to use customized names for the fields on the value axis in the hint, and customize the names as you want. A hint displays the value a bar represents when you point to the bar in Designer view mode, in HTML output, or at runtime.

   ![Format Bar dialog box - Hint](https://devnet.logianalytics.com/hc/article_attachments/4420550916119/fmtbar_hint.gif)
8. For a bar chart in a library component, you can define web behaviors on the bars in the **Behaviors** tab. A web behavior contains a trigger event and a web action to be triggered when the event occurs on the bars at runtime. You can add as many web behaviors to the bars as you need.

   ![Format Bar dialog box - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4420550916375/fmtbar_bhvr.gif)

   To define the web behavior, select a [trigger event](https://devnet.logianalytics.com/hc/en-us/articles/4405661415703-Using-Basic-Web-Controls-in-a-Report#Event) from the drop-down list in the **Events** column, then select in the **Actions** column and select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420550841879/btn_ellipsis1.gif). In the Web Action List dialog box, bind a web action [the same as you do to web controls](https://devnet.logianalytics.com/hc/en-us/articles/4405661415703-Using-Basic-Web-Controls-in-a-Report#Action) in the library component. The web actions you can bind include Filter, Sort, Parameter, Property, and SendMessage.

   You can select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif) to add and define more web behaviors; to delete a web behavior, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420542080407/btn_trashcan.gif). You can also select a web behavior and select **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420542078103/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420542078359/btn_mvdwn.gif) to adjust the order of the behaviors, then at runtime, when an event that is bound with more than one action happens, JDashboard triggers the upper action first.
9. Select **OK** to accept the changes and close the dialog box.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg)

* If the chart is a combo chart composed by bars and areas/lines, when you set the depth properties for the bars, Designer applies them to the areas/lines as well, and vice versa.
* If you set the style of the bars to "Cylinder", the style can take effect only when you specify Use Depth to "true" at the same time.
* For a 3-D bar chart, Designer disables the Show Static Data Label option in the Data Label tab of the Format Bar dialog box; however, you can still see the data labels by pointing to the bars when viewing the report in Designer view mode, in HTML output, or in Page Report Studio.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664380951-Formatting-the-Labels)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661359255-Formatting-the-Lines-in-a-Line-Chart)
