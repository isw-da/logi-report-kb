---
title: "Tracing Server Resource Change Events"
id: 1500009686242
section: "Using the Server API"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009686242-Tracing-Server-Resource-Change-Events
updated_at: 2021-11-03T06:58:35Z
---

# Tracing Server Resource Change Events

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009712221-Specifying-Report-Running-Properties-in-the-Session)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009711981-Configuring-the-Security-Cache-System)

# Tracing Server Resource Change Events

Using the Server API, you can trace the change of server resources caused by the following actions: Create, Open, Save, Delete, Change Permission, Change Property and Copy. To do this, you need to implement the listener interface ResourceNotifyTrigger and then add the implemented class to RptServer by calling *RptServer.getResourceActionNotifier().addNotifyTrigger(ResourceNotifyTrigger trigger)* in order to get action notification.

The following shows a resource action trigger. You need to implement the interface. When a resource action happens, the *beforeAction()* and *afterAction()* methods are called.

```
public interface ResourceNotifyTrigger {  

    public void beforeAction(ResourceNotifyInfo info)  

    public void afterAction(ResourceNotifyInfo info);
```

Logi JReport Server sends the resource information right before and after the change defined in the ResourceNotifyInfo object happens:

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

Below shows how to specify the action type and action source:

* The types of server actions performed on the resources can be specified as follows:

  `public static enum SERVER_ACTION_TYPE { Create, Open, Save, Delete, ChangePermission, ChangeProperty, Copy }`
* The types of server action sources indicating where the actions are sent can be specified as follows:

  `public static enum SERVER_ACTION_SOURCE { Designer, ServerConsole, ServerAdmin, API_RMI, API_Local, API_URL, Studio_Page, Studio_Web, Dashboard, VisualAnalysis }`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009712221-Specifying-Report-Running-Properties-in-the-Session)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009711981-Configuring-the-Security-Cache-System)
