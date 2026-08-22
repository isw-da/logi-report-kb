---
title: "Lesson 9: Creating a Parameter-Based Report"
id: 5741393493399
section: "Logi Report Tutorial v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741393493399-Lesson-9-Creating-a-Parameter-Based-Report
updated_at: 2022-11-30T02:36:32Z
---

# Lesson 9: Creating a Parameter-Based Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905613813911/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741406798103-Lesson-8-Creating-a-Report-That-Contains-a-Subreport)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905613870871/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741379967255-Track-2-Creating-Business-Views)

# Lesson 9: Creating a Parameter-Based Report

In [Lesson 1](https://devnet.logianalytics.com/hc/en-us/articles/5741398712727-Lesson-1-Creating-a-Standard-Banded-Report) of this track, we created a page report that contains an order list report tab to show order lists of every month from 2015 to 2016. Now, the sales manager is asking for this same report but with different orders during a specified time. Instead of building a new report about orders in each order date, we can save the page report as a new one and then modify the dataset it applies to meet the requirements.

Follow these tasks to create the report:

* [Task 1: Create the Parameters](#Task1)
* [Task 2: Modify the Report Dataset to Use Parameters](#Task2)
* [Task 3: Preview and Test the Report](#Task3)

## Task 1: Create the Parameters

1. In Designer, navigate to **File** > **Open** to open the report **OrderListbyDate.cls** we have created in Lesson 1 in the JinfonetGourmetJava.cat catalog file.
2. Navigate to **File** > **Save As** to save the report as **OrderListbyDate\_Parameter.cls**. Then we begin to modify this report instead of the former one.
3. In the **Data** panel, select **<New Parameter...>** in the Parameters node.

   ![New Parameter](https://devnet.logianalytics.com/hc/article_attachments/9905874687255/rpt_lsn9_prm.gif)
4. In the New Parameter dialog box, type **pStartDate** in the **Name** text box, keep the default **Value Setting**, select **Date** from the **Value Type** drop-down list, select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905874723735/btn_add.gif) to add a value row in the **Value List** box and type **May 1, 2016** as the prompting value, and then type **Please input start date:** as the prompting text. Select **OK** to create the parameter.

   ![Define the Parameter](https://devnet.logianalytics.com/hc/article_attachments/9905874762263/rpt_lsn9_crtprm.gif)
5. Repeat steps 3 to 4 to create another parameter with the following values:
   * **Parameter Name**: pEndDate
   * **Value Setting:** Type-in Parameter
   * **Value Type**: Date
   * **Prompting Values**: June 1, 2016
   * **Prompting Text**: Please input end date:

## Task 2: Modify the Report Dataset to Use Parameters

In this task, we apply the parameters created in the previous task to filter the dataset the report applies. Then when we view the report, we can specify different parameter values to dynamically filter the report to get data in the time period we want.

1. In the **Data** panel, select **Dataset Filter**![Dataset Filter button](https://devnet.logianalytics.com/hc/article_attachments/9905874809623/btn_fltr.gif) on the toolbar.
2. In the Dataset Filter dialog box, select **Add Condition** to add a filter line, select **ORDER DATE** from the field drop-down list, set **>=** as the operator, then select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9905874836759/btn_chsr.gif).
3. In the Expressions dialog box, double-click the **pStartDate** parameter to use it as value of the filter condition.
   Then close the Expressions dialog box.

   ![Filter Dataset](https://devnet.logianalytics.com/hc/article_attachments/9905863108631/rpt_lsn9_prmfltr.gif)
4. Select **Add Condition** to add another filter line. The relationship between the two filters is "And".
5. Specify condition of the newly added filter as follows:

   ![Dataset Filter Conditions](https://devnet.logianalytics.com/hc/article_attachments/9905874912919/rpt_lsn9_fltr.gif)
6. Select **OK** to apply the settings.

You can also use parameters to filter queries to limit data. However, in this task, we cannot set the filter on the query the report applies, because a query filter applies to all datasets based on the same query, meaning, it also applies to the report that we created in Lesson 1.

## Task 3: Preview and Test the Report

Users of this report can now specify any date to get orders with the time they need by specifying the parameter values dynamically.

1. Save the report and select the **View** tab to preview the report.

   Designer recognizes that the query is based on the value of two parameters, and therefore prompts for them as follows:

   ![Enter Parameter Values](https://devnet.logianalytics.com/hc/article_attachments/9905874933399/rpt_lsn9_value.gif)
2. Specify the start date and end date in the combo boxes or select the calendar to select the date.
3. Select **Default** to generate the report output based on the default values for the parameters. Designer displays the report as follows, which shows information for orders from May 1, 2016 to June 1, 2016 only.

   ![Preview Report](https://devnet.logianalytics.com/hc/article_attachments/9905863199511/rpt_lsn9_rpt.gif)

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) If the report does not look correct, you can compare it to the final version of the report included in Designer. To do this, save and close your current catalog, and then open the **JinfonetGourmetJava.cat** catalog file in `<install_root>\Demo\Reports\TutorialReports`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905613813911/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741406798103-Lesson-8-Creating-a-Report-That-Contains-a-Subreport)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905613870871/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741379967255-Track-2-Creating-Business-Views)
