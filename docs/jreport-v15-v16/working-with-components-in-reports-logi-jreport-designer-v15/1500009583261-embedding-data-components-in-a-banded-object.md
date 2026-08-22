---
title: "Embedding Data Components in a Banded Object"
id: 1500009583261
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009583261-Embedding-Data-Components-in-a-Banded-Object
updated_at: 2021-07-24T05:56:11Z
---

# Embedding Data Components in a Banded Object

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562882-Managing-Banded-Panels)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583301-Setting-Up-a-Data-Container-Link)

# Embedding Data Components in a Banded Object

Data components, including banded objects, tables, charts, crosstabs and geographic maps can be embedded inside a banded object. The embedded data components can have their own datasets or inherit the dataset from the parent, and when they inherit the parent's dataset, the report becomes powerful. For example, if you want a child data component to be automatically filtered by the group of the parent banded object, you can put the child data component in the group panel in the banded object and make it inherit dataset from its parent, then the child data component will be replicated for each group in the parent. Moreover, by embedding a chart in a banded object and having it inherit the dataset from the parent, you can make the chart a [Dynamic Chart in Excel](https://devnet.logianalytics.com/hc/en-us/articles/1500009583421-Creating-Dynamic-Charts-in-Excel).

However, when a data component is to be inserted into the Detail (DT), BandedPageHeader (BPH) or BandedPageFooter (BPF) panel of a banded object, you cannot make the data component inherit dataset from the parent.

Suppose you want to have a chart to give to each country showing the annual sales of each product category for the country, you can create the report as follows:

1. [Open the Catalog File](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog) SampleReports.cat in `<install_root>\Demo\Reports\SampleReports`.
2. [Create a page report with a banded object in it](https://devnet.logianalytics.com/hc/en-us/articles/1500009592821-Creating-a-Page-Report) based on the query WorldWideSales in Data Source 1 and grouped by the field Country.

   ![Banded object](https://devnet.logianalytics.com/hc/article_attachments/4404894006807/cmpnt_bdobj_embed1.gif)
3. Select the Country group by field and set its properties Foreground, Bold and Font Size to **0xff0000**, **true** and **10** respectively in the Report Inspector.
4. Right-click the banded header panel (BH) and select **Hide** from the shortcut menu to hide it.
5. Repeat the above step to hide the panels BPH, DT, GF, BPF and BF that do not contain any data.
6. Resize the group header panel (GH), drag and drop **Chart** from the Component to the panel below the Country group by field.
7. In the Data screen of the Create Chart wizard, check the **Current** radio button, the query WorldWideSales is selected by default, then select **Next**.
8. In the Type screen, keep the default chart type Clustered Bar 2-D and select **Next**.
9. In the Display screen, add the summary **Sum\_AnnualSalesbyCountry** to the Show Values box. The field Country is then added automatically to the Category box.
10. Add the field **Category** in the Products table to the Series box, then select **Finish** (for more information about creating a chart, select [here](https://devnet.logianalytics.com/hc/en-us/articles/1500009563242-Inserting-a-Chart#Page)).
11. The chart is embedded into the banded object and the report displays as follows:

    ![Chart in a banded object](https://devnet.logianalytics.com/hc/article_attachments/4404889428247/cmpnt_bdobj_embed2.gif)
12. Save the report and select the **View** tab.
    The annual sales for each product category
    in each country are filtered in the chart according to the group by field Country in the banded object.

    ![Chart in a banded object](https://devnet.logianalytics.com/hc/article_attachments/4404894007063/cmpnt_bdobj_embed3.gif)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562882-Managing-Banded-Panels)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583301-Setting-Up-a-Data-Container-Link)
