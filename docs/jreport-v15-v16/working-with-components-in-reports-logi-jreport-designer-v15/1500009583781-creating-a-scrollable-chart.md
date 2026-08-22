---
title: "Creating a Scrollable Chart"
id: 1500009583781
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009583781-Creating-a-Scrollable-Chart
updated_at: 2021-07-24T05:56:04Z
---

# Creating a Scrollable Chart

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583741-Editing-Range-Groups-on-Category-Values)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583761-Creating-a-Real-Time-Chart)

# Creating a Scrollable Chart

In a scrollable chart, values displayed on the chart are not fixed. A scrollbar on the scrollable chart can help you to control the visible value range on the X axis of the chart. This is often used where the X axis is a date or a time such as stock quotes; however, it can be used with any type of value. As shown below, any time the number of categories may become too large to be easily identified on the screen, consider adding a scrollable option.

Currently, scrollable charts are supported on charts of bar, bench, line, and area types in web reports and library components only.

**To make a chart of bar, bench, line, or area type scrollable:**

1. Right-click anywhere of the chart except the chart object and select **Scrollable Chart** from the shortcut menu to display the [Scrollable Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009588501-Scrollable-Chart-Dialog) dialog.

   ![Scrollable Chart dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893857559/scrlbcht.gif)
2. Check the **Enable Scrollable Chart** option to use a scrollbar to control the number of visible values on the axis.
3. Specify how many data items will be selected on the scrollbar and displayed on the axis by default in the Number of Visible Values box, then specify the percentage the scrollbar occupies the whole size of the chart.
4. Specify whether to show the thumbnail chart in the scrollbar.
5. Specify whether to recalculate the scale of Value (Y) Axis when the the value of the option Number of Visible Values is changed.
6. Select **OK** to apply the settings for the chart.

## Example of creating a scrollable chart

The following example shows how to create a scrollable chart:

1. [Open the catalog file](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog) SampleReports.cat in `<install_root>\Demo\Reports\SampleReports`.
2. [Create a web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Create).
3. [Insert a chart in the web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009563242-Inserting-a-Chart#Web) which is based on WorldWideSalesBV in Data Source 1, displays in the Clustered Bar 2-D chart type, shows City on X-Axis and Total Sales on Bar Length, and use Neutral as the report style.
4. Select the **View** tab to view this chart, and it appears as follows:

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889420183/cmpnt_cht_scroll1.gif)
5. Select the **Design** tab to return to the design mode.
6. Right-click anywhere of the chart except the chart object and select **Scrollable Chart** from the shortcut menu. The Scrollable Chart dialog appears.
7. Check the**Enable** **Scrollable Chart** option, then set the option Number of Visible Values to **10** and Percentage of Scrolling Area Height to **10%**. Then, select **OK** to apply the settings and leave the dialog.

   ![Scrollable Chart dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893996823/cmpnt_cht_scroll4.gif)
8. The option Auto Scale on Y Axis is checked by default, which means the scale of Value (Y) axis will be recalculated when the the value of the option Number of Visible Values is changed.
9. Save the report and select **View** > **Preview As** > **Web Report Result**, the report will show as follows in Web Report Studio:

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889420439/cmpnt_cht_scroll2.gif)
10. From the report result above, we can see only 10 total sales values from the city Almaty to Boston. To change the data items displayed on the X axis, drag the left or right handle or the area between the two handles on the scrollbar. See the result as follows:

    ![](https://devnet.logianalytics.com/hc/article_attachments/4404893997079/cmpnt_cht_scroll3.gif)

**Note:** When you export a scrollable chart to any format, the scrolling function will not be available. In the exported results, only the values that are selected at the time when the report is exported will be displayed.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583741-Editing-Range-Groups-on-Category-Values)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583761-Creating-a-Real-Time-Chart)
