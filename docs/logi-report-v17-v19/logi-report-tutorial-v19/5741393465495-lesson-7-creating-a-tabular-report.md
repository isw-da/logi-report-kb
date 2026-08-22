---
title: "Lesson 7: Creating a Tabular Report"
id: 5741393465495
section: "Logi Report Tutorial v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741393465495-Lesson-7-Creating-a-Tabular-Report
updated_at: 2022-11-30T02:36:32Z
---

# Lesson 7: Creating a Tabular Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905613813911/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741398819607-Lesson-6-Creating-a-Crosstab-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905613870871/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741406798103-Lesson-8-Creating-a-Report-That-Contains-a-Subreport)

# Lesson 7: Creating a Tabular Report

A report about performance of products is needed, in which the product ID is less than or equals to 10. The report includes annual sales of every product in every region, their unit price, the quantities that are sold, and the total of their annual sales of every product. The report should contain a crosstab, which is to represent annual sales of ten products in every region, a chart object, which is to represent quantities and total annual sales of these specified products, and a banded object, which is to represent the unit price and quantities.

Here is a sketch of the report that you can refer to:

![Report Sketch](https://devnet.logianalytics.com/hc/article_attachments/9905897586071/rpt_lsn7_sketch.gif)

In this lesson, we create a tabular report and insert a crosstab, chart, and banded object respectively into different tabular cells, so that we can arrange the components in the report easily with the tabular layout. The JinfonetGourmetJava.cat catalog contains all the data resources we need for creating the report, so in this lesson we do not need to create them ourselves.

Follow these tasks to create the report::

* [Task 1: Create the Tabular Report](#Task1)
* [Task 2: Add Components to the Tabular Report](#Task2)
* [Task 3: Format the Report](#Task3)

## Task 1: Create the Tabular Report

1. In Designer, navigate to **File** > **New** > **Page Report**.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) Be sure that JinfonetGourmetJava.cat is the current catalog because this is the catalog we use in this track. For information about specifying this catalog, see [Task 1, Steps 3 and 4](https://devnet.logianalytics.com/hc/en-us/articles/5741398712727-Lesson-1-Creating-a-Standard-Banded-Report#SelectCat) of Lesson 1.
2. In the Select Component for Page Report dialog box, select **Tabular** and select **OK**.
3. In the Tabular Wizard dialog box, keep the default settings and select **Finish** to create a 2\*2 tabular.

   ![Tabular Wizard](https://devnet.logianalytics.com/hc/article_attachments/9905875836695/rpt_lsn7_tblr.gif)
4. Designer displays a message dialog box prompting you to drag data fields and components to the blank report. Select **OK** in the message dialog box to close it.

Now a blank report with a 2\*2 tabular is generated. In the Report Inspector, they are respectively named TabularCell and TabularCell1 (the two cells in the first row of the tabular); TabularCell2 and TabularCell3 (the two cells in the second row of the tabular). We can then insert different components into the cells, so that we can align them easily just by adjusting the tabular cells.

The tabular fills the whole page panel, we can resize it by just dragging its cell borders. In this lesson, in order to make screen captures, we zoom out the tabular first.

## Task 2: Add Components to the Tabular Report

Before taking this task, make sure you have enabled the "Insert field name label with field" option in the Options dialog box as [described at the last step of Lesson 3](https://devnet.logianalytics.com/hc/en-us/articles/5741384902295-Lesson-3-Creating-a-Mailing-Label-Report#Options); otherwise, Designer does not insert the name labels together with the fields when you add fields to the report.

In this task, we add three components - a crosstab, a chart, and a banded object respectively to TabularCell, TabularCell2, and TabularCell3 and have them share the same dataset. Sharing dataset in the same report can greatly improve the report performance in the runtime environment. This is because Logi Report Engine creates each dataset by running a query against the database, and that is the most expensive part of running a report in terms of execution time. Even when two datasets are based on the same data resource, Logi Report Engine still runs the query separately for each dataset.

1. Select the two cells in the first row of the tabular (TabularCell and TabularCell1), then right-click and select **Merge** from the shortcut menu.
2. Select the merged tabular cell and navigate to **Insert** > **Crosstab**. Designer displays the Create Crosstab dialog box.
3. In the **Data** screen, select the query **ProductPerformance** from the Queries node of Data Source 1, then select **Next**.
4. In the **Display** screen, drag **Products\_Product ID** from the **Resources** box to the **Columns** box, drag the formula **Region\_AbbreviationName** to the **Rows** box, and drag the formula **Total** to the **Summaries** box, then double-click in the **Aggregate** text box and select **Sum** from the drop-down list as the aggregate function of the summary.

   ![Add Fields to Crosstab](https://devnet.logianalytics.com/hc/article_attachments/9905897656727/rpt_lsn7_crstbdsply.gif)
5. Select **Style** on the screen navigation bar to switch to the screen and apply the **Classic** style to the crosstab, then select  **Finish** to close the Create Crosstab dialog box and place the crosstab in the first tabular cell row.

   ![Insert Crosstab to Tabular Cell](https://devnet.logianalytics.com/hc/article_attachments/9905875899543/rpt_lsn7_crstb.gif)

Next, we insert the chart object to TabularCell2.

1. Select the left cell in the second row of the tabular (TabularCell2) and navigate to **Insert** > **Chart**.
2. In the **Data** screen of the Create Chart dialog box, select **More Options**, then select **Existing Dataset** and select the dataset **ProductPerformance**. Select **Next**.

   ![Select Existing Dataset](https://devnet.logianalytics.com/hc/article_attachments/9905875937431/rpt_lsn7_dtset.gif)
3. In the **Type** screen, select the **Bubble** in the **Chart Type** box and select **Next**.
4. In the **Display** screen, select the **Y Axis** node in the **Color** box, drag the summary **Count\_QuantitybyProductID** from the **Resources** box to it, then select the **Radius** node and drag **Sum\_ProductSalesbyProductID** to it. The summaries are grouped by the DBField **ProductID\_FK1** so Designer adds the field to the **Bubble** box automatically. Leave the Series box empty.

   ![Add Chart Fields](https://devnet.logianalytics.com/hc/article_attachments/9905875964183/rpt_lsn7_dsply.gif)
5. Select **Layout** to switch to the screen, select **Title** in the **Options** box, then specify **Category (X) Axis Title** as **Product ID**, and **Value (Y) Axis Title** as **Quantity**. Select **Next**.
6. In the **Style** screen, select the **Classic** style.
7. Select **Finish** to close the Create Chart dialog box and place the chart in TabularCell2.

Next, we insert the banded object to TabularCell3.

1. Select TabularCell3 (the right cell in the second row of the tabular) and navigate to **Insert** > **Banded Object**. Designer displays the Create Banded Object dialog box.
2. In the **Data** screen, select **More Options**, then select **Existing Dataset** and select the dataset **ProductPerformance**.
3. Select **Group** to switch to the screen, select the DBField **ProductID\_FK1** and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905875055127/btn_addarw.gif) to add it as the group-by field.
4. Go to the **Style** screen and select the **Classic** style for the banded object.
5. Select **Finish** to close the Create Banded Object dialog box and then select in TabularCell3 to place the banded object in it.

   Designer identifies the panels in the banded object on the left side by their abbreviations: a banded header panel (BH), a banded page header panel (BPH), a group header panel (GH), a detail panel (DT), a group footer panel (GF), a banded page footer panel (BPF), and a banded footer panel (BF).

   The three data components now display as follows in the tabular.

   ![Add Components to Report](https://devnet.logianalytics.com/hc/article_attachments/9905876011287/rpt_lsn7_cell.gif)
6. Drag the **Label** icon ![Label button](https://devnet.logianalytics.com/hc/article_attachments/9905897864599/btn_label.gif) from the **Components** panel to the BPH panel in the banded object, above the group-by field in the GH panel to label the field, then double-click the label and edit its text to
   **Product ID**.
7. Drag the DBField **Unit Price** and the summary **Count\_QuantitybyProductID** from the **Data** panel to the GH panel, then move their name labels to the BPH panel.
8. Adjust the position of the added field and summary and their name labels to align them side by side in the GH and BPH panels.
9. Select the label **Count\_QuantitybyProductID**, then in the Report Inspector, set its **Auto Map Field Name** property to **false** and **Text** property to **Quantity**.
10. Select the **Unit Price** and **Quantity** labels, set their **Bold** property to **true** and **Foreground** property to **White** in the Report Inspector.
11. Right-click in the BH panel and select **Hide** from the shortcut menu to hide it from view. Repeat this to hide all panels that do not hold data.

    ![Edit Banded Object](https://devnet.logianalytics.com/hc/article_attachments/9905897886871/rpt_lsn7_fld.gif)

Next, we need a report title for the tabular report to make the report look professional.

1. Right-click the tabular cell that holds the crosstab, and select **Insert Row Above** from the shortcut menu, then resize the row to a suitable height.
2. Double-click the newly-created tabular row, and type the text **Product Performance by Product ID** as the report title.

As required, the report only needs to show the products performance from the Product ID 1 to 10, so next we use the Dataset Filter feature to limit data selected from the dataset. Since all data components in the report share the same dataset, Designer applies the filter to them all.

1. Select **Dataset Filter**![Dataset Filter button](https://devnet.logianalytics.com/hc/article_attachments/9905874809623/btn_fltr.gif) on the toolbar of the Data panel.
2. In the Dataset Filter dialog box, select **Add Condition** to add a filter line, select **PRODUCTID\_FK1** from the field drop-down list, **<=** from the operator drop-down list, and type **10** in the value text box to specify the filter condition as "PRODUCTID\_FK1 <= 10". Select **OK**.

   ![Filter Dataset](https://devnet.logianalytics.com/hc/article_attachments/9905897936663/rpt_lsn7_fltr.gif)

## Task 3: Format the Report

To improve the report appearance, we need to do some adjustments to the report and the components in it.

1. Resize the tabular cells according to the components' sizes in every cell, so that they are not truncated by the tabular and can display well.

Next, we further format to improve the appearances of the components. First, we format the report title and the crosstab.

1. Select the text **Product Performance by Product ID**, right-click on it and select **Font** from the shortcut menu.
2. In the Font tab of the Format Text dialog box, set **Font Size** to **18**, **Font Color** to **Red** and **Bold** to **true**, then select **OK**.

   ![Format Report Title](https://devnet.logianalytics.com/hc/article_attachments/9905897956247/rpt_lsn7_title.gif)
3. Select the four DBFields in the summary area of the crosstab, then in the Report Inspector, specify the **Height** property to **0.25**, Width to **0.59**, and Format to **#,###.#**.

   ![Edit DBField Properties](https://devnet.logianalytics.com/hc/article_attachments/9905897978519/rpt_lsn7_fmtcrstb.gif)

Next, let's format the chart.

1. Double-click the label **Quantity** in the chart, then in the Format Label dialog box, switch to the **Font** tab, set **Font Color** to **808080**. Select **OK** to accept the settings.

   ![Format Chart Label](https://devnet.logianalytics.com/hc/article_attachments/9905876167959/rpt_lsn7_fmtlbl.gif)
2. Use the same way to format the label **Product ID** in the chart.
3. Right-click the chart and select **Hide Legend** on the shortcut menu to hide the legend.

Now, we format the banded object.

1. Select the **Product ID** name label in the BPH panel and its corresponding field in the GH panel, then navigate to **Format** > **Right**![Right Align button](https://devnet.logianalytics.com/hc/article_attachments/9905898027927/btn_alignright.gif) to align them the same as other labels and fields in the banded object.
2. Select the three DBFields in the GH pane, then in the Report Inspector, set their **Foreground** property to **Black**.
3. Select the **Unit Price** DBField and specify its **Format** property to **$#,###.00** in the Report Inspector.

   ![Format Banded Object](https://devnet.logianalytics.com/hc/article_attachments/9905898138775/rpt_lsn7_fmtbnd.gif)

After doing the adjustments, Designer displays the report like follows in design view:

![Report in Design View](https://devnet.logianalytics.com/hc/article_attachments/9905876246423/rpt_lsn7_dsgn.gif)

According to the sketch, a line needs to be added below the report title. We can do this just by setting tabular cell properties.

1. Select the tabular cell holding the report title, then in the Report Inspector, specify its **Top Line**, **Left Line**, and **Right Line** properties to **none**, **Border Color** to **Gray** and **Border Thickness** to **0.01**.

When viewing the report, the crosstab object displays much closer to the line we just customized and the other two components look too clumsy. We need to do some adjustments, which we can achieve easily by using features of a tabular.

1. Right-click the tabular cell holding the crosstab, and then select **Insert Row Above**  from the shortcut menu. Right-click the cell again and select **Insert Row Below**.

   Designer then adds two rows above and below the crosstab.
2. Resize the tabular rows to adjust the distances between the crosstab and the other components.
3. On the report tab bar, right-click the report tab and select **Rename** to rename it to  **ProductPerformance**.

   ![Rename Report Tab](https://devnet.logianalytics.com/hc/article_attachments/9905863488151/renmrpttb.gif)
4. Navigate to **File** > **Save** to save the report as **ProductPerformancebyProductID.cls**.
5. Select the **View** tab. Designer displays the report as follows, depending on what formatting you have done to the components.

   ![Preview Report](https://devnet.logianalytics.com/hc/article_attachments/9905876281111/rpt_lsn7_rpt.gif)

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) If the report does not look correct, you can compare it to the final version of the report included in Designer. To do this, save and close your current catalog, and then open the **JinfonetGourmetJava.cat** catalog file in `<install_root>\Demo\Reports\TutorialReports`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905613813911/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741398819607-Lesson-6-Creating-a-Crosstab-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905613870871/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741406798103-Lesson-8-Creating-a-Report-That-Contains-a-Subreport)
