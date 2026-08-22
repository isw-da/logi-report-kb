---
title: "Library Component Properties"
id: 1500009746282
section: "Logi Report Server Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009746282-Library-Component-Properties
updated_at: 2021-07-24T00:48:42Z
---

# Library Component Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746042-JDashboard-Profile-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009746062-Login-Server-Dialog-Box-Properties)

# Library Component Properties

This topic describes how you can use the Library Component Properties dialog box to [set the properties of a library component](https://devnet.logianalytics.com/hc/en-us/articles/1500009748702-Changing-Resource-Properties).

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

Select **Help** to view information about the Library Component Properties dialog box.

## General Tab Properties

Specifies the general properties of the library component.

![Library Component Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404880418583/prptylc_gen.gif)

**Resource Path**

Shows the resource path.

**Resource Node Name**

Specifies the name for the library component.

**Resource Type**

Shows the type of the resource.

**Resource Description**

Specifies description of the library component.

**[Custom Field Name]**

Specifies value of the custom field for the library component. A [custom field](https://devnet.logianalytics.com/hc/en-us/articles/1500009748662-Working-with-Custom-Fields) can be regarded as a resource property and is available when it is enabled.

**Enable Linked Catalog**

Enables to link the library component with a catalog. Once a library component is linked with a catalog, even if the library component and the catalog are not in the same directory, it can still be run with the catalog.

* **Use Specified**  
   Links the library component with a catalog in the server resource tree.
  + **Select Another Catalog**  
     Specifies another catalog in the [Select Another Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009746402-Select-Another-Catalog-Dialog-Box-Properties) dialog box.
* **Use Inherited**  
   Links the library component with the linked catalog inherited from its parent folder.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)If the parent level does not enable linked catalog, you cannot select this option.

**Maximum Number of Versions**

Specifies the [maximum version amount](https://devnet.logianalytics.com/hc/en-us/articles/1500009748742-Applying-an-Archive-Policy) that will be listed in the version table. By default, the version amount is unlimited.

## Permission Tab Properties

Specifies permissions of roles/users/groups on the library component. This tab is available when the library component is in a public folder and when you have the Grant permission on the library component.

![Library Component Properties dialog - Permission tab](https://devnet.logianalytics.com/hc/article_attachments/4404880419607/prptylc_prmsn.gif)

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

Select a role/user/group in the Selected box and then select the [permissions](https://devnet.logianalytics.com/hc/en-us/articles/1500009778641-Managing-Permissions) you would like the role/user/group to have on the library component.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746042-JDashboard-Profile-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009746062-Login-Server-Dialog-Box-Properties)
