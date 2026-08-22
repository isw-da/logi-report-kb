---
title: "Configuring Business View Security in a Catalog"
id: 1500010094161
section: "Defining Report Security - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010094161-Configuring-Business-View-Security-in-a-Catalog
updated_at: 2021-07-23T19:14:33Z
---

# Configuring Business View Security in a Catalog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094201-Introduction-to-Business-View-Security)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094181-Example-of-Using-Business-View-Security)

# Configuring Business View Security in a Catalog

To define security for the business views in a catalog, take the following steps:

1. [Open the required catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500010056622-Creating-Opening-and-Saving-Catalogs#Open).
2. In the Catalog Manager, do any of the following:
   * Expand the desired data source > **Security** node, right-click **Business View Security** and select **Edit Business View Security** on the shortcut menu. Designer displays the [Edit Business View Security dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096181-Edit-Business-View-Security-Dialog-Box).
   * When [working with a business view in the Business View Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010101061-Creating-Business-Views-in-a-Catalog), select **Menu** > **Tools** > **Security Configuration**. Designer displays the Edit Business View Security dialog box.
   * When [adding or editing a business view element using dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010101061-Creating-Business-Views-in-a-Catalog#Category), switch to the **Security** tab.

   The following is a sample dialog box:

   ![Business View Security dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856978967/edtbvscrty.gif)
3. In the **Users/Groups/Roles** panel, select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) and select **Import from Logi Report Server** from the drop-down menu (before importing, you should make sure Server is started). Designer then adds the users, roles, and groups created on Server in the principal box if Designer can connect to Server and log you in automatically; otherwise, it displays the [Connect to Logi Report Server dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095741-Connect-to-Logi-Report-Server-Dialog-Box) for you to specify the properties for connecting with Server first. The logged-in user should be an administrator user of the started Server so that Designer can perform the importing successfully.

   You can also select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) and select [Add User](https://devnet.logianalytics.com/hc/en-us/articles/1500010095561-Add-User-Dialog-Box), [Add Role](https://devnet.logianalytics.com/hc/en-us/articles/1500010095501-Add-Role-Dialog-Box), or [Add Group](https://devnet.logianalytics.com/hc/en-us/articles/1500010057942-Add-Group-Dialog-Box) from the drop-down menu to add principals manually in Designer or import them [from an XML file](https://devnet.logianalytics.com/hc/en-us/articles/1500010094221-Working-with-RLS-and-CLS-at-Data-Source-Scope#Export), however if you choose to add users, groups, and roles using these two methods, in order to make the business view security take effect on Server, the Server administrator should have created the users, groups, and roles in its security system before you publish the reports involving the business view security to Server.

   You can further edit or remove the principals in the User/Group/Role panel.

   * To edit a user/role/group, select it and select the **Edit** button ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404856829719/btn_edit.gif). In the corresponding edit dialog box, edit it as required. Changes to Server users, roles, and groups made in Designer cannot take effect on Server.
   * To delete a user/role/group, select it and select the **Remove** button ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif).

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

   * You cannot assign a user from Server to (or remove it from) a role from Server; similarly, you cannot re-assign a role from Server to (or remove it from) a user from Server. Therefore, if you obtain both users and roles from Server, you are not able to change their parental relationships.
   * You cannot assign a role from Server to a local user created in Designer, while you can grant a user from Server a local role.
   * During importing, if any existing users, roles, or groups that came from Server have the same names as those in Server, Designer refreshes their properties with new information from Server, for example, the role or group information and parental relationships; however, Designer reserves their permission settings. Specially, if you have assigned a user from Server to any roles defined in Designer, Designer reserves these roles in its member list.
4. Select one or more users/roles/groups in the principal box. If you want to select all users, roles, or groups at a time, select the **down** button ![Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856922775/btn_down.gif) and then select the corresponding item from the drop-down menu.
5. In the **Resources** box, select one or more view elements. You can select ![Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856922775/btn_down.gif) and select an item from the drop-down menu to select all the detail objects, group objects, aggregation objects, or categories in business views of the current catalog data source at a time.
6. In the **Security Options** box, clear the **Use Default** checkbox so as to customize the data security and resource security for the selected view elements. If you want to use the default security settings of the selected elements, make the checkbox selected.

   If you only select one principal and one view element to define the security, after you finish defining the data security and resource security, you can save the current security settings as the element's default security settings by selecting the **Set as Default** button.
7. In the **Data Security** box, specify whether the selected principals can access values of the selected view elements.
8. In the **Resource Security** box, specify whether you want the selected view elements to be visible to the principals.
9. If you select only a group object in step 4, you can further specify to allow or deny specific members of the group object for the principals in the Data Security box.
   1. Select the **Pencil** button ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404856829719/btn_edit.gif) above the **Allowed Set** or **Denied Set** box. Designer displays the [Edit Values dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096481-Edit-Values-Dialog-Box).

      ![Edit Values dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856973847/edtvlu.gif)
   2. Choose a method of specifying the members: select members from the available list, or compose an expression to retrieve members. You can use only one method.
      * To select members, first select the **Selected Values** radio button.

        If you would like to select all the possible members of the group object, select **<All>**.

        If you just want to select some of the members, leave <All> unselected. Add the members one by one by selecting one and then selecting the **Right Arrow** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif).
      * To compose an expression, select the **Expression** radio button, then select the **ellipsis** button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404848397591/btn_ellipsis.gif). Designer displays the [Edit Conditions dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058702-Edit-Conditions-Dialog-Box#FieldValue).

        ![Edit Conditions dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848587031/edtcndtn2.gif)

        Select the **Add Condition** button to add a condition line. Choose the operator with which to compose the condition expression from the operator drop-down list. From the value drop-down list, specify the value of how to build the condition. You can also type in the value manually. Repeat this to add more condition lines and define the logic relationship between the condition lines: "And", "Or", "And Not", or "Or Not".

        To group some condition lines, select them and select the **Group** button, Designer then adds the selected condition lines in one group and applies them as one line of filter expression (you can also group conditions and groups together); to take out any condition or group from a group, select it and select **Ungroup**; to adjust the priority of the condition lines, select it and select the **Up** or **Down** button; to delete a condition line, select it and select the **Delete** button.
   3. Select **OK** in the Edit Values dialog box to apply the specified values.
   4. If you select users, specify whether the unspecified members of the group object are available to the users.

   See [Permission Logic on Group Objects](https://devnet.logianalytics.com/hc/en-us/articles/1500010094201-Introduction-to-Business-View-Security#Logic) for more information about the permission logic between allowed set, denied set, and unspecified members.
10. Repeat steps 3 to 9 to customize other principals' permissions on the view elements.
11. Select **OK** in the dialog box.
12. Save the catalog.

    When you save the catalog, Designer saves the permission settings at the same time in an authorization file in the same folder as the catalog file. The catalog and authorization files have the same file name but different extensions, for example, if the catalog file is test.cat, the authorization file is test.auth.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) After you [publish a catalog with business view security to Server](https://devnet.logianalytics.com/hc/en-us/articles/1500010062722-Publishing-and-Downloading-Resources#Remotely), only the principals on Server which match the principals defined in the business view security can keep the security settings. If the administrator deletes a principal from the security system of Server, Server removes the related business view security settings from all catalogs.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094201-Introduction-to-Business-View-Security)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094181-Example-of-Using-Business-View-Security)
