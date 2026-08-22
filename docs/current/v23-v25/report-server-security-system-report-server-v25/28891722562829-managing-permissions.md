---
title: "Managing Permissions"
id: 28891722562829
section: "Report Server Security System Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891722562829-Managing-Permissions
updated_at: 2026-02-26T02:13:51Z
source_host: docs-report.zendesk.com
---
# 
Managing Permissions

Permissions, associated with resources including folders, in the public folders in the server resource tree, are the rules that you can grant to users to control their access to resources. This topic describes the permissions that Report Server reserves, and how to manage the permissions for the users, groups, and roles in the server security system.

This topic contains the following sections:

- Permissions on Report Server

- Editing Resource Permissions for Users, Groups, and Roles

## 
Permissions on Report Server

The following table lists the permissions on Report Server. By default, the system admin has all the permissions on the public folders in the server resource tree, while users that are not system admin only have the Visible and Read permissions on the public folders. An organization admin has all the server permissions on the organization folders.

| Permission | Description |
| --- | --- |
| Visible | Allow viewing object names in the resource tree or version table, such as folders, resources, and archive versions. |
| Read | Allow viewing object properties, versions, and, if it is a folder, folder contents. |
| Write | Allow publishing folders and resources, changing the properties (excluding permission settings) of the objects in the resource tree or version table, such as folders, resources, and archive versions, and modifying version table settings. |
| Execute | Allow: Basic View of Page Report Studio when running page reports and page report results in Page Report Studio. View Mode of Web Report Studio when running web reports in Web Report Studio. View mode of JDashboard when running dashboards. Opening analysis templates. Running reports in Advanced mode. Running reports, dashboards, or analysis templates via URL is also under the permission control. |
| Edit | Allow editing reports: Interactive View of Page Report Studio when running page reports and page report results in Page Report Studio. Edit Mode of Web Report Studio when running web reports in Web Report Studio. Edit mode of JDashboard when running dashboards. You also need the Execute permission. Running reports or dashboards via URL is also under the permission control. Allow editing catalogs: Edit catalogs in Catalog Studio. You need a license to access Catalog Studio. |
| Schedule | Allow submitting resources to schedules (for report type resources only). |
| Delete | Allow deleting objects from the resource tree or version table, such as folders, resources, and archive versions. |
| Grant | Allow granting permissions to other users, groups, or roles. You need to be an administrator to assign the Grant permission to other users, groups, or roles. Users, groups, or roles that have obtained the Grant permission are also endowed with the other permissions, and users can then grant these permissions except the Grant permission itself to other users in the same group. |
| Update Status | Allow updating report status, and if it is a folder, the status of reports in the folder. |

## 
Editing Resource Permissions for Users, Groups, and Roles

Server supports two ways to apply permissions to the set of users. One is the default way of setting permissions for users, groups, and roles. The other is role based definition, in which you define permissions on roles only, and map users and groups to roles. When Server is performing runtime security checking for a given user, it respects the permissions settings and follows the access control rules when processing the service requests.

 Users who have the Grant permission on a resource can manage the permissions of other users, groups, or roles on the resource while publishing the resource to Server, editing the resource properties, or when advanced running or scheduling to publish a report to the versioning system. See a sample UI:

To  edit the permissions of the users, groups, and roles on a resource:

- In the setting permission UI, select Enable Setting Permissions.

- Select Role, User, or Group.

- Select a role, user, or group in the Selected box, then select or clear the required permissions.
			If a role, user, or group is not listed in the Selected box, select it in the Available box and select the Add button  to add it to the Selected box first, then assign the permissions accordingly.

You can make use of the Search box to search for the required roles, users, and groups in the Available or Selected box: type the text of the principal names you want to search for,  and Server lists the principals containing the matched text. After typing text in the Search box, you can select  in the box to specify the following search options: Highlight All, Match Case, and Match Whole Word. To cancel the search operation, clear the text or select .

- To remove all the enabled permissions from a role, user, or group, first select it in the Selected table, then select . Server moves the role, user, or group  back to the Available box with no permissions. 
                To remove permissions for all roles, users, and groups on the resource, clear Enable Setting Permissions.

After you have set permissions for a parent folder, any new resources and subfolders in that folder will inherit the same permissions. If you do not want them to inherit these permissions, you can enable their user permissions and set their permissions separately. Resources and folders will inherit permissions from their parent folder if you don't enable their user permissions.

- To run reports in public folders in the server resource tree, you must have the Execute and/or Edit permissions on the reports, and the Visible/Read permissions on the catalogs that the reports use.

- You may need more than one permission to complete a task. For example, you must have both the Visible and Read permissions 
to view the properties of a report.

- Some permissions depend on other permissions, such as Write, Execute, Edit, and Schedule. Allowing anyone of these will also allow the Read permission.
