---
title: "Applying the Implementations of the Dashboard Listener API"
id: 1500009712001
section: "Using the Server API"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009712001-Applying-the-Implementations-of-the-Dashboard-Listener-API
updated_at: 2021-11-03T06:58:34Z
---

# Applying the Implementations of the Dashboard Listener API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009712101-Advanced-Running-Reports-Using-the-On-Demand-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009686382-Using-NLS-API)

# Applying the Implementations of the Dashboard Listener API

Dashboard Listener API defines the start and end events of adding and deleting library components for users to get dashboard related information at the event and to use the information in their own application.

**Event types**

* The start action of adding a library component
* The end action of adding a library component
* The start action of deleting a library component
* The end action of deleting a library component

**Basic information**

* Catalog information
* Dashboard information
* Library component information

For detailed usages about the Dashboard Listener API, refer to the com.jinfonet.web.modules.dashboard package in the Logi JReport Javadoc. You can also refer to the sample implementation file DashboardListenerDemo.java in `<install_root>\help\samples\APIDashboardListener`for additional information.

## Applying the Dashboard Listener API

Different uses should have different implementations of the Dashboard Listener API. The implementations can be managed on the Logi JReport Server console by administrators. After a new implementation is imported to the server and enabled, it will be able to take effect immediately without restarting the server.

In addition, after an implementation is uploaded to Logi JReport Server, you can apply it in the URL which is used for running dashboards. The URL way has higher priority than the enabled implementation in the server console.

**To import and enable an implementation in the Logi JReport Server console:**

1. In the Logi JReport Server console, point to **Administration** on the system toolbar, select **Other** > **Dashboard Listeners** from the drop-down menu. The Dashboard Listeners page is displayed.

   ![Dashboard Listeners page](https://devnet.logianalytics.com/hc/article_attachments/4412131513367/wkapi_srv_use_dshlstnr.gif)
2. Select **New Dashboard Listener**.
3. In the [New Dashboard Listener](https://devnet.logianalytics.com/hc/en-us/articles/1500009714741-New-Dashboard-Listener) dialog, select the **Browse** button to locate the implementation file which could be a zip or a jar file. Then select **Next**.
4. From the Class Name drop-down list, choose a class name which is defined in the implementation file.

   ![New Dashboard Listener dialog](https://devnet.logianalytics.com/hc/article_attachments/4412131468183/nwdshlsn_rsc.gif)
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4412131380631/btn_add1.gif) beside the Target box, then in the [Select Target](https://devnet.logianalytics.com/hc/en-us/articles/1500009689122-Select-Target) dialog specify the target dashboards you would like the implementation to apply to: all dashboard including the unsaved ones, the newly created dashboards that have not been saved, or dashboards in the specified folders.

   ![Select Target dialog](https://devnet.logianalytics.com/hc/article_attachments/4412131459351/slcttgt.gif)
6. Select **OK** and the specified dashboards will be listed in the Target box.

   When all dashboards have been added, the ![](https://devnet.logianalytics.com/hc/article_attachments/4412131380631/btn_add1.gif) button will be disabled. Later if you want to change the dashboards, you need to first delete the **<All dashboards>** item and then add other dashboards. To remove unwanted dashboards from the Target box, select them and then select ![](https://devnet.logianalytics.com/hc/article_attachments/4412112483991/btn_dltobj.gif) .
7. In the Description text box, enter a description for the implementation if necessary.
8. Select the **Enabled** checkbox to make the implementation enabled.
9. Select **Finish** and the registered class will take effect right away.

The registered implementation class is added in the class table on the Dashboard Listener page which consists of the following columns.

| Column Name | Description |
| --- | --- |
| Class Name | The implementation class name. Each is unique and cannot be null. |
| Target | Shows the resources that the implementation will take effect on. When a dashboard has been set as the target value of different implementations, the earliest implementation will take effect on the dashboard. |
| Description | The description of the implementation. |
| Enabled | Shows whether the implementation is enabled. |

In the class table, the system admin can perform the following on the implementations:

* To sort the table by certain column, select on the column name.
* To modify the target value of an implementation, select it, then select **Properties** on the toolbar or right-click and then select **Properties** from the shortcut menu. Then in the displayed dialog, [modify the target dashboards](#Target) as required.
* To enable implementations that are not enabled, select them, then select **Enable** on the toolbar or right-click and then select **Enable** from the shortcut menu.
* To disable implementations that are enabled, select them, then select **Disable** on the toolbar or right-click and then select **Disable** from the shortcut menu.
* To delete implementations, select them, then select **Delete** on the toolbar or right-click and then select **Delete** from the shortcut menu.

**To apply an implementation via URL:**

To apply the dashboard listener via URL, append the key-value pair jrd\_dsh\_listener=PackageName.ClassName in the URL which is used for running dashboards.

For example, if you want your implemented class TestListener to take effect on a new created dashboard (not the target defined in the server console), you can define it in the URL. Such URL will not affect the setting in the server console.

`http://localhost:8888/dashboard/app/entry/run.jsp?jrs.authorization=YWRtaW46YWRtaW4%3D&jrd_dsh_listener=com.jinfonet.TestListener&jrd_resext={"active":0,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard 1.dsh","ver":-1}]}`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009712101-Advanced-Running-Reports-Using-the-On-Demand-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009686382-Using-NLS-API)
