---
title: "Record Level and Column Level Security"
id: 1500010063241
section: "Defining Report Security - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010063241-Record-Level-and-Column-Level-Security
updated_at: 2021-07-24T10:39:31Z
---

# Record Level and Column Level Security

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010028602-Cached-Report-Bursting) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010028582-Business-View-Security)

# Record Level and Column Level Security

Record Level Security (RLS) and Column Level Security (CLS) allow you to control user access to different subsets of data and ensure that people only see what they are supposed to see: RLS allows you to define which records are to be revealed to any given user, while CLS allows you to define which report column is revealed to any given user. This enables you to provide different users with accordingly different, but appropriate contents. No matter to whom you need to provide information, a plant manager or thousands of customers, Logi JReport allows you to control access to information according to your requirements.

You can define record level security either based on a catalog data source, or on a single report, or simultaneously on both. When a report is applied RLS of both the report and data source scopes, the report scope RLS will override that of the data source scope. Column level security can be defined on data source scope only.

Below is a list of the sections covered in this topic:

* [RLS and CLS at Data Source Scope](#Data)
  + [Creating a Security Entry](#Create)
    - [Importing/Exporting Security Information from/to External XML Files](#Export)
  + [Applying a Security Entry](#Apply)
* [RLS at Report Scope](#Report)

## RLS and CLS at Data Source Scope

A RLS and CLS policy at data source scope refers to a security entry in the data source of a catalog. It allows you to control user access to different subsets of data, and ensures that people only see what they are supposed to see: certain records and/or columns. If you want to implement the same security policy in a group of reports, you can simply apply the same security entry to the reports, without having to repeatedly build the security information for each report. The predefined security entries work within a data source range, that is they can be applied to resources that are in the same catalog data source. A security entry with only RLS can also be used to [control parameter values](https://devnet.logianalytics.com/hc/en-us/articles/1500010068981-Parameter-Application-Cases#RLS) at runtime.

Security entries, together with the [business view security](https://devnet.logianalytics.com/hc/en-us/articles/1500010028582-Business-View-Security) defined in a catalog can be exported to a security file using the File > Export Security command, which will be stored in the same location as the current catalog. The security file can be used to create dynamic security for catalogs on Logi JReport Server (for details, see Dynamic Security in the *Logi JReport Server User's Guide*).

### Creating a Security Entry

To add a security entry to a data source in a catalog, follow the steps below:

1. Open the required catalog.
2. In the Catalog Manager select the data source to which you want to add the security policy.
3. Right-click **Security Entry**  under the Security node and then select **New Security Entry** from the shortcut menu.
4. In the Enter Security Name dialog, provide a name for the security policy and select **OK**. The [Security](https://devnet.logianalytics.com/hc/en-us/articles/1500010067681-Security-Dialog) dialog appears.

   ![Security dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901183511/scrty.gif)
5. In the Users/Groups/Roles panel, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif) and select **Import from JReport Server** from the drop-down menu, then in the [Import from JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500010066841-Import-from-JReport-Server-Dialog) dialog specify the properties for connecting to a started Logi JReport Server to import users, roles, and groups.
   Make sure that Logi JReport Server has been started and you are an administrator user of the server in order to perform the importing.

   You can also select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif) and select [Add User](https://devnet.logianalytics.com/hc/en-us/articles/1500010064761-Add-User-Dialog), [Add Role](https://devnet.logianalytics.com/hc/en-us/articles/1500010029722-Add-Role-Dialog) or [Add Group](https://devnet.logianalytics.com/hc/en-us/articles/1500010064681-Add-Group-Dialog) from the drop-down menu to add principals manually in Logi JReport Designer or [import them from an XML file](#Export). However if you choose the two methods to add users, roles and groups, in order for the security policies specified on them to work on Logi JReport Server, you should make sure there are the same users, roles and groups created on Logi JReport Server, and then import them to Logi JReport Designer with the Merge option. In this way the users, roles and groups are updated to those on the server while the security settings are reserved.

   You can further edit or remove the principals in the User/Group/Role panel.

   * To edit a user/role/group, select it and select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404901116439/btn_edit.gif). In the corresponding edit dialog, edit it as required. Changes to server users, roles, and groups will not take effect on Logi JReport Server.
   * To delete a user/role/group, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif).

   **Notes:**

   * A user from Logi JReport Server cannot be reassigned to (or removed from) a role from the server. Similarly, a role from the server cannot be re-assigned to (or removed from) a user from the server. Therefore if both users and roles are obtained from the server, you will not be able to change their parental relationships.
   * You cannot assign a role from the server to a local user created on Logi JReport Designer, while a user from the server can be assigned to a local role.
   * During importing, if any existing users, roles or groups that came from the server have the same names as those on the server, their properties will be refreshed with new information from the server, for example, role, or group information and parental relationships. However, their permission settings will be reserved. Specially, if a user from the server has been assigned to any roles defined in Designer, then these roles will be reserved in its members list.
6. Make a user/role/group selected.
7. To apply record level security, check the **Valid RLS** box. To apply column level security, check the **Valid CLS** box. By default the Valid RLS checkbox is selected but no condition is specified in the Record Level Security tab. In this case, all the users, groups, and roles do not have any permissions.
8. Leave the Disable Policy Settings option unchecked.
9. In the Record Level Security tab, specify the security conditions for the user/role/group. If no condition is added, the user/role/group will not be able to view any records, unless it inherits permissions from its other roles and groups.
   1. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404901122967/btn_chsr.gif) next to the Expression text box to specify the field on which to build the condition in the [Expressions](https://devnet.logianalytics.com/hc/en-us/articles/1500010065881-Expressions-Dialog#RLS) dialog. You can also type the name of the field manually in the text box (the input format should be *@FieldName* or *@"Field Name"* when the field name contains blank space).
   2. From the Operator drop-down list, set the operator with which to compose the condition.
   3. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404901122967/btn_chsr.gif) next to the Value text box to specify the value of how to compose the condition using the Expressions dialog. You can select the special field [User Name](https://devnet.logianalytics.com/hc/en-us/articles/1500010029242-Special-Fields#UserName) or a parameter in the Expressions dialog as the value to compose the condition dynamically (the usage of parameter in a security condition is similar to that of in a [query filter condition](https://devnet.logianalytics.com/hc/en-us/articles/1500010068981-Parameter-Application-Cases#FilterQuery)).

      If you are familiar with the values of the specified field, you can also input the value manually. When you type in the value: String values should be quoted with single quotes; the format of Date values should be consistent with that of your database; multiple values should be separated with ","; if "," or "\" is contained in the values, write it as "\," or "\\".
   4. If you want to append a new condition line, select ![Add Row button](https://devnet.logianalytics.com/hc/article_attachments/4404901280151/btn_addrow.gif) and select **AND** or **OR** from the drop-down menu. To add a new group, select ![Add Row button](https://devnet.logianalytics.com/hc/article_attachments/4404901280151/btn_addrow.gif) beside the condition line which shows End or End Group, then select **New Group** and specify the relationship between two adjacent groups.

      The following table lists the options that are available for adding condition lines and groups:

      | Option | Description |
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

    ![Column Level Security](https://devnet.logianalytics.com/hc/article_attachments/4404909290391/scrty_rlscls_dt1.gif)
11. Repeat steps 6 to 10 to customize another principal's record level security and column level security settings.
12. Select **OK** to create the security policy.

Once a security entry is created, you can further edit it, rename it, or delete it according to your requirement. To do this, right-click the security entry in the Catalog Manager resource tree and select the corresponding option on the shortcut menu.

#### Importing/Exporting Security Information from/to External XML Files

You can import or export your security information from/to external XML files (\*.acl.xml) when editing security in Logi JReport Designer. While if you want to use XML security information, you must first purchase a special license. For more information, contact Logi Analytics Support ([support@jinfonet.com](mailto:support@jinfonet.com)).

* To import the security information from an XML file, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif) in the User/Group/Role panel and then select **Import from File**  from the drop-down menu. In the Open an xml file dialog, select the XML file that contains the required security information and then select **Open**.
* To export the security information to an XML file, select ![Export button](https://devnet.logianalytics.com/hc/article_attachments/4404909158167/btn_expt2fl.gif) in the User/Group/Role panel. In the Save dialog, specify the name of the file and the location where to save it, then select **Save**.

The security information contained in the XML file is shown as follows:

![Security XML Structure](https://devnet.logianalytics.com/hc/article_attachments/4404901343639/scrty_rlscls_xml.gif)

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

### Applying a Security Entry

You can apply a security entry to a page report or library component by setting the Security Policy Name property on its [datasets](https://devnet.logianalytics.com/hc/en-us/articles/1500010070661-Creating-and-Managing-Datasets). However, since Column Level Security (CLS) is not supported on library components at present, only the security entries which have not been defined with CLS are available in the value list of library components' Security Policy Name property.

1. Select **File** > **Open** to open the page report or library component to which you want to apply the security policy.
2. In the Report Inspector, select the name of a dataset used in the page report or library component under the Datasets node for page report or Data Source node for library component.
3. In the Security section of the Properties sheet, select a required security entry for the Security Policy Name property.

   ![Apply Security Entry](https://devnet.logianalytics.com/hc/article_attachments/4404901343895/scrty_rlscls_dt2.gif)
4. Repeat the above steps to apply security entries to other datasets in the page report or library component if needed.

After the page report or library component is [published to Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500010070761-Publishing-and-Downloading-Resources#Remotely), when different users log onto the server and run it, they will only see the data they are supposed to see. However, as the user defined users and roles in a security entry may not be recognized by Logi JReport Server, if your security policy contains such users/roles, you need to first create these users and roles respectively on Logi JReport Server, and then in Logi JReport Designer, synchronize the security information with the server by means of importing security information from the sever with the Merge option checked.

However for page reports, the security entries for the primary reports and subreports can be set and applied individually, with different combinations causing different results. The relationships between the security policy settings and the viewing results are shown in the following table:

| Primary Report | Subreport | Users in Policy | Users NOT in Policy |
| --- | --- | --- | --- |
| Ð | Ð | No security policy is applied to either the primary report or the subreport. Users can therefore view all records in both reports. | |
| Ï | Ð | Can view specified records in the primary report and all records in the subreport. | Can view no records in the primary report and all records in the subreport. |
| Ð | Ï | Can view all records in the primary report and specified records in the subreport. | Can view all records in the primary report and no records in the subreport. |
| Ï | Ï | Can view specified records in both the primary report and the subreport. | Can view no records in either the primary report or the subreport. |

Ï - Security policy has been set and applied.  
Ð - Security policy has not been set and applied

## RLS at Report Scope

Record Level Security (RLS) can also be of report scope, that is, you can create different record level security policies for different reports. When a report is applied RLS of both the report and data source scopes, the report scope RLS will override that of the data source scope. Column Level Security (CLS) is not supported at report scope.

RLS at report scope cannot be applied to reports that use business view as the data source, that is it is only supported on a query based page report.

**To set up a record level security policy for a query based page report:**

1. Select **File** > **Open** to open the page report.
2. In the Report Inspector, select the name of a dataset used in the page report or library component under the Datasets node for page report or Data Source node for library component.
3. In the Security section of the Properties sheet, select in the value cell of the Record Security property, then select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404909121559/btn_chsr1.gif).

   ![Set Record Security Property](https://devnet.logianalytics.com/hc/article_attachments/4404901344151/scrty_rlscls_rpt.gif)

   The [Record Level Security Information](https://devnet.logianalytics.com/hc/en-us/articles/1500010067601-Record-Level-Security-Information-Dialog) dialog appears.

   ![Record Level Security Information dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901184279/rlsinfo.gif)
4. Select the **Add** button to add a condition line and edit the security information by selecting corresponding cells.

   If you want to use more values in one cell, use "|" to separate them (applies to the User, E-mail, and Title cells). This is useful when you want to apply the same conditions to multiple users. For example, if you want user1, user2, and user3 to share the same security setting, input **user1|user2|user3** in the User cell, and then define the security condition.
5. Add more condition lines as required. If you want to apply more than one condition expression to a user, you can edit the condition expressions in several individual lines, typing in the same user name for each line. For such compound conditions, the relationship among them is logical OR.

   You can also create a text file, add the security settings, and then select **Import Text** to import the security information from the text file into the Record Level Security Information dialog. After importing, you can select the cells to further edit the security settings if required. Note that when you create the text file to include the security information, you should use TAB to separate each item, and always keep the headings (User, Role, Column, and so on) on the first line of the text file. For example,

   | User | Role | Column | Operator | Value | E-mail | Title |
   | --- | --- | --- | --- | --- | --- | --- |
   | admin | admin |  |  |  |  |  |
   | user1 |  | Customer ID | >= | 10 | user1@yoursite.com | Mr. |
   | user1 |  | Customer Name | = | 'Absolute Java' |  |  |
   | user2 |  | Customer Name | IN | ('Absolute Java','American Coffee Inc.') | user2@yoursite.com | Miss |
   | user3 |  | Phone | IN | ('(212) 555-3462','(317) 555-1274') | user3@yoursite.com | Mrs. |
6. Select **OK** to finish defining the security information and close the dialog.
7. If necessary, you can also use a formula to specify the security condition and set it as value of the Function property on the dataset of the report to control the RLS conditions on the report.

   For example, if user1 should only see records which satisfy the condition State = 'CO' and Customer ID >= 10, you can create a formula as follows:

   `if ( @State == 'CO' && @"Customer ID">= 10 ) return "user1"`

   Then from the value list of the Function property, select the formula.

   When the Record Security and Function properties have been set to control the record level security on a report, both will take effect, and the relationship between them is logical OR.
8. Repeat the above steps to define record level security on the rest datasets in the page report if needed.

After the report is [published to Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500010070761-Publishing-and-Downloading-Resources#Remotely), when different users log onto the server and run it, they will only see the data they are supposed to see.

**Note:** In the Record Level Security Information dialog, the date values provided in the drop-down list may not be valid for your database, because they are date values that have already been reformatted using your date format settings in Logi JReport. For detailed information on how to set the date format in Logi JReport Designer, [select here](https://devnet.logianalytics.com/hc/en-us/articles/1500010031562-Get-JDBC-Connection-Information-Dialog#DateFormat).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010028602-Cached-Report-Bursting) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010028582-Business-View-Security)
