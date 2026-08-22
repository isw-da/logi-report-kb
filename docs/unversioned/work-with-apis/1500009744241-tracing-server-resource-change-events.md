---
title: "Tracing Server Resource Change Events"
id: 1500009744241
section: "Work With APIs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009744241-Tracing-Server-Resource-Change-Events
updated_at: 2021-07-25T07:20:24Z
---

# Tracing Server Resource Change Events

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718582-Specifying-Report-Running-Properties-in-the-Session)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718402-Auditing-on-Exporting-Printing-and-Saving-of-Reports)

# Tracing Server Resource Change Events

Using the Server API, you can trace the change of server resources caused by the following actions: Create, Open, Save, Delete, Change Permission, Change Property, and Copy. To do this, you need to implement the listener interface **ResourceNotifyTrigger** and then add the implemented class to RptServer by calling *RptServer.getResourceActionNotifier().addNotifyTrigger(ResourceNotifyTrigger trigger)* in order to get action notification.

The following shows a resource action trigger. You need to also implement the interface. When a resource action happens, the *beforeAction()* and *afterAction()* methods are called.

```
public interface ResourceNotifyTrigger {  
    public void beforeAction(ResourceNotifyInfo info)  
    public void afterAction(ResourceNotifyInfo info);
```

Logi Report Server sends the resource information right before and after the change defined in the **ResourceNotifyInfo** object happens:

```
public interface ResourceNotifyInfo {  
    public boolean isNode();  
        public PathInfo getResourceInfo();  
        public String getResourcePath();  
        public SERVER_ACTION_TYPE getActionType();  
        public SERVER_ACTION_SOURCE getActionSource();  
        public RptServer getServer();  
        public JUser getUserInfo();  
        public HttpSession getHttpSession();  
    }
```

The list below details how to specify the action type and action source:

* You can specify the types of server actions performed on the resources as follows:

  `public static enum SERVER_ACTION_TYPE { Create, Open, Save, Delete, ChangePermission, ChangeProperty, Copy }`
* You can specify the types of server action sources indicating where the actions are sent as follows:

  `public static enum SERVER_ACTION_SOURCE { Designer, ServerConsole, ServerAdmin, API_RMI, API_Local, API_URL, Studio_Page, Studio_Web, Dashboard, VisualAnalysis }`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718582-Specifying-Report-Running-Properties-in-the-Session)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718402-Auditing-on-Exporting-Printing-and-Saving-of-Reports)
