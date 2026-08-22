---
title: "Lesson 1: Creating a Standard Banded Report"
id: 5735563121559
section: "Logi Report Tutorial v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735563121559-Lesson-1-Creating-a-Standard-Banded-Report
updated_at: 2022-11-29T03:39:09Z
---

# Lesson 1: Creating a Standard Banded Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898403124503/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735519573911-Track-1-Creating-Page-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898403130775/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735563128343-Lesson-2-Creating-a-Horizontal-Banded-Report)

# Lesson 1: Creating a Standard Banded Report

The Vice President of Sales at Jinfonet Gourmet Java requests a report about the monthly sales for the last two years. In this report, totals for sales need to be broken down by each order and each month, and presented for a grand total of all months.

Here is a draft of the report the vice president has given to you:

![Report Sketch](https://devnet.logianalytics.com/hc/article_attachments/9898539204247/rpt_lsn1_sketch.gif)

You immediately recognize the repetitive, columnar data in the center of the report and associated subtotals as a candidate for a standard banded report. This type of report has horizontal "bands" or panels that are geared for either detail record display or calculations, such as subtotals, that apply to a preceding group or the entire report.

Follow these tasks to create the report:

* [Task 1: Create the Initial Report and Query](#Task1)
* [Task 2: Add Summaries and Print Date to the Report](#Task2)
* [Task 3: Fine Tune the Report Layout](#Task3)

## Task 1: Create the Initial Report and Query

In this task, the wizard collects the necessary information and then creates the standard banded report. We can also create the data resources such as query and formulas required for the report via the wizard.

1. Select **Logi Report Designer** in the **Logi Report** folder on the Start menu to open Designer.
2. Designer displays the main window and shows the Start Page by default. Close the Start Page.
3. Navigate to **File** > **Open Catalog**.

   ![Open Catalog](https://devnet.logianalytics.com/hc/article_attachments/9898523031191/rpt_lsn1_openctlg.gif)
4. In the Open Catalog File dialog box, browse to select the **JinfonetGourmetJava.cat** catalog file in `<install_root>\Demo\Reports\JinfonetGourmetJava`, then select **Open**.
5. Select **Yes** in the Warning dialog box. Designer displays the Catalog Manager for managing the selected catalog. Close it because we do not use it in this lesson.
6. Navigate to **File** > **New** > **Page Report**.
7. In the Select Component for Page Report dialog box, select **Banded** in the component box, then select **OK**.

   ![Select Banded for Page Report](https://devnet.logianalytics.com/hc/article_attachments/9898523036311/rpt_lsn1_nwrptst.gif)
8. In the **Data** screen of the Banded Wizard dialog box, select **<New Query...>** in the Queries node of Data Source 1, type **OrderListbyDate** in the Enter Query Name dialog box, then select **OK**.

   ![Create Query](https://devnet.logianalytics.com/hc/article_attachments/9898539217047/rpt_lsn1_qrynm.gif)

   Queries are a higher-level object in a catalog. The concept is similar to that of views in the database but they are stored in the catalog file rather than the database itself. You can use queries to view, change, and analyze data in different ways, and Logi Report can help you with the building of various professional reports based on queries.
9. In the Add Tables/Views/Queries dialog box, expand the JDBC connection node and then the **Tables** node, then select the **Orders**, **Orders Detail**, and **Products** tables and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898538498711/btn_addarw.gif) to add them to the query. Select **OK** to close the dialog box.

   ![Add Table for Query](https://devnet.logianalytics.com/hc/article_attachments/9898523045271/rpt_lsn1_addtbl.gif)
10. In the Query Editor dialog box, select all the columns in the three tables by selecting the top checkbox in each table, then clear the **Inventory** and **Reorder Level** columns in the **Products** table. Designer adds the columns you select in each table to the query and you can use them for creating reports.

    ![Select Table Columns for Query](https://devnet.logianalytics.com/hc/article_attachments/9898523051671/rpt_lsn1_clmn.gif)

By default, the auto join options for queries are enabled (you can find the corresponding commands on the Query > Auto Join menu in the Query Editor dialog box), which means Designer automatically joins the tables in queries based on the join criteria. So, the three tables are automatically joined because Designer recognizes the matching rows in each table. You can modify the join if you want or customize a different join for the tables.

Designer creates the SQL SELECT statement based on the columns, tables, and joins you specify. You can select the SQL button to see the SQL SELECT statement.

1. Select **OK** to create the query.
2. Select **Next** in the Banded Wizard dialog box to go to the **Display** screen. The Display screen determines which fields returned by the dataset are visible in the report.
3. From the **Resources** box, drag the following fields in the Products table to the right box one by one: **Product Type Name**, **Products\_Product ID**, **Product Name**, and **Category**, then select in the **Display Name** column for Products\_Product ID and type **Product ID**.

   ![Add Display Fields](https://devnet.logianalytics.com/hc/article_attachments/9898539239575/rpt_lsn1_dsply.gif)
4. Select **Next** to display the **Group** screen. The Group screen specifies the grouping criteria you want to apply to the selected records.

There are two levels of grouping in this report: first by Order Date and then by Orders\_Order ID.

1. In the Resources box, select **Order Date** in the Orders table and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898538498711/btn_addarw.gif) to add it as the first group-by field. Add **Orders\_Order ID** as the second group-by field. You can choose the sorting sequence of the groups in each group level in the Sort column. By default, the order is Ascend.
2. Select **For each month** from the **Special Function** drop-down list for the Order Date group. By applying this special function, Designer groups the records together, of which the field values are in the same month.

   ![Add Groups](https://devnet.logianalytics.com/hc/article_attachments/9898523056407/rpt_lsn1_grptb.gif)
3. Select **Style** on the screen navigation bar to switch to the screen and select **Simple** from the style list.

   By default, when you create a banded, table, crosstab, or chart report using wizard, Designer applies a default CSS style to it. In this lesson, we want to customize the report style by ourselves, so here we select the Simple style which has very little formatting.
4. Select **Finish** to create the report.

   The report tab with a banded object in it is now created. Designer identifies the panels in the banded object on the left side by their abbreviations: a banded header panel (BH), a banded page header panel (BPH), a detail panel (DT), a banded page footer panel (BPF), a banded footer panel (BF), and two group header panels (GH), and group footer panels (GF) for the two levels of grouping.

   ![Banded Panels](https://devnet.logianalytics.com/hc/article_attachments/9898523057943/rpt_lsn1_panels.gif)
5. Select the **View** tab to run the report and view it.

## Task 2: Add Summaries and Print Date to the Report

As described in the introduction of this lesson, you need to calculate the totals of sales per order and per month, and then the total of all months. You can accomplish these types of calculations by defining a dynamic summary that performs the computation and placing it in the group footer panel directly. A print date is a predefined field that is calculated at runtime by Logi Report.

First we need to add a field to the report that calculates the sales data. The predefined formula Total turns out to meet the requirement. The formula expression is: `@"Unit Price" * @Quantity - @"Unit Price" * @Quantity * @Discount/100`.

1. From the **Data** panel, drag the formula **Total** in the Formulas node next to the **Category** DBField. Designer places the label of the formula in the second GH panel.

   ![Add Total](https://devnet.logianalytics.com/hc/article_attachments/9898523085463/rpt_lsn1_addfml.gif)

   The Data panel is an integrated interface for managing the resources that the current report uses. You can create new resources including formulas, summaries, and parameters to use in the report and Designer saves them into the current catalog data source automatically.

Next, we create a dynamic summary based on the Total formula to compute total of product sales by order, by month, and also to calculate the grand total.

1. In the Data panel, select **<New Summary...>** in the Summaries node.
2. In the New Summary dialog box, choose **Sum** from the **Aggregate Function** drop-down list, select the formula **Total** in the Formulas node of the Resource box and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898539254039/btn_arrow.gif) to add it to the **Summary On** text box, select **Dynamic Summary** and keep its default settings, then select **OK**.

   ![New Summary](https://devnet.logianalytics.com/hc/article_attachments/9898539257495/rpt_lsn1_sum.gif)
3. Type **Sum\_ProductSales\_DynamicSummary** in the Enter Summary Name dialog box and select **OK** to create the summary.

Then when you insert this summary into the groups, Designer performs the calculation based on the groups. If you insert the summary into the banded header or banded footer panel, Designer computes based on the whole banded report.

5. Drag the summary **Sum\_ProductSales\_DynamicSummary** from the Summaries node of the Data panel to both of the two GF panels and the BF panel.
6. Select the labels for the newly added summaries, then in the Report Inspector, set their **Auto Map Field Name** property to **false**.
7. Double-click each label in the design area to edit the text to **Total by Order**, **Total by Month**, and **Grand Total** respectively.

   ![Add Summaries to Report](https://devnet.logianalytics.com/hc/article_attachments/9898523100311/rpt_lsn1_addsum.gif)
8. Resize the BPH panel and drag the **Label** icon ![Label button](https://devnet.logianalytics.com/hc/article_attachments/9898538675991/btn_label.gif) from the **Components** panel to it to add a label in the panel.
9. Resize the new label and double-click it to edit its text to **Order List by Date**.

   ![Add Label](https://devnet.logianalytics.com/hc/article_attachments/9898523104407/rpt_lsn1_lbl.gif)
10. Navigate to **Insert** > **Special Fields** > **Date-time** > **Print Date** and then place the special field in the BPH panel, next to the Order List by Date label.
11. Insert the Print Time special field in the same way.

    ![Add Special Fields](https://devnet.logianalytics.com/hc/article_attachments/9898523109143/rpt_lsn1_splfld.gif)
12. Double-click the **Print Date** label and edit its text to **Date**; edit the text of **Print Time** to **Time** in the same way.
13. Adjust the position of the two groups by fields, then add two labels ahead of them for identification and edit their text as **Order Date** and **Order ID**.

    ![Add Group Names](https://devnet.logianalytics.com/hc/article_attachments/9898539300119/rpt_lsn1_grpfld.gif)

## Task 3: Fine Tune the Report Layout

To make the report easier to read, we need to make some adjustments to the report layout.

1. Resize the second GH panel.
2. Select the **Product Type Name**, **Product ID**, **Product Name**, and **Category** name labels in the BPH panel and move them to the second GH panel, so that they can be closer to the actual data they describe.
3. Resize the **Product Type Name**, **Product ID**, **Product Name**, **Category**, and **Total** name labels, and their corresponding DBFields, then manually drag and align them as follows:

   ![Drag to Align Objects](https://devnet.logianalytics.com/hc/article_attachments/9898523118615/rpt_lsn1_algn.gif)
4. Select the **Product ID** name label and the corresponding DBField in the DT panel, then navigate to **Format** > **Left**![Left Align button](https://devnet.logianalytics.com/hc/article_attachments/9898522997911/btn_alignleft.gif) to change their alignment to improve the report layout.
5. Select the five labels **Product Type Name**, **Product ID**, **Product Name**, **Category**, and **Total**, then in the Report Inspector, set their **Background** property to **Lightgray** and **Foreground** to **White**.

   ![Edit Color in Inspector](https://devnet.logianalytics.com/hc/article_attachments/9898539309975/rpt_lsn1_color.gif)
6. Select the **Total by Order** and **Total by Month** summaries and their name labels, then change their **Foreground** property to **Gray** in the Report Inspector.
7. Select the **Grand Total** summary and its name label in the BF panel, then change the **Foreground** property to **Red** in the Report Inspector.

   ![Edit Summay Colors](https://devnet.logianalytics.com/hc/article_attachments/9898523150231/rpt_lsn1_sumfld.gif)
8. Select the **Order ID** group-by field and its name label in the second GH panel and change their **Foreground** property to **Red** in the Report Inspector.
9. Select the **Date** and **Time** special fields in the BPH panel and the **Order Date** group-by field in the first GH panel with their name labels, then change their **Foreground** property to **Gray** in the Report Inspector.
10. Resize the **Order List by Date** label, change its **Font Size** property to **18** and **Foreground** property to **Red** in the Report Inspector.
11. Resize the **Date** and **Time** special fields and their name labels and change their position in the BPH panel to make them look tidy in the report.
12. In the Report Inspector, select the nodes representing the two group footer panels and the banded footer panel, then set their **Background** property to **Transparent**.
13. Right-click in the BH panel and select **Hide** from the shortcut menu to hide it from view. Repeat to hide the BPF panel in the same way.

    After editing, the report looks somewhat as follows in design view:

    ![Report in Design View](https://devnet.logianalytics.com/hc/article_attachments/9898539326487/rpt_lsn1_dsgn.gif)

Next, we give the report tab a meaningful name and save the report.

1. On the report tab bar, right-click the report tab and select **Rename** from the shortcut menu.

   ![Rename Report Tab](https://devnet.logianalytics.com/hc/article_attachments/9898538532887/renmrpttb.gif)
2. In the Input Report Tab Name dialog box, type **OrderDetails** and select **OK**.
3. Navigate to **File** > **Save** to save the report as **OrderListbyDate.cls**.
4. Select the **View** tab to run the report and view it. Designer displays the report similar to this:

   ![Preview Report](https://devnet.logianalytics.com/hc/article_attachments/9898539331095/rpt_lsn1_rpt.gif)

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) If the report does not look correct, you can compare it to the final version of the report included in Designer. To do this, save and close your current catalog, and then open the **JinfonetGourmetJava.cat** catalog file in `<install_root>\Demo\Reports\TutorialReports`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898403124503/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735519573911-Track-1-Creating-Page-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898403130775/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735563128343-Lesson-2-Creating-a-Horizontal-Banded-Report)
