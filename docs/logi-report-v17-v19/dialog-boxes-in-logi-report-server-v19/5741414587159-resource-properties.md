---
title: "Resource Properties"
id: 5741414587159
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741414587159-Resource-Properties
updated_at: 2022-10-31T17:17:03Z
---

# Resource Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741433563287-Resource-Allocation-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741433620631-Schedule-Dialog-Box-Properties)

# Resource Properties

This topic describes how you can use the Properties dialog box to [set the properties of a resource](https://devnet.logianalytics.com/hc/en-us/articles/5741438178199-Changing-Resource-Properties).

This topic contains the following sections:

* [General Tab Properties](#General)
* [Permission Tab Properties](#Permission)
* [Available Business Views Tab Properties](#BV)
* [Business View Security Tab Properties](#BVSecurity)

Server disables or hides some properties for a [shared report](https://devnet.logianalytics.com/hc/en-us/articles/5741461964439-Sharing-Web-Reports).

You see these elements on all the tabs:

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## General Tab Properties

Use this tab to specify the general properties of the resource.

![Properties dialog box - General tab](https://devnet.logianalytics.com/hc/article_attachments/9905757816983/prptyrpt_gen.gif)

**Resource Path**

Resource path in the server resource tree.

**Resource Node Name**

You can update the name of the resource excluding a shared report.

**Resource Type**

Server shows the type of the resource.

**Resource Description**

Provide the description for the resource.

**Status**

Select the report status when the resource is a report excluding a shared report.

* **Active**  
   You can run, advanced run, and schedule to run the report.
* **Inactive**  
   You cannot run, advanced run, and schedule to run the report.
* **Incomplete**  
   You have not finished designing the report. You cannot run, advanced run, and schedule to run the report.

**National Language Support**

Clear this property if you do not want to enable the NLS feature for the resource.

The property is available to administrators when the resource is a report excluding a shared report, a dashboard, or an analysis template.

**Resource Real Path**

Specify the real path of the folder when the resource is a folder.

**Last Modified**

When the resource is a folder, Server shows the last time you modified the folder. This property is available to administrators.

**Enable Resources from Real Paths**

When the resource is a folder, you can select this property if you want to get resources from the folder's real path. Server maps the real path to the folder in the server resource tree, and therefore can get the resources and updates from the real path. For more information, see [Getting and Using Resources from a Real Path](https://devnet.logianalytics.com/hc/en-us/articles/5741482166807-Getting-and-Using-Resources-From-a-Real-Path).

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) You can select this property only when admin selected **Enable Resources from Real Paths** on the Server Console > Administration > Configuration > Advanced page.

**[Custom Field Name]**

Specify the value of the custom field for the resource. A [custom field](https://devnet.logianalytics.com/hc/en-us/articles/5741461739671-Working-with-Custom-Fields) is a resource property and is available when admin enabled it.

**Choose Profile**

This property is available to administrators when the resource is a page report. Select the Page Report Studio profile you want to apply when you run the report. A profile contains [a set of Page Report Studio settings](https://devnet.logianalytics.com/hc/en-us/articles/5741427459479-Page-Report-Studio-Profile-Properties).

**Resource Owner**

Select a user to be the owner of the resource who created the resource. The owner has full permission on the resource.

When the resource is neither in a public folder nor a shared report, system admin can change its owner if the resource does not belong to any organization, or the organization admin can do this if the resource belongs to the organization.

When [server.security](https://devnet.logianalytics.com/hc/en-us/articles/5741387498391-Configuring-Server-Using-Properties-in-server-properties#server.security)=false in the server.properties file, Server hides the **Resource Owner** property.

**Enable Linked Catalog**

This property is available when the resource is a report excluding a shared report, a library component, or a folder. By default, it is selected. You can link the resource with a catalog.

Once you link a report or library component with a catalog, even if they are not in the same directory, the report or library component can still run with the catalog.

When you background run, advanced run, or schedule to run a report, Server applies the linked catalog, instead of the original catalog in the same folder. For Advanced Run and Scheduled Run, you can change the catalog using the **Select Another Catalog** property in the **General** tab of the corresponding dialog box.

If you specify a linked catalog for a folder, then reports, library components, and subfolders in the folder can inherit the linked catalog from the folder once you enable their **Enable Linked Catalog** property.

* **Use Specified**  
   You can link the resource with a catalog in the server resource tree.
  + **Select Another Catalog**  
     Select this property and then choose another catalog in the [Select Another Catalog dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741433783191-Select-Another-Catalog-Dialog-Box-Properties).
* **Use Inherited**   
   Select if you want to link the resource with the linked catalog of its parent folder. The parent folder is the server level if the resource is a [built-in resource folder](https://devnet.logianalytics.com/hc/en-us/articles/5741438016279-Managing-Resources#Folder).

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) If the parent folder does not enable linked catalog, you cannot select this property.

**Apply Archive Policy**

Apply an [archive policy](https://devnet.logianalytics.com/hc/en-us/articles/5741482308887-Applying-an-Archive-Policy) to the versions of the resource, or to resource versions in the folder when the resource is a folder. This property is unavailable to a shared report.

* **Archive as New Version**  
   Select to enable multiple versions for the resource, or for the resources in the folder.

  **Maximum Number of Versions**  
   Specify the maximum number of versions that a resource can have. The default value 0 means unlimited version number.
* **Replace Old Version**  
   Select to replace the old version with the new version.

**Allow Edit**

This property is available when the resource is a shared report. It shows whether the report owner enables other users to edit the shared report.

**Reset**

Select to restore the **General** tab to its default status.

## Permission Tab Properties

Use this tab to specify permissions of roles/users/groups on the resource. Folder permissions can be inherited by the files and subfolders in the folder. This tab is available when the resource is in a public folder and when you have the **Grant** permission on the resource.

![Properties dialog box - Permission tab](https://devnet.logianalytics.com/hc/article_attachments/9905757832983/prptyrpt_prmsn.gif)

**Enable Setting Permissions**

Select if you want to set user permissions on the resource.

**Available**

Server lists the roles/users/groups to which you can assign permissions. You can search for items in the Available box by using the search box.

* **Role**  
   Select if you want to display roles in the Available box.
* **User**  
   Select if you want to display users in the Available box.
* **Group**  
   Select if you want to display groups in the Available box.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/9905636390807/btn_add.gif) **Add button**

Select to add the selected role, user, or group to the Selected box.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/9905657793175/btn_rmv.gif) **Remove button**

Select to remove the selected role, user, or group from the Selected box.

**Selected**

Select a role/user/group in the Selected box, and then select the [permissions](https://devnet.logianalytics.com/hc/en-us/articles/5741463668119-Managing-Permissions) you would like the role/user/group to have on the resource.

You can search for items in the Selected box by using the search box.

## Available Business Views Tab Properties

You can see the **Available Business Views** tab when the resource is a report that has a catalog available in the server resource tree and that is not in the **My Shared** folder, and if you are an administrator. Use this tab to select the business views for the report.

![Properties dialog box - Available Business Views tab](https://devnet.logianalytics.com/hc/article_attachments/9905714797079/prptyrpt_bv.gif)

**Select Business Views**

Select the business views you want the report to use.

**All**

Select to select all the listed business views.

**Export**

Select to export the selected business views to a plain text file.

## Business View Security Tab Properties

You can see the Business View Security tab when you are an administrator and the resource is a catalog you can manage. Use this tab to define the business view security in the catalog.

![Properties dialog box - Business View Security tab](https://devnet.logianalytics.com/hc/article_attachments/9905675978903/prptyrpt_bvs.gif)

**Name**

The business view security names.

* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905619223831/btn_add1.gif)**Add button**  
  Select to add a business view security and provide a name for it.
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/9905578411927/btn_delete.gif)**Remove button**  
  Select to remove the selected business view security from the Name box.

**N Business Views Selected**

Server displays the number of business views in the business view security you selected in the Name box. When the number N is not 0, you can select the arrow icon ![Expand button](https://devnet.logianalytics.com/hc/article_attachments/9905618988823/btn_mvdown1.gif) to expand and view the business views.

**Select**

Select to add or update the business views in the business view security you selected. Server displays the [Select Business Views dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741421631383-Select-Business-Views-Dialog-Box-Properties).

You use the following properties to select users, roles, and groups who will be able to view the selected business views in the business view security.

**Available**

Server lists the roles, users, or groups you can select from. You can search for items in the Available box by using the search box.

* **Role**  
   Select if you want to display roles in the Available box.
* **User**  
   Select if you want to display users in the Available box.
* **Group**  
   Select if you want to display groups in the Available box.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/9905636390807/btn_add.gif)**Add button**

Select to add the selected role, user, or group from the Available box to the Selected box.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/9905657793175/btn_rmv.gif)**Remove button**

Select to remove the selected role, user, or group from the Selected box.

**Selected**

Server lists the users, roles, and groups who will be able to view the selected business views in the business view security.

You can search for items in the Selected box by using the search box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741433563287-Resource-Allocation-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741433620631-Schedule-Dialog-Box-Properties)
