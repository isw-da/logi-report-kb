---
title: "Lesson 6: Creating a Crosstab Report"
id: 1500009770121
section: "Track 1: Creating Page Reports"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009770121-Lesson-6-Creating-a-Crosstab-Report
updated_at: 2021-07-24T00:49:51Z
---

# Lesson 6: Creating a Crosstab Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404885299607/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009742322-Lesson-5-Creating-a-Table-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880128919/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009742342-Lesson-7-Creating-a-Tabular-Report)

# Lesson 6: Creating a Crosstab Report

A report with quantities of different products that are sold in different regions and their sales totals is needed. You are required to create a crosstab that can clearly represent the necessary information, which enables the sales manager to easily compare the sales of different products in different regions.

Here is the sketch that is given to you:

![Report Sketch](https://devnet.logianalytics.com/hc/article_attachments/4404880683799/rpt_lsn6_sketch.gif)

Follow the tasks below to finish creating the report:

* [Task 1: Create the Crosstab](#Task1)
* [Task 2: Format the Crosstab](#Task2)
* [Task 3: Change the Page Layout](#Task3)
* [Task 4: Save the Report Style as .CSS](#Task4)

## Task 1: Create the Crosstab

Before taking this task, make sure you have enabled the Insert field name label with field option in the Options dialog box as [described at the last step of Lesson 3](https://devnet.logianalytics.com/hc/en-us/articles/1500009742302-Lesson-3-Creating-a-Mailing-Label-Report#Options). Otherwise, the name labels will not be inserted together with the fields when you add fields to the crosstab.

1. In Designer, select **File** > **New** > **Page Report**.
2. In the Select Component for Page Report dialog box, select **Crosstab** and select **OK**.

   Be sure that JinfonetGourmetJava.cat is specified as the current catalog because it is the catalog we use in this track. For information about specifying this catalog, see [Task 1, Step 2 and 3](https://devnet.logianalytics.com/hc/en-us/articles/1500009770081-Lesson-1-Creating-a-Standard-Banded-Report#SelectCat) of Lesson 1.
3. In the Data screen of the Crosstab Wizard dialog box, select **<New Query...>** in the Queries node of Data Source 1, type **ProductSalesAnalysis** in the Enter Query Name dialog box and select **OK**.
4. In the Add Tables/Views/Queries dialog box, expand the JDBC connection node and then the **Tables** node, then select the **Customers**, **Orders**, **Orders Detail** and **Products** tables and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404880676375/btn_addarw.gif) to add them to the query. Select **OK** to close the dialog box.
5. In the Query Editor dialog box, the tables are joined together automatically based on the auto join criteria. Select all the columns in the Orders Detail table by selecting the **\*** check box. For the Customers table, select the following columns: **Customer Name**, **Customers\_City**, **Customers\_State**, **Customers\_Country**, **Customers\_Territory** and **Customers\_Region**, and for the Products table, the following columns: **Products\_Product ID**, **Product Name**, **Category**, **Product Type Name** and **Price**.

   ![Select Columns for Quueries](https://devnet.logianalytics.com/hc/article_attachments/4404885682967/rpt_lsn6_addtbl.gif)

   You may notice that here we do not select any columns in the Orders table, that is because in this report, columns in this table are not needed but we need this table to create joins between tables in the query.
6. Select **OK** to create the query.
7. Select **Next** in the Crosstab Wizard dialog box.
8. In the Display screen, add the DBField **Category** to the Columns box by selecting it and selecting ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404880676375/btn_addarw.gif), add **Customers\_Country** to the Rows box by selecting it and selecting ![Add Row button](https://devnet.logianalytics.com/hc/article_attachments/4404880680343/btn_addrow.gif), add the **Quantity** DBField and **Total** formula to the Summaries box by selecting them and selecting ![Add Summary button](https://devnet.logianalytics.com/hc/article_attachments/4404885681047/btn_addsum.gif) one by one, and then double-click in the Aggregate text box and select **Sum** from the drop-down list to change the aggregate function of the two summaries.

   ![Add Display Fields](https://devnet.logianalytics.com/hc/article_attachments/4404885683223/rpt_lsn6_dsply.gif)
9. Select **Style** to switch to the screen and select **Basic** from the Style list, then select **Finish** to create the crosstab report.

## Task 2: Format the Crosstab

In this task, we will format the crosstab to make it look more professional.

1. Right-click on the crosstab and select **Position** > **Absolute**, then drag it to the following position:

   ![Change Crosstab Position](https://devnet.logianalytics.com/hc/article_attachments/4404885683479/rpt_lsn6_pstn.gif)

   By setting the Position property of an object to absolute, the object will be located at the position specified by dragging and dropping or by setting its X and Y coordinate property values.
2. Drag the **Label** icon ![Label button](https://devnet.logianalytics.com/hc/article_attachments/4404885681815/btn_label.gif) from the Basic group in the Components panel to add three labels in the report, then double-click each label to edit the text respectively to **Product Sales Analysis**, **Units** and **Sales**. Resize and adjust the crosstab and the three labels to place them as follows:

   ![Edit Labels](https://devnet.logianalytics.com/hc/article_attachments/4404885683863/rpt_lsn6_align.gif)

Next, we will edit properties of the crosstab report objects in the Report Inspector to improve the appearance of the report.

1. Select the **Units** label and edit its Bold property to **true**, Background property to **Gray** and Foreground property to **White**.

   ![Edit Label Properties](https://devnet.logianalytics.com/hc/article_attachments/4404880684311/rpt_lsn6_unit.gif)
2. Select the **Sales** label and edit its Bold property to **true**, Background property to **0x99ccff** and Foreground property to **White**.
3. Select the field on the column header (Category field) and edit its Background property to **0x99ccff** and Forground to **White**.

   ![Edit Field Properties](https://devnet.logianalytics.com/hc/article_attachments/4404885684119/rpt_lsn6_ctgry.gif)
4. Select the two **Total** cells, the field on the row header (Customers\_Country field) and the four **#####** cells in the crosstab by holding the Ctrl key on the keyboard, and then specify their Foreground property to **Gray**. Then select the four **#####** cells and change their Format property to **#,###**.

   ![Edit Field Foreground](https://devnet.logianalytics.com/hc/article_attachments/4404885684375/rpt_lsn6_frgrnd.gif)
5. Select the four **#,###.00** cells by holding the Ctrl key on the keyboard, change their Foreground property to **0x99ccff**, Bold property to **true** and Format property to **$#,###.00**.

   ![Edit Total Properties](https://devnet.logianalytics.com/hc/article_attachments/4404880684567/rpt_lsn6_fmt.gif)
6. Select the **Product Sales Analysis** label, set its Bold property to **true**, Font Size property to **18**, and Foreground property to **Red**, then resize it to make its text not be truncated.
7. On the report tab bar, right-click the report tab and select **Rename** to rename it to **ProductSales**.

   ![Rename Report Tab](https://devnet.logianalytics.com/hc/article_attachments/4404880677911/renmrpttb.gif)
8. Select **File** > **Save** to save the report as **ProductSalesAnalysis.cls**.
9. Select the **View** tab. Designer displays the crosstab report like the following one:

   ![Preview Report](https://devnet.logianalytics.com/hc/article_attachments/4404885684631/rpt_lsn6_rpt.gif)

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg) If the report does not look correct, you can compare it to the final version of the report included in Designer. To do this, save and close your current catalog, and then open the **JinfonetGourmetJava.cat** catalog file located at `<install_root>\Demo\Reports\TutorialReports`.

## Task 3: Change the Page Layout

When previewing the report, we can see that Designer displays the crosstab in two pages; however for a crosstab, such a layout is not convenient for analyzing data. Designer provides the Page Mode feature, which you can apply to specify how to layout the report pages: in pagination mode or continuous mode. When a report is in continuous mode, Designer lays out the whole report in a single page.

1. Select **View** > **Page Layout**.
2. Select the **View** tab to view the report again. Now, Designer displays the crosstab in a single page. We can drag the scrollbar to have a complete view of the crosstab.

For a crosstab component, when it is in continuous page mode, we can further set another two properties to determine how many rows and columns we would like to view.

1. Select the crosstab, and set its Items per Row Block and Items per Column Block property values to **3** in the Report Inspector.
2. View the report. Designer now displays only three items in the row and column blocks.

   ![Three Blocks in Crosstab](https://devnet.logianalytics.com/hc/article_attachments/4404880685591/rpt_lsn6_item.gif)
3. Select **Page Layout** on the View menu to switch back to the pagination mode, then the two properties will not take effect.
4. Select **File** > **Save** to save the report again.

## Task 4: Save the Report Style as .CSS

After formatting the report step by step in the Task 2, we can save the properties into a CSS style file, which we can apply to other crosstab reports directly.

1. Select the crosstab, right-click and select **Save Style** from the shortcut menu.
2. Keep the default settings in the New CSS Style dialog box and select **OK**.

   ![New CSS Style](https://devnet.logianalytics.com/hc/article_attachments/4404885684887/rpt_lsn6_nwcss.gif)
3. In the Save CSS As dialog box, type **Crosstab.css** in the File Name text box, then select **Save** to save the file to the default directory `<install_root>\style`.

   Designer displays the CSS Style Definition for CrosstabObject dialog box.

   ![CSS Definition for Crosstab](https://devnet.logianalytics.com/hc/article_attachments/4404885685143/rpt_lsn6_svcss.gif)
4. Add all the properties of the crosstab from the All Properties box to the Selected Properties box by selecting ![Add All button](https://devnet.logianalytics.com/hc/article_attachments/4404880685975/btn_addall.gif).
5. Select **Save** to save these properties in the Crosstab.css file.

Now, we have saved the style of the crosstab report as a CSS file. We can apply properties in the file to the corresponding components of other reports directly by selecting the CSS file from the <Import CSS File...> drop-down list on the Home menu tab in Designer.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404885299607/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009742322-Lesson-5-Creating-a-Table-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880128919/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009742342-Lesson-7-Creating-a-Tabular-Report)
