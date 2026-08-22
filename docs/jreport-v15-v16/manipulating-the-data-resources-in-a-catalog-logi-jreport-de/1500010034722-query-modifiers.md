---
title: "Query Modifiers"
id: 1500010034722
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010034722-Query-Modifiers
updated_at: 2021-07-24T10:37:46Z
---

# Query Modifiers

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010070721-Locking-Queries) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010034602-Cached-Query-Results)

# Query Modifiers

Query modifiers, also called WHERE portions in Logi JReport, are the WHERE clauses in SQL select statements. In Logi JReport, the SQL select statements are called queries. Both queries and query modifiers are stored in the catalog, and query modifiers are saved in the catalog independently (not related to queries). When a report is run using a Java application that uses the Engine Bean, the Logi JReport aPI will construct the SQL statement based on the query used in the report and may substitute the WHERE clause in the SQL statement if there is a given query modifier.

The query modifier can be stored in the catalog in two formats: structure and string. In the structure format, the groups of conditions are stored. The query modifier consists of many condition groups and the groups are connected by a logical operator. Each condition consists of many conditions and the conditions are also connected by a logical operator. Each condition consists of a left expression, the relationship operator and a right expression. In string format, the text of the query modifier is stored.

Before running a report, you can specify a query modifier to the Logi JReport system via the Engine Bean, so that you can generate the report on different data. You cannot run the report from the standard Logi JReport Server user interface.

**To add a query modifier in a catalog:**

1. [Open the catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500010063141-Creating-Opening-and-Saving-Catalogs#Open) to which you want to add the query modifier.
2. In the Catalog Manager, expand the desired data source and then the **Queries** node.
3. Right-click the **Query Modifiers** node and select **New Query Modifier** from the shortcut menu. The [Query Modifier Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500010032242-Query-Modifier-Editor-Dialog) appears.

   ![Query Modifier Editor](https://devnet.logianalytics.com/hc/article_attachments/4404901141143/qrymdfr.gif)
4. Enter a name for the query modifier in the Name text box and specify its type in the Type drop-down list, Structure or String.
5. Select a query from the Query drop-down list to build the query modifier. You can select the **Show Query** button to view the query if required.
6. In the editing area, edit the query modifier as required.

   If String type has been selected, a text editor will be shown where you can type in the WHERE clause. If the Structure type has been selected, a condition editor will be displayed where you can construct the query modifier by selecting buttons (for details about how to set the condition, see [Filtering with the filter format](https://devnet.logianalytics.com/hc/en-us/articles/1500010034642-Creating-Queries-in-a-Catalog#Filter)).
7. Select the **Check** button to check the validity of the query modifier according to the query.

   The validity of a query modifier is defined as: all the fields and formulas referred to by the query modifier are available to the chosen query. This validation check also ensures that the query modifier will work with the specified query.
8. Select the **Show SQL** button to view the string of the query modifier.
9. Select **OK** to create the query modifier.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010070721-Locking-Queries) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010034602-Cached-Query-Results)
