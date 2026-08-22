---
title: "Tracing Server Resource Change Events"
id: 1500009668481
section: "Working With APIs Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009668481-Tracing-Server-Resource-Change-Events
updated_at: 2021-07-24T20:55:30Z
---

# Tracing Server Resource Change Events

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009668821-Specifying-Report-Running-Properties-in-the-Session)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009643802-Configuring-the-Security-Cache-System)

# Tracing Server Resource Change Events

The change of server resources such as folders, reports, dashboards, analysis, and catalogs can be tracked. The change actions include create, open, save, delete, change permission, change property, and copy.

To use the feature, you need to implement the ResourceNotifyTrigger interface and add the implemented class to RptServer to get action notification.

Below is a list of the sections covered in this topic:

* [Implementing the Listener Interface ResourceNotifyTrigger](#Implement)
* [Adding Trigger to RptServer](#Add)

## Implementing the Listener Interface ResourceNotifyTrigger

|  |
| --- |
| ``` public interface ResourceNotifyTrigger {         public void beforeAction(ResourceNotifyInfo info);         public void afterAction(ResourceNotifyInfo info); ``` |

It is a resource action trigger to a user. Users need to implement the interface. When a resource action happens, the beforeAction() and afterAction() methods are called. Logi JReport Server sends the resource information right before and after the change happens in the ResourceNotifyInfo object:

|  |
| --- |
| ``` public interface ResourceNotifyInfo {    public boolean isNode();  public PathInfo getResourceInfo();  public String getResourcePath();  public SERVER_ACTION_TYPE getActionType(); public SERVER_ACTION_SOURCE getActionSource(); public RptServer getServer(); public JUser getUserInfo(); public HttpSession getHttpSession(); } ``` |

**Action type API**

`jet.cs.util.APIConst.java`

`public static enum SERVER_ACTION_TYPE { Create, Open, Save, Delete, ChangePermission, ChangeProperty, Copy }`

The types of server actions performed on the resources.

**Action source API**

`jet.cs.util.APIConst.java`

`public static enum SERVER_ACTION_SOURCE { Designer, ServerConsole, ServerAdmin, API_RMI, API_Local, API_URL, Studio_Page, Studio_Web, Dashboard, VisualAnalysis }`

The types of server action sources indicating from where the actions are sent.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Adding Trigger to RptServer

`RptServer.getResourceActionNotifier().addNotifyTrigger(ResourceNotifyTrigger trigger)`

For detailed usages of the API, see Logi JReport Javadoc in `<install_root>\help\api`.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009668821-Specifying-Report-Running-Properties-in-the-Session)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009643802-Configuring-the-Security-Cache-System)
