---
title: "Binding Data to a Shape Map"
id: 1500009584121
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009584121-Binding-Data-to-a-Shape-Map
updated_at: 2021-07-24T05:55:59Z
---

# Binding Data to a Shape Map

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584141-Inserting-a-Shape-Map)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563522-Adding-Conditional-Formats-to-Shape-Map-Areas)

# Binding Data to a Shape Map

You can bind a shape map to a dataset, so as to show values on the shape map areas. To achieve it:

1. In the Shape Map Editor, select **Bind Data** on the toolbar, or select **Menu > Insert** > **Bind Data**. The [Shape Map Data Binding Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009566722-Shape-Map-Data-Binding-Wizard-Dialog) appears.
2. In the Data screen, select the data resource to bind with the shape map. If the given data resources are not what you want, select the first item  in the corresponding resource node to create one. When a query is selected, select the **Edit** button to [modify the query](https://devnet.logianalytics.com/hc/en-us/articles/1500009570662-Editing-a-Query) if required. Then a new [dataset](https://devnet.logianalytics.com/hc/en-us/articles/1500009592421-Creating-and-Managing-Datasets) based on the selected data resource is created in the page report.

   If you want to use an existing dataset in the current page report for the shape map, select the **More Options** button and then:

   * Check the **Existing Dataset** radio button and select a dataset. You can select the **Edit** button to modify the selected dataset in the [Dataset Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009586301-Dataset-Editor-Dialog) if necessary, or select the **<New Dataset...>** item to create a new dataset in the page report to use. It is always better to use an existing dataset rather than create a new one. Even when the two datasets are based on the same query, Logi JReport will still run the query separately for each dataset.
   * Check the **Current Dataset** radio button to make the shape map inherit the dataset from its parent.

   ![Shape Map Data binding Wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404889328407/mpdtbdingwzd_dt.gif)
3. In the Group screen, add a field as the grouping criteria to group data in the specified dataset, then specify the sorting direction of the group in the Sort column. You can add only one group by field. For more information about data grouping, see [Grouping the Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009563642-Grouping-the-Data).

   ![Shape Map Data binding Wizard - Group](https://devnet.logianalytics.com/hc/article_attachments/4404889328663/mpdtbdingwzd_grp.gif)
4. In the Summary screen, add the fields as the summary fields, and specify the function as required. Data in each group will then be calculated based on the selected fields using the specified function, and the summary results will be displayed accordingly on map areas the names of which match with values of the group by field.

   ![Shape Map Data Binding Wizard - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404893866391/mpdtbdingwzd_sum.gif)
5. In the Filter screen, define some filter conditions to filter the data displayed on the map areas. For how to define a filter, refer to [Filtering the Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009584321-Filtering-the-Data).

   ![Shape Map Data Binding Wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404893866647/mpdtbdingwzd_fltr.gif)
6. Select **Finish** to apply the settings and leave the dialog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584141-Inserting-a-Shape-Map)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563522-Adding-Conditional-Formats-to-Shape-Map-Areas)
