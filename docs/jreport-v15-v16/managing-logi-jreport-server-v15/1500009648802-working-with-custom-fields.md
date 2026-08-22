---
title: "Working with Custom Fields"
id: 1500009648802
section: "Managing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009648802-Working-with-Custom-Fields
updated_at: 2021-07-24T20:54:03Z
---

# Working with Custom Fields

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648842-Customizing-TTF-Font-Location-for-Resources)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673641-Changing-Resource-Properties)

# Working With Custom Fields

Custom fields are user-defined fields which can be used as resource properties, the same as Type, Description, Last Modified, and so on.

After a custom field is created and enabled by administrators, it will be available in the resource information table on both the Logi JReport Administration > Resources page and the Logi JReport Console > Resources page. End users can define its value by [setting properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009673641-Changing-Resource-Properties).

Below is a list of the sections covered in this topic:

* [Creating and Enabling Custom Fields](#Create)
* [Editing Custom Fields](#Edit)
* [Deleting Custom Fields](#Delete)
* [Setting Value to Custom Fields](#Value)
* [Hiding Custom Fields](#Hide)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Creating and Enabling Custom Fields

**To create a custom field:**

1. On the Logi JReport Administration page, select **Configuration** on the system toolbar, then select **Custom Fields** from the drop-down menu. The Configuration - Custom Fields page is displayed.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926693527/mng_rsc_cstmfld.gif)
2. Select **New Custom Field**.
3. In the [New Custom Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009646562-New-Custom-Field) dialog, provide a name and description for the custom field.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920490263/nwcstmfld.gif)
4. To enable the custom field, check the **Enabled** option.
5. Select **OK** to create the custom field.

   The new custom field is then added in the custom field table which consists of the following columns.

   | Column Name | Description |
   | --- | --- |
   | Custom Field Name | Displays the names of the custom fields. |
   | Description | Displays the information about the custom fields. |
   | Enabled | Shows whether the custom fields are enabled or not. |

   All columns in the table are sortable. To sort the table by certain column, select on the column name.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Editing Custom Fields

1. In the custom field table, select the row where the custom field is in, then select **Properties**.
2. In the displayed dialog, modify the name and description for the custom field, and change its status if required.
3. Select **OK** to accept the changes.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Deleting Custom Fields

Administrators can delete the custom fields that are not required at any time. To do this:

1. In the custom field table, select the row where the custom field is. You can select multiple custom fields.
2. Select **Delete**.
3. Select **OK** in the warning message to confirm the deletion.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Setting Value to Custom Fields

When you [publish resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009673621-Publishing-Resources) to Logi JReport Server, either locally/remotely or from Logi JReport Designer, if there are custom fields enabled, they will be displayed in the publishing dialog and you can specify the value of the custom fields for each resource according to your requirements. Also, the custom field values can be defined by [setting resource properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009673641-Changing-Resource-Properties).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Hiding Custom Fields

By default, all the enabled custom fields will be displayed in the resource information table on both the Logi JReport Administration > Resources panel page the Logi JReport Console > Resources page. If you want to hide a custom field from being shown in this table, follow the steps below:

**For administrators:**

1. Select **Profile** on the system toolbar of the Logi JReport Administration page, then select **Customize Server Preferences** from the drop-down menu.
2. In the General tab, unselect the checkbox in front of the corresponding custom field in the Columns Shown in Resources List section.
3. Select **OK** to accept the setting.

**For end users:**

End users can hide a custom field on the Logi JReport Console > Profile page as shown in the above method, and besides have a second choice:

1. On the Logi JReport Console > Resources page, select **Tools** > **Preferences** on the task bar.
2. In the General tab of the Preferences dialog, unselect the checkbox in front of the corresponding custom field, then select **OK**.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648842-Customizing-TTF-Font-Location-for-Resources)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673641-Changing-Resource-Properties)
