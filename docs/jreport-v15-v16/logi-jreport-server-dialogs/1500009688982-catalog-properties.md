---
title: "Catalog Properties"
id: 1500009688982
section: "Logi JReport Server Dialogs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009688982-Catalog-Properties
updated_at: 2021-11-03T06:57:40Z
---

# Catalog Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009714561-Auditing)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009714581-Change-Password)

# Catalog Properties

The Catalog Properties dialog helps admin users to [set the properties of a specified catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009717861-Changing-Resource-Properties). It contains the following two tabs: [General](#General) and [Permission](#Permission).

**OK**

Retains the settings and submits the task to the server.

**Cancel**

Cancels any settings and closes the dialog.

**Reset**

Discards your modifications and restores the dialog to its default status.

**Help**

Displays the help document about this feature.

## General

Specifies the general properties of the catalog.

![Catalog Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4412131466519/prptyctlg_gen.gif)

**Resource Path**

Shows the resource path.

**Resource Node Name**

Specifies the name for the catalog.

**Resource Type**

Shows the type of the resource.

**Resource Description**

Specifies the description of the catalog.

**[Custom Field Name]**

Specifies value of the custom field for the catalog. A [custom field](https://devnet.logianalytics.com/hc/en-us/articles/1500009717761-Working-with-Custom-Fields) can be regarded as a resource property and is available when it is enabled.

**Apply Archive Policy**

Applies an [archive policy](https://devnet.logianalytics.com/hc/en-us/articles/1500009717941-Applying-an-Archive-Policy) to the catalog versions.

* **Archive as New Version**  
   Specifies whether to use multiple versions for the catalog.
  + **Maximum Number of Versions**  
     Specifies the maximum number of versions that will be listed in the version table of the catalog. The default value is 0, which means that the version number is unlimited.
* **Replace Old Version**  
   Specifies to replace the old version when a new version is generated.

## Permission

Specifies permissions of roles/users/groups on the catalog. This tab is available when the catalog is in a public folder.

![Catalog Properties dialog - Permission tab](https://devnet.logianalytics.com/hc/article_attachments/4412131466775/prptyctlg_prmsn.gif)

**Enable Setting Permissions**

Enables the setting of permissions.

**Available**

Lists the roles/users/groups to which you can assign permissions.

* **Role**  
   If checked, all roles will be displayed in the Available box for you to assign permissions.
* **User**  
   If checked, all users will be displayed in the Available box for you to assign permissions.
* **Group**  
   If checked, all groups will be displayed in the Available box for you to assign permissions.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4412112531223/btn_add.gif)

Adds the selected role, user or group to the Selected box.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4412112531735/btn_rmv.gif)

Removes the selected role, user or group from the Selected box.

**Selected**

Select a role/user/group in the Selected box and then select the [permissions](https://devnet.logianalytics.com/hc/en-us/articles/1500009718881-Managing-Permissions) you would like the role/user/group to have on the catalog.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009714561-Auditing)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009714581-Change-Password)
