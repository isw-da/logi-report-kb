---
title: "Lesson 4: Creating a Chart Report"
id: 4405664328087
section: "Logi Report Tutorial v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664328087-Lesson-4-Creating-a-Chart-Report
updated_at: 2022-01-27T20:34:08Z
---

# Lesson 4: Creating a Chart Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556073751/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661268247-Lesson-3-Creating-a-Mailing-Label-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420542052759/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664328983-Lesson-5-Creating-a-Table-Report)

# Lesson 4: Creating a Chart Report

The fourth quarter of the year has just ended, and the sales manager asked you to produce a chart that shows product annual sales for each sales region. He wants to compare the historical sales data with the current data. Here is a sketch of the report that the sales manager has given to you, a bar chart:

![Report Sketch](https://devnet.logianalytics.com/hc/article_attachments/4420542295191/rpt_lsn4_sketch.gif)

Logi Report supports more than 10 general chart types, and most of them have many subtypes or variations. After showing the sales manager the available bar chart types, he chose the 2-dimensional clustered bar chart.

Additionally, the sales manager requests that the report should be provided in Microsoft Excel file. This is not a problem, because you can export all predefined reports in Logi Report to HTML, PDF, Excel, RTF, XML, Text, Postscript, Mail, and Fax.

Follow these tasks to create the report:

* [Task 1: Create the Chart](#Task1)
* [Task 2: Format the Chart](#Task2)
* [Task 3: Export the Report to Excel](#Task3)

## Task 1: Create the Chart

1. In Designer, navigate to **File** > **New** > **Page Report**.
2. In the Select Component for Page Report dialog box, keep the default component type **Chart** and select **OK**.

   Be sure that JinfonetGourmetJava.cat is the current catalog because it is the catalog we use in this track. For information about specifying this catalog, see [Task 1, Step 2 and 3](https://devnet.logianalytics.com/hc/en-us/articles/4405664326167-Lesson-1-Creating-a-Standard-Banded-Report#SelectCat) of Lesson 1.
3. In the **Data** screen of the Chart Wizard dialog box, select the query **AnnualSalesbyRegion** from the Queries node of Data Source 1 and then select **Next**.
4. In the **Type** screen, keep the default chart type **Clustered Bar 2-D**, then select **Next**.

In this chart, we want to display the region name on the category (X) axis, and annual sales of each region on the value (Y) axis. However, as the region names are too long to display completely on the category axis, we want to create a formula here to just get the abbreviations of the region names.

1. In the **Display** screen, scroll down to the **Formulas** node in the **Resources** box, and then select **<New Formula...>**.
2. Type the formula name **Region\_AbbreviationName** in the Enter Formula Name dialog box and select **OK**, then define the formula in the Formula Editor dialog box as follows (you can copy the formula to the formula editing area directly), select **Save** on the toolbar to save the formula, and close the editor.

   ```
   if (@Customers_REGION == "Asia-Pacific")  
       "APAC"  
   else if (@Customers_REGION == "Europe, Middle East, Africa")  
       "EMEA"  
   else if (@Customers_REGION == "Latin America")  
       "LATAM"  
   else if (@Customers_REGION == "North America")  
       "NA"
   ```
3. Drag the formula **Region\_AbbreviationName** from the Resources box to the **X-Axis** box and **YearofOrderDate** to the **Clustering** box. In the Show Values box, a numerical value is required.

In this lesson, we want to show the annual sales of each region, so we need a summary which calculates data of the Annual Sales column based on Region\_AbbreviationName.

1. Select **<New Summary...>** under the Summaries node in the Resources box of the Display screen.
2. In the New Summary dialog box, specify the aggregate function as **Sum**, add the field **Annual Sales** from the Customers table to the **Summary On** text box, specify the **Group By** field as the **Region\_AbbreviationName** formula, then select **OK**.

   ![New Summary](https://devnet.logianalytics.com/hc/article_attachments/4420542295575/rpt_lsn4_sum.gif)
3. Type **Sum\_AnnualSalesbyRegion\_AbbreviationName** in the Enter Summary Name dialog box and select **OK** to create the summary.
4. Select the newly-created summary and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420542285335/btn_addarw.gif) beside the **Bar Length** box.

   ![Chart Display Fields](https://devnet.logianalytics.com/hc/article_attachments/4420542295959/rpt_lsn4_dsply.gif)

Next, we use the Layout screen of the Chart Wizard dialog box to add titles to the chart. The Layout screen provides options for customizing the layout of a chart, for example, you can hide some chart elements such as the legend and wall, set the offset of the category and series axes, and so on.

1. Select **Layout** on the screen navigation bar to switch to the screen, select **Title** from the **Options** box, and then type **Annual Sales by Region** in the **Chart Title** text box and **Regions** in **Category (X) Axis Title**.

   ![Edit Chart Titles](https://devnet.logianalytics.com/hc/article_attachments/4420542296343/rpt_lsn4_layout.gif)

Designer provides a set of CSS styles that you can apply to your reports to easily change the format and appearance of the reports.

1. Select **Next** to go to the **Style** screen and select **Classic** from the style list.
2. Select **Finish** to create the chart report and the report shows as follows in the design view.

   ![Report in Design View](https://devnet.logianalytics.com/hc/article_attachments/4420542296599/rpt_lsn4_dsgn.gif)
3. Select the **View** tab to view this chart.

   ![Preview Report Draft](https://devnet.logianalytics.com/hc/article_attachments/4420551100951/rpt_lsn4_vw.gif)

## Task 2: Format the Chart

The chart is accurate, but a little simple. We can polish to it by setting some chart properties. For each part of the chart object, such as the axes, legend, and wall, Designer provides a corresponding format dialog box, with which we can easily edit properties of a chart.

1. Select the **Design** tab to return to design mode to do the adjustments.
2. Double-click a bar of the chart. Designer displays the Format Bar dialog box.
3. In the **General** tab of the dialog box, set the **Use Depth** option to **true**. Keep the defaults for **Depth** and **Direction**.

   In the Format Bar dialog box, you can also choose another subtype for the chart in the Layout box if you want. In this lesson, we continue using Clustered - 2D.

   ![Format Bar](https://devnet.logianalytics.com/hc/article_attachments/4420556353943/rpt_lsn4_fmtbar.gif)
4. Switch to the **Data Label** tab, specify **Font Size** to **10 pt**.

   The data labels on a chart can be either static or dynamic. You can select Show Static Data Label and customize their position, so that the labels can display statically on the chart. In this lesson, we just use the labels as dynamic ones, meaning, they display when we point to the bars.

   ![Format Data Label](https://devnet.logianalytics.com/hc/article_attachments/4420556354327/rpt_lsn4_dtlbl.gif)
5. Select **OK** to apply these property settings to bars of the chart.
6. Right-click the legend and then select **Format Legend** from the shortcut menu.
7. In the Format Legend dialog box, select the **Font** tab, set **Font Size** to **10 pt**.
8. Switch to the **Mark** tab, keep **Item 0** selected in the **Mark Items** box, and select **circle** from the mark drop-down list.

   ![Format Legend Mark](https://devnet.logianalytics.com/hc/article_attachments/4420551101463/rpt_lsn4_mark.gif)
9. Select **Item 1** in the Mark Items box, and apply **upward triangle** to it in the same way.
10. Select **OK** in the Format Legend dialog box to apply these changes.
11. Right-click the chart and then navigate to **Format Axes** > **Format Value (Y) Axis** on the shortcut menu.
12. In the **Format** tab of the Format Value (Y) Axis dialog box, select **$#,##0** in the **Number** category, and then select **Add**.

    ![Format Y Axis](https://devnet.logianalytics.com/hc/article_attachments/4420542297111/rpt_lsn4_fmtaxis.gif)
13. Select **OK** in the Format Value (Y) Axis dialog box.
14. On the report tab bar, right-click the report tab and select **Rename** to rename it to **AnnualSales**.

    ![Rename Report Tab](https://devnet.logianalytics.com/hc/article_attachments/4420551091351/renmrpttb.gif)
15. Navigate to **File** > **Save** to save the report as **AnnualSalesbyRegion.cls**.
16. Select the **View** tab to preview the report and it looks somewhat as follows. We can easily compare the sales per region over a two-year period.

    ![Preview Report](https://devnet.logianalytics.com/hc/article_attachments/4420556354839/rpt_lsn4_chart.gif)

    ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) If the report does not look correct, you can compare it to the final version of the report included in Designer. To do this, save and close your current catalog, and then open the **JinfonetGourmetJava.cat** catalog file in `<install_root>\Demo\Reports\TutorialReports`.

## Task 3: Export the Report to Excel

Now we can export the report to different formats. The sales manager requies an Excel file for the report so we export it to Excel.

1. Navigate to **File** > **Export** > **To Excel**.
2. In the Export to Excel dialog box, keep the default settings and select **OK**.

   ![Export to Excel](https://devnet.logianalytics.com/hc/article_attachments/4420542297751/rpt_lsn4_expt.gif)
3. Open the file **AnnualSalesbyRegion\_AnnualSales.xls** in `<install_root>\Demo\Reports\JinfonetGourmetJava`.

   ![Excel Report Result](https://devnet.logianalytics.com/hc/article_attachments/4420556355735/rpt_lsn4_xls.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556073751/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661268247-Lesson-3-Creating-a-Mailing-Label-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420542052759/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664328983-Lesson-5-Creating-a-Table-Report)
