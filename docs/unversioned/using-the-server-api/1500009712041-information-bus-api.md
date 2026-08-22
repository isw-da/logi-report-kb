---
title: "Information Bus API"
id: 1500009712041
section: "Using the Server API"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009712041-Information-Bus-API
updated_at: 2021-11-03T06:58:33Z
---

# Information Bus API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686322-Dynamic-Security-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009711921-API-Demos)

# Information Bus API

Information Bus API enables you to access information container and get or put information in the container.

* InformationBus
    
   It is used to transmit information in Logi JReport Server. It contains three kinds of information containers, global level, organization level and user level, and you can get or put information in the containers.
* InformationBusManager
    
   It is used to get the Information Bus instance from the Information Bus Manager.
* InformationContainer
    
   It is used to store user information of the following types:
  + LONG\_TIME - The information exists in the container until it is removed or the container it belongs to is removed.
  + SPECIFIED\_TIME- The information exists in the container until the time you specify arrives or you remove it, or the container it belongs to is removed.
  + ONCE\_TIME - The information will be removed from the container once you get or remove it, or the container it belongs to is removed.
* InfoLifeCycleType
    
   It is used to specify the life cycle type of the information, which can be LONG\_TIME, SPECIFIED\_TIME OR ONCE\_TIME.

Reference: See the Logi JReport Javadoc in  `<install_root>\help\api` for detailed usages of Information Bus API.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686322-Dynamic-Security-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009711921-API-Demos)
