---
title: "Editing Range Groups on Category Values"
id: 1500009606142
section: "Working with Components in Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009606142-Editing-Range-Groups-on-Category-Values
updated_at: 2021-07-24T16:05:18Z
---

# Editing Range Groups on Category Values

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009606082-Labeling-Time-Series-Data-by-Constant-Interval) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009606182-Creating-Scrollable-Charts)

# Editing Range Groups on Category Values

Logi Report supports dividing data on the category axis of a chart into different range groups based on certain group criteria and customizing the data labels displayed for each range group to show required information. This can help you compare the information of the range groups. For example, suppose that you have a chart showing the total sales of each month in 2015 and 2016. Now you want to compare the total sales of the two years and also the percentage each month occupies. You can then apply this feature on the chart to achieve your goal.

The Range Group feature is supported on charts of the Bar, Bench, Line, and Area types that are created based on business views only.

The following example shows the usage in detail.

1. Make sure SampleReports.cat is the currently open catalog file. If not select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Select **File** > **New** > **Web Report** to create a web report.
3. [Insert a chart in the web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009628941-Inserting-Charts-in-a-Report#BV) as follows:

* Use WorldWideSalesBV in Data Source 1 of the catalog as the data source.
* Display in the Clustered Bar 2-D chart type.
* Show Sales Month on the category axis and Total Sales on the value axis.

4. Save the report and select the **View** tab to preview the chart. The chart appears as follows:

   ![Result of Clustered Bar 2-D](https://devnet.logianalytics.com/hc/article_attachments/4404904453783/cmpnt_cht_range2.gif)
5. Select the **Design** tab to return to the design mode.
6. Right-click the chart and select **Format Axes** > **Format Category (X) Axis** from the shortcut menu. The Format Category (X) Axis dialog appears.
7. Go to the **Range** > **Properties** tab, select the **Enable Range** option and then select the **Special Group** button to display the [User Defined Group](https://devnet.logianalytics.com/hc/en-us/articles/1500009610722-User-Defined-Group-Dialog) dialog.
8. Define two range groups as follows and select **OK**.

   ![Define Range Groups](https://devnet.logianalytics.com/hc/article_attachments/4404904454039/cmpnt_cht_range3.gif)
9. In the Gridline box, specify the line color as **#FF0000** and thickness as **2 px** for the separating line, then in the Fill box, specify the background colors of the 2015 and 2016 range groups as **#FFFFCC** and **#CCFFFF**.

   ![Set Range Properties](https://devnet.logianalytics.com/hc/article_attachments/4404904454295/cmpnt_cht_range4.gif)
10. Select the **Data Label**  sub tab, select the **Show Data Label** option and then select the **Edit Data Labels** button to display the [Data Label Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009630481-Data-Label-Editor-Dialog). You can see there are three data labels which represent the category ranges, the summary field names and values respectively by default. Select **OK**.

    ![Data Label Editor](https://devnet.logianalytics.com/hc/article_attachments/4404904454551/cmpnt_cht_range5.gif)
11. Select **value and percent** from the Data Label Type drop-down list. Select **OK**.
12. Select the **View** tab to preview the chart. The category values are now divided into two range groups with different background colors. In each range group, the data labels display the year information and the total sales of each year as well as the percentage of the total sales each year occupies.

    ![Result of Clustered Bar 2-D with Category Values in Two Range Groups](https://devnet.logianalytics.com/hc/article_attachments/4404904454935/cmpnt_cht_range6.gif)
13. Select the **Design** tab to return to the design mode. This time we will format some properties of the areas that display the data labels on the range groups and make the data labels show total sales of each month instead.
14. Right-click the chart and select **Format Axes** > **Format Category (X) Axis** from the shortcut menu to open the Format Category (X) Axis dialog again.
15. Go to the **Range** > **Data Label**  tab, in the Border box, specify Color as **#606060**, select the first item from the Line Style drop-down list, set Thickness to **2 px**.

    ![Set Data Label for Range](https://devnet.logianalytics.com/hc/article_attachments/4404904455191/cmpnt_cht_range7.gif)
16. Select the **Edit Data Labels** button to display the Data Label Editor.
17. Select **[Category]** from the first drop-down list of the last iterator.
18. Select on the right of the last drop-down list to select the last iterator, then right-click the iterator and
    select **Chart Iterator** from the shortcut menu to display the Chart Iterator dialog.

    ![Data Label Editor](https://devnet.logianalytics.com/hc/article_attachments/4404904455447/cmpnt_cht_range8.gif)
19. Select the **Category** option in the Iterated By box and select **OK**.

    ![Chart Iterator dialog - Iteration](https://devnet.logianalytics.com/hc/article_attachments/4404904455703/cmpnt_cht_range9.gif)
20. select **OK** in the Data Label Editor and Format Category (X) Axis dialog respectively to close them and apply the settings.
21. Resize the chart and preview it again. The border of the data label areas is displayed and the data labels now show the total sales of each month and the percentage each month occupies. You can put the mouse over the data labels when they cannot be completely displayed to get the full text.

    ![Clustered Bar 2-D Result](https://devnet.logianalytics.com/hc/article_attachments/4404904456215/cmpnt_cht_range10.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009606082-Labeling-Time-Series-Data-by-Constant-Interval) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009606182-Creating-Scrollable-Charts)
