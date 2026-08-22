---
title: "Managing Permissions"
id: 1500009718881
section: "Security System Data Model"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009718881-Managing-Permissions
updated_at: 2021-11-03T06:56:31Z
---

# Managing Permissions

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009692662-Managing-Aliases)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009692742-Multi-tenancy-Supported-via-Organizations)

# Managing Permissions

Permissions, associated with resources (including folders) located in the public folders in the server resource tree, are the rules that are granted to users to control their access to resources.

Permissions in Logi JReport Server include:

| Permission | Description |
| --- | --- |
| Visible | Allows or denies viewing object names in the resource tree or version table, such as folders, resources, and archive versions. |
| Read | Allows or denies viewing object properties, versions, and, if it is a folder, folder contents. |
| Write | Allows or denies publishing folders and resources, changing the properties (not including permission settings) of the objects in the resource tree or version table, such as folders, resources, and archive versions, and modifying version table settings. |
| Execute | Allows or denies:  * Basic View of Page Report Studio when running [page reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009692462-Running-Reports#Direct) and [page report results](https://devnet.logianalytics.com/hc/en-us/articles/1500009718741-Viewing-Scheduled-Report-Results#RSD) in Page Report Studio. * View Mode of Web Report Studio when running [web reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009692462-Running-Reports#Direct) in Web Report Studio. * View mode of JDashboard when [running dashboards](https://devnet.logianalytics.com/hc/en-us/articles/1500009712661-Running-Dashboards). * [Opening analysis templates](https://devnet.logianalytics.com/hc/en-us/articles/1500009686082-Starting-a-Visual-Analysis-Session#Run). * [Running reports in Advanced mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009692462-Running-Reports#Advanced).   Running reports, dashboards or analysis templates via [URL](https://devnet.logianalytics.com/hc/en-us/articles/1500009692942-Working-on-Logi-JReport-Server-via-URLs) is also under the permission control. |
| Edit | Allows or denies:  * Interactive View of Page Report Studio when running page reports and page report results in Page Report Studio. * Edit Mode of Web Report Studio when running web reports in Web Report Studio. * Edit mode of JDashboard when running dashboards. Execute permission is also required.   Running reports or dashboards via URL is also under the permission control. |
| Schedule | Allows or denies submitting resources to schedules (for report type resources only). |
| Delete | Allows or denies deleting objects from the resource tree or version table, such as folders, resources, and archive versions. |
| Grant | Allows or denies granting permissions to other users, groups or roles. Only members in the administrators role can assign the Grant permission to other users or groups or roles. Users, groups or roles that have obtained the Grant permission are also endowed with the other permissions, and users can then grant these permissions except the Grant permission itself to other users in the same group. |
| Update Status | Allows or denies updating report status, and if it is a folder, the status of reports in the folder. |

By default, the system admin has all the server permissions on the public folders, while users that are not system admin only have the Visible and Read permissions on the public folders. An [organization admin](https://devnet.logianalytics.com/hc/en-us/articles/1500009692742-Multi-tenancy-Supported-via-Organizations) has all the server permissions on the organization folders.

Logi JReport Server supports two ways to apply permissions to the set of users. One is the default system of setting permissions for users, groups and roles. The other is [role based definition](https://devnet.logianalytics.com/hc/en-us/articles/1500009718981-Role-Based-Security), in which permissions are defined on roles only, and users and groups are mapped to roles. When Logi JReport Server is performing runtime security checking for a given user, it will respect the permissions settings and follow the access control rules when processing the service requests.

Users who have the Grant permission on a resource can manage the permissions of other roles, users or groups on the resource while [publishing the resource](https://devnet.logianalytics.com/hc/en-us/articles/1500009717841-Publishing-Resources) to Logi JReport Server, [editing the resource properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009717861-Changing-Resource-Properties) or when [advanced running](https://devnet.logianalytics.com/hc/en-us/articles/1500009692462-Running-Reports#Advanced) or [scheduling a report to publish to the versioning system](https://devnet.logianalytics.com/hc/en-us/articles/1500009692502-Scheduling-Tasks-to-Publish-Reports#Version).

Below is a sample UI for your reference:

![Set Permissions dialog](https://devnet.logianalytics.com/hc/article_attachments/4412139520023/permsn.gif)

The following lists the permission management tasks:

* **Setting, viewing, changing resource permissions**  
   To set up or change permissions for a role, user or group, in the setting permission UI, first check **Enable Setting Permissions**, then select the role/user/group in the Selected box and check or uncheck the required permissions. If the role/user/group is not listed in the Selected box, select the corresponding radio button below the Available box, add the role/user/group to the Selected box and then assign the permissions accordingly.
* **Removing resource permissions**  
   To remove resource permissions for all users, groups and roles, uncheck the **Enable Setting Permissions option** in the setting permission UI.
* **Searching for roles/groups/users in the Available/Selected table**  
   In the corresponing Search box, type in the text of the principal names you want to search for and the principals containing the matched text will be listed. After entering text in the Search box, you can select ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/4412139498007/btn_mvdown1.gif) that appears in the box to specify the following search options: Highlight All, Match Case and Match Whole Word**.** To cancel the search operation, clear the text or select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4412112483991/btn_dltobj.gif).

After you have set permissions for a parent folder, any new resources and sub folders created in that folder will inherit the same permissions. If you do not want them to inherit these permissions, you can enable their user permissions and set their permissions separately. Resources and folders will inherit permissions from their parent folder if their user permissions are not enabled.

**Notes:**

* To complete a task, you may require more than one permission. For example, to view the properties of a report, you must have both the Visible and Read permissions.
* Some permissions depend on other permissions in order to work, such as Write, Execute, Edit and Schedule. Allowing anyone of these will also allow the Read permission.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009692662-Managing-Aliases)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009692742-Multi-tenancy-Supported-via-Organizations)
