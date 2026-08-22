---
title: "RLS and CLS at Data Source Scope"
id: 1500009593181
section: "Defining Report Security - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009593181-RLS-and-CLS-at-Data-Source-Scope
updated_at: 2021-07-24T05:53:43Z
---

# RLS and CLS at Data Source Scope

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009571222-Record-level-and-Column-level-Security)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009593201-RLS-at-Report-Scope)

# RLS and CLS at Data Source Scope

A record-level security (RLS) and column-level security (CLS) policy at data source scope refers to a security entry in the data source of a catalog. It allows you to control user access to different subsets of data, and ensures that people only see what they are supposed to see: certain records and/or columns. If you want to implement the same security policy in a group of reports, you can simply apply the same security entry to the reports, without having to repeatedly build the security information for each report. The predefined security entries work within a data source range, that is they can be applied to resources that are in the same catalog data source.

A security entry with only RLS can also be used to [control parameter values](https://devnet.logianalytics.com/hc/en-us/articles/1500009590061-Applying-RLS-to-a-Parameter) at runtime.

Below is a list of the sections covered in this topic:

> * [Creating a Security Entry](#Create)
> * [Applying a Security Entry](#Apply)

## Creating a Security Entry

To add a security entry to a data source in a catalog, follow the steps below:

1. Open the required catalog.
2. In the Catalog Manager select the data source to which you want to add the security policy.
3. Right-click **Security Entry**  under the Security node and then select **Add Security Entry** from the shortcut menu.
4. In the Enter Security Name dialog, provide a name for the security policy and select **OK**. The [Security](https://devnet.logianalytics.com/hc/en-us/articles/1500009588521-Security-Dialog) dialog appears.

   ![Security dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889276055/security.gif)
5. In the Users/Groups/Roles panel, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) and select **Import from Logi JReport Server** from the drop-down menu, then in the [Import from Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009566382-Import-from-Logi-JReport-Server-Dialog) dialog specify the information to connect to a started Logi JReport Server to import users, roles, and groups from the server, on which to set the security policy.
   Make sure that Logi JReport Server has been started and you are an administrator user of Logi JReport Server in order to perform the importing.

   You can also select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) and select **[Add User](https://devnet.logianalytics.com/hc/en-us/articles/1500009564502-Add-User-Dialog)**, **[Add Role](https://devnet.logianalytics.com/hc/en-us/articles/1500009585601-Add-Role-Dialog)** or **[Add Group](https://devnet.logianalytics.com/hc/en-us/articles/1500009585561-Add-Group-Dialog)** from the drop-down menu to add principals manually in Logi JReport Designer or [from them an XML file](https://devnet.logianalytics.com/hc/en-us/articles/1500009593141-Configuring-Business-View-Security#Export).
   However if you choose the two methods to add users, roles and groups,
   in order for the security policies specified on them to work on Logi JReport Server, you should make sure there are the same users, roles and groups created on Logi JReport Server, and then import them to Logi JReport Designer with the Merge option.
   In this way the users, roles and groups are updated to those on the server while the security settings are reserved.

   You can further edit or remove the principals in the User/Group/Role panel.

   * To edit a user/role/group, select it and select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404893791511/btn_edit.gif). In the corresponding edit dialog, edit it as required. Changes to server users, roles, and groups will not take effect on Logi JReport Server.
   * To delete a user/role/group, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif).

   **Notes:**

   * A user from Logi JReport Server cannot be reassigned to (or removed from) a role from the server. Similarly, a role from the server cannot be re-assigned to (or removed from) a user from the server. So, if both users and roles are obtained from the server, you will not be able to change their parental relationships.
   * You cannot assign a role from the server to a local user created on Logi JReport Designer, while a user from the server can be assigned to a local role.
   * During importing, if any existing users, roles or groups that came from the server have the same names as those on the server, their properties will be refreshed with new information from the server, for example, role, or group information and parental relationships. However, their permission settings will be reserved. Specially, if a user from the server has been assigned to any roles defined in Designer, then these roles will be reserved in its members list.
6. Make a user/role/group selected. You can use the quick search box to search for the required principal.
7. To apply record-level security, check the **Valid RLS** box. To apply column-level security, check the **Valid CLS** box. By default the Valid RLS checkbox is selected but no condition is specified in the Record Level Security tab. In this case, all the users, groups, and roles do not have any permissions.
8. Leave the Disable Policy Settings option unchecked.
9. In the Record Level Security tab, specify the security conditions for the user/role/group.

   To build a condition statement, specify a field in the first text box. You can either type in the name of the field manually or select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404889276567/btn_chsr.gif) to specify the field. It can be a DBField, formula, parameter, or special field. Select an operator from the Operator drop-down list. Lastly, specify the value to complete the condition. You can select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404889276567/btn_chsr.gif) to specify the value or input the value manually, and when you type in the value, if multiple values are required, they should be separated with ",", and if "," or "\" is contained in the values, input it as "\," or "\\". You can also use a parameter to [apply a dynamic RLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009590061-Applying-RLS-to-a-Parameter).

   If you want to append a new row, in the More drop-down list, select AND or OR.

   | Values | Description |
   | --- | --- |
   | AND | Specifies the relationship between two expression statements as logical AND. If this line is the last line in the expression list, when you select AND or OR, a new line will be appended to the end of the list. |
   | OR | Specifies the relationship between two expression statements as logical OR. If this line is the last line in the expression list, when you select AND or OR, a new line will be append to the end of the list. |
   | Insert Row | Inserts a new line behind the current line. |
   | Delete Row | Deletes the current line. |
   | New Group | Adds a new expression group to the list. The relationships between two groups can be: * **AND** - Logical AND relationship between two groups. Records satisfying both condition groups will be retrieved. * **OR** - Logical OR relationship between two groups. Records satisfying either one of the condition groups will be retrieved. * **AND NOT** - Records satisfying the first and not the second condition group will be retrieved. * **OR NOT** - Records satisfying the first or not the second condition group will be retrieved. |
