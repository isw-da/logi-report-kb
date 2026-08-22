---
title: "Lesson 4: Creating a Chart Report"
id: 45190390876813
section: "Report Tutorial"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190390876813-Lesson-4-Creating-a-Chart-Report
updated_at: 2026-04-30T15:11:44Z
source_host: logi-report-v26.insightsoftware.com
---
# Lesson 4: Creating a Chart Report

The fourth quarter of the year has just ended, and the sales manager asked you to produce a chart that shows product annual sales for each sales region. He wants to compare the historical sales data with the current data. Here is a sketch of the report that the sales manager has given to you, a bar chart:

Report supports more than 10 general chart types, and most of them have many subtypes or variations. After showing the sales manager the available bar chart types, he chose the 2-dimensional clustered bar chart.

Additionally, the sales manager requests that the report should be provided in Microsoft Excel file. This is not a problem, because you can export all predefined reports in Report to HTML, PDF, Excel, RTF, XML, Text, Postscript, Mail, and Fax.

Follow these tasks to create the report:

- Task 1: Create the Chart

- Task 2: Format the Chart

- Task 3: Export the Report to Excel

## 
Task 1: Create the Chart

- In Designer, navigate to File > New > Page Report. Be sure that JinfonetGourmetJava.cat is the current catalog because this is the catalog we use in this track. For information about specifying this catalog, see Task 1, Steps 3 and 4 of Lesson 1.    

- In the Select Component for Page Report dialog box, keep the default component type Chart and select OK.
    

- In the Data screen of the Chart Wizard dialog box, select the query AnnualSalesbyRegion from the Queries node of Data Source 1 and then select Next.

- In the Type screen, keep the default chart type Clustered Bar 2-D, then select Next.

In this chart, we want to display the region name on the category (X) axis, and annual sales of each region on the value (Y) axis. However, as the region names are too long to display completely on the category axis, we want to create a formula here to just get the abbreviations of the region names.

- In the Display screen, scroll down to the Formulas node in the Resources box, and then select <New Formula...>.

-  Type the formula name Region_AbbreviationName  in the Enter Formula Name dialog box and select OK, then define the formula in the Formula Editor dialog box as follows (you can copy the formula to the formula editing area directly), select Save on the toolbar to save the formula, and close the editor.
    

if (@Customers_REGION == "Asia-Pacific")
    "APAC"
else if (@Customers_REGION == "Europe, Middle East, Africa")
    "EMEA"
else if (@Customers_REGION == "Latin America")
    "LATAM"
else if (@Customers_REGION == "North America")
    "NA"

- Drag the formula Region_AbbreviationName from the Resources box to the X-Axis box and  YearofOrderDate to the Clustering box. In the Show Values box, a numerical value is required.

In this lesson, we want to show the annual sales of each region, so we need a summary that calculates data of the Annual Sales column based on  Region_AbbreviationName.

- Select <New Summary...> under the Summaries node in the Resources box of the Display screen.

- In the New Summary dialog box, specify the aggregate function as Sum, add the field Annual Sales from the Customers table to the Summary On text box, specify the Group By field as the Region_AbbreviationName formula, then select OK.
    

-  Type Sum_AnnualSalesbyRegion_AbbreviationName in the Enter Summary Name dialog box and select OK to create the summary.

- Select the newly-created summary and select Add beside the Bar Length box. 

Next, we use the Layout screen of the Chart Wizard dialog box to add titles to the chart. The Layout screen provides options for customizing the layout of a chart, for example, you can specify the offset of the category and series values, customize titles of the chart axes, and hide some chart elements such as the legend and wall. 

- Select Layout on the screen navigation bar to switch to the screen, select Title from the Options box, and then type Annual Sales by Region in the Chart Title text box and Regions in Category (X) Axis Title.
    

Designer provides a set of CSS styles that you can apply to your reports to easily change the format and appearance of the reports.

- Select Next to go to the Style screen and select Classic from the style list.

- Select Finish to create the chart report. The report shows as follows in design view. 

- Select the View tab to view this chart.

 

## 
Task 2: Format the Chart

The chart is accurate, but a little simple. We can polish to it by setting some chart properties. For each part of the chart object, such as the axes, legend, and wall, Designer provides a corresponding format dialog box, with which we can easily edit properties of a chart.

- Select the Design tab to return to design mode to do the adjustments.

- Double-click a bar of the chart. Designer displays the Format Bar dialog box.

- In the General tab of the dialog box, set the Use Depth option to true. Keep the defaults for Depth and Direction.
    In the Format Bar dialog box, you can also choose another subtype for the chart in the Layout box if you want. In this lesson, we continue using Clustered - 2D.

- Switch to the Data Label tab, specify Font Size to 10 pt. 
    The data labels on a chart can be either static or dynamic. You can select Show Static Data Label and customize their position, so that the labels can display statically on the chart. In this lesson, we just use the labels as dynamic ones, meaning, they display when we point to the bars.

- Select OK to apply these property settings to bars of the chart.

- Right-click the legend and then select Format Legend from the shortcut menu.

- In the Format Legend dialog box, select the Font tab, set Font Size to 10 pt.

- Switch to the Mark tab, keep Item 0 selected in the Mark Items box, and select circle from the mark drop-down list.
    

- Select Item 1 in the Mark Items box, and apply upward triangle to it in the same way. 

- Select OK in the Format Legend dialog box to apply these changes.

- Right-click the chart and then navigate to Format Axes > Format Value (Y) Axis on the shortcut menu.

- In the Format tab of the Format Value (Y) Axis dialog box, select  $#,##0 in the Number category, and then select Add.
    

- Select OK in the Format Value (Y) Axis dialog box.

- On the report tab bar, right-click the report tab and select Rename to rename it to AnnualSales.
    

- Navigate to File > Save to save the report as AnnualSalesbyRegion.cls.

- Select the View tab to preview the report and it looks somewhat as follows. We can easily compare the sales per region over a two-year period. 
    

 If the report does not look correct, you can compare it to the final version of the report included in Designer. To do this, save and close your current catalog, and then open the JinfonetGourmetJava.cat catalog file in <install_root>\Demo\Reports\TutorialReports.    

 

## 
Task 3: Export the Report to Excel

Now we can export the report to different formats. The sales manager requies an Excel file for the report so we export it to Excel.

- Navigate to File > Export > To Excel.

- In the Export to Excel dialog box, keep the default settings and select OK.
    

- Open the file AnnualSalesbyRegion_AnnualSales.xls in <install_root>\Demo\Reports\JinfonetGourmetJava.
