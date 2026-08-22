---
title: "Lesson 3: Creating and Performing Data Analysis on Page Reports"
id: 5735526578199
section: "Logi Report Tutorial v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735526578199-Lesson-3-Creating-and-Performing-Data-Analysis-on-Page-Reports
updated_at: 2022-11-29T03:39:09Z
---

# Lesson 3: Creating and Performing Data Analysis on Page Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898403124503/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735498124567-Lesson-2-Creating-a-Web-Report-Using-the-Wizard)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898403130775/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735511499671-Track-2-Self-Service-Dashboard-with-Logi-Report)

# Lesson 3: Creating and Performing Data Analysis on Page Reports

Using the Page Report Wizard, you can create a single component page report that you view in Page Report Studio. Page Report Studio provides the user a page mode view of the report very similar to a printed report.

The Page Report Wizard provides several report layouts to collect information for you: Blank (no component), Banded, Crosstab, Table, and Chart. You can add more components to a report after Page Report Studio generates it. In this lesson, we create a page report that contains three report tabs, and then perform data analysis on them one by one.

This lesson contains the following tasks:

* [Task 1: Create a Banded Report](#Task1)
* [Task 2: Create a Table Report](#Task2)
* [Task 3: Create a Crosstab Report](#Task3)
* [Task 4: Insert a Chart](#Task4)
* [Task 5: Analyze Data of the Banded Object](#Task5)
* [Task 6: Analyze Data of the Table](#Task6)
* [Task 7: Analyze Data of the Crosstab](#Task7)
* [Task 8: Analyze Data of the Chart](#Task8)

## Task 1: Create a Banded Report

1. In the [Start Page](https://devnet.logianalytics.com/hc/en-us/articles/5735563057559-Lesson-1-Starting-Server) of the Server Console, select **Page Report** in the **Create** category. Server displays a page.
2. Select the **SampleReports** folder and **SampleReports.cat** catalog file, then select **OK**.

   ![Select Catalog](https://devnet.logianalytics.com/hc/article_attachments/9898520501783/adhc_lsn3_tsk1_cat.gif)
3. In the New Page Report dialog box, type **Order Details** in the **Report Title** text box, select **Banded** in the layout box, then select **OK**.

   ![Select Banded for Page Report](https://devnet.logianalytics.com/hc/article_attachments/9898520506135/adhc_lsn3_tsk1_nwrptst.gif)
4. In the **Data** screen of the Banded Wizard dialog box, select **WorldWideSalesBV** in Data Source 1 from the **Available Data Resources** box.
   Select **Next**.
5. In the **Display** screen, expand the **Products** category in the **Resources** box, select **Product Name** and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898520508183/btn_add2.gif) to add it as a detail field to the right box, then expand the **Orders Detail** category and add **Quantity**, **Unit Price**, and **Total** one by one to the right box. Select **Next**.

   ![Add Banded Display Fields](https://devnet.logianalytics.com/hc/article_attachments/9898536706327/adhc_lsn3_tsk1_bddsply.gif)
6. In the **Group** screen, add **Country** in the **Customers** category as the group-by field, keep **Ascend** as the sort manner, and then select **Next**.
7. In the **Summary** screen, select the **Country** group in the right box, then add **Total Sales** to summarize the total sales for each country. Select **Next**.

   ![Add Banded Summary Field](https://devnet.logianalytics.com/hc/article_attachments/9898520520855/adhc_lsn3_tsk1_bdsum.gif)
8. Skip the **Dataset Filter** screen and select **Next**.
9. In the **Style** screen, set the style to **Classic**, then select **Finish** to create the report in Page Report Studio.

   ![Banded Report](https://devnet.logianalytics.com/hc/article_attachments/9898536730391/adhc_lsn3_tsk1_bdrpt.gif)
10. Navigate to **Menu** > **File** > **Rename Report Tab**.
11. In the Rename Report Tab dialog box, type **OrderDetails** as the report tab name and select **OK**.
12. Select **Save**![Save button](https://devnet.logianalytics.com/hc/article_attachments/9898520531223/btn_save.gif) on the toolbar.
13. In the Save As dialog box, type **CustomerOrders.cls** in the **File Name** text box, then select **OK** to save the report into the Public Reports > SampleReports folder in the server resource tree.

## Task 2: Create a Table Report

1. In the current open report window, select **New Report Tab** ![New Report Tab button](https://devnet.logianalytics.com/hc/article_attachments/9898536741399/btn_nwrpt.gif) on the toolbar.
2. In the New Report Tab dialog box, type **Customer Information** in the **Report Title** text box, select **Table (Group Above)**  in the layout box, then select **OK**.
3. In the **Data** screen of the Table Wizard dialog box, select **CoffeeSalesUSA** in Data Source 1, then select **Next**.
4. In the **Display** screen, select **Customer Name**, **Phone**, **Postal Code** , and **Address 1** in the **Resources** box and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898520508183/btn_add2.gif) to add them as the detail fields of the table one by one. Select **Next**.

   ![Add Table Display Fields](https://devnet.logianalytics.com/hc/article_attachments/9898536746263/adhc_lsn3_tsk2_tbldsply.gif)
5. Skip the **Group**, **Summary**, and **Dataset Filter** screens.
6. In the **Style** screen, set the style to **Classic**, then select **Finish** to create the table report.

   ![Table Report](https://devnet.logianalytics.com/hc/article_attachments/9898536759319/adhc_lsn3_tsk2_tblrpt.gif)
7. Navigate to **Menu** > **File** > **Rename Report Tab** to rename the report tab as **CustomerInfo**.
8. Select **Save**![Save button](https://devnet.logianalytics.com/hc/article_attachments/9898520531223/btn_save.gif) on the toolbar.
9. In the Save Report Template dialog box, select **Yes** to save the report.

## Task 3: Create a Crosstab Report

1. In the current open report window, select **New Report Tab**![New Report Tab button](https://devnet.logianalytics.com/hc/article_attachments/9898536741399/btn_nwrpt.gif) on the toolbar.
2. In the New Report Tab dialog box, type **Product Sales** in the **Report Title** text box, select **Crosstab** in the layout box, then select **OK**. Page Report Studio displays the Crosstab Wizard dialog box.
3. In the **Data** screen, select **WorldWideSalesBV** in Data Source 1 and then select **Next**.
4. In the **Display** screen, add **Country** as the row field and **Category** as the column field (keep **Ascend** as the sort manner for both columns and rows), add **Total Sales** as the summary field, then select **Next**.

   ![Add Crosstab Display Fields](https://devnet.logianalytics.com/hc/article_attachments/9898536763927/adhc_lsn3_tsk3_crstbdsply.gif)
5. Skip the **Dataset Filter** screen. Select **Next**.
6. In the **Style** screen, set the crosstab style to **Classic**, then select **Finish** to create the crosstab report.

   ![Crosstab Report](https://devnet.logianalytics.com/hc/article_attachments/9898520566807/adhc_lsn3_tsk3_crstbrpt.gif)
7. Navigate to **Menu** > **File** > **Rename Report Tab** to rename the report tab as **ProductSales**.
8. Select **Save**![Save button](https://devnet.logianalytics.com/hc/article_attachments/9898520531223/btn_save.gif) on the toolbar.
9. In the Save Report Template dialog box, select **Yes** to save the report.

## Task 4: Insert a Chart

In this task, we insert a chart below the crosstab that we created in Task 3.

1. Drag **Chart** from the **Toolbox** panel to place it under the last row of the crosstab.

   ![Insert Chart Below Crosstab](https://devnet.logianalytics.com/hc/article_attachments/9898536771095/adhc_lsn3_tsk4_drg.gif)
2. In the **Data** screen the Chart Wizard dialog box, select **WorldWideSalesBV** in Data Source 1, then select **Next**.
3. In the **Type** screen, keep the default chart type **Clustered Bar 2-D** and select **Next**.
4. In the **Display** screen, select **Sales Quarter** in the **Resources** box and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898520508183/btn_add2.gif) beside the **Category** box to add it as the category field of the chart, then add **Product Type** to the **Series** box and **Total Sales** to the **Show Values** box.

   ![Add Chart Display Fields](https://devnet.logianalytics.com/hc/article_attachments/9898536779159/adhc_lsn3_tsk4_chtdsply.gif)
5. Select **Finish** to create the chart.

   ![Chart Component](https://devnet.logianalytics.com/hc/article_attachments/9898536783639/adhc_lsn3_tsk4_chtrpt.gif)
6. Select **Save**![Save button](https://devnet.logianalytics.com/hc/article_attachments/9898520531223/btn_save.gif) on the toolbar.
7. In the Save Report Template dialog box, select **Yes** to save the report.

## Task 5: Analyze Data of the Banded Object

1. In the current report window, select **OrderDetails** from the **Go To** drop-down list on the toolbar to switch to this report tab.

   ![Switch to Banded Report Tab](https://devnet.logianalytics.com/hc/article_attachments/9898520593047/adhc_lsn3_tsk5_rptstbr.gif)

We want to make the orders in each country further grouped by order ID, so first we need to add another group into the banded object.

2. Close the **Toolbox** panel on the left.
3. Expand the **Orders Detail** category in the **Resource View** panel, drag **Order ID** below the **Australia** group header and release the mouse button when Page Report Studio displays a blue line and a tip "Group Header".

   ![Add Banded Group](https://devnet.logianalytics.com/hc/article_attachments/9898536799127/adhc_lsn3_tsk5_addgrp.gif)

Next, we want to add a column about the discount of each product.

1. Drag **Discount** from the Resource View panel to the detail panel of the banded object.

   ![Add Banded Detail](https://devnet.logianalytics.com/hc/article_attachments/9898536804503/adhc_lsn3_tsk5_adddtl.gif)

   The new group and detail column display in the banded object as follows:

   ![Banded with Newly Added Detail](https://devnet.logianalytics.com/hc/article_attachments/9898536810263/adhc_lsn3_tsk5_discnt.gif)

Now let's do some adjustments to improve the appearance of the banded object.

1. Right-click the **Discount** label in the banded header and select **Properties** from the shortcut menu. Page Report Studio displays the Label Properties dialog box.
2. In the **General** tab, edit the **Width** property to **1.04**, then select the **Font** tab and change **Horizontal Alignment** to **right**. Select **OK** to apply the property settings. The Discount label now aligns with the values in the same column.

   ![Edit Label Properties](https://devnet.logianalytics.com/hc/article_attachments/9898520638743/adhc_lsn3_tsk5_prpty.gif)

There are two group levels in the banded object, to easily distinguish them, we want to change the background color of the Order ID group.

1. Right-click any of the Order ID group header panel, the panel of 3033 for example, then select **Properties** on the shortcut menu.
2. In the **General** tab of the Banded Panel Properties dialog box, set the **Background** property to **#668cb2**, then select **OK** to confirm.

There is a blank panel before each new order ID begins. This is the group footer panel of the Order ID group. Since the panel does not contain any data, we can hide it.

1. Right-click any of the Order ID group footer panel, the blank footer of 3033 for example, then select **Hide** from the shortcut menu.

   ![Hide Category Group Footer](https://devnet.logianalytics.com/hc/article_attachments/9898536819223/adhc_lsn3_tsk5_grpftr.gif)

   After we made the appearance adjustments, the banded object looks as follows:

   ![Banded Without Category Group Footer](https://devnet.logianalytics.com/hc/article_attachments/9898520663703/adhc_lsn3_tsk5_frmt.gif)

Next, we want to sort and filter the banded object. We sort the totals in descending order for each group, and filter the records by discount to show orders in which the discount is 10 point only.

1. Select **Sort**![Sort button](https://devnet.logianalytics.com/hc/article_attachments/9898536826903/btn_sort.gif) on the toolbar.
2. In the Sort dialog box, choose **Total** from the field drop-down list, select the sorting manner as **Descend**, and then select **OK** to apply the settings.

   ![Sort Total Ascend](https://devnet.logianalytics.com/hc/article_attachments/9898520680983/adhc_lsn3_tsk5_srt.gif)
3. Right-click any value in the **Discount** column, then on the shortcut menu, navigate to **Filter** > **10.00**.

   ![Filter Discount](https://devnet.logianalytics.com/hc/article_attachments/9898520686743/adhc_lsn3_tsk5_fltr.gif)

   The banded object finally turns out as follows:

   ![Banded After Sort and Filter](https://devnet.logianalytics.com/hc/article_attachments/9898536844951/adhc_lsn3_tsk5_final.gif)
4. Select **Save**![Save button](https://devnet.logianalytics.com/hc/article_attachments/9898520531223/btn_save.gif) on the toolbar.
5. In the Save Report Template dialog box, select **Yes** to save the report.

In this task, we used two ways to sort and filter the report: one by dialog box and the other by right-click menu command. In fact, you can achieve both operations by either way.

## Task 6: Analyze Data of the Table

1. Select **CustomerInfo** from the **Go To** drop-down list on the toolbar to switch to this report tab.

First, we want to add more columns to the table. We can do this either by dragging fields from the Resource View panel or using dialog box.

1. In the **Resource View** panel, expand the **Customers** category, then drag **Customer ID** to the top left boundary of the **Customer Name** column and release the mouse button when Page Report Studio displays a vertical blue line on the left of Customer Name. Select **OK** in the prompt message to use the group object as a detail object.

   ![Drag to Add Detail Column](https://devnet.logianalytics.com/hc/article_attachments/9898536848407/adhc_lsn3_tsk6_drgclmn.gif)
2. Right-click any label in the table header, Customer ID for example, and navigate to **Insert** > **Group Column** on the shortcut menu.

   ![Insert Group Column](https://devnet.logianalytics.com/hc/article_attachments/9898536861335/adhc_lsn3_tsk6_instclmn.gif)
3. In the Insert Group Column dialog box, select **State** in the **Resources** box as the group-by field and add it to the right box, select the group position as **Group Above**, keep the default sort order, then select **OK** to insert the column.

   ![Define the Group](https://devnet.logianalytics.com/hc/article_attachments/9898536896663/adhc_lsn3_tsk6_slctgrp.gif)

   Page Report Studio now groups the table by state as follows:

   ![Add Group Result](https://devnet.logianalytics.com/hc/article_attachments/9898536908183/adhc_lsn3_tsk6_grprst.gif)

We consider the postal code information is not very useful. We want to replace the column with City.

1. Drag **City** from the **Resource View** panel to the **Postal Code** column label and release the mouse button when it covers the label.

   ![Replace Field with Another Field](https://devnet.logianalytics.com/hc/article_attachments/9898536912023/adhc_lsn3_tsk6_ovwrt.gif)

   The table changes to:

   ![Table with New Field](https://devnet.logianalytics.com/hc/article_attachments/9898520756503/adhc_lsn3_tsk6_city.gif)

Lastly, we want to make some adjustments to improve the table appearance. We resize the Address 1 columns to display values in the column entirely and hide the blank group footer.

1. Point to the right boundary of the **City** column header, when Page Report Studio displays a double headed arrow, drag the boundary to the left.

   ![Resize Column](https://devnet.logianalytics.com/hc/article_attachments/9898536925463/adhc_lsn3_tsk6_resz.gif)
2. Select in the blank group footer row. When Page Report Studio displays the icon ![Select button](https://devnet.logianalytics.com/hc/article_attachments/9898520763927/btn_crsarw.gif) at the top left of the table, right-click the icon, then navigate to **Show** > **Table Group Footer** on the shortcut menu.

   ![Hide Group Footer](https://devnet.logianalytics.com/hc/article_attachments/9898536931607/adhc_lsn3_tsk6_hdftr.gif)

   The table finally changes to:

   ![Table Report Result](https://devnet.logianalytics.com/hc/article_attachments/9898520777879/adhc_lsn3_tsk6_final.gif)
3. Select **Save**![Save button](https://devnet.logianalytics.com/hc/article_attachments/9898520531223/btn_save.gif) on the toolbar.
4. In the Save Report Template dialog box, select **Yes** to save the report.

## Task 7: Analyze Data of the Crosstab

In this task, we demonstrate the Drill feature of Page Report Studio based on the crosstab in the ProductSales report tab. Page Report Studio supports four types of drill actions: drill-up, drill-down, drill-to, and drill-to-by-value. You can apply them on crosstabs, charts, grouped tables, and banded objects. However, to perform the drill-up and drill-down actions on a data component, the business view that the component uses should contain predefined hierarchies, so that you are able to drill from one group level up or down to another within a hierarchy.

1. Select **ProductSales** from the **Go To** drop-down list on the toolbar to switch to the report tab, which contains a crosstab and a chart.

Since Country is a middle level predefined in the hierarchy Geography of WorldWideSalesBV, we can drill it up or down to the adjacent level.

1. Right-click any country in the row header, then navigate to **Drill Up** > **Region** on the shortcut menu.

   ![Drill up to Region](https://devnet.logianalytics.com/hc/article_attachments/9898536960023/adhc_lsn3_tsk7_drlup.gif)

   The crosstab refreshes to show as follows:

   ![Drill up to Region Result](https://devnet.logianalytics.com/hc/article_attachments/9898520788759/adhc_lsn3_tsk7_drluprst.gif)

Next, we want to drill down from Region to Country. However, it is not simply a reversed process of drilling up from Country to Region. When you drill down to a lower group level, Page Report Studio applies the currently selected value as a filter condition to show its data in the lower group level only. Therefore, after drill-down you cannot use drill-up to go back to the previous state, instead you can simply perform an Undo action.

1. Right-click **Asia-Pacific** in the row header and navigate to **Drill Down** > **Country** on the shortcut menu. The crosstab now displays only countries in the Asia-Pacific region in the row header.

   ![Drill down to Country](https://devnet.logianalytics.com/hc/article_attachments/9898536982679/adhc_lsn3_tsk7_drldw.gif)

We can further drill Country down to State and then to City in this way. Here let's leave the crosstab as it is and try the other two drill actions.

1. Right-click any product category in the column header, then navigate to **Drill To** > **Sales Year** on the shortcut menu.

   ![Drill To Menu List](https://devnet.logianalytics.com/hc/article_attachments/9898537005975/adhc_lsn3_tsk7_drlto.gif)

   The crosstab now shows sales in the Asia-Pacific countries in 2015 and 2016.

   ![Drill to Sales Year](https://devnet.logianalytics.com/hc/article_attachments/9898537009687/adhc_lsn3_tsk7_drltorst.gif)
2. Right-click **2016** in the column header and navigate to **Drill to by Value** > **Product Name** on the shortcut menu. The crosstab now shows each product's sales in the Asia-Pacific countries in 2016.

   ![Drill to by Value](https://devnet.logianalytics.com/hc/article_attachments/9898537015703/adhc_lsn3_tsk7_drltobyvl.gif)

Lastly, we want to rotate the crosstab, that is, to switch its column and row headers so that the crosstab is not split into two.

1. Select any aggregation cell in the crosstab to select the crosstab, then select **Rotate**![Rotate button](https://devnet.logianalytics.com/hc/article_attachments/9898520839191/btn_rotate.gif) on the toolbar.
2. Resize the crosstab row header by dragging its right boundary to the right to display values in the row header completely.

   ![Crosstab Final Result](https://devnet.logianalytics.com/hc/article_attachments/9898537028375/adhc_lsn3_tsk7_final.gif)
3. Select **Save**![Save button](https://devnet.logianalytics.com/hc/article_attachments/9898520531223/btn_save.gif) on the toolbar.
4. In the Save Report Template dialog box, select **Yes** to save the report.

## Task 8: Analyze Data of the Chart

In this task, we focus on the chart below the crosstab in the ProductSales report tab. Page Report Studio supports converting a chart to a crosstab, and vice versa. Let's convert the chart to a crosstab first.

1. Right-click on the chart and select **To Crosstab** from the shortcut menu. Page Report Studio displays the To Crosstab dialog box.
2. The **Resources** box in the **Display** tab lists the fields used in the crosstab. Add **Product Type** to the **Columns** box, **Sales Quarter** to the **Rows** box, and **Total Sales** to the **Summaries** box. Select **OK** to generate the crosstab.

   ![Convert Chart to Crosstab](https://devnet.logianalytics.com/hc/article_attachments/9898537036055/adhc_lsn3_tsk8_dsply.gif)

   Page Report Studio converts the chart to a crosstab.

   ![Converted Crosstab](https://devnet.logianalytics.com/hc/article_attachments/9898520850327/adhc_lsn3_tsk8_crstb.gif)

Next, we want to return the crosstab to chart to go on analyzing with chart. We want to change the chart type to line chart.

1. Select **Undo**![Undo button](https://devnet.logianalytics.com/hc/article_attachments/9898537045911/btn_undo.gif) on the toolbar to cancel the operation of converting chart to crosstab.
2. Right-click on the chart and navigate to **Chart Type** > **Line** > **Line 2-D** on the shortcut menu.

   ![Change Chart Type](https://devnet.logianalytics.com/hc/article_attachments/9898537057943/adhc_lsn3_tsk8_line.gif)

In Page Report Studio, you can change the definition of a chart at any time. Next, we want to use different type and fields to redefine the chart.

1. Right-click anywhere in the chart except the legend and select **Chart Wizard** on the shortcut menu. Page Report Studio displays the Chart Definition dialog box.
2. In the **Type** tab, select the **Bench** chart type, keep the default subtype **Clustered Bench 2-D**.
3. Select the **Display** tab, remove the fields in the **Category** and **Series** boxes respectively.
4. Select **Category** in the **Resources** box and select **Add** ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898520508183/btn_add2.gif) beside the **Category** box to add it as the category field of the chart, then add **RegionAbbr** to the **Series** box and **Total Quantity** to the **Show Values** box. Select **OK** to create the chart.

   ![Define the Bench Chart](https://devnet.logianalytics.com/hc/article_attachments/9898537063447/adhc_lsn3_tsk8_chtdfn.gif)

   The new bench chart displays as follows:

   ![Bench Chart](https://devnet.logianalytics.com/hc/article_attachments/9898537070487/adhc_lsn3_tsk8_bench.gif)

You can format properties of the elements in a chart, such as the platform, paper, legend, and axes using the corresponding format dialog boxes to suit your requirements. Next, we edit some properties of the tick marks on the Y axis to briefly introduce the Chart Format feature.

1. Right-click anywhere in the chart except the legend and navigate to **Format Axis** > **Format Value (Y) Axis** on the shortcut menu.
2. In the Format Value (Y) Axis dialog box, switch to the **Tick Mark** tab, in the **Major Tick Mark** subtab, select **Cross**, clear **Correlate with Axis** and type **#ff3333** in the **Color** text box, specify to show data labels every **2** tick marks. Select **OK** to apply the properties.

   ![Format Value Axis](https://devnet.logianalytics.com/hc/article_attachments/9898537072791/adhc_lsn3_tsk8_yfmt.gif)

   The tick marks and data labels on the Y axis apply the new properties.

   ![Final Chart](https://devnet.logianalytics.com/hc/article_attachments/9898537078039/adhc_lsn3_tsk8_final.gif)
3. Select **Save**![Save button](https://devnet.logianalytics.com/hc/article_attachments/9898520531223/btn_save.gif) on the toolbar.
4. In the Save Report Template dialog box, select **Yes** to save the report.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898403124503/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735498124567-Lesson-2-Creating-a-Web-Report-Using-the-Wizard)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898403130775/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735511499671-Track-2-Self-Service-Dashboard-with-Logi-Report)
