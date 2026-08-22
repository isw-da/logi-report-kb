---
title: "Lesson 1: Creating a Standard Banded Report"
id: 1500009582301
section: "Logi JReport Tutorial v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009582301-Lesson-1-Creating-a-Standard-Banded-Report
updated_at: 2021-07-24T05:56:27Z
---

# Lesson 1: Creating a Standard Banded Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404893760791/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009582281-Track-1-Creating-Page-Reports) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404893761047/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009561962-Lesson-2-Creating-a-Horizontal-Banded-Report)

# Lesson 1: Creating a Standard Banded Report

This topic introduces how to create a Standard Banded Report.

A report of monthly sales for the last two years has been requested by the Vice President of Sales at Jinfonet Gourmet Java. In this report, totals for sales need to be broken down by each order and each month, as well as presented for a grand total of all months.

Here's a draft of the report the vice president has given to you:

![Report Sketch](https://devnet.logianalytics.com/hc/article_attachments/4404894041239/rpt_lsn1_sketch.gif)

You immediately recognize the repetitive, columnar data in the center of the report and associated subtotals as a candidate for a standard banded report. This type of report has horizontal "bands" or panels that are geared for either detailed record display or calculations, such as subtotals, that apply to a preceding group or the entire report.

Follow the tasks below to finish creating the report:

* [Task 1: Create the Initial Report and Query to Populate It](#Task1)
* [Task 2: Add Summaries and a Print Date to the Report](#Task2)
* [Task 3: Fine Tune the Report Layout](#Task3)

## Task 1: Create the Initial Report and Query to Populate It

In this task, the report wizard collects the necessary information and then creates the standard banded report. The data resources such as query and formulas needed in the report can be created via the report wizard.

1. Select **Start** > **Logi JReport 15** > **Logi JReport Designer** to start Logi JReport Designer. The Logi JReport Designer window with the Start Page appears. Close the Start Page.
2. Cick **File** >**Open Catalog**.

   ![Open Catalog](https://devnet.logianalytics.com/hc/article_attachments/4404894041495/rpt_lsn1_openctlg.gif)

   The Open Catalog File dialog appears.
3. Browse to select the **JinfonetGourmetJava.cat** catalog file in `<install_root>\Demo\Reports\JinfonetGourmetJava`, select the **Open** button, and then select **Yes** in the Warning dialog.

   The Catalog Manager appears for managing the selected catalog. Close it since we will not use it in the lesson.
4. Select **File** > **New** > **Page Report**.
5. In the Select Component for Page Report dialog, select  **Banded**, then select **OK**.

   ![Select Banded for Page Report](https://devnet.logianalytics.com/hc/article_attachments/4404894041751/rpt_lsn1_nwrptst.gif)
6. In the Data screen of the Banded Wizard, select **<New Query...>** in the Queries node of Data Source 1, input **OrderListbyDate** in the Enter Query Name dialog and then select **OK**.

   ![Create Query](https://devnet.logianalytics.com/hc/article_attachments/4404889451287/rpt_lsn1_qrynm.gif)

   Queries are a higher-level object in a catalog. The concept is similar to that of views in the database but they are stored in the catalog file rather than the database itself. You can use queries to view, change and analyze data in different ways, and Logi JReport can help you with the building of various professional reports based on queries.
7. In the Add Tables/Views/Queries dialog, expand the JDBC connection node and then the **Tables** node, then select the tables **Orders**, **Orders Detail** and **Products** and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404894023447/btn_addarw.gif) to add them to the query. Select **OK** to close the dialog.

   ![Add Table for Query](https://devnet.logianalytics.com/hc/article_attachments/4404894042007/rpt_lsn1_addtbl.gif)
8. In the Query Editor, select all the columns in the three tables by selecting the **\*** checkbox, then uncheck the **Inventory** and **Reorder Level** columns in the Products table. The selected columns will be added to the query and can be used for creating reports.

   ![Select Table Columns for Query](https://devnet.logianalytics.com/hc/article_attachments/4404894042263/rpt_lsn1_clmn.gif)

By default, the auto join options for queries are enabled (you can find the options on the sub menu of Query > Auto Join in the Query Editor), which means tables will be automatically joined in queries based on the join criteria. So, the three tables are automatically joined because Logi JReport Designer recognizes the matching rows in each table. You can modify the join if desired or customize a different join for set of tables.

Logi JReport creates the SQL SELECT statement based on the columns, tables, and joins you specify. Select the **SQL** button to see the SQL SELECT statement if necessary.

1. Select **OK** at the bottom of the Query Editor to create the query.
2. Select **Next** in the Banded Wizard to show the Display screen. The Display screen determines which fields returned by the dataset are visible in the report.
3. From the Resources box, drag and drop the following fields in the Products table to the right-hand box one by one: **Product Type Name**, **Products\_Product ID**, **Product Name** and **Category**, then change the display name of Products\_Product ID to **Product ID**.

   ![Add Display Fields](https://devnet.logianalytics.com/hc/article_attachments/4404889451671/rpt_lsn1_dsply.gif)
4. Select **Next** to display the Group screen. The Group screen specifies the grouping criteria to be applied to the selected records.

There are two levels of grouping in this report: first by Order Date and second by Orders\_Order ID.

1. From the Resources box, select the fields **Order Date** and **Orders\_Order ID** in the Orders table and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404894023447/btn_addarw.gif) to add them as the group by fields one by one.

   You can choose the sorting sequence of the groups in the Sort column. Specify it in descending order (c,b,a), ascending order (a,b,c) or a special ordering criteria. By default the order is Ascend.
2. Select **For each month** from the Special Function drop-down list for the Order Date group.

   ![Add Groups](https://devnet.logianalytics.com/hc/article_attachments/4404894042519/rpt_lsn1_grptb.gif)

   By selecting the for each month special function, the records, of which the field values are in the same month, will be grouped together.
3. Select **Style** to switch to the screen and select **Simple** from the Style list. The Summary, Chart, and Filter screens are skipped.

   By default, when you create a banded, table, crosstab or chart report via the report wizard, a default style Basic will be applied to it. However, in this lesson, we want to customize the report style by ourselves, so here we select the Simple style which has very little formatting.
4. Select **Finish** to create the report.

   The report with banded object is created. The panels in the banded object are identified on the left side by their abbreviations: a banded header panel (BH), a banded page header panel (BPH), a detail panel (DT), a banded page footer panel (BPF), a banded footer panel (BF), and two group header panels (GH) and group footer panels (GF) for the two levels of grouping:

   ![Banded Panels](https://devnet.logianalytics.com/hc/article_attachments/4404894042775/rpt_lsn1_panels.gif)
5. Select the **View** tab to run the report and view it.

## Task 2: Add Summaries and a Print Date to the Report

As it is described in the first paragraph of this lesson, you need to calculate the totals of sales per order and per month, and then the total of all months. These types of calculations can be accomplished by defining a dynamic summary that performs the computation and placing it in the group footer panel directly. A print date is a predefined field that is calculated at runtime by Logi JReport.

First we need to add a field to the report that calculates the sales data. The predefined formula Total turns out to meet the requirement. The formula expression is as follows: `@"Unit Price" * @Quantity - @"Unit Price" * @Quantity * @Discount/100`.

1. From the Data panel, drag the **Total** formula in the Formulas node and drop it next to the Category DBField. The label of the formula is then placed in the second GH panel as follows:

   ![Add Total](https://devnet.logianalytics.com/hc/article_attachments/4404894043031/rpt_lsn1_addfml.gif)

   The Data panel is an integrated interface for managing the resources that are used in the current report. You can create new resources including formulas, summaries and parameters to use in the report and they will be saved into the current catalog data source.

Next, we will create a dynamic summary based on the Total formula, so as to compute total of product sales by order, by month and also to calculate the grand total.

1. In the Data panel, select **<New Summary...>** in the Summaries node.
2. In the New Summary dialog, choose **Sum** from the Aggregate Function drop-down list, select the **Total** formula in the Formulas node of the Resource box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404894043287/btn_arrow.gif) to add it to the Summary On field, check the **Dynamic Summary** radio button and keep its default settings, then select **OK**.

   ![New Summary](https://devnet.logianalytics.com/hc/article_attachments/4404889451927/rpt_lsn1_sum.gif)
3. Input **Sum\_ProductSales\_DynamicSummary** in the Enter Summary Name dialog and select **OK** to create the summary.

Then when we insert this summary into the groups. Logi JReport will do the calculation based on the groups. If the summary is inserted into the banded header or banded footer panel, it will compute based on the whole banded report.

5. Drag the summary **Sum\_ProductSales\_DynamicSummary** from the Summaries node of the Data panel to both of the two GF panels as well as the BF panel.
6. Double-click the label for each of the newly added summaries to edit the text to **Total by Order**, **Total by Month** and **Grand Total** respectively.

   ![Add Summaries to Report](https://devnet.logianalytics.com/hc/article_attachments/4404894043671/rpt_lsn1_addsum.gif)
7. Resize the BPH panel and drag ![Label button](https://devnet.logianalytics.com/hc/article_attachments/4404889442071/btn_label.gif) from the Basic group in the Components panel to add a label in it.
8. Resize the newly-added label and double-click it to edit its text to **Order List by Date**.

   ![Add Label](https://devnet.logianalytics.com/hc/article_attachments/4404889452183/rpt_lsn1_lbl.gif)
9. Select **Insert** > **Special Fields** > **Date-time** > **Print Date** and then place the special field in the BPH panel, next to the Order List by Date label.
10. Insert the Print Time special field in the same way.

    ![Add Special Fields](https://devnet.logianalytics.com/hc/article_attachments/4404894043927/rpt_lsn1_splfld.gif)
11. Double-click the **Print Date** and **Print Time** labels and edit their text to **Date** and **Time**, respectively.
12. Adjust the position of the two groups by fields, add two labels ahead of them for identification and edit their text as **Order Date** and **Order ID** as follows:

    ![Add Group Names](https://devnet.logianalytics.com/hc/article_attachments/4404894044183/rpt_lsn1_grpfld.gif)

## Task 3: Fine Tune the Report Layout

To make the report easier to read, we need to make some adjustments to the report layout.

1. Resize the second GH panel. Select the **Product Type Name**, **Product ID**, **Product Name** and **Category** name labels in the BPH panel by holding the Ctrl key on the keyboard and move them to the second GH panel, so that they can be closer to the actual data they describe.
2. Resize the **Product Type Name**, **Product ID**, **Product Name**, **Category** and **Total** name labels, as well as their corresponding DBFields, manually drag and align them as follows:

   ![Drag to Align Objects](https://devnet.logianalytics.com/hc/article_attachments/4404894044439/rpt_lsn1_algn.gif)
3. Select the **Product ID** name label and the corresponding DBField in the DT panel by holding the Ctrl key on the keyboard, then select **Format** > **Left**![Left Align button](https://devnet.logianalytics.com/hc/article_attachments/4404894040471/btn_alignleft.gif) to change their alignment so as to improve the report layout.
4. Select the five labels **Product Type Name**, **Product ID**, **Product Name**, **Category** and **Total** by holding the Ctrl key on the keyboard, then in the Report Inspector, set their properties Background and Foreground to **Lightgray** and **White**.

   ![Edit Color in Inspector](https://devnet.logianalytics.com/hc/article_attachments/4404894044695/rpt_lsn1_color.gif)
5. Select the **Total by Order** and **Total by Month** summaries as well as their name labels by holding the Ctrl key on the keyboard, then change their Foreground property to **Gray** in the Report Inspector.
6. Select the **Grand Total** summary and its name label in the BF panel by holding the Ctrl key on the keyboard, then change the Foreground property to **Red** in the Report Inspector.

   ![Edit Summay Colors](https://devnet.logianalytics.com/hc/article_attachments/4404894044951/rpt_lsn1_sumfld.gif)
7. Select the **Order ID** group by field and its name label in the second GH panel by holding the Ctrl key on the keyboard and change their Foreground property to **Red** in the Report Inspector.
8. Select the **Date** and **Time** special fields in the BPH panel and the **Order Date** group by field in the first GH panel with their name labels by holding the Ctrl key on the keyboard, then change their Foreground property to **Gray** in the Report Inspector.
9. Resize the **Order List by Date** label, change its Font Size property to **18,** and Foreground property to **Red** in the Report Inspector.
10. Resize the **Date** and **Time** special fields and their name labels and change their position in the BPH panel to make them look tidy in the report.
11. In the Report Inspector, select the nodes representing the two group footer panels and the banded footer panel by holding the Ctrl key on the keyboard, then set their Background property to **Transparent**.
12. Right-click in the BH panel and select **Hide** from the shortcut menu to hide it from view. Repeat to hide the BPF panel in the same way.

    After editing, the report looks somewhat like below in design view:

    ![Report in Design View](https://devnet.logianalytics.com/hc/article_attachments/4404889452439/rpt_lsn1_dsgn.gif)

Next, we will give the report tab a meaningful name and save the report.

1. On the report tab bar, right-click the report tab and select **Rename** from the shortcut menu.

   ![Rename Report Tab](https://devnet.logianalytics.com/hc/article_attachments/4404894024471/renmrpttb.gif)
2. In the Input Report Tab Name dialog, enter **OrderDetails** and select **OK**.
3. Select **File** > **Save** to save the report as **OrderListbyDate.cls**.

Select the **View** tab to run the report and view it. The report should look similar to the following one:

![Preview Report](https://devnet.logianalytics.com/hc/article_attachments/4404889452695/rpt_lsn1_rpt.gif)

**Note:** If the report does not look correct, you can compare it to the final version of the report provided by Logi JReport. To do so, you will need to save and close this catalog and then open the JinfonetGourmetJava.cat catalog file located at `<install_root>\Demo\Reports\TutorialReports`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404893760791/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009582281-Track-1-Creating-Page-Reports) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404893761047/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009561962-Lesson-2-Creating-a-Horizontal-Banded-Report)
