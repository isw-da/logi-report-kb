---
title: "Managing Permissions"
id: 4405684023831
section: "Logi Report Server Security System Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405684023831-Managing-Permissions
updated_at: 2022-01-27T07:59:49Z
---

# Managing Permissions

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405684020759-Managing-Aliases)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405684028567-Multitenancy-Supported-via-Organizations)

# Managing Permissions

Permissions, associated with resources including folders, in the public folders in the server resource tree, are the rules that you can grant to users to control their access to resources. This topic describes the permissions that Logi Report Server reserves, and how to manage the permissions for the users, groups, and roles in the server security system.

This topic contains the following sections:

* [Permissions on Logi Report Server](#Permission)
* [Editing Resource Permissions for Users, Groups, and Roles](#Edit)

## Permissions on Logi Report Server

The following table lists the permissions on Logi Report Server. By default, the system admin has all the permissions on the public folders in the server resource tree, while users that are not system admin only have the Visible and Read permissions on the public folders. An [organization admin](https://devnet.logianalytics.com/hc/en-us/articles/4405684028567-Multitenancy-Supported-via-Organizations) has all the server permissions on the organization folders.

| Permission | Description |
| --- | --- |
| Visible | Allow viewing object names in the resource tree or version table, such as folders, resources, and archive versions. |
| Read | Allow viewing object properties, versions, and, if it is a folder, folder contents. |
| Write | Allow publishing folders and resources, changing the properties (excluding permission settings) of the objects in the resource tree or version table, such as folders, resources, and archive versions, and modifying version table settings. |
| Execute | Allow:  * Basic View of Page Report Studio when running [page reports](https://devnet.logianalytics.com/hc/en-us/articles/4405690675223-Running-Reports#Direct) and [page report results](https://devnet.logianalytics.com/hc/en-us/articles/4405684011031-Viewing-Scheduled-Report-Results#RSD) in Page Report Studio. * View Mode of Web Report Studio when running [web reports](https://devnet.logianalytics.com/hc/en-us/articles/4405690675223-Running-Reports#Direct) in Web Report Studio. * View mode of JDashboard when [running dashboards](https://devnet.logianalytics.com/hc/en-us/articles/4405683598743-Running-Dashboards). * [Opening analysis templates](https://devnet.logianalytics.com/hc/en-us/articles/4405690466839-Starting-a-Visual-Analysis-Session#Run). * [Running reports in Advanced mode](https://devnet.logianalytics.com/hc/en-us/articles/4405690675223-Running-Reports#Advanced).   Running reports, dashboards, or analysis templates [via URL](https://devnet.logianalytics.com/hc/en-us/articles/4405684050455-Working-on-Logi-Report-Server-via-URL-Logi-Report-Server-v18) is also under the permission control. |
| Edit | Allow:  * Interactive View of Page Report Studio when running page reports and page report results in Page Report Studio. * Edit Mode of Web Report Studio when running web reports in Web Report Studio. * Edit mode of JDashboard when running dashboards. You also need the Execute permission.   Running reports or dashboards via URL is also under the permission control. |
| Schedule | Allow submitting resources to schedules (for report type resources only). |
| Delete | Allow deleting objects from the resource tree or version table, such as folders, resources, and archive versions. |
| Grant | Allow granting permissions to other users, groups, or roles. You need to be an administrator to assign the Grant permission to other users, groups, or roles. Users, groups, or roles that have obtained the Grant permission are also endowed with the other permissions, and users can then grant these permissions except the Grant permission itself to other users in the same group. |
| Update Status | Allow updating report status, and if it is a folder, the status of reports in the folder. |

## Editing Resource Permissions for Users, Groups, and Roles

Server supports two ways to apply permissions to the set of users. One is the default way of setting permissions for users, groups, and roles. The other is [role based definition](https://devnet.logianalytics.com/hc/en-us/articles/4405684029591-Role-Based-Security), in which you define permissions on roles only, and map users and groups to roles. When Server is performing runtime security checking for a given user, it respects the permissions settings and follows the access control rules when processing the service requests.

Users who have the Grant permission on a resource can manage the permissions of other users, groups, or roles on the resource while [publishing the resource](https://devnet.logianalytics.com/hc/en-us/articles/4405683932951-Publishing-Resources) to Server, [editing the resource properties](https://devnet.logianalytics.com/hc/en-us/articles/4405683933975-Changing-Resource-Properties), or when [advanced running](https://devnet.logianalytics.com/hc/en-us/articles/4405690675223-Running-Reports#Advanced) or [scheduling to publish a report to the versioning system](https://devnet.logianalytics.com/hc/en-us/articles/4405684006039-Examples-of-Scheduling-Reports#Version). See a sample UI:

![Set Permissions dialog](https://devnet.logianalytics.com/hc/article_attachments/4420453462295/permsn.gif)

**To edit the permissions of the users, groups, and roles on a resource:**

1. In the setting permission UI, select **Enable Setting Permissions**.
2. Select **Role**, **User**, or **Group**.
3. Select a role, user, or group in the Selected box, then select or clear the required permissions.

   If a role, user, or group is not listed in the Selected box, select it in the Available box and select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420447121559/btn_add.gif) to add it to the Selected box first, then assign the permissions accordingly.

   You can make use of the Search box to search for the required roles, users, and groups in the Available or Selected box: type the text of the principal names you want to search for, and Server lists the principals containing the matched text. After typing text in the Search box, you can select ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/4420453419415/btn_mvdown1.gif) in the box to specify the following search options: Highlight All, Match Case, and Match Whole Word. To cancel the search operation, clear the text or select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4420461456151/btn_dltobj.gif).
4. To remove all the enabled permissions from a role, user, or group, first select it in the Selected table, then select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420461527319/btn_rmv.gif). Server moves the role, user, or group back to the Available box with no permissions.

   To remove permissions for all roles, users, and groups on the resource, clear **Enable Setting Permissions**.

After you have set permissions for a parent folder, any new resources and subfolders in that folder will inherit the same permissions. If you do not want them to inherit these permissions, you can enable their user permissions and set their permissions separately. Resources and folders will inherit permissions from their parent folder if you don't enable their user permissions.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg)

* To run reports in public folders in the server resource tree, you must have the Execute and/or Edit permissions on the reports, and the Visible/Read permissions on the catalogs that the reports use.
* You may need more than one permission to complete a task. For example, you must have both the Visible and Read permissions
  to view the properties of a report.
* Some permissions depend on other permissions, such as Write, Execute, Edit, and Schedule. Allowing anyone of these will also allow the Read permission.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405684020759-Managing-Aliases)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405684028567-Multitenancy-Supported-via-Organizations)
