---
title: "Creating Computed Columns in a Query"
id: 1500009570682
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009570682-Creating-Computed-Columns-in-a-Query
updated_at: 2021-07-24T05:53:53Z
---

# Creating Computed Columns in a Query

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009570742-Editing-the-SQL-Statements-of-a-Query)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009570702-Adding-Formula-Fields-to-a-Query)

# Creating Computed Columns in a Query

Computed columns can be created in a query that is built on tables, views, and synonyms from one JDBC connection only.

**To create a computed column in a query:**

1. In the Query Editor, select **New Computed Column** on the toolbar or select **Menu** > **Column** > **New Computed Column**. The [New Computed Column](https://devnet.logianalytics.com/hc/en-us/articles/1500009587881-New-Computed-Column-Dialog) dialog appears.

   ![New Computed Column dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893824023/crtcmptedclmn.gif)
2. Input a name for the column in the Computed Column Name text box.
3. Compose your functions for the column.

   In the lower part of the dialog, there are functions and tables/columns of the query. These are just for your reference. You can specify the expression by yourself in the editing text box, only if the expression can be accepted by your database.

   In addition, the functions in this dialog are not from the Logi JReport system. They are from the database you are connected to. If you change your database, some of these functions may no longer exist. For each database, a different set of supported functions will be returned. The following functions will help you with writing an expression.

   * **+**: Add numbers or fields together in the Expression menu.
   * **-**: Subtract numbers or fields together in the Expression menu.
   * **\***: Multiply numbers or fields together in the Expression menu.
   * **/**: Divide numbers or fields together in the Expression menu.
   * **=**: Equate fields together.
   * **"**: Place quotations on long character strings or names that have blanks in them (example: place quotes on values such as "New York" or "Washington DC").
   * **||**: Place fields together in the same Expression menu. (Example: "New York" || "Washington DC").
   * **()**: Place your fields in parentheses.
4. When done, select the **OK** button to create the computed column and it will be added to the [SQL of the query](https://devnet.logianalytics.com/hc/en-us/articles/1500009570742-Editing-the-SQL-Statements-of-a-Query).

   Suppose you have created a computed column named Net Total in a query and the computation is @UNITPRICE \* @QUANTITY \* (100 - @DISCOUNT) / 100, when you view the SQL statements of the query, you will see the following SQL statement being inserted into the SQL: @UNITPRICE \* @QUANTITY \* (100 - @DISCOUNT) / 100 AS "Net Total".

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009570742-Editing-the-SQL-Statements-of-a-Query)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009570702-Adding-Formula-Fields-to-a-Query)
