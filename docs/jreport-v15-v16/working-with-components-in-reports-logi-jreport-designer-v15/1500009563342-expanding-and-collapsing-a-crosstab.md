---
title: "Expanding and Collapsing a Crosstab"
id: 1500009563342
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009563342-Expanding-and-Collapsing-a-Crosstab
updated_at: 2021-07-24T05:56:02Z
---

# Expanding and Collapsing a Crosstab

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583801-Managing-the-Aggregate-Fields-in-a-Crosstab)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583861-Using-Crosstab-Formulas)

# Expanding and Collapsing a Crosstab

If a crosstab has more than one row/column group level, you can specify whether or not to enable the crosstab to be expanded at runtime, and set the default expanding/collapsing state of groups in the outer level. This behavior is controlled by two properties: Expand Data and Expand Detail Data.

* **Expand Data**: A property on both crosstab, and DBField or formula added into crosstab as a dimension (group level). This property on crosstab controls whether or not to enable end users to expand/collapse dimensions in a crosstab, and when it is enabled, you can use the property on DBFields or formulas to specify whether this dimension can be expanded/collapsed respectively.
* **Expand Detail Data**: A property on DBFields or formulas added into the crosstab as a dimension (group level). It specifies whether or not to display the details of this field by default.

**Note:** These two properties work only in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009571022-Designing-a-Report-Page#Mode), so they are supported for page report only, and after setting the two properties, if you have further modified the crosstab layout, they may not take effect.

The following example shows how to use the two properties:

1. [Open the catalog file](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog) SampleReports.cat in `<install_root>\Demo\Reports\SampleReports`.
2. Create a crosstab report on the query WorldWideSales in Data Source 1 of the catalog as follows: add Product Type Name and Category in the Products table as the column fields, Region, Country and State in the Customers table as the row fields, Quantity in the Orders Detail table as the aggregate field and specify Sum as the aggregate function, set the crosstab to be Vertical Layout (Number of Rows: 1), and apply the style Classic to the crosstab.
3. In the Report Inspector, set the Expand Data property of the crosstab to **true**.
4. Set the Expand Data property of the DBField Country to **false**, and the Expand Detail Data property of the DBField Product Type Name to **false**.
5. Uncheck **Page Layout** on the View menu.
6. Save the crosstab.
7. Select **View** > **Preview As** > **Page Report Result** to preview the report. You can then select the buttons with a plus or minus sign to expand/collapse the Region and Product Type Name dimensions, and since the Expand Detail Data property of Product Type Name is set to false, you will find the details of this dimension are not expanded by default.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889410711/cmpnt_crstb_xpnd.gif)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583801-Managing-the-Aggregate-Fields-in-a-Crosstab)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583861-Using-Crosstab-Formulas)
