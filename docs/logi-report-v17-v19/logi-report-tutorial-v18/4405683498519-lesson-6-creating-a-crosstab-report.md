---
title: "Lesson 6: Creating a Crosstab Report"
id: 4405683498519
section: "Logi Report Tutorial v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683498519-Lesson-6-Creating-a-Crosstab-Report
updated_at: 2022-01-27T07:58:19Z
---

# Lesson 6: Creating a Crosstab Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453376919/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690448023-Lesson-5-Creating-a-Table-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420461444759/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683499543-Lesson-7-Creating-a-Tabular-Report)

# Lesson 6: Creating a Crosstab Report

A report with quantities of different products that are sold in different regions and their sales totals is needed. You are required to create a crosstab that can clearly represent the necessary information, which enables the sales manager to easily compare the sales of different products in different regions.

Here is the sketch that is given to you:

![Report Sketch](https://devnet.logianalytics.com/hc/article_attachments/4420453737495/rpt_lsn6_sketch.gif)

Follow these tasks to create the report:

* [Task 1: Create the Crosstab](#Task1)
* [Task 2: Format the Crosstab](#Task2)
* [Task 3: Change the Page Layout](#Task3)
* [Task 4: Save the Report Style as .CSS](#Task4)

## Task 1: Create the Crosstab

Before taking this task, make sure you have enabled the "Insert field name label with field" option in the Options dialog box as [described at the last step of Lesson 3](https://devnet.logianalytics.com/hc/en-us/articles/4405683496343-Lesson-3-Creating-a-Mailing-Label-Report#Options); otherwise, Designer does not insert the name labels together with the fields when you add fields to the crosstab.

1. In Designer, navigate to **File** > **New** > **Page Report**.
2. In the Select Component for Page Report dialog box, select **Crosstab** and select **OK**.

   Be sure that JinfonetGourmetJava.cat is the current catalog because it is the catalog we use in this track. For information about specifying this catalog, see [Task 1, Step 2 and 3](https://devnet.logianalytics.com/hc/en-us/articles/4405690446871-Lesson-1-Creating-a-Standard-Banded-Report#SelectCat) of Lesson 1.
3. In the **Data** screen of the Crosstab Wizard dialog box, select **<New Query...>** in the Queries node of Data Source 1, type **ProductSalesAnalysis** in the Enter Query Name dialog box and select **OK**.
4. In the Add Tables/Views/Queries dialog box, expand the JDBC connection node and then the **Tables** node, then select the **Customers**, **Orders**, **Orders Detail**, and **Products** tables and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420447410583/btn_addarw.gif) to add them to the query. Select **OK** to close the dialog box.
5. In the Query Editor dialog box, Designer joins the tables together automatically based on the auto join criteria. Select all the columns in the **Orders Detail** table. For the Customers table, select the following columns: **Customer Name**, **Customers\_City**, **Customers\_State**, **Customers\_Country**, **Customers\_Territory**, and **Customers\_Region**, and for the Products table, the following columns: **Products\_Product ID**, **Product Name**, **Category**, **Product Type Name**, and **Price**.

   ![Select Columns for Quueries](https://devnet.logianalytics.com/hc/article_attachments/4420447413783/rpt_lsn6_addtbl.gif)

   You may notice that here we do not select any columns in the Orders table, that is because in this report, columns in this table are not needed but we need this table to create joins between tables in the query.
6. Select **OK** to create the query.
7. Select **Next** in the Crosstab Wizard dialog box.
8. In the **Display** screen, drag **Category** from the Resources box to the **Columns** box, drag **Customers\_Country** to the **Rows** box, and drag **Quantity** and the formula **Total** to the **Summaries** box one by one, then double-click in the **Aggregate** text box and select **Sum** from the drop-down list to change the aggregate function of the two summaries.

   ![Add Display Fields](https://devnet.logianalytics.com/hc/article_attachments/4420447414039/rpt_lsn6_dsply.gif)
9. Select **Style** on the screen navigation bar to switch to the screen and select the **Basic** style to apply to the crosstab.
10. Select **Finish** to create the crosstab report.

## Task 2: Format the Crosstab

In this task, we format the crosstab to make it look more professional.

1. Right-click on the crosstab and navigate to **Position** > **Absolute** on the shortcut menu, then drag it to the following position:

   ![Change Crosstab Position](https://devnet.logianalytics.com/hc/article_attachments/4420447414295/rpt_lsn6_pstn.gif)

   By setting the Position property of an object to "absolute", Designer locates the object at the position specified by drag-and-drop editing or by setting its X and Y coordinate property values.
2. Drag the **Label** icon ![Label button](https://devnet.logianalytics.com/hc/article_attachments/4420447412375/btn_label.gif) from the **Components** panel to add three labels in the report, then double-click each label to edit the text respectively to **Product Sales Analysis**, **Units**, and **Sales**.
3. Resize and adjust the crosstab and the three labels to place them as follows:

   ![Edit Labels](https://devnet.logianalytics.com/hc/article_attachments/4420461793559/rpt_lsn6_align.gif)

Next, we edit properties of the crosstab report objects in the Report Inspector to improve the appearance of the report.

1. Select the **Units** label and edit its **Bold** property to **true**, **Background** property to **Gray** and **Foreground** property to **White**.

   ![Edit Label Properties](https://devnet.logianalytics.com/hc/article_attachments/4420461793815/rpt_lsn6_unit.gif)
2. Select the **Sales** label and edit its **Bold** property to **true**, **Background** property to **0x99ccff** and **Foreground** property to **White**.
3. Select the field on the column header (Category field) and edit its **Background** property to **0x99ccff** and **Forground** to **White**.

   ![Edit Field Properties](https://devnet.logianalytics.com/hc/article_attachments/4420461794071/rpt_lsn6_ctgry.gif)
4. Select the two **Total** cells, the field on the row header (Customers\_Country field), and the four **#####** cells in the crosstab, then specify their **Foreground** property to **Gray**; select the four **#####** cells and change their **Format** property to **#,###**.

   ![Edit Field Foreground](https://devnet.logianalytics.com/hc/article_attachments/4420461794327/rpt_lsn6_frgrnd.gif)
5. Select the four **#,###.00** cells, change their **Foreground** property to **0x99ccff**, **Bold** property to **true**, and **Format** property to **$#,###.00**.

   ![Edit Total Properties](https://devnet.logianalytics.com/hc/article_attachments/4420461794583/rpt_lsn6_fmt.gif)
6. Select the **Product Sales Analysis** label, set its **Bold** property to **true**, **Font Size** property to **18**, and **Foreground** property to **Red**, then resize it to display its text completely.
7. On the report tab bar, right-click the report tab and select **Rename** to rename it to **ProductSales**.

   ![Rename Report Tab](https://devnet.logianalytics.com/hc/article_attachments/4420447410839/renmrpttb.gif)
8. Navigate to **File** > **Save** to save the report as **ProductSalesAnalysis.cls**.
9. Select the **View** tab to preview the crosstab.

   ![Preview Report](https://devnet.logianalytics.com/hc/article_attachments/4420447414551/rpt_lsn6_rpt.gif)

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg) If the report does not look correct, you can compare it to the final version of the report included in Designer. To do this, save and close your current catalog, and then open the **JinfonetGourmetJava.cat** catalog file in `<install_root>\Demo\Reports\TutorialReports`.

## Task 3: Change the Page Layout

When previewing the report, we can see that Designer displays the crosstab in two pages; however for a crosstab, such a layout is not convenient for analyzing data. Designer provides the Page Mode feature, which you can apply to specify how to layout the report pages: in pagination mode or continuous mode. When a report is in continuous mode, Designer lays out the whole report in a single page.

1. Clear **Page Layout** on the **View** menu tab.
2. Select the **View** tab to view the report again. Now, Designer displays the crosstab in a single page. We can scroll to have a complete view of the crosstab.

For a crosstab component, when it is in continuous page mode, you can further set another two properties to determine how many rows and columns we would like to view.

1. Select the crosstab, and set its **Items per Row Block** and **Items per Column Block** property values to **3** in the Report Inspector.
2. View the report. Designer now displays only three items in the row and column blocks.

   ![Three Blocks in Crosstab](https://devnet.logianalytics.com/hc/article_attachments/4420461794839/rpt_lsn6_item.gif)
3. Select **Page Layout** on the **View** menu tab to switch back to pagination mode. The two properties cannot take effect now.
4. Navigate to **File** > **Save** to save the report again.

## Task 4: Save the Report Style as .CSS

After formatting the report step by step in the Task 2, we can save the properties into a CSS style file, which we can apply to other crosstab reports directly.

1. Select the crosstab, right-click and select **Save Style** from the shortcut menu.
2. Keep the default settings in the New CSS Style dialog box and select **OK**.

   ![New CSS Style](https://devnet.logianalytics.com/hc/article_attachments/4420453737879/rpt_lsn6_nwcss.gif)
3. In the Save CSS As dialog box, type **Crosstab.css** in the **File Name** text box, then select **Save** to save the file to the default directory `<install_root>\style`.

   Designer displays the CSS Style Definition for CrosstabObject dialog box.

   ![CSS Definition for Crosstab](https://devnet.logianalytics.com/hc/article_attachments/4420453738135/rpt_lsn6_svcss.gif)
4. Add all the properties of the crosstab from the **All Properties** box to the **Selected Properties** box by selecting **Add All**![Add All button](https://devnet.logianalytics.com/hc/article_attachments/4420453738391/btn_addall.gif).
5. Select **Save** to save these properties in Crosstab.css.

Now, we have saved the style of the crosstab report as a CSS file. We can apply properties in the file to the corresponding components of other reports directly by selecting the CSS file from the <Import CSS File...> drop-down list on the Home menu tab in Designer.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453376919/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690448023-Lesson-5-Creating-a-Table-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420461444759/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683499543-Lesson-7-Creating-a-Tabular-Report)
