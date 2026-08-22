---
title: "Dataset Editor Dialog"
id: 1500009607762
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009607762-Dataset-Editor-Dialog
updated_at: 2021-07-24T16:04:50Z
---

# Dataset Editor Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009607702-Data-Mapping-Editor-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009607782-Dataset-Filter-Dialog)

# Dataset Editor Dialog

The Dataset Editor helps you to [edit the selected dataset](https://devnet.logianalytics.com/hc/en-us/articles/1500009635941-Creating-and-Managing-Datasets#Manage). It appears when you select the More Options button and select the Existing Dataset radio button, select an existing dataset and select the Edit button in the Data screen of the report wizard when creating a data component using a query resource in a page report.

The editor contains two tabs: [Data](#Data) and [Filter](#Filter).

**OK**

Applies the changes and closes the dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Help**

Displays the help document about this feature.

## Data

Adds extra data fields to the dataset or removes existing data fields from the dataset.

![Dataset Editor - Data](https://devnet.logianalytics.com/hc/article_attachments/4404904355863/dtstedtr_dt.gif)

**Available Resources**

Lists all the DBFields in the query resource on which the dataset is created, as well as parameters and valid formulas of these DBFields in the same catalog data source as the query resource.

**Dataset****Resources**

Lists all the fields that are included in the dataset.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif)

Moves the selected data field up a step.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif)

Moves the selected data field down a step.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif)

Adds the selected data field to the dataset.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)

Removes the selected data field from the dataset. Only the fields which are not used by any data component created on the dataset, either directly or indirectly, can be removed.

![Remove All button](https://devnet.logianalytics.com/hc/article_attachments/4404911605783/btn_rmvall.gif)

Removes all the data fields from the dataset. When you select the button, only the unused data fields will be removed actually. When you open the dialog the next time, you will find that the data fields used by data components created on the dataset will still display in the Dataset Resources box.

## Filter

Sets conditions to filter the dataset.

![Dataset Editor - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404904356119/dtstedtr_fltr.gif)

The options in the tab are the same as those in the [Dataset Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009607782-Dataset-Filter-Dialog) dialog.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009607702-Data-Mapping-Editor-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009607782-Dataset-Filter-Dialog)
