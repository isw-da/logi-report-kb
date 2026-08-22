---
title: "Labeling Time Series Data by Constant Interval"
id: 4405661367447
section: "Working with Components in Reports - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661367447-Labeling-Time-Series-Data-by-Constant-Interval
updated_at: 2022-01-27T20:34:28Z
---

# Labeling Time Series Data by Constant Interval

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664369943-Applying-Conditional-Color-Fills-to-Charts)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661370647-Editing-Range-Groups-on-Category-Values)

# Labeling Time Series Data by Constant Interval

Time series data is data collected over time for a single or a group of variables. When using date series and time series values on the category (X) axis of a chart, it is often beneficial to see the chart with constant ranges rather than just what is in the data values. This can avoid the missing values for weekends and holidays that may leave gaps in the chart which distorts the chart and might lead to incorrect decisions. This topic presents an example to show how you can use a constant interval to label time series data on the category axis of a chart.

1. Make sure **SampleReports.cat** is the currently open catalog file. If not, navigate to **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Navigate to **File** > **New** > **Web Report** to create a web report.
3. [Insert a chart in the web report](https://devnet.logianalytics.com/hc/en-us/articles/4405664387479-Inserting-Charts-in-a-Report#BV) as follows:
   * Use **WorldWideSalesBV** in Data Source 1 of the catalog.
   * Display in the **Line 2-D** chart type.
   * Show **Order Date** on the category axis and **Total Quantity** on the value axis.
   * Apply the filter "Order Date >= 2015-01-06 And Order Date <= 2015-01-28".
   * Use the **Basic** style.
4. Save the report and select the **View** tab to preview the chart.

   ![Initial Chart](https://devnet.logianalytics.com/hc/article_attachments/4420410923543/cmpnt_cht_intvl2.gif)
5. Select the **Design** tab to return to design mode.
6. Right-click the chart and navigate to **Format Axes** > **Format Category (X) Axis** on the shortcut menu. Designer displays the Format Category (X) Axis dialog box.
7. In the **Tick Mark** tab, select the **Minor Tick Mark** subtab, select **Inside** in the **Type** box to show the minor tick marks inside the axis, and then select **Show Minor Tick Mark Labels** in the **Option** box to show the minor tick mark labels.

   ![Set Minor Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4420394920983/cmpnt_cht_intvl3.gif)
8. Select the **Scale** subtab, select **Use Constant Interval**, then set **Minimum**, **Maximum**, **Major Unit**, and **Minor Unit** to **Fixed**. Specify the minimum value to **Jan 1, 2015** and the maximum value to **Jan 29, 2015**. Set Major Unit and Minor Unit to **1** and select the unit as **Weeks** and **Days** respectively which stand for 1 week and 1 day.

   ![Set Tick Mark Scale](https://devnet.logianalytics.com/hc/article_attachments/4420410923927/cmpnt_cht_intvl4.gif)

   When specifying the Minimum and Maximum values, you can also select the **calendar**![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4420402355351/btn_clndr.gif) to select a date and time value from the calendar widget if the field on the category axis is Date, Time, or DateTime data type, or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4420410598551/btn_fmla.gif) and [select a formula](https://devnet.logianalytics.com/hc/en-us/articles/4405664601367-Using-Formulas-to-Control-Object-Properties) or DBField from the drop-down list to control the value. If you select a DBField, Designer applies its first record in the database as the value; if you select a formula which references a parameter, users can dynamically specify the minimum/maximum value at runtime.
9. Select the **Format** tab and then the **Minor Label** subtab, select the format in the **Stack** box and select **Remove** to delete it. Select **Date/Time** from the **Category** box, type **d** in the **Properties** text box and select **Add** to add the format to the Stack box.

   ![Set Format for Minor Label](https://devnet.logianalytics.com/hc/article_attachments/4420394925207/cmpnt_cht_intvl5.gif)
10. Select **OK** in the Format Category (X) Axis dialog box to apply the axis settings.
11. Double-click the line. Designer displays the Format Line dialog box.
12. In the **Node** tab, select **Use Single Color**, then select **true** from the **Show Node** drop-down list to show nodes on the line, and specify the node color to **#000000**. Select **OK** to accept the settings.

    ![Set Line Node](https://devnet.logianalytics.com/hc/article_attachments/4420410925719/cmpnt_cht_intvl6.gif)
13. Resize the chart and preview it again.

    ![Line Chart with Constant Interval Labeled Time Series](https://devnet.logianalytics.com/hc/article_attachments/4420394925719/cmpnt_cht_intvl7.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664369943-Applying-Conditional-Color-Fills-to-Charts)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661370647-Editing-Range-Groups-on-Category-Values)
