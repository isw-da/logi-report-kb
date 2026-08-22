---
title: "Lesson 2: Creating a Web Report Using Wizard"
id: 1500011463241
section: "Logi JReport Tutorial v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500011463241-Lesson-2-Creating-a-Web-Report-Using-Wizard
updated_at: 2021-07-24T10:39:37Z
---

# Lesson 2: Creating a Web Report Using Wizard

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)Previous Page](https://devnet.logianalytics.com/hc/en-us/articles/1500011463261-Lesson-1-Creating-a-Web-Report-the-Quick-Start-Way) [Next Page![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011463221-Lesson-3-Creating-and-Performing-Data-Analysis-on-Page-Reports)

# Lesson 2: Creating a Web Report Using Wizard

In this lesson, we will create a web report using the Web Report Wizard, which is using the traditional way of Web Report Studio. The report will contain these data components: a crosstab, a table, and a banded object. After the report is created, we will use the powerful analysis features of Web Report Studio to analyze data in each component.

This lesson contains the following tasks:

* [Task 1: Create a Web Report Using Wizard](#Task1)
* [Task 2: Work with the Crosstab](#Task2)
* [Task 3: Work with the Chart](#Task3)
* [Task 4: Work with the Table](#Task4)
* [Task 5: Work with the Banded Object](#Task5)
* [Task 6: Apply a Filter](#Task6)

## Task 1: Create a Web Report Using Wizard

1. In the [Logi JReport Server Start Page](https://devnet.logianalytics.com/hc/en-us/articles/1500011431562-Lesson-1-Starting-Logi-JReport-Server), select **My Profile** in the Manage category.
2. In the My Profile > Customize Server Preferences > General tab, select the **Yes** checkbox for **Use Wizard for Web Report Studio**. select **OK** to save the setting.
   Then in the prompt message box, select **OK**.
3. Select **Resources** on the system toolbar to switch to the page, then go to the **Public Reports** > **SampleReports** folder.
4. Select **New** > **Web Report** on the task bar.

   ![New Web Report](https://devnet.logianalytics.com/hc/article_attachments/4404909075991/adhc_lsn2_crt_new.gif)

   The Web Report Wizard appears.
5. In the Page screen of the wizard, the Blank template is selected by default. Input **Sales Performance** in the Label text box and then select **Next**.

   ![Select Report Template](https://devnet.logianalytics.com/hc/article_attachments/4404901057687/adhc_lsn2_crt_tmplt.gif)

   You can also select from the other two templates if you want, with which you can customize the company logo and company name.
6. In the Layout screen, select the **T-Style** layout. In the first row, select the **Select here to select component** link in the left cell and select **Crosstab** from the drop-down menu. Select **Table** for the right cell and **Banded Object** for the bottom row.

   ![Define Report Components](https://devnet.logianalytics.com/hc/article_attachments/4404909076247/adhc_lsn2_crt_layout.gif)
7. Select **Next** to go to the Bind Data screen to define data for the three components one by one. First define the crosstab: from the Data Source drop-down list, select **WorldWideSalesBV** in Data Source 1, add **Region** to the Columns box, **Sales Month** to the Rows box, and **Total Sales** to the Summaries box.

   ![Define Crosstab Fields](https://devnet.logianalytics.com/hc/article_attachments/4404909076503/adhc_lsn2_crt_crstb.gif)
8. Select **Next** to define the table: keep the business view in the Data Source text box unchanged to use the same data source as the crosstab, in the Details tab add these fields: **Product Name**, **Order Date**, and **Total**, then select the **Group** tab and add **Country** as the group-by field.

   ![Define Table Fields](https://devnet.logianalytics.com/hc/article_attachments/4404901057943/adhc_lsn2_crt_tbl.gif)
9. Select **Next** to define the banded object: keep the business view in the Data Source text box unchanged to use the same data source as the crosstab, in the Details tab add these fields: **Order ID**, **Product Name**, **Quantity**, **Unit Price** and **Total**, then select the **Group** tab and add **Country** as the group-by field.

   ![Define Table Fields](https://devnet.logianalytics.com/hc/article_attachments/4404901058199/adhc_lsn2_crt_bdobj.gif)
10. Select **Next** to display the Style screen and select **Logi JReportDemo** as the style.
11. Select **Run**. The report is opened in Web Report Studio.

    ![Run Report in Web Report Studio](https://devnet.logianalytics.com/hc/article_attachments/4404909076759/adhc_lsn2_crt_rpt.gif)
12. Select the **Save** button ![Save button](https://devnet.logianalytics.com/hc/article_attachments/4404901050647/btn_save.gif) on the toolbar.
13. In the Save As dialog, type **SalesPerformance.wls** in the File Name text field, then select **OK** to save the web report into the Public Reports > SampleReports folder in the server resource tree. select **OK** in the prompted message box.

## Task 2: Work with the Crosstab

Groups on the crosstab row and column headers can be easily changed using the Switch feature. We will change the row header to analyze data by quarter.

1. Right-click the row header and select **Switch Row**  > **Sales Quarter** from the shortcut menu.

   ![Switch Row](https://devnet.logianalytics.com/hc/article_attachments/4404909077015/adhc_lsn2_crstb_switch.gif)

   The row header now displays quarters:

   ![Switch Row Resulr](https://devnet.logianalytics.com/hc/article_attachments/4404901058455/adhc_lsn2_crstb_switchrst.gif)

Next we will use the Go feature to analyze data from different views. Let's try Go-to-by-Value first, which allows to go to another group based on the current value.

1. Right-click **2015-Q1** in the row header, select **Go to by Value** > **Category** from the shortcut menu. The crosstab refreshes to show the total sales of each product category in the first quarter of 2015 in different regions.

   ![Go to by Value](https://devnet.logianalytics.com/hc/article_attachments/4404901058711/adhc_lsn2_crstb_go.gif)

Next we will use Go-Up and Go-Down to drill data in higher and lower group levels. To use these two functions, you need to make sure the business view used to create the report has predefined hierarchies, so that you are able to go up and down between the group levels in the hierarchies.

1. Right-click on the row header and select **Go Up** > **Product Type** from the shortcut menu.

   ![Go Up](https://devnet.logianalytics.com/hc/article_attachments/4404901058967/adhc_lsn2_crstb_goup.gif)

   The crosstab changes to：

   ![Go Up Result](https://devnet.logianalytics.com/hc/article_attachments/4404909077271/adhc_lsn2_crstb_gouprst.gif)

Now we will go down from Product Type to Category, however it is not simply a reversed process of going up from Category to Product Type. When you go down to a lower group level, Logi JReport will apply the currently selected value as a filter condition to show its data in the lower group level only.

1. Right-click **Regular** and select **Go Down** > **Category** from the shortcut menu. The crosstab refreshes to show the total sales of the regular categories in the first quarter of 2015 in different regions.

   ![Go Down Result](https://devnet.logianalytics.com/hc/article_attachments/4404901059223/adhc_lsn2_crstb_godwrst.gif)

Crosstab can be converted to chart and vice versa. Next we will use chart to display the data in the current crosstab.

1. Right-click the blank cell in the intersection of the crosstab row and column headers, then select **To Chart** from the shortcut menu.

   ![Convert Crosstab to Chart](https://devnet.logianalytics.com/hc/article_attachments/4404901059479/adhc_lsn2_crstb_2cht.gif)
2. In the To Chart dialog, the data fields used in the crosstab are listed. We will define the chart based on these fields. Keep the default chart type as Clustered Bar 2-D, add **Total Sales** to the Bar Length box, **Category** to the X-Axis box and **Region** to the Clustering box as follows:

   ![Define the Chart](https://devnet.logianalytics.com/hc/article_attachments/4404909077527/adhc_lsn2_crstb_2chtdlg.gif)
3. Select **OK** to generate the chart. Then drag the chart bottom border to enlarge its height. The total sales of the regular categories in the first quarter of 2015 in different regions now displays in the chart as follows:

   ![Converted Chart](https://devnet.logianalytics.com/hc/article_attachments/4404909077783/adhc_lsn2_crstb_2chtrst.gif)
4. Select ![Save button](https://devnet.logianalytics.com/hc/article_attachments/4404901050647/btn_save.gif) on the toolbar to save the report.

## Task 3: Work with the Chart

We will continue to perform on the chart that is converted from the crosstab in the previous task. First we want to exchange the fields on the category and series axes.

1. Select the **Swap Chart Groups** button ![Swap Chart Groups button](https://devnet.logianalytics.com/hc/article_attachments/4404901059863/btn_swap.gif) on the toolbar. The chart changes as follows:

   ![Swap Chart Groups](https://devnet.logianalytics.com/hc/article_attachments/4404901060119/adhc_lsn2_cht_swap.gif)

Next we will change the chart type to analyze data in line chart.

1. Select the **Chart Type** button ![Chart Type button](https://devnet.logianalytics.com/hc/article_attachments/4404901060375/btn_chttype.gif) on the toolbar, then from the drop-down menu select **Line** > **Line 2-D**.

   ![Chart Type List](https://devnet.logianalytics.com/hc/article_attachments/4404909078039/adhc_lsn2_cht_type.gif)

   From the line trend we can easily figure out the change of the category total sales across the regions. You can put the mouse pointer on any line node to get the detailed data it represents in the chart.

   ![Chart Value Tip](https://devnet.logianalytics.com/hc/article_attachments/4404901060631/adhc_lsn2_cht_tip.gif)

A summary in a report can be linked to a specific detail table. Now we will use this feature to view the detailed information of each chart value.

1. Right-click the highest node and select **Go to Detail** from the shortcut menu.

   ![Go to Detail](https://devnet.logianalytics.com/hc/article_attachments/4404909078295/adhc_lsn2_cht_go2dtl.gif)

   The detail table of the Bold category's total sales in Europe, Middle East, Africa shows as follows:

   ![Detail Table](https://devnet.logianalytics.com/hc/article_attachments/4404909078551/adhc_lsn2_cht_go2dtlrst1.gif)

The default detail table contains all the group and detail fields in the same business view category as the aggregate field from which the summary of a report is created. In our case, the default detail table does not satisfy our requirements, so next we will edit the detail table manually.

1. Select the Back button ![Back button](https://devnet.logianalytics.com/hc/article_attachments/4404901061015/btn_back.gif) on the toolbar to return to the main report.
2. Right-click any node in the line chart and select **Edit Detail Table** from the shortcut menu.
3. In the Resources box of the Edit Detail Table dialog, all the group and detail fields in the business view used by the chart are listed. Add these fields to the right box to display in the detail table one by one: **Customer Name**, **Discount**, **Quantity**, **Unit Price** and **Total**. Select **OK** to finish editing the detail table.

   ![Edit Detail Table Fields](https://devnet.logianalytics.com/hc/article_attachments/4404909078807/adhc_lsn2_cht_edtdtltbl.gif)
4. Right-click the highest node again and select **Go to Detail** from the shortcut menu. The detail table now shows as follows:

   ![Customized Detail Table](https://devnet.logianalytics.com/hc/article_attachments/4404901061271/adhc_lsn2_cht_go2dtlrst2.gif)
5. Select ![Back button](https://devnet.logianalytics.com/hc/article_attachments/4404901061015/btn_back.gif) on the toolbar to return to the main report.
6. Select ![Save button](https://devnet.logianalytics.com/hc/article_attachments/4404901050647/btn_save.gif) on the toolbar to save the report.

## Task 4: Work with the Table

We want to add some fields into the table to get more order information. We will add a detail column to show order quantity and add another group to group the table by sales year first and then country.

1. Select the table. Then from the Resources panel on the left, drag **Quantity** to the right border of the Order Date column and release the mouse when an orange line appears.

   ![Add Quantity Column](https://devnet.logianalytics.com/hc/article_attachments/4404909079063/adhc_lsn2_tbl_addclmn.gif)

   The table now displays as follows:

   ![New Table](https://devnet.logianalytics.com/hc/article_attachments/4404909079319/adhc_lsn2_tbl_addrst.gif)

Next we want to sort the table by the order dates in descending order.

1. Put the mouse pointer over the **Order Date** column header, the sort icon appears.

   ![Sort Order Date](https://devnet.logianalytics.com/hc/article_attachments/4404901061527/adhc_lsn2_tbl_srt.gif)
2. Select the down arrow to sort the dates in descending order.

   ![Sort Result](https://devnet.logianalytics.com/hc/article_attachments/4404901061783/adhc_lsn2_tbl_srtrst.gif)

Now we will summarize the order total in each group.

1. Right-click any value in the Total column, then select **Aggregate On** from the shortcut menu.
2. In the Aggregate On dialog, set the function to **Sum** and select **OK**.

   We can see the order total in each country is added in the group header.

   ![Summarize Order Total for Groups](https://devnet.logianalytics.com/hc/article_attachments/4404901062039/adhc_lsn2_tbl_sumrst.gif)

   This operation also creates a dynamic aggregation which is given a default name Sum\_Total. You can find it in the Dynamic Resources > Aggregations list in the Resources panel and you can use it again in the report.

Lastly we will use the Conditional Format feature to highlight the orders the quantity of which are equal to and larger than 1500.

1. Right-click any value in the Quantity column and select **Conditional Formatting** from the shortcut menu.
2. In the Conditional Formatting dialog, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901062295/btn_add1.gif) above the Condition box.
3. In the Edit Conditions dialog, select **Current Field** from the field drop-down list, **>=** from the operator drop-down list, then in the value text box input **1500**. Select **OK** to finish editing the condition and return to the Conditional Formatting dialog.
4. Select the color image ahead of the Background Color text box and select the yellow color **#FFCC00** from the color palette. Select **OK** to apply the conditional format setting.

   ![Edit Conditional Format](https://devnet.logianalytics.com/hc/article_attachments/4404901062551/adhc_lsn2_tbl_cdtnlfmt.gif)

   The table refreshes to display as follows:

   ![Conditional Format Result](https://devnet.logianalytics.com/hc/article_attachments/4404901062807/adhc_lsn2_tbl_cdtnlfmtrst.gif)
5. From the Resources panel on the left, drag **Sales Year** above the Australia group, release the mouse when an orange line appears.

   ![Add Sales Year Group](https://devnet.logianalytics.com/hc/article_attachments/4404909079575/adhc_lsn2_tbl_addgrp.gif)

   The table refreshes as follows:

   ![Add Sales Year Group Result](https://devnet.logianalytics.com/hc/article_attachments/4404909079831/adhc_lsn2_tbl_addgrprst.gif)
6. Select ![Save button](https://devnet.logianalytics.com/hc/article_attachments/4404901050647/btn_save.gif) on the toolbar to save the report.

## Task 5: Work with the Banded Object

We will add a detail column to show product cost, add one more group to group the banded object by region first and then country, and add a chart in the region group. We can make use of the banded object template editor to do these things.

1. Select in the banded object. Then select the **Edit Template** button ![Edit Template button](https://devnet.logianalytics.com/hc/article_attachments/4404901063063/btn_edttmplt.gif) on the visualization toolbar to access the template editor.

   ![Template editor](https://devnet.logianalytics.com/hc/article_attachments/4404901063319/adhc_lsn2_bndobj_tmpltedtr.gif)
2. Drag the detail object **Cost** from the Resources panel to the detail panel on the right of the Total column in the banded object.

   ![Add Detail Object](https://devnet.logianalytics.com/hc/article_attachments/4404909080087/adhc_lsn2_bndobj_adddtl.gif)

   The result is shown as follows:

   ![Add Detail Object Result](https://devnet.logianalytics.com/hc/article_attachments/4404909080343/adhc_lsn2_bndobj_adddtlrst.gif)
3. Drag **Region** from the Resources panel to GH in the template editor until an orange line appears above GH and then release the mouse.

   ![Add group field](https://devnet.logianalytics.com/hc/article_attachments/4404909080599/adhc_lsn2_bndobj_drgfld.gif)

   The Region group will be added above the Country group:

   ![Added group field result](https://devnet.logianalytics.com/hc/article_attachments/4404901063575/adhc_lsn2_bndobj_drgfldrst.gif)

We will insert a chart in the Region group header. The chart will inherit data from the banded object and be filtered by the region value.

1. Drag the **Bar Chart** icon ![Bar Chart icon](https://devnet.logianalytics.com/hc/article_attachments/4404901063831/btn_barcht.gif) from the visualization toolbar to the GH panel of the Region group.

   ![Insert Chart](https://devnet.logianalytics.com/hc/article_attachments/4404909080855/adhc_lsn2_bndobj_instbarcht.gif)
2. In the Insert Chart dialog, add **Total Sales** to the Bar Length box and **Category** to the X-Axis box.

   ![Define Chart Fields](https://devnet.logianalytics.com/hc/article_attachments/4404901064087/adhc_lsn2_bndobj_chtdlg.gif)
3. Select **OK** to insert the chart. We will resize the chart smaller. Select in the chart to select it, then drag the bottom right corner of the chart
   to resize. Move the chart to the required position by dragging and dropping if required.

   ![Resize Chart](https://devnet.logianalytics.com/hc/article_attachments/4404901064343/adhc_lsn2_bndobj_rszcht.gif)
4. Select the GH panel which contains the chart to select the panel. Drag the bottom border of the panel to be closer to the chart.

   ![Resize GH Panel](https://devnet.logianalytics.com/hc/article_attachments/4404901064599/adhc_lsn2_bndobj_rszpnl.gif)
5. Select the **Return** button ![Return Button](https://devnet.logianalytics.com/hc/article_attachments/4404901064855/btn_rtn.gif) on the visualization toolbar to exit the template editor.
   The banded object looks as follows:

   ![Banded Object Result](https://devnet.logianalytics.com/hc/article_attachments/4404909081111/adhc_lsn2_bndobj_rst.gif)
6. We will switch from the Region group to Sales Year to see how the chart responds to the change of the group value. right-click **Asia-Pacific**
   and select **Switch Group** > **Sales Year** from the shortcut menu.

   ![Switch Group](https://devnet.logianalytics.com/hc/article_attachments/4404901065367/adhc_lsn2_bndobj_swtchgrp.gif)

   The banded object is now shown as follows:

   ![Switch Group Result](https://devnet.logianalytics.com/hc/article_attachments/4404901065623/adhc_lsn2_bndobj_swtchgrprst.gif)

## Task 6: Apply a Filter

In Web Report Studio, you can apply a filter to each data component in a report individually or use the Filter panel and filter controls to filter multiple data components at a time. For the usage of filter controls, you can learn from [Creating Web Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500011463421-Track-3-Creating-Web-Reports) in the Advanced Part. Here we focus on using the Filter panel to filter report data.

1. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901062295/btn_add1.gif)on the title bar of the Filter panel on the left. The Select Field dialog appears.
2. Check **Country**  and **Region**, keep the default Apply To setting, then select **OK**.

   ![Select Fields for Filter](https://devnet.logianalytics.com/hc/article_attachments/4404909081367/adhc_lsn2_fltr_slctfld.gif)

   A filter box which contains all values of the selected fields is added in the Filter panel, titled by the name of the first selected field in the Select Fields dialog.

   ![Filter Panel](https://devnet.logianalytics.com/hc/article_attachments/4404909081623/adhc_lsn2_fltr_pnl1.gif)
3. Select **North America**  in the value list. The report comes out as follows:

   ![North America Result](https://devnet.logianalytics.com/hc/article_attachments/4404901065879/adhc_lsn2_fltr_rst1.gif)

   At the meantime, Logi JReport processes values in the filter box to put the countries in the selected region on the top of the value list. You can select a country in the region or another other value to go on filtering the report.

   ![Filter Panel](https://devnet.logianalytics.com/hc/article_attachments/4404901066135/adhc_lsn2_fltr_pnl2.gif)
4. Select **Mexico**. The report is filtered to show the following data:

   ![Mexico Result](https://devnet.logianalytics.com/hc/article_attachments/4404901066391/adhc_lsn2_fltr_rst2.gif)
5. Select the **Clear** button in the Filter panel to remove all filters applied to the report via the panel.
6. Select ![Save button](https://devnet.logianalytics.com/hc/article_attachments/4404901050647/btn_save.gif) on the toolbar to save the report.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)Previous Page](https://devnet.logianalytics.com/hc/en-us/articles/1500011463261-Lesson-1-Creating-a-Web-Report-the-Quick-Start-Way) [Next Page![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011463221-Lesson-3-Creating-and-Performing-Data-Analysis-on-Page-Reports)
