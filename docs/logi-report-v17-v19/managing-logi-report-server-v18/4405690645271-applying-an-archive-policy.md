---
title: "Applying an Archive Policy"
id: 4405690645271
section: "Managing Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690645271-Applying-an-Archive-Policy
updated_at: 2022-01-27T07:59:39Z
---

# Applying an Archive Policy

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683941911-Checking-Version-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690646167-Deleting-Versions)

# Applying an Archive Policy

Logi Report Server uses an archive policy to control resource versions. This topic describes how you can set archive policy to resources.

Archive policy can apply to a single resource individually or to many resources in a folder as a whole. It can also apply when you publish resources to the server resource tree or when you advanced run or schedule a report task.

When applying an archive policy, you can choose whether to use multiple versions for a resource or always use the new version to replace the old one.

**Archive as New Version**

The resource can have multiple versions. You can add a new version to the resource.

* **Maximum Number of Versions**  
  The maximum number of versions that can display in the version table of the resource. The default value 0 means that the version number is unlimited.

**Replace Old Version**

The resource can only have one version and the new version always overwrites the old version.

If you do not define an archive policy for a resource, the resource will inherit the archive policy from its parent. If afterwards you then specify an archive policy for the resource, the new policy will override the one that the resource inherited from the parent.

This topic contains the following sections:

* [Applying an Archive Policy to Resources in the Resource Tree](#Tree)
* [Applying an Archive Policy to the Built-in Version Table](#Table)

## Applying an Archive Policy to Resources in the Resource Tree

To apply an archive policy to a resource in the resource tree, refer to the table:

| If you want to | Then do | Result |
| --- | --- | --- |
| Apply archive policy when publishing resources | In the publish resource dialog box (for how to access the dialog box, see [Publishing Resources](https://devnet.logianalytics.com/hc/en-us/articles/4405683932951-Publishing-Resources)):  * If the resource is to publish to the My Reports or Public Reports folder, set the **Apply Archive Policy** option. * If the resource is to publish to the My Components or Public Components folder, set the **Maximum Number of Versions** option. | The archive policy applies to the resource. Note iconThe archive policy you specified for a folder applies to the folder contents. |
| Apply archive policy to a folder | 1. Access the Properties dialog box for the folder (for how to access the dialog box, see [Changing Resource and Folder Properties](https://devnet.logianalytics.com/hc/en-us/articles/4405683933975-Changing-Resource-Properties)). 2. In the dialog box,    * For a folder in the My Reports or Public Reports folder (including the root folder itself), set the **Apply Archive Policy** option, then select **OK**.    * For a folder in the My Components or Public Components folder (including the root folder itself), set the **Maximum Number of Versions** option, then select **OK**. | The archive policy applies to the folder contents. Note iconThis does not include resources that already have individually applied archive policies. |
| Apply archive policy to a resource | 1. Access the Properties dialog box for the resource (for how to access the dialog box, see [Changing Resource and Folder Properties](https://devnet.logianalytics.com/hc/en-us/articles/4405683933975-Changing-Resource-Properties)). 2. In the dialog box,    * For a resource in the My Reports or Public Reports folder, set the **Apply Archive Policy** option, then select **OK**.    * For a resource in the My Components or Public Components folder, set the **Maximum Number of Versions** option, then select **OK**. | The archive policy applies to the resource, overriding its inherited archive policy. Note iconIf you do not specify the archive policy, the resource will inherit the archive policy from its parent object, for example, the folder it resides in. |
| Apply archive policy when running a task in Advanced mode | 1. On the Server Console, go to the server resource tree in the Resources page, browse to the resource you want to run. 2. Put the mouse pointer over the resource row and select the **Advanced Run** button Advanced Run button on the floating toolbar. 3. In the **Archive** tab, select **Auto Archive Properties**. 4. Finish the other relevant information. Make sure that you set **Archive Location** to the resource tree folder. 5. Set the **Apply Archive Policy** option. 6. Select **Finish**. | The archive policy applies to a result type resource. Note iconIf you do not specify the archive policy, the resource will use its old archive policy or inherit the archive policy from its parent object, for example, the folder it resides in. |
| Apply archive policy when scheduling a task | 1. On the Server Console, go to the server resource tree in the Resources page, browse to the resource you want to schedule. 2. Put the mouse pointer over the resource row and select the **Schedule** button Schedule button on the floating toolbar. 3. In the **Publish** tab, select the **To Version** sub tab, then select **Publish to Versioning System**. 4. Finish the other relevant information. Make sure that you set **Archive Location** to the resource tree folder. 5. Set the **Apply Archive Policy option.** 6. Select **Finish**. | The archive policy applies to a result type resource. Note iconIf you do not specify the archive policy, the resource will use its old archive policy or inherit the archive policy from its parent object, for example, the folder it resides in. |

## Applying an Archive Policy to the Built-in Version Table

The versions in the built-in version folder have their own archive policy.

To apply an archive policy to the built-in version table, refer to the table:

| If you want to | Then do |
| --- | --- |
| Apply archive policy to a built-in version table | 1. Access the version table for the resource (report type) (for how to access the table, see [Browsing Versions](https://devnet.logianalytics.com/hc/en-us/articles/4405683939607-Browsing-Versions)). 2. In the **Report Result Versions** tab, select the **Maximum Number of Versions** option, then type a number in the text box. 3. Select **OK**. |
| Apply archive policy when running a task in Advanced mode | 1. On the Server Console, go to the server resource tree in the Resources page, browse to the resource you want to run. 2. Put the mouse pointer over the resource row and select the **Advanced Run** button Advanced Run button on the floating toolbar. 3. In the **Archive** tab, select the **Auto Archive Properties**  option. 4. Finish the other relevant information. Make sure that you set **Archive Location** to **Built-in Version Folder**. 5. Set the **Apply Archive Policy** option. 6. Select **Finish**. |
| Apply archive policy when scheduling a task | 1. On the Server Console, go to the server resource tree in the Resources page, browse to the resource you want to schedule. 2. Put the mouse pointer over the resource row and select the **Schedule** button Schedule button on the floating toolbar. 3. In the **Publish** tab, select the **To Version** sub tab, then select the **Publish to Versioning System** option. 4. Finish the other relevant information. Make sure that you set **Archive Location** to **Built-in Version Folder**. 5. Set the **Apply Archive Policy** option. 6. Select **Finish**. |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683941911-Checking-Version-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690646167-Deleting-Versions)
