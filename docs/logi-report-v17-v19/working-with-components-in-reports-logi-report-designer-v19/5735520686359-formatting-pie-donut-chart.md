---
title: "Formatting Pie/Donut Chart"
id: 5735520686359
section: "Working with Components in Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735520686359-Formatting-Pie-Donut-Chart
updated_at: 2022-11-02T04:28:01Z
---

# Formatting Pie/Donut Chart

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735506840727-Formatting-Area-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735563915671-Formatting-Bubble-Chart)

# Formatting Pie/Donut Chart

This topic describes how you can format the pies/donuts of a pie/donut chart, and the KPI value labels when the chart shows KPI values.

This topic contains the following sections:

* [Formatting Pies/Donuts](#Pie)
* [Formatting KPI Value Labels](#KPIValue)

## Formatting Pies/Donuts

1. Right-click any pie/donut in the pie/donut chart and select **Format Pie**/**Format Donut** on the shortcut menu, or double-click any section in a pie/donut in the chart. Designer displays the [Format Pie dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735542955543-Format-Pie-Dialog-Box) or [Format Donut dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735509250455-Format-Donut-Dialog-Box).

   ![Format Pie dialog box - General tab](https://devnet.logianalytics.com/hc/article_attachments/9898480273431/fmtpie_gnrl.gif)
2. In the **General** tab, set the general properties of the pies/donuts.
   * In the **Options** box, specify the distance between every two adjacent pies/donuts in the **Gap Amount** text box and the distance between the sections in each pie/donut and the pie/donut center in the **Explode Amount** text box. For a donut chart, you can also specify the radius percentage of the donut hole to the total donut circle by setting **Donut Hole**.
   * When you do not set the chart property [Swap Groups](https://devnet.logianalytics.com/hc/en-us/articles/5735545992599-Chart-Properties#SwapGroups) to "true" in the Report Inspector, Designer enables the options in the **KPI Value** box. You can select **Show KPI Value** to display KPI value for each pie/donut. By default, Designer uses the total value of each pie/donut as the KPI value; if you want to customize the value, clear **Auto** and type a value in the text box, or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/9898457345303/btn_fmla.gif) and select a formula or summary from the drop-down list to use its value as the KPI value. Designer calculates KPI values based on series if the chart contains series field; otherwise based on the total value. From the **Position** drop-down list, select the position of the KPI value relative to the pies/donuts; if you select **customized**, you can specify the position by dragging any KPI value in the pie/donut chart. When you specify to show KPI value in the chart, you can further [format the KPI value labels](#KPIValue) according to your requirements.
   * In the **Angle** box, specify the rotation angle of the pies/donuts around the X and Y axes.
3. In the **Fill** tab, specify the fill type and the color pattern to fill the pies/donuts.

   ![Format Pie dialog box - Fill tab](https://devnet.logianalytics.com/hc/article_attachments/9898480279447/fmtpie_fill.gif)

   * When you select the **Use Single Color** fill type,
     + Make your choice for the **Self Settings** option. When Self Settings is cleared (the default behavior), Designer synchronizes the color pattern that you specify here with the [Pattern List](https://devnet.logianalytics.com/hc/en-us/articles/5735545992599-Chart-Properties#Pattern) property of the chart in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart. When you select Self Settings, it indicates that the color pattern is private to the current data markers themselves (the pies/donuts in this case), which Designer remembers and applies to data markers of the new type automatically if you change the type of the chart later.
     + Specify the color and transparency to fill the pie/donut sections in the current data series, that is, the sections in the same data series as the one you have selected on to open the Format Pie or Format Donut dialog box (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box).
     + You can also select **Color List** to specify the color pattern for pie/donut sections in each data series respectively in the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522093463-Color-List-Dialog-Box).
   * When you select the **Use Single Color with Condition** fill type, specify the conditions and the color pattern for each condition respectively. See [Adding Conditional Color Fills to Charts](https://devnet.logianalytics.com/hc/en-us/articles/5735511924119-Applying-Conditional-Color-Fills-to-Charts).
4. In the **Border** tab, select **Show Border** if you want to display border for the pie/donut sections, then specify the border properties.

   ![Format Pie dialog box - Border tab](https://devnet.logianalytics.com/hc/article_attachments/9898463163159/fmtpie_border.gif)

   * Specify the color, transparency, line style, thickness, ending style, and line joint mode of the border.
   * In the **Path** box, specify the fill pattern of the border: Outline Path or Fill Path.
   * In the **Dash** box, select to automatically adjust the dash size or use fixed dash size if you select a dash line style for the border.
5. In the **Data Label** tab, specify properties of the static data labels in the pie/donut chart.

   ![Format Pie dialog box - Data Label tab](https://devnet.logianalytics.com/hc/article_attachments/9898463169303/fmtpie_data.gif)

   * In the **Static Data Label** box, select **Show Static Data Label** if you want to show static data labels for the pie/donut sections, then specify the position of the data labels relative to the pie/donut sections, the type of the data labels, whether to scale big and small numbers in the data labels, the color of the line pointing to the static data labels, and whether to hide the data label when its value is 0. Select **Show Truncated Label** if you want to truncate the static data labels that go beyond the boundaries of the chart paper instead of them being hidden altogether (the default behavior). Designer then displays an ellipsis (…) from the right side of the label, along with part of the name instead of the entire name. The truncated labels are also affected if you select the Position option as "best fit", where the label is cut off from the left or the right depending on the position of the label.
   * In the **Font** and **Effects** box, specify the font format and special effects of the data labels, such as the font face, font size, font color, and the font style of the data labels.
6. In the **Hint** tab, specify properties of the chart hint. A hint displays the value a section in the pie/donut chart represents when you point to the section in Designer view mode, in HTML output, or at runtime.

   ![Format Pie - Hint](https://devnet.logianalytics.com/hc/article_attachments/9898480307479/fmtpie_hint.gif)

   * Clear **Show Category and Series** if you do not want to include the category and series values in the hint.
   * Specify whether to scale big and small numbers in the hint.
   * Select **Customize Chart Value Name** to use customized names for the fields on the value axis in the hint and select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898423153431/btn_ellipsis1.gif) to customize the names as you want.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) You should not edit the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/5735546052119-Chart-Paper-Properties#ShowTips) property of the Chart Paper object in the Report Inspector which is "true" by default, if you want to display the hint.
7. For a pie/donut chart in a library component, you can [specify web behaviors](https://devnet.logianalytics.com/hc/en-us/articles/9898540480023-Defining-Web-Behaviors-of-Objects-in-a-Report#WebControl) for it in the **Behaviors** tab, to enable users to trigger different web actions when they perform specific operations such as Click and Mouse Over on the pies/donuts at runtime.

   ![Format Pie dialog box - Behaviors tab](https://devnet.logianalytics.com/hc/article_attachments/9898480316695/fmtpie_bhvr.gif)
8. Select **OK** to accept the changes and close the dialog box.

## Formatting KPI Value Labels

When a pie/donut chart displays KPI values, you can customize the KPI value labels, for example, edit the size and border of the labels, change the label font size, font color, and so on.

**To format the KPI value labels of a pie/donut chart**

1. Right-click the KPI value for any pie/donut and select **Format KPI Label** on the shortcut menu, or double-click the KPI value for any pie/donut. Designer displays the [Format KPI Label dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735529676695-Format-KPI-Label-Dialog-Box).

   ![Format KPI Label - General](https://devnet.logianalytics.com/hc/article_attachments/9898519356311/fmtkpilbl_gnrl.gif)
2. In the **General** tab, specify the general properties of the labels.
   * In the **Size** box, set the width and height of the labels, the horizontal and vertical coordinate of the top left corner of the labels relative to their parent container, the alignment of the text in the labels, and whether to wrap the label text.
   * In the **Fill** box, specify the color or effects and the transparency to fill the labels.
   * In the **Border** box, specify properties for the border of the labels, including the type, color, line style, transparency, thickness, ending style, line joint mode, fill pattern, and dash size.
   * In the **Orientation** box, specify the angle to rotate the labels.
3. In the **Font** tab, specify the font properties of the labels, including the font face, size, color, transparency, rotation angle, and shearing angle. You can also apply some special effects to the labels, such as italicizing the labels and adding a horizontal line under the labels.

   ![Format KPI Label - Font](https://devnet.logianalytics.com/hc/article_attachments/9898519363863/fmtkpilbl_font.gif)
4. In the **Format** tab, specify the data format of the labels.

   ![Format KPI Label - Format](https://devnet.logianalytics.com/hc/article_attachments/9898519367191/fmtkpilbl_fmt.gif)

   * Select a category from the **Category** box, then select a format from the **Format** box and select **Add** to add it to the **Stack** box. [Select here](https://devnet.logianalytics.com/hc/en-us/articles/5735500256407-Data-Format-Dialog-Box#DataFormat) for more information about each format.
   * When the formats Designer provides in the Format box cannot meet your requirement, you can define the format in the **Properties** text box and add it as the format of the selected category. You can add more than one format, but for each category, only one format is allowed.
   * If you do not need a format anymore, select it in the Stack box and select **Remove** to clear it.
   * Set the **Auto Scale in Number** option to specify whether to automatically scale the big and small Number values.
5. Select **OK** to accept the changes and close the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735506840727-Formatting-Area-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735563915671-Formatting-Bubble-Chart)
