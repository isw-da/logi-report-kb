---
title: "Working with Custom Fields"
id: 1500009717761
section: "Managing Resources"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009717761-Working-with-Custom-Fields
updated_at: 2021-11-03T06:56:55Z
---

# Working with Custom Fields

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009717821-Customizing-TTF-Font-Location-for-Resources)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009717861-Changing-Resource-Properties)

# Working With Custom Fields

Custom fields are user-defined fields which can be used as resource properties, the same as Type, Description, Last Modified, and so on. They are created and maintained by administrators in Logi JReport Server console.

Below is a list of the sections covered in this topic:

* [Creating and Enabling Custom Fields](#Create)
* [Setting Value to Custom Fields](#Value)
* [Hiding Custom Fields](#Hide)

## Creating and Enabling Custom Fields

1. In the server console, point to **Administration** on the system toolbar, and then select **Other** > **Custom Fields** from the drop-down menu to display the Custom Fields page.

   ![Custom Fields page](https://devnet.logianalytics.com/hc/article_attachments/4412112562327/mng_rsc_cstmfld.gif)
2. Select **New Custom Field**.
3. In the [New Custom Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009714701-New-Custom-Field) dialog, provide a name and description for the custom field.

   ![New Custom Field dialog](https://devnet.logianalytics.com/hc/article_attachments/4412131438231/nwcstmfld.gif)
4. To enable the custom field, check the **Enabled** option.
5. Select **OK** to create the custom field.

The new custom field is then added in the custom field table which consists of the following columns.

| Column Name | Description |
| --- | --- |
| Custom Field Name | Displays the names of the custom fields. |
| Description | Displays the information about the custom fields. |
| Enabled | Shows whether the custom fields are enabled or not. |

In the custom field table, administrators can sort, edit and delete the custom fields as follows:

* To sort the custom fields by a column, select on the column name.
* To edit a custom field, select it in the table and select **Properties** above the table. In the displayed dialog, modify the name and description for the custom field, change its status if required, then select **OK** to accept the changes.
* To delete a custom field, select it in the table and select **Delete** above the table. Select **OK** in the warning message to confirm the deletion. You can select multiple custom fields and delete them at a time.

## Setting Value to Custom Fields

When [publishing resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009717841-Publishing-Resources) to Logi JReport Server, if there are custom fields enabled, they will be displayed in the publishing dialog and you can specify the value of the custom fields for each resource according to your requirements. The custom field values can also be defined by [setting resource properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009717861-Changing-Resource-Properties).

## Hiding Custom Fields

By default, all the enabled custom fields will be displayed the Resources page in the server console. If you want to hide a custom field from being shown in this page, follow the steps below:

Any user can hide a custom field for himself:

1. In the server console, go to the Resources page and select **Tools** > **Preferences** on the task bar.
2. In the General tab of the Preferences dialog, unselect the checkbox in front of the corresponding custom field, then select **OK**.

Or,

1. In the server console, select **My Profile** on the system toolbar and select **Customize Server Preferences** from the drop-down menu.
2. In the Customize Server Preferences page, go to the General tab, unselect the checkbox in front of the corresponding custom field in the Columns Shown in Resources List section.
3. Select **OK** to accept the setting.

Administrators can hide a custom field for all users:

1. In the server console, point to **Administration** on the system toolbar, and then select **Server Profile** > **Customize Server Preferences** from the drop-down menu.
2. In the Customize Server Preferences page, go to the General tab, unselect the checkbox in front of the corresponding custom field in the Columns Shown in Resources List section.
3. Select **OK** to accept the setting.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009717821-Customizing-TTF-Font-Location-for-Resources)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009717861-Changing-Resource-Properties)
