---
title: "Changing Resource Properties"
id: 5741438178199
section: "Managing Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741438178199-Changing-Resource-Properties
updated_at: 2022-10-31T17:18:06Z
---

# Changing Resource Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741461739671-Working-with-Custom-Fields)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741474194455-Linking-Resources-and-Catalogs)

# Changing Resource Properties

You can edit the properties of any resources including folders in the server resource tree, such as node name, description, archive policy, and user permissions, in the Resources page of the Server Console. This topic describes how you can edit the properties of one or more resources at a time, and define business view security in a catalog.

This topic contains the following sections:

* [Editing Properties of a Single Resource](#SingleResource)
* [Editing Properties of Multiple Resources at a Time](#MultipleResource)
* [Defining Business View Security in a Catalog](#BVSecurity)

## Editing Properties of a Single Resource

1. Browse to the resource in the server resource tree and then choose a method:
   * Hover over the resource row and select the **Properties** button ![Properties button](https://devnet.logianalytics.com/hc/article_attachments/9905657474071/btn_srv_prpty.gif) on the floating toolbar.
   * Select the resource row, right-click and select **Properties** from the shortcut menu.
   * Select the resource row and select **Tools** > **Properties** on the task bar.

   Server displays the [Properties dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741414587159-Resource-Properties).
2. Change the resource properties in the **General** tab.
3. If the **Permission** tab is available, [specify the permissions](https://devnet.logianalytics.com/hc/en-us/articles/5741463668119-Managing-Permissions) of different principals on the resource.
4. If the **Available Business Views** tab is available, [select the business views](https://devnet.logianalytics.com/hc/en-us/articles/5741448388759-Customizing-Business-Views-for-Reports) for the report to use.
5. If the **Business View Security** tab is available, [define business view security](#BVSecurity) in the catalog.
6. Select **OK** to apply your changes.

## Editing Properties of Multiple Resources at a Time

1. Browse to the folder where the resources are.
2. Select the required resources. To select all the resources, select the top checkbox.
3. Select **Tools** > **Properties** on the task bar, or right-click in any selected resource row and select **Properties** from the shortcut menu. Server displays the [Multiple Type Properties dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741427584151-Multiple-Type-Properties).
4. In the **General** tab, edit the description, status, linked catalog, and version archive policy for the resources. Settings for description and archive policy apply to all the selected resources, while the status setting works on report resources and linked catalog on report, library component, and folder resources only.
5. If the **Permission** tab is available, specify the permissions of different principals on the resources.
6. Select **OK** to accept the changes.

## Defining Business View Security in a Catalog

You can define business view security in a catalog that you can manage if you are an administrator, using the Properties dialog box.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)Only the system admin can see the catalogs in the server resource tree by default. If you are an administrator in an organization and want to see the catalogs, set the **web.page.option.show\_catalog** property to **true** in the **server.properties** file in the `<install_root>\bin` directory.

1. [Access the Properties dialog box of the catalog](#SingleResource).
2. Select the **Business View Security** tab.

   ![Properties dialog - Business View Security tab](https://devnet.logianalytics.com/hc/article_attachments/9905675978903/prptyrpt_bvs.gif)
3. Select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905619223831/btn_add1.gif) above the **Name** box to create a business view security. Server displays the Business View Security Name dialog box.

   ![Business View Security Name dialog box](https://devnet.logianalytics.com/hc/article_attachments/9905676001687/mng_rsc_prpty_bvsnm.gif)
4. Type a name for the business view security.
5. Select **OK**. Server adds the business view security in the Name box.
6. Select **Select** to select business views for the business view security. Server displays the [Select Business Views dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741421631383-Select-Business-Views-Dialog-Box-Properties).

   ![Select Business Views dialog box](https://devnet.logianalytics.com/hc/article_attachments/9905714417815/slctbv.gif)
7. Select the business views you want to add in the business view security.
8. Select **All** if you want to select all the business views in the catalog.
9. Select **OK**. Server displays the number of business views in the business view security.
10. By selecting the arrow icon ![Expand button](https://devnet.logianalytics.com/hc/article_attachments/9905618988823/btn_mvdown1.gif) you can expand and view the business views.
11. To enable some users, roles, or groups in the server security system to access the business views in the business view security, select **User**, **Role**, or **Group**.
12. Server displays in the Available box the users, roles, or groups in the server security system that you can manage.
13. Select an item in the Available box.
14. Select the **Add** button ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/9905636390807/btn_add.gif) to add the item to the Selected box.
15. Repeat step 13 and 14 to add more items. The items you added in the Selected box will be able to access the business views in the business view security.
16. You can define more business view security following the preceding procedure.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)The business view security you define here on Server has higher priority than that you define in the catalog using Logi Report Designer.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741461739671-Working-with-Custom-Fields)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741474194455-Linking-Resources-and-Catalogs)
