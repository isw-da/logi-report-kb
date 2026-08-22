---
title: "Lesson 7: Creating a Tabular Report"
id: 12491064837645
section: "Report Tutorial v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12491064837645-Lesson-7-Creating-a-Tabular-Report
updated_at: 2025-05-30T02:58:15Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# Lesson 7: Creating a Tabular Report

A report about performance of products is needed, in which the product ID is less than or equals to 10. The report includes annual sales of every product in every region, their unit price, the quantities that are sold, and the total of their annual sales of every product. The report should contain a crosstab, which is to represent annual sales of ten products in every region, a chart object, which is to represent quantities and total annual sales of these specified products, and a banded object, which is to represent the unit price and quantities.

Here is a sketch of the report that you can refer to:

In this lesson, we create a tabular report and insert a crosstab, chart, and banded object respectively into different tabular cells, so that we can arrange the components in the report easily with the tabular layout. The JinfonetGourmetJava.cat catalog contains all the data resources we need for creating the report, so in this lesson we do not need to create them ourselves. 

Follow these tasks to create the report::

- Task 1: Create the Tabular Report

- Task 2: Add Components to the Tabular Report

- Task 3: Format the Report

## 
Task 1: Create the Tabular Report

- In Designer, navigate to File > New > Page Report. Be sure that JinfonetGourmetJava.cat is the current catalog because this is the catalog we use in this track. For information about specifying this catalog, see Task 1, Steps 3 and 4 of Lesson 1.    

- In the Select Component for Page Report dialog box, select Tabular and select OK.
    

- In the Tabular Wizard dialog box, keep the default settings and select Finish to create a 2*2 tabular.
    

- Designer displays a message dialog box prompting you to drag data fields and components to the blank report. Select OK in the message dialog box to close it.

Now a blank report with a 2*2 tabular is generated. In the Report Inspector, they are respectively named TabularCell and TabularCell1 (the two cells in the first row of the tabular); TabularCell2 and TabularCell3 (the two cells in the second row of the tabular). We can then insert different components into the cells, so that we can align them easily just by adjusting the tabular cells.

The tabular fills the whole page panel, we can resize it by just dragging its cell borders. In this lesson, in order to make screen captures, we zoom out the tabular first.

## 
Task 2: Add Components to the Tabular Report

Before taking this task, make sure you have enabled the "Insert field name label with field" option in the Options dialog box as described at the last step of Lesson 3; otherwise, Designer does not insert the name labels together with the fields when you add fields to the report.

In this task, we add three components - a crosstab, a chart, and a banded object respectively to TabularCell, TabularCell2, and TabularCell3 and have them share the same dataset. Sharing dataset in the same report  can greatly improve the report performance in the runtime environment. This is because Report Engine creates each dataset by running a query against the database, and that is the most expensive part of running a report in terms of execution time. Even when two datasets are based on the same data resource, Report Engine still runs the query separately for each dataset. 

- Select the two cells in the first row of the tabular (TabularCell and TabularCell1), then right-click and select Merge from the shortcut menu.

- Select the merged tabular cell and navigate to Insert > Crosstab. Designer displays the Create Crosstab dialog box.

- In the Data screen, select the query ProductPerformance from the Queries node of Data Source 1, then select Next.

- In the Display screen, drag Products_Product ID from the Resources box to the Columns box, drag the formula Region_AbbreviationName to the Rows box, and drag the formula Total to the Summaries box, then double-click in the Aggregate text box and select Sum from the drop-down list as the aggregate function of the summary.
    

- Select Style on the screen navigation bar to switch to the screen and apply the Classic style to the crosstab, then select  Finish to close the Create Crosstab dialog box and place the crosstab in the first tabular cell row.
    

Next, we insert the chart object to TabularCell2.

- Select the left cell in the second row of the tabular (TabularCell2) and navigate to Insert > Chart.

- In the Data screen of the Create Chart dialog box, select More Options, then select Existing Dataset and select the dataset ProductPerformance. Select Next.
    

- In the Type screen, select the Bubble in the Chart Type box and select Next.

- In the Display screen, select the Y Axis node in the Color box, drag  the summary Count_QuantitybyProductID from the Resources box to it, then select the Radius node and drag Sum_ProductSalesbyProductID to it. The summaries are grouped by the DBField ProductID_FK1 so Designer adds the field to the Bubble box automatically. Leave the Series box empty.
    

- Select Layout to switch to the screen, select Title in the Options box, then specify Category (X) Axis Title as Product ID, and Value (Y) Axis Title as Quantity. Select Next. 

- In the Style screen, select the Classic style.

- Select Finish to close the Create Chart dialog box and place the chart in TabularCell2.

Next, we insert the banded object to TabularCell3.

- Select TabularCell3 (the right cell in the second row of the tabular) and navigate to Insert > Banded Object. Designer displays the Create Banded Object dialog box.

