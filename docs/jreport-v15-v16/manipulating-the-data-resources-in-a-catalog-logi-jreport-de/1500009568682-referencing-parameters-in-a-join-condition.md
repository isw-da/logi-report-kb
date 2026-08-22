---
title: "Referencing Parameters in a Join Condition"
id: 1500009568682
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009568682-Referencing-Parameters-in-a-Join-Condition
updated_at: 2021-07-24T05:54:29Z
---

# Referencing Parameters in a Join Condition

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590081-Binding-a-Parameter-to-a-DBField)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590061-Applying-RLS-to-a-Parameter)

# Referencing Parameters in a Join Condition

Using parameters in join conditions of [data source pre-joins](https://devnet.logianalytics.com/hc/en-us/articles/1500009583161-Defining-the-Join-Relationships-Between-Resources#Create) and [query joins](https://devnet.logianalytics.com/hc/en-us/articles/1500009592501-Joining-Tables-in-a-Query#Manually) can dynamically change query results at runtime. It works similar to [query filters](https://devnet.logianalytics.com/hc/en-us/articles/1500009590161-Dynamically-Filtering-Queries). In a join condition, you can select a parameter, or manually input a parameter name in the format *@ParameterName* or *:ParameterName*. See the following example.

1. [Open the catalog file](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog) SampleReports.cat in `<install_root>\Demo\Reports\SampleReports`.
2. In the Catalog Manager, create a type-in parameter in Data Source 1, which is named pCountry of String type with two values: Canada and Italy.

   ![New Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889299991/prmtr_app_join1.gif)
3. Right-click the **ShipmentDetailsbyCustomer** query in Data Source 1 and select **Edit Query**.
4. In the Query Editor, double-click the join icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404893822743/btn_join.gif) in the join line.
5. In the [Join Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009566602-Join-Options-Dialog) dialog, select **Add Condition** to add a new condition line. In the second condition line, select the first ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404889276567/btn_chsr.gif) to select the **Country** field by double-clicking it from the Values dialog, then select the second ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404889276567/btn_chsr.gif) to select the parameter **pCountry**. Select **OK** in the Join Options dialog.

   ![Join Options dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889300247/prmtr_app_join2.gif)
6. Select **OK** in the Query Editor and then save the catalog.
7. [Create a page report](https://devnet.logianalytics.com/hc/en-us/articles/1500009592821-Creating-a-Page-Report) based on the ShipmentDetailsbyCustomer query in Data Source 1.
8. View the report result and you will be prompted to enter the parameter value for pCountry. Select Italy and the report shows only data of Italy.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590081-Binding-a-Parameter-to-a-DBField)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590061-Applying-RLS-to-a-Parameter)
