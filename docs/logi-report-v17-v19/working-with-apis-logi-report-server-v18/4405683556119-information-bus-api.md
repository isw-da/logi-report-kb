---
title: "Information Bus API"
id: 4405683556119
section: "Working with APIs Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683556119-Information-Bus-API
updated_at: 2022-01-27T08:00:00Z
---

# Information Bus API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683554071-Dynamic-Security-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690472343-API-Demos)

# Information Bus API

You can use the Information Bus API to access information container and get or put information in the container. This topic describes the interfaces of the Information Bus API.

* InformationBus
    
   It is used to transmit information in Logi Report Server. It contains three kinds of information containers, global level, organization level, and user level, and you can get or put information in the containers.
* InformationBusManager
    
   It is used to get the Information Bus instance from the Information Bus Manager.
* InformationContainer
    
   It is used to store user information of the following types:
  + LONG\_TIME - The information exists in the container until it is removed or the container it belongs to is removed.
  + SPECIFIED\_TIME- The information exists in the container until the time you specify arrives or you remove it, or the container it belongs to is removed.
  + ONCE\_TIME - The information will be removed from the container once you get or remove it, or the container it belongs to is removed.
* InfoLifeCycleType
    
   It is used to specify the life cycle type of the information, which can be LONG\_TIME, SPECIFIED\_TIME OR ONCE\_TIME.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683554071-Dynamic-Security-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690472343-API-Demos)
