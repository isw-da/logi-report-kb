---
title: "Working with KPIs"
id: 12480003049485
section: "Working with Components in Reports - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480003049485-Working-with-KPIs
updated_at: 2026-02-25T23:50:28Z
source_host: docs-report.zendesk.com
---
# 
Working with KPIs

A KPI (Key Performance Indicator) is a data container based on a business view for displaying KPI value together with a chart to help illustrate the value. This topic introduces what objects a KPI can contain and how you can create KPIs in a report.

 You cannot use KPIs in page reports. 

This topic contains the following sections:

- Objects in a KPI

- Inserting KPIs in a Report

- Example: Creating a KPI

## 
Objects in a KPI

You can add the following objects in a KPI: 

- Aggregations and formulas as the KPI values.

- Labels to describe the values and as the KPI title or description.

- Images to decorate the KPI or used as logo.

- A KPI chart to assist the KPI values, for example, to show the trend of total sales over time. You can include at most one KPI chart  in a KPI. A KPI chart does not have the legend and axes compared to normal Report charts. You can insert a KPI chart in a KPI only and the KPI chart should inherit the dataset from the KPI. A KPI chart can be one of the following 2-D chart types: Bar, Bench, Line, Area, Pie, and Bullet.

A KPI is bound with a dataset created on a business view and the KPI value and KPI chart in it are both based on this dataset. You can position and resize the objects in a KPI  freely by dragging them inside the KPI.

## 
Inserting KPIs in a Report

- Position the mouse pointer at the allowed report location where you want to insert the KPI.
				

- Do one of the following:
    
- From the Components panel, drag the KPI icon  in the Visual category to the destination.

- Navigate to Insert > KPI.

- Navigate to Home > Insert > KPI. 

- In the Choose Data dialog box, specify the dataset you want to bind with the KPI and select OK.    

- Designer inserts a blank KPI at the destination. You can then define the KPI by adding objects into it.
    

- Drag an aggregation or a dynamic formula from the Data panel as the KPI value. Designer adds the name label of the object at the same time by default. You can edit the label text. 

- Insert a KPI chart to demonstrate data about the KPI value.
- Right-click in the blank area of the KPI and select Insert KPI Chart from the shortcut menu. Designer displays the Create KPI Chart dialog box.

- The Data screen shows that the KPI chart inherits the dataset bound with the KPI. You cannot change the dataset.
        

- In the Type screen, select a 2-D Bar, Bench, Line, Area, Pie, or Bullet chart type.
        

- In the Display, Layout, and Style screens, define the KPI chart as you would do for a general chart.

- Select Finish to  insert the chart  into the KPI.

- You can add more aggregations, dynamic formulas, labels, and images  into the KPI.

- Resize the KPI and the objects in it and drag the objects to adjust their position in the KPI to improve the layout. 

After you create a KPI, you can further edit the objects in it. The KPI chart in a KPI supports most of the operations that you can apply to a general chart. For example, you can modify its definition using the KPI Chart Wizard dialog box, add link to its data markers, and format its paper, platform, wall, label, and data markers (bars/benches, lines, areas, pies, or bullets). If you want to remove the KPI chart, select the KPI, right-click and select Remove KPI Chart on the shortcut menu. 

## 
Example: Creating a KPI

This example uses a KPI to show total sales.

- Make sure SampleReports.cat is the currently open catalog file. If not, navigate to File > Open Catalog to open it from <install_root>\Demo\Reports\SampleReports.

- Navigate to File > New > Web Report  to create a web report. 

- Drag  from the Components panel to the destination.

- In the Choose Data dialog box, select WorldWideSalesBV in the current catalog to bind it with the KPI and select OK. Designer inserts a blank KPI  at the destination.

- In the Data panel, create a dynamic formula in the name KPI_TotalSales with the following expression. Use it as Aggregation.
    if (@"Orders Detail.Total Sales">=1000000)
    ToText(@"Orders Detail.Total Sales"/1000000, "$#,###.00")+"M"
else if (@"Orders Detail.Total Sales">=1000)
    ToText(@"Orders Detail.Total Sales"/1000, "$#,###.00")+"K"
else
     ToText(@"Orders Detail.Total Sales", "$#,###.00")

- Drag the formula from the Data panel to the KPI as the KPI value. 

- Right-click in the blank area of the KPI and select Insert KPI Chart from the shortcut menu.

- In the Create KPI Chart dialog box, go to the Display screen, add the group object Sales Quarter to the category axis, the aggregation object Total Sales to the value axis, then select Finish to insert the KPI chart.
    

- Adjust the position of the objects in the KPI.

- Select the View tab to preview the real data.
