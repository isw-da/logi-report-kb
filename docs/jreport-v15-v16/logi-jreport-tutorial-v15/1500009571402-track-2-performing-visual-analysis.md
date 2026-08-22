---
title: "Track 2: Performing Visual Analysis"
id: 1500009571402
section: "Logi JReport Tutorial v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009571402-Track-2-Performing-Visual-Analysis
updated_at: 2021-07-24T05:53:39Z
---

# Track 2: Performing Visual Analysis

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404893760791/back.png)Previous Page](https://devnet.logianalytics.com/hc/en-us/articles/1500009571382-Track-1-Self-service-Dashboard-with-Logi-JReport) [Next Page![Next](https://devnet.logianalytics.com/hc/article_attachments/4404893761047/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009593421-Track-3-Creating-and-Analyzing-Ad-Hoc-Reports)

# Track 2: Performing Visual Analysis

Visual Analysis is a WYSIWYG product to visualize the result of every step of your work. Simply by dragging and dropping data fields onto a layout module, you are able to visually create crosstabs and charts step by step.

Business views are the data sources used in Visual Analysis.

* [Task 1: Select a Business View](#Task1)
* [Task 2: Adding Data Fields](#Task2)
* [Task 3: Saving the Template](#Task3)
* [Task 4: Filtering the Data](#Task4)

**Note:** A Visual Analysis license is required in order to perform this track. If you do not have the license, please contact your Jinfonet Software account manager to obtain one first.

## Task 1: Select a Business View

1. On the [Logi JReport Server Start Page](https://devnet.logianalytics.com/hc/en-us/articles/1500009582241-Lesson-1-Starting-Logi-JReport-Server), select **Analysis** in the Create category.
2. The Select Data Source dialog lists all catalogs in the current folder and the business views in the catalogs. Go to **Public Reports** > **SampleReport.cat** > **Data Source 1** and select **WorldWideSalesBV**, then select **OK**.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889249687/va_bv.gif)
3. The Visual Analysis window will be displayed.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893761303/va_wndw.gif)

## Task 2: Adding Data Fields

This section demonstrates how to drag data fields to the data presentation area and how to use the legend buttons.

1. In the Visual Analysis, select the **Display Type** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404893761559/btn_txt.gif) and then select Bar ![](https://devnet.logianalytics.com/hc/article_attachments/4404889249943/btn_bar.gif) from the drop-down list.
2. Drag **Total Sales** from the resources panel on the left to the row control box ![](https://devnet.logianalytics.com/hc/article_attachments/4404893762327/btn_drpaggrw.gif). The Total Sales field is used to draw the axis in the row header.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893762583/va_bar1.gif)
3. Drag **Category** to the column control box ![](https://devnet.logianalytics.com/hc/article_attachments/4404893762839/btn_drpgrpclmn.gif) as the column header.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889250199/va_bar2.gif)
4. Drag Sales Year right to Category: when an arrow appears on the right, drop the field.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889250455/va_bar3.gif)

   You can also make use of the ![](https://devnet.logianalytics.com/hc/article_attachments/4404889250711/btn_add.gif) button to add a field from its drop-down resource list.
5. To replace Sales Year with Sales Quarter, drag Sales Quarter over Sales Year. An arrow will appear above Sales Year (in the center), then drop Sales Quarter.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893763223/va_bar4.gif)
6. To Remove Category, right-click on it and select **Delete** from the drop-down menu.
   Or you can simply drag the
   Category label out of its position to remove it.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893763479/va_bar5.gif)
7. To mark different regions by color, drag **Region** to the Color button ![](https://devnet.logianalytics.com/hc/article_attachments/4404893763735/btn_clr.gif) in the legend section.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893763991/va_bar6.gif)
8. We will sort sales quarters.
   Right-click **Sales Quarter** and select **Sort**.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893764247/va_bar7.gif)
9. In the Sort dialog,
   check the **Sort Using Another Field** option, and then select **Total Sales** from the drop-down list.
   Select **OK**.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893764503/va_bar8.gif)
10. Here is the sort result.

    ![](https://devnet.logianalytics.com/hc/article_attachments/4404893764759/va_bar9.gif)
11. Hover the cursor on a bar and you will see related information.

    ![](https://devnet.logianalytics.com/hc/article_attachments/4404889251223/va_bar10.gif)
12. Drag Sales Month after Sales Quarter.

    ![](https://devnet.logianalytics.com/hc/article_attachments/4404889251479/va_bar11.gif)
13. The scrollbar shows and we cannot see the whole chart. Widen the presentation area and select **Fit Visible** from the drop-down list of
    Normal View on the toolbar so that the bar is fully displayed according to the current space.

    ![](https://devnet.logianalytics.com/hc/article_attachments/4404889251735/va_bar12.gif)
14. Next we will use the Pie type to demonstrate the slice-by feature. Since a pie does not need as much space as the above bar, we will change Fit Visible back to Normal View on the toolbar.
15. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889249943/btn_bar.gif) and then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893765015/btn_pie.gif) from the drop-down list. Then remove Sales Quarter and Sales Month from the column header by dragging them out of their positions.
16. Move Total Sales from the row header to be the slice-by field by moving it to the ![](https://devnet.logianalytics.com/hc/article_attachments/4404889252119/btn_slice.gif) button in the legend section on the right. Slice-by decides the angle for the total sales in each region.

    ![](https://devnet.logianalytics.com/hc/article_attachments/4404889252375/va_pie.gif)

## Task 3: Saving the Template

The current data state can be saved as a template. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893765271/btn_sv.gif) on the toolbar. In the Save As dialog, leave the save location be the My Reports folder, type in **ProductSales** in the File Name text box, and select **OK**. Next time we will be able to open the template in the My Reports folder in the server resource tree.

## Task 4: Filtering the data

We will use the Text display type to show the filter feature.

1. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893765527/btn_menu.gif) and then select **New** from the drop-down menu to start a new Visual Analysis session.
2. In the Select Data Source dialog, select **WorldWideSalesBV** and select **OK**.
3. From the resources panel, drag **Country** to the row header ![](https://devnet.logianalytics.com/hc/article_attachments/4404889252631/btn_drpaggrw1.gif), **Category** to the column header ![](https://devnet.logianalytics.com/hc/article_attachments/4404893762839/btn_drpgrpclmn.gif), and **Total Sales** to the ![](https://devnet.logianalytics.com/hc/article_attachments/4404889253015/btn_label.gif) button in the legend section.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889253271/va_text.gif)
4. From the resources panel drag **Region** to the Filters panel below. By default all the values are selected.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889253527/va_fltrpnl.gif)
5. To view the data in Asia-Pacific, uncheck **<All>** and then select **Asia-Pacific**. The data will be refreshed to show the countries in Asia-Pacific.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893765783/va_fltrst.gif)
6. Save the template as **Sales-text** in the My Reports folder.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404893760791/back.png)Previous Page](https://devnet.logianalytics.com/hc/en-us/articles/1500009571382-Track-1-Self-service-Dashboard-with-Logi-JReport) [Next Page![Next](https://devnet.logianalytics.com/hc/article_attachments/4404893761047/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009593421-Track-3-Creating-and-Analyzing-Ad-Hoc-Reports)
