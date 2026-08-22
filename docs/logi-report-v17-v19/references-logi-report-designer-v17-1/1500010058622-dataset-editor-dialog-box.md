---
title: "Dataset Editor Dialog Box"
id: 1500010058622
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010058622-Dataset-Editor-Dialog-Box
updated_at: 2021-07-23T19:15:14Z
---

# Dataset Editor Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058582-Data-Mapping-Editor-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058642-Dataset-Filter-Dialog-Box)

# Dataset Editor Dialog Box

You can use the Dataset Editor dialog box to [edit the selected dataset](https://devnet.logianalytics.com/hc/en-us/articles/1500010062542-Creating-and-Managing-Datasets#Manage). This topic describes the options in the dialog box.

Designer displays the Dataset Editor dialog box when you select the More Options button, then select the Existing Dataset radio button, select an existing dataset and select the Edit button in the Data screen of the report wizard when creating a data component using a query resource in a page report.

The dialog box contains the following tabs:

* [Data Tab](#Data)
* [Filter Tab](#Filter)

You see these buttons in both tabs:

**OK**

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## Data Tab

Use this tab to add extra data fields to the dataset or remove existing data fields from the dataset.

![Dataset Editor - Data](https://devnet.logianalytics.com/hc/article_attachments/4404856980375/dtstedtr_dt.gif)

**Available Resources**

The box lists all the DBFields in the query resource on which the dataset is created, as well as the parameters and valid formulas of these DBFields in the same catalog data source as the query resource.

Dataset Resources

The box lists all the fields that you specify to include in the dataset.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add button**

Select to add the specified data field to the dataset.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)**Remove button**

Select to remove the specified data field from the dataset. You can only remove the fields that are not used by any data component created on the dataset, either directly or indirectly.

![Remove All button](https://devnet.logianalytics.com/hc/article_attachments/4404848392215/btn_rmvall.gif)**Remove All button**

Select to remove all the data fields from the dataset. When you select the button, Designer only removes the unused data fields actually. When you open the dialog box the next time, you can see that the data fields used by data components created on the dataset still display in the Dataset Resources box.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**

Select to move the specified data field higher in the display order.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**

Select to move the specified data field lower in the display order.

## Filter Tab

Use this tab to specify conditions to filter the dataset.

Designer displays the same options in the tab as in the [Dataset Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058642-Dataset-Filter-Dialog-Box).

![Dataset Editor - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404848589079/dtstedtr_fltr.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058582-Data-Mapping-Editor-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058642-Dataset-Filter-Dialog-Box)
