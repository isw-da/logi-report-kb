---
title: "Lesson 3: Running Reports"
id: 4405661258647
section: "Logi Report Tutorial v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661258647-Lesson-3-Running-Reports
updated_at: 2022-01-27T20:34:07Z
---

# Lesson 3: Running Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556073751/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664323479-Lesson-2-Publishing-Resources)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420542052759/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661260183-Lesson-4-Scheduling-Reports)

# Lesson 3: Running Reports

This lesson describes how to run reports from the Server Console. This lesson represents one way that end users could access and run published reports. Reports that are embedded in a Java application cannot be accessed from the Server Console, but instead from the Java application. The interaction with the report itself however would be the same as described here.

The reports you view in this lesson are in the JinfonetGourmetJava folder, which is the folder you published them to in [Lesson 2 > Task 1](https://devnet.logianalytics.com/hc/en-us/articles/4405664323479-Lesson-2-Publishing-Resources#Task1) of this track. Before you can view the reports, make sure you have the Execute and/or Edit permissions on them.

This lesson contains the following tasks:

* [Task 1: Directly Run a Report](#Task1)
* [Task 2: Run a Parameter-Based Report](#Task2)
* [Task 3: Run a Report in Advanced Mode](#Task3)

## Task 1: Directly Run a Report

Direct running of reports is to use the default format settings to view the reports. By default, Server runs page reports (.cls) in Page Report Studio and web reports (.wls) in Web Report Studio.

In this task, we run a page report in the JinfonetGourmetJava folder as an example.

1. In the Resources page of the Server Console, go to the **Public Reports** > **JinfonetGourmetJava** folder.
2. Select the **ShipmentDetailsbyCustomer.cls** link to run the report.

   Server displays Page Report Studio in a separate web browser window, showing the ShipmentDetails report tab in the page report.

   ![Shipment Report](https://devnet.logianalytics.com/hc/article_attachments/4420556371223/admin_lsn3_rpt.gif)

When you directly run a report, if the report contains parameters, Server asks you to specify the parameter values. See the next task for more information.

## Task 2: Run a Parameter-Based Report

As you saw in the [Creating a Parameter-Based Report](https://devnet.logianalytics.com/hc/en-us/articles/4405661271703-Lesson-9-Creating-a-Parameter-Based-Report) lesson, parameter-driven reports are another way to have a dynamic report. They enable the report users to specify the data that they want to see before Logi Report Engine issues the query to the database. By only selecting the data that the report needs, the query is more efficient.

When you run a parameter-based report on Server, Server automatically displays the Enter Parameter Values dialog box to prompt you for the expected values. Server displays the default values in the dialog box, if they are included in the report template definition.

**To run the parameter-based report**

1. In the JinfonetGourmetJava folder, select the **OrderListbyDate\_Parameter.cls** link.

   Server displays the Enter Parameter Values dialog box in a new web browser window for you to specify the parameter values. The report template includes start date of May 1, 2016 and end date of June 1, 2016 as default. You can select the Submit button to admit these defaults, or you can type new values to view the report. Here we use the default values.

   ![Enter Parameter Values](https://devnet.logianalytics.com/hc/article_attachments/4420551122199/admin_lsn3_prm.gif)
2. Server displays the requested report showing only order details from May 1, 2016 to June 1, 2016.

   ![Parameter Report](https://devnet.logianalytics.com/hc/article_attachments/4420556371607/admin_lsn3_prmrpt.gif)

## Task 3: Run a Report in Advanced Mode

The Advanced Run command enables you to specify additional properties when running a report, for example you can specify a different report format instead of the default one, which can be one of the following: HTML, PDF, Text, Excel, Postscript, Rich Text Format (RTF), and XML. In this task, we run the report as PDF.

1. In the JinfonetGourmetJava folder, point to the **CustomerContactCard.cls** report row, then select **Advanced Run**![Advanced Run button](https://devnet.logianalytics.com/hc/article_attachments/4420556371863/btn_advrun.gif) on the floating toolbar.
2. In the Advanced Run dialog box, select the **Format** tab and select **PDF** from the **Select Format** drop-down list.

   ![Run in PDF](https://devnet.logianalytics.com/hc/article_attachments/4420556372119/admin_lsn3_vwpdf.gif)

   In this task, we do not use the additional options in the Advanced Run dialog box; however, these options can be quite useful in real reporting scenarios. For example, you can specify database credentials under which the query should execute, or apply a style group so that the report has a different look.
3. Select **Finish**. According to your Adobe configuration, Server displays the report as a PDF file in your web browser, or saves it into the default download folder of your browser.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556073751/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664323479-Lesson-2-Publishing-Resources)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420542052759/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661260183-Lesson-4-Scheduling-Reports)
