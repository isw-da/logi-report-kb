---
title: "Working with Custom Fields"
id: 4405683927831
section: "Managing Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683927831-Working-with-Custom-Fields
updated_at: 2022-01-27T07:59:39Z
---

# Working with Custom Fields

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683930903-Customizing-TTF-Font-Location-for-Resources)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683933975-Changing-Resource-Properties)

# Working With Custom Fields

Custom fields are user defined fields that you can use as resource properties, the same as Type, Description, and Last Modified. This topic describes how you can create and use custom fields.

You can create and maintain custom fields on the Server Console if you are an administrator.

This topic contains the following sections:

* [Creating and Enabling Custom Fields](#Create)
* [Setting Values to Custom Fields](#Value)
* [Hiding Custom Fields](#Hide)

## Creating and Enabling Custom Fields

1. On the system toolbar of the Server Console, navigate to **Administration** > **Other** > **Custom Fields**. Server displays the Custom Fields page.

   ![Custom Fields page](https://devnet.logianalytics.com/hc/article_attachments/4420447187863/mng_rsc_cstmfld.gif)
2. Select **New Custom Field**.
3. Server displays the [New Custom Field](https://devnet.logianalytics.com/hc/en-us/articles/4405690551447-New-Custom-Field-Dialog-Box-Properties) dialog box. Provide a name and description for the custom field.

   ![New Custom Field dialog](https://devnet.logianalytics.com/hc/article_attachments/4420447188119/nwcstmfld.gif)
4. To enable the custom field, select **Enabled**.
5. Select **OK** to create the custom field.

Server adds the new custom field in the custom field table which consists of the following columns.

| Column Name | Description |
| --- | --- |
| Custom Field Name | The names of the custom fields. |
| Description | The information about the custom fields. |
| Enabled | Show whether you have enabled the custom fields. |

In the custom field table, you can sort, edit, and delete the custom fields:

* To sort the custom fields by a column, select on the column name.
* To edit a custom field, select it in the table and select **Properties**. Server displays a dialog box. Modify the name and description for the custom field, change its status if you want, then select **OK** to accept the changes.
* To delete a custom field, select it in the table and select **Delete**. Select **OK** in the warning message to confirm the deletion. You can select multiple custom fields and delete them at a time.

## Setting Values to Custom Fields

When you [publish resources](https://devnet.logianalytics.com/hc/en-us/articles/4405683932951-Publishing-Resources) to Server, if there are custom fields enabled, Server displays them in the publishing dialog box and you can specify the values of the custom fields for each resource. You can also define the custom field values by [setting resource properties](https://devnet.logianalytics.com/hc/en-us/articles/4405683933975-Changing-Resource-Properties).

## Hiding Custom Fields

By default, Server displays all the enabled custom fields in the Resources page on the Server Console. If you want to hide a custom field from being shown in this page, follow the steps:

Any user can hide a custom field for themselves:

1. On the Server Console, go to the Resources page and navigate to **Tools** > **Preferences** on the task bar.
2. In the General tab of the Preferences dialog box, clear the custom field, then select **OK**.

Or,

1. On the Server Console, select **My Profile** on the system toolbar and select **Customize Server Preferences** from the drop-down menu.
2. In the Customize Server Preferences page, go to the **General** tab, clear the custom field in the **Columns Shown in Resources List** section.
3. Select **OK** to accept the setting.

Administrators can hide a custom field for all users:

1. On the system toolbar of the Server Console, navigate to **Administration** > **Server Profile** > **Customize Server Preferences**. Server displays the Customize Server Preferences page.
2. Go to the **General** tab, clear the corresponding custom fields in the **Columns Shown in Resources List** section.
3. Select **OK** to accept the setting.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683930903-Customizing-TTF-Font-Location-for-Resources)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683933975-Changing-Resource-Properties)
