---
title: "Creating Scrollable Charts"
id: 1500010063661
section: "Working with Components in Reports - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010063661-Creating-Scrollable-Charts
updated_at: 2021-07-24T10:39:23Z
---

# Creating Scrollable Charts

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010029022-Editing-Range-Groups-on-Category-Values) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010063641-Creating-Real-Time-Charts)

# Creating Scrollable Charts

In a scrollable chart, values displayed on the chart are not fixed. A scrollbar on the scrollable chart can help you to control the visible value range on the category (X) axis of the chart. This is often used where the category axis is a date or a time such as stock quotes; however, it can be used with any type of value. As shown below, any time the number of categories may become too large to be easily identified on the screen, consider adding a scrollable option.

Scrollable charts are supported on charts of the Bar, Bench, Line and Area types in web reports and library components only.

**To make a bar, bench, line or area chart scrollable:**

1. Right-click on any element of the chart and select **Scrollable Chart** from the shortcut menu to display the [Scrollable Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010067661-Scrollable-Chart-Dialog) dialog.

   ![Scrollable Chart dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901183767/scrlbcht.gif)
2. Check the **Enable Scrollable Chart** option to use a scrollbar to control the number of visible values on the category axis.
3. Specify how many data items will be selected on the scrollbar and displayed on the category axis by default in the Number of Visible Values box, then specify the percentage the scrollbar occupies the whole size of the chart.
4. Specify whether to show the thumbnail chart in the scrollbar.
5. Specify whether to recalculate the scale of the value (Y) axis when the the value of the option Number of Visible Values is changed.
6. Select **OK** to apply the settings for the chart.

## Example of creating a scrollable chart

1. Make sure SampleReports.cat is the currently open catalog file. If not select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Select **File** > **New** > **Web Report** to create a web report.
3. [Insert a chart in the web report](https://devnet.logianalytics.com/hc/en-us/articles/1500010063601-Inserting-Charts-in-a-Report#BV) as follows:

* Use WorldWideSalesBV in Data Source 1 of the catalog as the data source.
* Display in the Clustered Bar 2-D chart type.
* Show Sales Month on the category axis and Total Sales on the value axis.
* Apply the Classic style.

4. Save the report and select the **View** tab to preview the chart. The chart appears as follows:

   ![Initial Chart](https://devnet.logianalytics.com/hc/article_attachments/4404901331863/cmpnt_cht_scroll1.gif)
5. Select the **Design** tab to return to the design mode.
6. Right-click on any bar and select **Scrollable Chart** from the shortcut menu.
7. In the Scrollable Chart dialog, check**Enable Scrollable Chart,** set Number of Visible Values to **10** and Percentage of Scrolling Area Height to **10%**.
   Keep the other two options checked and select **OK** to apply the settings and leave the dialog.

   ![Define the Scrollable Chart](https://devnet.logianalytics.com/hc/article_attachments/4404901332119/cmpnt_cht_scroll2.gif)
8. Save the report and select **View** > **Preview As** > **Web Report Result**. The chart appears as follows in Web Report Studio:

   ![Preview Scrollable Chart in Web Report Studio](https://devnet.logianalytics.com/hc/article_attachments/4404901332375/cmpnt_cht_scroll3.gif)
9. From the report result above, we can see only 10 total sales values. To change the data items displayed on the X axis, drag the highlighted section on the scrollbar, or resize the width of the section by dragging its left or right edge.

   ![Scroll the Chart](https://devnet.logianalytics.com/hc/article_attachments/4404901332631/cmpnt_cht_scroll4.gif)
10. To go back to the initial state of the chart, select the arrow at the upper right corner of the chart paper.

**Note:** When you export a scrollable chart to any format, the scrolling function will not be available. In the exported results, only the values that are selected at the time when the report is exported will be displayed.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010029022-Editing-Range-Groups-on-Category-Values) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010063641-Creating-Real-Time-Charts)
