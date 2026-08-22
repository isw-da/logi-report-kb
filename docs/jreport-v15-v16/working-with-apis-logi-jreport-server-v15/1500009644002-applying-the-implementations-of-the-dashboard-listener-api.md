---
title: "Applying the Implementations of the Dashboard Listener API"
id: 1500009644002
section: "Working With APIs Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009644002-Applying-the-Implementations-of-the-Dashboard-Listener-API
updated_at: 2021-07-24T20:55:29Z
---

# Applying the Implementations of the Dashboard Listener API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009668721-Specifying-Paths-for-the-Result-Files-When-Using-On-Demand-API)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644082-Using-NLS-API)

# Applying the Implementations of the Dashboard Listener API

Dashboard Listener API defines the start and end events of adding and deleting library components for users to get dashboard related information at the event and to use the information in their own application.

**Event types**

* The start action of adding a library component
* The end action of adding a library component
* The start action of deleting a library component
* The end action of deleting a library component

**Basic Information**

* Catalog information
* Dashboard information
* Library component information

For detailed usages about the Dashboard Listener API, see Logi JReport Javadoc com.jinfonet.web.modules.dashboard package in `<install_root>\help\api`. Also, there is a sample implementation file DashboardListenerDemo.java in `<install_root>\help\samples\APIDashboardListener`.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Applying the Dashboard Listener API

Different uses should have different implementations of the Dashboard Listener API. The implementations can be managed on the server by administrators. After a new implementation is imported to the server and enabled, it will be able to take effect immediately without restarting the server.

Besides, after an implementation is uploaded to the server, you can apply it in the URL which is used for running dashboards. The URL way has higher priority than the enabled implementation on the Logi JReport Administration page.

**To import and enable an implementation on the Logi JReport Administration page:**

1. On the Logi JReport Administration page, select **Configuration** on the system toolbar and select **Dashboard Listeners** from the drop-down menu. The Configuration - Dashboard Listeners page is displayed.

   ![Dashboard Listeners page](https://devnet.logianalytics.com/hc/article_attachments/4404920661143/wkapi_srv_use_dshlstnr.gif)
2. Select **New Dashboard Listener**.
3. In the [New Dashboard Listener](https://devnet.logianalytics.com/hc/en-us/articles/1500009646582-New-Dashboard-Listener) dialog, select the **Browse** button to locate the implementation file which could be a zip or a jar file. Then select **Next**.
4. From the Class Name drop-down list, choose a class name which is defined in the implementation file.

   ![New Dashboard Listener dialog](https://devnet.logianalytics.com/hc/article_attachments/4404920570263/nwdshlsn_rsc.gif)
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385047/btn_add1.gif) beside the Target box, then in the [Select Target](https://devnet.logianalytics.com/hc/en-us/articles/1500009671261-Select-Target) dialog specify the target dashboards you would like the implementation to apply to: all dashboard including the unsaved ones, the newly created dashboards that have not been saved, or dashboards in the specified folders.

   ![Select Target dialog](https://devnet.logianalytics.com/hc/article_attachments/4404920558487/slcttgt.gif)
6. Select **OK** and the specified dashboards will be listed in the Target box.

   When all dashboards have been added, the ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385047/btn_add1.gif) button will be disabled. Later if you want to change the dashboards, you need to first delete the **<All dashboards>** item and then add other dashboards. To remove unwanted dashboards from the Target box, select them and then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920360855/btn_dltobj.gif) .
7. In the Description text field, enter a description for the implementation if necessary.
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

To apply the dashboard listener via URL, append the key-value pair *jrd\_dsh\_listener=PackageName.ClassName* in the URL which is used for running dashboards.

For example, if you want your implemented class TestListener to take effect on a new created dashboard (not the target defined on the Logi JReport Administration page), you can define it in the URL. Such URL will not affect the setting on the Logi JReport Administration page.

`http://localhost:8888/dashboard/app/entry/run.jsp?jrs.authorization=YWRtaW46YWRtaW4%3D&jrd_dsh_listener=com.jinfonet.TestListener&jrd_resext={"active":0,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard1.dsh","ver":"-1"}]}`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009668721-Specifying-Paths-for-the-Result-Files-When-Using-On-Demand-API)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644082-Using-NLS-API)
