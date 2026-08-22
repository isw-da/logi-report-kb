---
title: "Applying an Archive Policy"
id: 1500009673721
section: "Managing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009673721-Applying-an-Archive-Policy
updated_at: 2021-07-24T20:54:01Z
---

# Applying an Archive Policy

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673781-Checking-Version-Properties)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673761-Deleting-Versions)

# Applying an Archive

Logi JReport Server uses an archive policy to control resource versions. The archive policy can be applied to a single resource individually or to many resources in a folder as a whole. It can also be applied when you publish resources to the server resource tree or when you advanced run or schedule a report.

When applying an archive policy, you can choose whether to use multiple versions for a resource or always use the new version to replace the old one.

**Archive as New Version**

Specifies to use multiple versions for the specified resource.

* **Maximum Number of Versions**  
   Specifies the maximum number of versions that will be listed in the version table of the resource. The default value is 0, which means that the version number is unlimited.

**Replace Old Version**

Specifies to replace the old version when a new version is generated.

If there is no archive policy specified for a resource, the resource will inherit the archive policy from its parent. If afterwards you then specify an archive policy for the resource, the new policy will override the one inherited from the parent.

Below is a list of the sections covered in this topic:

* [Applying an Archive Policy to Resources in the Resource Tree](#Tree)
* [Applying an Archive Policy to the Built-In Version Table](#Table)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Applying an Archive Policy to Resources in the Resource Tree

To apply an archive policy to a resource in the resource tree, refer to the table below:

| If you want to | Then do | Result |
| --- | --- | --- |
| Apply archive policy when publishing resource | In the publish resource dialog (for how to access the dialog, see [Publishing Resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009673621-Publishing-Resources)):  * If the resource is to be published to the My Reports or Public Reports folder, set the Apply Archive Policy option as required. * If the resource is to be published to the My Components or Public Components folder, set the Maximum Number of Versions option as required. | The archive policy is applied to the resource. **Note:** A folder by itself does not have versions; the archive policy specified for a folder applies to the folder content. |
| Apply archive policy to a folder | 1. Access the Properties dialog for the folder (for how to access the dialog, see [Changing Resource and Folder Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009673641-Changing-Resource-Properties)). 2. In the dialog,    * For folder in the My Reports or Public Reports folder (including the root folder itself), set the Apply Archive Policy option as required, then select **OK**.    * For folder in the My Components or Public Components folder (including the root folder itself), set the Maximum Number of Versions option as required, then select **OK**. | The archive policy will be applied to all of the folder content. **Note:** This does not include resources that already have individually applied archive policies. |
| Apply archive policy to a resource | 1. Access the Properties dialog for the resource (for how to access the dialog, see [Changing Resource and Folder Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009673641-Changing-Resource-Properties)). 2. In the dialog,    * For resource in the My Reports or Public Reports folder, set the Apply Archive Policy option as required, then select **OK**.    * For resource in the My Components or Public Components folder, set the Maximum Number of Versions option as required, then select **OK**. | The archive policy is applied to the resource, overriding its inherited archive policy. **Note:** If you leave the archive policy unspecified, the resource will inherit the archive policy from its parent object, for example, the folder it resides in. |
| Apply archive policy when running a task in Advanced mode | 1. On the Logi JReport Console > Resources page, browse to the resource you want to run. 2. Put the mouse pointer over the resource row and select the **Advanced Run** button  on the floating toolbar. 3. In the Archive tab, check the **Auto Archive Properties**  option. 4. Finish the other relevant information, making sure that Archive Location is set to the resource tree folder. 5. Set the Apply Archive Policy option as required, and then select **Finish**. | The archive policy will be applied to a result type resource. **Note:** If you leave the archive policy unspecified, the resource will use its old archive policy or inherit the archive policy from its parent object, for example, the folder it resides in. |
| Apply archive policy when scheduling a task | 1. On the Logi JReport Console > Resources page, browse to the resource you want to schedule. 2. Put the mouse pointer over the resource row and select the **Schedule** button  on the floating toolbar. 3. In the Publish tab, select the **To Version** sub tab, then check the **Publish to Versioning System** option. 4. Finish the other relevant information, making sure that Archive Location is set to the resource tree folder. 5. Set the Apply Archive Policy option as required, then select **Finish**. | The archive policy is applied to a result type resource. **Note:** If you leave the archive policy unspecified, the resource will use its old archive policy or inherit the archive policy from its parent object, for example, the folder it resides in. |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Applying an Archive Policy to the Built-In Version Table

The above table applies to the resource in the resource tree only. The versions in the built-in version folder are controlled by its own archive policy.

To apply an archive policy to the built-in version table, refer to the table below:

| If you want to | Then do |
| --- | --- |
| Apply archive policy to a built-in version table | 1. Access the version table for the resource (report type) (for how to access the table, see [Browsing Versions](https://devnet.logianalytics.com/hc/en-us/articles/1500009673741-Browsing-Versions)). 2. In the Report Result Versions tab, check the **Maximum Number of Versions** option, specify the versions to be saved as required, then select **OK**. |
| Apply archive policy when running a task in Advanced mode | 1. On the Logi JReport Console > Resources page, browse to the resource you want to run. 2. Put the mouse pointer over the resource row and select the **Advanced Run** button  on the floating toolbar. 3. In the Archive tab, check the **Auto Archive Properties**  option. 4. Finish the other relevant information, making sure that Archive Location is set to the Built-in Version Folder. 5. Set the Apply Archive Policy option as required, then select **Finish**. |
| Apply archive policy when scheduling a task | 1. On the Logi JReport Console > Resources page, browse to the resource you want to schedule. 2. Put the mouse pointer over the resource row and select the **Schedule** button  on the floating toolbar. 3. In the Publish tab, select the **To Version** sub tab, then check the **Publish to Versioning System** option. 4. Finish the other relevant information, making sure that Archive Location is set to Built-in Version Folder. 5. Set the Apply Archive Policy option as required, then select **Finish**. |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673781-Checking-Version-Properties)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673761-Deleting-Versions)
