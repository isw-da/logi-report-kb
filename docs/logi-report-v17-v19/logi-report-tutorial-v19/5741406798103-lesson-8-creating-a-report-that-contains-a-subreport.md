---
title: "Lesson 8: Creating a Report That Contains a Subreport"
id: 5741406798103
section: "Logi Report Tutorial v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741406798103-Lesson-8-Creating-a-Report-That-Contains-a-Subreport
updated_at: 2022-11-30T02:36:32Z
---

# Lesson 8: Creating a Report That Contains a Subreport

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905613813911/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741393465495-Lesson-7-Creating-a-Tabular-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905613870871/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741393493399-Lesson-9-Creating-a-Parameter-Based-Report)

# Lesson 8: Creating a Report That Contains a Subreport

This lesson shows a report combined with another report. In Logi Report, when you add report A into report B, the report A is referred to as a subreport, while report B is considered as a primary report.

In this lesson, we need to create a report that contains a subreport to show the order detail information, the related customers, and employees information. We first create a page report that contains two report tabs - one is about orders detail information, and the other is a tabular report with two charts of different types. We take the first report tab in the page report as the primary report and the second one as the subreport, then we insert the second report tab to the first one to show the sales total by orders in different order ID groups.

Follow these tasks to create the report:

* [Task 1: Create a Page Report with Two Report Tabs](#Task1)
* [Task 2: Insert a Subreport to the Report](#Task2)

## Task 1: Create a Page Report with Two Report Tabs

Before taking this task, make sure you have enabled the "Insert field name label with field" option in the Options dialog box as [described at the last step of Lesson 3](https://devnet.logianalytics.com/hc/en-us/articles/5741384902295-Lesson-3-Creating-a-Mailing-Label-Report#Options); otherwise, Designer does not insert the name labels together with the fields when you add fields to the report.

1. In Designer, navigate to **File** > **New** > **Page Report**.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) Be sure that JinfonetGourmetJava.cat is the current catalog because this is the catalog we use in this track. For information about specifying this catalog, see [Task 1, Steps 3 and 4](https://devnet.logianalytics.com/hc/en-us/articles/5741398712727-Lesson-1-Creating-a-Standard-Banded-Report#SelectCat) of Lesson 1.
2. In the Select Component for Page Report dialog box, select **Banded** and select **OK**.
3. In the **Data** screen of the Banded Wizard dialog box, expand the **Imported SQLs** node in Data Source 1 and select **OrdersReport**.

   ![Select Data](https://devnet.logianalytics.com/hc/article_attachments/9905863231639/rpt_lsn8_slctsql.gif)
4. Select **Style** on the screen navigation bar to switch to the screen and select the **Simple** style for the report.
5. Select **Finish** to create a report with a blank standard banded object.

   Designer identifies the panels in the banded object on the left by their abbreviations: a banded header panel (BH), a banded page header panel (BPH), a detail panel (DT), a banded page footer panel (BPF), and a banded footer panel (BF).

   ![Banded Panels](https://devnet.logianalytics.com/hc/article_attachments/9905875031447/rpt_lsn8_bndrpt.gif)

If you would like to write your own SQL statement, you can edit it using the Imported SQL Editor dialog box or import the SQL statement from a file. SQLs can work like queries in Designer.

In this lesson, we need to group data by Order IDs, so next we add a group to the banded object.

1. Right-click the banded object and select **Banded Wizard** from the shortcut menu.
2. In the **Group** screen of the Banded Wizard dialog box, select the DBField **Orders\_OrderID** in the **Resources** box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905875055127/btn_addarw.gif) to add it as the group-by field. Select **Finish**.

   ![Add Group](https://devnet.logianalytics.com/hc/article_attachments/9905875086231/rpt_lsn8_fmtgrp.gif)
3. Resize the GH panel of the banded object, drag the fields **Customer\_Name**, **Orders\_OrderDate**, **Contact\_LastName**, and **Orders\_PaymentReceived** from the **Data** panel to the panel.
4. Select the **Customer\_Name**, **Orders\_OrderDate**, **Contact\_LastName**, and **Orders\_PaymentReceived** name labels, set their **Auto Map Field Name** property to **false** in the Report Inspector, then double-click and edit the name labels to **Customer Name**, **Order Date**,  **Employee Last Name**, and **Payment Received** one by one.
5. Align the newly-added objects and resize them in the GH panel as follows:

   ![Add Fields to Banded Object](https://devnet.logianalytics.com/hc/article_attachments/9905863325207/rpt_lsn8_algn.gif)
6. Resize the group-by field in the GH panel, navigate to **Insert** > **Label** to add a label ahead of it and edit its text to "**Order ID:**".

   ![Add Label](https://devnet.logianalytics.com/hc/article_attachments/9905863358359/rpt_lsn8_id.gif)
7. Select the **Order Date** DBField and set its **Format** property to **M/d/yyyy** in the Report Inspector.
8. Select the BPH panel, navigate to **Insert** > **Label** to add a label in it and edit its text to **Order Details**. The label then displays in every page as the report title.
9. Hide the BH, DT, GF, BPF, and BF panels one by one by right-clicking the panel and selecting **Hide** from the shortcut menu.
10. Format labels and DBFields in the report to improve their appearance. Here, we do not describe the formatting process in detail. You can refer to [Task 3 of Lesson 1](https://devnet.logianalytics.com/hc/en-us/articles/5741398712727-Lesson-1-Creating-a-Standard-Banded-Report#Task3) for assistance.

    ![Main Report](https://devnet.logianalytics.com/hc/article_attachments/9905863415319/rpt_lsn8_frstrpt.gif)

    The report tab displays somewhat as follows in view mode:

    ![Preview the Main Report](https://devnet.logianalytics.com/hc/article_attachments/9905863431831/rpt_lsn8_view.gif)
11. On the report tab bar, right-click the report tab and select **Rename** to rename it to **OrderDetailInformation**.

    ![Rename Report Tab](https://devnet.logianalytics.com/hc/article_attachments/9905863488151/renmrpttb.gif)

By now, we have finished creating the first report tab in the report that shows the order detail information. Next, we create the second report tab, which is a tabular report containing two charts.

1. Navigate to **File** > **New** > **Page Report Tab**.
2. In the Select Component for Page Report Tab dialog box, select **Tabular** from the layout box, then select **OK**.
3. In the Tabular Wizard dialog box, keep the default settings and select **Finish**. Designer creates a report tab with a blank 2\*2 tabular.
4. Merge the tabular cells into two rows by selecting two cells in a row, right-clicking on them, and then selecting **Merge** from the shortcut menu
5. Adjust the two tabular rows to place the bar chart and pie chart vertically in the report tab.

Next, we will insert the two charts into the tabular cells and have them [share the same dataset](https://devnet.logianalytics.com/hc/en-us/articles/5741393465495-Lesson-7-Creating-a-Tabular-Report#Dataset) as the OrdersDetailInformation report tab.

1. Select the first tabular cell and navigate to **Insert** > **Chart**. Designer displays the Create Chart dialog box.
2. In the **Data** screen, select **More Options**, select **Existing Dataset**, then select the dataset **OrdersReport**. Select **Next**.
3. In the **Type** screen, keep the default chart type **Clustered Bar 2-D** and select **Next**.
4. In the **Display** screen, select the summary **Sum\_SQLProductSalesbyOrderID** and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905875055127/btn_addarw.gif) beside the **Bar Length** box, Designer then adds **Orders\_OrderID** automatically to the **X-Axis** box.
5. Select **Style** on the screen navigation bar to switch to the screen and select the **Basic** style.
6. Select **Finish** to create the chart.
7. When a box attached to your mouse pointer, select the tabular cell to place the chart there.

   ![Insert Chart](https://devnet.logianalytics.com/hc/article_attachments/9905863548183/rpt_lsn8_box.gif)
8. Select the second tabular cell and insert a clustered pie chart in it, which uses the same dataset, displays the same data, and applies the same style as the bar chart.
9. Double-click any bar of the chart.
10. In the Formar Bar dialog box, switch to the **Fill** tab and select **Vary Colors by Color List** to fill each bar with a different color schema, then select **OK** to apply the setting and close the dialog box.

    ![Add Label to Chart](https://devnet.logianalytics.com/hc/article_attachments/9905863569815/rpt_lsn8_varyclr.gif)
11. Right-click the bar chart and select **Add Label** from the shortcut menu. Designer then adds a label to the chart.

    ![Add Label to Chart](https://devnet.logianalytics.com/hc/article_attachments/9905875349911/rpt_lsn8_addlbl.gif)
12. Move the label to the top of the chart, then double-click it to display the Format Label dialog box.
13. In the **General** tab, change the label text to **Current Orders for This Customer**.
14. Switch to the **Font** tab, change **Font Size** to **12pt**, **Font Color** to **808080** and select **OK**.

    ![Format Label](https://devnet.logianalytics.com/hc/article_attachments/9905875383575/rpt_lsn8_fmtlbl.gif)
15. Resize the label to make sure the text can display completely.
16. Add a label to the pie chart and format it using the same way and edit its text to **Current Orders for This Employee**.
17. In the Report Inspector, select the **Chart Object** and **Chart Object 1** nodes in the report structure tree, then change the **Border Type** property to **none**.

    ![Edit Border Type](https://devnet.logianalytics.com/hc/article_attachments/9905863815447/rpt_lsn8_border.gif)
18. Select the **Chart Legend Object** and **Chart Legend Object 1** nodes and change the **Border Type** property to **none** as well.
19. Further format the two charts to improve their appearance if desired. For more information about formatting chart, see [Task 2 of Lesson 4](https://devnet.logianalytics.com/hc/en-us/articles/5741406737431-Lesson-4-Creating-a-Chart-Report#Task2).

    By now, we finished creating the second report tab in the report to show the sales total by orders.

    ![Subreport](https://devnet.logianalytics.com/hc/article_attachments/9905863840151/rpt_lsn8_scdrpt.gif)
20. On the report tab bar, right-click the report tab containing the charts to rename it to **Sub\_OrderDetails**.
21. Navigate to **File** > **Save** to save the report as **OrdersReport.cls**.

## Task 2: Insert a Subreport to the Report

After creating the report, we can insert the subreport to the primary report by specifying relationships between them. In this lesson, we can specify different relationships between the primary report (the first one) and the two chart components in the second report tab by setting up different links between them. Designer then builds a subreport for every order with the conditions, so that it is convenient to see the corresponding customer and employee information of every order.

We want this subreport to be at the end of the existing reports, thus we need to add a second group header and add the subreport to the new header.

1. Select **OrderDetailInformation** on the report tab bar to switch to the report tab.

   ![Report Tab Bar](https://devnet.logianalytics.com/hc/article_attachments/9905863861399/rpt_lsn8_bar.gif)
2. Right-click in the GH panel of the banded object and choose **Insert Panel After** from the shortcut menu.
3. Select the newly-added panel and navigate to **Insert** > **Subreport**.
4. When a box attached to your mouse pointer, select the newly-added panel to place the subreport into it. Designer displays the Subreport dialog box.
5. Select **Browse**, select **OrdersReport.cls** and then select **Open**.
6. Select **Sub\_OrderDetails** from the **Report Tab** drop-down list.
7. In the **Field** tab, select **Add** beside the **Component in Report Tab** box, then in the Choose Component dialog box, select **Chart Object** and select **OK**.

   ![Add Component from Subreport](https://devnet.logianalytics.com/hc/article_attachments/9905863901207/rpt_lsn8_subrpt.gif)
8. Select **Orders\_CustomerID** in the resource box on the right box and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905875055127/btn_addarw.gif) to build the relationship between the primary report and the selected chart object on the field.  

   ![Edit Subreport Relationship](https://devnet.logianalytics.com/hc/article_attachments/9905897483671/rpt_lsn8_rltnshp.gif)
9. Select **Add** again. This time, select **Chart Object 1** in the Choose Component dialog box and select **OK**.
10. Build the relationship between the primary report and the second chart object on the **Orders\_EmployeeID** field.
11. Select **OK** in the Subreport dialog box. Designer inserts the report tab in the OrderDetails report tab.

    ![Insert Subreport](https://devnet.logianalytics.com/hc/article_attachments/9905875738007/rpt_lsn8_instsub.gif)

Next, we filter the dataset used by the two report tabs in the report to enhance the performance when running the report.

1. Navigate to **Report** > **Manage Datasets**. Designer displays the Manage Datasets dialog box.

   The Manage Datasets dialog box lists all datasets the current report applies. In our report, all data components share the same dataset, so here we see only one dataset.
2. Select the **Filter** tab, select **Add Condition** to add a filter line, select **ORDERS\_ORDERID** from the field drop-down list, **<=** from the operator drop-down list, and type **3050** in the value text box to specify the filter condition as "ORDERS\_ORDERID <= 3050". Select **OK** to apply the filter.

   ![Filter Dataset](https://devnet.logianalytics.com/hc/article_attachments/9905897553047/rpt_lsn8_fltr.gif)
3. Navigate to **File** > **Save** to save the report.
4. Select the **View** tab. Designer displays the report tab that contains a subreport as follows: the primary report shows the orders detail information grouped by order ID, and the subreport shows the orders information by different customers and different employees respectively in the two charts.

   ![Preview Report](https://devnet.logianalytics.com/hc/article_attachments/9905875783063/rpt_lsn8_rpt.gif)

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) If the report does not look correct, you can compare it to the final version of the report included in Designer. To do this, save and close your current catalog, and then open the **JinfonetGourmetJava.cat** catalog file in `<install_root>\Demo\Reports\TutorialReports`.

As you learned in this lesson, it is very convenient to build up a library of reports that act as components which you can add to various primary reports. Properly designed and used, subreports save a lot of time and effort in rapidly adapting your applications to changing user requirements and needs.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905613813911/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741393465495-Lesson-7-Creating-a-Tabular-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905613870871/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741393493399-Lesson-9-Creating-a-Parameter-Based-Report)
