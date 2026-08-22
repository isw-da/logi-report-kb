---
title: "Working with KPIs"
id: 5735507271831
section: "Working with Components in Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735507271831-Working-with-KPIs
updated_at: 2022-11-02T04:13:09Z
---

# Working with KPIs

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735521118231-Using-Shape-Maps)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735564320919-Working-with-Labels)

# Working with KPIs

A KPI (Key Performance Indicator) is a data container based on a business view for displaying KPI value together with a chart to help illustrate the value. This topic introduces what objects a KPI can contain and how you can create KPIs in a report.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) You cannot use KPIs in page reports.

This topic contains the following sections:

* [Objects in a KPI](#Object)
* [Inserting KPIs in a Report](#Insert)
* [Example: Creating a KPI](#Example)

## Objects in a KPI

You can add the following objects in a KPI:

* Aggregations and formulas as the KPI values.
* Labels to describe the values and as the KPI title or description.
* Images to decorate the KPI or used as logo.
* A KPI chart to assist the KPI values, for example, to show the trend of total sales over time. You can include at most one KPI chart in a KPI. A KPI chart does not have the legend and axes compared to normal Logi Report charts. You can insert a KPI chart in a KPI only and the KPI chart should inherit the dataset from the KPI. A KPI chart can be one of the following 2-D chart types: Bar, Bench, Line, Area, Pie, and Bullet.

A KPI is bound with a dataset created on a business view and the KPI value and KPI chart in it are both based on this dataset. You can position and resize the objects in a KPI freely by dragging them inside the KPI.

## Inserting KPIs in a Report

1. Position the mouse pointer at the [allowed report location](https://devnet.logianalytics.com/hc/en-us/articles/9898540172311-Component-Placement-in-Different-Report-Type) where you want to insert the KPI.
2. Do one of the following:
   * From the **Components** panel, drag the **KPI** icon ![KPI icon](https://devnet.logianalytics.com/hc/article_attachments/9898533135639/icon_kpi.gif) in the **Visual** category to the destination.
   * Navigate to **Insert** > **KPI**.
   * Navigate to **Home** > **Insert** > **KPI**.
3. In the [Choose Data dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565124375-Choose-Data-Dialog-Box), [specify the dataset](https://devnet.logianalytics.com/hc/en-us/articles/5735586128791-Applying-Datasets-in-a-Report#DC) you want to bind with the KPI and select **OK**.

   ![Choose Data dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898518368535/chsdt-bv.gif)
4. Designer inserts a blank KPI at the destination. You can then define the KPI by adding objects into it.

   ![Blank KPI](https://devnet.logianalytics.com/hc/article_attachments/9898518375575/cmpnt_kpi_blank.gif)
5. Drag an [aggregation](https://devnet.logianalytics.com/hc/en-us/articles/5735507390615-Working-with-Summary-Fields) or a [dynamic formula](https://devnet.logianalytics.com/hc/en-us/articles/5735507254295-Working-with-Formula-Fields) from the **Data** panel as the KPI value. Designer adds the name label of the object at the same time by default. You can edit the label text.
6. Insert a KPI chart to demonstrate data about the KPI value.
   1. Right-click in the blank area of the KPI and select **Insert KPI Chart** from the shortcut menu. Designer displays the [Create KPI Chart dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735528774039-Create-KPI-Chart-Dialog-Box).
   2. The Data screen shows that the KPI chart inherits the dataset bound with the KPI. You cannot change the dataset.

      ![Create KPI Chart - Data](https://devnet.logianalytics.com/hc/article_attachments/9898515898903/crtkpicht_dt.gif)
   3. In the **Type** screen, select a 2-D Bar, Bench, Line, Area, Pie, or Bullet chart type.

      ![Create KPI Chart - Type](https://devnet.logianalytics.com/hc/article_attachments/9898532315927/crtkpicht_type.gif)
   4. In the Display, Layout, and Style screens, define the KPI chart [as you would do for a general chart](https://devnet.logianalytics.com/hc/en-us/articles/5735512245143-Inserting-Charts-in-a-Report#ChartDisplay).
   5. Select **Finish** to insert the chart into the KPI.
7. You can add more aggregations, dynamic formulas, [labels](https://devnet.logianalytics.com/hc/en-us/articles/5735564320919-Working-with-Labels), and [images](https://devnet.logianalytics.com/hc/en-us/articles/5735564305815-Working-with-Images) into the KPI.
8. Resize the KPI and the objects in it and drag the objects to adjust their position in the KPI to improve the layout.

After you create a KPI, you can further edit the objects in it. The KPI chart in a KPI supports most of the operations that you can apply to a general chart. For example, you can [modify its definition](https://devnet.logianalytics.com/hc/en-us/articles/5735498861207-Modifying-Charts#Edit) using the [KPI Chart Wizard dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735514748567-KPI-Chart-Wizard-Dialog-Box), [add link](https://devnet.logianalytics.com/hc/en-us/articles/5735569846807-Adding-Links-in-a-Report#Add) to its data markers, and format its [paper](https://devnet.logianalytics.com/hc/en-us/articles/5735564051223-Formatting-Chart-Paper), [platform](https://devnet.logianalytics.com/hc/en-us/articles/5735512145303-Formatting-Chart-Platform), [wall](https://devnet.logianalytics.com/hc/en-us/articles/5735507095959-Formatting-Chart-Wall-Floor), [label](https://devnet.logianalytics.com/hc/en-us/articles/5735563973015-Formatting-Chart-Labels), and data markers ([bars/benches](https://devnet.logianalytics.com/hc/en-us/articles/5735512007575-Formatting-Bar-Bench-Chart), [lines](https://devnet.logianalytics.com/hc/en-us/articles/5735520668823-Formatting-Line-Chart), [areas](https://devnet.logianalytics.com/hc/en-us/articles/5735506840727-Formatting-Area-Chart), [pies](https://devnet.logianalytics.com/hc/en-us/articles/5735520686359-Formatting-Pie-Donut-Chart), or [bullets](https://devnet.logianalytics.com/hc/en-us/articles/5735520593815-Formatting-Bullet-Chart)). If you want to remove the KPI chart, select the KPI, right-click and select **Remove KPI Chart** on the shortcut menu.

## Example: Creating a KPI

This example uses a KPI to show total sales.

1. Make sure **SampleReports.cat** is the currently open catalog file. If not, navigate to **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Navigate to **File** > **New** > **Web Report** to create a web report.
3. Drag ![KPI button](https://devnet.logianalytics.com/hc/article_attachments/9898533135639/icon_kpi.gif) from the **Components** panel to the destination.
4. In the Choose Data dialog box, select **WorldWideSalesBV** in the current catalog to bind it with the KPI and select **OK**. Designer inserts a blank KPI at the destination.
5. In the **Data** panel, [create a dynamic formula](https://devnet.logianalytics.com/hc/en-us/articles/5735534296599-Using-Dynamic-Resources-and-Local-Parameters-in-a-Report#Formula) in the name **KPI\_TotalSales** with the following expression. Use it as **Aggregation**.

   `if (@"Orders Detail.Total Sales">=1000000)  
    ToText(@"Orders Detail.Total Sales"/1000000, "$#,###.00")+"M"  
   else if (@"Orders Detail.Total Sales">=1000)  
    ToText(@"Orders Detail.Total Sales"/1000, "$#,###.00")+"K"  
   else  
    ToText(@"Orders Detail.Total Sales", "$#,###.00")`
6. Drag the formula from the Data panel to the KPI as the KPI value.
7. Right-click in the blank area of the KPI and select **Insert KPI Chart** from the shortcut menu.
8. In the Create KPI Chart dialog box, go to the **Display** screen, add the group object **Sales Quarter** to the category axis, the aggregation object **Total Sales** to the value axis, then select **Finish** to insert the KPI chart.

   ![Add Fields to the KPI Chart](https://devnet.logianalytics.com/hc/article_attachments/9898534665495/cmpnt_kpi_cht.gif)
9. Adjust the position of the objects in the KPI.

   ![Adjust Objects in the KPI](https://devnet.logianalytics.com/hc/article_attachments/9898518393879/cmpnt_kpi_pstn.gif)
10. Select the **View** tab to preview the real data.

    ![Preview the KPI](https://devnet.logianalytics.com/hc/article_attachments/9898518409495/cmpnt_kpi_prvw.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735521118231-Using-Shape-Maps)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735564320919-Working-with-Labels)
