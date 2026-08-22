---
title: "Information Bus API"
id: 1500009771081
section: "Using the Server API"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009771081-Information-Bus-API
updated_at: 2021-07-24T00:49:36Z
---

# Information Bus API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009743182-Dynamic-Security-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009770861-API-Demos)

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009743182-Dynamic-Security-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009770861-API-Demos)
