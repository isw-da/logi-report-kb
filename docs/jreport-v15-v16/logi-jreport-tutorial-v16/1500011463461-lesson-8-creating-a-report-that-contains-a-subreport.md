---
title: "Lesson 8: Creating a Report That Contains a Subreport"
id: 1500011463461
section: "Logi JReport Tutorial v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500011463461-Lesson-8-Creating-a-Report-That-Contains-a-Subreport
updated_at: 2021-07-24T10:39:39Z
---

# Lesson 8: Creating a Report That Contains a Subreport

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500011431362-Lesson-7-Creating-a-Tabular-Report) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011463441-Lesson-9-Creating-a-Parameter-Based-Report)

# Lesson 8: Creating a Report That Contains a Subreport

Here we need to create a report that contains a subreport to show the order detail information, the related customers and employees information.

This lesson shows a report combined with another report. When adding report A into report B, the report A is referred to as a subreport, while report B is considered as a primary report. We will first create a page report that contains two report tabs - one is about orders detail information, and the other is about a tabular report with two charts of different types.

In this lesson, we take the first report tab in the page report as the primary report, and the second one as the subreport. So that we can insert the second report tab to the first one to show the sales total by orders in different order ID groups.

Follow the tasks below to finish creating the report:

* [Task 1: Create a Page Report with Two Report Tabs](#Task1)
* [Task 2: Insert a Subreport to the Report](#Task2)

## Task 1: Create a Page Report with Two Report Tabs

Before taking this task, make sure you have enabled the Insert field name label with field option in the Options dialog as [described at the last step of Lesson 3](https://devnet.logianalytics.com/hc/en-us/articles/1500011431422-Lesson-3-Creating-a-Mailing-Label-Report#Options). Otherwise, the name labels will not be inserted together with the fields when you add fields to the report.

1. In Logi JReport Designer select **File** > **New** > **Page Report**.
2. In the Select Component for Page Report dialog, select **Banded** and select **OK**.
3. Be sure that JinfonetGourmetJava.cat is specified as the current catalog because this is the catalog we use in this track. For information about specifying this catalog, see [Task 1, Step 2 and 3](https://devnet.logianalytics.com/hc/en-us/articles/1500011431462-Lesson-1-Creating-a-Standard-Banded-Report#SelectCat) of Lesson 1.
4. In the Data screen of the Banded Wizard, expand the **Imported SQLs** node in Data Source 1 and select **OrdersReport**.

   ![Select Data](https://devnet.logianalytics.com/hc/article_attachments/4404901074839/rpt_lsn8_slctsql.gif)
5. Select **Style** to switch to the screen and select the **Simple** style for the report, then select **Finish**.

   A report with a blank standard banded object is created as follows. The panels in the banded object are identified on the left by their abbreviations: a banded header panel (BH), a banded page header panel (BPH), a detail panel (DT), a banded page footer panel (BPF) and a banded footer panel (BF).

   ![Banded Panels](https://devnet.logianalytics.com/hc/article_attachments/4404901075095/rpt_lsn8_bndrpt.gif)

For users who wish to write their own SQL statement, Logi JReport Enables them to put the SQL statement into a file and then load them from this file. SQL files can work like queries in Logi JReport.

In this lesson, we need to group data by Order IDs, so we will add a group to the banded object.

1. Right-click the banded object and then select **Banded Wizard**  from the shortcut menu.
2. In the Group screen of the Banded Wizard, add the DBField **Orders\_OrderID** as the group-by field by selecting it and selecting ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901075351/btn_addarw.gif), then select **Finish**.

   ![Add Group](https://devnet.logianalytics.com/hc/article_attachments/4404909087767/rpt_lsn8_fmtgrp.gif)
3. Resize the GH panel of the banded object, drag the fields **Customer\_Name**, **Orders\_OrderDate**, **Contact\_LastName** and **Orders\_PaymentReceived** from the Data panel and drop them into it.
4. For the Customer\_Name, Orders\_OrderDate, Contact\_LastName and Orders\_PaymentReceived name labels, set their **Auto Map Field Name** property to **false** in the Text Format category of the Report Inspector. Then double-click and edit the name labels to **Customer Name, Order Date, Employee Last Name** and **Payment Received** one by one.
5. Align the newly-added objects and resize them in the GH panel as follows:

   ![Add Fields to Banded Object](https://devnet.logianalytics.com/hc/article_attachments/4404901075607/rpt_lsn8_algn.gif)
6. Resize the group-by field in the GH panel, select **Insert** > **Label** to add a label ahead of it and edit its text to "**Order ID:**".

   ![Add Label](https://devnet.logianalytics.com/hc/article_attachments/4404901075863/rpt_lsn8_id.gif)
7. Select the **Order Date** DBField and set its Format property to **M/d/yyyy** in the Report Inspector.
8. Select the BPH panel, select **Insert** > **Label** to add a label in it and edit its text to **Order Details**. The label will then be shown in every page as the report title.
9. Hide the BH, DT, GF, BPF and BF panels one by one by right-clicking the panel and selecting **Hide** from the shortcut menu.
10. Format labels and DBFields in the report to improve their appearance. Here, we will not describe the formatting process in detail, you can refer to [Task 3 of Lesson 1](https://devnet.logianalytics.com/hc/en-us/articles/1500011431462-Lesson-1-Creating-a-Standard-Banded-Report#Task3) for assistance.

    Then the first report tab in the report is created to show the order detail information as follows in design mode:

    ![Main Report](https://devnet.logianalytics.com/hc/article_attachments/4404901076119/rpt_lsn8_frstrpt.gif)

    And the report looks as follows in view mode:

    ![Preview the Main Report](https://devnet.logianalytics.com/hc/article_attachments/4404901076375/rpt_lsn8_view.gif)
11. On the report tab bar, right-click the report tab and select **Rename** to rename it to **OrderDetailInformation**.

    ![Rename Report Tab](https://devnet.logianalytics.com/hc/article_attachments/4404901076631/renmrpttb.gif)

Next, we will create the second report tab in the report.

1. Select **File** > **New** > **Page Report Tab**.
2. In the Select Component for Page Report Tab dialog, select **Tabular** from the layout box, then select **OK**.
3. In the Tabular Wizard, keep the default settings and select **Finish**. A report tab with a blank 2\*2 tabular is created.
4. Merge the tabular cells into two rows by selecting two cells in a row while holding the Ctrl key on the keyboard, right-clicking on them and selecting **Merge** from the shortcut menu, then adjust them in order to place the bar chart and pie chart vertically in the report tab.

Next, we will insert the two charts into the tabular cells and have them share the same dataset as the OrdersDetailInformation report tab.

1. Select the first tabular cell and select **Insert** > **Chart** on the menu bar.
2. In the Data screen of the Create Chart wizard, select the **More Options** button, check the **Existing Dataset** radio button, then select the dataset **OrdersReport**. select **Next**.
3. In the Type screen, keep the default chart type Clustered Bar 2-D and select **Next**.
4. In the Display screen, select the summary **Sum\_SQLProductSalesbyOrderID** and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901075351/btn_addarw.gif) beside the Show Values box, Orders\_OrderID is then added automatically to the Category box.
5. Select **Style** the switch to the screen and select **Basic** from the Style list. select **Finish** to create the chart.
6. When a box attached to your mouse pointer, select the tabular cell to place the chart there.

   ![Insert Chart](https://devnet.logianalytics.com/hc/article_attachments/4404901076887/rpt_lsn8_box.gif)
7. Select the second tabular cell and insert a clustered pie chart in it which uses the same dataset and displays the same data in the same style with the bar chart.
8. Double-click any bar of the chart. In the Formar Bar dialog, switch to the **Fill** tab and check the **Vary Colors by Color List** checkbox to make each bar filled with a different color schema, then select **OK** to apply the setting and close the dialog. The chart shows as follows:

![Add Label to Chart](https://devnet.logianalytics.com/hc/article_attachments/4404901077143/rpt_lsn8_varyclr.gif)

9. Right-click the bar chart and select **Add Label** from the shortcut menu. A label is then added to the chart.

   ![Add Label to Chart](https://devnet.logianalytics.com/hc/article_attachments/4404901077399/rpt_lsn8_addlbl.gif)
10. Move the label to the top of the chart, then double-click it to display the Format Label dialog.
11. In the General tab, change the label text to **Current Orders for This Customer**.
12. Switch to the **Font** tab, change Font Size to **12pt**, Font Color to **808080** and select **OK**.

    ![Format Label](https://devnet.logianalytics.com/hc/article_attachments/4404909088023/rpt_lsn8_fmtlbl.gif)
13. Resize the label to make sure the text is displayed completely.
14. Add a label to the pie chart and format it using the same way and edit its text to **Current Orders for This Employee**.
15. In the Report Inspector, select the **Chart Object** and **Chart Object 1** nodes from the report structure tree by holding the Ctrl key on the keyboard, then change the Border Type properties to **none**.

    ![Edit Border Type](https://devnet.logianalytics.com/hc/article_attachments/4404909088279/rpt_lsn8_border.gif)
16. Select the **Chart Legend Object** and **Chart Legend Object 1** nodes and change the Border Type property to **None** as well.
17. Further format the two charts to improve their appearance if desired. For details about formatting chart, you can refer to [Task 2 of Lesson 4](https://devnet.logianalytics.com/hc/en-us/articles/1500011431402-Lesson-4-Creating-a-Chart-Report#Task2).

    Now the second report tab in the report is created to show the sales total by orders.

    ![Subreport](https://devnet.logianalytics.com/hc/article_attachments/4404909088535/rpt_lsn8_scdrpt.gif)
18. On the report tab bar, right-click the report tab containing the charts to rename it to **Sub\_OrderDetails**.
19. Select **File** > **Save** to save the report as **OrdersReport.cls**.

## Task 2: Insert a Subreport

After creating the report, we can insert the subreport to the primary report by specifying relationships between them. In this lesson, we can specify different relationships between the primary report (the first one) and the two chart components in the second report tab by setting up different links between them. Then Logi JReport will build a subreport for every order with the conditions, so that it is convenient to see the corresponding customer and employee information of every order.

We want this subreport to be at the end of the existing reports, thus we need to add a second group header and add the subreport to the new header.

1. Select **OrderDetailInformation** on the report tab bar to switch to the report tab.

   ![Report Tab Bar](https://devnet.logianalytics.com/hc/article_attachments/4404901077655/rpt_lsn8_bar.gif)
2. Right-click in the GH panel of the banded object and choose **Insert Panel After** from the shortcut menu.
3. Select the newly-added panel and select **Insert** > **Subreport**.
4. When a box attached to the mouse pointer, select the newly-added panel to place the subreport into it, and the Subreport dialog appears.
5. Select the **Browse** button, select **OrdersReport.cls** and then select **Open**.
6. Select **Sub\_OrderDetails** from the Report Tab drop-down list.
7. Select the **Add** button beside the Component in Report Tab box in the Field tab, choose **Chart Object** in the Choose Component dialog, then select **OK**.

   ![Add Component from Subreport](https://devnet.logianalytics.com/hc/article_attachments/4404909088791/rpt_lsn8_subrpt.gif)
8. Build the relationship between the primary report and the selected chart object on the Orders\_CustomerID field by selecting the field and selecting ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901075351/btn_addarw.gif).

   ![Edit Subreport Relationship](https://devnet.logianalytics.com/hc/article_attachments/4404909089047/rpt_lsn8_rltnshp.gif)
9. Select the **Add** button again, this time choose **Chart Object 1** in the Choose Component dialog, then select **OK**.
10. Build the relationship between the primary report and the second chart object on the Orders\_EmployeeID field.
11. Select **OK** in the Subreport dialog and the report tab will be inserted in the OrderDetails report tab as follows:

    ![Insert Subreport](https://devnet.logianalytics.com/hc/article_attachments/4404909089303/rpt_lsn8_instsub.gif)

Next, we will filter the dataset used by report tabs in the report so as to enhance the performance when running the report.

1. Select **Report** > **Manage Datasets** to display the Manage Datasets dialog.

   The Manage Datasets dialog lists all the dataset used in the current report. In our report, all the components share the same dataset, so here only one dataset is shown.
2. Select the **Filter** tab, select the **Add Condition** button to add a filter line, select **ORDERS\_ORDERID**from the field drop-down list, **<=** from the operator drop-down list, and enter **3050** in the value text field to specify the filter condition as **ORDERS\_ORDERID <= 3050**, then select **OK**.

   ![Filter Dataset](https://devnet.logianalytics.com/hc/article_attachments/4404901077911/rpt_lsn8_fltr.gif)
3. Select **File** > **Save** to save the report.
4. Select the **View** tab, the report tab that contains a subreport is displayed as follows: the primary report shows the orders detail information grouped by order ID, and the subreport shows the orders information by different customers and different employees respectively in the two charts.

   ![Preview Report](https://devnet.logianalytics.com/hc/article_attachments/4404901078167/rpt_lsn8_rpt.gif)

   **Note:** If the report does not look correct, you can compare it to the final version of the report provided by Logi JReport. To do so, you will need to save and close this catalog and then open the JinfonetGourmetJava.cat catalog file located at `<install_root>\Demo\Reports\TutorialReports`.

As you learned in this lesson, it is very convenient to build up a library of reports that act as components that you can add to various primary reports. Properly designed and used, subreports save a lot of time and effort in rapidly adapting your applications to changing user requirements and needs.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500011431362-Lesson-7-Creating-a-Tabular-Report) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011463441-Lesson-9-Creating-a-Parameter-Based-Report)
