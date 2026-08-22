---
title: "Configuring Business View Security"
id: 1500009593141
section: "Defining Report Security - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009593141-Configuring-Business-View-Security
updated_at: 2021-07-24T05:53:44Z
---

# Configuring Business View Security

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009571182-Permission-Logic-on-Group-Elements)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009571162-Example-of-Using-Business-View-Security)

# Configuring Business View Security

This topic demonstrates how to configure security on business views in a catalog.

1. In the Catalog Manager, do any of the following:
   * Expand the desired data source > **Security** node, right-click on **Business View Security** and select **Edit Business View Security** on the shortcut menu. The Edit Business View Security dialog is displayed.
   * When creating or editing a [business view](https://devnet.logianalytics.com/hc/en-us/articles/1500009562602-Creating-a-Business-View), select **Tools** > **Security Configuration**. The Edit Business View Security dialog is displayed.
   * When adding or editing a [business view element](https://devnet.logianalytics.com/hc/en-us/articles/1500009562642-Adding-and-Modifying-Elements) using dialog, switch to the **Security** tab.

   The following is a sample dialog.

   ![Business View Security dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889277847/edtbvscrty.gif)
2. In the Users/Groups/Roles panel, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) and select **Import from Logi JReport Server** from the drop-down menu**,** then in the [Connect to Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009566382-Import-from-Logi-JReport-Server-Dialog) dialog specify the information to connect to a started Logi JReport Server to import users, roles, and groups from the server, on which to set the security policy.
   Make sure that Logi JReport Server has been started and you are an administrator user of Logi JReport Server in order to perform the importing.

   You can also select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) and select **[Add User](https://devnet.logianalytics.com/hc/en-us/articles/1500009564502-Add-User-Dialog)**, **[Add Role](https://devnet.logianalytics.com/hc/en-us/articles/1500009585601-Add-Role-Dialog)** or **[Add Group](https://devnet.logianalytics.com/hc/en-us/articles/1500009585561-Add-Group-Dialog)** from the drop-down menu to add principals manually in Logi JReport Designer or import them [from an XML file](#Export), however if you choose to add users, groups and roles via these two ways, in order to make the business view security take effect on Logi JReport Server, the users, groups and roles should have been created in the Logi JReport Server security system before the reports involving the business view security are published to Logi JReport Server.

   You can further edit or remove the principals in the User/Group/Role panel.

   * To edit a user/role/group, select it and select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404893791511/btn_edit.gif). In the corresponding edit dialog, edit it as required. Changes to server users, roles, and groups will not take effect on Logi JReport Server.
   * To delete a user/role/group, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif).

   **Notes:**

   * A user from Logi JReport Server cannot be reassigned to (or removed from) a role from the server. Similarly, a role from the server cannot be re-assigned to (or removed from) a user from the server. So, if both users and roles are obtained from the server, you will not be able to change their parental relationships.
   * You cannot assign a role from the server to a local user created on Logi JReport Designer, while a user from the server can be assigned to a local role.
   * During importing, if any existing users, roles or groups that came from the server have the same names as those on the server, their properties will be refreshed with new information from the server, for example, role, or group information and parental relationships. However, their permission settings will be reserved. Specially, if a user from the server has been assigned to any roles defined in Designer, then these roles will be reserved in its member list.
3. Select one or more users/roles/groups in the principal box. You can use the quick search box to search for the required principals. If you want to select all users, roles or groups at a time, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889278103/btn_drpdwn.gif) and then select the corresponding item from the drop-down menu.
4. In the Resources box, select one or more fields. You can also use the quick search box to locate the required fields, or select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889278103/btn_drpdwn.gif) and select an item from the drop-down menu to select all the details, groups, aggregations, or categories in the current catalog data source at a time.
5. In the Security Options box, uncheck the **Use Default** option so as to customize the data security and resource security for the selected fields. If you want to use the default security settings of the selected fields, make the option checked.

   When only one principal and one field is selected, after you finish defining the data security and resource security, you can save the current security settings as the field's default security settings by selecting the **Set as Default** button.
