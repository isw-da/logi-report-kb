---
title: "Working with Custom Fields"
id: 28891673834637
section: "Managing Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891673834637-Working-with-Custom-Fields
updated_at: 2026-02-26T02:13:29Z
source_host: docs-report.zendesk.com
---
# 
Working With Custom Fields 

Custom fields are user defined fields that you can use as resource properties, the same as Type, Description, and Last Modified. This topic describes how you can create and use custom fields.

You can create and maintain custom fields on the Server Console if you are an administrator.

This topic contains the following sections:

- 
                    Creating and Enabling Custom Fields
                

- 
                    Setting Values to Custom Fields
                

- 
                    Hiding Custom Fields
                

## 
Creating and Enabling Custom Fields

- On the system toolbar of the Server Console, navigate to Administration > Other > Custom Fields. Server displays the Custom Fields page.
    

- Select New Custom Field.

- Server displays the New Custom Field dialog box. Provide a name and description for the custom field.
    

- To enable the custom field, select Enabled.

- Select OK to create the custom field. 

Server adds the new custom field in the custom field table which consists of the following columns.

| Column Name | Description |
| --- | --- |
| Custom Field Name | The names of the custom fields. |
| Description | The information about the custom fields. |
| Enabled | Show whether you have enabled the custom fields. |

In the custom field table, you can sort, edit, and delete the custom fields: 

- To sort the custom fields by a column, select on the column name. 

- To edit a custom field, select it in the table and select Properties. Server displays a dialog box. Modify the name and description for the custom field, change its status if you want, then select OK to accept the changes. 

- To delete a custom field, select it in the table and select Delete. Select OK in the warning message to confirm the deletion. You can select multiple custom fields and delete them at a time.

## 
Setting Values to Custom Fields

When you publish resources to Server, if there are custom fields enabled, Server displays them in the publishing dialog box and you can specify the values of the custom fields for each resource. You can also define the custom field values by setting resource properties.

## 
Hiding Custom Fields

By default, Server displays all the enabled custom fields in the Resources page on the Server Console. If you want to hide a custom field from being shown in this page, follow the steps: 

Any user can hide a custom field for themselves:

- On the Server Console, go to the Resources page and navigate to Tools > Preferences on the task bar. 

- In the General tab of the Preferences dialog box, clear the custom field, then select OK.

Or,

-  On the Server Console, select My Profile on the system toolbar and select Customize Server Preferences from the drop-down menu.

- In the Customize Server Preferences page, go to the General tab, clear the custom field in the Columns Shown in Resources List section.

- Select OK to accept the setting. 

Administrators can hide a custom field for all users: 

-  On the system toolbar of the Server Console, navigate to Administration > Server Profile > Customize Server Preferences. Server displays the Customize Server Preferences page.

- Go to the General tab, clear the corresponding custom fields in the Columns Shown in Resources List section.

- Select OK to accept the setting.
