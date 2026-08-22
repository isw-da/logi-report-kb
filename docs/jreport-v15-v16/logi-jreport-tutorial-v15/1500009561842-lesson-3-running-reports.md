---
title: "Lesson 3: Running Reports"
id: 1500009561842
section: "Logi JReport Tutorial v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009561842-Lesson-3-Running-Reports
updated_at: 2021-07-24T05:56:28Z
---

# Lesson 3: Running Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404893760791/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009561822-Lesson-2-Publishing-Resources) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404893761047/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009561862-Lesson-4-Scheduling-Reports)

# Lesson 3: Running Reports

This topic describes how to run reports from the Logi JReport Server user console. This lesson represents one way that end users could access and run published reports. Reports that are embedded in a Java application would not be accessed from the user console, but instead from the Java application. The interaction with the report itself however would be the same as described here.

The reports you view in this lesson are in the JinfonetGourmetJava folder, which is the folder you published them to in [Lesson 2 > Task 1](https://devnet.logianalytics.com/hc/en-us/articles/1500009561822-Lesson-2-Publishing-Resources#Task1) of this track. Before you can view the reports, make sure you have the Execute and/or Edit permissions on them.

* [Task 1: Directly Run a Report](#Task1)
* [Task 2: Run a Parameter-based Report](#Task2)
* [Task 3: Run a Report in Advanced Mode](#Task3)

## Task 1: Directly Run a Report

Direct running of reports is to use the default format setting to view the report result. By default, page reports (.cls) are opened in Page Report Studio and web reports (.wls) in Web Report Studio.

In this task, we will run a page report in the JinfonetGourmetJava folder as an example:

1. On the Logi JReport Console page, go to the **Public Reports** > **JinfonetGourmetJava** folder.
2. Select the **ShipmentDetailsbyCustomer.cls** link to run the report.

   Page Report Studio then appears in a separate web browser window, with the report result for the ShipmentDetails report tab in the page report:

   ![Shipment Report](https://devnet.logianalytics.com/hc/article_attachments/4404894054039/admin_lsn3_rpt.gif)

When you directly run a report, if the report contains parameters, you will be asked to specify the parameter values. See the next task for details.

## Task 2: Run a Parameter-based Report

As you saw in the [Creating a parameter-based report](https://devnet.logianalytics.com/hc/en-us/articles/1500009562042-Lesson-9-Creating-a-Parameter-based-Report) lesson, parameter-driven reports are another way to have a dynamic report. They allow the end users to specify the data that they want to see before the query is issued to the database. By only selecting the data that the report needs, the query is more efficient.

When a parameter-based report is run, Logi JReport Server automatically displays the Enter Parameter Values dialog to prompt the user for the expected values. Default values, if included in the report template definition, are also displayed.

**To run the parameter-based report:**

1. In the JinfonetGourmetJava folder, select the **OrderListbyDate\_Parameter.cls** link.

   A new web browser window opens for you to enter the parameter values. The report template includes start date of May 1, 2015 and end date of June 1, 2015 as default. You can select **Submit** button to admit these defaults, or you can type new values to view the report.

   ![Enter Parameter Values](https://devnet.logianalytics.com/hc/article_attachments/4404889458583/admin_lsn3_prm.gif)
2. The requested report is displayed showing only order details from May 1, 2016 8:00:00 AM to June 1, 2016 8:00:00 AM.

   ![Parameter Report](https://devnet.logianalytics.com/hc/article_attachments/4404894054295/admin_lsn3_prmrpt.gif)

## Task 3: Run a Report in Advanced Mode

The Advanced Run command allows you to specify additional properties when running a report, for example you can specify a different report format instead of the default one. Options available include Applet, HTML, PDF, Text, Excel, Postscript, Rich Text Format (RTF), XML and Page Report. In this lesson we will run the report as PDF format.

1. In the JinfonetGourmetJava folder, put the mouse pointer over the **CustomerContactCard.cls** report row, then select the **Advanced Run** button ![Advanced Run button](https://devnet.logianalytics.com/hc/article_attachments/4404894054551/btn_advrun.gif) on the floating toolbar.
2. Select the **Format** tab and select **PDF** from the Select Format drop-down list, as shown below:

   ![Run in PDF](https://devnet.logianalytics.com/hc/article_attachments/4404894054807/admin_lsn3_vwpdf.gif)

   In this task, the additional options in the Advanced Run page are not used. However these options can be quite useful in real reporting scenarios. For example, you can specify database credentials under which the query should execute, or apply a style group so that the report has a different look.
3. Select the **Finish** button. According to your Adobe configuration, the report is displayed as a PDF file in your web browser, or saved into the default download folder of your browser.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404893760791/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009561822-Lesson-2-Publishing-Resources) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404893761047/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009561862-Lesson-4-Scheduling-Reports)
