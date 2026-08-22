---
title: "Lesson 4: Creating a Chart Report"
id: 1500009582341
section: "Logi JReport Tutorial v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009582341-Lesson-4-Creating-a-Chart-Report
updated_at: 2021-07-24T05:56:26Z
---

# Lesson 4: Creating a Chart Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404893760791/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009582321-Lesson-3-Creating-a-Mailing-Label-Report) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404893761047/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009561982-Lesson-5-Creating-a-Table-Report)

# Lesson 4: Creating a Chart Report

This topic introduces how to create a Chart Report.

The fourth quarter of the year has just ended, and you have been asked to produce a chart that shows product annual sales for each sales region. The sales manager wants to compare the historical sales data with the current data. Here's a sketch of the report that the sales manager has given to you, a bar chart:

![Report Sketch](https://devnet.logianalytics.com/hc/article_attachments/4404894033559/rpt_lsn4_sketch.gif)

Logi JReport supports more than 10 general chart types, and most of them have many sub-types or variations. After showing the sales manager the available bar chart types, he chose the 2-dimensional clustered bar chart.

Additionally, the sales manager requests that the report should be provided in Microsoft Excel file. This is not a problem, because all pre-defined reports in Logi JReport can be exported to HTML, PDF, Excel, RTF, XML, Text, Postscript, Mail and Fax.

Follow the tasks below to finish creating the report:

* [Task 1: Create the Chart](#Task1)
* [Task 2: Format the Chart](#Task2)
* [Task 3: Export the Report to an Excel File](#Task4)

## Task 1: Create the Chart

1. In Logi JReport Designer select **File** > **New** > **Page Report**.
2. In the Select Component for Page Report dialog, keep the default selected component type Chart and select **OK**.

   Be sure that JinfonetGourmetJava.cat is specified as the current catalog because it is the catalog we use in this track. For information about specifying this catalog, see [Task 1, Step 2 and 3](https://devnet.logianalytics.com/hc/en-us/articles/1500009582301-Lesson-1-Creating-a-Standard-Banded-Report#SelectCat) of Lesson 1.
3. In the Data screen of the Chart Wizard, select the query **AnnualSalesbyRegion** from the Queries node of Data Source 1 and then select **Next**.
4. In the Type screen, keep the default chart type Clustered Bar 2-D, then select **Next**.

In this chart, we want to display the region name on the category (X) axis, and annual sales of each region on the value (Y) axis. However, as the region names are too long to be displayed completely on the category axis, we will create a formula here to just get the abbreviations of the region names.

1. In the Display screen, scroll down to the **Formulas** node in the Resources box, and then select **<New Formula...>**.
2. Input the formula name **Region\_AbbreviationName** in the Enter Formula Name dialog and select **OK**, then define the formula in the Formula Editor as follows (you can copy the formula to the formula editing area directly), select **Save** on the toolbar to save the formula, and close the editor.

   |  |
   | --- |
   | ``` if (@Customers_REGION == "Asia-Pacific")             "APAC" else if (@Customers_REGION == "Europe, Middle East, Africa")             "EMEA" else if (@Customers_REGION == "Latin America")             "LATAM" else if (@Customers_REGION == "North America")             "NA" ``` |
3. Add the formula **Region\_AbbreviationName** to the Category box and **YearofOrderDate** to the Series box one by one by selecting each and selecting ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404894023447/btn_addarw.gif) beside the corresponding box. In the Show Values box, a numerical value is required.

In this lesson, we need to show the annual sales of each region, so a summary which is created on the column Annual Sales, and grouped by the formula Region\_AbbreviationName is needed.

1. Select **<New Summary...>** under the Summaries node in the Resources box of the Display screen.
2. In the New Summary dialog, specify the aggregate function as **Sum**, add the field **Annual Sales** from the Customers table to the Summary On field, specify the Group By field as the **Region\_AbbreviationName** formula, then select **OK**.

   ![New Summary](https://devnet.logianalytics.com/hc/article_attachments/4404894033943/rpt_lsn4_sum.gif)
3. Input **Sum\_AnnualSalesbyRegion\_AbbreviationName** in the Enter Summary Name dialog and select **OK** to create the summary.
4. Select the newly-created summary and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404894023447/btn_addarw.gif) beside the Show Values box. The Display screen appears as follows:

   ![Chart Display Fields](https://devnet.logianalytics.com/hc/article_attachments/4404894034199/rpt_lsn4_dsply.gif)

Next we will use the Layout screen of the Chart Wizard to add titles to the chart. The Layout screen provides options for customizing the layout of a chart, for example, you can hide some chart elements such as the legend and wall, set the offset of the category and series axes and so on.

1. Select **Layout** to switch to the  screen, select **Title** from the Options box, and then enter **Annual Sales by Region**  in the Chart Title text box and **Regions** in Category (X) Axis Title.

   ![Edit Chart Titles](https://devnet.logianalytics.com/hc/article_attachments/4404894034455/rpt_lsn4_layout.gif)

Logi JReport provides a set of CSS styles that can be applied to reports to easily change the format and appearance of the report. We will apply the Classic style to the chart.

1. Select **Next** to go to the Style screen and select **Classic** from the style list.
2. Select **Finish** to create the chart report and the report shows as follows in the design view:

   ![Report in Design View](https://devnet.logianalytics.com/hc/article_attachments/4404889447063/rpt_lsn4_dsgn.gif)
3. Select the **View** tab to view this chart, and it appears as follows:

   ![Preview Report Draft](https://devnet.logianalytics.com/hc/article_attachments/4404889447319/rpt_lsn4_vw.gif)

## Task 2: Format the Chart

The chart is accurate, but a little simple. We can add some polish to it by setting some of the chart properties. For each part of the chart object, such as the axes, legend, wall and so on, Logi JReport provides a corresponding format dialog, with which we can easily edit properties of a chart.

1. Select the **Design** tab to return to the design mode to do the adjustments.
2. Double-click a bar of the chart, and the Format Bar dialog appears.
3. In the General tab of the dialog, set the **Use Depth** option to **true**. Keep the default Depth and Direction.

   In the Format Bar dialog, you could also choose another sub-type for the chart in the Layout box if desired. In this lesson, we will continue using Clustered - 2D.

   ![Format Bar](https://devnet.logianalytics.com/hc/article_attachments/4404894034711/rpt_lsn4_fmtbar.gif)
4. Switch to the **Data Label** tab, specify Font as **Arial** and Font Size to **10 pt**.

   The Data labels that charts contain can be either static or dynamic. You can check the Show Static Data Label option and specify the Position for data labels according to your requirements, so that the labels are displayed statically in the chart. But in this lesson, we will just use the labels as dynamic ones, which will appear when the cursor is placed on bars.
5. Select **OK** to apply these property settings to bars of the chart.
6. Right-click the legend and then select **Format Legend** from the shortcut menu.
7. In the Format Legend dialog, select the **Font** tab, set Font as **Arial** and Font Size to **10 pt**.
8. Switch to the **Mark** tab, keep Item 0 selected in the Mark Items box, and select **circle** from the mark drop-down list.

   ![Format Legend Mark](https://devnet.logianalytics.com/hc/article_attachments/4404889447575/rpt_lsn4_mark.gif)
9. Select **Item 1** in the Mark Items box, and apply **upward****triangle**  to it in the same way.
10. Select **OK** in the Format Legend dialog to apply these changes.
11. Right-click the chart and then select **Format Axes** > **Format Value (Y) Axis** from the shortcut menu.
12. In the Format tab of the Format Value (Y) Axis dialog, select **$#,##0** in the Number category, and then select **Add**.

    ![Format Y Axis](https://devnet.logianalytics.com/hc/article_attachments/4404889447831/rpt_lsn4_fmtaxis.gif)
13. Select **OK** in the Format Value (Y) Axis dialog.
14. Double-click the **Regions** label. In the Format Label dialog, switch to the **Font** tab, specify Font as **Arial** and Font Size to **10 pt** , and then select **OK**.
15. On the report tab bar, right-click the report tab and select **Rename** to rename it to **AnnualSales**.

    ![Rename Report Tab](https://devnet.logianalytics.com/hc/article_attachments/4404894024471/renmrpttb.gif)
16. Select **File** > **Save** to save the report as **AnnualSalesbyRegion.cls**.
17. Select the **View** tab to preview the report and it looks somewhat as follows. We can easily compare the sales per region over a two-year period.

    ![Preview Report](https://devnet.logianalytics.com/hc/article_attachments/4404894034967/rpt_lsn4_chart.gif)

    **Note:** If the report does not look correct, you can compare it to the final version of the report provided by Logi JReport. To do so, you will need to save and close this catalog and then open the JinfonetGourmetJava.cat catalog file located at `<install_root>\Demo\Reports\TutorialReports`.

## Task 3: Export the Report to an Excel File

Now we can export the report to different formats as required. The sales manager requies an Excel file for the report so we will export it to the Excel format.

1. Select **File** > **Export** > **To Excel**.
2. In the Export to Excel dialog, keep the default settings and select **OK**.

   ![Export to Excel](https://devnet.logianalytics.com/hc/article_attachments/4404894035223/rpt_lsn4_expt.gif)
3. Open the file **AnnualSalesbyRegion\_AnnualSales.xls** saved in `<install_root>\Demo\Reports\JinfonetGourmetJava`. It appears as follows:

   ![Excel Report Result](https://devnet.logianalytics.com/hc/article_attachments/4404889448087/rpt_lsn4_xls.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404893760791/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009582321-Lesson-3-Creating-a-Mailing-Label-Report)  [NextTopic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404893761047/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009561982-Lesson-5-Creating-a-Table-Report)
