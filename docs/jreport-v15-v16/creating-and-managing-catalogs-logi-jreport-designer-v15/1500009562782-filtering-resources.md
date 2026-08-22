---
title: "Filtering Resources"
id: 1500009562782
section: "Creating and Managing Catalogs - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009562782-Filtering-Resources
updated_at: 2021-07-24T05:56:14Z
---

# Filtering Resources

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583201-Searching-for-Resources)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583141-Using-a-Reference-Table-to-Clarify-Resource-Relationships)

# Filtering Resources

The Catalog Manager allows you to filter the data resources in a catalog and show only the selected resources to you.

**To filter resources in a catalog:**

1. In the Catalog Manager, select **Filter View** on the toolbar. The [Filter View](https://devnet.logianalytics.com/hc/en-us/articles/1500009586881-Filter-View-Dialog) dialog appears.

   ![Filter View dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889362199/fltrvw.gif)
2. Provide a filter condition in the Filter Expression text box. Use "\*" to stand for any string, and use "?" to stand for any character. Also you can leave this text box blank.
3. Select the **Case Sensitive** checkbox if you want Logi JReport to distinguish between uppercase and lowercase characters when filtering.
4. In the Select the elements to include in the view box, check the resource types you want to remain in the catalog resource tree.
   * If you want to select/deselect all the resource types under one certain data source, check/uncheck the checkbox of the data source node.
   * If you want to select/deselect all the resource types in the box, select the **Select All**/**Deselect All** button.
5. Select the **OK** button to filter the resources.

   The filter result will be the union of the resources that match the filter condition and the selected resource types.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583181-Setting-Resource-Properties) [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583141-Using-a-Reference-Table-to-Clarify-Resource-Relationships)
