---
title: "Result Properties"
id: 1500009746302
section: "Logi Report Server Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009746302-Result-Properties
updated_at: 2021-07-24T00:48:41Z
---

# Result Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009774541-Resource-Allocation-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009774581-Schedule-Dialog-Box-Properties)

# Result Properties

This topic describes how you can use the Result Properties dialog box to [set the properties of a specified result](https://devnet.logianalytics.com/hc/en-us/articles/1500009748702-Changing-Resource-Properties).

This topic contains the following sections:

* [General Tab Properties](#General)
* [Permission Tab Properties](#Permission)

You see these elements on all the tabs:

**OK**

Select **OK** to apply any changes you made here.

**Cancel**

Select **Cancel** to close the dialog box without saving any changes.

**Reset**

Select **Reset** to restore the dialog box to its default status.

**Help**

Select **Help** to view information about the Result Properties dialog box.

## General Tab Properties

Specifies the general properties of the result.

![Result Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404880416663/prptyrslt_gen.gif)

**Resource Path**

Shows the resource path.

**Resource Node Name**

Specifies the name for the result.

**Resource Type**

Shows the type of the resource.

**Resource Description**

Specifies the description of the result.

**[Custom Field Name]**

Specifies value of the custom field for the result. A [custom field](https://devnet.logianalytics.com/hc/en-us/articles/1500009748662-Working-with-Custom-Fields) can be regarded as a resource property and is available when it is enabled.

**Apply Archive Policy**

Applies an [archive policy](https://devnet.logianalytics.com/hc/en-us/articles/1500009748742-Applying-an-Archive-Policy) to the result versions.

* **Archive as New Version**  
   Specifies whether to use multiple versions for the result.
  + **Maximum Number of Versions**  
     Specifies the maximum number of versions that will be listed in the version table of the result. The default value is 0, which means that the version number is unlimited.
* **Replace Old Version**  
   Specifies to replace the old version when a new version is generated.

## Permission Tab Properties

Specifies permissions of roles/users/groups on the result. This tab is available when the result is in a public folder and when you have the Grant permission on the result.

![Result Properties dialog - Permission tab](https://devnet.logianalytics.com/hc/article_attachments/4404885505687/prptyrslt_prmsn.gif)

**Enable Setting Permissions**

Enables the setting of permissions.

**Available**

Lists the roles/users/groups to which you can assign permissions.

* **Role**  
   If the option is selected, all roles will be displayed in the Available box for you to assign permissions.
* **User**  
   If the option is selected, all users will be displayed in the Available box for you to assign permissions.
* **Group**  
   If the option is selected, all groups will be displayed in the Available box for you to assign permissions.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404880219927/btn_add.gif)

Adds the selected role, user, or group to the Selected box.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4404880220567/btn_rmv.gif)

Removes the selected role, user, or group from the Selected box.

**Selected**

Select a role/user/group in the Selected box and then select the [permissions](https://devnet.logianalytics.com/hc/en-us/articles/1500009778641-Managing-Permissions) you would like the role/user/group to have on the result.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009774541-Resource-Allocation-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009774581-Schedule-Dialog-Box-Properties)
