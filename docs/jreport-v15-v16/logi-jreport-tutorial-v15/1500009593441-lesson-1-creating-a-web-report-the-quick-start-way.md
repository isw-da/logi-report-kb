---
title: "Lesson 1: Creating a Web Report the Quick Start Way"
id: 1500009593441
section: "Logi JReport Tutorial v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009593441-Lesson-1-Creating-a-Web-Report-the-Quick-Start-Way
updated_at: 2021-07-24T05:53:40Z
---

# Lesson 1: Creating a Web Report the Quick Start Way

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404893760791/back.png)Previous Page](https://devnet.logianalytics.com/hc/en-us/articles/1500009593421-Track-3-Creating-and-Analyzing-Ad-Hoc-Reports) [Next Page![Next](https://devnet.logianalytics.com/hc/article_attachments/4404893761047/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009593461-Lesson-2-Creating-a-Web-Report-Using-Wizard)

# Lesson 1: Creating a Web Report the Quick Start Way

In this lesson, we will create a web report the quick start way and learn about the visualization toolbar which is also available in the [standard way](https://devnet.logianalytics.com/hc/en-us/articles/1500009593461-Lesson-2-Creating-a-Web-Report-Using-Wizard).

This lesson contains the following tasks:

* [Task 1: Create a Web Report](#Task1)
* [Task 2: Convert the Table to a Crosstab](#Task2)
* [Task 3: Convert the Crosstab to a Chart](#Task3)

## Task 1: Create a Web Report

1. On the [Logi JReport Server Start Page](https://devnet.logianalytics.com/hc/en-us/articles/1500009582241-Lesson-1-Starting-Logi-JReport-Server), select **Web Reports** in the Create category.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893785495/adhc_lsn1_strtpg.gif)
2. In the Select Data Source dialog, select **WorldWideSalesBV** from the Resources panel and the data fields **Region**, **Sales Year**, **Total Sales**, and **Category** from the business view to display in the table report. Select **OK**.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893785751/adhc_lsn1_slctdtsc.gif)
3. A table is generated.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893786007/adhc_lsn1_qcktbl.gif)

## Task 2: Convert the Table to a Crosstab

1. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893786263/btn_2crstb.gif) on the visualization toolbar on the left to convert the table to a crosstab:

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893786647/adhc_lsn1_2crstb.gif)
2. We will adjust the fields using the wizard to build a better looking report. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893786903/btn_wizard.gif) on the visualization toolbar and the Crosstab Wizard is displayed.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893787159/adhc_lsn1_crstbwzd.gif)
3. In the Rows box, select **Sales Year** and then select the **x** button at the top right of the box to remove it.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893787415/adhc_lsn1_rmvrow.gif)
4. Also remove Category from the Columns box.
5. In the Resources box, browse to the Products category at the bottom and select **Category**. Then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889271191/btn_add.gif) to add it to the Rows box.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889271447/adhc_lsn1_crstbwzdfinal.gif)
6. Select **OK** to confirm the changes. A message dialog is displayed asking for your confirmation of the change. Select **OK** in the dialog. Here we get a new crosstab.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893787671/adhc_lsn1_crstbnew.gif)

## Task 3: Convert the Crosstab to a Chart

1. There are many chart types available to the crosstab on the visualization toolbar. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889271703/btn_barcht.gif) to convert the crosstab to a bar chart:

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893787927/adhc_lsn1_barcht.gif)
2. If you'd like to view the data in a different chart type, select another chart type button on the visualization toolbar. Here, we select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889271959/btn_gauge.gif) to change it to a gauge chart.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893788183/adhc_lsn1_gauge.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404893760791/back.png)Previous Page](https://devnet.logianalytics.com/hc/en-us/articles/1500009593421-Track-3-Creating-and-Analyzing-Ad-Hoc-Reports) [Next Page![Next](https://devnet.logianalytics.com/hc/article_attachments/4404893761047/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009593461-Lesson-2-Creating-a-Web-Report-Using-Wizard)
