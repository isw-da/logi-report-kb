---
title: "Lesson 2: Creating a Web Report Using Wizard"
id: 1500009593461
section: "Logi JReport Tutorial v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009593461-Lesson-2-Creating-a-Web-Report-Using-Wizard
updated_at: 2021-07-24T05:53:39Z
---

# Lesson 2: Creating a Web Report Using Wizard

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404893760791/back.png)Previous Page](https://devnet.logianalytics.com/hc/en-us/articles/1500009593441-Lesson-1-Creating-a-Web-Report-the-Quick-Start-Way) [Next Page![Next](https://devnet.logianalytics.com/hc/article_attachments/4404893761047/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009571362-Lesson-3-Creating-and-Performing-Data-Analysis-on-Page-Reports)

# Lesson 2: Creating a Web Report Using Wizard

In this lesson, we will create a web report using the Web Report Wizard, that is using the standard way of Web Report Studio. The report will contain a table, a crosstab, and a chart.

This lesson contains the following tasks:

* [Task 1: Create a Web Report Using the Wizard](#Task1)
* [Task 2: Operate on the Crosstab](#Task2)
* [Task 3: Perform on the Chart](#Task3)
* [Task 4: Work with the Table](#Task4)
* [Task 5: Apply a Filter](#Task5)

## Task 1: Create a Web Report Using the Wizard

1. On the [Logi JReport Server Start Page](https://devnet.logianalytics.com/hc/en-us/articles/1500009582241-Lesson-1-Starting-Logi-JReport-Server), select **Profile** in the Manage category.
2. In the Profile > Customize Server Preferences > General tab, select the **Yes** checkbox for Use Wizard for Web Report Studio. Select **OK** to save the setting.
   Then in the prompt message box, select **OK**.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889264791/adhc_lsn2_profile.gif)
3. Select **Resources** on the system toolbar to switch to the page, then go to the **Public Reports** > **SampleReports** folder.
4. Select **New** > **Web Report** on the task bar.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889265047/adhc_lsn2_clklnk.gif)
5. The Web Report Wizard appears. In the Page screen of the wizard, select **Template2**, which allows for company logo, company name, and report titles to be defined and added in the report's page header panel. We will keep the current company logo and titles, and just change the report titles. In the Report Title text field, input **Sales Performance**. Leave the Sub Title text field blank. Then select **Next**.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893781271/adhc_lsn2_tmplt.gif)
6. In the Layout screen, select the **T-Style** layout. In the first tabular row, select the **Click here to select component** link in the left cell, select **Crosstab** from the drop-down menu, select **Chart** for the right cell. For the bottom cell, select **Table** from the drop-down menu.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893781527/adhc_lsn2_layout.gif)
7. Select **Next** to go to the Bind Data screen to define data for the three components one by one. We will make the three components use the same business view. From the Data Source drop-down list, select **WorldWideSalesBV** in Data Source 1.
8. First define the crosstab. Add **Region** to the Columns box, **Sales Month** to the Rows box, and **Total Sales** to the Summaries box.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889265303/adhc_lsn2_wzdcrstb.gif)
9. Select **Next** to define the chart.
   The default chart type is Clustered Bar 2-D, you can change it by selecting another type from the drop-down list.
   Here we use the default type.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893781783/adhc_lsn2_wzdchtty.gif)

   Add **Total Sales** to the Bar Length box and **Country** to the X-Axis box.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889265687/adhc_lsn2_wzdcht.gif)
10. Select **Next** to define the table. In the Details tab, add these fields: **Customer Name**, **Product Name**, **Order Date**, and **Total**. In the Group tab, add **Country** as the group by field.

    ![](https://devnet.logianalytics.com/hc/article_attachments/4404889266071/adhc_lsn2_wzdtbl.gif)
11. Select **Next** to display the Style screen and select **Neutral** as the style.
12. Select **Run** and the report is opened in Web Report Studio.

    ![](https://devnet.logianalytics.com/hc/article_attachments/4404889266455/adhc_lsn2_rpt.gif)
13. Select the **Save** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404893772055/btn_save.gif) on the toolbar.
14. In the Save As dialog, type **SalesPerformance.wls** in the File Name text field, then select **OK** to save the web report. In the prompt message box, select **OK**.

## Task 2: Operate on the Crosstab

1. First we want to change the style of the crosstab. Place the cursor in the crosstab, when the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404893777303/btn_crsarw.gif) appears at its upper top left, right-click the icon, then select **Apply Style** > **JReportDemo** from the shortcut menu.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889266839/adhc_lsn2_chgsty.gif)
2. We will change the data view from Sales Month to Sales Quarter in the row headers. Right-click the row header which displays months, select **Switch Row**  > **Sales Quarter** from the shortcut menu. The row header now displays quarters.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893782039/adhc_lsn2_crstb.gif)
3. To further view information about the product category in the first quarter of 2015, right-click **2015-Q1** in the row header, select **Go to by Value** > **Category** from the shortcut menu. The crosstab now shows the total sales of the product categories in the first quarter of 2015 in different regions.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893782295/adhc_lsn2_ordrid.gif)
4. The row and column headers can be switched. Select the **Rotate Crosstab** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404889263511/btn_rotate.gif) on the toolbar.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893782551/adhc_lsn2_crstbrtt.gif)
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889263767/btn_undo.gif) on the toolbar to undo the rotation.

