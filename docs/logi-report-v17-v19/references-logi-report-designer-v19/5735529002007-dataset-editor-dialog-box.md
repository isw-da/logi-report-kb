---
title: "Dataset Editor Dialog Box"
id: 5735529002007
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735529002007-Dataset-Editor-Dialog-Box
updated_at: 2022-11-02T04:14:50Z
---

# Dataset Editor Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735565537303-Data-Mapping-Editor-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735508603927-Dataset-Filter-Dialog-Box)

# Dataset Editor Dialog Box

You can use the Dataset Editor dialog box to [edit a dataset](https://devnet.logianalytics.com/hc/en-us/articles/5735586128791-Applying-Datasets-in-a-Report#Edit) in a page or ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")web report. This topic describes the options in the dialog box.

Designer displays the Dataset Editor dialog box when you select an existing dataset and select Edit in one of the following dialog boxes: [Bind Data dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565057943-Bind-Data-Dialog-Box), [Choose Data dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565124375-Choose-Data-Dialog-Box), or the Data screen of the component wizard.

This dialog box contains the following tabs:

* [Data Tab](#Data)
* [Filter Tab](#Filter)

Designer displays these buttons in all the tabs:

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## Data Tab

Use this tab to add extra data fields to the dataset or remove existing data fields from the dataset.

![Dataset Editor - Data](https://devnet.logianalytics.com/hc/article_attachments/9898464831767/dtstedtr_dt.gif)

**Available Resources**

This box lists the data fields you can use for the dataset.

* For a dataset based on a query resource, the available resources include all DBFields in the query resource, and the parameters and valid formulas of these DBFields in the same catalog data source as the query resource.
* ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")For a dataset based on a business view, the available resources include all view elements of the business view and the dynamic resources you have created for the business view in the current report.

**Dataset Resources**

This box lists the data fields you add to the dataset.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif)**Add button**

Select to add the specified data field in the Available Resources box to include in the dataset.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/9898422552599/btn_rmvarrow.gif)**Remove button**

Select to remove the specified data field from the dataset. You can only remove the fields that are not used by any data component created on the dataset, either directly or indirectly.

![Remove All button](https://devnet.logianalytics.com/hc/article_attachments/9898422565655/btn_rmvall.gif)**Remove All button**

Select to remove all data fields from the dataset. When you select this button, Designer only removes the unused data fields actually. When you open the dialog box the next time, you can see that the data fields used by data components created on the dataset still display in the Dataset Resources box.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif)**Move Up button**

Select to move the specified data field higher in the display order.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif)**Move Down button**

Select to move the specified data field lower in the display order.

## Filter Tab

Use this tab to specify conditions to filter the dataset.

Designer displays different options in the Filter tab according to the type of the data resource on which the dataset is based, query resource or ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")business view. See [Dataset Filter Dialog Box](https://devnet.logianalytics.com/hc/en-us/articles/5735508603927-Dataset-Filter-Dialog-Box) for more information about the options.

![Dataset Editor - Filter](https://devnet.logianalytics.com/hc/article_attachments/9898464836631/dtstedtr_fltr.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735565537303-Data-Mapping-Editor-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735508603927-Dataset-Filter-Dialog-Box)
