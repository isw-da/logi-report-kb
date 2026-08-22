---
title: "Embedding Data Components in a Banded Object"
id: 1500010028642
section: "Working with Components in Reports - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010028642-Embedding-Data-Components-in-a-Banded-Object
updated_at: 2021-07-24T10:39:30Z
---

# Embedding Data Components in a Banded Object

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010063321-Modifying-Banded-Objects) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010028622-Obtaining-Detailed-Information-from-a-Banded-Object)

# Embedding Data Components in a Banded Object

Data components, including banded objects, tables, charts, crosstabs and geographic maps can be embedded inside a banded object. The embedded data components can have their own datasets or inherit the dataset from the parent, and when they inherit the parent's dataset, the report becomes powerful. For example, if you want a child data component to be automatically filtered by the group of the parent banded object, you can put the child data component in the group panel in the banded object and make it inherit dataset from its parent, then the child data component will be replicated for each group in the parent. Moreover, by embedding a chart in a banded object and having it inherit the dataset from the parent, you can make the chart a [dynamic chart in Excel](https://devnet.logianalytics.com/hc/en-us/articles/1500010028742-Creating-Dynamic-Charts-in-Excel).

However, when a data component is to be inserted into the Detail (DT), Banded Page Header (BPH) or Banded Page Footer (BPF) panel of a banded object, you cannot make the data component inherit dataset from the parent.

Suppose you want to have a chart to give to each country showing the annual sales of each product category for the country, you can create the report as follows:

1. Make sure SampleReports.cat is the currently open catalog file. If not select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. [Create a page report with a banded object in it](https://devnet.logianalytics.com/hc/en-us/articles/1500010034782-Creating-Reports#Page) based on the query WorldWideSales in Data Source 1 and grouped by the field Country.

   ![Banded Object](https://devnet.logianalytics.com/hc/article_attachments/4404901343127/cmpnt_bdobj_embed1.gif)
3. Select the **Country** group-by field and in the Report Inspector set its properties Foreground, Bold and Font Size to **0xff0000**, **true** and **10** respectively.
4. Right-click the banded header panel (BH) and select **Hide** from the shortcut menu to hide it.
5. Repeat the above step to hide the panels BPH, DT, GF, BPF and BF that do not contain any data.
6. Resize the group header panel (GH), drag and drop ![Bar Chart button](https://devnet.logianalytics.com/hc/article_attachments/4404909287063/btn_barcht.gif) from the Components panel to the group header panel below the Country group-by field.
7. In the Create Chart wizard, [define the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010063601-Inserting-Charts-in-a-Report#Query) as follows:
   * Use the current dataset WorldWideSales used by its parent.
   * Display in the default chart type Clustered Bar 2-D.
   * Show the summary Sum\_AnnualSalesbyCountry on the value axis (the field Country is added automatically as the category field), Category as the series field.

   The chart is embedded into the banded object as follows in the design area:

   ![Chart in a Banded Object](https://devnet.logianalytics.com/hc/article_attachments/4404909289623/cmpnt_bdobj_embed2.gif)
8. Save the report and select the **View** tab to preview it. The annual sales for each product category in each country are filtered in the chart according to the group-by field Country in the banded object.

   ![Preview the Report](https://devnet.logianalytics.com/hc/article_attachments/4404909289879/cmpnt_bdobj_embed3.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010063321-Modifying-Banded-Objects) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010028622-Obtaining-Detailed-Information-from-a-Banded-Object)
