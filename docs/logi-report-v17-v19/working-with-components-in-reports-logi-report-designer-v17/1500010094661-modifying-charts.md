---
title: "Modifying Charts"
id: 1500010094661
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010094661-Modifying-Charts
updated_at: 2021-07-23T19:14:43Z
---

# Modifying Charts

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057042-Inserting-Charts-in-a-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094401-Formatting-Chart-Elements)

# Modifying Charts

For any chart in a report, you can further modify it at any time. This topic introduces how you can modify a chart by editing the data displayed in the chart.

This topic contains the following sections:

* [Editing a Chart with Wizard](#Edit)
* [Defining Special Groups](#Special)
* [Grouping Data by Intervals](#Group)
* [Setting Order/Select N Condition](#SelectN)

## Editing a Chart with Wizard

You can further modify a chart by accessing its shortcut menu wizard which contains a set of screens that are similar to the wizard screens used to create the chart. For example, you can change the data used by the chart, modify the chart type, and so on.

1. Right-click the chart and select **Chart Wizard** from the shortcut menu to display the [Chart Wizard dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058202-Chart-Wizard-Dialog-Box).
2. In the **Data** screen, you can specify a new data source for the chart.
3. In the **Type** screen, specify the type of the chart.

   If you want to change the chart type, you may need to first remove all the chart data. Specially, if you change a combo type to a single type or vice versa, Designer prompts you to make sure because it will remove all chart data automatically.
4. In the **Display** screen, specify the fields to display in the chart.
   Use the button ![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404856888855/btn_replace.gif) to replace a current field. For more information about how to define a chart, see [Inserting Charts in a Report](https://devnet.logianalytics.com/hc/en-us/articles/1500010057042-Inserting-Charts-in-a-Report).
5. In the **Layout** screen, specify settings for the chart elements.
6. In the **Style** screen, select a style for the chart.
7. Select **Finish** to accept the changes.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) When you change a type of 2-D chart to another type of 2-D chart, or a type of 3-D chart to another type of 3-D chart, Designer keeps all the previous properties. Nevertheless, when you change a 2-D chart to a 3-D chart, Designer sets the properties of the Z axis, the Y-Z wall, and the floor of the 3-D chart to the default values (since a 2-D chart does not have the Z axis, the Y-Z wall, or the floor), and removes all the other properties from the 2-D chart; when you change a 3-D chart to a 2-D chart, Designer sets the properties of the Y2 axis of the 2-D chart to the default values (since a 3-D chart does not have the Y2 axis).

## Defining Special Groups

You can define how to group values on the category/series axis of a chart (for a heat map, on its groups). To do this:

1. When creating or editing a chart with wizard, select the **Special Group** button in the **Display** screen. Designer displays the [User Defined Group dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060782-User-Defined-Group-Dialog-Box).

   ![User Defined Group dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848484375/udg.gif)
2. Select the **Add** button to add a grouping line and specify the **Group Name**, **Operator**, and **Operand** as required. Repeat this to add more group criteria.

   For example, if you place a field named "Score" for grouping which contains student scores that range from 0 to 100, and you want to group the students in 5 ranks, namely rank A: 90~100, B: 80~89, C: 70~79, D: 60~69, and F: 0~59. You can set the groups as follows:

   | Group Name | Operator | Operand |
   | --- | --- | --- |
   | A | between | Op1: 90, Op2: 100 |
   | B | between | Op1: 80, Op2: 89 |
   | C | between | Op1: 70, Op2: 79 |
   | D | between | Op2: 60, Op2: 69 |
   | F | <= | 59 |

   There are five groups in the order from A to F. If you want to change the order of the groups, you can also do so via the User Defined Group dialog box.
3. Select **Keep values outside of the range in special group** checkbox if you want to put the values that are not included in the specified criteria in a new special group, and then provide a name for the special group in the **Special Group Name** text box.
4. Select **OK** to accept the settings.
5. Select **Finish** in the chart wizard to apply the changes.

## Grouping Data by Intervals

For a chart that uses a query resource in a page report, if the data type of the field on the category/series axis of the chart (for a heat map, a group-by field) is of the Numeric, String, Date, Time, or DateTime type, you can specify special functions to the field so as to group the corresponding data by intervals.

1. When creating or editing a chart with wizard, select the **Special Function** button in the **Display** screen. Designer displays the Special Function dialog box.

   ![Special Function dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848493463/spclfctn.gif)
2. Select the [special function](https://devnet.logianalytics.com/hc/en-us/articles/1500010094941-Grouping-the-Data-in-Tables#FunctionList) for the category/series/group field from the **Function** drop-down list, then select **OK**.
3. Select **Finish** in the chart wizard to apply the selected special function to the field.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* The special function for field on the category axis should be the same as that of the summary on the value axis. If you add a summary with a special function to the value axis, Designer applies the special function automatically to the field on the category axis and you cannot change the function. If you want to apply a special function to the summary on the value axis, you should make sure the category field has the same special function. When the summary applies no special function, you can add any special function to the category field as you want.
* If you have defined a special function to the group-by field of a table or banded object, and insert a chart in the table or banded object which inherits dataset from the parent and has the same grouping structure with the parent, Designer applies the special function defined for the field to the chart too. You can specify another special function to the field on the chart axis if you want.
* When you define both special functions and Select N conditions in a chart, the former takes higher priority, meaning, grouping data by intervals takes effect before Top/Bottom N.

## Setting Order/Select N Condition

One of the most difficult problems with charts is when there are too many category or series values, the chart becomes unreadable and also can become very slow to run, so you may want to show only specified category/series values in a chart and make the values sort according to a specified order. To achieve this, you can use the Order/Select N feature. By applying a Order/Select N condition to a chart, you can decide how many category/series values you want to display in the chart and how to sort the values. You can even use an Integer-typed parameter to control the value of Select N. The Order/Select N feature works on the groups of heat maps as well.

1. When creating or editing a chart with wizard, select the **Order/Select N** button in the **Display** screen. Designer displays the [Category Options](https://devnet.logianalytics.com/hc/en-us/articles/1500010058442-Category-Options-Dialog-Box)/[Series Options](https://devnet.logianalytics.com/hc/en-us/articles/1500010098601-Series-Options-Dialog-Box)/[Group Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097481-Group-Options-Dialog-Box).

   ![Category Options dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856984471/ctgryoptn.gif)
2. In the **Category Order**/**Series Order**/**Group Order** box of the dialog box, specify the sort order of the category/series/group values.
   * **Ascend**  
     Sorts values in an ascending order.
   * **Descend**  
     Sorts values in a descending order.
   * **No Sort**  
     Values are not sorted and appear in the original order from the database.
3. Specify the **Select** condition to **All**, **Top N**, or **Bottom N**.
   * **All**  
      If selected, the chart displays all the category/series/group values.
   * **Top/Bottom N**   
      If selected, the combo box to the right is enabled and you can specify an integer number in the text box, or select a parameter which returns an integer from the drop-down list to dynamically define the Top/Bottom N condition, then the chart only displays the first or last N (N is the number you specify by the integer or parameter) category/series/group values.

     ![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4404856819991/criticalicon.gif) If you use an Integer-typed parameter to define the Top/Bottom N condition dynamically at runtime, you should make sure that the parameter has at least one default value that is larger than 0; otherwise, you get exceptions when running the report on Server.
4. Select the **Based On** checkbox and specify values for the options that follow.

   If Based On is unselected, Logi Report sorts all the category/series/group values or its first/last N values in the order you specify in the [Category/Series/Group Order box](#Order) of the dialog box; if you select Based On, you can make the values sorted based on a field added to the value axis of the chart and select a radio button next to the Based On drop-down list to specify the sort order as you want. When you select **Custom Sort** from the Based On drop-down list, you can customize the fields based on which to sort the values and set the sort order for each sort-by field using the [Custom Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095981-Custom-Sort-Dialog-Box).
5. If you have selected Top N or Bottom N from the Select drop-down list, you can select the **Remaining Categories In** checkbox and then type a character string in the text box, Logi Report then merges the category/series/group values beyond the first or last N range into the group with the name as that character string.
6. If you are specifying the Order/Select N condition for the category field, you can also select **Overall Series** to specify to calculate the top or bottom N category values based on the series values.
7. You can select **Skip First** and type a number M in the text box, Logi Report then skips the first M category/series/group values, and the Select N condition begins with "M+1". Logi Report merges the skipped values into the Remaining Categories group.
8. Select **OK** to accept the settings.
9. Select **Finish** in the chart wizard to apply the changes.

The following example shows the usage of the Order/Select N feature on charts in detail.

1. Make sure **SampleReports.cat** is the currently open catalog file. If not, select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Select **File** > **New** > **Web Report** to create a web report.
3. [Insert a chart in the web report](https://devnet.logianalytics.com/hc/en-us/articles/1500010057042-Inserting-Charts-in-a-Report#BV) as follows:

* Use **WorldWideSalesBV** in Data Source 1 of the catalog as the data source.
* Display in the **Clustered Bar 2-D** chart type.
* Show **Product ID** on the category axis and **Total Sales** on the value axis.
* Apply the **Classic** style.

4. Save the report and select the **View** tab to preview the chart. The chart appears as follows:

   ![Chart Result Based on BV](https://devnet.logianalytics.com/hc/article_attachments/4404848690199/cmpnt_cht_mdfy_slctn1.gif)
5. Right-click the chart and select **Chart Wizard** from the shortcut menu. Designer displays the Chart Wizard dialog box.
6. In the Display screen, select the **Order/Select N**button below the Category box.
7. In the Category Options dialog box, set the Select condition to **Top 6**, based on **Total Sales** descending, then select the **Remaining Categories In** checkbox and type **Other** in the text box so as to put the categories that do not meet the condition into the Other group. Select **OK** to accept the settings and leave the dialog box.

   ![Set Category Options](https://devnet.logianalytics.com/hc/article_attachments/4404857059479/cmpnt_cht_mdfy_slctn2.gif)
8. Select **Finish** in the Chart Wizard dialog box to finish editing the chart.
9. Preview the chart again. It now shows as follows:

   ![Chart Result](https://devnet.logianalytics.com/hc/article_attachments/4404857059735/cmpnt_cht_mdfy_slctn3.gif)
10. Select the **Design** tab to go back to design mode and repeat step 5 to 7.
11. In the Category Options dialog box, select the **Skip First** checkbox and input **2** in the text box, then select **OK**.
12. Select **Finish** in the Chart Wizard dialog box.
13. Preview the chart and the result changes to below:

    ![Chart Result for Skipping the First 2 Categories](https://devnet.logianalytics.com/hc/article_attachments/4404848690455/cmpnt_cht_mdfy_slctn4.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057042-Inserting-Charts-in-a-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094401-Formatting-Chart-Elements)