10. In the Column Level Security tab, make a choice:
    * Check the **Select Column** option and check the boxes to select the DBFields, formulas, parameters, or summaries. You can set the selected columns to be shown or hidden from the user/role/group by checking the Allow or Deny option. Whether the principal can see the unselected columns depends on whether the parent groups/roles allow them.
    * Choose **Allow all** to show all the columns to the user/role/group.
    * Choose **Deny all** to hide all the columns from the user/role/group.

    ![Column Level Security](https://devnet.logianalytics.com/hc/article_attachments/4404893791767/scrty_rlscls_cat_cls.gif)
11. Repeat steps 6 to 10 to customize another principal's record-level security and column-level security settings.
12. If necessary, you can [export the security information](https://devnet.logianalytics.com/hc/en-us/articles/1500009593141-Configuring-Business-View-Security#Export) defined in the security policy to an XML file.
13. Upon finishing, select the **OK** button to create the security policy.

Once a security entry is created, you can further edit it, rename it, or delete it according to your requirement. To do this, right-click the security entry in the Catalog Manager resource tree and select the corresponding option on the shortcut menu.

## Applying a Security Entry

You can apply a security entry to a page report or library component by setting the Security Policy Name property on its dataset. However, since column-level security is not supported on library components at present, only the security entries which have not been defined with CLS are available in the value list of library components' Security Policy Name property.

1. Open the report or library component to which you want to apply the security policy.
2. In the Report Inspector, select the node that represents the dataset the report or library component uses in the Datasets node.
3. In the Security section of the Properties sheet, select a required security entry for the Security Policy Name property.

After the report or library component is [published to Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009592641-Publishing-Resources#Remotely), when different users log onto the server and run it, they will only see the data they are supposed to see. However, as the user defined users and roles in a security entry may not be recognized by Logi JReport Server, if your security policy contains such users/roles, you need to first create these users and roles respectively on Logi JReport Server, and then in Logi JReport Designer, synchronize the security information with the server by means of [importing security information from the sever](https://devnet.logianalytics.com/hc/en-us/articles/1500009593141-Configuring-Business-View-Security#Server) with the Merge option checked.

However for page reports, the security entries for the primary reports and subreports can be set and applied individually, with different combinations causing different results. The relationships between the security policy settings and the viewing results are shown in the following table:

| Primary Report | Subreport | Users in Policy | Users NOT in Policy |
| --- | --- | --- | --- |
| Ð | Ð | No security policy is applied to either the primary report or the subreport. Users can therefore view all records in both reports. | |
| Ï | Ð | Can view specified records in the primary report and all records in the subreport. | Can view no records in the primary report and all records in the subreport. |
| Ð | Ï | Can view all records in the primary report and specified records in the subreport. | Can view all records in the primary report and no records in the subreport. |
| Ï | Ï | Can view specified records in both the primary report and the subreport. | Can view no records in either the primary report or the subreport. |

Ï - Security policy has been set and applied.  
Ð - Security policy has not been set and applied

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009571222-Record-level-and-Column-level-Security)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009593201-RLS-at-Report-Scope)
