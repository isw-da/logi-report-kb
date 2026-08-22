---
title: "Information Bus API"
id: 5741386457495
section: "Working with APIs Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741386457495-Information-Bus-API
updated_at: 2022-10-31T17:15:51Z
---

# Information Bus API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741415142807-Dynamic-Security-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741407991063-API-Demos)

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741415142807-Dynamic-Security-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741407991063-API-Demos)
