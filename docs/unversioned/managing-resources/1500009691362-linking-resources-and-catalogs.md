---
title: "Linking Resources and Catalogs"
id: 1500009691362
section: "Managing Resources"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009691362-Linking-Resources-and-Catalogs
updated_at: 2021-11-03T06:56:54Z
---

# Linking Resources and Catalogs

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009717861-Changing-Resource-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009717901-Sharing-Reports)

# Linking Resources and Catalogs

A resource, such as a report or a library component, can be linked with a catalog in Logi JReport. The benefits of a linked catalog compared to a copied catalog are:

* There is no need to also copy the wanted catalog to the destination directory when saving the resource to a different location.
* When the linked catalog is updated, the resource using the catalog can run with the updated version. However, the copied catalog cannot be updated if its original catalog is updated since they are two independent versions.
* When the resource and its linked catalog are not in the same directory, the resource can still run with the catalog. You do not need to publish duplicate copies of the catalog that can lead to errors and inconsistencies as well as more memory and disk space usage. You can organize the reports into folders on the server without worrying about making copies of catalogs and maintaining multiple versions of the same catalog.

When directly running a resource, the linked catalog has higher priority than the catalog specified in the same folder as the resource (without linked catalog, the resource will run within the selected catalog in the same folder). As for Advanced Run and Schedule, the default selected catalog is the linked catalog if there is one, however, you can change it by the provided option Select Another Catalog.

## Setting Linked Catalog

Linked catalog can be set at server level, folder level, and resource level as follows:

* To set linked catalog at server level (this can only be done by administrators):
  1. In the Logi JReport Server console, point to **Administration** on the system toolbar, and then select **Configuration** > **Advanced** from the drop-down menu.
  2. In the Advanced page, check **Enable Linked Catalog**, then select the **Select Another Catalog** link to specify the catalog which will be used as the linked catalog at server level.
  3. Select **Save** to save the change.
  4. Restart Logi JReport Server to make the settings take effect.
* To set linked catalog at folder/resource level, go to the [Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009717861-Changing-Resource-Properties) dialog of the folder/resource, check **Enable Linked Catalog**, then specify the linked catalog as required. End users can specify a linked catalog for multiple resources at a time.
  + **Use Specified** - If checked, you can specify a linked catalog which can be any catalog in the server resource tree to the folder/resource.
  + **Use Inherited** - If a linked catalog has been specified on the parent level of the folder/resource, you can use the parent-level linked catalog as the linked catalog of the folder/resource. For the built-in resource folders, the Public Reports folder for example, the parent level is the server level; for the other folders or resources, the parent level is the parent folder.

**Notes:**

* If a schedule task has been submitted and then the linked catalog in use is modified, the task will still use the previous catalog until the task information is updated.
* When [saving a page report](https://devnet.logianalytics.com/hc/en-us/articles/1500009691682-Saving-the-Report) in Page Report Studio, you can also save the original catalog as a linked catalog for the page report. It is the same case when [saving a web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009719241-Saving-the-Report) in Web Report Studio.
* The [saved analysis templates](https://devnet.logianalytics.com/hc/en-us/articles/1500009686062-Saving-Analysis-Templates) are linked to their original catalogs. You cannot customize the analysis templates to be linked with a different catalog.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009717861-Changing-Resource-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009717901-Sharing-Reports)
