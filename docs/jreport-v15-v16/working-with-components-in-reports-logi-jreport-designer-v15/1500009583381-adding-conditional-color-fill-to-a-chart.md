---
title: "Adding Conditional Color Fill to a Chart"
id: 1500009583381
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009583381-Adding-Conditional-Color-Fill-to-a-Chart
updated_at: 2021-07-24T05:56:10Z
---

# Adding Conditional Color Fill to a Chart

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583641-Formatting-the-Stock-Chart)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583681-Binding-a-Link-to-a-Chart)

# Adding Conditional Color Fill to a Chart

Usually, for a data marker in a chart, it uses a predefined color pattern assigned by Logi JReport. By using the Conditional Color Fill feature, you can assign color patterns based on different value ranges. Thus, with the distinguishing colors, it is easy for you to locate the values you need to focus on in a chart. Currently, the Conditional Color Fill feature is supported on bar, bench, pie, donut, area (Area 2-D and Area 3-D types), 2-D line and heat map charts.

There are two types of conditional color fill settings: Single Color with Condition and Multiple Colors with Condition. With a single color, you can make the data marker that meets the specified condition apply the color pattern bound with the condition. By using multiple colors, you can divide each data marker into different parts based on different value ranges along the direction of the value axis, and then specify different conditional colors to different value ranges. However, the fill type Multiple Colors with Condition can only be applied to Clustered Bar/Bench 2-D, Clustered Bar/Bench 3-D, Bar/Bench 3-D, Area 2-D and Area 3-D chart types.

Below is a list of the sections covered in this topic:

