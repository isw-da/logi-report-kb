---
title: "Information Bus API"
id: 1500009668661
section: "Working With APIs Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009668661-Information-Bus-API
updated_at: 2021-07-24T20:55:28Z
---

# Information Bus API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009668621-Dynamic-Security-API)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009643602-API-Demos)

# Information Bus API

The following Information Bus APIs enable you to access information container and get or put information in the container:

* **InformationBus**  
   It is used to transmit information in Logi JReport Server. It contains three kinds of information containers, global level, organization level and user level, and you can get or put information in the containers.
* **InformationBusManager**  
   It is used to get the Information Bus instance from the Information Bus Manager.
* **InformationContainer**  
   It is used to store user information of the following types:
  + **LONG\_TIME**  
     The information exists in the container until it is removed or the container it belongs to is removed.
  + **SPECIFIED\_TIME**  
     The information exists in the container until the time you specify arrives or you remove it, or the container it belongs to is removed.
  + **ONCE\_TIME**  
     The information will be removed from the container once you get or remove it, or the container it belongs to is removed.
* **InfoLifeCycleType**  
   It is used to specify the life cycle type of the information, which can be LONG\_TIME, SPECIFIED\_TIME OR ONCE\_TIME.

**Reference:** See the Logi JReport Javadoc in  `<install_root>\help\api` for detailed usages of Information Bus API.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009668621-Dynamic-Security-API)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009643602-API-Demos)
