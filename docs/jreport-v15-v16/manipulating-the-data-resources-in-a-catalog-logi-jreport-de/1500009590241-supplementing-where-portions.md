---
title: "Supplementing WHERE Portions"
id: 1500009590241
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009590241-Supplementing-WHERE-Portions
updated_at: 2021-07-24T05:54:28Z
---

# Supplementing WHERE Portions

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590161-Dynamically-Filtering-Queries)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590081-Binding-a-Parameter-to-a-DBField)

# Supplementing WHERE Portions

Logi JReport allows you to change a query at runtime using the API. To do this, you can call the method setWherePortion() from your Java application. However, by calling this method, the original WHERE portion of the query will be replaced. If you want to append the runtime WHERE portion to the original one instead of replacing it/them, you can do it in the following way without using the Java API:

1. [Open the catalog file](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog) SampleReports.cat in `<install_root>\Demo\Reports\SampleReports`.
2. In the Catalog Manager, expand the desired data source and create a type-in parameter named p\_Portion of String type (leave the other settings to their default).
3. In the same data source, [create a query](https://devnet.logianalytics.com/hc/en-us/articles/1500009592461-Creating-a-Query) CustomersInfo on the table Customers. Select all the fields contained in the table.
4. [Create a page report with a table in it](https://devnet.logianalytics.com/hc/en-us/articles/1500009592821-Creating-a-Page-Report) based on the query, and have the fields Customer ID, Customer Name, City and Phone displayed in the report, then apply the Commercial style.
5. In the Data panel, right-click the node that represents the query, and then select **Edit Query** from the shortcut menu.
6. In the Query Editor, select **Menu** > **Query** > **Filter**.
7. In the Search Condition dialog, add two condition lines (WHERE portions) for the query as follows (for details, see [Filtering with the Filter Format](https://devnet.logianalytics.com/hc/en-us/articles/1500009570722-Filtering-the-Fields-of-a-Query#Filter)):

   **![Filter Condition](https://devnet.logianalytics.com/hc/article_attachments/4404893825815/prmtr_app_splmnt1.gif)**

   The colon is used to append the parameter value (of String type) to the first condition line instead of replacing it.
8. Select **OK** to apply the change to the query.
9. View the report, and in the Enter Parameter Values dialog, write a WHERE portion in standard SQL syntax as value of p\_Portion, for example, CUSTOMERID<20. Then, both of the two WHERE portions will be used to filter the query.

   ![Report Result](https://devnet.logianalytics.com/hc/article_attachments/4404893826071/prmtr_app_splmnt2.gif)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590161-Dynamically-Filtering-Queries)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590081-Binding-a-Parameter-to-a-DBField)
