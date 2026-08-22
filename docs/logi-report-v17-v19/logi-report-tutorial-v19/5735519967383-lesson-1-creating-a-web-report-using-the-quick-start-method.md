---
title: "Lesson 1: Creating a Web Report Using the Quick Start Method"
id: 5735519967383
section: "Logi Report Tutorial v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735519967383-Lesson-1-Creating-a-Web-Report-Using-the-Quick-Start-Method
updated_at: 2022-11-29T03:39:09Z
---

# Lesson 1: Creating a Web Report Using the Quick Start Method

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898403124503/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735526532375-Track-1-Creating-and-Analyzing-Ad-Hoc-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898403130775/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735498124567-Lesson-2-Creating-a-Web-Report-Using-the-Wizard)

# Lesson 1: Creating a Web Report Using the Quick Start Method

In this lesson, we create a web report using the quick start method and learn about the visualization toolbar of Web Report Studio, which is also available when you use the [traditional method](https://devnet.logianalytics.com/hc/en-us/articles/5735498124567-Lesson-2-Creating-a-Web-Report-Using-the-Wizard).

This lesson contains the following tasks:

* [Task 1: Create a Web Report](#Task1)
* [Task 2: Work with the Visualization Toolbar](#Task2)

## Task 1: Create a Web Report

1. In the [Start Page](https://devnet.logianalytics.com/hc/en-us/articles/5735563057559-Lesson-1-Starting-Server) of the Server Console, select **Web Report** in the **Create** category. Server displays Web Report Studio in a new tab and prompts you to select data for the new report.
2. In the Select Catalog dialog box, expand the **SampleReports** folder, select the **SampleReports.cat** catalog and select **OK**.

   ![Select Report Data](https://devnet.logianalytics.com/hc/article_attachments/9898537489431/adhc_lsn1_slctcat.gif)
3. In the Select Data Source dialog box, select **WorldWideSalesBV** in the **Resources** box, Web Report Studio then displays all the elements in the business view in the right box. Select the following view elements: **Region**, **Sales Year**, **Total Sales**, and **Category**, then select **OK**.

   ![Select Report Data](https://devnet.logianalytics.com/hc/article_attachments/9898537493271/adhc_lsn1_slctdt.gif)

   Web Report Studio creates a web report containing a table.

   ![Table](https://devnet.logianalytics.com/hc/article_attachments/9898537498519/adhc_lsn1_qcktbl.gif)

## Task 2: Work with the Visualization Toolbar

Via the visualization toolbar (the toolbar displayed vertically) of Web Report Studio, you can conveniently convert a data component between the following types: table, crosstab, or chart.

First, we convert the table to a crosstab.

1. Select **Convert or drag to add Crosstab**![Crosstab button](https://devnet.logianalytics.com/hc/article_attachments/9898537504023/btn_2crstb.gif) on the visualization toolbar. Web Report Studio converts the table to a crosstab.

   ![Convert Table to Crosstab](https://devnet.logianalytics.com/hc/article_attachments/9898521354391/adhc_lsn1_2crstb.gif)

The visualization toolbar also provides entry to the wizard of current data component. With the wizard, you can redefine a data component, and apply filter to narrow down data in the component.

Next, we use the wizard to edit the data fields in the crosstab.

1. Select **Crosstab Wizard**![Wizard button](https://devnet.logianalytics.com/hc/article_attachments/9898521361047/btn_wizard.gif) on the visualization toolbar. Web Report Studio displays the Crosstab Wizard dialog box.

   ![Crosstab Wizard](https://devnet.logianalytics.com/hc/article_attachments/9898537547159/adhc_lsn1_crstbwzd.gif)
2. In the **Rows** box of the **Data** tab, select **Sales Year** and then select **Remove****X** at the top right of the box to remove it.

   ![Remove Row Field](https://devnet.logianalytics.com/hc/article_attachments/9898521372567/adhc_lsn1_rmvrow.gif)
3. Remove **Category** from the **Columns** box in the same way.
4. In the **Resources** box, select **Category** and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898537556503/btn_add.gif) to add it to the **Rows** box, then select **OK** to confirm the changes.

   ![Add Row Field](https://devnet.logianalytics.com/hc/article_attachments/9898537559063/adhc_lsn1_crstbwzdfinal.gif)
5. Web Report Studio displays a message dialog box, asking for your confirmation of the change. Select **OK** in the dialog box and Web Report Studio creates a new crosstab.

   ![Newly Defined Crosstab](https://devnet.logianalytics.com/hc/article_attachments/9898521382807/adhc_lsn1_crstbnew.gif)

Lastly, we convert the crosstab to a chart and save the web report.

1. Select **Convert or drag to add Bar**![Bar Chart button](https://devnet.logianalytics.com/hc/article_attachments/9898521237399/btn_barcht.gif) on the visualization toolbar. Web Report Studio converts the crosstab to a bar chart. You can also select other chart types on the toolbar.

   ![Convert Crosstab to Chart](https://devnet.logianalytics.com/hc/article_attachments/9898521388183/adhc_lsn1_barcht.gif)
2. Select **Save**![Save button](https://devnet.logianalytics.com/hc/article_attachments/9898520531223/btn_save.gif) on the toolbar. Web Report Studio displays .
3. In the Save As dialog box, select the **My Reports** folder from the **Save In** drop-down list, type **Product Sales** in the **File Name** text box, then select **OK** to save the report to the server resource tree.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898403124503/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735526532375-Track-1-Creating-and-Analyzing-Ad-Hoc-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898403130775/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735498124567-Lesson-2-Creating-a-Web-Report-Using-the-Wizard)
