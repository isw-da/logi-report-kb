---
title: "Lesson 9: Creating a Parameter-Based Report"
id: 1500009770141
section: "Track 1: Creating Page Reports"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009770141-Lesson-9-Creating-a-Parameter-Based-Report
updated_at: 2021-07-24T00:49:50Z
---

# Lesson 9: Creating a Parameter-Based Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404885299607/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009742362-Lesson-8-Creating-a-Report-That-Contains-a-Subreport)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880128919/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009770061-Track-2-Creating-Business-Views)

# Lesson 9: Creating a Parameter-Based Report

In [Lesson 1](https://devnet.logianalytics.com/hc/en-us/articles/1500009770081-Lesson-1-Creating-a-Standard-Banded-Report) of this track we created a page report that contains an order list report tab to show order lists of every month from 2015 to 2016. Now, the sales manager is asking for this same report but with different orders during a specified time. Instead of building a new report about orders in each order date, we will save the page report as a new one and then modify the dataset used by its report to meet the requirements.

Follow the tasks below to finish creating the report:

* [Task 1: Create the Parameters](#Task1)
* [Task 2: Modify the Report Dataset to Use Parameters](#Task2)
* [Task 3: Preview and Test the Report](#Task3)

## Task 1: Create the Parameters

1. In Designer, select **File** > **Open** to open the report OrderListbyDate.cls created in Lesson 1 in the JinfonetGourmetJava.cat catalog file.
2. Select **File** > **Save As** to save the report as **OrderListbyDate\_Parameter.cls**. Then we begin to modify this report instead of the former one.
3. In the Data panel, select the **<New Parameter...>** item in the Parameters node.

   ![New Parameter](https://devnet.logianalytics.com/hc/article_attachments/4404880673303/rpt_lsn9_prm.gif)
4. In the New Parameter dialog box, type **pStartDate** in the Name field, keep the default Value Setting, select **DateTime** from the Value Type drop-down list, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404880673687/btn_add.gif) to add a value row in the Value List box and type **May 1, 2016, 8:00:00 AM** as the prompting value, and then type **Please input start date:** as the prompting text. Select **OK** to create the parameter.

   ![Define the Parameter](https://devnet.logianalytics.com/hc/article_attachments/4404880673943/rpt_lsn9_crtprm.gif)
5. Repeat steps 3 to 4 to create another parameter with the following values:
   * **Parameter Name**: pEndDate
   * **Value Setting:** Type-in Parameter
   * **Value Type**: DateTime
   * **Prompting Values**: June 1, 2016, 8:00:00 AM
   * **Prompting Text**: Please input end date:

## Task 2: Modify the Report Dataset to Use Parameters

In this task, we will apply the parameters created above to filter the dataset which is used by the report. Then when we view the report, we can specify different parameter values to dynamically filter the report to get data in the desired time period.

1. On the Data panel toolbar, select the **Dataset Filter** button ![Dataset Filter button](https://devnet.logianalytics.com/hc/article_attachments/4404880674199/btn_fltr.gif).
2. In the Dataset Filter dialog box, select the **Add Condition** button to add a filter line, select **ORDER DATE** from the field drop-down list, set **>=** as the operator, then select the **ellipsis** button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404885677719/btn_chsr.gif).
3. In the Expressions dialog box, double-click the **pStartDate** parameter to use it as value of the filter condition.
   Then close the Expressions dialog box.

   ![Filter Dataset](https://devnet.logianalytics.com/hc/article_attachments/4404885677975/rpt_lsn9_prmfltr.gif)
4. Select **Add Condition** button to add another filter line. The relationship between the two filters will be And.
5. Specify condition of the newly added filter as follows:

   ![Dataset Filter Conditions](https://devnet.logianalytics.com/hc/article_attachments/4404880674839/rpt_lsn9_fltr.gif)
6. Select **OK** in the dialog box to apply the settings.

Parameters can also be used to filter queries to limit their data. However, in this task, we cannot set the filter on the report's query. If we do that, all datasets based on the query will be affected, that is to say, the filter will also be applied to the report created in Lesson 1.

## Task 3: Preview and Test the Report

After the steps above, readers of this report can specify any date to get orders with the time they need by specifying the parameter values dynamically.

1. Save the report and select the **View** tab to preview the report.

   Designer recognizes that the query is based on the value of two parameters, and therefore prompts for them as follows:

   ![Enter Parameter Values](https://devnet.logianalytics.com/hc/article_attachments/4404880675351/rpt_lsn9_value.gif)
2. Specify the start date and end date as required in the combo boxes or select the calendar icon to select the date.
3. Select the **Default** button to generate the report output based on the default values for the parameters. Designer displays the report as follows, showing information for orders from May 1, 2016 8:00:00 AM to June 1, 2016 8:00:00 AM only:

   ![Preview Report](https://devnet.logianalytics.com/hc/article_attachments/4404880675607/rpt_lsn9_rpt.gif)

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg) If the report does not look correct, you can compare it to the final version of the report included in Designer. To do this, save and close your current catalog, and then open the **JinfonetGourmetJava.cat** catalog file located at `<install_root>\Demo\Reports\TutorialReports`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404885299607/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009742362-Lesson-8-Creating-a-Report-That-Contains-a-Subreport)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880128919/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009770061-Track-2-Creating-Business-Views)
