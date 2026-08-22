---
title: "Business View Security"
id: 1500009605382
section: "Defining Report Security - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009605382-Business-View-Security
updated_at: 2021-07-24T16:05:25Z
---

# Business View Security

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009605402-Record-Level-and-Column-Level-Security) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009610882-Printing-and-Exporting-Reports)

# Business View Security

Business view security enables report designers to limit user access to [elements](https://devnet.logianalytics.com/hc/en-us/articles/1500009613122-Business-View-Elements) of the business views in a catalog. After defining users, groups and roles' permissions on the view elements, when a user accesses a report at runtime that involves the view elements, Logi Report checks the user, group and role of the user and merges the data in the report the user is authorized to see and displays it to the user, thus different report result can be created for different users. Business view security also applies to new reports end users create on Logi Report Server using the business views.

Business view security contains two parts:

* **Data security**  
  It controls whether a user/role/group can access the data of the view elements at runtime. For a group object, you can further allow or deny the access of its specific members to a user/role/group.
* **Resource security**  
  It controls whether a user/role/group can see the view elements at runtime.

Business view security, together with the [security entries](https://devnet.logianalytics.com/hc/en-us/articles/1500009605402-Record-Level-and-Column-Level-Security#Data) defined in a catalog can be exported to a security file using the File > Export Security command, which will be stored in the same location as the current catalog. The security file can be used to create dynamic security for catalogs on Logi Report Server (for details, refer to Dynamic Security in the *Logi Report Server Guide*).

This topic includes the following sections:

* [Configuring Business View Security in a Catalog](#Configure)
  + [Permission Logic on Group Objects](#Logic)
* [Example of Using Business View Security](#Example)

## Configuring Business View Security in a Catalog

To define security for the business views in a catalog, take the following steps:

1. [Open the required catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009628301-Creating-Opening-and-Saving-Catalogs#Open).
2. In the Catalog Manager, do any of the following:
   * Expand the desired data source > **Security** node, right-click on **Business View Security** and select **Edit Business View Security** on the shortcut menu. The Edit Business View Security dialog is displayed.
   * When [working with a business view in the Business View Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009613102-Creating-Business-Views-in-a-Catalog), select **Menu** > **Tools** > **Security Configuration**. The Edit Business View Security dialog is displayed.
   * When [adding or editing a business view element using dialog](https://devnet.logianalytics.com/hc/en-us/articles/1500009613102-Creating-Business-Views-in-a-Catalog#Category), switch to the **Security** tab.

   The following is a sample dialog.

   ![Business View Security dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904352919/edtbvscrty.gif)
3. In the Users/Groups/Roles panel, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) and select **Import from Logi Report Server** from the drop-down menu (before importing you should make sure Logi Report Server is started). The users, roles and groups created on the server are then added in the principal box if Logi Report Designer can connect to the server and log you in automatically, otherwise you will be prompted with the [Connect to Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009607442-Connect-to-Logi-Report-Server-Dialog) dialog to specify the properties for connecting with the server first. The logged-in user should be an administrator user of the started Logi Report Server so that the importing can be successfully performed.

   You can also select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) and select [Add User](https://devnet.logianalytics.com/hc/en-us/articles/1500009629881-Add-User-Dialog), [Add Role](https://devnet.logianalytics.com/hc/en-us/articles/1500009629861-Add-Role-Dialog) or [Add Group](https://devnet.logianalytics.com/hc/en-us/articles/1500009629841-Add-Group-Dialog) from the drop-down menu to add principals manually in Logi Report Designer or import them [from an XML file](https://devnet.logianalytics.com/hc/en-us/articles/1500009605402-Record-Level-and-Column-Level-Security#Export), however if you choose to add users, groups and roles via these two ways, in order to make the business view security take effect on Logi Report Server, the users, groups and roles should have been created in the Logi Report Server security system before the reports involving the business view security are published to Logi Report Server.

   You can further edit or remove the principals in the User/Group/Role panel.

   * To edit a user/role/group, select it and select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404911588375/btn_edit.gif). In the corresponding edit dialog, edit it as required. Changes to server users, roles, and groups will not take effect on Logi Report Server.
   * To delete a user/role/group, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif).

   **Notes:**

   * A user from Logi Report Server cannot be reassigned to (or removed from) a role from the server. Similarly, a role from the server cannot be re-assigned to (or removed from) a user from the server. So, if both users and roles are obtained from the server, you will not be able to change their parental relationships.
   * You cannot assign a role from the server to a local user created on Logi Report Designer, while a user from the server can be assigned to a local role.
   * During importing, if any existing users, roles or groups that came from the server have the same names as those on the server, their properties will be refreshed with new information from the server, for example, role, or group information and parental relationships. However, their permission settings will be reserved. Specially, if a user from the server has been assigned to any roles defined in Designer, then these roles will be reserved in its member list.
4. Select one or more users/roles/groups in the principal box. If you want to select all users, roles or groups at a time, select ![Drop-down Menu button](https://devnet.logianalytics.com/hc/article_attachments/4404904353815/btn_drpdwn.gif) and then select the corresponding item from the drop-down menu.
5. In the Resources box, select one or more view elements. You can select ![Drop-down Menu button](https://devnet.logianalytics.com/hc/article_attachments/4404904353815/btn_drpdwn.gif) and select an item from the drop-down menu to select all the detail objects, group objects, aggregation objects, or categories in business views of the current catalog data source at a time.
6. In the Security Options box, clear the **Use Default** option so as to customize the data security and resource security for the selected view elements. If you want to use the default security settings of the selected elements, make the option selected.

   When only one principal and one view element is selected, after you finish defining the data security and resource security, you can save the current security settings as the element's default security settings by selecting the **Set as Default** button.
7. In the Data Security box, specify whether the selected principals can access values of the selected view elements.
8. In the Resource Security box, specify whether you want the selected view elements to be visible to the principals.
9. If only a group object is selected in step 4, you can further specify which members of the group object are allowed and which are denied for the principals in the Data Security box (for more information, see [Permission Logic on Group Objects](#Logic)).
   1. Select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404911588375/btn_edit.gif) above the Allowed Set or Denied Set box. The [Edit Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009630921-Edit-Values-Dialog) dialog appears.

      ![Edit Values dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904344727/edtvlu.gif)
   2. Choose a way of specifying the members: select members from the available list, or compose an expression to retrieve members. Only one can be used.
      * To select members, first select the **Selected Values** radio button.

        If you would like all the possible members of the group object to be selected, select **<All>**.

        If you just want to select some of the members, leave <All> unselected. Add them one by one by selecting one and then selecting ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif).
      * To compose an expression, select the **Expression** radio button, then select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904178967/btn_chsr.gif). The [Edit Conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009607862-Edit-Conditions-Dialog#FieldValue) dialog appears.

        ![Edit Conditions dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904352151/edtcndtn2.gif)

        Select the **Add Condition** button to add a condition line. Choose the operator with which to compose the condition expression from the operator drop-down list. From the value drop-down list, specify the value of how to build the condition. You can also type in the value manually. Select **Add Condition** to add more condition lines and define the relationship between the condition lines.

        To make some conditions grouped, select them and select the **Group** button, then the selected conditions will be added in one group and work as one line of filter expression. Conditions and groups together can be further grouped. To take any condition or group in a group out, select it and select **Ungroup.**

        To adjust the priority of the conditions, select it and select the **Up** or **Down** button.

        To delete a condition line, select it and select the **Delete** button.
   3. Select **OK** to save the values.
   4. If users are selected, check whether the unspecified members of the group object are available to the users.

   See [Permission Logic on Group Objects](#Logic) for details about the permission logic between allowed set, denied set and unspecified members.
10. Repeat steps 3 to 8 to customize other principals' permissions on the view elements.
11. When finished, select **OK** in the dialog.
12. Save the catalog.

    When you save the catalog, the permission settings are also saved and they are saved in an authorization file in the same folder as the catalog file. The catalog and authorization files have the same file name but different extensions, for example, if the catalog file is test.cat, the authorization file will be named test.auth. The authorization file is loaded by the view authorization manager of its catalog during runtime.

See also [Edit Business View Security](https://devnet.logianalytics.com/hc/en-us/articles/1500009607842-Edit-Business-View-Security-Dialog) dialog for addition information about options in the dialogs.

**Note:** When a catalog with business view security is published to Logi Report Server, only the principals on the server which match the principals defined in the business view security will maintain the business view security setting. When a principal is deleted from the server security system, the related business view security setting in all catalogs will be removed.

### Permission Logic on Group Objects

The relationship between a principal (user, role or group) and the members of a group object in a business view are classified into three sets:

* **Allowed Set**  
   The members of a group object that a principal is allowed to access, which are directly specified to the principal, excluding those inherited from the parent roles or groups.
* **Denied Set**  
   The members of a group object that a principal is not allowed to access, which are directly specified to the principal, excluding those inherited from the parent roles or groups.
* **Unspecified Members**   
   The members of a group object that are specified neither in a user's allowed/denied set nor in the inherited allowed/denied set from the user's parent roles/groups. Report designer can determine whether a user can access the unspecified members.

A principal can have its own allowed/denied set and inherit the allowed/denied sets from its parent roles or groups. The parent allowed/denied sets will be calculated first and it is a recursive process.

The following are the detailed working logic:

* If for a principal a member exists in both the allowed set and denied set, the denied set has higher priority than the allowed set. In this case the member is not available to the principal.
* The directly defined permission on a principal always overwrites the permission inherited from its parents. That is, for a member of a group object, if its permission has not been defined on a given user/role/group, the permission will inherit from the parents of the user/role/group; if it is defined, the permission will be used directly.
* Inheritance rule:
  + If a member is denied by any parent, it will be denied, or else if a member is allowed by any parent, it will be allowed.
  + If a member is neither denied nor allowed by any parent, the permission is regarded as unspecified.
* After inheritance rule is applied to a specific user, if some members are still unspecified, the status of the members will depend on the option setting whether to make them allowed or denied.

Here is the priority order:

Denied Set > Allowed Set > Inherited Denied Set > Inherited Allowed Set > Unspecified (no matter whether it is allowed or denied).

See the diagram below:

![Priority diagram](https://devnet.logianalytics.com/hc/article_attachments/4404916840471/scrty_bv_logic.gif)

The final result of the members of a group object that a principal is allowed to access will be:

({Allowed Set} - {Denied Set}) U   
 (({Inherited Allowed Set from parent 1} U {Inherited Allowed Set from parent 2} U ...) - ({Inherited Denied Set from parent 1} U {Inherited Denied Set from parent 2} U ...)) U   
 {Unspecified if allowed}

The final set of the unspecified will be:

{All} - ({Allowed Set} U {Denied Set} U {Inherited Allowed Set from parent 1} U {Inherited Denied Set from parent 1} U {Inherited Allowed Set from parent 2} U ...)

For a user, the security in a business view would be like this:

{Accessible members of group1} And {Accessible members of group2} And...

**Note:** If all members are denied in a group object regardless of whether it is set to a principal directly or to the parents indirectly, no data will be retrieved from the group object to the principal.

We will take some examples to further demonstrate the relationship between a principal and the group object members.

**Example 1**

Here we use a simple sample to describe a case when a user belongs to multiple roles.

Assume there is a group object Order ID={1,2,3,4,5,6,7,8,9}, and we set business view security on this group object for a user (user1) and two roles (role1, role2) separately.

|  | Belong To | Allowed Set | Denied Set |
| --- | --- | --- | --- |
| user1 | role1, role2 | 1 |  |
| role1 |  | 2,3 | 4,5 |
| role2 |  | 3,4,5 | 1,2 |

The unspecified members will be {1,2,3,4,5,6,7,8,9} - ({1}U{2,3}U{4,5}U{3,4,5}U{1,2}) = {6,7,8,9}.

Assume we set the property "Allow Unspecified Members" to true, which means the unspecified members {6,7,8,9} are allowed to the user.

The final result that user1 can see when only this business view security is taking effect will be:

{1} U ( ({2,3}U{3,4,5}) - ({4,5}U{1,2}) ) U {6,7,8,9}={1,3,6,7,8,9}

**Example 2**

This example is more complex. It contains four properties of the business view security setting.

Assume there is a summary table with three group objects and a summary.

| Region | Country | City | Summary (the count of Order\_ID) |
| --- | --- | --- | --- |
| APAC |  |  | 41 |
|  | Australia |  | 20 |
|  |  | Sydney | 20 |
|  | China |  | 21 |
|  |  | Beijing | 9 |
|  |  | Hongkong | 4 |
|  |  | Shanghai | 8 |

And in below table, we list the business view security setting in the left cells, and the final results a user will get are listed in the right cells.

| Business View Security Specified As | The Result User Will Get |
| --- | --- |
| | Group | Allowed Set | Denied Set | Allow Unspecified Members | | --- | --- | --- | --- | | Region | <empty> | <empty> | True | | Country | <empty> | {China} | True | | City | <empty> | <empty> | True | | | Region | Country | City | Summary (count Order\_ID) | | --- | --- | --- | --- | | APAC |  |  | 20 | |  | Australia |  | 20 | |  |  | Sydney | 20 | |
| | Group | Allowed Set | Denied Set | Allow Unspecified Members | | --- | --- | --- | --- | | Region | <empty> | <empty> | True | | Country | {China} | <empty> | False | | City | <empty> | {Beijing,Shanghai} | True | | | Region | Country | City | Summary (count Order\_ID) | | --- | --- | --- | --- | | APAC |  |  | 4 | |  | China |  | 4 | |  |  | Hongkong | 4 | |
| | Group | Allowed Set | Denied Set | Allow Unspecified Members | | --- | --- | --- | --- | | Region | <empty> | <empty> | True | | Country | {China} | <empty> | False | | City | <empty> | {Beijing,Shanghai} | False | | | Region | Country | City | Summary (count Order\_ID) | | --- | --- | --- | --- | |  |  |  | 0 | |

## Example of Using Business View Security

This example is based on the business view WorldWideSalesBV in the SampleReports.cat catalog file. It is assumed that the server administrator has already created two users on Logi Report Server: User1 and User2, with the passwords abc and xyz respectively. We will create a security policy on SampleReports.cat to limit the two users' access to different group members of WorldWideSalesBV. Before starting the example, make sure Logi Report Server is started.

The example contains the following tasks:

* [Task 1: Set security on business view groups](#Task1)
* [Task 2: Create a crosstab and publish it to Logi Report Server](#Task2)
* [Task 3: View the crosstab](#Task3)

**Task 1: Set security on business view groups**

In this task, we will import the two server users to Logi Report Designer and limit their access to different members of the Region group in WorldWideSalesBV.

1. Make sure SampleReports.cat is the currently open catalog file. If not select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. In the Catalog Manager, go to the **Data Source 1** > **Security** > **Business View Security** node, right-click and select **Edit Business View Security** from the shortcut menu.
3. In the Edit Business View Security dialog, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) and select **Import from Logi Report Server**.
4. In the Connect to Logi Report Server dialog, specify the required connection information and select **Connect**.

   The principals created on the server will all be imported and listed in the Users/Groups/Roles box.

   ![Import Users](https://devnet.logianalytics.com/hc/article_attachments/4404904471575/scrty_bv_eg_addusr.gif)

Next, we will assign field members availability to User1 and User2. We will make User1 have access on the North America region only and User2 regions other than North America.

1. Select **User1**, in the Resources box select **Region** in WorldWideSalesBV.
2. In the Security Options box, clear **Use Default**.
3. In the Data Security box, allow the Access permission.
4. Select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404911588375/btn_edit.gif) above the Allowed Set box.
5. In the Edit Values dialog, select **North America** from the Available Values box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif) to add it to the Selected Values box, then select **OK** to close the dialog.

   ![Add Value for User1](https://devnet.logianalytics.com/hc/article_attachments/4404904471831/scrty_bv_eg_vlu.gif)
6. In the Edit Business View Security dialog, clear the option **Allow Unspecified Members**, then in the Resource Security box, allow the Visible permission.

   ![Permission of Users](https://devnet.logianalytics.com/hc/article_attachments/4404904472087/scrty_bv_eg_user1.gif)
7. Select **User2** and the same field **Region** in WorldWideSalesBV, then clear **Use Default** in the Security Options box.
8. In the Data Security box, allow the Access permission, then select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404911588375/btn_edit.gif) above the Denied Set box.
9. In the Edit Values dialog, select **North America** from the Available Values box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif), then select **OK**.
10. In the Resource Security box, allow the Visible permission for User2.

    ![Permission of User2](https://devnet.logianalytics.com/hc/article_attachments/4404904472343/scrty_bv_eg_user2.gif)
11. Select **OK** in the Edit Business View Security dialog to save the changes.
12. Close the Catalog Manger.

**Task 2: Create a crosstab and publish it to Logi Report Server**

In this task, we will create a crosstab using WorldWideSalesBV in the SampleReports catalog and then publish it to Logi Report Server.

1. In Logi Report Designer, select **File** > **New** > **Web Report**. A blank web report is created.
2. Select **Insert** > **Crosstab**. The Create Crosstab wizard is displayed.
3. In the Data screen, select **WorldWideSalesBV** under Data Source 1, then select **Next**.
4. In the Display screen, select **Region** as the column field, **Category** as the row field, and **Total Sales** as the summary field. Select **Finish** to create the crosstab.

   ![Create Crosstab](https://devnet.logianalytics.com/hc/article_attachments/4404904472855/scrty_bv_eg_crtcrstb.gif)
5. Select the **View** tab to preview the crosstab. It shows full data.

   ![Preview Crosstab](https://devnet.logianalytics.com/hc/article_attachments/4404916840727/scrty_bv_eg_viewcrstb.gif)
6. Go back to the design mode and select **File** > **Save** to save the crosstab as **mlscrstab.wls**.

Next, we will publish the crosstab to Logi Report Server.

1. Select **File** > **Publish** > **Publish Report to Server**.
2. In the Connect to Logi Report Server dialog, specify the required connection information and select **Connect**.
3. In the Publish to Logi Report Server dialog, unselect the **All** checkbox and then select the **SampleReports.cat** and **mlscrstab.wls** only.
4. Select the **Browse** button next to the Publish Resource To text box, then in the Select Folder dialog, select **Public Reports**  in the Folder box and select **OK**.
5. In the Publish to Logi Report Server dialog, select the **More Options** button, select **mlscrstab.wls** in the resource box, then on the right panel, switch to the **Permissions** tab.

We will grant the two users the necessary permissions on the web report, so that after the report is published to Logi Report Server, they are able to run them.

1. Select the **Enable Setting Permissions** checkbox, select the **User** sub tab, select **User1** in the user box and select the **Visible** and **Execute** checkboxes; select **User2** and do the same.

   ![Publish Resource to Server](https://devnet.logianalytics.com/hc/article_attachments/4404904473111/scrty_bv_eg_pblsh.gif)
2. Select the **OK** button to publish the resources to Logi Report Server.

**Task 3: View the crosstab**

Now, we can log onto Logi Report Server as User1 and User2 separately to view the crosstab.

1. Log onto the Logi Report Server console as User1 with the password abc.
2. Open the Public Reports folder and run the web report mlscrstab.wls. The result will be:

   ![User1 Crosstab Result](https://devnet.logianalytics.com/hc/article_attachments/4404904473367/scrty_bv_eg_rst1.gif)
3. Log out and then log in again as User2 with the password xyz. Run the report and the result will be:

   ![User2 Crosstab Result](https://devnet.logianalytics.com/hc/article_attachments/4404904473623/scrty_bv_eg_rst2.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009605402-Record-Level-and-Column-Level-Security) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009610882-Printing-and-Exporting-Reports)
