---
title: "Creating Dynamic Charts in Excel"
id: 1500009605662
section: "Working with Components in Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009605662-Creating-Dynamic-Charts-in-Excel
updated_at: 2021-07-24T16:05:22Z
---

# Creating Dynamic Charts in Excel

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009629001-Creating-Motion-Charts) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009629261-Tables)

# Creating Dynamic Charts in Excel

You can make data in a chart map to a single cell in Excel, then when you change the data in a cell, the corresponding change will also be displayed in the chart. This kind of chart is called dynamic chart. To create a dynamic chart in Excel, the chart should use the same data as a banded object or table, which is exported to Excel together with the chart. That is to say, each data value in the chart must correspond to the one in the banded object or table. Moreover, the option Report Format should be selected when exporting the report to Excel.

To have the same data with a banded object or table, you must meet the following conditions for the chart before exporting the report to Excel:

* When the chart inherits data from the banded object or table:
  + The chart should have the same group structure as that of the banded object or table.

    The following example further explains what the same group structure means.

    A banded object has two groups: group 1 and group 2 (group 1 is the higher level)

    - When the chart is to be inserted into the banded header panel:
      * Add the summary 2 based on group 2 to the value axis, then group 2 will be added to the category axis automatically, and you need to add group 1 to the series axis manually.
      * Add the summary 1 based on group 1 to the value axis, then group 1 will be added to the category axis automatically, and no value need to be added to the series axis.
    - When the chart is to be inserted into the group header panel 1 which displays group 1, only summary 2 based on group 2 can be added to the value axis. Then group 2 will be added to the category axis, and no value will be added to the series axis.
    - When the chart is to be inserted into the group header panel 2 which displays group 2, the value axis cannot contain any summary value.
  + Different conditions apply to chart based on only detailed records and chart containing summary information:
    - The former does not contain summary value on the value axis, but DBFields. The DBFields on the value axis and the value on the category axis must be in the detail panel of the banded object or table, and should not be hidden.
    - The latter contains summary value on the value axis, and the summary on the value axis must be in the banded object or table, and should not be hidden.
* When the chart does not inherit data from the banded object or table:
  + The chart should use the same dataset as the banded object or table.
  + The chart should have the same group structure as that of the banded object or table.
  + The chart should have the same filter/sort condition, Top N condition and special function as that of the banded object or table.
  + The chart can only be inserted into the banded header/footer panel or outside of the banded object.
  + Different conditions apply to chart based on only detailed records and chart containing summary information:
    - For a chart based on only detailed records,
      * DBFields on the value axis must be in the detail panel of the banded object or table, and should not be hidden.
      * The category value must be in the detail panel of the banded object or table, and should not be hidden.
      * If the chart, banded object or table has a Top N condition, then the chart will not be mapped to the banded object or table.
    - For a chart containing summary information, the summary on the value axis must be in the banded object or table, and should not be hidden.

The following example shows how to use the Dynamic Chart feature in Excel. Here the chart inherits the dataset from its parent banded object.

1. Make sure SampleReports.cat is the currently open catalog file. If not, select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. [Create a query](https://devnet.logianalytics.com/hc/en-us/articles/1500009635981-Creating-Queries-in-a-Catalog) named Products in Data Source 1 of the catalog, which contains the table Products with all of its columns.
3. Select **File** > **New** > **Page Report** to
   create a page report with a banded object in its first report tab.
4. [Define the banded object](https://devnet.logianalytics.com/hc/en-us/articles/1500009605502-Inserting-a-Banded-Object#Query) as follows:
   * Use the query Products as the data source.
   * Show the following detail fields: Product ID, Product Name and Price.
   * Group by Category and Product Type Name (Category is the higher level).
   * Apply the Classic style.
5. In the Data panel of the main window, select **<New Summary...>** in the Summaries node to [create a summary](https://devnet.logianalytics.com/hc/en-us/articles/1500009611182-Summaries#Create) named Sum\_Price as follows:
   * Use Sum as the aggregate function.
   * Sum on the Price field in the Products table.
   * Apply to the Product Type Name group level.

   ![Create a Summary](https://devnet.logianalytics.com/hc/article_attachments/4404904463255/cmpnt_cht_dynmc1.gif)
6. Drag the summary to the footer panel of the Product Type Name group in the banded object.

   ![Drag the Summary to the Banded Object](https://devnet.logianalytics.com/hc/article_attachments/4404904463511/cmpnt_cht_dynmc2.gif)
7. Drag and drop ![Bar Chart button](https://devnet.logianalytics.com/hc/article_attachments/4404904463767/btn_barcht.gif) from the Components panel to the banded header (BH) panel.
8. In the Create Chart wizard, [define the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009628941-Inserting-Charts-in-a-Report#Query) as follows:
   * Use the current dataset Products used by its parent.
   * Display in the default chart type Clustered Bar 2-D.
   * Show Product Type Name on the category axis, Category on the series axis, and Sum\_Price on the value axis.

   The chart displays in the banded object as follows in the design area:

   ![Insert a Chart](https://devnet.logianalytics.com/hc/article_attachments/4404904464023/cmpnt_cht_dynmc3.gif)
9. Right-click the chart and select **Chart Wizard** from the shortcut menu.
10. In the Chart Wizard, switch to the **Layout** screen, select **Export** in the Options box and then select **BandedObject** from the Mapping Component drop-down list. select **Finish** to accept the change.

    ![Export Setting](https://devnet.logianalytics.com/hc/article_attachments/4404904464279/cmpnt_cht_dynmc4.gif)
11. Select **File** > **Options**. In the Options dialog, select the option **Check the availability of dynamic chart for Excel** in the General category, then select **OK**.

    This option is provided to check if the chart can be correctly mapped to the banded object when you save the report or export it to Excel.
12. Select **File** > **Export** > **To Excel** to export the report to Excel (make sure Report Format is selected in the Export to Excel dialog).

    ![Export to Excel](https://devnet.logianalytics.com/hc/article_attachments/4404904464663/cmpnt_cht_dynmc5.gif)
13. Open the exported result file in `<install_root>\Demo\Reports\SampleReports`.

    ![Exported Result](https://devnet.logianalytics.com/hc/article_attachments/4404904464919/cmpnt_cht_dynmc6.gif)
14. Change the price of Gold Coast Blend and Colombia El Tambo to **30.00**, and you will find that the value of the chart is changed accordingly.

    ![Change Values in the Chart](https://devnet.logianalytics.com/hc/article_attachments/4404904465175/cmpnt_cht_dynmc7.gif)

**Notes:**

* You cannot make charts of bubble, stock and scatter types to be dynamic charts if they have summary value on the value axis.
* Chart and the summary used in the chart cannot be inserted into the repeated panel of the banded object or table.
* For summary chart, only value axis can be mapped to each single cell in Excel. That is to say, when you change the data in Excel, the corresponding value axis will also be changed.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009629001-Creating-Motion-Charts) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009629261-Tables)
