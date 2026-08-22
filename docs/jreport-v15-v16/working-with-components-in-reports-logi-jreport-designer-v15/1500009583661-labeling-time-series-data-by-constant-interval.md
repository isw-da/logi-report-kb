---
title: "Labeling Time Series Data by Constant Interval"
id: 1500009583661
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009583661-Labeling-Time-Series-Data-by-Constant-Interval
updated_at: 2021-07-24T05:56:06Z
---

# Labeling Time Series Data by Constant Interval

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583681-Binding-a-Link-to-a-Chart)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583741-Editing-Range-Groups-on-Category-Values)

# Labeling Time Series Data by Constant Interval

Time series data is data collected over time for a single or a group of variables. When using date series and time series values on the category (X) axis, it is often beneficial to see the chart with constant ranges rather than just what is in the data values. Missing values for weekends and holidays leaves gaps which distorts the chart and might lead to incorrect decisions.

The following example shows how to use a constant interval to label time series data on the category axis:

1. [Open the catalog file](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog) SampleReports.cat in `<install_root>\Demo\Reports\SampleReports`.
2. [Create a web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Create).
3. [Insert a chart in the web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009563242-Inserting-a-Chart#Web) which is based on WorldWideSalesBV in Data Source 1, displays in the Line 2-D chart type, shows Order Date on X-Axis and Total Quantity on Y Values.
4. Right-click the chart in the report and select **Format Filter**  from the shortcut menu to open the Edit Filter dialog.
5. Select **Add Condition** to add a condition line, then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889276567/btn_chsr.gif) next to the field text box, select **Order Date** in the Orders Detail table of the View Element Resources dialog, and select **OK** to return to the Edit Filter dialog. Select **>=** from the operator drop-down list, then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889276567/btn_chsr.gif) next to the value text box, double-click **2015-01-06** in the Value tab of the Values dialog to select it, and close the dialog to return to the Edit Filter dialog.
6. Repeat the step above to add another condition line and set the the condition to **Order Date <= 2015-01-28**. Specify the relationship between the two conditions as **And**.
   Select **OK**.

   ![Edit Filter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889422359/cmpnt_cht_intvl_cht6.gif)
7. Select the **View** tab to view this chart, and it appears as follows:

   ![Line chart in Web Report](https://devnet.logianalytics.com/hc/article_attachments/4404894001303/cmpnt_cht_intvl_tkmk1.gif)
8. Select the **Design** tab to return to the design mode.
9. Right-click the chart and select **Format Axes** > **Format Category (X) Axis** from the shortcut menu. The Format Category (X) Axis dialog appears.
10. In the Tick Mark tab of the dialog, select the **Minor Tick Mark** sub tab, check **Inside** in the Type box to show the minor tick marks inside the axis, and then check **Show Minor Tick Mark Labels** in the Option box to show the minor tick mark labels.

    ![Format Category (X) Axis - Tick Mark - Minor](https://devnet.logianalytics.com/hc/article_attachments/4404889422615/cmpnt_cht_intvl_cht7.gif)
11. Select the **Scale** sub tab, check the **Use Constant Interval** option, then set the Minimum, Maximum, Major Unit and Minor Unit options to **Fixed**. Specify the minimum value to **Jan 1, 2015** and the maximum value to **Jan 29, 2015**. Set the Major Unit and Minor Unit values to **1** and select the unit as **Weeks** and **Days** respectively which stand for 1 week and 1 day.

    ![Format Category (X) Axis - Tick Mark - Scale](https://devnet.logianalytics.com/hc/article_attachments/4404894001559/cmpnt_cht_intvl_tkmk3.gif)
12. In the Minor Label sub tab of the Format tab, select the format in the Stack box and select **Remove** to delete it. Select **Date/Time** from the Category box, input **d** in the Properties text box and select **Add** to add the format to the Stack box.
    Then select **OK** to apply the settings.

    ![Format Category (X) Axis - Format - Mionor Label](https://devnet.logianalytics.com/hc/article_attachments/4404889422999/cmpnt_cht_intvl_tkmk4.gif)
13. Double-click the line to bring out the Format Line dialog. In the Node tab, select **Use Single Color**, then select **true** from the Show Node drop-down list to show nodes on the line, and specify the node color to **#000000**. Select **OK** to accept the settings.

    ![Format Line dialo - Node](https://devnet.logianalytics.com/hc/article_attachments/4404894001815/cmpnt_cht_intvl_cht8.gif)
14. Resize the chart, save the report and select the **View** tab, then the report will be shown as follows:

    ![Line chart in Web Report](https://devnet.logianalytics.com/hc/article_attachments/4404889423255/cmpnt_cht_intvl_tkmk2.gif)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563122-Formatting-the-Legend)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583741-Editing-Range-Groups-on-Category-Values)
