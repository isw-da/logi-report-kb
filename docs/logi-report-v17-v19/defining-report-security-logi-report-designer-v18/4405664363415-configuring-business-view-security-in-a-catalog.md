---
title: "Configuring Business View Security in a Catalog"
id: 4405664363415
section: "Defining Report Security - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664363415-Configuring-Business-View-Security-in-a-Catalog
updated_at: 2022-01-27T20:34:20Z
---

# Configuring Business View Security in a Catalog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664364311-Introduction-to-Business-View-Security)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661338135-Example-of-Using-Business-View-Security)

# Configuring Business View Security in a Catalog

To define security for the business views in a catalog, take the following steps:

1. [Open the required catalog](https://devnet.logianalytics.com/hc/en-us/articles/4405661330711-Creating-Opening-and-Saving-Catalogs#Open).
2. In the Catalog Manager, do any of the following:
   * Expand the data source > **Security** node, right-click **Business View Security** and select **Edit Business View Security** on the shortcut menu. Designer displays the [Edit Business View Security dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661506455-Edit-Business-View-Security-Dialog-Box).
   * When [working with a business view in the Business View Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664681111-Creating-Business-Views-in-a-Catalog), navigate to **Menu** > **Tools** > **Security Configuration**. Designer displays the Edit Business View Security dialog box.
   * When [adding or editing a business view element using dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664681111-Creating-Business-Views-in-a-Catalog#Category), switch to the **Security** tab.

   The following shows a sample dialog box.

   ![Business View Security dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420542227607/edtbvscrty.gif)
3. In the **Users/Groups/Roles** panel, select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif) and select **Import from Logi Report Server** from the drop-down menu. Designer then adds the users, roles, and groups created on the Server it connects to in the principal box if Designer can set up the connection to a started Server and sign you in automatically; otherwise, it displays the [Connect to Logi Report Server dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661471511-Connect-to-Logi-Report-Server-Dialog-Box) for you to specify the connection and user information first. The user should be an administrator user of the started Server so that Designer can perform the importing successfully.

   You can also select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif) and select [Add User](https://devnet.logianalytics.com/hc/en-us/articles/4405664426647-Add-User-Dialog-Box), [Add Role](https://devnet.logianalytics.com/hc/en-us/articles/4405661452695-Add-Role-Dialog-Box), or [Add Group](https://devnet.logianalytics.com/hc/en-us/articles/4405661449495-Add-Group-Dialog-Box) from the drop-down menu to add principals manually in Designer or import them [from an XML file](https://devnet.logianalytics.com/hc/en-us/articles/4405661342359-Working-with-RLS-and-CLS-at-Data-Source-Scope#Export), however if you choose to add users, groups, and roles using these two methods, in order to make the business view security take effect on Server, the Server administrator should have created the users, groups, and roles in its security system before you publish the reports involving the business view security to Server.

   You can further edit or remove the principals in the User/Group/Role panel.

   * To edit a user/role/group, select it and select **Edit**![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4420556150039/btn_edit.gif). In the corresponding edit dialog box, edit it as required. Changes to Server users, roles, and groups made in Designer cannot take effect on Server.
   * To delete a user/role/group, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420542080407/btn_trashcan.gif).

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg)

   * You cannot assign a user from Server to (or remove it from) a role from Server; similarly, you cannot reassign a role from Server to (or remove it from) a user from Server. Therefore, if you obtain both users and roles from Server, you are not able to change their parental relationships.
   * You cannot assign a role from Server to a local user created in Designer, while you can grant a user from Server a local role.
   * During importing, if any existing users, roles, or groups that came from Server have the same names as those on Server, Designer refreshes them with new information from Server, such as the role or group information and parental relationships; however, Designer reserves their permission settings, specially, if you have assigned a user from Server to any roles defined in Designer, Designer reserves these roles in its member list.
4. Select one or more users/roles/groups in the principal box. If you want to select all users, roles, or groups at a time, select ![Down button](https://devnet.logianalytics.com/hc/article_attachments/4420551011223/btn_down1.gif) and then select the corresponding item from the drop-down menu.
5. In the **Resources** box, select one or more view elements. You can select ![Down button](https://devnet.logianalytics.com/hc/article_attachments/4420551011223/btn_down1.gif) and select an item from the drop-down menu to select all the detail objects, group objects, aggregation objects, or categories in business views of the current catalog data source at a time.
6. In the **Security Options** box, clear **Use Default** to customize the data security and resource security for the selected view elements. If you want to use the default security settings of the selected elements, keep the checkbox selected.

   If you only select one principal and one view element to define the security, after you finish defining the data security and resource security, you can save the current security settings as the element's default security settings by selecting **Set as Default**.
7. In the **Data Security** box, specify whether the selected principals can access values of the selected view elements.
8. In the **Resource Security** box, specify whether you want the selected view elements to be visible to the principals.
9. If you select only a group object in step 4, you can further specify to allow or deny specific members of the group object for the principals in the Data Security box.
   1. Select **Edit**![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4420556150039/btn_edit.gif) above the **Allowed Set** or **Denied Set** box. Designer displays the [Edit Values dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664469271-Edit-Values-Dialog-Box).

      ![Edit Values dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420556200343/edtvlu.gif)
   2. Choose a method of specifying the members: select members from the available list, or compose an expression to retrieve the members. You can use only one method.
      * To select members, keep **Selected Values** selected. If you would like to select all the possible members of the group object, select **<All>**; if you just want to select some of the members, leave <All> cleared, then select the members in the **Available Values** box and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550823447/btn_addarrow.gif) to add them to the **Selected Values** box.
      * To compose an expression, select **Expression**, then select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420550827287/btn_ellipsis2.gif). Designer displays the [Edit Conditions dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664456727-Edit-Conditions-Dialog-Box#FieldValue).

        ![Edit Conditions dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420556205335/edtcndtn2.gif)

        Select **Add Condition** to add a condition line. Choose the operator with which to compose the condition expression from the operator drop-down list. From the value drop-down list, specify the value of how to build the condition. You can also type in the value manually. Repeat this to add more condition lines and define the logic relationship between the condition lines: "And", "Or", "And Not", or "Or Not".

        To group some condition lines, select them and select **Group**, Designer then adds the selected condition lines in one group and applies them as one line of filter expression (you can also group conditions and groups together); to take out any condition or group from a group, select it and select **Ungroup**; to adjust the priority of the condition lines, select it and select **Up** or **Down**; to delete a condition line, select it and select **Delete**.
   3. Select **OK** in the Edit Values dialog box to apply the specified values.
   4. If you select users, specify whether the unspecified members of the group object are available to the users.

   See [Permission Logic on Group Objects](https://devnet.logianalytics.com/hc/en-us/articles/4405664364311-Introduction-to-Business-View-Security#Logic) for more information about the permission logic between allowed set, denied set, and unspecified members.
10. Repeat steps 3 to 9 to customize other principals' permissions on the view elements.
11. Select **OK** in the dialog box.
12. Save the catalog.

    When you save the catalog, Designer saves the permission settings at the same time in an authorization file in the same folder as the catalog file. The catalog and authorization files have the same file name but different extensions, for example, if the catalog file is test.cat, the authorization file is test.auth.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) After you [publish a catalog with business view security to Server](https://devnet.logianalytics.com/hc/en-us/articles/4405661923607-Publishing-and-Downloading-Resources#Remotely), only the principals on Server which match the principals defined in the business view security can keep the security settings. If the administrator deletes a principal from the security system of Server, Server removes the related business view security settings from all catalogs.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664364311-Introduction-to-Business-View-Security)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661338135-Example-of-Using-Business-View-Security)
