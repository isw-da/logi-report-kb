---
title: "Track 2: Performing Visual Analysis "
id: 1500010093641
section: "Logi Report Tutorial v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010093641-Track-2-Performing-Visual-Analysis
updated_at: 2021-07-23T19:14:27Z
---

# Track 2: Performing Visual Analysis 

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856777623/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010056482-Track-1-Self-service-Dashboard-with-Logi-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404848352023/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010056422-Track-3-Creating-and-Analyzing-Ad-Hoc-Reports)

# Track 2: Performing Visual Analysis

Visual Analysis is an in-context analysis tool to visualize the result of every step of your work. Simply by dragging and dropping data fields onto a layout module, you are able to visually analyze data in either text or graphs. Business views are the data sources used in Visual Analysis.

This track contains the following tasks:

* [Task 1: Analyzing by Text](#Task1)
* [Task 2: Analyzing by Graphs](#Task2)

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4404856819991/criticalicon.gif) A Visual Analysis license is required in order to perform this track. If you do not have the license, please contact your Logi Analytics account manager to obtain one first.

## Task 1: Analyzing by Text

1. In the [Start Page](https://devnet.logianalytics.com/hc/en-us/articles/1500010093101-Lesson-1-Starting-Server) of the Server Console, select **Public Folder** in the **Open** category to open the folder.
2. In the Resources page of the Server Console, select **New** > **Analysis** on the task bar.

   ![New Visual Analysis](https://devnet.logianalytics.com/hc/article_attachments/4404857085591/va_new.gif)

   Server displays Visual Analysis in a new window and prompts the Select Data Source dialog box for you to select the data source that you want to use to perform the analysis. You can select a business view from all the public catalogs.

   ![Select Business View](https://devnet.logianalytics.com/hc/article_attachments/4404857085847/va_bv.gif)
3. Select **WorldWideSalesBV** in Data Source 1 of the SampleReports catalog and select **OK**.

   Visual Analysis lists the group ![Group button](https://devnet.logianalytics.com/hc/article_attachments/4404848711191/btn_grp.gif) and aggregation ![Aggregation button](https://devnet.logianalytics.com/hc/article_attachments/4404857086103/btn_agg.gif) fields in the selected business view in the Data Source panel on the left. You can drag them to the data presentation area on the right to perform analysis.

   ![Visual Analysis](https://devnet.logianalytics.com/hc/article_attachments/4404848711575/va_wndw.gif)
4. From the Data Source panel, drag the group field **Country** to the row control box for grouping ![Drop for Row button](https://devnet.logianalytics.com/hc/article_attachments/4404848711831/btn_drpaggrw1.gif) as the row header.

   ![Drag Group for Row](https://devnet.logianalytics.com/hc/article_attachments/4404857086487/va_addrow.gif)
5. Drag the group field **Category** to the column control box for grouping ![Drop for Column button](https://devnet.logianalytics.com/hc/article_attachments/4404848712343/btn_drpgrpclmn.gif) as the column header.

   ![Drag Group for Column](https://devnet.logianalytics.com/hc/article_attachments/4404857086743/va_addclmn.gif)
6. Drag the aggregation field **Total Sales** to the **Label** button ![Label button](https://devnet.logianalytics.com/hc/article_attachments/4404848712599/btn_label.gif) in the legend section. The report shows as follows. You can hover the mouse on any value to get the detailed information:

   ![Drag Aggregation to Label Button in Legend](https://devnet.logianalytics.com/hc/article_attachments/4404848712983/va_text.gif)

Next, we make use of the Filter panel to filter data in the report.

1. From the Data Source panel, drag **Region** to the **Filters** panel. Visual Analysis adds a filter based on this field in the Filters panel.

   ![Drag Field to Filters Panel](https://devnet.logianalytics.com/hc/article_attachments/4404857087127/va_fltrpnl.gif)
2. Clear **<All>** and then select **Asia-Pacific**. Visual Analysis refreshes the report to show the countries in Asia-Pacific only.

   ![Filter Data](https://devnet.logianalytics.com/hc/article_attachments/4404848713239/va_fltrst.gif)
3. Select the **Save** button ![Save button](https://devnet.logianalytics.com/hc/article_attachments/4404857087511/btn_sv.gif) on the toolbar. Visual Analysis displays the Save As dialog box.
4. Leave the save location be the My Reports folder, type **ProductSales** in the **File Name** text box, and select **OK**. Visual Analysis saves the current data state as an analysis template
   to the My Reports folder in the server resource tree.

## Task 2: Analyzing by Graphs

In this task, we start a new Visual Analysis session to analyze data by graphs.

1. Select the **Menu** button ![Resources button](https://devnet.logianalytics.com/hc/article_attachments/4404848713751/btn_menu.gif) and select **New** from the drop-down menu. Visual Analysis displays a new tab in your browser window.
2. In the Select Data Source dialog box, select **WorldWideSalesBV**, then select **OK**.
3. In the data presentation area, select the **Display Type** button ![Display Type button](https://devnet.logianalytics.com/hc/article_attachments/4404848714135/btn_txt.gif), then select **Bar**![Bar button](https://devnet.logianalytics.com/hc/article_attachments/4404857087767/btn_bar.gif) from the drop-down list.
4. From the Data Source panel, drag the aggregation field  **Total Sales** to the row control box used for aggregating ![Drop for Row button](https://devnet.logianalytics.com/hc/article_attachments/4404857088023/btn_drpaggrw.gif).

   ![Drag Aggregation to Row](https://devnet.logianalytics.com/hc/article_attachments/4404848714647/va_bar1.gif)
5. Drag the group field **Sales Year**  to the column control box used for grouping ![Drop for Column button](https://devnet.logianalytics.com/hc/article_attachments/4404848712343/btn_drpgrpclmn.gif).

   ![Drag Group to Column](https://devnet.logianalytics.com/hc/article_attachments/4404857088279/va_bar2.gif)
6. Drag **Category** to the right of Sales Year. When Visual Analysis displays an arrow, release the mouse (you can also make use of the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404848714903/btn_add.gif) beside a data control box to add a field from the resource list).

   ![Drag Field near Column Field](https://devnet.logianalytics.com/hc/article_attachments/4404857088535/va_bar3.gif)

   Visual Analysis displays the report as follows:

   ![Report Result](https://devnet.logianalytics.com/hc/article_attachments/4404857088791/va_bar4.gif)

We want to analyze data of the two sales years by quarter, so next we replace Sales Year with Sales Quarter.

1. From the Data Source panel, drag **Sales Quarter** over Sales Year. When Visual Analysis displays an arrow above Sales Year (in the center), release the mouse.

   ![Replace Field with Another Field](https://devnet.logianalytics.com/hc/article_attachments/4404857089047/va_bar5.gif)

   In the control box sections, you can also drag and drop a field to the right/left or top/bottom to change the display order of the field, or drag a field out of its control box to remove it.

Next, we try another important feature of Visual Analysis, analyzing with the legend.

1. Drag **Region** to the **Color** button ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4404857089303/btn_clr.gif) in the legend section. Visual Analysis marks data of each region by different color. You can select the Color button ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4404857089303/btn_clr.gif) to customize the colors if you want. Here we keep the default color pattern.

   ![Mark Field by Color](https://devnet.logianalytics.com/hc/article_attachments/4404848715287/va_bar6.gif)

Visual Analysis displays the report with a scrollbar which is not convenient for comparing data. We can change the fit setting to improve the layout.

1. Enlarge the browser window size a bit, then select **Fit Visible** from the drop-down list of **Normal View** on the toolbar. Visual Analysis now fully displays the report according to the current window size.

   ![Display Whole Chart](https://devnet.logianalytics.com/hc/article_attachments/4404857089559/va_bar7.gif)
2. Hover the mouse on different color sections on a bar and you can see related information.

   ![Color Section Tips](https://devnet.logianalytics.com/hc/article_attachments/4404857089943/va_bar8.gif)

Visual Analysis supports the Sort feature on the fields used for grouping the columns and rows. Next, we want to sort the sales quarters based on their total sales in descending order.

1. Right-click **Sales Quarter** and select **Sort** from the shortcut menu.

   ![Sort Field](https://devnet.logianalytics.com/hc/article_attachments/4404848715543/va_sort1.gif)
2. In the Sort dialog box, select **Descending**, select the **Sort Using Another Field** option and select **Total Sales** from the drop-down list. Select **OK**.

   ![Sort Using Another Field](https://devnet.logianalytics.com/hc/article_attachments/4404848715799/va_sort2.gif)

   The report now displays as follows:

   ![Sort Result](https://devnet.logianalytics.com/hc/article_attachments/4404857090327/va_sort3.gif)

Lastly, we change the data display type to Pie so that it is easy to find out which region sales the most.

1. Select the **Display Type** button ![Bar button](https://devnet.logianalytics.com/hc/article_attachments/4404857087767/btn_bar.gif) and then select **Pie**![Pie button](https://devnet.logianalytics.com/hc/article_attachments/4404848716055/btn_pie.gif) from the drop-down list.
2. Remove **Sales Quarter** and **Category** from the column control boxes by dragging them out of their positions.
3. Move **Total Sales** from the row control box to the **Slice** button ![Slice button](https://devnet.logianalytics.com/hc/article_attachments/4404848716567/btn_slice.gif) in the legend section. The report changes to below:

   ![Pie Chart](https://devnet.logianalytics.com/hc/article_attachments/4404848716823/va_pie.gif)

   We can see that North America occupies the largest amount of the total sales.
4. Select the **Save** button ![Save button](https://devnet.logianalytics.com/hc/article_attachments/4404857087511/btn_sv.gif) on the toolbar to save the data state as an analysis template into the server resource tree.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856777623/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010056482-Track-1-Self-service-Dashboard-with-Logi-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404848352023/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010056422-Track-3-Creating-and-Analyzing-Ad-Hoc-Reports)
