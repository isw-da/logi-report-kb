---
title: "Managing Permissions"
id: 1500009778641
section: "Security System Data Model"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009778641-Managing-Permissions
updated_at: 2021-07-24T00:47:36Z
---

# Managing Permissions

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009778601-Managing-Aliases)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009749922-Multitenancy-Supported-via-Organizations)

# Managing Permissions

Permissions, associated with resources including folders, in the public folders in the server resource tree, are the rules that you can grant to users to control their access to resources. This topic describes the permissions that Logi Report Server reserves, and how to manage the permissions for the users, groups, and roles in the server security system.

This topic contains the following sections:

* [Permissions on Logi Report Server](#Permission)
* [Editing Resource Permissions for Users, Groups, and Roles](#Edit)

## Permissions on Logi Report Server

The following table lists the permissions on Logi Report Server. By default, the system admin has all the permissions on the public folders in the server resource tree, while users that are not system admin only have the Visible and Read permissions on the public folders. An [organization admin](https://devnet.logianalytics.com/hc/en-us/articles/1500009749922-Multitenancy-Supported-via-Organizations) has all the server permissions on the organization folders.

| Permission | Description |
| --- | --- |
| Visible | Allows or denies viewing object names in the resource tree or version table, such as folders, resources, and archive versions. |
| Read | Allows or denies viewing object properties, versions, and, if it is a folder, folder contents. |
| Write | Allows or denies publishing folders and resources, changing the properties (not including permission settings) of the objects in the resource tree or version table, such as folders, resources, and archive versions, and modifying version table settings. |
| Execute | Allows or denies:  * Basic View of Page Report Studio when running [page reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009778381-Running-Reports#Direct) and [page report results](https://devnet.logianalytics.com/hc/en-us/articles/1500009749642-Viewing-Scheduled-Report-Results#RSD) in Page Report Studio. * View Mode of Web Report Studio when running [web reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009778381-Running-Reports#Direct) in Web Report Studio. * View mode of JDashboard when [running dashboards](https://devnet.logianalytics.com/hc/en-us/articles/1500009771861-Running-Dashboards). * [Opening analysis templates](https://devnet.logianalytics.com/hc/en-us/articles/1500009742962-Starting-a-Visual-Analysis-Session#Run). * [Running reports in Advanced mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009778381-Running-Reports#Advanced).   Running reports, dashboards, or analysis templates [via URL](https://devnet.logianalytics.com/hc/en-us/articles/1500009750282-Working-on-Server-via-URL) is also under the permission control. |
| Edit | Allows or denies:  * Interactive View of Page Report Studio when running page reports and page report results in Page Report Studio. * Edit Mode of Web Report Studio when running web reports in Web Report Studio. * Edit mode of JDashboard when running dashboards. Execute permission is also required.   Running reports or dashboards via URL is also under the permission control. |
| Schedule | Allows or denies submitting resources to schedules (for report type resources only). |
| Delete | Allows or denies deleting objects from the resource tree or version table, such as folders, resources, and archive versions. |
| Grant | Allows or denies granting permissions to other users, groups, or roles. Only administrators can assign the Grant permission to other users, groups, or roles. Users, groups, or roles that have obtained the Grant permission are also endowed with the other permissions, and users can then grant these permissions except the Grant permission itself to other users in the same group. |
| Update Status | Allows or denies updating report status, and if it is a folder, the status of reports in the folder. |

## Editing Resource Permissions for Users, Groups, and Roles

Logi Report Server supports two ways to apply permissions to the set of users. One is the default way of setting permissions for users, groups, and roles. The other is [role based definition](https://devnet.logianalytics.com/hc/en-us/articles/1500009749942-Role-Based-Security), in which permissions are defined on roles only, and users and groups are mapped to roles. When Logi Report Server is performing runtime security checking for a given user, it will respect the permissions settings and follow the access control rules when processing the service requests.

Users who have the Grant permission on a resource can manage the permissions of other users, groups, or roles on the resource while [publishing the resource](https://devnet.logianalytics.com/hc/en-us/articles/1500009777241-Publishing-Resources) to Logi Report Server, [editing the resource properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009748702-Changing-Resource-Properties), or when [advanced running](https://devnet.logianalytics.com/hc/en-us/articles/1500009778381-Running-Reports#Advanced) or [scheduling a report to publish to the versioning system](https://devnet.logianalytics.com/hc/en-us/articles/1500009778441-Examples-of-Scheduling-Reports#Version). See a sample UI below:

![Set Permissions dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880219543/permsn.gif)

**To edit the permissions of the users, groups, and roles on a resource:**

1. In the setting permission UI, select **Enable Setting Permissions**.
2. Select the **Role**, **User**, or **Group** radio button.
3. Select a role, user, or group in the Selected box, then select or clear the required permissions.

   If a role, user, or group is not listed in the Selected box, select it in the Available box and select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404880219927/btn_add.gif) to add it to the Selected box first, then assign the permissions accordingly.

   You can make use of the Search box to search for the required roles, users, and groups in the Available or Selected box: type the text of the principal names you want to search for and the principals containing the matched text will be listed. After typing text in the Search box, you can select ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/4404885328919/btn_mvdown1.gif) that appears in the box to specify the following search options: Highlight All, Match Case, and Match Whole Word. To cancel the search operation, clear the text or select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404885308823/btn_dltobj.gif).
4. To remove all the enabled permissions from a role, user, or group, first select it in the Selected table, then select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404880220567/btn_rmv.gif). The role, user, or group will be added back to the Available box with no permissions.

   To remove permissions for all roles, users, and groups on the resource, clear **Enable Setting Permissions**.

After you have set permissions for a parent folder, any new resources and subfolders created in that folder will inherit the same permissions. If you do not want them to inherit these permissions, you can enable their user permissions and set their permissions separately. Resources and folders will inherit permissions from their parent folder if their user permissions are not enabled.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)

* You may need more than one permission to complete a task. For example, you must have both the Visible and Read permissions
  to view the properties of a report.
* Some permissions depend on other permissions, such as Write, Execute, Edit, and Schedule. Allowing anyone of these will also allow the Read permission.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009778601-Managing-Aliases)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009749922-Multitenancy-Supported-via-Organizations)
