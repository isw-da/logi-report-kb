---
title: "Manage Datasets Dialog"
id: 1500009587781
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009587781-Manage-Datasets-Dialog
updated_at: 2021-07-24T05:55:03Z
---

# Manage Datasets Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009587761-Manage-Customized-Controls-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009587841-Mapping-Table-Dialog)

# Manage Datasets Dialog

The Manage Datasets dialog appears when you select Report > Manage Datasets. It helps you to [manage the datasets](https://devnet.logianalytics.com/hc/en-us/articles/1500009592421-Creating-and-Managing-Datasets) created for the open report. [See the dialog](javascript:%20void(null)).

![Manage Datasets dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889298711/mngdtst.gif)

The following are details about options in this dialog:

**Dataset List**

Lists all the datasets that you created for the open report.

* **Name**  
   Shows the name of the dataset.
* **Data Source**  
   Shows the data source in which the dataset is located.
* **Query**/**Business View**  
   Shows the data resource that the dataset is based on.

**Add**

Opens the [New Dataset](https://devnet.logianalytics.com/hc/en-us/articles/1500009566802-New-Dataset-Dialog) dialog to add a new dataset to the report. Available only when managing datasets in a page report.

**Remove**

Removes the specified dataset from the report. You cannot remove a dataset that is being used by any data component.

**Optimize Dataset**

Opens the [Optimize Dataset](https://devnet.logianalytics.com/hc/en-us/articles/1500009566982-Optimize-Dataset-Dialog) dialog to optimize the selected dataset. Available only when managing datasets in a page report.

**Data tab**

Modifies fields in the selected dataset.

* **Available Resource box**  
   Lists all the resources that can be added to the dataset.

  For a dataset created on data resource such as query, stored procedure, imported SQL, UDS, and HDS, it lists all the DBFields in the data resource, as well as parameters and valid formulas in the catalog data source where the data resource is added.

  For a dataset created on a business view, it lists all the view elements and the dynamic resources created in the report.
* **Dataset box**  
   Lists the fields that are added to the dataset.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)  
   Adds the selected fields to the dataset.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)  
   Removes the selected fields from the dataset. Only the fields which are not used by any data component created on the dataset, either directly or indirectly, can be removed.
* ![Remove All button](https://devnet.logianalytics.com/hc/article_attachments/4404889274263/btn_rmvall.gif)  
   Remove all the data fields from the dataset. When you select the button, only the unused data fields will be removed actually. When you enter the dialog the next time, you will find that the data fields used by data components created on the dataset will still display in the Dataset box.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)  
   Moves the specified field one step up.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)  
   Moves the specified field one step down.

**Filter tab**

Sets filter conditions for data in the selected dataset.

The tab varies based on the data resource on which the selected dataset is created.

If the dataset is created on a data resource such as query, stored procedure, imported SQL, UDS, and HDS, the options in the tab as the same as those in the [Dataset Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009565142-Dataset-Filter-Dialog) dialog.

If the dataset is created on a business view, the options in the tab are as follows:

* **Filter**  
   Lists all the predefined filters of the business view on which the dataset is created. Select one from the drop-down list to apply, or select User Defined and define a new filter according to your requirements.
* The other options in the tab as the same as those in the [Condition panel of the Predefined Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009567062-Predefined-Filter-Dialog#Condition) dialog.

**OK**

Applies the changes and closes the dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Apply**

Applies the changes and leaves the dialog open.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009587761-Manage-Customized-Controls-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009587841-Mapping-Table-Dialog)
