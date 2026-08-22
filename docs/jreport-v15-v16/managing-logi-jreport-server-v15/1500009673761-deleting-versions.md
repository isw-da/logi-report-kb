---
title: "Deleting Versions"
id: 1500009673761
section: "Managing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009673761-Deleting-Versions
updated_at: 2021-07-24T20:54:01Z
---

# Deleting Versions

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673721-Applying-an-Archive-Policy)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673801-Advanced-Version-Topics)

# Deleting Versions

After creating versions, periodically you may want to delete some expired or unused versions. You can choose to remove these versions manually or configure Logi JReport Server to delete them automatically. When removing the versions using the user interface, the archive versions stored on disk in the history folder are also physically deleted.

Below is a list of the sections covered in this topic:

* [Deleting Manually](#Manual)
* [Deleting Automatically](#Auto)

## Deleting Manually

To delete versions of a resource manually, first [open the version table](https://devnet.logianalytics.com/hc/en-us/articles/1500009673741-Browsing-Versions) of the resource, then:

* For administrators, in the version table, check the checkbox ahead of the versions that you want to remove and then select the **Delete** link.
* For end users, in the version table, find the version you want to remove, then:
  + Select the version row and select **Edit** > **Delete** on the task bar.
  + Select the version row, right-click in the row and select **Delete** on the shortcut menu.
  + Put the mouse pointer over the version row and select the **Delete** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920360855/btn_dltobj.gif).

After receiving "The version has been deleted" message, view the version information again. You will find that the version you selected has now been removed from the version table.

You can also use the [Database Archive](https://devnet.logianalytics.com/hc/en-us/articles/1500009673481-Archiving-and-Restoring-Server-Data) feature to remove versions older than a specified date or use [URL commands](https://devnet.logianalytics.com/hc/en-us/articles/1500009650542-Working-with-Logi-JReport-Server-Guide-v15-Server#Version) to directly delete a specific version.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Deleting Automatically

There are two approaches to automatically deleting versions:

* **[Apply Archive Policy](https://devnet.logianalytics.com/hc/en-us/articles/1500009673721-Applying-an-Archive-Policy)**  
   The Apply Archive Policy controls the number of versions that will be recorded in the version table of a resource.

  When creating a resource version, you can specify the maximum number that will be saved. If the number of versions exceeds the specified number, the oldest version will automatically be removed from the version list.

  For example, if you specify Maximum Number of Versions as 5, when the sixth version is created, the first version will automatically be removed.
* **Result Auto-delete**  
   Result Auto-delete controls the duration of report result versions and result versions.

  When creating a report result version via advanced running or scheduling or when modifying the properties of a result version, you can specify a certain period of time to keep the version. The version will automatically be removed from the version list after the number of days or the specified date.

  For example, if you specify "Result Expires in 30 days", it will be automatically removed 30 days after its creation.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673721-Applying-an-Archive-Policy)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673801-Advanced-Version-Topics)
