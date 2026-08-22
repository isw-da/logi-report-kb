---
title: "Lesson 1: Creating a Web Report the Quick Start Way"
id: 1500011463261
section: "Logi JReport Tutorial v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500011463261-Lesson-1-Creating-a-Web-Report-the-Quick-Start-Way
updated_at: 2021-07-24T10:39:38Z
---

# Lesson 1: Creating a Web Report the Quick Start Way

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)Previous Page](https://devnet.logianalytics.com/hc/en-us/articles/1500011463281-Track-3-Creating-and-Analyzing-Ad-Hoc-Reports) [Next Page![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011463241-Lesson-2-Creating-a-Web-Report-Using-Wizard)

# Lesson 1: Creating a Web Report the Quick Start Way

In this lesson, we will create a web report the quick start way and learn about the visualization toolbar of Web Report Studio, which is also available in the [traditional way](https://devnet.logianalytics.com/hc/en-us/articles/1500011463241-Lesson-2-Creating-a-Web-Report-Using-Wizard).

This lesson contains the following tasks:

* [Task 1: Create a Web Report](#Task1)
* [Task 2: Work with the Visualization Toolbar](#Task2)

## Task 1: Create a Web Report

1. In the [Logi JReport Server Start Page](https://devnet.logianalytics.com/hc/en-us/articles/1500011431562-Lesson-1-Starting-Logi-JReport-Server), select **Web Report** in the Create category. Web Report Studio is then displayed in a new tab, prompting you to select data for the new report.
2. In the Select Catalog dialog, expand the **SampleReports** folder, select the **SampleReports.cat** catalog and select **OK**.

   ![Select Report Data](https://devnet.logianalytics.com/hc/article_attachments/4404909081879/adhc_lsn1_slctcat.gif)
3. In the Select Data Source dialog, select **WorldWideSalesBV** in the Resources box. All the data fields contained in the business view are then displayed in the right box. Select **Region**, **Sales Year**, **Total Sales**, and **Category** and select **OK**.

   ![Select Report Data](https://devnet.logianalytics.com/hc/article_attachments/4404901066647/adhc_lsn1_slctdt.gif)

   A web report containing a table is generated.

   ![Table](https://devnet.logianalytics.com/hc/article_attachments/4404901066903/adhc_lsn1_qcktbl.gif)

## Task 2: Work with the Visualization Toolbar

Via the visualization toolbar (the toolbar displayed vertically) of Web Report Studio, you can conveniently convert a data component between the following types: table, crosstab or chart.

First, we will convert the table to a crosstab.

1. Select ![Crosstab button](https://devnet.logianalytics.com/hc/article_attachments/4404901067159/btn_2crstb.gif) on the visualization toolbar. The table is converted to a crosstab:

   ![Convert Table to Crosstab](https://devnet.logianalytics.com/hc/article_attachments/4404909082135/adhc_lsn1_2crstb.gif)

The visualization toolbar also provides entry to the wizard of current data component. With the wizard you can redefine a data component, apply filter to narrow down data displayed in the component.

Next we will use the wizard to edit the data fields displayed in the crosstab.

1. Select ![Wizard button](https://devnet.logianalytics.com/hc/article_attachments/4404901067415/btn_wizard.gif) on the visualization toolbar and the Crosstab Wizard is displayed.

   ![Crosstab Wizard](https://devnet.logianalytics.com/hc/article_attachments/4404901067671/adhc_lsn1_crstbwzd.gif)
2. In the Rows box of Data tab, select **Sales Year** and then select the **X** button at the top right of the box to remove it.

   ![Remove Row Field](https://devnet.logianalytics.com/hc/article_attachments/4404909082391/adhc_lsn1_rmvrow.gif)
3. Remove Category from the Columns box in the same way.
4. In the Resources box, browse to the Products category at the bottom and select **Category**, then select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404909082647/btn_add.gif) to add it to the Rows box.

   ![Add Row Field](https://devnet.logianalytics.com/hc/article_attachments/4404901067927/adhc_lsn1_crstbwzdfinal.gif)
5. Select **OK** to confirm the changes. A message dialog is displayed asking for your confirmation of the change. select **OK** in the dialog.

   A new crosstab is created.

   ![Newly Defined Crosstab](https://devnet.logianalytics.com/hc/article_attachments/4404901068183/adhc_lsn1_crstbnew.gif)

Lastly we will convert the crosstab to a chart and save the web report.

1. Select ![Bar Chart button](https://devnet.logianalytics.com/hc/article_attachments/4404901063831/btn_barcht.gif) on the visualization toolbar. The crosstab is converted to a bar chart as follows. You can also select other chart types on the toolbar.

   ![Convert Crosstab to Chart](https://devnet.logianalytics.com/hc/article_attachments/4404901068439/adhc_lsn1_barcht.gif)
2. Select the **Save** button ![Save button](https://devnet.logianalytics.com/hc/article_attachments/4404901050647/btn_save.gif) on the toolbar, the Save As dialog is then displayed.
3. From the Save In drop-down list, select the **My Reports** folder, input **Product Sales** in the File Name text box, then select **OK** to save the report to the server resource tree.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)Previous Page](https://devnet.logianalytics.com/hc/en-us/articles/1500011463281-Track-3-Creating-and-Analyzing-Ad-Hoc-Reports) [Next Page![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011463241-Lesson-2-Creating-a-Web-Report-Using-Wizard)
