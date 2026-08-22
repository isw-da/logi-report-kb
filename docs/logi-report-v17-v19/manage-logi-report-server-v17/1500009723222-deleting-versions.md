---
title: "Deleting Versions"
id: 1500009723222
section: "Manage Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009723222-Deleting-Versions
updated_at: 2021-07-25T07:18:56Z
---

# Deleting Versions

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009723202-Applying-an-Archive-Policy)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009723262-Advanced-Version-Topics)

# Deleting Versions

After creating versions, periodically you may want to delete some expired or unused versions. You can choose to remove these versions manually or configure Logi Report Server to delete them automatically. When removing the versions using the server console, the archive versions stored on disk in the history folder are also physically deleted.

You can either delete versions manually or make them deleted automatically.

**To delete versions of a resource manually:**

[Open the version table](https://devnet.logianalytics.com/hc/en-us/articles/1500009750201-Browsing-Versions) of the resource, then:

* To delete a version of the resource:
  + Select the version row and select **Edit** > **Delete** on the task bar.
  + Select the version row, right-click in the row and select **Delete** on the shortcut menu.
  + Put the mouse pointer over the version row and select the **Delete** button ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404942446871/btn_dltobj.gif) on the floating toolbar.
* To delete multiple versions of the resource at a time, select the version rows, then select **Edit** > **Delete** on the task bar or right-click in any row and select **Delete** on the shortcut menu.

Logi Report Server will then prompt you a message box, asking for your confirmation about the removal. Select **Yes** in the message box and the selected versions will be removed from the version table.

You can also use the [Database Archive](https://devnet.logianalytics.com/hc/en-us/articles/1500009723022-Managing-Server-Data#Archive) feature to remove versions older than a specified date or use [URL commands](https://devnet.logianalytics.com/hc/en-us/articles/1500009725002-Working-with-Logi-Report-Server#Version) to directly delete a specific version.

**To delete versions automatically:**

There are two approaches to automatically deleting versions:

* **[Apply Archive Policy](https://devnet.logianalytics.com/hc/en-us/articles/1500009723202-Applying-an-Archive-Policy)**  
   The Apply Archive Policy controls the number of versions that will be recorded in the version table of a resource.

  When creating a resource version, you can specify the maximum number that will be saved. If the number of versions exceeds the specified number, the oldest version will automatically be removed from the version list.

  For example, if you specify Maximum Number of Versions as 5, when the sixth version is created, the first version will automatically be removed.
* **Result Auto-delete**  
   Result Auto-delete controls the duration of report result versions and result versions.

  When creating a report result version via Advanced Run or Schedule Run or when modifying the properties of a result version, you can specify a certain period of time to keep the version. The version will automatically be removed from the corresponding version table after the number of days or the specified date.

  For example, if you specify "Result Expires in 30 days" for a report result version, the version will be automatically removed 30 days after its creation.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009723202-Applying-an-Archive-Policy)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009723262-Advanced-Version-Topics)
