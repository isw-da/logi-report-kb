---
title: "Formatting Bullet Chart"
id: 5735520593815
section: "Working with Components in Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735520593815-Formatting-Bullet-Chart
updated_at: 2022-11-02T04:27:56Z
---

# Formatting Bullet Chart

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735520622999-Formatting-Indicator-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735527346839-Formatting-Heat-Map-Rectangles)

# Formatting Bullet Chart

This topic describes how you can format the bullets in a bullet chart.

1. Right-click any bullet in the bullet chart and select **Format Bullet** from the shortcut menu, or double-click any bullet in the chart. Designer displays the [Format Bullet dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735566000919-Format-Bullet-Dialog-Box).

   ![Format Bullet dialog box - General](https://devnet.logianalytics.com/hc/article_attachments/9898463934999/fmtbult_gnrl.gif)
2. In the **General** tab, specify the size of the bullets by setting the width of the featured measure, comparative measure, and qualitative ranges respectively.
3. In the **Fill** tab, set the color pattern to fill the bullets.

   ![Format Bullet dialog box - Fill](https://devnet.logianalytics.com/hc/article_attachments/9898463941783/fmtbult_fill.gif)

   * In the **Featured Measure Color List** box,
     + Specify whether to define the color pattern on the featured measures themselves by using the **Self Settings** option. When Self Settings is cleared (the default behavior), Designer synchronizes the color pattern that you specify here with the [Pattern List](https://devnet.logianalytics.com/hc/en-us/articles/5735545992599-Chart-Properties#Pattern) property of the chart in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart. When you select Self Settings, it indicates that the color pattern is private to the current data markers themselves (the bullets in this case), which Designer remembers and applies to data markers of the new type automatically if you change the type of the chart later.
     + Set the color and transparency to fill all the featured measures (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box)
     + If you want to apply different colors to the featured measures, select **Vary Colors by Color List**, then select **Color List** to specify the color pattern for each featured measure in the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522093463-Color-List-Dialog-Box).
   * In the **Comparative Measure Color List**/ **Qualitative Ranges Color List** box, specify the color and transparency to fill the selected comparative measures/qualitative ranges in the same data series, or select **Color List** to specify the color pattern for comparative measures/qualitative ranges in the same data series respectively.
4. In the **Border** tab, select **Show Border** if you want to display border for the bullets, then specify the border properties.

   ![Format Bullet dialog box - Border](https://devnet.logianalytics.com/hc/article_attachments/9898481059095/fmtbult_border.gif)

   * Specify the color, transparency, line style, thickness, ending style, and line joint mode of the border.
   * In the **Path** box, specify the fill pattern of the border: Outline Path or Fill Path.
   * In the **Dash** box, select to automatically adjust the dash size or use fixed dash size if you select a dash line style for the border.
5. Skip the Data Label tab because Designer does not support displaying data labels in bullet charts.
6. In the **Hint** tab, specify properties of the chart hint. A hint displays the value a bullet represents when you point to the bullet in Designer view mode, in HTML output, or at runtime.

   ![Format Bullet - Hint](https://devnet.logianalytics.com/hc/article_attachments/9898463985303/fmtbult_hint.gif)

   * Clear **Show Category and Series** if you do not want to include the category and series values in the hint.
   * Specify whether to scale big and small numbers in the hint.
   * Select **Customize Chart Value Name** to use customized names for the fields on the value axis in the hint and select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898423153431/btn_ellipsis1.gif) to customize the names as you want.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) You should not edit the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/5735546052119-Chart-Paper-Properties#ShowTips) property of the Chart Paper object in the Report Inspector which is "true" by default, if you want to display the hint.
7. For a bullet chart in a library component, you can [specify web behaviors](https://devnet.logianalytics.com/hc/en-us/articles/9898540480023-Defining-Web-Behaviors-of-Objects-in-a-Report#WebControl) for it in the **Behaviors** tab, to enable users to trigger different web actions when they perform specific operations such as Click and Mouse Over on the bullets at runtime.

   ![Format Bullet dialog box - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/9898481073175/fmtbult_bhvr.gif)
8. Select **OK** to accept the changes and close the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735520622999-Formatting-Indicator-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735527346839-Formatting-Heat-Map-Rectangles)
