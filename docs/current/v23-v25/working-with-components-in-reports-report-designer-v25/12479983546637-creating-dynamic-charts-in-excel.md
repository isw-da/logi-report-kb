---
title: "Creating Dynamic Charts in Excel"
id: 12479983546637
section: "Working with Components in Reports - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12479983546637-Creating-Dynamic-Charts-in-Excel
updated_at: 2026-02-25T23:50:40Z
source_host: docs-report.zendesk.com
---
# Creating Dynamic Charts in Excel

You can make data in a chart map to a single cell in Excel, then when you change the data in a cell, the corresponding change  also reflects in the chart. This kind of chart is Dynamic Chart. This topic introduces the characteristics of dynamic charts and presents an example to show how you can create a dynamic chart.

To create a dynamic chart in Excel, the chart should use the same data as a banded object or table, which you export to Excel together with the chart. That is to say, each data value in the chart must correspond to a value in the banded object or table. Moreover, you should select the Report Format option when exporting the report to Excel.

To make a chart have the same data with a banded object or table, the chart must meet the following conditions:

- When the chart inherits data from the banded object or table,
- The chart should have the same group structure as that of the banded object or table. For example, a banded object has two groups: group 1 and group 2 (group 1 is the higher level)
- When you insert the chart  into the banded header panel,
- Add the summary 2 based on group 2 to the value axis, Designer then adds group 2 to the category axis automatically, and you need to add group 1 to the series axis manually.

- Add the summary 1 based on group 1 to the value axis, Designer then adds group 1  to the category axis automatically, and you do not need to add  any value to the series axis.

- When you insert the chart  into the group header panel 1 which displays group 1, you can only add summary 2 based on group 2 to the value axis. Designer then add group 2 to the category axis, and you do not need to add any value to the series axis. 

- When you insert the chart into the group header panel 2 which displays group 2, the value axis cannot contain any summary value. 

- Different conditions apply to the chart based on only detail records and chart containing summary information.
- The former does not contain summary value on the value axis, but DBFields. The DBFields on the value axis and the value on the category axis must be in the detail panel of the banded object or table, and should not be hidden. 

- The latter contains summary value on the value axis, and the summary on the value axis must be in the banded object or table, and should not be hidden.

- When the chart does not inherit data from the banded object or table,
- The chart should use the same dataset as the banded object or table.

- The chart should have the same group structure as that of the banded object or table.

- The chart should have the same filter/sort condition, Top N condition, and special function as that of the banded object or table.

- The chart can only be in the banded header/footer panel or outside the banded object.

- Different conditions apply to chart based on only detail records and chart containing summary information.
- For a chart based on only detail records,
            
- DBFields on the value axis must be in the detail panel of the banded object or table, and should not be hidden. 

- The category value must be in the detail panel of the banded object or table, and should not be hidden. 

- If the chart, banded object, or table has a Top N condition, the chart is not mapped to the banded object or table.

- For a chart containing summary information, the summary on the value axis must be in the banded object or table, and should not be hidden.

The following example shows how to use the Dynamic Chart feature in Excel. Here the chart inherits the dataset from its parent banded object.

- Make sure SampleReports.cat is the currently open catalog file. If not, navigate to File > Open Catalog to open it from <install_root>\Demo\Reports\SampleReports.

- 
Create a query named Products in Data Source 1 of the catalog, which contains the Products table with all of its columns.  
  

- Navigate to File > New > Page Report to 
 create a page report with a banded object in its first report tab.  
  

- 
Define the banded object as follows:
    
- Use the query Products in Data Source 1 of the catalog.

- Display  these detail fields: Product ID, Product Name, and Price.

- Group it by Category and Product Type Name (Category is the higher level).

- Apply the Classic style.

- In the Data panel of the main window, select <New Summary...> in the Summaries node.

- 
Create the summary Sum_Price which uses the aggregate function Sum, summarizes on the field Price in the Products table, and applies to the Product Type Name group level.

- Drag the summary to the footer panel of the Product Type Name group in the banded object.
    

- Select the banded header panel (BH) and insert a Clustered Bar 2-D chart in it. The chart inherits the dataset from the banded object (make sure to select Current Dataset in the Data screen of the Create Chart dialog box), and shows Product Type Name on the category axis, Category on the series axis, and Sum_Price on the value axis.
    

- Right-click the chart and select Chart Wizard from the shortcut menu.

- In the Chart Wizard dialog box, switch to the Layout screen, select Export in the Options box and then select Banded Object from the Mapping Component drop-down list. Select Finish to accept the change. 
    

- Navigate to File > Options. In the Options dialog box, select Check the availability of dynamic chart for Excel in the General category, then select OK. Designer provides this option to help you check if a chart can be correctly mapped to a banded object when you save the report or export it to Excel.

- Navigate to File > Export > To Excel to export the report to Excel (make sure to select Report Format in the Export to Excel dialog box).
    

- Open the output file in <install_root>\Demo\Reports\SampleReports.
    

- Change the price of Gold Coast Blend and Colombia El Tambo to 30.00. The value of the chart changes accordingly. 
    

- You cannot make charts of Bubble, Stock, and Scatter types to be dynamic charts if they have summary value on the value axis.

- You cannot insert the chart and the summary used in the chart  into the repeated panel of the banded object or table.

- For summary chart, Designer can only map the value axis to each single cell in Excel, meaning, when you change the data in Excel, the corresponding value axis also changes.
