---
title: "Linking Resources and Catalogs"
id: 5741474194455
section: "Managing Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741474194455-Linking-Resources-and-Catalogs
updated_at: 2022-10-31T17:18:07Z
---

# Linking Resources and Catalogs

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741438178199-Changing-Resource-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741461964439-Sharing-Web-Reports)

# Linking Resources and Catalogs

You can link a resource, such as a report or a library component, with a catalog in Logi Report, without the need of putting them in one folder. This topic describes the benefits of linking resources and catalogs and how you can set linked catalogs.

The benefits of a linked catalog compared to a copied catalog are:

* There is no need to also copy the catalog to the destination directory when you save a resource to a different location.
* When you update the linked catalog, the resources that use the catalog can run with the updated version. However, Logi Report does not automatically update the copied catalog if you update its original catalog since they are two independent versions.
* When the resource and its linked catalog are not in the same directory, the resource can still run with the catalog. You do not need to publish duplicate copies of the catalog that can lead to errors and inconsistencies as well as more memory and disk space usage. You can organize the reports into folders on the server without worrying about making copies of catalogs and maintaining multiple versions of the same catalog.

When you directly run a resource, the linked catalog has higher priority than the catalog in the same folder as the resource. Without linked catalog, the resource will run within the selected catalog in the same folder. As for Advanced Run and Schedule, the default selected catalog is the linked catalog if there is one, however, you can change it by the option **Select Another Catalog**.

## Setting Linked Catalog

You can set linked catalog at the server level, folder level, and resource level:

* To set linked catalog at the server level (you need to be an administrator):
  1. On the system toolbar of the Server Console, navigate to **Administration** > **Configuration** > **Advanced**. Server displays the Advanced page.
  2. Select **Enable Linked Catalog**.
  3. Select **Select Another Catalog** to specify the catalog as the linked catalog at the server level.
  4. Select **Save** to save the changes.
  5. Restart Server to make the settings take effect.
* To set linked catalog at the folder/resource level, go to the [Properties](https://devnet.logianalytics.com/hc/en-us/articles/5741438178199-Changing-Resource-Properties) dialog box of the folder/resource, select **Enable Linked Catalog**, then specify the linked catalog. You can specify a linked catalog for multiple resources at a time.
  + **Use Specified** - You can specify a linked catalog which can be any catalog in the server resource tree for the folder/resource.
  + **Use Inherited** - If the parent level of the folder/resource has a linked catalog, you can use the parent-level linked catalog as the linked catalog of the folder/resource. For the built-in resource folder, **Public Reports**, the parent level is the server level.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)

* If you modified the linked catalog in use after you submitted a scheduled task, the task still uses the previous catalog until you update the task information.
* When [saving a page report](https://devnet.logianalytics.com/hc/en-us/articles/5741462847767-Saving-a-Page-Report) in Page Report Studio, or [saving a web report](https://devnet.logianalytics.com/hc/en-us/articles/5741464615703-Saving-a-Web-Report) in Web Report Studio, you can also save the original catalog as a linked catalog for the page report.
* Server links the [analysis templates that you saved](https://devnet.logianalytics.com/hc/en-us/articles/5741407785751-Saving-Analysis-Templates) with their original catalogs. You cannot change linked catalogs of analysis templates.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741438178199-Changing-Resource-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741461964439-Sharing-Web-Reports)