6. In the Data Security box, specify whether the selected principals can access the values of the selected fields.
7. If a group field is selected, you can specify which members of the field are allowed and which are denied for the principals.
   1. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791511/btn_edit.gif) above the Allowed Set or Denied Set box. The [Edit Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009565422-Edit-Values-Dialog) dialog appears.

      ![Edit Values dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893793559/edtvlu.gif)
   2. Choose a way of specifying the members: select members from the available list, or compose an expression to retrieve members. Only one can be used.
      * To select members, first check the **Selected Values** radio button.

        If you would like all the possible members of the field to be selected, select **<All>**.

        If you just want to select some of the members, leave <All> unchecked. Add them one by one by selecting one and then selecting ![](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif). You can make use of the quick search toolbar to search for the required members.
      * To compose an expression, check the **Expression** radio button, then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889276567/btn_chsr.gif). The [Edit Conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009586381-Edit-Conditions-Dialog#FieldValue) dialog appears.

        ![Edit Conditions dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893793815/edtcndtn2.gif)

        Select the **Add Condition** button to add a condition line. Choose the operator with which to compose the condition expression from the operator drop-down list. From the value drop-down list, specify the value of how to build the condition. You can also type in the value manually. Select **Add Condition** to add more condition lines and define the relationship between the condition lines.

        To make some conditions grouped, select them and select the **Group** button, then the selected conditions will be added in one group and work as one line of filter expression. Conditions and groups together can be further grouped. To take any condition or group in a group out, select it and select **Ungroup.**

        To adjust the priority of the conditions, select it and select the **Up** or **Down** button.

        To delete a condition line, select it and select the **Delete** button.
   3. Select **OK** to save the values.
   4. If users are selected, check whether the unspecified members are available to the users.
8. In the Resource Security box, specify whether you want the fields to be visible to the principals.
9. Repeat steps 3 to 8 to customize other principals' permissions on different fields.
10. When finished, select **OK** in the dialog.
11. Save the catalog.

    When you save the catalog, the permission settings are also saved and they are saved in an authorization file in the same folder as the catalog file. The catalog and authorization files have the same file name but different extensions, for example, if the catalog file is test.cat, the authorization file will be named test.auth. The authorization file is loaded by the view authorization manager of its catalog during runtime.

See also [Edit Business View Security](https://devnet.logianalytics.com/hc/en-us/articles/1500009565182-Edit-Business-View-Security-Dialog) dialog for addition information about options in the dialogs.

**Note:** When a catalog with business view security is published to Logi JReport Server, only the principals on the server which match the principals defined in the business view security will maintain the business view security setting. When a principal is deleted from the server security system, the related business view security setting in all catalogs will be removed.

## Importing/exporting security information from/to external XML files

You can import or export your security information from/to external XML files (\*.acl.xml). While if you want to use XML security information, you must first purchase a special license. For more information, contact Jinfonet Support ([support@jinfonet.com](mailto:support@jinfonet.com)).

* To import the security information from an XML file, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) in the User/Group/Role panel and then select **Import from File**  from the drop-down menu. In the Open an xml file dialog, select the XML file that contains the required security information and then select **Open**.
* To export the security information to an XML file, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889278487/btn_expt2fl.gif) in the User/Group/Role panel. In the Save dialog, specify the name of the file and the location where to save it, then select **Save**.

The security information contained in the XML file is shown as follows:

![Security XML Structure](https://devnet.logianalytics.com/hc/article_attachments/4404893794071/scrty_bv_config_xml.gif)

You can create your own XML format security information files according to the above structure. However, the best way to generate an XML security information file is to use the Security dialog. With this dialog, you can edit the security information, and then export it to an external XML file.

For example, if the simple security policy has been set up as follows:

| USER | |
| --- | --- |
| User Name: | d\_d\_u1 |
| Belongs to Role: | d\_d\_r1 |
| Permissions: | (@"Customer ID">=5 AND @"Customer ID"<=10) AND @"YTD Sales"<=65000 |
| ROLE | |
| Role Name: | d\_d\_r1 |
| Belongs to User: | d\_d\_u1 |

The corresponding XML code would be:

|  |
| --- |
| `<ACL version="1.2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">    <ACLEntry>        <User>           <Roles>d_d_r1</Roles>           <UserName>d_d_u1</UserName>           <SourceName>UserDefined</SourceName>        </User>       <Permission>           <PermissionType>RLS</PermissionType>           <PermissionName>visible</PermissionName>           <Policy>               <SCGroup>                   <AndCondition>                     <logic>AND</logic>                     <Left>@&quot;Customer ID&quot;</Left>                     <operator>&gt;=</operator>                     <Right>5</Right>                   </AndCondition>                   <AndCondition>                     <logic>AND</logic>                     <Left>@&quot;Customer ID&quot;</Left>                     <operator>&lt;=</operator>                     <Right>10</Right>                   </AndCondition>               </SCGroup>               <SCGroup>                   <AndCondition>                     <logic>End</logic>                     <Left>@&quot;YTD Sales&quot;</Left>                     <operator>&lt;=</operator>                     <Right>65000</Right>                   </AndCondition>               </SCGroup>           </Policy>       </Permission>    </ACLEntry>    <ACLEntry>        <Role>           <RoleName>d_d_r1</RoleName>           <Users>d_d_u1</Users>           <SourceName>UserDefined</SourceName>        </Role>       <Permission>           <PermissionType>RLS</PermissionType>           <PermissionName>visible</PermissionName>           <Policy></Policy>       </Permission>    </ACLEntry> </ACL>` |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009571182-Permission-Logic-on-Group-Elements)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009571162-Example-of-Using-Business-View-Security)
