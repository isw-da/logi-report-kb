---
title: "Creating Dynamic Charts in Excel"
id: 1500009583421
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009583421-Creating-Dynamic-Charts-in-Excel
updated_at: 2021-07-24T05:56:10Z
---

# Creating Dynamic Charts in Excel

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583361-Creating-a-Back-to-back-Bench-Chart)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584261-Tables)

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

The following example shows how to use the Dynamic Chart feature in Excel. Here the chart inherits data from its parent banded object.

1. [Open the catalog file](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog) SampleReports.cat in `<install_root>\Demo\Reports\SampleReports`.
2. [Create a query](https://devnet.logianalytics.com/hc/en-us/articles/1500009592461-Creating-a-Query) named Products in Data Source 1 of the catalog, which contains the table Products with all of its columns.
3. [Create a page report with a banded object in it](https://devnet.logianalytics.com/hc/en-us/articles/1500009592821-Creating-a-Page-Report) based on the query Products. The banded report displays the following fields: Product ID, Product Name and Price, is grouped by Category and Product Type Name (Category is the higher level), and takes the Neutral report style. Resize the fields and it displays as follows:

   ![Banded Object](https://devnet.logianalytics.com/hc/article_attachments/4404889424279/cmpnt_cht_dynmc5.gif)
4. In the Data panel, select **<New Summary...>** from the Summaries node and [create a summary](https://devnet.logianalytics.com/hc/en-us/articles/1500009589741-Creating-a-Summary) named Sum\_Price which uses the function Sum, sums on Price in the Products table, and applies to the Product Type Name group level.

   ![New Summary dialog](https://devnet.logianalytics.com/hc/article_attachments/4404894003095/cmpnt_cht_dynmc6.gif)
5. Drag the summary to the footer panel of the Product Type Name group level in the banded object.

   ![Banded object](https://devnet.logianalytics.com/hc/article_attachments/4404894003351/cmpnt_cht_dynmc7.gif)
6. Select **Insert** > **Chart** to insert a Clustered Bar 2-D chart into the banded header panel.
   The chart inherits the dataset from the banded object (make sure Current Dataset is checked in the Data screen of the Create Chart wizard), displays Product Type Name on the category axis, Category on the series axis, and Sum\_Price on the value axis.

   ![Chart in Banded object](https://devnet.logianalytics.com/hc/article_attachments/4404889424535/cmpnt_cht_dynmc8.gif)
7. Right-click the chart and select **Chart Wizard** from the shortcut menu.
8. In the Chart Wizard, switch to the **Layout** screen, select **Export** in the Options box and then select **BandedObject** from the Mapping Component drop-down list, then select **Finish**.

   ![Chart Wizard - Layout](https://devnet.logianalytics.com/hc/article_attachments/4404889424791/cmpnt_cht_dynmc9.gif)
9. Select **File** > **Options**. In the Options dialog, check the option **Check the availability of dynamic chart for Excel** in the General category, then select **OK**.

   This option is provided to check if the chart can be correctly mapped to the banded object when you save the report or export it to Excel.
10. Select **File** > **Export** > **Excel** to export the report to Excel (make sure Report Format is checked in the Export to Excel dialog).

    ![Export to Excel dialog](https://devnet.logianalytics.com/hc/article_attachments/4404894003607/cmpnt_cht_dynmc11.gif)
11. Open the exported result file in `<install_root>\Demo\Reports\SampleReports`.

    ![](https://devnet.logianalytics.com/hc/article_attachments/4404889425047/cmpnt_cht_dynmc1.gif)
12. Change the price of Gold Coast Blend and Colombia El Tambo to **30.00**, and you will find that the value of the chart is changed accordingly.

    ![](https://devnet.logianalytics.com/hc/article_attachments/4404894003863/cmpnt_cht_dynmc2.gif)

**Notes:**

* You cannot make charts of bubble, stock and scatter types to be dynamic charts if they have summary value on the value axis.
* Chart and the summary used in the chart cannot be inserted into the repeated panel of the banded object or table.
* For summary chart, only value axis can be mapped to each single cell in Excel. That is to say, when you change the data in Excel, the corresponding value axis will also be changed.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583361-Creating-a-Back-to-back-Bench-Chart)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584261-Tables)
