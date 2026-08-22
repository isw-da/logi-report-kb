---
title: "Labeling Time Series Data by Constant Interval"
id: 1500010028982
section: "Working with Components in Reports - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010028982-Labeling-Time-Series-Data-by-Constant-Interval
updated_at: 2021-07-24T10:39:25Z
---

# Labeling Time Series Data by Constant Interval

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010063341-Applying-Conditional-Color-Fills-to-Charts) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010029022-Editing-Range-Groups-on-Category-Values)

# Labeling Time Series Data by Constant Interval

Time series data is data collected over time for a single or a group of variables. When using date series and time series values on the category (X) axis of a chart, it is often beneficial to see the chart with constant ranges rather than just what is in the data values. Missing values for weekends and holidays leaves gaps which distorts the chart and might lead to incorrect decisions.

The following example shows how to use a constant interval to label time series data on the category axis:

1. Make sure SampleReports.cat is the currently open catalog file. If not select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Select **File** > **New** > **Web Report** to create a web report.
3. [Insert a chart in the web report](https://devnet.logianalytics.com/hc/en-us/articles/1500010063601-Inserting-Charts-in-a-Report#BV) as follows:
   * Use WorldWideSalesBV in Data Source 1 of the catalog as the data source.
   * Display in the Line 2-D chart type.
   * Show Order Date on the category axis and Total Quantity on the value axis.
   * Apply the following filter:

     ![Filter Conditions for Chart](https://devnet.logianalytics.com/hc/article_attachments/4404901336343/cmpnt_cht_intvl1.gif)
4. Save the report and select the **View** tab to preview the chart. The chart appears as follows:

   ![Initial Chart](https://devnet.logianalytics.com/hc/article_attachments/4404909285271/cmpnt_cht_intvl2.gif)
5. Select the **Design** tab to return to the design mode.
6. Right-click the chart and select **Format Axes** > **Format Category (X) Axis** from the shortcut menu. The Format Category (X) Axis dialog appears.
7. In the Tick Mark tab of the dialog, select the **Minor Tick Mark** sub tab, check **Inside** in the Type box to show the minor tick marks inside the axis, and then check **Show Minor Tick Mark Labels** in the Option box to show the minor tick mark labels.

   ![Set Minor Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4404901336727/cmpnt_cht_intvl3.gif)
8. Select the **Scale** sub tab, check the **Use Constant Interval** option, then set the Minimum, Maximum, Major Unit and Minor Unit options to **Fixed**. Specify the minimum value to **Jan 1, 2015** and the maximum value to **Jan 29, 2015**. Set the Major Unit and Minor Unit values to **1** and select the unit as **Weeks** and **Days** respectively which stand for 1 week and 1 day.

   ![Set Tick Mark Scale](https://devnet.logianalytics.com/hc/article_attachments/4404909285527/cmpnt_cht_intvl4.gif)

   When specifying the Minimum/Maximum value, you can also select ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4404909137175/btn_clndr.gif) to select a date and time value from the calendar if the field on the category axis is of Date, DateTime or Time type, or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404901133335/btn_fmla.gif) and [Select a formula to control the value](https://devnet.logianalytics.com/hc/en-us/articles/1500010033202-Using-Formulas-to-Control-Object-Properties). When a DBField is selected from the drop-down list, its first record in the database will be used as the value. If the selected formula references a parameter, you can dynamically specify the minimum/maximum value at runtime.
9. In the Minor Label sub tab of the Format tab, select the format in the Stack box and select **Remove** to delete it. Select **Date/Time** from the Category box, input **d** in the Properties text box and select **Add** to add the format to the Stack box. Then select **OK** to apply the settings.

   ![Set Format for Minor Label](https://devnet.logianalytics.com/hc/article_attachments/4404901336983/cmpnt_cht_intvl5.gif)
10. Double-click the line to bring out the Format Line dialog. In the Node tab, select **Use Single Color**, then select **true** from the Show Node drop-down list to show nodes on the line, and specify the node color to **#000000**. Select **OK** to accept the settings.

    ![Set Line Node](https://devnet.logianalytics.com/hc/article_attachments/4404909285783/cmpnt_cht_intvl6.gif)
11. Resize the chart and preview it again. The chart now shows as follows:

    ![Line Chart with Constant Interval Labeled Time Series](https://devnet.logianalytics.com/hc/article_attachments/4404909286039/cmpnt_cht_intvl7.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010063341-Applying-Conditional-Color-Fills-to-Charts) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010029022-Editing-Range-Groups-on-Category-Values)
