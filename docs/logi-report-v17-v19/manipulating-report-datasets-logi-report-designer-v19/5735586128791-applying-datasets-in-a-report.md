---
title: "Applying Datasets in a Report"
id: 5735586128791
section: "Manipulating Report Datasets - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735586128791-Applying-Datasets-in-a-Report
updated_at: 2022-11-02T08:23:48Z
---

# Applying Datasets in a Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/7933644552087/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735555287063-Manipulating-Report-Datasets)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/7933656663191/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735555312279-Filtering-Datasets-in-a-Report)

# Applying Datasets in a Report

You can apply a dataset to the body of a report and to each data component in the report. You may want to share datasets in the same report whenever possible, which can have a dramatic effect on the performance of your reports in the runtime environment. This is because Logi Report Engine creates each dataset by running a query against the database, and that is the most expensive part of running a report in terms of execution time. Even when two datasets are based on the same data resource, Logi Report Engine still runs the query separately for each dataset. However, by leveraging datasets amongst different data components in a report, you can optimize the overall performance by running a dataset once and caching it for all data components that apply the dataset to reuse. This topic describes how you can apply and edit datasets in a report.

This topic contains the following sections:

* [Binding a Dataset to the Report Body](#Body)
* [Specifying Dataset for a Data Component](#DC)
* [Editing a Dataset](#Edit)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/7933685587863/noteicon.jpg) When applying a dataset created from a hierarchical data source, you need to pay attention to the [unique features of HDS](https://devnet.logianalytics.com/hc/en-us/articles/5735527967639-Developing-Reports-from-Hierarchical-Data-Sources).

## Binding a Dataset to the Report Body

When you [create a blank page report tab](https://devnet.logianalytics.com/hc/en-us/articles/5735569787671-Creating-Reports#Tab), you need to specify a dataset to bind to its report body. You can also bind a dataset explicitly to the report body, so you can use it directly for objects in the report.

**To bind a dataset to the report body when creating a blank page report tab**

In the [Choose Data dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565124375-Choose-Data-Dialog-Box):

![Choose Data dialog box](https://devnet.logianalytics.com/hc/article_attachments/7933648957335/chsdt.gif)

Select the required data resource from the resource tree. Designer then automatically creates a dataset based on the data resource in the page report. When the predefined data resources are not what you want, you can select the first item in the corresponding resource node to create or add a data resource of the type in the catalog. If you select a query ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/7933646501655/___newv19.png "New for version 19.")or business view, you can select **Edit** to modify the [query](https://devnet.logianalytics.com/hc/en-us/articles/5735547138327-Creating-Queries-in-a-Catalog) or [business view](https://devnet.logianalytics.com/hc/en-us/articles/5735576514071-Creating-Business-Views-in-a-Catalog). The dataset is empty until you add data fields to display in data components applying the dataset.

If you want to use an existing dataset in the current page report for the page report tab, select **More Options**, then select **Existing Dataset** and select a dataset. You can select **Edit** to [modify the specified dataset](#Edit), or select **<New Dataset...>** to [create a dataset](https://devnet.logianalytics.com/hc/en-us/articles/5735576548887-Managing-Datasets-in-a-Report#NewDataset) in the page report.

**To bind a dataset to the report body explicitly**

1. Switch to the web report, library component, or the report tab in a page report.
2. Navigate to **Report** > **Bind Data**, or right-click any blank area in the report body and select **Bind Data** from the shortcut menu. Designer displays the [Bind Data dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565057943-Bind-Data-Dialog-Box) with different options according to the report type: page/web report or library component.
   * To bind data to a page or web report：

     ![Bind Data dialog box](https://devnet.logianalytics.com/hc/article_attachments/7933690155799/bddt.gif)

     + To bind a new dataset to the report body, select **New Dataset**, then select a data resource in the resource tree to create a dataset based on it. When the predefined data resources are not what you want, you can also select the first item in the corresponding resource node to create or add a data resource of the type in the current catalog. When you select a query ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/7933646501655/___newv19.png "New for version 19.")or business view, you can select **Edit** to modify the query or business view.
     + To bind an existing dataset in the report to the report body, select **Existing Dataset** and then select a dataset. You can select **Edit** to [modify the specified dataset](#Edit), or select **<New Dataset...>** to [create a dataset](https://devnet.logianalytics.com/hc/en-us/articles/5735576548887-Managing-Datasets-in-a-Report#NewDataset) in the report.
   * To bind data to a library component, choose a business view from the predefined business views in the current catalog. Designer then automatically creates a dataset based on the business view in the library component.

     ![Bind Data dialog box](https://devnet.logianalytics.com/hc/article_attachments/7933690165015/bddt_bv.gif)
3. Select **OK** to bind the dataset.
4. Select any blank area in the report body and you can locate the dataset bound to it in the Data panel.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/7933685587863/noteicon.jpg) Once you have bound a dataset to the report body and created any data component in the report which inherits the dataset, if you change the bound dataset of the report body to another one but the new dataset does not contain the same DBFields as the original one, Designer marks the invalid fields with a red cross icon in the data component. You cannot run the report until you update the data component or the new dataset to fix all the unmatched fields.

![Unmatched Fields in Newly Bound Data](https://devnet.logianalytics.com/hc/article_attachments/7933634747287/dtset_apply_bddt.gif)

## Specifying Dataset for a Data Component

When you create or edit a data component using the component wizard in a report, you need to specify a dataset for the data component. You can either create a dataset in the report to use or apply an existing dataset in the report. However, you cannot share datasets in library components, meaning, each data component in a library component should always be based on a new dataset.

**To specify dataset for a data component in a page or web report**

In the Data screen of the component wizard or [Choose Data dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565124375-Choose-Data-Dialog-Box) for a KPI:

![Specify Dataset for Data Component in Report](https://devnet.logianalytics.com/hc/article_attachments/7933690188951/dtset_apply_rpt.gif)

Select a predefined data resource in the current catalog from the resource tree, or select the first item in the corresponding resource node to create or add a data resource of the type in the catalog. When you select a query ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/7933646501655/___newv19.png "New for version 19.")or business view, you can select **Edit** to modify the query or business view. Designer then automatically creates a dataset based on the specified data resource in the report and applies it to the data component. The dataset is empty until you add data fields to display in the data component.

If you want to use an existing dataset in the report, select **More Options** and then:

* Select **Existing Dataset** and select a dataset from the dataset list. You can select **Edit** to [modify the specified dataset](#Edit), or select **<New Dataset...>** to [create a dataset](https://devnet.logianalytics.com/hc/en-us/articles/5735576548887-Managing-Datasets-in-a-Report#NewDataset) in the report.

  ![Select from Existing Datasets](https://devnet.logianalytics.com/hc/article_attachments/7933663884055/dtset_apply_existing.gif)
* If you have specified to create the data component in an object that already applies a dataset, such as in a banded panel, Designer enables the **Current Dataset** radio button. Select it if you want the data component to use this current dataset, meaning, inherit the dataset from its parent object.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/7933685587863/noteicon.jpg)

* Geographic maps cannot use inherited dataset.
* After you have bound a dataset to the report body, when you insert a data component in the cell of a tabular that is directly inside the report body, or in the cell of a nested tabular and the parent of the outermost tabular is the report body, you can also use the Current Dataset option to have the data component inherit dataset from the report body.

**To specify dataset for a data component in a library component**

In the Data screen of the component wizard or [Choose Data dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565124375-Choose-Data-Dialog-Box) for a KPI, select a predefined business view in the current catalog from the resource tree. Designer then automatically creates a dataset based on the business view in the library component and applies it to the data component. The dataset is empty until you add data fields to display in the data component.

![Specify Dataset for Data Component in Library Component](https://devnet.logianalytics.com/hc/article_attachments/7933663891735/dtset_apply_lc.gif)

## Editing a Dataset

When you select an existing dataset in a page or ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/7933646501655/___newv19.png "New for version 19.")web report to bind to the report body or apply to a data component in the report, you can further edit the dataset to add or remove data fields from it or apply a filter to narrow down its data.

1. In the dialog box where you can select to use an existing dataset in the report, for example, the [Bind Data dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565057943-Bind-Data-Dialog-Box), [Choose Data dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565124375-Choose-Data-Dialog-Box), or the Data screen of the component wizard, select an existing dataset and select **Edit**. Designer displays the [Dataset Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735529002007-Dataset-Editor-Dialog-Box).

   ![Dataset Editor - Data](https://devnet.logianalytics.com/hc/article_attachments/7933634784279/dtstedtr_dt.gif)
2. In the **Data** tab, [add or remove data fields in the dataset](https://devnet.logianalytics.com/hc/en-us/articles/5735576548887-Managing-Datasets-in-a-Report#Add).
3. Select the **Filter** tab and specify the [filter conditions](https://devnet.logianalytics.com/hc/en-us/articles/5735555312279-Filtering-Datasets-in-a-Report).

   ![Dataset Editor - Filter](https://devnet.logianalytics.com/hc/article_attachments/7933634801175/dtstedtr_fltr.gif)
4. Select **OK** to apply the changes.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/7933644552087/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735555287063-Manipulating-Report-Datasets)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/7933656663191/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735555312279-Filtering-Datasets-in-a-Report)
