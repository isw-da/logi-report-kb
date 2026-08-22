---
title: "Formatting the Areas in an Area Chart"
id: 1500010094421
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010094421-Formatting-the-Areas-in-an-Area-Chart
updated_at: 2021-07-23T19:14:38Z
---

# Formatting the Areas in an Area Chart

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094521-Formatting-the-Lines-in-a-Line-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010056982-Formatting-the-Pies-Donuts-and-KPI-Value-Labels-in-a-Pie-Donut-Chart)

# Formatting the Areas in an Area Chart

This topic describes how you can format the area of an area chart.

1. Right-click any area in the area chart and select **Format 2D Area** or **Format 3D Area** on the shortcut menu, or double-click any area in the chart. Designer displays the [Format Area dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096941-Format-Area-Dialog-Box).

   ![Format Area dialog box - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404856967319/fmtarea_gnrl_1.gif)
2. In the **General** tab, specify the layout style of the area chart. Select **Ignore Null Value** if you want to draw the areas from the previous data values to the next data values directly when null data values appear to avoid breaks on the areas.

   For a 2-D area chart, if you want to add a 3-dimensional effect to the areas, set the **Use Depth** option to **true** and the specify the depth and direction. If the chart uses a query resource, you can [use a formula to control](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties) the Use Depth option. You can also select to show the lines that represent the data categories by selecting **High-Low Lines**.
3. In the **Fill** tab, specify the fill type and the color pattern to fill the areas.

   ![Format Area dialog box - Fill tab](https://devnet.logianalytics.com/hc/article_attachments/4404856968087/fmtarea_fill.gif)

   If you select the **Use Single Color** fill type, first make a choice for the **Self Settings** checkbox: when Self Settings is unselected (the default behavior), Designer synchronizes the color pattern that you specify here with the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#Pattern) on the chart object in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart; when you select Self Settings, it indicates that the color pattern is private to the current data markers themselves (the areas in this case), which Designer remembers and applies to the data markers of a new type automatically if later you change the type of the chart. Then, specify the color pattern as follows: set the color and the transparency of the color to fill the current area, that is, the area you have right-clicked on to open the Format Area dialog box (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box), or select the **Color List** button to specify the color pattern for each area in the area chart using the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058302-Color-List-Dialog-Box).

   If the chart is of the Area 2-D or Area 3-D type, you can select the **Use Multiple Colors with Condition** fill type to divide each area into several parts based on different value ranges along the direction of the value axis and apply separate color patterns to these different value ranges. For more information, see [Adding Conditional Color Fills to Charts](https://devnet.logianalytics.com/hc/en-us/articles/1500010094361-Applying-Conditional-Color-Fills-to-Charts).
4. In the **Border** tab, specify the properties for the border of the areas.

   ![Format Area dialog box - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4404856968343/fmtarea_border.gif)

   Select **Show Border** if you want to show the border of the areas, then specify the color, color transparency, line style, thickness, end caps style, and line joint mode of the border.

   In the **Path** box, specify the fill pattern of the border: Outline Path or Fill Path.

   In the **Dash** box, select to automatically adjust the dash size or use fixed dash size if you select a dash line style for the border.
5. In the **Data Label** tab, specify the properties of the static data labels in the area chart.

   ![Format Area dialog box - Data Label tab](https://devnet.logianalytics.com/hc/article_attachments/4404856968599/fmtarea_data.gif)

   For a 2-D area chart, in the **Static Data Label** box, select **Show Static Data Label** if you want to show static data labels for the area nodes, then select the position of the data labels relative to the area nodes, in which way to display the values in the data labels, whether to scale big and small numbers in the data labels, and whether to hide the data label whose value is 0.

   In the **Font** box, specify the font format of the text in the data labels, including the font face, size, color, color transparency, rotation angle, shearing angle.

   In the **Effects** box, specify the special effects for the text in the data labels such as style, strikethrough, and underline.
6. In the **Hint** tab, specify whether to include the category and series values and whether to scale big and small numbers in the area hint (you need to set the [Show Tips](https://devnet.logianalytics.com/hc/en-us/articles/1500010100301-Chart-Paper-Properties#ShowTips) property on the chart paper to "true" in the Report Inspector if you want to show the hint). A hint displays the value an area represents when you point the mouse pointer at the area in Designer view mode, in HTML output, or at runtime.

   ![Format Area dialog box - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404856968855/fmtarea_hint.gif)
7. For an area chart in a library component, you can define web behaviors on the areas in the **Behaviors** tab.
   A web behavior contains a trigger event and a web action to be triggered when the event occurs on the areas at runtime. You can add as many web behaviors to the areas as you need.

   ![Format Area dialog box for library component - Behaviors tab](https://devnet.logianalytics.com/hc/article_attachments/4404848574103/fmtarea_bhvr.gif)

   To define the web behavior, select a [trigger event](https://devnet.logianalytics.com/hc/en-us/articles/1500010057562-Using-Basic-Web-Controls-in-a-Report#Event) from the drop-down list in the **Events** column, then select in the **Actions** column and select the **ellipsis** button ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif) in the text box. In the Web Action List dialog box, bind a web action [the same as you do to web controls](https://devnet.logianalytics.com/hc/en-us/articles/1500010057562-Using-Basic-Web-Controls-in-a-Report#Action) in the library component. The web actions you can bind include Filter, Sort, Parameter, Property, and SendMessage.

   You can select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add and define more web behaviors; if a web behavior is not required, select it and select the **Remove** button ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif) to delete it. Select a web behavior and select the **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif) button to adjust the order of the behaviors, then at runtime, when an event that is bound with more than one action happens, JDashboard triggers the upper action first.
8. Select **OK** to accept the changes and close the dialog box.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* If the chart is a combo chart composed by areas and bars/lines, when you set the depth properties for the areas, Designer applies them to the bars/lines as well, and vice versa.
* For a 3-D area chart, Designer disables the Show Static Data Label option in the Data Label tab in the Format Area dialog box; however, you can still see the data labels by moving the mouse pointer over the areas when viewing the report result in Designer view mode, in HTML output, or in Page Report Studio.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094521-Formatting-the-Lines-in-a-Line-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010056982-Formatting-the-Pies-Donuts-and-KPI-Value-Labels-in-a-Pie-Donut-Chart)
