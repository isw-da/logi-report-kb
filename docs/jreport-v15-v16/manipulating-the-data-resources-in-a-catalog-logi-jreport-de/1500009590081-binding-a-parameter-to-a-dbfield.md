---
title: "Binding a Parameter to a DBField"
id: 1500009590081
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009590081-Binding-a-Parameter-to-a-DBField
updated_at: 2021-07-24T05:54:30Z
---

# Binding a Parameter to a DBField

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590241-Supplementing-WHERE-Portions)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568682-Referencing-Parameters-in-a-Join-Condition)

# Binding a Parameter to a DBField

Logi JReport provides a mechanism which links each field value of a "display column" with the exact value of a "bind column". When you select the field value from the "display column", the field value of the "bind column" is sent to the query to filter the query result. Both columns can come from any data source in a catalog, and Logi JReport always retrieves just distinct values from the data source for the columns. So even though the value selection might be Countries from Customers, only countries with current customers will be displayed.

For example, if you specified customer ID to query data, but you would like to show customer name not customer ID for the parameter values which display at runtime, you can do so by selecting a different column for the display column than for the bind column. By default the bind column and display column are identical.

1. [Open the catalog file](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog) SampleReports.cat in `<install_root>\Demo\Reports\SampleReports`.
2. In the Catalog Manager, expand the data source where to create the parameter.
3. Right-click the **Parameters** node and select **New Parameter** on the shortcut menu.
4. In the New Parameter dialog, enter **BindColumn** in the Name field, select **Bind with Single Column** from the Value Setting drop-down list, select **Tables and Views** from the Source drop-down list, then select **Customer ID** from the Bind Column drop-down list, and choose **Customer Name** from the Display Column drop-down list. Select **OK**.

   ![New Parameter](https://devnet.logianalytics.com/hc/article_attachments/4404893829015/prmtr_app_bind1.gif)

   **Note:** Selecting a display column different from the bind column will establish a link between the two columns (DBFields). When you select the field value from the display column, the corresponding field value of the bind column is actually assigned to the parameter.
5. In the same data source, [create a query](https://devnet.logianalytics.com/hc/en-us/articles/1500009592461-Creating-a-Query) CustomersInfo on the table Customers. Select all the fields contained in the table.
6. [Create a page report with a standard banded object in it](https://devnet.logianalytics.com/hc/en-us/articles/1500009592821-Creating-a-Page-Report) based on the query, and have the fields Customer ID, Customer Name, City and Phone displayed in the report.
7. In the Data panel, right-click the node that represents the query, and then select **Edit Query** from the shortcut menu.
8. In the Query Editor, select **Menu** > **Query** > **Filter**.
9. In the Search Condition dialog, add a condition for the query as follows (for details, see [Filtering with the Filter Format](https://devnet.logianalytics.com/hc/en-us/articles/1500009570722-Filtering-the-Fields-of-a-Query#Filter)):

   ![Filter Condition](https://devnet.logianalytics.com/hc/article_attachments/4404889302295/prmtr_app_bind.gif)
10. Select **OK** to apply the changes to the query.
11. Select the **View** tab to view the report. All the customer na
12. mes will be listed in the Enter Parameter Values dialog. You can select a value from the list to query data with the customer ID instead of customer name.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590241-Supplementing-WHERE-Portions)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568682-Referencing-Parameters-in-a-Join-Condition)
