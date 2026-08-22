---
title: "Applying the Implementations of the Dashboard Listener API"
id: 1500009771021
section: "Using the Server API"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009771021-Applying-the-Implementations-of-the-Dashboard-Listener-API
updated_at: 2021-07-24T00:49:37Z
---

# Applying the Implementations of the Dashboard Listener API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009771161-Advanced-Running-Reports-Using-the-On-Demand-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009743222-Using-the-NLS-API)

# Applying the Implementations of the Dashboard Listener API

The Dashboard Listener API defines the start and end events of adding and deleting library components. You can get dashboard related information at the event and use the information in your applications. This topic describes the Dashboard Listener API and how you can apply its implementation in the Server Console or via URL.

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

Different uses should have different implementations of the Dashboard Listener API. Administrators can manage the implementations on the Logi Report Server Console. After you import a new implementation to the server and enable it, it will be able to take effect immediately without restarting the server.

In addition, after uploading an implementation to Logi Report Server, you can apply it in the URL for running dashboards. The URL way has higher priority than the enabled implementation in the Server Console.

**To import and enable an implementation in the Logi Report Server Console:**

1. In the Server Console, point to **Administration** on the system toolbar, select **Other** > **Dashboard Listeners** from the drop-down menu. Server displays the Dashboard Listeners page.

   ![Dashboard Listeners page](https://devnet.logianalytics.com/hc/article_attachments/4404880579991/wkapi_srv_use_dshlstnr.gif)
2. Select **New Dashboard Listener**. Server displays the [New Dashboard Listener](https://devnet.logianalytics.com/hc/en-us/articles/1500009774081-New-Dashboard-Listener-Dialog-Box-Properties) dialog box.
3. Select **Browse** to locate the implementation file which could be a zip or a jar file. Then select **Next**.
4. From the **Class Name** drop-down list, choose a class name which is defined in the implementation file.

   ![New Dashboard Listener dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885512343/nwdshlsn_rsc.gif)
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404880163351/btn_add1.gif) beside the **Target** box. Server displays the [Select Target](https://devnet.logianalytics.com/hc/en-us/articles/1500009746462-Select-Target-Dialog-Box-Properties) dialog box.
6. Specify the target dashboards you would like the implementation to apply to: all dashboards including the unsaved ones, the newly created dashboards that have not been saved, or dashboards in the specified folders.

   ![Select Target dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880412823/slcttgt.gif)
7. Select **OK**. Report Server lists the specified dashboards in the **Target** box.

   When you have added all dashboards, Report Server disables the ![](https://devnet.logianalytics.com/hc/article_attachments/4404880163351/btn_add1.gif) button. Later if you want to change the dashboards, you need to first delete the **<All dashboards>** item and then add other dashboards. To remove unwanted dashboards from the Target box, select them and then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404885308823/btn_dltobj.gif) .
8. In the **Description** text box, you can type a description for the implementation.
9. Select **Enabled** to enable the implementation.
10. Select **Finish** and the registered class will take effect right away.

Report Server adds the registered implementation class in the class table on the Dashboard Listener page which consists of the following columns.

| Column Name | Description |
| --- | --- |
| Class Name | The implementation class name. Each is unique and cannot be null. |
| Target | Shows the resources that the implementation will take effect on. When a dashboard has been set as the target value of different implementations, the earliest implementation will take effect on the dashboard. |
| Description | The description of the implementation. |
| Enabled | Shows whether the implementation is enabled. |

In the class table, the system admin can perform the following on the implementations:

* To sort the table by certain column, select on the column name.
* To modify the target value of an implementation, select it, then select **Properties** on the toolbar or right-click and then select **Properties** from the shortcut menu. Then in the displayed dialog box, you can [modify the target dashboards](#Target).
* To enable implementations that are not enabled, select them, then select **Enable** on the toolbar or right-click and then select **Enable** from the shortcut menu.
* To disable implementations that are enabled, select them, then select **Disable** on the toolbar or right-click and then select **Disable** from the shortcut menu.
* To delete implementations, select them, then select **Delete** on the toolbar or right-click and then select **Delete** from the shortcut menu.

**To apply an implementation via URL:**

To apply the dashboard listener via URL, append the key-value pair **jrd\_dsh\_listener=PackageName.ClassName** in the URL for running dashboards.

For example, if you want your implemented class **TestListener** to take effect on a newly created dashboard (not the target defined in the Server Console), you can define it in the URL. Such URL will not affect the setting in the Server Console.

`http://localhost:8888/dashboard/app/entry/run.jsp?jrs.authorization=YWRtaW46YWRtaW4%3D&jrd_dsh_listener=com.jinfonet.TestListener&jrd_resext={"active":0,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard 1.dsh","ver":-1}]}`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009771161-Advanced-Running-Reports-Using-the-On-Demand-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009743222-Using-the-NLS-API)