- In the Data screen, select More Options, then select Existing Dataset and select the dataset ProductPerformance.

- Select Group to switch to the screen, select the DBField ProductID_FK1 and select Add to add it as the group-by field.

- Go to the Style screen and select the Classic style for the banded object.

- Select Finish to close the Create Banded Object dialog box and then select in TabularCell3 to place the banded object in it.
              Designer identifies the panels in the banded object  on the left side by their abbreviations: a banded header panel (BH), a banded page header panel (BPH), a group header panel (GH), a detail panel (DT), a group footer panel (GF), a banded page footer panel (BPF), and a banded footer panel (BF).

The three data components now display as follows in the tabular.

- Drag the Label icon  from the Components panel to the BPH panel in the banded object, above the group-by field in the GH panel to label the field, then double-click the label and edit its text to 
  Product ID.

- Drag the DBField Unit Price and the summary Count_QuantitybyProductID from the Data panel to the GH panel,  then move their name labels  to the BPH panel.

- Adjust the position of the added field and summary and their name labels to align them side by side in the GH and BPH panels.

- Select the label Count_QuantitybyProductID, then in the Report Inspector, set its Auto Map Field Name property to false and Text property to Quantity.

- Select the Unit Price and Quantity labels, set their Bold property to true and Foreground property to White in the Report Inspector. 

- Right-click in the BH panel and select Hide from the shortcut menu to hide it from view. Repeat this to hide all panels that do not hold data.
    

Next, we need a report title for the tabular report to make the report look professional.

- Right-click the tabular cell that holds the crosstab, and select Insert Row Above from the shortcut menu, then resize the row to a suitable height.

- Double-click the newly-created tabular row, and type the text Product Performance by Product ID as the report title.

As required, the report only needs to show the products performance from the Product ID 1 to 10, so next we use the Dataset Filter feature to limit data selected from the dataset. Since all data components in the report share the same dataset, Designer applies the filter to them all. 

- Select Dataset Filter on the toolbar of the Data panel. 

- In the Dataset Filter dialog box, select Add Condition to add a filter line, select PRODUCTID_FK1 from the field drop-down list, <= from the operator drop-down list, and type 10 in the value text box to specify the filter condition as "PRODUCTID_FK1 <= 10". Select OK.
    

## 
Task 3: Format the Report

To improve the report appearance, we need to do some adjustments to the report and the components in it.

- Resize the tabular cells according to the components' sizes in every cell, so that they are not truncated by the tabular and can display well. 

Next, we further format to improve the appearances of the components. First, we format the report title and the crosstab. 

- Select the text Product Performance by Product ID, right-click on it and select Font from the shortcut menu.

- In the Font tab of the Format Text dialog box, set Font Size to 18, Font Color to Red and Bold to true, then select OK. 

- Select the four DBFields in the summary area of the crosstab, then in the Report Inspector, specify the Height property to 0.25, Width to 0.59, and Format to #,###.#.
    

Next, let's format the chart. 

- Double-click the label Quantity in the chart, then in the Format Label dialog box, switch to the Font tab, set Font Color to 808080. Select OK to accept the settings. 
    

- Use the same way to format the label Product ID in the chart.

- Right-click the chart and select Hide Legend on the shortcut menu to hide the legend.

Now, we format the banded object. 

- Select the Product ID name label in the BPH panel and its corresponding field in the GH panel, then navigate to Format > Right to align them the same as other labels and fields in the banded object.

- Select the three DBFields in the GH pane, then in the Report Inspector, set their Foreground property to Black.

- Select the Unit Price DBField and specify its Format property to $#,###.00 in the Report Inspector.
    

After doing the adjustments, Designer displays the report like follows in design view:

According to the sketch, a line needs to be added below the report title. We can do this just by setting tabular cell properties.

- Select the tabular cell holding the report title, then in the Report Inspector, specify its Top Line, Left Line, and Right Line properties to none, Border Color to Gray and Border Thickness to 0.01.

When viewing the report, the crosstab object displays much closer to the line we just customized and the other two components look too clumsy. We need to do some adjustments, which we can achieve easily by using features of a tabular.

- Right-click the tabular cell holding the crosstab, and then select Insert Row Above  from the shortcut menu. Right-click the cell again and select Insert Row Below.
    Designer then adds two rows above and below the crosstab.

- Resize the tabular rows to adjust the distances between the crosstab and the other components.

- On the report tab bar, right-click the report tab and select Rename to rename it to  ProductPerformance.
    

- Navigate to File > Save to save the report as ProductPerformancebyProductID.cls.

- Select the View tab. Designer displays the report as follows, depending on what formatting you have done to the components.
    

 If the report does not look correct, you can compare it to the final version of the report included in Designer. To do this, save and close your current catalog, and then open the JinfonetGourmetJava.cat catalog file in <install_root>\Demo\Reports\TutorialReports.    

Previous Topic  Next Topic
