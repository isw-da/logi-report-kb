---
title: "Labeling Time Series Data by Constant Interval"
id: 1500010057062
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010057062-Labeling-Time-Series-Data-by-Constant-Interval
updated_at: 2021-07-23T19:14:43Z
---

# Labeling Time Series Data by Constant Interval

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094361-Applying-Conditional-Color-Fills-to-Charts)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057102-Editing-Range-Groups-on-Category-Values)

# Labeling Time Series Data by Constant Interval

Time series data is data collected over time for a single or a group of variables. When using date series and time series values on the category (X) axis of a chart, it is often beneficial to see the chart with constant ranges rather than just what is in the data values. This can avoid the missing values for weekends and holidays that may leave gaps in the chart which distorts the chart and might lead to incorrect decisions. This topic presents an example to show how you can use a constant interval to label time series data on the category axis of a chart.

1. Make sure **SampleReports.cat** is the currently open catalog file. If not, select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Select **File** > **New** > **Web Report** to create a web report.
3. [Insert a chart in the web report](https://devnet.logianalytics.com/hc/en-us/articles/1500010057042-Inserting-Charts-in-a-Report#BV) as follows:
   * Use **WorldWideSalesBV** in Data Source 1 of the catalog as the data source.
   * Display in the **Line 2-D** chart type.
   * Show **Order Date** on the category axis and **Total Quantity** on the value axis.
   * Apply the following filter:

     ![Filter Conditions for Chart](https://devnet.logianalytics.com/hc/article_attachments/4404848690711/cmpnt_cht_intvl1.gif)
4. Save the report and select the **View** tab to preview the chart. The chart appears as follows:

   ![Initial Chart](https://devnet.logianalytics.com/hc/article_attachments/4404848690967/cmpnt_cht_intvl2.gif)
5. Select the **Design** tab to return to design mode.
6. Right-click the chart and select **Format Axes** > **Format Category (X) Axis** from the shortcut menu. Designer displays the Format Category (X) Axis dialog box.
7. In the **Tick Mark** tab of the dialog box, select the **Minor Tick Mark** sub tab, select **Inside** in the **Type** box to show the minor tick marks inside the axis, and then select **Show Minor Tick Mark Labels** in the **Option** box to show the minor tick mark labels.

   ![Set Minor Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4404848691479/cmpnt_cht_intvl3.gif)
8. Select the **Scale** sub tab, select the **Use Constant Interval** option, then set the **Minimum**, **Maximum**, **Major Unit**, and **Minor Unit** options to **Fixed**. Specify the minimum value to **Jan 1, 2015** and the maximum value to **Jan 29, 2015**. Set the Major Unit and Minor Unit values to **1** and select the unit as **Weeks** and **Days** respectively which stand for 1 week and 1 day.

   ![Set Tick Mark Scale](https://devnet.logianalytics.com/hc/article_attachments/4404848691735/cmpnt_cht_intvl4.gif)

   When specifying the Minimum/Maximum value, you can also select the **calendar** button ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4404848444439/btn_clndr.gif) to select a date and time value from the calendar if the field on the category axis is of the Date, Time, or DateTime type, or select the **Formula** button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif) and [select a formula to control the value](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties). When you select a DBField from the drop-down list, Logi Report applies its first record in the database as the value. If the selected formula references a parameter, the report users can dynamically specify the minimum/maximum value at runtime.
9. In the **Minor Label** sub tab of the **Format** tab, select the format in the **Stack** box and select **Remove** to delete it. Select **Date/Time** from the **Category** box, type **d** in the **Properties** text box and select **Add** to add the format to the Stack box. Then select **OK** to apply the settings.

   ![Set Format for Minor Label](https://devnet.logianalytics.com/hc/article_attachments/4404848691991/cmpnt_cht_intvl5.gif)
10. Double-click the line. Designer displays the Format Line dialog box.
11. In the **Node** tab, select **Use Single Color**, then select **true** from the **Show Node** drop-down list to show nodes on the line, and specify the node color to **#000000**. Select **OK** to accept the settings.

    ![Set Line Node](https://devnet.logianalytics.com/hc/article_attachments/4404857059991/cmpnt_cht_intvl6.gif)
12. Resize the chart and preview it again. The chart now shows as follows:

    ![Line Chart with Constant Interval Labeled Time Series](https://devnet.logianalytics.com/hc/article_attachments/4404857060247/cmpnt_cht_intvl7.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094361-Applying-Conditional-Color-Fills-to-Charts)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057102-Editing-Range-Groups-on-Category-Values)
