---
title: "Managing Datasets in Page Report"
id: 7985371620375
section: "Page Report Studio Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/7985371620375-Managing-Datasets-in-Page-Report
updated_at: 2022-10-31T17:15:24Z
---

# Managing Datasets in Page Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741438849559-Using-Dynamic-Resources-in-Page-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741462882967-Sorting-Page-Report-Data)

# Managing Datasets in Page Report

This topic describes how you can manage the datasets that a page report applies, for example, create more datasets in the report, specify the data fields to include in the datasets, and filter the datasets.

When you run a report, Engine fetches data from the datasets the report applies and displays the report according to the report template. A dataset is the set of data built from the result of a data resource: query, stored procedure, imported SQL, imported APE, user-defined data source, hierarchical data source, or business view, and can optionally apply filter conditions. You can leverage datasets amongst different data components in the same report, to optimize the overall performance by running a dataset once and caching it for all data components that apply the dataset to reuse.

This topic contains the following sections:

* [Creating a Dataset](#Create)
* [Adding/Removing Data Fields in a Dataset](#Add)
* [Filtering a Dataset](#Filter)
* [Optimizing a Dataset](#Optimize)
* [Renaming a Dataset](#Rename)
* [Removing a Dataset](#Remove)

To manage the datasets in a page report, navigate to **Menu** > **Report** > **Manage Datasets** to display the [Manage Datasets dialog box](https://devnet.logianalytics.com/hc/en-us/articles/7985360431639-Manage-Datasets-Dialog-Box-Properties).

![Manage Datasets dialog box](https://devnet.logianalytics.com/hc/article_attachments/9905574828183/mngdtst.gif)

## Creating a Dataset

When you bind data to the report body or specify the data resource you want to use for a data component, you create a dataset implicitly in the corresponding report. In the Manage Datasets dialog box, you can also create datasets explicitly in a report so you can use them directly in the report.

1. Select **New**.
   Server displays the New Dataset dialog box.
2. From the Choose Data from drop-down list, select a business view on which you want to create the dataset.
3. In the **New Dataset Name** text box, type the name of the dataset.
4. Select **OK** to create the dataset based on the specified business view.
5. Add the data fields you want to include in the dataset as shown in the next section.

## Adding/Removing Data Fields in a Dataset

For any dataset, Server automatically adds fields to it when you add fields to the data components that use the dataset, and removes the fields from the dataset once you remove them from the data components; therefore, there generally is no need to ever add or remove fields from a dataset specifically. However, you can still manually add or remove data fields from a dataset if you want. To do this, in the **Dataset List** box, select the dataset you want to edit, then in the **Data** tab,

**To add more data fields to the dataset**

Select the fields in the **Resources** box, and then select the Add button ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/9905612569111/btn_additem.gif) to add them to the dataset. A dataset created from a business view can contain view elements and [dynamic resources](https://devnet.logianalytics.com/hc/en-us/articles/5741438849559-Using-Dynamic-Resources-in-Page-Report) of the business view.

**To remove an unnecessary data field from the dataset**

Select the field in the **Dataset Resources** box and select the **Remove** button ![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/9905574572823/btn_rmvitem.gif). You can only remove the fields which are not used by any data component created on the dataset, either directly or indirectly.

## Filtering a Dataset

1. In the Dataset List box, select the dataset you want to filter.
2. Select the **Filter** tab.
3. Define the filter conditions. For more information, refer to [Applying Filters to Datasets](https://devnet.logianalytics.com/hc/en-us/articles/5741469268887-Applying-Filters-to-Page-Report#BV) (start from step 2).

## Optimizing a Dataset

You can increase or decrease the scope of retrieved data for a dataset in a page report, and therefore make a balanceable decision between better performance and special usage cases/demands.

1. In the Dataset List box, select the dataset that you want to optimize.
2. Select **Optimize Dataset**. Server displays the Optimize Dataset dialog box.
3. Choose a retrieved data scope for the dataset.
   * **Only Resources Used in Report**  
     Select it if you only want to retrieve data resources used in the current report at runtime. This way ensures the best performance since the least data is retrieved. This is always the default.
   * **All Resources in Dataset**  
     Select it if you want to retrieve all data resources defined in the dataset at runtime. Unless you [manually added data fields to the dataset](#Add), this is the same as Only Resources Used in Report.
   * **All Resources in Business View**  
     Select it if you want to retrieve all data resources in the business view on which the dataset is based at runtime. This usually leads to lower performance and is not of any benefit unless you expect to often need to add more fields to the report.
4. Select **OK** to optimize the dataset.

## Renaming a Dataset

1. In the Dataset List box, select the dataset name that you want to modify.
2. Type a new name in the text box.

## Removing a Dataset

1. In the Dataset List box, select the dataset that you want to remove.
2. Select **Remove**.
3. Select **Yes** in the prompted message box to confirm the removal.

   You cannot remove any dataset that is used by a data component. If you want to do this, you need to first remove the data component which references this dataset.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741438849559-Using-Dynamic-Resources-in-Page-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741462882967-Sorting-Page-Report-Data)
