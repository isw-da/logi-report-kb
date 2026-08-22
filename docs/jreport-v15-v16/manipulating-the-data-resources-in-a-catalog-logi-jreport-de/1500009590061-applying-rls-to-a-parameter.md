---
title: "Applying RLS to a Parameter"
id: 1500009590061
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009590061-Applying-RLS-to-a-Parameter
updated_at: 2021-07-24T05:54:29Z
---

# Applying RLS to a Parameter

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568682-Referencing-Parameters-in-a-Join-Condition)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568642-Filtering-a-Parameter-with-Another-Parameter)

# Applying RLS to a Parameter

When a parameter is [bound to a DBField](https://devnet.logianalytics.com/hc/en-us/articles/1500009590081-Binding-a-Parameter-to-a-DBField), you can apply a [record-level security policy](https://devnet.logianalytics.com/hc/en-us/articles/1500009593181-RLS-and-CLS-at-Data-Source-Scope) (RLS) of data source scope to the parameter. The security policy is specified on the DBField that is bound to the parameter. At runtime, end users will only see parameter values which the security identifier allows to view in the parameter value drop-down list.

The following example explains how to apply RLS to the value drop-down list of a parameter in detail.

1. [Open the catalog file](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog) SampleReports.cat in `<install_root>\Demo\Reports\SampleReports`.
2. In the Catalog Manager, expand the data source where you want to create the parameter.
3. Right-click **Security Entry**  in the Security node, select **New Security Entry** on the shortcut menu, then name the security policy **CusCountry**.
4. In the Security dialog, make sure Valid RLS is checked at the bottom left.
5. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) and then select **Add User** to add the user John, which has the permission to view the Canada records in the Country column only.

   ![Set Permission for John](https://devnet.logianalytics.com/hc/article_attachments/4404893829527/prmtr_app_apply1.gif)
6. Add another user David which has the permission to view records in the United Kingdom only.
7. In the same data source, right-click the **Parameters**  node and select **New Parameter** on the shortcut menu.
8. In the New Parameter dialog, enter **pCountry** in the Name field, select **Bind with Single Column** from the Value Setting drop-down list, and bind the parameter with the **Country** column. In the Options box, select **CusCountry** as value of Record Level Security, and then set the Distinct option to **true**. Select **OK**.

   ![New Parameter](https://devnet.logianalytics.com/hc/article_attachments/4404889302551/prmtr_app_apply3.gif)
9. [Create a query](https://devnet.logianalytics.com/hc/en-us/articles/1500009592461-Creating-a-Query) CustomersInfo on the table Customers. Select all the fields contained in the table.
10. [Create a page report with a standard banded object in it](https://devnet.logianalytics.com/hc/en-us/articles/1500009592821-Creating-a-Page-Report)  based on the query, and have the fields Customer ID, Customer Name, Country and Phone displayed in the report.
11. In the Data panel, right-click the node that represents the query, and then select **Edit Query** from the shortcut menu.
12. In the Query Editor, select **Menu** > **Query** > **Filter**.
13. In the Search Condition dialog, add a condition for the query as follows (for details, see [Filtering with the Filter Format](https://devnet.logianalytics.com/hc/en-us/articles/1500009570722-Filtering-the-Fields-of-a-Query#Filter)):

    ![Filter Condition](https://devnet.logianalytics.com/hc/article_attachments/4404889302807/prmtr_app_apply2.gif)
14. Select **OK** to apply the changes to the query.
15. Select **File** > **Options**, in the General category of the Options dialog, set the User Name as **John**.
16. View the report, and the Enter Parameter Values dialog is displayed.
17. Select the parameter value drop-down list, and you can see that only Canada is displayed for the user name.

    ![Enter Parameter Value](https://devnet.logianalytics.com/hc/article_attachments/4404893829911/prmtr_app_apply4.gif)
18. Set the user name as **David** in the Options dialog and view the report again. You will find that only the value United Kingdom is displayed in the parameter value drop-down list this time.

**Notes:**

* When applying an RLS policy to a parameter bound with a column, you must make sure the parameter bound column and the column used to set conditions in the RLS policy are in the same table. In addition, if the RLS policy also contains conditions defined on other columns, all the columns must be in the same table, and the RLS policy cannot contain parameters and formulas; otherwise, when you apply the RLS to the parameter, the RLS would not work properly.
* When you have applied an RLS policy to a parameter and then you edit the SQL statement of the parameter via the Import SQL option in the New Parameter dialog, the parameter value drop-down list may be Null because the changed SQL statement may not match the permissions of the RLS.
* When previewing a report that contains parameters applied with RLS in the Page Report Result or Web Report Result format in Logi JReport Designer, you need to make sure your RLS policy contains the user Jinfonet. That is because the user Jinfonet is the default and only user of the preview server. Any other users in the RLS policy cannot be recognized by the preview server.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568682-Referencing-Parameters-in-a-Join-Condition)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568642-Filtering-a-Parameter-with-Another-Parameter)
