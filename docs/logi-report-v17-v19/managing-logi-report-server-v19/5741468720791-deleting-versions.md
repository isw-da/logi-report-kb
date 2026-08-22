---
title: "Deleting Versions"
id: 5741468720791
section: "Managing Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741468720791-Deleting-Versions
updated_at: 2022-10-31T17:18:10Z
---

# Deleting Versions

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741482308887-Applying-an-Archive-Policy)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741462230423--Advanced-Version-Topics-About-Version-Structure-and-Storage)

# Deleting Versions

After creating versions, periodically you may want to delete some expired or unused versions. This topic describes how you can remove versions manually or configure Server to delete them automatically.

When you remove the versions on the Server Console, Server also deletes the archive versions stored on disk in the history folder.

This topic contains the following sections:

* [Deleting Versions of a Resource Manually](#Manual)
* [Deleting Versions Automatically](#Auto)

## Deleting Versions of a Resource Manually

[Open the version table](https://devnet.logianalytics.com/hc/en-us/articles/5741462114583-Browsing-Versions) of the resource, then:

* To delete a version of the resource:
  + Select the version row and select **Edit** > **Delete** on the task bar.
  + Select the version row, right-click in the row, and select **Delete** on the shortcut menu.
  + Put the mouse pointer over the version row and select the **Delete** button ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/9905616261527/btn_dltobj.gif) on the floating toolbar.
* To delete multiple versions of the resource at a time, select the version rows, then select **Edit** > **Delete** on the task bar or right-click in any row and select **Delete** on the shortcut menu.

Server prompts you a message box, asking for your confirmation about the removal. Select **Yes** in the message box to remove the selected versions from the version table.

You can also use the [Database Archive](https://devnet.logianalytics.com/hc/en-us/articles/5741448346007-Managing-Server-Data#Archive) feature to remove versions older than a specified date or use [URL commands](https://devnet.logianalytics.com/hc/en-us/articles/5741485252503-Working-with-Server-via-URL#Version) to directly delete a specific version.

## Deleting Versions Automatically

There are two approaches to automatically deleting versions:

* **[Apply Archive Policy](https://devnet.logianalytics.com/hc/en-us/articles/5741482308887-Applying-an-Archive-Policy)**  
   You can use Archive Policy to control the number of versions to record in the version table of a resource.

  When creating a resource version, you can specify the maximum number of versions. If the number of versions exceeds the specified number, Server automatically removes the oldest version from the version list.

  For example, if you specify **Maximum Number of Versions** as 5, when it creates the sixth version, Server automatically removes the first version.
* **Result Auto-delete**  
   Result Auto-delete controls the duration of report result versions and result versions.

  When creating a report result version via Advanced Run or Schedule Run, or when modifying the properties of a result version, you can specify a certain period to keep the version. Server automatically removes the version from the corresponding version table after the number of days or the specified date.

  For example, if you specify "Result Expires in 30 days" for a report result version, Server automatically removes the version 30 days after its creation.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741482308887-Applying-an-Archive-Policy)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741462230423--Advanced-Version-Topics-About-Version-Structure-and-Storage)
