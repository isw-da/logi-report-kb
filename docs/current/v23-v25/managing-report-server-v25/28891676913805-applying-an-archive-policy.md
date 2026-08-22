---
title: "Applying an Archive Policy"
id: 28891676913805
section: "Managing Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891676913805-Applying-an-Archive-Policy
updated_at: 2026-02-26T02:13:32Z
source_host: docs-report.zendesk.com
---
# 
Applying an Archive Policy 

Report Server uses an archive policy to control resource versions. This topic describes how you can set archive policy to resources.

Archive policy can apply to a single resource individually or to many resources in a folder as a whole. It can also apply when you publish resources to the server resource tree or when you advanced run or schedule a report task.

When applying an archive policy, you can choose whether to use multiple versions for a resource or always use the new version to replace the old one. 

Archive as New Version

The resource can have multiple versions. You can add a new version to the resource.

- 
Maximum Number of Versions
The maximum number of versions that can display in the version table of the resource. The default value 0 means that the version number is unlimited.

Replace Old Version

The resource can only have one version and the new version always overwrites the old version.

If you do not define an archive policy for a resource, the resource will inherit the archive policy from its parent. If afterwards you then specify an archive policy for the resource, the new policy will override the one that the resource inherited from the parent.

This topic contains the following sections:

- Applying an Archive Policy to Resources in the Resource Tree

- Applying an Archive Policy to the Built-in Version Table

## 
Applying an Archive Policy to Resources in the Resource Tree

To apply an archive policy to a resource in the resource tree, refer to the table:

| If you want to | Then do | Result |
| --- | --- | --- |
| Apply archive policy when publishing resources | In the publish resource dialog box (for how to access the dialog box, see Publishing Resources): If the resource is to publish to the My Reports or Public Reports folder, set the Apply Archive Policy option. If the resource is to publish to the My Components or Public Components folder, set the Maximum Number of Versions option. | The archive policy applies to the resource. The archive policy you specified for a folder applies to the folder contents. |
| Apply archive policy to a folder | Access the Properties dialog box for the folder (for how to access the dialog box, see Changing Resource and Folder Properties). In the dialog box, For a folder in the My Reports or Public Reports folder (including the root folder itself), set the Apply Archive Policy option, then select OK. For a folder in the My Components or Public Components folder (including the root folder itself), set the Maximum Number of Versions option, then select OK. | The archive policy applies to the folder contents. This does not include resources that already have individually applied archive policies. |
| Apply archive policy to a resource | Access the Properties dialog box for the resource (for how to access the dialog box, see Changing Resource and Folder Properties). In the dialog box, For a resource in the My Reports or Public Reports folder, set the Apply Archive Policy option, then select OK. For a resource in the My Components or Public Components folder, set the Maximum Number of Versions option, then select OK. | The archive policy applies to the resource, overriding its inherited archive policy. If you do not specify the archive policy, the resource will inherit the archive policy from its parent object, for example, the folder it resides in. |
| Apply archive policy when running a task in Advanced mode | On the Server Console, go to the server resource tree in the Resources page, browse to the resource you want to run. Put the mouse pointer over the resource row and select the Advanced Run button on the floating toolbar. In the Archive tab, select Auto Archive Properties. Finish the other relevant information. Make sure that you set Archive Location to the resource tree folder. Set the Apply Archive Policy option. Select Finish. | The archive policy applies to a result type resource. If you do not specify the archive policy, the resource will use its old archive policy or inherit the archive policy from its parent object, for example, the folder it resides in. |
| Apply archive policy when scheduling a task | On the Server Console, go to the server resource tree in the Resources page, browse to the resource you want to schedule. Put the mouse pointer over the resource row and select the Schedule button on the floating toolbar. In the Publish tab, select the To Version sub tab, then select Publish to Versioning System. Finish the other relevant information. Make sure that you set Archive Location to the resource tree folder. Set the Apply Archive Policy option. Select Finish. | The archive policy applies to a result type resource. If you do not specify the archive policy, the resource will use its old archive policy or inherit the archive policy from its parent object, for example, the folder it resides in. |

## 
Applying an Archive Policy to the Built-in Version Table

The versions in the built-in version folder have their own archive policy.

To apply an archive policy to the built-in version table, refer to the table:

| If you want to | Then do |
| --- | --- |
| Apply archive policy to a built-in version table | Access the version table for the resource (report type) (for how to access the table, see Browsing Versions). In the Report Result Versions tab, select the Maximum Number of Versions option, then type a number in the text box. Select OK. |
| Apply archive policy when running a task in Advanced mode | On the Server Console, go to the server resource tree in the Resources page, browse to the resource you want to run. Put the mouse pointer over the resource row and select the Advanced Run button on the floating toolbar. In the Archive tab, select the Auto Archive Properties option. Finish the other relevant information. Make sure that you set Archive Location to Built-in Version Folder. Set the Apply Archive Policy option. Select Finish. |
| Apply archive policy when scheduling a task | On the Server Console, go to the server resource tree in the Resources page, browse to the resource you want to schedule. Put the mouse pointer over the resource row and select the Schedule button on the floating toolbar. In the Publish tab, select the To Version sub tab, then select the Publish to Versioning System option. Finish the other relevant information. Make sure that you set Archive Location to Built-in Version Folder. Set the Apply Archive Policy option. Select Finish. |
