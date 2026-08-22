---
title: "Applying the Implementations of the Dashboard Listener API"
id: 5741394931863
section: "Working with APIs Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741394931863-Applying-the-Implementations-of-the-Dashboard-Listener-API
updated_at: 2022-10-31T17:15:48Z
---

# Applying the Implementations of the Dashboard Listener API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741400530711-Advanced-Running-Reports-Using-the-On-Demand-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741408431895-Using-the-NLS-API)

# Applying the Implementations of the Dashboard Listener API

The Dashboard Listener API defines the start and end events of adding and deleting library components. You can get dashboard related information at the event and use the information in your applications. This topic describes the Dashboard Listener API and how you can apply its implementation on the Server Console or via URL.

**Event types**

* The start action of adding a library component
* The end action of adding a library component
* The start action of deleting a library component
* The end action of deleting a library component

**Basic information**

* Catalog information
* Dashboard information
* Library component information

For more information, see the **com.jinfonet.web.modules.dashboard** package in the Logi Report Javadoc. You can also refer to the sample implementation file **DashboardListenerDemo.java** in `<install_root>\help\samples\APIDashboardListener` for additional information.

## Applying the Dashboard Listener API

Different uses should have different implementations of the Dashboard Listener API. Administrators can manage the implementations on the Server Console. After you import a new implementation to the server and enable it, it will be able to take effect immediately without restarting the server.

In addition, after uploading an implementation to Server, you can apply it in the URL for running dashboards. The URL way has higher priority than the enabled implementation on the Server Console.

**To import and enable an implementation in the Server Console:**

1. On the system toolbar of the Server Console, navigate to **Administration** > **Other** > **Dashboard Listeners**. Server displays the Dashboard Listeners page.

   ![Dashboard Listeners page](https://devnet.logianalytics.com/hc/article_attachments/9905831501847/wkapi_srv_use_dshlstnr.gif)
2. Select **New Dashboard Listener**. Server displays the [New Dashboard Listener dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741442672663-New-Dashboard-Listener-Dialog-Box-Properties).
3. Select **Browse** to locate the implementation file which could be a zip or a jar file.
4. Select **Next**.
5. From the **Class Name** list, choose a class name which you defined in the implementation file.

   ![New Dashboard Listener dialog](https://devnet.logianalytics.com/hc/article_attachments/9905736236055/nwdshlsn_rsc.gif)
6. Select the Add button ![](https://devnet.logianalytics.com/hc/article_attachments/9905619223831/btn_add1.gif) beside the **Target** box. Server displays the [Select Target dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741443597975-Select-Target-Dialog-Box-Properties).
7. Specify the target dashboards you would like the implementation to apply to: all dashboards including the unsaved ones, the newly created dashboards that you have not saved, or dashboards in the specified folders.

   ![Select Target dialog](https://devnet.logianalytics.com/hc/article_attachments/9905735525015/slcttgt.gif)
8. Select **OK**. Server lists the specified dashboards or folders in the **Target** box.

   When you have added all dashboards, Server disables the ![](https://devnet.logianalytics.com/hc/article_attachments/9905619223831/btn_add1.gif) button. Later if you want to change the dashboards, you need to first delete the **<All dashboards>** item, and then add other dashboards. To remove unwanted dashboards from the Target box, select them and then select the Remove button ![](https://devnet.logianalytics.com/hc/article_attachments/9905616261527/btn_dltobj.gif) .
9. In the **Description** text box, you can type a description for the implementation.
10. Select **Enabled** to enable the implementation.
11. Select **Finish**. The registered class will take effect right away.

Server adds the registered implementation class in the class table on the Dashboard Listener page which consists of the following columns.

| Column Name | Description |
| --- | --- |
| Class Name | The implementation class name. Each is unique and cannot be null. |
| Target | The dashboards or folders that the implementation will take effect on. When a dashboard is the target value of different implementations, the earliest implementation will take effect on the dashboard. |
| Description | The description of the implementation. |
| Enabled | Server shows whether you have enabled the implementation. |

In the class table, the system admin can perform the following actions on the implementations:

* To sort the table by certain column, select the column name.
* To modify the target value of an implementation, select it, then select **Properties** on the toolbar or right-click and then select **Properties** from the shortcut menu. Server displays a dialog box, and you can [modify the target dashboards](#Target).
* To enable implementations that are not enabled, select them, then select **Enable** on the toolbar or right-click and then select **Enable** from the shortcut menu.
* To disable implementations that are enabled, select them, then select **Disable** on the toolbar or right-click and then select **Disable** from the shortcut menu.
* To delete implementations, select them, then select **Delete** on the toolbar or right-click and then select **Delete** from the shortcut menu.

**To apply an implementation via URL:**

To apply the dashboard listener via URL, append the key-value pair **jrd\_dsh\_listener=PackageName.ClassName** in the URL for running dashboards.

For example, if you want your implemented class **TestListener** to take effect on a newly created dashboard (not the target you defined on the Server Console), you can define it in the URL. Such URL will not affect the setting on the Server Console.

`http://localhost:8888/dashboard/app/entry/run.jsp?jrs.authorization=YWRtaW46YWRtaW4%3D&jrd_dsh_listener=com.jinfonet.TestListener&jrd_resext={"active":0,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard 1.dsh","ver":-1}]}`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741400530711-Advanced-Running-Reports-Using-the-On-Demand-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741408431895-Using-the-NLS-API)
