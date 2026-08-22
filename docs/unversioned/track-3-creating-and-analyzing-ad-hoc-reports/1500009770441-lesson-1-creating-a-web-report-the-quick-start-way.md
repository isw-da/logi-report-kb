---
title: "Lesson 1: Creating a Web Report the Quick Start Way"
id: 1500009770441
section: "Track 3: Creating and Analyzing Ad Hoc Reports"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009770441-Lesson-1-Creating-a-Web-Report-the-Quick-Start-Way
updated_at: 2021-07-24T00:49:44Z
---

# Lesson 1: Creating a Web Report the Quick Start Way

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404885299607/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009742662-Track-3-Creating-and-Analyzing-Ad-Hoc-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880128919/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009770461-Lesson-2-Creating-a-Web-Report-Using-the-Wizard)

# Lesson 1: Creating a Web Report the Quick Start Way

In this lesson, we create a web report in the quick start way and learn about the visualization toolbar of Web Report Studio, which is also available in the [traditional way](https://devnet.logianalytics.com/hc/en-us/articles/1500009770461-Lesson-2-Creating-a-Web-Report-Using-the-Wizard).

This lesson contains the following tasks:

* [Task 1: Create a Web Report](#Task1)
* [Task 2: Work with the Visualization Toolbar](#Task2)

## Task 1: Create a Web Report

1. In the [Start Page](https://devnet.logianalytics.com/hc/en-us/articles/1500009769941-Lesson-1-Starting-Server) of the Server Console, select **Web Report** in the **Create** category.

   Server displays Web Report Studio in a new tab and prompts you to select data for the new report.
2. In the Select Catalog dialog box, expand the **SampleReports** folder, select the **SampleReports.cat** catalog and select **OK**.

   ![Select Report Data](https://devnet.logianalytics.com/hc/article_attachments/4404880656663/adhc_lsn1_slctcat.gif)
3. In the Select Data Source dialog box, select **WorldWideSalesBV** in the **Resources** box, Web Report Studio then displays all the folders in the business view in the right box. Select the data fields **Region**, **Sales Year**, **Total Sales**, and **Category**, and then select **OK**.

   ![Select Report Data](https://devnet.logianalytics.com/hc/article_attachments/4404880657175/adhc_lsn1_slctdt.gif)

   Web Report Studio creates a web report containing a table:

   ![Table](https://devnet.logianalytics.com/hc/article_attachments/4404880657431/adhc_lsn1_qcktbl.gif)

## Task 2: Work with the Visualization Toolbar

Via the visualization toolbar (the toolbar displayed vertically) of Web Report Studio, you can conveniently convert a data component between the following types: table, crosstab, or chart.

Firstly, we convert the table to a crosstab.

1. Select the button ![Crosstab button](https://devnet.logianalytics.com/hc/article_attachments/4404880657687/btn_2crstb.gif) on the visualization toolbar. Web Report Studio converts the table to a crosstab:

   ![Convert Table to Crosstab](https://devnet.logianalytics.com/hc/article_attachments/4404885666839/adhc_lsn1_2crstb.gif)

The visualization toolbar also provides entry to the wizard of current data component. With the wizard, you can redefine a data component, and apply filter to narrow down data in the component.

Next, we use the wizard to edit the data fields in the crosstab.

1. Select the **Crosstab Wizard** button ![Wizard button](https://devnet.logianalytics.com/hc/article_attachments/4404880658327/btn_wizard.gif) on the visualization toolbar. Web Report Studio displays the Crosstab Wizard dialog box.

   ![Crosstab Wizard](https://devnet.logianalytics.com/hc/article_attachments/4404885667095/adhc_lsn1_crstbwzd.gif)
2. In the **Rows** box of the **Data** tab, select **Sales Year** and then select the **Remove** button **X** at the top right of the box to remove it.

   ![Remove Row Field](https://devnet.logianalytics.com/hc/article_attachments/4404880658711/adhc_lsn1_rmvrow.gif)
3. Remove **Category** from the **Columns** box in the same way.
4. In the Resources box, browse to the **Products** category at the bottom and select **Category**, then select the button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404880659223/btn_add.gif) to add it to the Rows box.

   ![Add Row Field](https://devnet.logianalytics.com/hc/article_attachments/4404885667479/adhc_lsn1_crstbwzdfinal.gif)
5. Select **OK** to confirm the changes. Web Report Studio displays a message dialog box, asking for your confirmation of the change. Select **OK** in the dialog box.

   Web Report Studio creates a new crosstab:

   ![Newly Defined Crosstab](https://devnet.logianalytics.com/hc/article_attachments/4404880659863/adhc_lsn1_crstbnew.gif)

Lastly, we convert the crosstab to a chart and save the web report.

1. Select the button ![Bar Chart button](https://devnet.logianalytics.com/hc/article_attachments/4404880652311/btn_barcht.gif) on the visualization toolbar. Web Report Studio converts the crosstab to a bar chart as follows. You can also select other chart types on the toolbar.

   ![Convert Crosstab to Chart](https://devnet.logianalytics.com/hc/article_attachments/4404880660375/adhc_lsn1_barcht.gif)
2. Select the **Save** button ![Save button](https://devnet.logianalytics.com/hc/article_attachments/4404880621335/btn_save.gif) on the toolbar. Web Report Studio displays the Save As dialog box.
3. From the **Save In** drop-down list, select the **My Reports** folder, type **Product Sales** in the **File Name** text box, then select **OK** to save the report to the server resource tree.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404885299607/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009742662-Track-3-Creating-and-Analyzing-Ad-Hoc-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880128919/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009770461-Lesson-2-Creating-a-Web-Report-Using-the-Wizard)
