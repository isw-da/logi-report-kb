---
title: "Applying Conditional Color Fills to Charts"
id: 1500009605602
section: "Working with Components in Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009605602-Applying-Conditional-Color-Fills-to-Charts
updated_at: 2021-07-24T16:05:23Z
---

# Applying Conditional Color Fills to Charts

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009606002-Formatting-the-Stock-in-a-Stock-Chart) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009606082-Labeling-Time-Series-Data-by-Constant-Interval)

# Applying Conditional Color Fills to Charts

Usually, for a data marker in a chart, it uses a predefined color pattern assigned by the [style](https://devnet.logianalytics.com/hc/en-us/articles/1500009613442-Creating-and-Applying-Styles) the chart applies. By using the Conditional Color Fill feature, you can specify color patterns based on different value ranges. With distinguishing colors, it is easy for you to locate the values you need to focus on in a chart.

This topic includes the following sections:

* [Types of Conditional Color Fills in Charts](#Type)
* [Adding Single-Color Conditional Fill to a Chart](#Single)
  + [Example of Applying Single-Color Conditional Fill in a Chart](#SExample)
* [Adding Multiple-Color Conditional Fill to a Chart](#Multiple)
  + [Example of Applying Multiple-Color Conditional Fill in a Chart](#MExample)

## Types of Conditional Color Fills in Charts

There are two types of conditional color fills for charts in Logi Report Designer:

* **Single Color with Condition**  
   With a single color, you can make the data marker that meets the specified condition apply the color pattern bound with the condition.
* **Multiple Colors with Condition**  
   By using multiple colors, you can divide each data marker into different parts based on different value ranges along the direction of the value axis, and then specify different color patterns to different value ranges.

The Conditional Color Fill feature is supported on the following chart types: Bar, Bench, Pie, Donut, Area 2-D, Area 3-D, Line 2-D and Heat Map, and for the Multiple Colors with Condition fill type, Clustered Bar/Bench 2-D, Clustered Bar/Bench 3-D, Bar/Bench 3-D, Area 2-D and Area 3-D chart types only.

## Adding Single-Color Conditional Fill to a Chart

1. Double-click on any data marker in the chart.
2. In the corresponding format dialog, switch to the **Fill** tab. For a line chart, you can set conditional color fills on both the chart line and the nodes on the lines in the Fill and Node tab respectively using the same method.
3. Select the fill type as **Use Single Color with Condition**. See a sample dialog below.

   ![Format Line dialog - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404904466583/cmpnt_cht_cndtnfl_sngl.gif)
4. You can edit the conditional fills in either of the two modes: [normal mode](#Normal) or [advanced mode](#Advanced) (to switch between the two modes, select the **Advanced** or **Normal** button).

   **To edit conditional fills in normal mode**:

   1. From the Select Field drop-down list, select the field based on which to define the conditions.
   2. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) to add a condition line.
   3. Define the condition.
      * When the category/series field or a field whose return value is not a number is selected from the Select Field drop-down list, select a value from the Values drop-down list or type it directly in the text box. You can specify an empty string as the value for a field of String type, by simply clearing the text box (value length=0).
      * When the value field or a field that returns a number is selected from the Select Field drop-down list, specify the start and end values for the condition from the Start Value and End Value drop-down lists or type them directly in the text boxes.

        For 100% Stacked Bar/Bench 2-D chart, 100% Stacked Bar/Bench 3-D chart, 100% Stacked Line 2-D chart or Pie/Donut chart, you can display the data in the condition expression in percent. To achieve it, select **Percent**, and then type the percent value in decimal fraction in the Start Value and End Value text boxes.
   4. Set the properties such as color and transparency for values in the condition (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box).

      For a line chart, you can make the color pattern specified on the node apply to the corresponding line. To do this, in the Node tab, select **Apply Color to Line**. The Color and Transparency properties in the Fill tab will then be disabled.
   5. By default, the expression of the condition will be shown as its legend entry label. If you want to change it, select **Label** and change the label in the text box that follows. For a line chart, this option is available in the Node tab of the Format Line dialog only.
   6. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) and repeat the above steps to add more conditional fills.
   7. The values beyond the ranges you have defined in all your conditions will automatically apply the Other condition settings. You can edit properties of the Other condition and edit its legend entry label as well.
   8. For a line chart, besides properties in the Conditional Fill box of the Format Line dialog, you can edit more line/node properties for values in a condition.

      To edit the line properties of a condition, select the condition and select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404911588375/btn_edit.gif) in the Conditional Fill box in the Fill tab of the Format Line dialog. In the [Edit Line Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009607922-Edit-Line-Style-Dialog) dialog, specify the color and transparency of the chart line and the area formed by the chart axes and the chart line, and the style and thickness of the chart line respectively. A sample based on your selection will be displayed in the Sample box. Select **OK** if you are satisfied with the format.

      ![Edit Line Style](https://devnet.logianalytics.com/hc/article_attachments/4404904347799/edtlnstly.gif)

      To edit the node properties of a condition, select the condition and select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404911588375/btn_edit.gif) in the Conditional Fill box in the Node tab of the Format Line dialog. In the [Edit Node Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009607942-Edit-Node-Style-Dialog) dialog, set Show Node to **true** if you want to show the nodes in the chart line, then specify the style, transparency, width, height and color of the nodes. In the Border box, set the border properties of the nodes in the selected chart line, including border color, transparency, line style and thickness. If you set the node style to plus, multiplication, star1 or star2, the Line box is available instead of the Border box, in which you can specify the line style and thickness for the nodes with selected styles. Select **OK** to apply the node properties and close the dialog.

      ![Edit Node Style dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904347287/edtndstly.gif)

   **To edit conditional fills in advanced mode**:

   1. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) to add a condition in the Edit Conditions dialog. The following is a sample dialog.

      ![Edit Conditions dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904351255/edtcndtn1.gif)
   2. From the Select Query for Value Field drop-down list, select the query which contains the fields the values of which you want to use to build the conditions.

      For a line chart, if you want to use field values to build the conditions, you need to select **Imported Conditions** at the bottom of the dialog.
   3. Select the **Add Condition** button to add a condition, select a field on which the condition is based from the field drop-down list, specify the operator with which to compose the condition, then select a field in the specified query from the value drop-down list as the value to build the condition or select **<Input...>** and type the value in the text box. ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404911621015/___newv17.jpg "New for version 17.")You can specify an empty string as the value for a field of String type, by simply leaving the text box blank (value length=0).

      You can repeat this to add more conditions. To make some conditions grouped, select them and select the **Group** button, then the selected conditions will be added in one group and work as one line of filter expression. Conditions and groups together can be further grouped. To take any condition or group in a group out, select it and select **Ungroup.** To adjust the priority of the conditions, select it and select the **Up** or **Down** button. To delete a condition, select it and select the **Delete** button.

      For 100% Stacked Bar/Bench 2-D chart, 100% Stacked Bar/Bench 3-D chart or Pie/Donut chart, if you select a value field from the field drop-down list, you can control whether to display the data in the condition expression as value or in percent by selecting Value or Percent at the right bottom of the dialog.
   4. Specify the fill properties for values in the condition.

      For a chart other than the line type, select the fields in the specified query to control the color and transparency of the condition, however the values of the field you select to control color should contain strings such as 0x000000, and the values of the field used to control transparency should be integers between 0 and 100. Otherwise, select **<Input...>** and type the value in the text box.

      For a line chart, specify values for the [line properties](#Line)/[node properties](#Node). When Imported Conditions is selected, you can select the fields in the specified query to control some of the properties, such as Color and Transparency.
   5. Select **OK** to close the dialog and return to the chart format dialog.

      The condition specified in the Edit Conditions dialog is now listed in the Conditional Fill box in the chart format dialog. You can select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404911588375/btn_edit.gif) to further edit the condition and the corresponding conditional fill properties.
   6. By default, the expression of the condition will be shown as the legend entry label. If you want to change it, select **Label** and change the label in the text box that follows. For a line chart, this option is available in the Node tab of the Format Line dialog only.
   7. For a chart of Bar, Bench or Line type, you can select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) and repeat the above steps to add more conditional fills.
   8. The values beyond the ranges you have defined in all your conditions will automatically apply the Other condition settings. You can edit properties of the Other condition and edit its legend entry label as well. For a line chart, besides properties in the Conditional Fill box, you can select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404911588375/btn_edit.gif) to edit more conditional fill properties for the Other condition in the same way as you do [when editing the conditional fills in normal mode](#More).
5. Select **OK** to accept the settings and close the dialog.

### Example of Applying Single-Color Conditional Fill in a Chart

1. Make sure SampleReports.cat is the currently open catalog file. If not select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Select **File** > **New** > **Web Report** to create a web report.
3. [Insert a chart in the web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009628941-Inserting-Charts-in-a-Report#BV) as follows:

* Use WorldWideSalesBV in Data Source 1 of the catalog as the data source.
* Display in the Clustered Pie chart type.
* Show the group object City on the category axis and the aggregation object Total Sales on the value axis.
* Apply a Select N condition to the category field City to show its Top 12 values only.

4. Save the report and select the **View** tab to preview the chart. The chart appears as follows:

   ![Clustered Pie with Top 12 Categories](https://devnet.logianalytics.com/hc/article_attachments/4404904466967/cmpnt_cht_cndtnfl1.gif)
5. Go back to the design mode and double-click a pie in the chart.
6. In the Format Pie dialog, go to the **Fill** tab and select **Use Single Color with Condition**.
7. From the Select Field drop-down list, select **[Category]City**, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) three times to add three condition lines and specify the condition values and colors as follows:

   ![Set Fill Conditions Based on City](https://devnet.logianalytics.com/hc/article_attachments/4404904467223/cmpnt_cht_cndtnfl2.gif)
8. Select **OK** to apply the settings and close the dialog.
9. Preview the chart again. Now you can see pie sections that represent the city Almaty, Brussels and Beijing are filled with the defined colors, and other cities are all distributed to the Other group.

   ![Pie Result with Conditional Fill Based on City](https://devnet.logianalytics.com/hc/article_attachments/4404904467479/cmpnt_cht_cndtnfl3.gif)

   Next, we will use percentage values to edit the condition expressions.
10. Go back to the design mode and open the Format Pie dialog again.
11. In the Fill tab, select **[Value]Total Sales** from the Select Field drop-down list and select the **Percent** radio button. Specify the color for the Other condition to **FBFBC4**. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) to add a condition line, set the condition Start Value to **0.04**, End Value to **0.06** and color to **00CCFF**, then select the **Label** checkbox and modify the condition label to **4% <= Total Sales < 6%**.

    ![Set Fill Conditions Based on Total Sales](https://devnet.logianalytics.com/hc/article_attachments/4404904467735/cmpnt_cht_cndtnfl4.gif)
12. select **OK** to accept the settings and close the dialog.
13. Preview the chart and the result looks like below:

    ![Pie Result with Conditional Fill Based on Total Sales](https://devnet.logianalytics.com/hc/article_attachments/4404904467991/cmpnt_cht_cndtnfl5.gif)
14. From the result above, you can see the Other group and all the pie sections whose values are between 4% and 6% of the total value are filled with the defined colors. To make the result more clear, you can display the data label of the pie sections in percent by setting the property Data Label Type on the chart paper to percent in the Report Inspector. Then the report result is shown as follows:

    ![Pie Result with Percent Type Value Label](https://devnet.logianalytics.com/hc/article_attachments/4404916839063/cmpnt_cht_cndtnfl6.gif)

## Adding Multiple-Color Conditional Fill to a Chart

The fill type Multiple Colors with Condition is supported only on Clustered Bar/Bench 2-D, Clustered Bar/Bench 3-D, Bar/Bench 3-D, Area 2-D and Area 3-D chart types.

1. Double-click on any data marker in the chart.
2. In the corresponding format dialog, switch to the **Fill** tab.
3. Select the fill type as **Use Multiple Colors with Condition**. The following is a sample dialog.

   ![Format Bar dialog - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404916839319/cmpnt_cht_cndtnfl_mltpl.gif)
4. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) to add a condition line, specify the start value and end value for the condition from the drop-down lists or type them in the text boxes, then set the color and transparency for the value range (to change the color, select the color indicator and select a color from the [color palette,](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette) or type the hexadecimal value of a color in the text box).
5. By default, the expression of the condition will be shown as its legend entry label. If you want to change it, select **Label**, and then change the label in the text box that follows.
6. Repeat the above steps to add more conditional fills.
7. The values beyond the ranges you have defined in all your conditions will automatically apply the Other condition settings. You can edit the color and transparency of the Other condition and edit its legend entry label as well.
8. Select **OK** to accept the settings and close the dialog.

### Example of applying multiple-color conditional fill in a chart

1. Make sure SampleReports.cat is the currently open catalog file. If not select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Select **File** > **New** > **Web Report** to create a web report.
3. [Insert a chart in the web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009628941-Inserting-Charts-in-a-Report#BV) as follows:

* Use WorldWideSalesBV in Data Source 1 of the catalog as the data source.
* Display in the Clustered Bar 2-D chart type.
* Show City on the category axis and Total Sales on the value axis.
* Apply a Select N condition to the category field City to show its Top 12 values only.

4. Save the report and select the **View** tab to preview the chart. The chart appears as follows:

   ![Result of Clustered Bar 2-D](https://devnet.logianalytics.com/hc/article_attachments/4404904468247/cmpnt_cht_cndtnfl7.gif)
5. Back to the design mode and double-click a bar in the chart.
6. In the Format Bar dialog, select the **Fill** tab, then select **Use Multiple Colors with Condition** as the fill type.
7. The value field Total Sales is selected by default in the Select Field drop-down list. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) four times to add four condition lines and specify the condition values and colors as follows:

   ![Set Multiple Colors with Condition](https://devnet.logianalytics.com/hc/article_attachments/4404904468503/cmpnt_cht_cndtnfl8.gif)
8. By default, the condition expression is used as the legend entry label for each condition. Take the first condition line for example, its condition expression is 10000 <= Total Sales < 20000. Select each condition line and select the **Label** checkbox one by one. Select **OK**.
9. Preview the chart again and it displays as follows now. Each bar is divided into several parts based on different value ranges with different conditional colors.

   ![Result of Bar Chart with Multiple-color Conditions](https://devnet.logianalytics.com/hc/article_attachments/4404904468759/cmpnt_cht_cndtnfl9.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009606002-Formatting-the-Stock-in-a-Stock-Chart) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009606082-Labeling-Time-Series-Data-by-Constant-Interval)
