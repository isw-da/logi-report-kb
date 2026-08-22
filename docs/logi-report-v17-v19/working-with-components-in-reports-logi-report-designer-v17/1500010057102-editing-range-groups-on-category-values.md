---
title: "Editing Range Groups on Category Values"
id: 1500010057102
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010057102-Editing-Range-Groups-on-Category-Values
updated_at: 2021-07-23T19:14:43Z
---

# Editing Range Groups on Category Values

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057062-Labeling-Time-Series-Data-by-Constant-Interval)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057142-Creating-Scrollable-Charts)

# Editing Range Groups on Category Values

In Designer, you can divide data on the category axis of a chart into different range groups based on certain group criteria and customize the data labels for each range group to show required information. This can help you compare the chart data in the way you desire. This topic presents an example to show you how to customize range groups in a chart.

You can use the Range Group feature on charts which meet the following conditions:

* The chart is of the Bar, Bench, Line, or Area type.
* The value fields of the chart do not contain detail information. For example, for a business view-based chart, its value fields cannot be the detail objects in the business view.

In the following example, it is supposed that you have a chart showing the total sales of each month in 2015 and 2016, and you want to compare the total sales of the two years and also the percentage each month occupies. Take the following steps to define the range groups:

1. Make sure **SampleReports.cat** is the currently open catalog file. If not, select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Select **File** > **New** > **Web Report** to create a web report.
3. [Insert a chart in the web report](https://devnet.logianalytics.com/hc/en-us/articles/1500010057042-Inserting-Charts-in-a-Report#BV) as follows:

* Use **WorldWideSalesBV** in Data Source 1 of the catalog as the data source.
* Display in the **Clustered Bar 2-D** chart type.
* Show **Sales Month** on the category axis and **Total Sales** on the value axis.

4. Save the report and select the **View** tab to preview the chart. The chart appears as follows:

   ![Initial Chart Result](https://devnet.logianalytics.com/hc/article_attachments/4404857057047/cmpnt_cht_range2.gif)
5. Select the **Design** tab to return to design mode.
6. Right-click the chart and select **Format Axes** > **Format Category (X) Axis** from the shortcut menu. Designer displays the Format Category (X) Axis dialog box.
7. Select the **Range** > **Properties** tab, select the **Enable Range** option and then select the **Special Group** button to open the [User Defined Group dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060782-User-Defined-Group-Dialog-Box).
8. Select the **Add** button two times and define the two range groups as follows:

   ![Define Range Groups](https://devnet.logianalytics.com/hc/article_attachments/4404848688279/cmpnt_cht_range3.gif)
9. Select the **Keep values outside of the range in special group** checkbox and keep the default name for the special group.
10. Select **OK** to apply the range groups and return to the Format Category (X) Axis dialog box.
11. In the **Gridline** box, specify the line color as **FF0000** and thickness as **2 px** for the separating line, then in the **Fill** box, specify the background colors of the 2015 and 2016 range groups as **FFFFCC** and **CCFFFF**.

    ![Set Range Properties](https://devnet.logianalytics.com/hc/article_attachments/4404857057303/cmpnt_cht_range4.gif)
12. Select the **Data Label** sub tab, select the **Show Data Label** option and then select the **Edit Data Labels** button. Designer displays the [Data Label Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058562-Data-Label-Editor-Dialog-Box). You can see there are three data labels which represent the category ranges, the summary field name, and the values of the summary field respectively by default. Select **OK** to go back to the Format Category (X) Axis dialog box.

    ![Data Label Editor dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848688535/cmpnt_cht_range5.gif)
13. Select **value and percent** from the **Data Label Type** drop-down list. Select **OK**.
14. Select the **View** tab to preview the chart again. Designer divides the category values into two range groups with different background colors. In each range group, the data labels display the year information and the total sales of each year, as well as the percentage of the total sales each year occupies.

    ![Chart Result with Category Values in Two Range Groups](https://devnet.logianalytics.com/hc/article_attachments/4404857057559/cmpnt_cht_range6.gif)
15. Select the **Design** tab to return to design mode.

    This time, we format some properties of the areas that display the data labels on the range groups and make the data labels show total sales of each month instead.
16. Right-click the chart and select **Format Axes** > **Format Category (X) Axis** from the shortcut menu to open the Format Category (X) Axis dialog box again.
17. Go to the **Range** > **Data Label** tab, in the **Border** box, specify **Color** as **606060**, select the first item from the **Line Style** drop-down list, set **Thickness** to **2 px**.

    ![Set Data Label for Range](https://devnet.logianalytics.com/hc/article_attachments/4404857058071/cmpnt_cht_range7.gif)
18. Select the **Edit Data Labels** button to open the Data Label Editor dialog box.
19. Select **[Category]** from the drop-down list of the first iterator.
20. Right-click the blank area in the Data Label Editor dialog box and
    select **Chart Iterator** from the shortcut menu.

    ![Method to Open the Chart Iterator dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404857058455/cmpnt_cht_range8.gif)

    Designer displays the [Chart Iterator dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058182-Chart-Iterator-Dialog-Box).
21. Select **Category** in the **Iterated By** box and select **OK**.

    ![Specify the Iterator](https://devnet.logianalytics.com/hc/article_attachments/4404848688791/cmpnt_cht_range9.gif)
22. Select **OK** in the Data Label Editor and Format Category (X) Axis dialog boxes respectively to close them and apply the settings.
23. Resize the chart and preview it again. Designer displays the border of the data label areas and the data labels now show the total sales of each month and the percentage each month occupies. You can put the mouse over the data labels when they cannot completely display to get the full text.

    ![Iterated Data Lables by Category](https://devnet.logianalytics.com/hc/article_attachments/4404857058839/cmpnt_cht_range10.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057062-Labeling-Time-Series-Data-by-Constant-Interval)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057142-Creating-Scrollable-Charts)
