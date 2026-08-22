---
title: "Managing Datasets in a Report"
id: 5735576548887
section: "Manipulating Report Datasets - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735576548887-Managing-Datasets-in-a-Report
updated_at: 2022-11-02T08:17:41Z
---

# Managing Datasets in a Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735555312279-Filtering-Datasets-in-a-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735533990295-Editing-Properties-of-Datasets-in-a-Report-)

# Managing Datasets in a Report

This topic describes how you can manage the datasets that a report applies, for example, create more datasets in the report, specify the data fields to include in the datasets, and filter the datasets.

This topic contains the following sections:

* [Creating a Dataset](#Create)
* [Adding/Removing Data Fields in a Dataset](#Add)
* [Filtering a Dataset](#Filter)
* [Optimizing a Dataset](#Optimize)
* [Renaming a Dataset](#Rename)
* [Removing a Dataset](#Remove)

To manage the datasets in a report, [open the report](https://devnet.logianalytics.com/hc/en-us/articles/5735586443159-Opening-Reports), then navigate to **Report** > **Manage Datasets** to display the [Manage Datasets dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735543613335-Manage-Datasets-Dialog-Box).

![Manage Datasets dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898475519639/mngdtst.gif)

## Creating a Dataset

When you bind data to the report body or specify the data resource you want to use for a data component, you [create a dataset implicitly](https://devnet.logianalytics.com/hc/en-us/articles/5735586128791-Applying-Datasets-in-a-Report) in the corresponding report. In the Manage Dataset dialog box, you can also create datasets explicitly in a report so you can use them directly in the report.

1. Select **New** (Designer disables this button for library components). Designer displays the [New Dataset dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735566804375-New-Dataset-Dialog-Box).

   ![New Dataset dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898458485655/nwdtst.gif)
2. From the data source drop-down list, select the catalog data source that contains the data you need.
3. Designer displays the data resources you have added in the specified catalog data source in the resource box. Select the data resource on which to create the dataset. You can also select the first item in a resource node to create a data resource of the type to use for the dataset.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) When you select to add a new stored procedure or imported SQL for the dataset,

   * If the specified catalog data source contains only one connection other than the JDBC connection, Designer displays the [Get JDBC Connection dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735530237847-Get-JDBC-Connection-Information-Dialog-Box) for you to [set up the JDBC connection](https://devnet.logianalytics.com/hc/en-us/articles/5735521536663-Setting-Up-JDBC-Connections-in-a-Catalog) first.
   * If the specified catalog data source contains more than one connection, Designer displays the [Choose JDBC Connection dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735513226263-Choose-JDBC-Connection-Dialog-Box) for you to select the JDBC connection in the data source, via which you want to add the stored procedure or imported SQL. You can also select **<Add JDBC Connection...>** in the dialog box to create a JDBC connection and then add the stored procedure or imported SQL from the new connection.
4. In the **New Dataset Name** text box, type the name of the dataset.
5. Select **OK** to create the dataset based on the specified data resource.
6. Add the data fields you want to include in the dataset as shown in the next section.

## Adding/Removing Data Fields in a Dataset

For any dataset, Designer automatically adds fields to it when you add fields to the data components that use the dataset, and removes the fields from the dataset once you remove them from the data components; therefore, there generally is no need to ever add or remove fields from a dataset specifically. However, you can still manually add or remove data fields from a dataset if you want. To do this, in the **Dataset List** box, select the dataset you want to edit, then in the **Data** tab,

**To add more data fields to the dataset**

Select the fields in the **Available Resource** box and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif) to add them to the dataset. You can also select a field and drag it to the **Dataset Resources** box.

* A dataset built on a query data resource can contain all DBFields in the data resource, and the parameters and valid formulas of these DBFields in the same catalog data source.
* A dataset created from a business view can contain view elements and [dynamic resources](https://devnet.logianalytics.com/hc/en-us/articles/5735534296599-Using-Dynamic-Resources-and-Local-Parameters-in-a-Report) of the business view.

**To remove an unnecessary data field from the dataset**

Select the field in the **Dataset Resources** box and select **Remove**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/9898422552599/btn_rmvarrow.gif). You can only remove the fields that are not used by any data component applying this dataset, either directly or indirectly. To remove all the data fields in a dataset, select **Remove All**![Remove All button](https://devnet.logianalytics.com/hc/article_attachments/9898422565655/btn_rmvall.gif), however, when you select the button, Designer only removes the unused data fields actually. When you open the dialog box the next time, you can find that the data fields used by data components that apply the dataset still display in the Dataset box.

## Filtering a Dataset

1. In the Dataset List box, select the dataset you want to filter.
2. Select the **Filter** tab.
3. [Define the filter conditions](https://devnet.logianalytics.com/hc/en-us/articles/5735555312279-Filtering-Datasets-in-a-Report).

## Optimizing a Dataset

You can increase or decrease the scope of retrieved data for a dataset in a page or ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")web report, and therefore make a balanceable decision between better performance and special usage cases/demands.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) You cannot apply the Optimize Dataset feature to datasets in a library component. For these datasets, you can use the [Prefetch](https://devnet.logianalytics.com/hc/en-us/articles/5735525923095-Business-View-Properties#Prefetch) property on the business views for similar purpose.

1. In the Dataset List box, select the dataset that you want to optimize.
2. Select **Optimize Dataset**. Designer displays the Optimize Dataset dialog box.

   ![Optimize Dataset dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898475546519/dtset_optmz.gif)
3. Choose a retrieved data scope for the dataset.
   * **Only Columns Used in Report**  
     Select it if you only want to retrieve data resources used in the current report at runtime. This way ensures the best performance since the least data is retrieved. This is always the default.
   * **All Columns in Dataset**  
     Select it if you want to retrieve all data resources defined in the dataset at runtime. Unless you [manually added data fields to the dataset](#Add), this is the same as Only Columns Used in Report.
   * **All Columns in Query**  
     Select it if you want to retrieve all data resources in the query on which the dataset is based at runtime. This usually leads to lower performance and is not of any benefit unless you expect the users to often need to add more fields to the report.

   ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) When the dataset is based on a business view, the option names are Only Resources Used in Report, All Resources in Dataset, and All Resources in Business View respectively.
4. Select **OK** to optimize the dataset.

## Renaming a Dataset

1. In the Dataset List box, select the dataset that you want to modify.
2. Double-click in the **Name** text box of the dataset.
3. Type a new name in the text box and select **Enter** on the keyboard to apply the change.

## Removing a Dataset

1. In the Dataset List box, select the dataset that you want to remove.
2. Select **Remove**.
3. Select **Yes** in the prompted message box to confirm the removal.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) You cannot remove any dataset that is used by a data component. If you want to do this, you need to first remove the data component which references this dataset.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735555312279-Filtering-Datasets-in-a-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735533990295-Editing-Properties-of-Datasets-in-a-Report-)