A crosstab can be converted to a chart and vice versa. Next we want to convert the crosstab to a chart to view and analyze data from different aspects with different focuses.

1. Place the cursor in the crosstab, when the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404893777303/btn_crsarw.gif) appears at its upper top left, right-click the icon, then select **To Chart** from the shortcut menu.
2. In the To Chart dialog, the data fields used in the crosstab are listed. We need to define our chart based on these fields. Clustered Bar 2-D is the default chart type. Add the data fields as follows:

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889267223/adhc_lsn2_tocht.gif)
3. Select **OK**. Here is the chart:

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893782935/adhc_lsn2_tochtrst.gif)
4. To switch the category and the series values, select the **Swap Chart Groups** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404889267479/btn_swap.gif) on the toolbar. Resize the chart and it displays as follows:

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889267735/adhc_lsn2_swp.gif)
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893772055/btn_save.gif) on the toolbar to save the report.

## Task 3: Perform on the Chart

1. Point to any bar in the chart and a tip shows up. From the tip we can easily get the data information each bar stands for.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893783191/adhc_lsn2_chttip.gif)

   We want to link the chart values to a table which contains detailed information about the values.
2. Right-click on a bar, select **Edit Detail Table** from the shortcut menu.
3. In the Edit Detail Table dialog, add these fields to the right panel concerning the total sales in the countries: **Country**, **Product Name**, **Quantity**, **Unit Price**, **Discount**, and **Total**, then select **OK**.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893783447/adhc_lsn2_edtdtltbl.gif)

   Now we can view the details about the chart values.
4. Right-click on the highest bar which represents USA and select **Go to Detail** on the shortcut menu. The following table is displayed showing information about USA.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889267991/adhc_lsn2_dtltbl.gif)
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889268247/btn_back.gif) on the toolbar to return to the main report.

Since the business view has a defined hierarchy, we can go through data upward and downward directly.

1. Right-click any country name on the X axis and select **Go Up** > **Region**. The chart now displays as follows:

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893783703/adhc_lsn2_goup.gif)

   Next we want to go down from Region to Country, however it is not a reversed process of going up from Country to Region, but applying an additional filter.
2. Right-click **Asia-Pacific** on the X axis and select **Go Down**  > **Country**.
   The chart shows the countries in the Asia-Pacific instead of all the countries.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889268503/adhc_lsn2_godown.gif)
3. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893772055/btn_save.gif) on the toolbar to save the report.

## Task 4: Work with the Table

1. We first sort the table based on the Total column in descending order. Right-click any value in the Total column and then select **Sort** > **Descend** from the shortcut menu.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889268759/adhc_lsn2_tblsrt.gif)

   Next, we want to summarize the total sales for each country group.
2. Right-click any value in the Total column, then select **Aggregate On** from the shortcut menu.
3. In the Aggregate On dialog, set the function to **Sum**, then select **OK**. We can see the total sales for each country group is added in the group header.

   The sum of total for Australia:

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889269015/adhc_lsn2_tbl.gif)

   This operation also creates a dynamic aggregation which is given a default name Sum\_Total. You can find it in the Dynamic Resource > Aggregations list in the Resources panel and you can use it again in the report.

   Now we want to make the table linked with another report.
