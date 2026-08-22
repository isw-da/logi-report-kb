---
title: "Working with RLS and CLS at Data Source Scope"
id: 1500010094221
section: "Defining Report Security - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010094221-Working-with-RLS-and-CLS-at-Data-Source-Scope
updated_at: 2021-07-23T19:14:35Z
---

# Working with RLS and CLS at Data Source Scope

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010056702-Applying-Record-Level-and-Column-Level-Security)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094241-Applying-RLS-at-Report-Scope)

# Working with RLS and CLS at Data Source Scope

A security policy with Record Level Security (RLS) and Column Level Security (CLS) at data source scope refers to a security entry in the data source of a catalog. It enables you to control user access to different subsets of data, and ensures that people only see what they are supposed to see: certain records and/or report columns. This topic describes how you can define RLS and CLS at data source scope, meaning creating security entries in a catalog, and apply the security entries to reports.

If you want to implement the same security policy in a group of reports, you can simply apply the same security entry to the reports, without having to repeatedly build the security information for each report. The predefined security entries work within a data source range, that is you can apply them to reports that are in the same catalog data source. You can also use a security entry that contains RLS only to [control parameter values](https://devnet.logianalytics.com/hc/en-us/articles/1500010099741-Parameter-Application-Cases#RLS) at runtime.

This topic contains the following sections:

* [Creating Security Entries in a Catalog](#Create)
  + [Importing/Exporting Security Information from/to External XML Files](#Export)
* [Applying Security Entries to Reports](#Apply)

## Creating Security Entries in a Catalog

To add a security entry to a data source in a catalog, follow the steps below:

1. [Open the required catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500010056622-Creating-Opening-and-Saving-Catalogs#Open).
2. In the Catalog Manager, select the data source to which you want to add the security policy.
3. Right-click **Security Entry**  under the **Security** node and then select **New Security Entry** from the shortcut menu.
4. In the Enter Security Name dialog box, provide a name for the security policy and select **OK**. Designer displays the [Security dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060282-Security-Dialog-Box).

   ![Security dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856896919/scrty.gif)
5. In the **Users/Groups/Roles** panel, select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) and select **Import from Logi Report Server** from the drop-down menu, then in the [Import from Logi Report Server dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059582-Import-from-Logi-Report-Server-Dialog-Box), specify the properties for connecting to a started Server to import users, roles, and groups.
   Make sure that Server is started and you are an administrator user of Server in order to perform the importing.

   You can also select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) and select [Add User](https://devnet.logianalytics.com/hc/en-us/articles/1500010095561-Add-User-Dialog-Box), [Add Role](https://devnet.logianalytics.com/hc/en-us/articles/1500010095501-Add-Role-Dialog-Box), or [Add Group](https://devnet.logianalytics.com/hc/en-us/articles/1500010057942-Add-Group-Dialog-Box) from the drop-down menu to add principals manually in Designer or [import them from an XML file](#Export). However, if you choose the two methods to add users, roles, and groups, in order for the security policies specified on them to take effect on Server, you should make sure there are the same users, roles, and groups on Server, and then import them to Designer with the **Merge** option. In this way, Designer can update the users, roles, and groups to those on Server while reserving the security settings.

   You can further edit or remove the principals in the User/Group/Role panel.

   * To edit a user/role/group, select it and select the **Edit** button ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404856829719/btn_edit.gif). In the corresponding edit dialog box, edit it as required. Changes to Server users, roles, and groups made in Designer cannot take effect on Server.
   * To delete a user/role/group, select it and select the **Remove** button ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif).

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

   * You cannot re-assign a user from Server to (or remove it from) a role from Server; similarly, you cannot re-assign a role from Server (or remove it from) a user from Server. Therefore, if you obtain both the users and roles from Server, you are not able to change their parental relationships.
   * You cannot assign a role from Server to a local user created on Designer, while you can assign a user from Server to a local role.
   * During importing, if any existing users, roles, or groups that come from Server have the same names as those on Server, Designer refreshes their properties with new information from Server, such as the role or group information and parental relationships. However, Designer reserves their permission settings; specially, if you assign a user from Server to any roles defined in Designer, Designer reserves these roles in its member list.
6. Select a user/role/group in the principal box.
7. To apply record level security, select **Valid RLS**; to apply column level security, select **Valid CLS**.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) By default, Designer selects the Valid RLS checkbox but defines no condition in the **Record Level Security** tab, which means all the users, groups, and roles do not have any permissions.
8. Leave the **Disable Policy Settings** option unselected.
9. In the **Record Level Security** tab, specify the security conditions for the selected user/role/group. If you do not add a condition, the user/role/group is not able to view any records, unless it inherits permissions from its other roles and groups.
   1. Select the **ellipsis** button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404848397591/btn_ellipsis.gif) next to the **Expression** text box to specify the field on which to build the condition in the [Expressions dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058942-Expressions-Dialog-Box#RLS). You can also type the name of the field manually in the text box (the format should be *@FieldName* or *@"Field Name"* when the field name contains blank space).
   2. From the **Operator** drop-down list, set the operator with which to compose the condition.
   3. Select ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404848397591/btn_ellipsis.gif) next to the **Value** text box to specify the value of how to compose the condition using the Expressions dialog box. You can select the special field "[User Name](https://devnet.logianalytics.com/hc/en-us/articles/1500010094881-Working-with-Special-Fields#UserName)" or a parameter in the Expressions dialog box as the value to compose the condition dynamically (the usage of parameter in a security condition is similar to that of in a [query filter condition](https://devnet.logianalytics.com/hc/en-us/articles/1500010099741-Parameter-Application-Cases#FilterQuery)).

      You can also specify the value manually if you are familiar with the values of the specified field. When you type in the value, you need to:

      * Quote String values with single quotes.
      * Use the format of your database for Date values.
      * Separate multiple values with ",".
      * Type "," or "\" contained in the value as "\," or "\\".
   4. If you want to append a new condition line, select the **drop-down** button ![Drop-down button](https://devnet.logianalytics.com/hc/article_attachments/4404848444823/btn_drpdwn.gif) and select **AND** or **OR** from the drop-down menu. To add a new group, select ![Drop-down button](https://devnet.logianalytics.com/hc/article_attachments/4404848444823/btn_drpdwn.gif) beside the condition line which shows "End" or "End Group", then select **New Group** and specify the relationship between two adjacent groups.

      The following table lists the options that are available for adding condition lines and groups:

      | Option | Description |
      | --- | --- |
      | AND | Specify the relationship between two expression statements as logical "AND". If this line is the last line in the expression list, when you select AND or OR, Designer appends a new line to the end of the list. |
      | OR | Specify the relationship between two expression statements as logical "OR". If this line is the last line in the expression list, when you select AND or OR, Designer appends a new line to the end of the list. |
      | Insert Row | Insert a new line behind the current line. |
      | Delete Row | Delete the current line. |
      | New Group | Add a new expression group to the list. The relationships between two groups can be: * **AND** - Logical "AND" relationship between two groups. It specifies to retrieve records satisfying both condition groups. * **OR** - Logical "OR" relationship between two groups. It specifies to retrieve records satisfying either one of the condition groups. * **AND NOT** - Specify to retrieve records satisfying the first and not the second condition group * **OR NOT** - Specify to retrieve records satisfying the first or not the second condition group. |
10. In the **Column Level Security** tab, make a choice:
    * Select the **Select Column** option and then select the DBFields, formulas, parameters, or summaries. You can set the selected columns to be shown or hidden from the user/role/group by selecting the **Allow** or **Deny** option. Whether the principal can see the unselected columns depends on whether the parent groups/roles allow them.
    * Choose **Allow all** to show all the columns to the user/role/group.
    * Choose **Deny all** to hide all the columns from the user/role/group.

    ![Column Level Security](https://devnet.logianalytics.com/hc/article_attachments/4404848699799/scrty_rlscls_data_cls.gif)
11. Repeat steps 6 to 10 to customize another principal's RLS and CLS settings.
12. Select **OK** to create the security policy.

For any security entry, you can further edit it, rename it, or delete it according to your requirement. To do this, right-click the security entry in the Catalog Manager resource tree and select the corresponding option on the shortcut menu.

You can also export the security entries, together with the [business view security](https://devnet.logianalytics.com/hc/en-us/articles/1500010094141-Setting-Up-Business-View-Security) defined in a catalog to a security file using the File > Export Security command. Designer saves the security file in the same location as the current catalog by default. The Server administrators can then use the security file to create dynamic security for catalogs on Server (for more information , see Dynamic Security in the *Logi Report Server Guide*).

### Importing/Exporting Security Information from/to External XML Files

You can import or export your security information from/to external XML files (\*.acl.xml) when editing security in Designer. While if you want to use XML security information, you must first purchase a special license. For more information, contact Logi Analytics Support at [support@logianalytics.com.](mailto:support@logianalytics.com)

* To import the security information from an XML file, select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) in the User/Group/Role panel and then select **Import from File** from the drop-down menu. In the Open an xml file dialog box, select the XML file that contains the required security information and then select **Open**.
* To export the security information to an XML file, select the **Export** button ![Export button](https://devnet.logianalytics.com/hc/article_attachments/4404856897303/btn_expt2fl.gif) in the User/Group/Role panel. In the Save dialog box, specify the name of the file and the location where to save it, then select **Save**.

The following diagram shows the security information the XML file can contain:

![Security XML Structure](https://devnet.logianalytics.com/hc/article_attachments/4404857068439/scrty_rlscls_data_xml.gif)

You can create your own XML security information files according to the above structure; however, the best way to generate an XML security information file is to use the Security dialog box. With this dialog box, you can edit the security information, and then export it to an external XML file.

For example, if you create a simple security policy as follows:

| USER | |
| --- | --- |
| User Name: | d\_d\_u1 |
| Belongs to Role: | d\_d\_r1 |
| Permissions: | (@"Customer ID">=5 AND @"Customer ID"<=10) AND @"YTD Sales"<=65000 |
| ROLE | |
| Role Name: | d\_d\_r1 |
| Belongs to User: | d\_d\_u1 |

The corresponding XML code would be:

```
<ACL version="1.2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">  
   <ACLEntry>  
       <User>  
          <Roles>d_d_r1</Roles>  
          <UserName>d_d_u1</UserName>  
          <SourceName>UserDefined</SourceName>  
       </User>  
      <Permission>  
          <PermissionType>RLS</PermissionType>  
          <PermissionName>visible</PermissionName>  
          <Policy>  
              <SCGroup>  
                  <AndCondition>  
                    <logic>AND</logic>  
                    <Left>@&quot;Customer ID&quot;</Left>  
                    <operator>&gt;=</operator>  
                    <Right>5</Right>  
                  </AndCondition>  
                  <AndCondition>  
                    <logic>AND</logic>  
                    <Left>@&quot;Customer ID&quot;</Left>  
                    <operator>&lt;=</operator>  
                    <Right>10</Right>  
                  </AndCondition>  
              </SCGroup>  
              <SCGroup>  
                  <AndCondition>  
                    <logic>End</logic>  
                    <Left>@&quot;YTD Sales&quot;</Left>  
                    <operator>&lt;=</operator>  
                    <Right>65000</Right>  
                  </AndCondition>  
              </SCGroup>  
          </Policy>  
      </Permission>  
   </ACLEntry>  
   <ACLEntry>  
       <Role>  
          <RoleName>d_d_r1</RoleName>  
          <Users>d_d_u1</Users>  
          <SourceName>UserDefined</SourceName>  
       </Role>  
      <Permission>  
          <PermissionType>RLS</PermissionType>  
          <PermissionName>visible</PermissionName>  
          <Policy></Policy>  
      </Permission>  
   </ACLEntry>  
</ACL>
```

## Applying Security Entries to Reports

You can apply a security entry to a page report or library component by setting the Security Policy Name property on its [datasets](https://devnet.logianalytics.com/hc/en-us/articles/1500010062542-Creating-and-Managing-Datasets). However, since Column Level Security (CLS) is not supported on library components at present, you can only get the security entries which do not contain CLS in the value list of library components' Security Policy Name property.

1. Select **File** > **Open** to open the page report or library component to which you want to apply the security policy.
2. In the Report Inspector, select the name of a dataset used in the page report or library component under the **Datasets** node for page report or **Data Source** node for library component.
3. In the **Security** section of the Properties sheet, select a required security entry for the **Security Policy Name** property.

   ![Apply Security Entry](https://devnet.logianalytics.com/hc/article_attachments/4404857068951/scrty_rlscls_data_apply.gif)
4. You can repeat the above steps to apply security entries to other datasets in the page report or library component.

After you [publish the page report or library component to Server](https://devnet.logianalytics.com/hc/en-us/articles/1500010062722-Publishing-and-Downloading-Resources#Remotely), when different users log onto Server and run it, they will only see the data they are supposed to see. However, as Server may not be able to recognize the user-defined users, groups, and roles in a security entry, if your security policy contains such users, groups, or roles, you need to first create them respectively on Server, and then in Designer, synchronize the security information with Server by means of importing security information from Server with the **Merge** option selected.

Furthermore, for page reports, you can set and apply the security entries for the primary reports and subreports individually, which results in that different combinations cause different results. The following table shows the relationships between the security policy settings and the viewing results:

| Primary Report | Subreport | Users in Policy | Users NOT in Policy |
| --- | --- | --- | --- |
| Ð | Ð | Neither the primary report nor the subreport applies security policy. Users can therefore view all records in both reports. | |
| Ï | Ð | Can view specified records in the primary report and all records in the subreport. | Can view no records in the primary report and all records in the subreport. |
| Ð | Ï | Can view all records in the primary report and specified records in the subreport. | Can view all records in the primary report and no records in the subreport. |
| Ï | Ï | Can view specified records in both the primary report and the subreport. | Can view no records in either the primary report or the subreport. |

Ï - Security policy has been set and applied.  
Ð - Security policy has not been set and applied

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010056702-Applying-Record-Level-and-Column-Level-Security)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094241-Applying-RLS-at-Report-Scope)
