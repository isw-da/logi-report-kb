---
title: "Managing Privileges"
id: 28891736718605
section: "Report Server Security System Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891736718605-Managing-Privileges
updated_at: 2026-02-26T02:13:51Z
source_host: docs-report.zendesk.com
---
# 
Managing Privileges

Report Server offers two types of privileges for users, groups, and roles: Publish and Advanced Properties. This topic describes how you can grant and remove the privileges for users, groups, and roles, as an administrator.

You need to have the corresponding privilege before you can perform certain task on the server. When you have the Publish privilege and at the same time the Write permission on a folder on the server resource tree, you are able to publish resources to the folder. When you have the privilege of Advanced Properties, you can view advanced information about version properties such as catalog connections and report related resources. By default, only the role "administrators" and the user account "admin" have the Publish and Advanced Properties privileges. 

To manage privileges,  first select the realm which contains the users, groups, or roles you want to grant privilege for, then on the system toolbar of the Server Console, navigate to Administration > Security > Privilege to display the Privilege page.

To managing the privileges for users, groups, and roles:

- Select the Role, User, or Group radio button.

- Select a role, user, or group in the Selected box, then select or clear the required privileges.
			If a role, user, or group is not listed in the Selected box, select it in the Available box and select the Add button  to add it to the Selected box first, then grant it the privileges accordingly.

You can make use of the Search box to search for the required roles, users, and groups in the Available or Selected box: type the text of the principal names you want to search for  and Server lists the principals that contain the matched text. After typing text in the Search box, you can select the arrow  in the box to specify the following search options: Highlight All, Match Case, and Match Whole Word. To cancel the search operation, clear the text or select .

- To remove all privileges from a role, user, or group, first select it in the Selected table, then select . Server adds the role, user, or group back to the Available box with no privileges. 

- Select OK to apply the changes. 

You can also grant privileges  to users, groups, and roles while creating or editing the users, groups, and roles.
