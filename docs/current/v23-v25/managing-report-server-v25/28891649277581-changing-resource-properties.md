---
title: "Changing Resource Properties"
id: 28891649277581
section: "Managing Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891649277581-Changing-Resource-Properties
updated_at: 2026-02-26T02:13:30Z
source_host: docs-report.zendesk.com
---
# 
Changing Resource Properties 

You can edit the properties of any resources including folders in the server resource tree, such as node name, description, archive policy, and user permissions, in the Resources page of the Server Console. This topic describes how you can edit the properties of one or more resources at a time, and define business view security in a catalog.

This topic contains the following sections:

- Editing Properties of a Single Resource

- Editing Properties of Multiple Resources at a Time

- Defining Business View Security in a Catalog

## 
Editing Properties of a Single Resource

- Browse to the resource in the server resource tree and then choose a method:
    
- Hover over the resource row and select the Properties button  on the floating toolbar. 

-  Select the resource row, right-click and select Properties from the shortcut menu.

- Select the resource row and select Tools > Properties on the task bar.

Server displays the Properties dialog box.

- Change the resource properties in the General tab. 

- If the Permission tab is available, specify the permissions of different principals on the resource.

- If the Available Business Views tab is available, select the business views for the report to use.

- If the Business View Security tab is available, define business view security in the catalog.

- Select OK to apply your changes.

## 
Editing Properties of Multiple Resources at a Time

- Browse to the folder where the resources are.

- Select the required resources. To select all the resources, select the top checkbox.

- Select Tools > Properties on the task bar, or right-click in any selected resource row and select Properties from the shortcut menu. Server displays the Multiple Type Properties dialog box. 

- In the General tab, edit the description, status, linked catalog, and version archive policy for the resources. Settings for description and archive policy apply to all the selected resources, while the status setting works on report resources and linked catalog on report, library component, and folder resources only. 

- If the Permission tab is available, specify the permissions of different principals on the resources.

- Select OK to accept the changes. 

## 
Defining Business View Security in a Catalog

You can define business view security in a catalog that you can manage if you are an administrator, using the Properties dialog box.

Only the system admin can see the catalogs in the server resource tree by default. If you are an administrator in an organization and want to see the catalogs, set the web.page.option.show_catalog property to true in the server.properties file in the <install_root>\bin directory.

- 
Access the Properties dialog box of the catalog.

- Select the Business View Security tab.

- Select the Add button  above the Name box to create a business view security. Server displays the Business View Security Name dialog box.

- Type a name for the business view security.

- Select OK. Server adds the business view security in the Name box.

- Select Select to select business views for the business view security. Server displays the Select Business Views dialog box.

- Select the business views you want to add in the business view security.

- Select All if you want to select all the business views in the catalog.

- Select OK. Server displays the number of business views in the business view security.

- By selecting the arrow icon  you can expand and view the business views.

- To enable some users, roles, or groups in the server security system to access the business views in the business view security, select User, Role, or Group.

- Server displays in the Available box the users, roles, or groups in the server security system that you can manage.

- Select an item in the Available box.

- Select the Add button  to add the item to the Selected box.

- Repeat step 13 and 14 to add more items. The items you added in the Selected box will be able to access the business views in the business view security.

- You can define more business view security following the preceding procedure. 

The business view security you define here on Server has higher priority than that you define in the catalog using Report Designer.