4. Right-click on any Product Name value and select **Link** from the shortcut menu.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893783959/adhc_lsn2_lnkmn.gif)
5. In the Insert Link dialog, select **Browse** to select **Link.wls** in the SampleReports folder. Select **OK**.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889269655/adhc_lsn2_slctlnkrpt.gif)
6. Select the **More** button to show more settings.
7. In the Filter tab, select  ![](https://devnet.logianalytics.com/hc/article_attachments/4404893784215/btn_addcom.gif) above the Components box. In the Choose Component dialog, select **Bar Chart** in the linked report as the link target and select **OK**.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889269911/adhc_lsn2_lnkcmp.gif)
8. Repeat the above step to add TableComp to the Components box.
9. Select **Bar Chart** in the Components box, select the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404893784215/btn_addcom.gif) above the Field Conditions box to add a condition row, then select the **Product Name** field from the Fields (Primary) and Fields (Linked) drop-down lists to set up the filter condition between the table and the target chart based on the field.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893784471/adhc_lsn2_lnkdlg.gif)
10. Select **TableComp** in the Components box, check **Pass on-screen filters to the linked components** and select  **OK** to apply the settings.

    ![](https://devnet.logianalytics.com/hc/article_attachments/4404893784727/adhc_lsn2_lnkdlg1.gif)
11. Select **View Mode** from the mode drop-down menu on the toolbar.
12. Select **Mexico Organic** in the Product Name column of the table, or right-click **Mexico Organic** and select **Show Linked Target** from its shortcut menu. The link.wls report is displayed with the chart filtered to show only data about Mexico Organic.

    ![](https://devnet.logianalytics.com/hc/article_attachments/4404893784983/adhc_lsn2_lnkrpt.gif)

    The following is the original link.wls for comparison:

    ![](https://devnet.logianalytics.com/hc/article_attachments/4404889270423/adhc_lsn2_lnkrptorg.gif)
13. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889268247/btn_back.gif) on the toolbar to return to the primary report.
14. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893772055/btn_save.gif) on the toolbar to save the report.

## Task 5: Apply a Filter

The three data components in the report use the same business view, therefore we can apply filters to them at the same time. Even if they used different business views, as long as they had the same field values from different business views you can still filter all components with a single filter. We can use the Filter panel and filter controls to filter report data and the filters created via the two are referred to as on-screen filters. For the usage of filter controls, you can learn from [Creating Web Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009562062-Track-3-Creating-Web-Reports) in the Advanced Part. Here we focus on using the Filter panel to dynamically filter report data. When we define the linked report in Task 4, we have enabled the on-screen filters to be passed from primary report to the table component in the linked report, so the filter condition specified via the Filter panel in the primary report will be applied in the linked report when we trigger the link.

We would like to filter data with product names, so we need to add the Product Name field to the Filter panel.

1. Switch Web Report Studio to Edit Mode.
2. Select **+** on the title bar of the Filter panel on the left, then in the Select Field dialog, select **Product Name**  and select **OK**. The Product Name field is now added in the Filter panel with its values.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889270679/adhc_lsn2_fltrpnl.gif)
3. Select **Mexico Organic** in the Product Name box. The report comes out as follows:

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889270935/adhc_lsn2_fltrrpt.gif)
4. Switch to View Mode. Select **Mexico Organic** in the Product Name column of the table to open the linked report.

   This time the table in the linked report is also filtered to show only data about Mexico Organic as the on-screen filter defined in the Filter panel of the primary report is passed to it.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893785239/adhc_lsn2_psfltr.gif)
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889268247/btn_back.gif) on the toolbar to return to the primary report.
6. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893772055/btn_save.gif) on the toolbar to save the report.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404893760791/back.png)Previous Page](https://devnet.logianalytics.com/hc/en-us/articles/1500009593441-Lesson-1-Creating-a-Web-Report-the-Quick-Start-Way) [Next Page![Next](https://devnet.logianalytics.com/hc/article_attachments/4404893761047/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009571362-Lesson-3-Creating-and-Performing-Data-Analysis-on-Page-Reports)
