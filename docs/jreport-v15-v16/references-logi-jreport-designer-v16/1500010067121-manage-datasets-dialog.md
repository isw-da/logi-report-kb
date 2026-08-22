---
title: "Manage Datasets Dialog"
id: 1500010067121
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010067121-Manage-Datasets-Dialog
updated_at: 2021-07-24T10:38:37Z
---

# Manage Datasets Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010031642-Manage-Customized-Controls-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010067161-Mapping-Table-Dialog)

# Manage Datasets Dialog

The Manage Datasets dialog helps you to [manage the datasets](https://devnet.logianalytics.com/hc/en-us/articles/1500010070661-Creating-and-Managing-Datasets#Manage) created for the open library component or page report that is created using query resources. It appears when you select Report > Manage Datasets.

![Manage Datasets dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901144727/mngdtst.gif)

The following are details about options in this dialog:

**Dataset List**

Lists all the datasets that you created for the open report.

* **Name**  
   Shows the name of the dataset. You can select in the text box to edit the name.
* **Data Source**  
   Shows the data source in which the dataset is located.
* **Query**/**Business View**  
   Shows the data resource that the dataset is based on.

**New**

Opens the [New Dataset](https://devnet.logianalytics.com/hc/en-us/articles/1500010031902-New-Dataset-Dialog) dialog to add a new dataset to the report. Available only when managing datasets in a page report created using query resources.

**Remove**

Removes the specified dataset from the report. You cannot remove a dataset that is being used by any data component.

**Optimize Dataset**

Optimizes the selected dataset. Available only when managing datasets in a page report created using query resources.

**Data tab**

Modifies fields in the selected dataset.

* **Available Resources box**  
   Lists all the resources that can be added to the dataset.

  For a dataset created on a query resource, it lists all the DBFields in the data resource, as well as parameters and valid formulas of these DBFields in the same catalog data source as the data resource.

  For a dataset created on a business view, it lists all the view elements and the dynamic resources created for the business view in the report.
* **Dataset Resources box**  
   Lists the fields that are added to the dataset.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif)  
   Adds the selected fields to the dataset.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404901121047/btn_rmvarrow.gif)  
   Removes the selected fields from the dataset. Only the fields which are not used by any data component created on the dataset, either directly or indirectly, can be removed.
* ![Remove All button](https://devnet.logianalytics.com/hc/article_attachments/4404909117847/btn_rmvall.gif)  
   Remove all the data fields from the dataset. When you select the button, only the unused data fields will be removed actually. When you enter the dialog the next time, you will find that the data fields used by data components created on the dataset will still display in the Dataset Resources box.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif)  
   Moves the selected field one step up.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif)  
   Moves the selected field one step down.

**Filter tab**

Sets filter conditions for the selected dataset.

The tab varies based on the data resource on which the selected dataset is created.

If the dataset is created on a query resource, the options in the tab as the same as those in the [Dataset Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500010030362-Dataset-Filter-Dialog) dialog.

If the dataset is created on a business view, the options in the tab are as follows:

* **Filter**  
   Lists all the predefined filters of the business view on which the dataset is created. Select one from the drop-down list to apply, or select User Defined and define a new filter according to your requirements.
* The other options in the tab as the same as those in the [Condition panel](https://devnet.logianalytics.com/hc/en-us/articles/1500010032042-Predefined-Filter-Dialog#Condition) of the Predefined Filter dialog.

**OK**

Applies the changes and closes the dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Apply**

Applies the changes and leaves the dialog open.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010031642-Manage-Customized-Controls-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010067161-Mapping-Table-Dialog)
