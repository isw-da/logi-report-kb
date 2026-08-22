---
title: "Embedding Data Components in a Banded Object"
id: 1500010056742
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010056742-Embedding-Data-Components-in-a-Banded-Object
updated_at: 2021-07-23T19:14:35Z
---

# Embedding Data Components in a Banded Object

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094321-Modifying-Banded-Objects)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010056722-Obtaining-Detailed-Information-from-a-Banded-Object)

# Embedding Data Components in a Banded Object

You can embed data components, including banded objects, tables, charts, crosstabs, and geographic maps inside a banded object. The embedded data components can have their own datasets or inherit the dataset from the parent, and when they inherit the parent's dataset, the report becomes powerful. This topic describes how you can make use of this unique Embedding Data Component feature of banded objects to design powerful reports.

For example, if you want Designer to filter a child data component automatically by the group of the parent banded object, you can put the child data component in the group panel in the banded object and make it inherit dataset from its parent, then Logi Report replicates the child data component for each group in the parent. Moreover, by embedding a chart in a banded object and having it inherit the dataset from the parent, you can make the chart a [dynamic chart in Excel](https://devnet.logianalytics.com/hc/en-us/articles/1500010056862-Creating-Dynamic-Charts-in-Excel). However, when you want to insert a data component into the Detail (DT), Banded Page Header (BPH), or Banded Page Footer (BPF) panel of a banded object, you cannot make the data component inherit dataset from the parent.

Suppose you want to deliver a chart to give to each country showing the annual sales of each product category for the country, you can create the report as follows:

1. Make sure **SampleReports.cat** is the currently open catalog file. If not, select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. [Create a page report with a banded object in it](https://devnet.logianalytics.com/hc/en-us/articles/1500010101181-Creating-Reports#Page) based on the query **WorldWideSales** in Data Source 1 and group it by the field **Country**.

   ![Banded Object](https://devnet.logianalytics.com/hc/article_attachments/4404857066775/cmpnt_bdobj_embed1.gif)
3. Select the Country group-by field, then in the Report Inspector, set its properties **Foreground**, **Bold**, and **Font Size** to **0xff0000**, **true**, and **10** respectively.
4. Right-click the banded header panel (BH) and select **Hide** from the shortcut menu to hide it.
5. Repeat the above step to hide the panels BPH, DT, GF, BPF, and BF that do not contain any data.
6. Resize the group header panel (GH), drag and drop the **Clustered Bar** icon ![Bar Chart button](https://devnet.logianalytics.com/hc/article_attachments/4404857062167/btn_barcht.gif) from the **Components** panel to the group header panel below the Country group-by field.
7. In the Create Chart wizard, [define the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010057042-Inserting-Charts-in-a-Report#Query) as follows:
   * Use the current dataset **WorldWideSales** its parent applies.
   * Display in the default chart type **Clustered Bar 2-D**.
   * Show the summary **Sum\_AnnualSalesbyCountry** on the value axis (Designer adds the field Country automatically as the category field).
   * Add **Category** as the series field.

   Designer embeds the chart in the banded object as follows in the design area:

   ![Chart in a Banded Object](https://devnet.logianalytics.com/hc/article_attachments/4404848698391/cmpnt_bdobj_embed2.gif)
8. Save the report and select the **View** tab to preview it. Designer filters the annual sales for each product category in each country in the chart according to the group-by field Country in the banded object.

   ![Preview the Report](https://devnet.logianalytics.com/hc/article_attachments/4404857067415/cmpnt_bdobj_embed3.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094321-Modifying-Banded-Objects)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010056722-Obtaining-Detailed-Information-from-a-Banded-Object)
