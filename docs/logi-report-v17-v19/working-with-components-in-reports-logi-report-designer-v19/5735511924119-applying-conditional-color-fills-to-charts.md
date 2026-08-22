---
title: "Applying Conditional Color Fills to Charts"
id: 5735511924119
section: "Working with Components in Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735511924119-Applying-Conditional-Color-Fills-to-Charts
updated_at: 2022-11-02T04:12:42Z
---

# Applying Conditional Color Fills to Charts

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735527361815-Formatting-Stock-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735512266391-Labeling-Time-Series-Data-by-Constant-Interval)

# Applying Conditional Color Fills to Charts

Usually, for a data marker in a chart, it uses a predefined color pattern assigned by the [style](https://devnet.logianalytics.com/hc/en-us/articles/5735586514071-Creating-and-Applying-Styles) the chart applies. By using the Conditional Color Fill feature, you can specify color patterns based on different value ranges. With distinguishing colors, it is easy for users to locate the values they need to focus on in a chart. This topic introduces the types of the chart conditional color fills Designer supports and how you can apply them to your charts.

This topic contains the following sections:

* [Types of Conditional Color Fills](#Type)
* [Adding Single-Color Conditional Fill to Chart](#Single)
  + [Example: Applying Single-Color Conditional Fill in a Chart](#SExample)
* [Adding Multiple-Color Conditional Fill to Chart](#Multiple)
  + [Example: Applying Multiple-Color Conditional Fill in a Chart](#MExample)

## Types of Conditional Color Fills

Designer supports the following two types of conditional color fills on charts:

* **Single Color with Condition**  
  With a single color, you can make the data markers that meet the specified condition apply the color pattern bound with the condition.
* **Multiple Colors with Condition**  
  By using multiple colors, you can divide each data marker into several parts based on different value ranges along the direction of the value axis, and then specify separate color patterns to these different value ranges.

You can apply the Conditional Color Fill feature to the following chart types: Bar, Bench, Pie, Donut, Area 2-D, Area 3-D, Line 2-D, and Heat Map, and use the Multiple Colors with Condition fill type to these chart types only: Clustered Bar/Bench 2-D, Clustered Bar/Bench 3-D, Bar/Bench 3-D, Area 2-D, and Area 3-D.

## Adding Single-Color Conditional Fill to Chart

1. Double-click any data marker in the chart.
2. In the corresponding format dialog box, switch to the **Fill** tab.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) For a line chart, you can apply conditional color fills to both the chart lines and nodes on the lines in the Fill and Node tabs respectively, using the same method.
3. Select the **Use Single Color with Condition** fill type. The following shows a sample dialog box.

   ![Format Line dialog box - Fill](https://devnet.logianalytics.com/hc/article_attachments/9898519596183/cmpnt_cht_cndtnfl_sngl.gif)
4. You can edit conditional fills in either of the two modes: [normal mode](#Normal) or [advanced mode](#Advanced) (to switch between the two modes, select **Advanced** or **Normal**).

   **To edit conditional fills in normal mode**

   1. From the **Select Field** drop-down list, select the field based on which to define the conditions.
   2. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif) to add a condition line.
   3. Define the condition.
      * If you select the category/series field of the chart, or a field that does not contain numeric values from the Select Field drop-down list, select a value from the **Values** drop-down list or type it in the text box. You can specify an empty string as the value for a field of String type, by simply clearing the text box (value length=0).
      * If you select the value field of the chart, or a field containing numeric values from the Select Field drop-down list, specify the start and end values for the condition from the **Start Value** and **End Value** drop-down lists or type them in the text boxes. For a 100% Stacked Bar/Bench 2-D chart, 100% Stacked Bar/Bench 3-D chart, 100% Stacked Line 2-D chart, or a pie/donut chart, you can select **Percent** to display the data in the condition expression in percent; if you select the option, you need to type the percent value in decimal fraction in the Start Value and End Value text boxes.
   4. Specify the options such as color and transparency for values in the condition (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box). For a line chart, you can apply color pattern of the node to the corresponding line by selecting **Apply Color to Line** in the **Node** tab. Designer then disables the Color and Transparency columns in the **Conditional Fill** box of the Fill tab.
   5. By default, Designer uses the expression of the condition as its legend entry label. If you want to change it, select **Label** and change the label in the text box. For a line chart, this option is available in the Node tab of the Format Line dialog box only.
   6. Repeat the preceding steps to add more conditional fills. To remove a condition fill, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif).
   7. The values beyond the ranges that you define in all conditions automatically apply the **Other** condition settings. You can edit settings of the Other condition and its legend entry label as well.
   8. For a line chart, besides options in the Conditional Fill box of the Format Line dialog box, you can specify more line/node formatting for values in a condition.
      * To specify the line formatting of a condition, select the condition and select **Edit**![Edit button](https://devnet.logianalytics.com/hc/article_attachments/9898474047383/btn_edit.gif) in the Conditional Fill box in the Fill tab of the Format Line dialog box. In the [Edit Line Style dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522592791-Edit-Line-Style-Dialog-Box), specify the color and transparency of the chart line and the area formed by the chart axes and the chart line, and the style and thickness of the chart line respectively. Designer displays a sample based on your selection in the **Sample** box. Select **OK** if you are satisfied with the style.

        ![Edit Line Style](https://devnet.logianalytics.com/hc/article_attachments/9898519615127/edtlnstly.gif)
      * To specify the node formatting of a condition, select the condition and select **Edit**![Edit button](https://devnet.logianalytics.com/hc/article_attachments/9898474047383/btn_edit.gif) in the Conditional Fill box in the Node tab of the Format Line dialog box. In the [Edit Node Style dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735513788311-Edit-Node-Style-Dialog-Box), set **Show Node** to **true** if you want to show the nodes in the chart line, then specify the style, transparency, width, height, and color of the nodes. In the **Border** box, set the border properties of the nodes in the selected chart line, including the border color, transparency, line style, and thickness. If you set the node style to **plus**, **multiplication**, **star1** or **star2**, Designer displays the **Line** box instead of the Border box, in which you can specify the line style and thickness for the nodes. Select **OK** to apply the node properties and close the dialog box.

        ![Edit Node Style dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898481696407/edtndstly.gif)

   **To edit conditional fills in advanced mode**

   1. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif) to add a condition in the [Edit Conditions dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735513701143-Edit-Conditions-Dialog-Box#Chart). The following shows a sample dialog box.

      ![Edit Conditions dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898481795991/edtcndtn1.gif)
   2. From the **Select Query for Value Field** drop-down list, select the query which contains the fields the values of which you want to use to build the conditions. For a line chart, if you want to use field values to build the conditions, you need to select **Imported Conditions** at the bottom of the dialog box.
   3. Select **Add Condition** to add a condition line, select the field on which the condition is based from the field drop-down list, specify the operator with which to compose the condition, then select a field in the specified query from the value drop-down list as the value to build the condition or select **<Input...>** and type the value in the text box. When the condition is based on a String field, you can apply an empty string as the value, by simply leaving the text box blank (value length=0).
      For a 100% Stacked Bar/Bench 2-D chart, 100% Stacked Bar/Bench 3-D chart, or a pie/donut chart, if you specify to define the condition on a field that contains numeric values, you can control whether to display data in the condition expression as value or in percent by selecting **Value** or **Percent** at the right bottom of the dialog box.
   4. Repeat the preceding step to define more condition lines and specify the logic relationship between the condition lines: "And", "Or", "And Not", or "Or Not".
      * To group some condition lines, select them and select **Group**, Designer then adds the selected condition lines in one group and applies them as one line of filter expression (you can also group conditions and groups together).
      * To take out any condition or group from a group, select it and select **Ungroup**.
      * To adjust the priority of the condition lines, select it and select **Up** or **Down**.
      * To delete a condition line, select it and select **Delete**.
   5. Specify the fill pattern for values in the condition.
      * For a chart other than the Line type, select the fields in the specified query to control the color and transparency of the condition. The values of the field that you select to control color should contain strings such as "0x000000", and the values of the field used to control transparency should be integers between 0 and 100; otherwise, select **<Input...>** and type the value in the text box.
      * For a line chart, specify the [line formatting](#Line)/[node formatting](#Node). When you select **Imported Conditions**, you can select the fields in the specified query to control some of the options, such as Color and Transparency.
   6. Select **OK** to close the dialog box and return to the format dialog box. Designer displays the condition that you specify in the Edit Conditions dialog box in the **Conditional Fill** box in the format dialog box. You can select **Edit**![Edit button](https://devnet.logianalytics.com/hc/article_attachments/9898474047383/btn_edit.gif) to further edit the condition and the corresponding conditional fill pattern.
   7. By default, Designer shows the expression of the condition as the legend entry label. If you want to change it, select **Label** and change the label in the text box. For a line chart, this option is available in the Node tab of the Format Line dialog box only.
   8. For a chart of the Bar, Bench, or Line type, you can select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif) and repeat the preceding steps to add more conditional fills.
   9. The values beyond the ranges that you define in all conditions automatically apply the **Other** condition settings. You can edit options of the Other condition and edit its legend entry label as well. For a line chart, besides options in the Conditional Fill box, you can select **Edit**![Edit button](https://devnet.logianalytics.com/hc/article_attachments/9898474047383/btn_edit.gif) to specify more conditional fill settings for the Other condition in the same way as you do [when editing the conditional fills in normal mode](#More).
5. Select **OK** to accept the settings and close the dialog box.

### Example: Applying Single-Color Conditional Fill in a Chart

1. Make sure **SampleReports.cat** is the currently open catalog file. If not, navigate to **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Navigate to **File** > **New** > **Web Report** to create a web report.
3. [Insert a chart in the web report](https://devnet.logianalytics.com/hc/en-us/articles/5735512245143-Inserting-Charts-in-a-Report#BV) as follows:

* Use **WorldWideSalesBV** in Data Source 1 of the catalog.
* Display in the **Clustered Pie** chart type.
* Show the group object **City** on the category axis and the aggregation object **Total Sales** on the value axis.
* Apply a Select N condition to the category field City to show its **Top 12** values only.
* Use the **Basic** style.

4. Save the report and select the **View** tab to preview the chart.

   ![Clustered Pie with Top 12 Categories](https://devnet.logianalytics.com/hc/article_attachments/9898519619991/cmpnt_cht_cndtnfl1.gif)
5. Select the **Design** tab to go back to design mode and double-click a pie in the chart.
6. In the Format Pie dialog box, go to the **Fill** tab and select **Use Single Color with Condition**.
7. From the **Select Field** drop-down list, select **[Category]City**.
8. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif) three times to add three condition lines and specify the condition values and colors respectively as seen in the following image.

   ![Set Fill Conditions Based on City](https://devnet.logianalytics.com/hc/article_attachments/9898535889943/cmpnt_cht_cndtnfl2.gif)
9. Select **OK** to apply the settings and close the dialog box.
10. Preview the chart again. Designer now fills the pie sections that represent Almaty, Brussels, and Beijing with the specified colors, and distributes all the other cities to the Other group.

    ![Pie Result with Conditional Fill Based on City](https://devnet.logianalytics.com/hc/article_attachments/9898519629335/cmpnt_cht_cndtnfl3.gif)

Next, we use percentage values to edit the condition expressions.

1. Switch to design mode and open the Format Pie dialog box again.
2. In the Fill tab, select **[Value]Total Sales** from the Select Field drop-down list and select **Percent**.
3. Specify the color for the **Other** condition to **FBFBC4**.
4. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif) to add a condition line, set the start value of the condition to **0.04** and end value to **0.06**, and specify the condition color to **00CCFF**.
5. Select **Label** and modify the condition label to **4% <= Total Sales < 6%**.

   ![Set Fill Conditions Based on Total Sales](https://devnet.logianalytics.com/hc/article_attachments/9898535900055/cmpnt_cht_cndtnfl4.gif)
6. Select **OK** to accept the settings and close the dialog box.
7. Preview the chart. Designer fills the Other group and all the pie sections whose values are between 4% and 6% of the total value with the defined colors.

   ![Pie Result with Conditional Fill Based on Total Sales](https://devnet.logianalytics.com/hc/article_attachments/9898519644055/cmpnt_cht_cndtnfl5.gif)
8. To make the result clearer, you can display data label of the pie sections in percent by setting the **Data Label Type** property of the chart paper to **percent** in the Report Inspector.

   ![Pie Result with Percent Type Value Label](https://devnet.logianalytics.com/hc/article_attachments/9898535914519/cmpnt_cht_cndtnfl6.gif)

## Adding Multiple-Color Conditional Fill to Chart

You can apply the Multiple Colors with Condition fill type to the following chart types only: Clustered Bar/Bench 2-D, Clustered Bar/Bench 3-D, Bar/Bench 3-D, Area 2-D, and Area 3-D.

1. Double-click any data marker in the chart.
2. In the corresponding format dialog box, select the **Fill** tab.
3. Select the **Use Multiple Colors with Condition** fill type. The following shows a sample dialog box.

   ![Format Bar dialog box - Fill](https://devnet.logianalytics.com/hc/article_attachments/9898519654039/cmpnt_cht_cndtnfl_mltpl.gif)
4. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif) to add a condition line, specify the start value and end value for the condition from the drop-down lists or type them in the text boxes, then set the color and color transparency for the value range (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box).
5. By default, Designer shows the expression of the condition as its legend entry label. If you want to change it, select **Label** and then change the label in the text box that follows.
6. Repeat the preceding steps to add more conditional fills.
7. The values beyond the ranges you have defined in all your conditions automatically apply the **Other** condition settings. You can edit the color and transparency of the Other condition and edit its legend entry label as well.
8. Select **OK** to accept the settings and close the dialog box.

### Example: Applying Multiple-Color Conditional Fill in a Chart

1. Make sure **SampleReports.cat** is the currently open catalog file. If not, navigate to **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Navigate to **File** > **New** > **Web Report** to create a web report.
3. [Insert a chart in the web report](https://devnet.logianalytics.com/hc/en-us/articles/5735512245143-Inserting-Charts-in-a-Report#BV) as follows:

* Use **WorldWideSalesBV** in Data Source 1 of the catalog.
* Display in the **Clustered Bar 2-D** chart type.
* Show **City** on the category axis and **Total Sales** on the value axis.
* Apply a Select N condition to the category field City to show its **Top 12** values only.
* Use the **Basic** style.

4. Save the report and select the **View** tab to preview the chart.

   ![Result of Clustered Bar 2-D](https://devnet.logianalytics.com/hc/article_attachments/9898519656983/cmpnt_cht_cndtnfl7.gif)
5. Select the **Design** tab to go back to design mode and double-click a bar in the chart.
6. In the Format Bar dialog box, select the **Fill** tab, then select the **Use Multiple Colors with Condition** fill type.
7. Designer selects the value field **Total Sales** in the **Select Field** drop-down list by default. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif) four times to add four condition lines and specify the condition values and colors respectively as seen in the following image.

   ![Set Multiple Colors with Condition](https://devnet.logianalytics.com/hc/article_attachments/9898535925911/cmpnt_cht_cndtnfl8.gif)
8. By default, Designer uses the condition expression as the legend entry label for each condition. Take the first condition line for example, its condition expression is "10000 <= Total Sales < 20000". Select each condition line and select **Label** one by one. Select **OK**.
9. Preview the chart again. Designer now divides each bar into several parts based on different value ranges and fills them with different conditional colors.

   ![Result of Bar Chart with Multiple-color Conditions](https://devnet.logianalytics.com/hc/article_attachments/9898535934359/cmpnt_cht_cndtnfl9.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735527361815-Formatting-Stock-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735512266391-Labeling-Time-Series-Data-by-Constant-Interval)
