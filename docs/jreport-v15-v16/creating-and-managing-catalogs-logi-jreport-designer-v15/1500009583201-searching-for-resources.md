---
title: "Searching for Resources"
id: 1500009583201
section: "Creating and Managing Catalogs - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009583201-Searching-for-Resources
updated_at: 2021-07-24T05:56:12Z
---

# Searching for Resources

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583181-Setting-Resource-Properties)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562782-Filtering-Resources)

# Searching for Resources

When there are many resources in a catalog, sometimes you may find that it is difficult to locate where a resource is. The Catalog Manager provides you with a search function which enables you to search resources in the leaf node of the catalog data resource tree.

**To search resources in a catalog:**

1. In the Catalog Manager, select **Search** on the toolbar. The [Search](https://devnet.logianalytics.com/hc/en-us/articles/1500009567642-Search-Dialog) dialog appears.

   ![Search dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893800343/srch.gif)
2. Provide a search condition in the Search Expression text field. Use "\*" to stand for any string, and use "?" to stand for any character.
3. Select the **Case Sensitive** checkbox if you want Logi JReport to distinguish between uppercase and lowercase characters when searching.
4. Specify the search scope:
   * **Selected Resources**: Logi JReport will search from the resources you have selected in the Catalog Manager resource tree before you bring out the dialog.
   * **Search In**: If there are multiple data sources in this catalog, select the required data source from the drop-down list. To search from all data sources, select All.
5. Select **Search** to start searching.

   ![Search Result panel](https://devnet.logianalytics.com/hc/article_attachments/4404893794327/rptenv_srchrst.gif)

   All the matched results will be listed in the Search Result panel which has three columns: Resource Name, Resource Type and Resource Path. You can sort the search result alphabetically by selecting the column headers. Select an item from the Search Result panel, the data resource node that contains it will be expanded and with that item highlighted in the Catalog Manager.

For example, if you want to find the DBField Customer Name in the Queries node, first select the node in the Catalog Manager, select **Search** on the toolbar, then in the Search dialog, input **Customer Name**  in the Search Expression field, check the scope as **Selected Resource** and select the **Search** button. The results will then be displayed in the Search Result panel. You can select any of the results to highlight it in the catalog resource tree.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583181-Setting-Resource-Properties)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562782-Filtering-Resources)
