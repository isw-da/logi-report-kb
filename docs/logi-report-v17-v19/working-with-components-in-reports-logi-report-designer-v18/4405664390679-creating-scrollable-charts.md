---
title: "Creating Scrollable Charts"
id: 4405664390679
section: "Working with Components in Reports - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664390679-Creating-Scrollable-Charts
updated_at: 2022-01-27T20:34:28Z
---

# Creating Scrollable Charts

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661370647-Editing-Range-Groups-on-Category-Values)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661371799-Creating-Real-Time-Charts)

# Creating Scrollable Charts

In a scrollable chart, values displaying in the chart are not fixed. A scroll bar in the scrollable chart can help you control the visible value range on the category axis of the chart. This is often used where the category axis is a date or a time such as stock quotes; however, you can use it with any type of value. Any time the number of categories may become too large to be easily identified on the screen, consider adding a scrollable option. This topic shows how you can edit a chart to become a scrollable chart.

You can create scrollable charts from charts of the 2-D Bar, Bench, Line, and Area types in web reports and library components only.

**To make a bar, bench, line, or area chart scrollable**

1. Right-click any element of the chart and select **Scrollable Chart** from the shortcut menu. Designer displays the [Scrollable Chart dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664562327-Scrollable-Chart-Dialog-Box).

   ![Scrollable Chart dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420550982039/scrlbcht.gif)
2. Select **Enable Scrollable Chart** to use a scroll bar to control the number of visible values on the category axis.
3. Specify how many data items are selected on the scroll bar and display on the category axis by default in the **Number of Visible Values** box, then specify the percentage the scroll bar occupies the whole size of the chart.
4. Specify whether to show the thumbnail chart on the scroll bar.
5. Specify whether to recalculate the scale of the value (Y) axis when the value of the option Number of Visible Values is changed.
6. Select **OK** to apply the settings for the chart.

## Example of creating a scrollable chart

1. Make sure **SampleReports.cat** is the currently open catalog file. If not, navigate to **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Navigate to **File** > **New** > **Web Report** to create a web report.
3. [Insert a chart in the web report](https://devnet.logianalytics.com/hc/en-us/articles/4405664387479-Inserting-Charts-in-a-Report#BV) as follows:

* Use **WorldWideSalesBV** in Data Source 1 of the catalog.
* Display in the **Clustered Bar 2-D** chart type.
* Show **Sales Month** on the category axis and **Total Sales** on the value axis.
* Apply the **Classic** style.

4. Save the report and select the **View** tab to preview the chart.

   ![Initial Chart](https://devnet.logianalytics.com/hc/article_attachments/4420542202135/cmpnt_cht_scroll1.gif)
5. Select the **Design** tab to return to design mode.
6. Right-click on any bar and select **Scrollable Chart** from the shortcut menu.
7. In the Scrollable Chart dialog box, select **Enable Scrollable Chart,** set **Number of Visible Values** to **10** and **Percentage of Scrolling Area Height** to **10%**.
   Keep the other two options selected and select **OK** to apply the settings and close the dialog box.

   ![Define the Scrollable Chart](https://devnet.logianalytics.com/hc/article_attachments/4420542202391/cmpnt_cht_scroll2.gif)
8. Save the report.
9. Navigate to **View** > **Preview As** > **Web Report Result** to preview the report in Web Report Studio.

   ![Preview Scrollable Chart in Web Report Studio](https://devnet.logianalytics.com/hc/article_attachments/4420556246423/cmpnt_cht_scroll3.gif)
10. We can see only 10 total sales values on the chart. To change the data items displaying on the X axis, drag the highlighted section on the scroll bar, or resize the width of the section by dragging its left or right edge.

    ![Scroll the Chart](https://devnet.logianalytics.com/hc/article_attachments/4420542203159/cmpnt_cht_scroll4.gif)
11. To go back to the initial state of the chart, select the arrow at the upper right corner of the chart paper.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) When you export a scrollable chart to any format, the scrolling function is not available. In the output result, the chart only displays the values that are selected at the time when you export the report.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661370647-Editing-Range-Groups-on-Category-Values)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661371799-Creating-Real-Time-Charts)