> * [Adding Conditional Fill with a Single Color](#Single)
> * [Adding Conditional Fill with Multiple Colors](#Multiple)

## Adding Conditional Fill with a Single Color

1. Double-click on any data marker in a chart, and the corresponding format dialog is displayed.
2. Switch to the **Fill** tab. For a line chart, you can set conditional color fill on both the chart line and the nodes on the line in the Fill and Node tab respectively using the same method.
3. Select the fill type as **Use Single Color with Condition**. Below is a sample dialog.

   ![Format Line dialog - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404894004375/cmpnt_cht_cndtnfl_sngl.gif)
4. You can edit the conditional fill in either of the two modes: [normal mode](#Normal) or [advanced mode](#Advanced) (to switch between the two modes, select the **Advanced** or **Normal** button).

   **Normal Mode**

   1. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) to add a condition line.
   2. From the Select Field drop-down list, select the field based on which the condition will be created.
   3. Define the condition.
      * When the category/series field or a field whose return value is not a number is selected from the Select Field drop-down list, select a value from the Values drop-down list or input it directly in the text box.
      * When the value field or a field that returns a number is selected from the Select Field drop-down list, specify the start and end values for the condition from the Start Value and End Value drop-down lists or input them directly in the text boxes.

        For 100% Stacked Bar/Bench 2-D chart, 100% Stacked Bar/Bench 3-D chart, 100% Stacked Line 2-D chart or pie/donut chart, you can control to display the data in the condition expression in percent. To achieve it, check **Percent**, and then input the percent value in decimal fraction in the Start Value and End Value text boxes.
   4. Set the properties such as color and transparency for values in the condition (to change the color, select the color image and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette) or input the hexadecimal value of a color directly in the text box).

      For a line chart, you can make the color pattern specified on the node apply to the corresponding line. To do this, in the Node tab, check **Apply Color to Line**. The Color and Transparency properties in the Fill tab will then be disabled.
   5. By default, the expression of the condition will be shown as its legend entry label. If you want to change it, check **Label** and change the label in the text box that follows. For a line chart, this option is available in the Node tab of the Format Line dialog only.
   6. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) and repeat the above steps to add more conditional fill.
   7. The values beyond the ranges you have defined in all your conditions will automatically apply the Other condition settings. You can edit properties of the Other condition and edit its legend entry label as well.
   8. For a line chart, besides properties in the Conditional Fill box of the Format Line dialog, you can edit more line/node properties for values in a condition.

      To edit the line properties of a condition, select the condition and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791511/btn_edit.gif) in the Conditional Fill box in the Fill tab of the Format Line dialog. In the [Edit Line Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009565342-Edit-Line-Style-Dialog) dialog, specify the color and transparency of the chart line and the area formed by the chart axes and the chart line, and the style and thickness of the chart line respectively. A sample based on your selection will be displayed in the Sample box. Select **OK** if you are satisfied with the format.

      ![Edit Line Style dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893923351/edtlnstly.gif)

      To edit the node properties of a condition, select the condition and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791511/btn_edit.gif) in the Conditional Fill box in the Node tab of the Format Line dialog. In the [Edit Node Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009586501-Edit-Node-Style-Dialog) dialog, set Show Node to **true** if you want to show the nodes in the chart line, then specify the style, transparency, width, height and color of the nodes. In the Border box, set the border properties of the nodes in the selected chart line, including border color, transparency, line style and thickness. If you set the node style to plus, multiplication, star1 or star2, the Line box is available instead of the Border box, in which you can specify the line style and thickness for the nodes with selected styles. Select **OK** to apply the node properties and close the dialog.

      ![Edit Node Style dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893923095/edtndstly.gif)

   **Advanced Mode**

   1. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) to add a condition in the Edit Conditions dialog. The following is a sample dialog.

      ![Edit Conditions dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893926935/edtcndtn1.gif)
   2. From the Select Query for Value Field drop-down list, select the query which contains the fields the values of which you want to use to build the conditions.

      For a line chart, if you want to use field values to build the conditions, you need to check **Imported Conditions** at the bottom of the dialog.
   3. Select the **Add Condition** button to add a condition, select a field on which the condition is based from the field drop-down list, specify the operator with which to compose the condition, then select a field in the specified query from the value drop-down list as the value to build the condition or select **<Input...>** and input the value directly in the text box. Repeat this to add more conditions if necessary. To make some conditions grouped, select them and select the **Group** button, then the selected conditions will be added in one group and work as one line of filter expression. Conditions and groups together can be further grouped. To take any condition or group in a group out, select it and select **Ungroup.** To adjust the priority of the conditions, select it and select the **Up** or **Down** button. To delete a condition, select it and select the **Delete** button.

      For 100% Stacked Bar/Bench 2-D chart, 100% Stacked Bar/Bench 3-D chart or pie/donut chart, if you select a value field from the field drop-down list, you can control whether to display the data in the condition expression as value or in percent by checking Value or Percent at the right bottom of the dialog.
   4. Specify the fill properties for values in the condition.

      For a chart other than the line type, select the fields in the specified query to control the color and transparency of the condition, however the values of the field you select to control color should contain strings such as 0x000000, and the values of the field used to control transparency should be integers between 0 and 100. Otherwise, select  **<Input...>** and input the value directly in the text box.

      For a line chart, specify values for the [line properties](#Line)/[node properties](#Node). When Imported Conditions is checked, you can select the fields in the specified query to control some of the properties, such as Color and Transparency.
   5. When done, select **OK** to close the dialog and return to the chart format dialog.

      The condition specified in the Edit Conditions dialog is now listed in the Conditional Fill box in the chart format dialog. You can select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791511/btn_edit.gif) to further edit the condition and the corresponding conditional fill properties if required.
   6. By default, the expression of the condition will be shown as the legend entry label. If you want to change it, check **Label** and change the label in the text box that follows. For a line chart, this option is available in the Node tab of the Format Line dialog only.
   7. For a chart of bar, bench or line type, you can select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) and repeat the above steps to add more conditional fill.
   8. The values beyond the ranges you have defined in all your conditions will automatically apply the Other condition settings. You can edit properties of the Other condition and edit its legend entry label as well. For a line chart, besides properties in the Conditional Fill box, you can select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791511/btn_edit.gif) to edit more conditional fill properties for the Other condition in the same way as you do [when editing the conditional fill in normal mode](#More).
5. When done, select **OK** to accept the settings and close the dialog.

The following example shows how to add conditional color fill to a chart using the Single Color with Condition fill type.

1. [Open the catalog file](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog) SampleReports.cat in `<install_root>\Demo\Reports\SampleReports`.
2. [Create a web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Create).
3. [Insert a chart in the web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009563242-Inserting-a-Chart#Web) which is based on WorldWideSalesBV in Data Source 1, displays in the Clustered Pie chart type, shows City on Slice and Total Sales on Slice Size.
4. Right-click the chart in the report and select **Chart Wizard** from the shortcut menu to open the Chart Wizard.
5. In the Display screen, select the **Order/Select N** button below the Slice box.
6. In the Category Options dialog, select **Top N** from the Select drop-down list, input **12** in the text field to the right, then select **OK**.

   ![Category Options dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889425815/cmpnt_cht_cndtnfl_ctgyoptn.gif)
7. Select **Finish** in the Chart Wizard.
8. Save the report and select the **View** tab, the report will show as follows:

   ![Clustered Pie in a report](https://devnet.logianalytics.com/hc/article_attachments/4404889426071/cmpnt_cht_cndtnfl1.gif)
9. Go back to the design mode and double-click a pie in the chart. The Format Pie dialog will be displayed.
10. Go to the Fill tab and select **Use Single Color with Condition**. From the Select Field drop-down list, select **[Category]City**, then select the add button ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) three times to add three condition lines, and specify the conditions and related colors as follows:

    ![Conditonal Fill of Pie](https://devnet.logianalytics.com/hc/article_attachments/4404894004631/cmpnt_cht_cndtnfl2.gif)
11. Select **OK** to apply the settings and close the dialog.
12. View the report again. Now you can see pie sections standing for the city Almaty, Brussels and Beijing are filled with the defined color for distinguishing, and other cities are all be distributed to the Other group.

    ![Clustered Pie in a report](https://devnet.logianalytics.com/hc/article_attachments/4404894004887/cmpnt_cht_cndtnfl3.gif)

Next, we will use percentage values to edit the condition expressions.

1. Go back to the design mode and enter the Format Pie dialog again.
2. Select **Use Single Color with Condition** again in the Fill tab, then select **[Value]Total Sales** from the Select Field drop-down list. Check the **Percent** radio button, and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) to add a new condition line. Set the start value to **0.04**, and the end value to **0.06**, and then input **00CCFF** in the Color text field. Check the **Label** checkbox, then modify the condition expression to **4% <= Total Sales < 6%**. Specify the color for the Other group to **FFFF99**. Select **OK** to accept the settings. View the report and the result looks like:

   ![Clustered Pie in a Report](https://devnet.logianalytics.com/hc/article_attachments/4404889426327/cmpnt_cht_cndtnfl4.gif)
3. From the report above, you can see the Other group and all the pie sections whose values are between 4% and 6% of the total value are filled with the defined colors. To make the result more clear, you can specify to display the value label of the pies in percent by setting the property Value Label Type of the chart paper to percent in the Report Inspector. Then the report result is shown as follows:

   ![Clusteerd Pie in a report](https://devnet.logianalytics.com/hc/article_attachments/4404894005143/cmpnt_cht_cndtnfl5.gif)

## Adding Conditional Fill with Multiple Colors

The fill type Multiple Colors with Condition is supported only on Clustered Bar/Bench 2-D, Clustered Bar/Bench 3-D, Bar/Bench 3-D, Area 2-D and Area 3-D chart types.

1. Double-click on any data marker in a chart, and the corresponding format dialog is displayed.
2. Switch to the **Fill** tab.
3. Select the fill type as **Use Multiple Colors with Condition**. The following is a sample dialog.

   ![Format Bar - multiple colors conditional filling](https://devnet.logianalytics.com/hc/article_attachments/4404889426583/cmpnt_cht_cndtnfl_mltpl.gif)
4. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) to add a condition line, specify the start value and end value for the condition from the drop-down lists or input them directly in the text boxes, then set the color and transparency for the value range (to change the color, select the color image and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette) or input the hexadecimal value of a color directly in the text box).
5. By default, the expression of the condition will be shown as its legend entry label. If you want to change it, check **Label**, and then change the label in the text box that follows.
6. Repeat the above steps to add more conditional fill.
7. The values beyond the ranges you have defined in all your conditions will automatically apply the Other condition settings. You can edit the color and transparency of the Other condition and edit its legend entry label as well.
8. Select **OK** to accept the settings and close the dialog.

The following example shows how to add conditional color fill to a chart using the Multiple Colors with Condition fill type.

1. Create a report which uses the same data and Order/Select N condition as the report in the [above example](#Pie). The only difference is that the chart type is Clustered Bar 2-D.
2. Save the report and select the **View** tab, the report will show as follows:

   ![Bar chart in a report](https://devnet.logianalytics.com/hc/article_attachments/4404894005399/cmpnt_cht_cndtnfl6.gif)
3. Back to the Design mode and double-click a bar in the chart to display the Format Bar dialog.
4. In the Fill tab, select **Use Multiple Colors with Condition** as the fill type, then the value field Total Sales will be the selected by default in the Select Field drop-down list. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) four times to add four condition lines and specify the conditions and the colors as follows:

   ![Multiple corlors conditonal fill of Bar](https://devnet.logianalytics.com/hc/article_attachments/4404889426839/cmpnt_cht_cndtnfl7.gif)
5. By default, the condition expression will be used as the legend entry label. Take the first condition line for example, its condition expression is 10000 <= Total Sales < 20000. Select each condition line and check the **Label** check box one by one. Cick **OK**.
6. Save the report and select the **View** tab, the result will be displayed as follows. Each bar is divided into several parts based on different value ranges with different conditional colors.

   ![Bar chart in a report](https://devnet.logianalytics.com/hc/article_attachments/4404889427095/cmpnt_cht_cndtnfl8.gif)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583641-Formatting-the-Stock-Chart)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583681-Binding-a-Link-to-a-Chart)
