---
title: "Result Properties"
id: 1500009715021
section: "Logi JReport Server Dialogs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009715021-Result-Properties
updated_at: 2021-11-03T06:57:38Z
---

# Result Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009715041-Resource-Allocation)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009715061-Schedule)

# Result Properties

The Result Properties dialog helps you to [set the properties of a specified result](https://devnet.logianalytics.com/hc/en-us/articles/1500009717861-Changing-Resource-Properties). It contains the following two tabs: [General](#General) and [Permission](#Permission).

**OK**

Retains the settings and submits the task to server.

**Cancel**

Cancels any settings and closes the dialog.

**Reset**

Discards your modifications and restores the dialog to its default status.

**Help**

Displays the help document about this feature.

## General

Specifies the general properties of the result.

![Result Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4412131460887/prptyrslt_gen.gif)

**Resource Path**

Shows the resource path.

**Resource Node Name**

Specifies the name for the result.

**Resource Type**

Shows the type of the resource.

**Resource Description**

Specifies the description of the result.

**[Custom Field Name]**

Specifies value of the custom field for the result. A [custom field](https://devnet.logianalytics.com/hc/en-us/articles/1500009717761-Working-with-Custom-Fields) can be regarded as a resource property and is available when it is enabled.

**Apply Archive Policy**

Applies an [archive policy](https://devnet.logianalytics.com/hc/en-us/articles/1500009717941-Applying-an-Archive-Policy) to the result versions.

* **Archive as New Version**  
   Specifies whether to use multiple versions for the result.
  + **Maximum Number of Versions**  
     Specifies the maximum number of versions that will be listed in the version table of the result. The default value is 0, which means that the version number is unlimited.
* **Replace Old Version**  
   Specifies to replace the old version when a new version is generated.

## Permission

Specifies permissions of roles/users/groups on the result. This tab is available when the result is in a public folder and when you have the Grant permission on the result.

![Result Properties dialog - Permission tab](https://devnet.logianalytics.com/hc/article_attachments/4412112605719/prptyrslt_prmsn.gif)

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

Select a role/user/group in the Selected box and then select the [permissions](https://devnet.logianalytics.com/hc/en-us/articles/1500009718881-Managing-Permissions) you would like the role/user/group to have on the result.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009715041-Resource-Allocation)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009715061-Schedule)
