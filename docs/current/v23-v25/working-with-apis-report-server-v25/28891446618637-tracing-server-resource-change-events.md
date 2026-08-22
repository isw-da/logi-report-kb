---
title: "Tracing Server Resource Change Events"
id: 28891446618637
section: "Working with APIs Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891446618637-Tracing-Server-Resource-Change-Events
updated_at: 2026-02-26T02:11:04Z
source_host: docs-report.zendesk.com
---
# 
Tracing Server Resource Change Events 

You can trace the change of server resources using the Server API when following actions happen on the server resources: Create, Open, Save, Delete, Change Permission, Change Property, and Copy. This topic describes how you can implement the listener interface ResourceNotifyTrigger and add the trigger to RptServer to get action notification.

This topic contains the following sections:

- Implementing the listener interface ResourceNotifyTrigger

- Adding trigger to RptServer

## 
Implementing the listener interface ResourceNotifyTrigger

You can implement a resource action trigger as follows. When a resource action happens, Server calls the beforeAction() and afterAction() methods.

public interface ResourceNotifyTrigger {
    public void beforeAction(ResourceNotifyInfo info)
    public void afterAction(ResourceNotifyInfo info);
Report Server sends the resource information right before and after the change defined in the ResourceNotifyInfo object happens:

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
You can specify the action type and action source as follows:

- Specify the types of server actions performed on the resources:
                public static enum SERVER_ACTION_TYPE { Create, Open, Save, Delete, ChangePermission, ChangeProperty, Copy	}

- Specify the types of server action sources indicating where the actions are sent:
                public static enum SERVER_ACTION_SOURCE { Designer, ServerConsole, ServerAdmin, API_RMI, API_Local, API_URL, Studio_Page, Studio_Web, Dashboard, VisualAnalysis }

## 
Adding trigger to RptServer

You can add the implemented trigger to RptServer as follows:

RptServer.getResourceActionNotifier().addNotifyTrigger(ResourceNotifyTrigger trigger)
