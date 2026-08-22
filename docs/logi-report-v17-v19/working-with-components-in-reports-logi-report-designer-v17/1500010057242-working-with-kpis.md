---
title: "Working with KPIs"
id: 1500010057242
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010057242-Working-with-KPIs
updated_at: 2021-07-23T19:14:45Z
---

# Working with KPIs

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094801-Using-Shape-Maps)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057262-Working-with-Labels)

# Working with KPIs

A KPI (Key Performance Indicator) is a data container based on a business view for displaying KPI value together with a chart to help illustrate the value. This topic introduces what objects a KPI can contain and how you can create KPIs in a report.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) You cannot use KPIs in page reports.

This topic contains the following sections:

* [Objects in a KPI](#Object)
* [Inserting KPIs in a Report](#Insert)
* [Example of Creating a KPI](#Example)

## Objects in a KPI

You can add the following objects in a KPI:

* Aggregations and formulas as the KPI values.
* Labels to describe the values and as the KPI title or description.
* Images to decorate the KPI or used as logo.
* A KPI chart to assist the KPI values, for example, to show the trend of total sales over time. You can include at most one KPI chart in a KPI. A KPI chart does not have the legend and axes compared to normal Logi Report charts. You can insert a KPI chart in a KPI only and the KPI chart should inherit the dataset from the KPI. A KPI chart can be one of the following chart types: Bar, Bench, Line, Area, Pie, or Bullet.

A KPI is bound with a business view so the KPI value and KPI chart in it are both based on this business view. You can position and resize the objects in a KPI freely by dragging them inside the KPI.

## Inserting KPIs in a Report

To create a KPI in a web report or library component, take the following steps:

1. Position the mouse pointer at the destination where you want to insert the KPI. You can insert a KPI in a web report or library component as listed in [Component Placement](https://devnet.logianalytics.com/hc/en-us/articles/1500010094261-Working-with-Components-in-Reports#Relationship).
2. Do either of the following:
   * From the **Components** panel, drag the **KPI** icon ![KPI button](https://devnet.logianalytics.com/hc/article_attachments/4404857008279/btn_kpi.gif) in the Visual category to the destination.
   * Select **Insert** > **KPI**.
   * Select **Home** > **Insert** > **KPI**.
3. In the [Choose Data dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095701-Choose-Data-Dialog-Box#BV), select a business view in the current catalog to bind with the KPI and select **OK**.

   ![Choose Data dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848629911/chsdt-bv.gif)
4. Designer inserts a blank KPI at the destination. You can then define the KPI by adding objects into it.

   ![Blank KPI](https://devnet.logianalytics.com/hc/article_attachments/4404857043351/cmpnt_kpi_blank.gif)
5. Drag an [aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500010094901-Working-with-Summary-Fields) or a [dynamic formula](https://devnet.logianalytics.com/hc/en-us/articles/1500010094741-Working-with-Formula-Fields) from the **Data** panel as the KPI value. Designer adds the name label of the object at the same time by default. You can edit the label text.
6. Insert a KPI chart to demonstrate data about the KPI value as follows:
   1. Right-click in the blank area of the KPI and select **Insert KPI Chart** from the shortcut menu. Designer displays the [Create KPI Chart dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058382-Create-KPI-Chart-Dialog-Box).
   2. The Data screen shows that the KPI chart inherits the business view bound with the KPI. You cannot change the business view.

      ![Create KPI Chart - Data](https://devnet.logianalytics.com/hc/article_attachments/4404848596631/crtkpicht_dt.gif)
   3. In the **Type** screen, select a 2-D Bar, Bench, Line, Area, Pie, or Bullet chart type.

      ![Create KPI Chart - Type](https://devnet.logianalytics.com/hc/article_attachments/4404848596887/crtkpicht_type.gif)
   4. In the Display, Layout, and Style screens, define the chart [as you would do for a general chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010057042-Inserting-Charts-in-a-Report#ChartDisplay).
   5. Select **Finish** to insert the chart into the KPI.
7. You can add more aggregations, dynamic formulas, [labels](https://devnet.logianalytics.com/hc/en-us/articles/1500010057262-Working-with-Labels), and [images](https://devnet.logianalytics.com/hc/en-us/articles/1500010094761-Working-with-Images) into the KPI.
8. Resize the KPI and the objects in it and adjust the position of the objects by dragging to improve the layout.

After you have created a KPI in a report, you can further edit the objects in it according to your requirements. The KPI chart in a KPI supports most of the operations that you can apply to a general chart. For example, you can [modify its definition](https://devnet.logianalytics.com/hc/en-us/articles/1500010094661-Modifying-Charts#Edit) using the [KPI Chart Wizard dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097821-KPI-Chart-Wizard-Dialog-Box), [add link](https://devnet.logianalytics.com/hc/en-us/articles/1500010101261-Adding-Links-in-Reports#Add) to its data markers, and format its [paper](https://devnet.logianalytics.com/hc/en-us/articles/1500010094541-Formatting-the-Paper), [platform](https://devnet.logianalytics.com/hc/en-us/articles/1500010094561-Formatting-the-Platform), [wall](https://devnet.logianalytics.com/hc/en-us/articles/1500010094641-Formatting-the-Wall-Floor), [label](https://devnet.logianalytics.com/hc/en-us/articles/1500010094501-Formatting-the-Labels), and data markers ([bars/benches](https://devnet.logianalytics.com/hc/en-us/articles/1500010094461-Formatting-the-Bars-in-a-Bar-Bench-Chart), [lines](https://devnet.logianalytics.com/hc/en-us/articles/1500010094521-Formatting-the-Lines-in-a-Line-Chart), [areas](https://devnet.logianalytics.com/hc/en-us/articles/1500010094421-Formatting-the-Areas-in-an-Area-Chart), [pies](https://devnet.logianalytics.com/hc/en-us/articles/1500010056982-Formatting-the-Pies-Donuts-and-KPI-Value-Labels-in-a-Pie-Donut-Chart), or [bullets](https://devnet.logianalytics.com/hc/en-us/articles/1500010056902-Formatting-the-Bullets-in-a-Bullet-Chart)). If you want to remove the KPI chart, select the KPI, right-click and select **Remove KPI chart** on the shortcut menu.

## Example of Creating a KPI

The following example uses a KPI to show total sales:

1. Make sure **SampleReports.cat** is the currently open catalog file. If not, select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Select **File** > **New** > **Web Report** to create a blank web report.
3. From the **Components** panel, drag the **KPI** icon ![KPI button](https://devnet.logianalytics.com/hc/article_attachments/4404857008279/btn_kpi.gif) in the Visual category to the destination.
4. In the Choose Data dialog box, select **WorldWideSalesBV** in the current catalog to bind it with the KPI and select **OK**.

   Designer inserts a blank KPI at the destination.
5. In the **Data** panel, [create a dynamic formula](https://devnet.logianalytics.com/hc/en-us/articles/1500010101361-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Formula) named "KPI\_TotalSales" with the following expression. Use it as **Aggregation**.

   `if (@"Orders Detail.Total Sales">=1000000)  
    ToText(@"Orders Detail.Total Sales"/1000000, "$#,###.00")+"M"  
   else if (@"Orders Detail.Total Sales">=1000)  
    ToText(@"Orders Detail.Total Sales"/1000, "$#,###.00")+"K"  
   else  
    ToText(@"Orders Detail.Total Sales", "$#,###.00")`
6. Drag the formula from the Data panel to the KPI as the KPI value.
7. Right-click in the blank area of the KPI and select **Insert KPI Chart** from the shortcut menu.
8. In the Create KPI Chart dialog box, go to the **Display** screen, add the group object **Sales Quarter** to the category axis, the aggregation object **Total Sales** to the value axis, then select **Finish** to insert the KPI chart.

   ![Add Fields to the KPI Chart](https://devnet.logianalytics.com/hc/article_attachments/4404848673175/cmpnt_kpi_cht.gif)
9. Adjust the position of the inserted objects. Widen the formula label and field so that the label and value can fully display.

   ![Adjust the Position of the Inserted Objects](https://devnet.logianalytics.com/hc/article_attachments/4404857043735/cmpnt_kpi_rst.gif)
10. Select the **View** tab to preview the real data.

    ![Preview the Report](https://devnet.logianalytics.com/hc/article_attachments/4404848673559/cmpnt_kpi_vw.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094801-Using-Shape-Maps)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057262-Working-with-Labels)
