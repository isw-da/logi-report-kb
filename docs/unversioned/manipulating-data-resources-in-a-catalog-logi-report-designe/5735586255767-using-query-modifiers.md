---
title: "Using Query Modifiers"
id: 5735586255767
section: "Manipulating Data Resources in a Catalog - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735586255767-Using-Query-Modifiers
updated_at: 2022-11-02T08:17:47Z
---

# Using Query Modifiers

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735586187287-Working-with-Cached-Query-Results)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735586234007-Applying-Dynamic-Queries)

# Using Query Modifiers

Query modifiers, also called WHERE portions in Logi Report, are the WHERE clauses in SQL select statements, which are saved independently from queries in a catalog (not related to queries). When you run a report using a Java application that uses the Engine Bean, you can specify a query modifier to the Logi Report system via the Engine Bean, the Logi Report API then constructs the SQL statement based on the query the report uses and may substitute the WHERE clause in the SQL statement if there is a given query modifier, so that you can generate the report on different data. This topic describes how you can create query modifiers in a catalog.

**To add a query modifier in a catalog**

1. [Open the catalog](https://devnet.logianalytics.com/hc/en-us/articles/5735563628951-Creating-Opening-and-Saving-Catalogs#Open) to which you want to add the query modifier.
2. In the Catalog Manager, expand the node of a data source, and then the **Queries** node.
3. Right-click the **Query Modifiers** node and select **New Query Modifier** from the shortcut menu. Designer displays the [Query Modifier Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552456215-Query-Modifier-Editor-Dialog-Box).

   ![Query Modifier Editor](https://devnet.logianalytics.com/hc/article_attachments/9898475076887/qrymdfr.gif)
4. Type a name for the query modifier in the **Name** text box.
5. From the **Type** drop-down list, select the type of the query modifier: Structure or String. You can save a query modifier in a catalog in two formats: structure and string. In the structure format, the groups of conditions are stored. The query modifier consists of many condition groups and the groups are connected by a logical operator. Each condition consists of many conditions and the conditions are also connected by a logical operator. Each condition contains a left expression, the relationship operator, and a right expression. In the string format, the text of the query modifier is stored.
6. Select a query from the **Query** drop-down list to build the query modifier. You can select **Show Query** to view the query.
7. In the editing panel, edit the query modifier. If you select the String type, a text editor is available where you can type the WHERE clause; if you select the Structure type, a condition editor is available and you can construct the query modifier by selecting buttons (for more information about how to set the condition, see [Filtering with the Filter Format](https://devnet.logianalytics.com/hc/en-us/articles/5735547138327-Creating-Queries-in-a-Catalog#Filter)).
8. Select **Check** to check the validity of the query modifier according to the query. Designer defines the validity of a query modifier as, all the fields and formulas referenced by the query modifier are available to the chosen query. This validation check also ensures that the query modifier can work with the specified query.
9. Select **Show SQL** to view the string of the query modifier.
10. Select **OK** to create the query modifier.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735586187287-Working-with-Cached-Query-Results)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735586234007-Applying-Dynamic-Queries)
