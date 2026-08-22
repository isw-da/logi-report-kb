---
title: "Query Modifiers"
id: 1500009636041
section: "Manipulating the Data Resources in a Catalog - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009636041-Query-Modifiers
updated_at: 2021-07-24T16:03:24Z
---

# Query Modifiers

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009613222-Locking-Queries) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009635961-Cached-Query-Results)

# Query Modifiers

Query modifiers, also called WHERE portions in Logi Report, are the WHERE clauses in SQL select statements. In Logi Report, the SQL select statements are called queries. Both queries and query modifiers are stored in the catalog, and query modifiers are saved in the catalog independently (not related to queries). When a report is run using a Java application that uses the Engine Bean, the Logi Report aPI will construct the SQL statement based on the query used in the report and may substitute the WHERE clause in the SQL statement if there is a given query modifier.

The query modifier can be stored in the catalog in two formats: structure and string. In the structure format, the groups of conditions are stored. The query modifier consists of many condition groups and the groups are connected by a logical operator. Each condition consists of many conditions and the conditions are also connected by a logical operator. Each condition consists of a left expression, the relationship operator and a right expression. In string format, the text of the query modifier is stored.

Before running a report, you can specify a query modifier to the Logi Report system via the Engine Bean, so that you can generate the report on different data. You cannot run the report from the standard Logi Report Server user interface.

**To add a query modifier in a catalog:**

1. [Open the catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009628301-Creating-Opening-and-Saving-Catalogs#Open) to which you want to add the query modifier.
2. In the Catalog Manager, expand the desired data source and then the **Queries** node.
3. Right-click the **Query Modifiers** node and select **New Query Modifier** from the shortcut menu. The [Query Modifier Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009609922-Query-Modifier-Editor-Dialog) appears.

   ![Query Modifier Editor](https://devnet.logianalytics.com/hc/article_attachments/4404904194583/qrymdfr.gif)
4. Type a name for the query modifier in the Name text box and specify its type in the Type drop-down list, Structure or String.
5. Select a query from the Query drop-down list to build the query modifier. You can select the **Show Query** button to view the query.
6. In the editing area, edit the query modifier as required.

   If String type has been selected, a text editor will be shown where you can type in the WHERE clause. If the Structure type has been selected, a condition editor will be displayed where you can construct the query modifier by selecting buttons (for details about how to set the condition, see [Filtering with the filter format](https://devnet.logianalytics.com/hc/en-us/articles/1500009635981-Creating-Queries-in-a-Catalog#Filter)).
7. Select the **Check** button to check the validity of the query modifier according to the query.

   The validity of a query modifier is defined as: all the fields and formulas referred to by the query modifier are available to the chosen query. This validation check also ensures that the query modifier will work with the specified query.
8. Select the **Show SQL** button to view the string of the query modifier.
9. Select **OK** to create the query modifier.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009613222-Locking-Queries) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009635961-Cached-Query-Results)
