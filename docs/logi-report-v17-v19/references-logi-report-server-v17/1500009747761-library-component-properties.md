---
title: "Library Component Properties"
id: 1500009747761
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009747761-Library-Component-Properties
updated_at: 2021-07-25T07:19:37Z
---

# Library Component Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009720582-JDashboard-Profile)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009747461-Login-Server)

# Library Component Properties

The Library Component Properties dialog box is used to [set the properties of a library component](https://devnet.logianalytics.com/hc/en-us/articles/1500009723122-Changing-Resource-Properties).

There are the following tabs in this dialog box: [General](#General) and [Permission](#Permission).

**OK**

Closes this dialog box and applies the properties to the library component.

**Cancel**

Cancels any settings and closes the dialog box.

**Reset**

Discards your modifications and restores the dialog box to its default status.

**Help**

Displays the help document about this feature.

## General

Specifies the general properties of the library component.

![Library Component Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404936882967/prptylc_gen.gif)

**Resource Path**

Shows the resource path.

**Resource Node Name**

Specifies the name for the library component.

**Resource Type**

Shows the type of the resource.

**Resource Description**

Specifies description of the library component.

**[Custom Field Name]**

Specifies value of the custom field for the library component. A [custom field](https://devnet.logianalytics.com/hc/en-us/articles/1500009723042-Working-with-Custom-Fields) can be regarded as a resource property and is available when it is enabled.

**Enable Linked Catalog**

Enables to link the library component with a catalog. Once a library component is linked with a catalog, even if the library component and the catalog are not in the same directory, it can still be run with the catalog.

* **Use Specified**  
   Links the library component with a catalog in the server resource tree.
  + **Select Another Catalog**  
     Specifies another catalog in the [Select Another Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009720942-Select-Another-Catalog) dialog box.
* **Use Inherited**  
   Links the library component with the linked catalog inherited from its parent folder. Note that if the parent level does not enable linked catalog, you are not allowed to select this option.

**Maximum Number of Versions**

Specifies the [maximum version amount](https://devnet.logianalytics.com/hc/en-us/articles/1500009723202-Applying-an-Archive-Policy) that will be listed in the version table. By default the version amount is unlimited.

## Permission Tab

Specifies permissions of roles/users/groups on the library component. This tab is available when the library component is in a public folder and when you have the Grant permission on the library component.

![Library Component Properties dialog - Permission tab](https://devnet.logianalytics.com/hc/article_attachments/4404936883223/prptylc_prmsn.gif)

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

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404942476823/btn_add.gif)

Adds the selected role, user or group to the Selected box.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4404936763159/btn_rmv.gif)

Removes the selected role, user or group from the Selected box.

**Selected**

Select a role/user/group in the Selected box and then select the [permissions](https://devnet.logianalytics.com/hc/en-us/articles/1500009751241-Managing-Permissions) you would like the role/user/group to have on the library component.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009720582-JDashboard-Profile)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009747461-Login-Server)
