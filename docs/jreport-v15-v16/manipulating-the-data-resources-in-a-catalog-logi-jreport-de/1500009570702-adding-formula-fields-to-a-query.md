---
title: "Adding Formula Fields to a Query"
id: 1500009570702
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009570702-Adding-Formula-Fields-to-a-Query
updated_at: 2021-07-24T05:53:54Z
---

# Adding Formula Fields to a Query

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009570682-Creating-Computed-Columns-in-a-Query)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592521-Previewing-a-Query)

# Adding Formula Fields to a Query

In addition to the table columns, you can also add formula fields to a query.

**To add a formula field to a query:**

1. In the Query Editor, select **Add Formula Fields** on the toolbar or select **Menu** > **Column** > **Add Formula Fields**. The [Add Formula Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009585521-Add-Formula-Fields-Dialog) dialog appears.

   ![Add Formula Field dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893823767/addfmlfld.gif)
2. Choose the required formula in the Formulas box and then select **Add**. The formula will then be added to the SELECT columns in the [SQL of the query](https://devnet.logianalytics.com/hc/en-us/articles/1500009570742-Editing-the-SQL-Statements-of-a-Query) and placed into the criteria panel in the lower part of the Query Editor. You can add filter criteria based on the formula column the same as on any other columns in the query.
3. Repeat the above step until you have added all the required formula fields, and then select **Close**. The formulas are added to the current query.

After a formula field has been added to a query, if you want to replace it with another one, you can double-click its name in the criteria panel, and then choose the required field in the Replace Formula dialog.

**Notes:**

* When you add a formula field, if the table that contains the field doesn't exist in the query, this table will be automatically added to the query.
* You are not able to add or edit a formula in the Add Formula Field dialog.
* The processing is very different from adding a [computed column](https://devnet.logianalytics.com/hc/en-us/articles/1500009570682-Creating-Computed-Columns-in-a-Query) even though the data looks the same. The computed column is calculated by the database engine before the data is returned. The formula value is calculated by Logi JReport after the data is returned so is less efficient.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009570682-Creating-Computed-Columns-in-a-Query)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592521-Previewing-a-Query)
