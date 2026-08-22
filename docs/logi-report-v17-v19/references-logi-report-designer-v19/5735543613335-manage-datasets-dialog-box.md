---
title: "Manage Datasets Dialog Box"
id: 5735543613335
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735543613335-Manage-Datasets-Dialog-Box
updated_at: 2022-11-02T04:39:43Z
---

# Manage Datasets Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735566696983-Manage-Customized-Controls-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735566747927-Mapping-Table-Dialog-Box)

# Manage Datasets Dialog Box

You can use the Manage Datasets dialog box to [manage datasets in a report](https://devnet.logianalytics.com/hc/en-us/articles/5735576548887-Managing-Datasets-in-a-Report). This topic describes the options in the dialog box.

Designer displays the Manage Datasets dialog box when you navigate to Report > Manage Datasets.

![Manage Datasets dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898475519639/mngdtst.gif)

Designer displays these options:

**Dataset List**

This box lists all the datasets you have created for the report.

* **Name**  
  This column shows the names of the datasets. You can select in the text box to edit the name.
* **Data Source**  
  This column shows the catalog data sources in which you have created the datasets.
* **Query**/**Business View**  
  This column shows the data resources based on which you have created the datasets.

**New**

Select to open the [New Dataset dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735566804375-New-Dataset-Dialog-Box) to add a new dataset in the report. Designer disables this button when you use the dialog box for managing datasets in a library component.

**Remove**

Select to remove the specified dataset from the report. You cannot remove a dataset that is being used by any data component.

**Optimize Dataset**

Select to optimizes the specified dataset. Designer disables this button when you use the dialog box for managing datasets in a library component.

**Data tab**

You can specify the data fields to include in the selected dataset in this tab.

* **Available Resources**  
  This box lists the resources you can use for the dataset.
  + For a dataset based on a query resource, the available resources include all DBFields in the query resource, and the parameters and valid formulas of these DBFields in the same catalog data source as the query resource.
  + For a dataset based on a business view, the available resources include all view elements of the business view and the dynamic resources you have created for the business view in the report.
* **Dataset Resources**  
  This box lists the data fields you add to the dataset.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif)**Add button**  
  Select to add the specified data fields in the Available Resources box to include in the dataset.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/9898422552599/btn_rmvarrow.gif)**Remove button**  
  Select to remove the specified data fields from the dataset. You can only remove the fields that are not used by any data component that uses the dataset, either directly or indirectly.
* ![Remove All button](https://devnet.logianalytics.com/hc/article_attachments/9898422565655/btn_rmvall.gif)**Remove All button**  
  Select to remove all data fields from the dataset. When you select this button, Designer only removes the unused data fields actually. When you open the dialog box the next time, you can find that the data fields which are used by data components created on the dataset still display in the Dataset Resources box.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif)**Move Up button**  
  Select to move the specified data field higher in the display order.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif)**Move Down button**  
  Select to move the specified data field lower in the display order.

**Filter tab**

You can specify conditions to filter the selected dataset in this tab.

Designer displays different options in the Filter tab according to the type of the data resource on which the dataset is based: query resource or business view. See [Dataset Filter Dialog Box](https://devnet.logianalytics.com/hc/en-us/articles/5735508603927-Dataset-Filter-Dialog-Box) for more information about the options.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Apply**

Select to apply all changes and leave the dialog box open.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735566696983-Manage-Customized-Controls-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735566747927-Mapping-Table-Dialog-Box)
